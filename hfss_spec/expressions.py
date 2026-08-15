"""Expression parsing for spec variables — dimensions and cycles, not values.

Q2 settled that variables carry expressions (`sub_W: "patch_W + 6*h"`) rather
than literals, because the parametric link has to survive into AEDT's variable
table: change `patch_W` in the UI and the substrate follows. The reducer found
this pattern already live in real models (`gnd_x: subX`), so it is confirmed by
evidence rather than by argument.

The compiler passes expressions to AEDT verbatim — AEDT is the evaluator that
matters. This module exists only to answer two offline questions before a
license is ever touched:

1. **Is it dimensionally sound?** `patch_L + inset_d` is an error when one is a
   length and the other a frequency.
2. **Does it terminate?** `air_pad -> sub_W -> air_pad` is a cycle, and AEDT
   reports it as an unhelpful runtime failure long after the desktop is up.

Values are computed as a side effect and are useful for the physics pre-check,
but they are never written back into the spec: AEDT owns evaluation.

Stdlib only (`ast`); no pyAEDT import, so this runs in Tier 0.
"""

from __future__ import annotations

import ast
import math
import re
from dataclasses import dataclass

from .units import (
    CONSTANTS,
    DIMENSIONLESS,
    UNITS,
    Dimension,
    Quantity,
    UnitError,
    canonical_unit,
    parse_quantity,
)


class ExpressionError(ValueError):
    """A malformed, cyclic, or dimensionally unsound expression."""


@dataclass(frozen=True)
class Value:
    """An evaluated expression: an SI magnitude plus its dimension."""

    si: float
    dimension: Dimension

    def __str__(self) -> str:
        return f"{self.si:g} [{self.dimension}]"


# Functions callable from a spec expression. Each takes and returns plain
# floats; dimensional rules are applied by the evaluator, not by these.
FUNCTIONS = {
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "abs": abs,
    "min": min,
    "max": max,
    "log": math.log,
    "log10": math.log10,
    "exp": math.exp,
}

# Functions whose argument must be dimensionless (and whose result is too).
_DIMENSIONLESS_FUNCS = {
    "sin", "cos", "tan", "asin", "acos", "atan", "log", "log10", "exp",
}


# A number glued to a unit inside a larger expression: `patch_L + 2mm`. AEDT
# writes these routinely and they are not valid Python, so they are lifted out
# to placeholders before the AST ever sees them. The trailing (?![A-Za-z0-9_])
# keeps `2mm` from matching inside a name like `x2mmy`, and requiring a known
# unit keeps a variable called `mil` from being eaten.
_UNIT_LITERAL_RE = re.compile(
    r"(?<![A-Za-z0-9_.])(\d+\.?\d*(?:[eE][-+]?\d+)?)\s*([A-Za-z]+)(?![A-Za-z0-9_])"
)


def _lift_unit_literals(expression: str) -> tuple[str, dict[str, Value]]:
    """Replace `2mm` with a placeholder name bound to its Value."""
    extra: dict[str, Value] = {}

    def swap(match: "re.Match[str]") -> str:
        number, unit = match.group(1), match.group(2)
        try:
            canonical = canonical_unit(unit)
        except UnitError:
            return match.group(0)        # not a unit -- leave it to the parser
        quantity = Quantity(float(number), canonical)
        placeholder = f"__unit_literal_{len(extra)}"
        extra[placeholder] = Value(quantity.si, quantity.dimension)
        return placeholder

    return _UNIT_LITERAL_RE.sub(swap, expression), extra


def references(expression: str) -> set[str]:
    """Every bare name an expression mentions, functions and literals excluded."""
    if not isinstance(expression, str):
        return set()
    rewritten, _extra = _lift_unit_literals(expression)
    try:
        tree = ast.parse(rewritten, mode="eval")
    except SyntaxError:
        return set()
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            names.add(node.id)
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            names.discard(node.func.id)
    return {n for n in names
            if n not in FUNCTIONS and not n.startswith("__unit_literal_")}


def dependency_order(variables: dict[str, object]) -> list[str]:
    """Variable names in dependency order. Raises ExpressionError on a cycle.

    A cycle is reported with the ring that closes it, because
    `air_pad -> sub_W -> air_pad` is far more useful than "invalid variable".
    """
    deps = {
        name: {r for r in references(raw) if r in variables and r != name}
        for name, raw in variables.items()
    }
    ordered: list[str] = []
    state: dict[str, int] = {}          # 0 = visiting, 1 = done

    def visit(name: str, trail: list[str]) -> None:
        mark = state.get(name)
        if mark == 1:
            return
        if mark == 0:
            ring = trail[trail.index(name):] + [name]
            raise ExpressionError("cycle: " + " -> ".join(ring))
        state[name] = 0
        for dep in sorted(deps[name]):
            visit(dep, trail + [name])
        state[name] = 1
        ordered.append(name)

    for name in variables:
        visit(name, [])
    return ordered


