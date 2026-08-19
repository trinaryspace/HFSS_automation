"""Load and dump `design.yaml`, with readable errors on a malformed spec.

Pydantic's raw `ValidationError` is a wall of text with a `loc` tuple per
problem; the compiler's diagnosis seam wants `geometry[2].size[0]` and a
sentence. This module is the translation, so every entry point — the CLI, the
validator, the compiler — reports a spec problem the same way.
"""

from __future__ import annotations

import json
from pathlib import Path

from pydantic import ValidationError

from .schema import DesignSpec
from .validate import ERROR, Finding, Report


class SpecLoadError(ValueError):
    """A spec that does not even parse into the schema."""

    def __init__(self, report: Report):
        self.report = report
        super().__init__(report.text())


def _read(path) -> dict:
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() in (".yaml", ".yml"):
        data = _unbool_keys(parse_yaml(text))
    else:
        data = json.loads(text)
    if not isinstance(data, dict):
        raise SpecLoadError(Report([Finding(
            path.name, ERROR, "a spec must be a mapping at the top level")]))
    return data


# YAML 1.1 resolves a bare `on`, `off`, `yes`, `no`, `y` or `n` to a boolean.
# That is the wrong dialect for this file format, in two ways.
#
# 1. The selector field is spelled `on:` throughout the design — natural
#    English, and what `phase-2-detail.md` specifies — so an unquoted spec used
#    to arrive with `True` for a key and fail with "Keys should be strings, got
#    True", which tells the author nothing.
#
# 2. Worse, and found 2026-08-19: **it silently renames and can silently merge
#    design variables.** A variable declared `Off:` came back as `off`, so every
#    expression referring to `Off` failed with `unknown name 'Off'` pointing at
#    the geometry rather than at the declaration. And because `On` and `Yes`
#    both resolve to True, declaring both left **one variable holding the
#    other's value** with nothing reported. `N` is the case that matters most:
#    an array spec that writes `N: 4` for its element count is not exotic, and
#    `n` is false in YAML 1.1.
#
# The fix is to read the file as YAML 1.2 core, where only `true` and `false`
# are booleans, so a key means what it says. `on:` then arrives as the string
# "on" and the selector still works unquoted. Values are unaffected in
# practice: pydantic still coerces "yes"/"on" to True for the handful of
# genuinely boolean fields (`cover`, `close`, `keep_tools`).
_YAML_12_BOOLS = "tTfF"


def _yaml_loader():
    """A SafeLoader that resolves only `true`/`false` as booleans."""
    import yaml

    class SpecLoader(yaml.SafeLoader):
        pass

    # Copy the resolver table, then drop bool for every first-character bucket
    # except the ones `true`/`false` can start with, and narrow those two.
    SpecLoader.yaml_implicit_resolvers = {
        key: [(tag, regex) for tag, regex in mappings
              if tag != "tag:yaml.org,2002:bool" or key in _YAML_12_BOOLS]
        for key, mappings in yaml.SafeLoader.yaml_implicit_resolvers.items()
    }
    import re
    strict = re.compile(r"^(?:true|True|TRUE|false|False|FALSE)$")
    for key in _YAML_12_BOOLS:
        SpecLoader.yaml_implicit_resolvers[key] = [
            (tag, strict if tag == "tag:yaml.org,2002:bool" else regex)
            for tag, regex in SpecLoader.yaml_implicit_resolvers.get(key, [])
        ]
    return SpecLoader


def parse_yaml(text: str):
    """Parse spec YAML under the 1.2 core boolean rules. The only entry point.

    Every reader of a spec goes through here so a spec cannot mean one thing to
    the validator and another to the compiler.
    """
    import yaml
    return yaml.load(text, Loader=_yaml_loader())


# Retained as a safety net for specs that arrive as a dict from somewhere other
# than `parse_yaml` — a JSON file, the reducer, a test. With the 1.2 loader in
# place it is normally a no-op.
_BOOL_KEYS = {True: "on", False: "off"}


def _unbool_keys(node):
    if isinstance(node, dict):
        return {_BOOL_KEYS.get(k, k) if isinstance(k, bool) else k: _unbool_keys(v)
                for k, v in node.items()}
    if isinstance(node, list):
        return [_unbool_keys(item) for item in node]
    return node


def spec_from_dict(data: dict) -> DesignSpec:
    """Build a DesignSpec, or raise SpecLoadError carrying a Report."""
    try:
        return DesignSpec.model_validate(data)
    except ValidationError as exc:
        raise SpecLoadError(Report(_findings(exc))) from None


def load_spec(path) -> DesignSpec:
    return spec_from_dict(_read(path))


def load_spec_text(text: str) -> DesignSpec:
    """Load a spec from a YAML string — same path as `load_spec`, no file.

    Tests that want to vary one dimension of a spec should not have to write a
    temp file to do it, and must not hand-roll the load: `_unbool_keys` is the
    reason a bare `on:` key works at all, and a test that skipped it would be
    exercising a spec shape no real file can produce.
    """
    data = _unbool_keys(parse_yaml(text))
    if not isinstance(data, dict):
        raise SpecLoadError(Report([Finding(
            "<text>", ERROR, "a spec must be a mapping at the top level")]))
    return spec_from_dict(data)


def _findings(exc: ValidationError) -> list[Finding]:
    findings = []
    for error in exc.errors():
        findings.append(Finding(
            _path(error.get("loc", ())),
            ERROR,
            error.get("msg", "invalid"),
            hint=_hint(error),
        ))
    return findings


def _path(loc) -> str:
    """Pydantic's loc tuple as `geometry[2].size[0]`.

    Union members show up as an extra tag element (`FaceOf`, `ObjectRef`);
    they are noise in a path, so they are dropped.
    """
    out = ""
    for part in loc:
        if isinstance(part, int):
            out += f"[{part}]"
        elif part in ("FaceOf", "ObjectRef", "OuterFaces", "MaterialRef",
                      "MaterialDef", "EdgeMid", "Point"):
            continue
        else:
            out = f"{out}.{part}" if out else str(part)
    return out or "<spec>"


def _hint(error: dict) -> str:
    kind = error.get("type", "")
    if kind == "extra_forbidden":
        return "unknown field — check the spelling against the schema"
    if kind == "missing":
        return "required field"
    given = error.get("input")
    if given is not None and not isinstance(given, (dict, list)):
        return f"got {given!r}"
    return ""


def dump_spec(spec: DesignSpec) -> str:
    """A spec back to YAML, round-trip stable."""
    import yaml
    data = spec.model_dump(mode="json", by_alias=True, exclude_none=True,
                           exclude_defaults=False)
    return yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100)
