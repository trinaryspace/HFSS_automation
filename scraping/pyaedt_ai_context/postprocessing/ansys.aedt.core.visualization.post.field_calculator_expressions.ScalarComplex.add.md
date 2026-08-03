---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.add.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# add 

ScalarComplex.add(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _assignment =None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Register this expression as an AEDT named expression. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the named expression to create. 

**assignment**`optional` 
    
Object assignment passed through to `FieldsCalculator.add_expression()`. Geometry referenced through [`Line`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.Line.html#ansys.aedt.core.visualization.post.field_calculator_expressions.Line "ansys.aedt.core.visualization.post.field_calculator_expressions.Line") / [`Surface`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.Surface.html#ansys.aedt.core.visualization.post.field_calculator_expressions.Surface "ansys.aedt.core.visualization.post.field_calculator_expressions.Surface") / [`Volume`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.Volume.html#ansys.aedt.core.visualization.post.field_calculator_expressions.Volume "ansys.aedt.core.visualization.post.field_calculator_expressions.Volume") is already embedded in the operation stack, so this is usually `None`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
The named-expression name when successful, `False` otherwise.
Examples
Register a compiled expression through the bound calculator.

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
>>> fx.vector("E").magnitude().add("e_mag")
'e_mag'

```
Copy to clipboard
# add 

ScalarComplex.add(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _assignment =None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Register this expression as an AEDT named expression. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the named expression to create. 

**assignment**`optional` 
    
Object assignment passed through to `FieldsCalculator.add_expression()`. Geometry referenced through [`Line`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.Line.html#ansys.aedt.core.visualization.post.field_calculator_expressions.Line "ansys.aedt.core.visualization.post.field_calculator_expressions.Line") / [`Surface`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.Surface.html#ansys.aedt.core.visualization.post.field_calculator_expressions.Surface "ansys.aedt.core.visualization.post.field_calculator_expressions.Surface") / [`Volume`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.Volume.html#ansys.aedt.core.visualization.post.field_calculator_expressions.Volume "ansys.aedt.core.visualization.post.field_calculator_expressions.Volume") is already embedded in the operation stack, so this is usually `None`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
The named-expression name when successful, `False` otherwise.
Examples
Register a compiled expression through the bound calculator.

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
>>> fx.vector("E").magnitude().add("e_mag")
'e_mag'

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.add.rst.txt)

# add 

ScalarComplex.add(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _assignment =None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Register this expression as an AEDT named expression. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the named expression to create. 

**assignment**`optional` 
    
Object assignment passed through to `FieldsCalculator.add_expression()`. Geometry referenced through [`Line`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.Line.html#ansys.aedt.core.visualization.post.field_calculator_expressions.Line "ansys.aedt.core.visualization.post.field_calculator_expressions.Line") / [`Surface`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.Surface.html#ansys.aedt.core.visualization.post.field_calculator_expressions.Surface "ansys.aedt.core.visualization.post.field_calculator_expressions.Surface") / [`Volume`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.Volume.html#ansys.aedt.core.visualization.post.field_calculator_expressions.Volume "ansys.aedt.core.visualization.post.field_calculator_expressions.Volume") is already embedded in the operation stack, so this is usually `None`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
The named-expression name when successful, `False` otherwise.
Examples
Register a compiled expression through the bound calculator.

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
>>> fx.vector("E").magnitude().add("e_mag")
'e_mag'

```
Copy to clipboard