def evaluate(expression, scope: dict[str, Value]) -> Value:
    """Evaluate one expression against already-resolved variables.

    `scope` maps variable names to Values. Literals with units short-circuit,
    so `1.6mm` never reaches the AST walker (`1.6mm` is not Python anyway).
    """
    if not isinstance(expression, str):
        quantity = parse_quantity(expression)
        return Value(quantity.si, quantity.dimension)
    try:
        quantity = parse_quantity(expression)
    except UnitError:
        pass
    else:
        return Value(quantity.si, quantity.dimension)

    rewritten, literals = _lift_unit_literals(expression)
    try:
        tree = ast.parse(rewritten, mode="eval")
    except SyntaxError as exc:
        raise ExpressionError(f"{expression!r} is not a valid expression: {exc.msg}")
    return _eval_node(tree.body, {**scope, **literals}, expression)


def resolve_all(variables: dict[str, object]) -> dict[str, Value]:
    """Resolve a whole variable table in dependency order."""
    scope: dict[str, Value] = {}
    for name in dependency_order(variables):
        try:
            scope[name] = evaluate(variables[name], scope)
        except ExpressionError as exc:
            raise ExpressionError(f"variables.{name}: {exc}") from None
    return scope


def _eval_node(node, scope: dict[str, Value], source: str) -> Value:
    if isinstance(node, ast.Constant):
        if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
            raise ExpressionError(f"{source!r}: {node.value!r} is not a number")
        return Value(float(node.value), DIMENSIONLESS)

    if isinstance(node, ast.Name):
        if node.id in scope:
            return scope[node.id]
        if node.id in CONSTANTS:
            si, dimension = CONSTANTS[node.id]
            return Value(si, dimension)
        raise ExpressionError(f"{source!r}: unknown name {node.id!r}")

    if isinstance(node, ast.UnaryOp):
        operand = _eval_node(node.operand, scope, source)
        if isinstance(node.op, ast.USub):
            return Value(-operand.si, operand.dimension)
        if isinstance(node.op, ast.UAdd):
            return operand
        raise ExpressionError(f"{source!r}: unsupported unary operator")

    if isinstance(node, ast.BinOp):
        left = _eval_node(node.left, scope, source)
        right = _eval_node(node.right, scope, source)
        op = node.op
        if isinstance(op, (ast.Add, ast.Sub)):
            if left.dimension != right.dimension:
                raise ExpressionError(
                    f"{source!r}: cannot {'add' if isinstance(op, ast.Add) else 'subtract'} "
                    f"{left.dimension} and {right.dimension}"
                )
            si = left.si + right.si if isinstance(op, ast.Add) else left.si - right.si
            return Value(si, left.dimension)
        if isinstance(op, ast.Mult):
            return Value(left.si * right.si, left.dimension * right.dimension)
        if isinstance(op, ast.Div):
            if right.si == 0:
                raise ExpressionError(f"{source!r}: division by zero")
            return Value(left.si / right.si, left.dimension / right.dimension)
        if isinstance(op, ast.Pow):
            if not right.dimension.dimensionless:
                raise ExpressionError(f"{source!r}: exponent must be dimensionless")
            exponent = right.si
            if not left.dimension.dimensionless and exponent != int(exponent):
                raise ExpressionError(
                    f"{source!r}: cannot raise {left.dimension} to a fractional power"
                )
            return Value(left.si ** exponent, left.dimension ** int(exponent))
        raise ExpressionError(f"{source!r}: unsupported operator {type(op).__name__}")

    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name) or node.func.id not in FUNCTIONS:
            name = getattr(node.func, "id", "?")
            raise ExpressionError(f"{source!r}: unknown function {name!r}")
        name = node.func.id
        args = [_eval_node(a, scope, source) for a in node.args]
        if node.keywords:
            raise ExpressionError(f"{source!r}: {name}() takes no keyword arguments")
        if name in _DIMENSIONLESS_FUNCS:
            for arg in args:
                if not arg.dimension.dimensionless:
                    raise ExpressionError(
                        f"{source!r}: {name}() needs a dimensionless argument, "
                        f"got {arg.dimension}"
                    )
            return Value(FUNCTIONS[name](*(a.si for a in args)), DIMENSIONLESS)
        if name == "sqrt":
            arg = args[0]
            half = Dimension(*(getattr(arg.dimension, b) // 2 for b in
                               ("length", "time", "resistance", "angle")))
            if half * half != arg.dimension:
                raise ExpressionError(
                    f"{source!r}: sqrt() of {arg.dimension} is not a whole dimension"
                )
            return Value(math.sqrt(arg.si), half)
        # abs / min / max preserve their (single, shared) dimension.
        dimensions = {a.dimension for a in args}
        if len(dimensions) > 1:
            raise ExpressionError(f"{source!r}: {name}() mixes {', '.join(map(str, dimensions))}")
        return Value(FUNCTIONS[name](*(a.si for a in args)), args[0].dimension)

    raise ExpressionError(f"{source!r}: unsupported syntax {type(node).__name__}")


def as_quantity(value: Value, unit: str) -> Quantity:
    """A resolved Value back into a unit, for display. Raises UnitError on mismatch."""
    unit = canonical_unit(unit)
    if not unit:
        if not value.dimension.dimensionless:
            raise UnitError(f"{value} is not dimensionless")
        return Quantity(value.si, "")
    scale, dimension = UNITS[unit]
    if dimension != value.dimension:
        raise UnitError(f"{value} cannot be expressed in {unit} ({dimension})")
    return Quantity(value.si / scale, unit)
