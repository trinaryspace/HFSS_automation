---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.evaluate.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# evaluate 

VectorReal.evaluate(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _intrinsics : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _assignment =None_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Register and evaluate this expression to a single value. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Named-expression name. A unique one is generated when not provided. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Solution name, for example `"Setup1 : LastAdaptive"`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables (`Freq` / `Time` / `Phase`). 

**assignment**`optional` 
    
Forwarded to [`add()`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.add.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.add "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.add"). 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
The evaluated value.
Examples
Register an expression and forward evaluation to the calculator.

```
>>> calc = type(
...     "Calc",
...     (),
...     {
...         "design_type": "HFSS",
...         "add_expression": staticmethod(lambda *args, **kwargs: kwargs["name"]),
...         "evaluate": staticmethod(lambda *args, **kwargs: 3.14),
...     },
... )()
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calc)
>>> fx.vector("E").magnitude().evaluate(name="e_mag")
3.14

```
Copy to clipboard
# evaluate 

VectorReal.evaluate(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _intrinsics : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _assignment =None_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Register and evaluate this expression to a single value. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Named-expression name. A unique one is generated when not provided. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Solution name, for example `"Setup1 : LastAdaptive"`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables (`Freq` / `Time` / `Phase`). 

**assignment**`optional` 
    
Forwarded to [`add()`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.add.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.add "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.add"). 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
The evaluated value.
Examples
Register an expression and forward evaluation to the calculator.

```
>>> calc = type(
...     "Calc",
...     (),
...     {
...         "design_type": "HFSS",
...         "add_expression": staticmethod(lambda *args, **kwargs: kwargs["name"]),
...         "evaluate": staticmethod(lambda *args, **kwargs: 3.14),
...     },
... )()
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calc)
>>> fx.vector("E").magnitude().evaluate(name="e_mag")
3.14

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.evaluate.rst.txt)

# evaluate 

VectorReal.evaluate(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _intrinsics : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _assignment =None_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Register and evaluate this expression to a single value. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Named-expression name. A unique one is generated when not provided. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Solution name, for example `"Setup1 : LastAdaptive"`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables (`Freq` / `Time` / `Phase`). 

**assignment**`optional` 
    
Forwarded to [`add()`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.add.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.add "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.add"). 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
The evaluated value.
Examples
Register an expression and forward evaluation to the calculator.

```
>>> calc = type(
...     "Calc",
...     (),
...     {
...         "design_type": "HFSS",
...         "add_expression": staticmethod(lambda *args, **kwargs: kwargs["name"]),
...         "evaluate": staticmethod(lambda *args, **kwargs: 3.14),
...     },
... )()
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calc)
>>> fx.vector("E").magnitude().evaluate(name="e_mag")
3.14

```
Copy to clipboard