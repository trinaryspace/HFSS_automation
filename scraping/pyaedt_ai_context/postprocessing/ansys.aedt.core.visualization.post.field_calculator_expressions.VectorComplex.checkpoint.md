---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.checkpoint.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# checkpoint 

VectorComplex.checkpoint(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → FieldExpression 
    
Register this expression and return a single-entry reference to it.
Combining a sub-expression with itself duplicates its operations every time (for example `dot(a, a)` repeats `a`), so heavy reuse can grow the operation stack very quickly and overflow the calculator. Checkpoint the sub-expression once, then continue from the returned reference, whose operation stack is a single `NameOfExpression` entry. This mirrors the calculator’s own named-expression / `CopyToStack` mechanism. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Named-expression name. A unique one is generated when not provided. 

Returns: 
     

`FieldExpression`
    
A new expression of the same kind referencing the registered name.
Examples
Reuse a named sub-expression through a single entry.

```
>>> calc = type(
...     "Calc",
...     (),
...     {
...         "design_type": "HFSS",
...         "add_expression": staticmethod(lambda *args, **kwargs: kwargs["name"]),
...     },
... )()
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calc)
>>> ref = fx.vector("E").magnitude().checkpoint("e_mag")
>>> ref.operations
["NameOfExpression('e_mag')"]

```
Copy to clipboard
# checkpoint 

VectorComplex.checkpoint(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → FieldExpression 
    
Register this expression and return a single-entry reference to it.
Combining a sub-expression with itself duplicates its operations every time (for example `dot(a, a)` repeats `a`), so heavy reuse can grow the operation stack very quickly and overflow the calculator. Checkpoint the sub-expression once, then continue from the returned reference, whose operation stack is a single `NameOfExpression` entry. This mirrors the calculator’s own named-expression / `CopyToStack` mechanism. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Named-expression name. A unique one is generated when not provided. 

Returns: 
     

`FieldExpression`
    
A new expression of the same kind referencing the registered name.
Examples
Reuse a named sub-expression through a single entry.

```
>>> calc = type(
...     "Calc",
...     (),
...     {
...         "design_type": "HFSS",
...         "add_expression": staticmethod(lambda *args, **kwargs: kwargs["name"]),
...     },
... )()
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calc)
>>> ref = fx.vector("E").magnitude().checkpoint("e_mag")
>>> ref.operations
["NameOfExpression('e_mag')"]

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.checkpoint.rst.txt)

# checkpoint 

VectorComplex.checkpoint(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → FieldExpression 
    
Register this expression and return a single-entry reference to it.
Combining a sub-expression with itself duplicates its operations every time (for example `dot(a, a)` repeats `a`), so heavy reuse can grow the operation stack very quickly and overflow the calculator. Checkpoint the sub-expression once, then continue from the returned reference, whose operation stack is a single `NameOfExpression` entry. This mirrors the calculator’s own named-expression / `CopyToStack` mechanism. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Named-expression name. A unique one is generated when not provided. 

Returns: 
     

`FieldExpression`
    
A new expression of the same kind referencing the registered name.
Examples
Reuse a named sub-expression through a single entry.

```
>>> calc = type(
...     "Calc",
...     (),
...     {
...         "design_type": "HFSS",
...         "add_expression": staticmethod(lambda *args, **kwargs: kwargs["name"]),
...     },
... )()
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calc)
>>> ref = fx.vector("E").magnitude().checkpoint("e_mag")
>>> ref.operations
["NameOfExpression('e_mag')"]

```
Copy to clipboard