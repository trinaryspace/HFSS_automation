---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.export.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# export 

ScalarReal.export(_output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _** kwargs_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Register and export this expression to a field file.
Extra keyword arguments are forwarded to `FieldsCalculator.export`(``solution`()`, `sample_points`, `grid_type`, `intrinsics` …). `is_vector` is set automatically. 

Parameters: 
     

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path and name to save the file to. The default is `None`, in which case the file is exported to the working directory. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Solution name, for example `"Setup1 : LastAdaptive"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
The path to the exported field file when successful, `False` when failed.
Examples
Export a field quantity through the bound calculator.

```
>>> calc = type(
...     "Calc",
...     (),
...     {
...         "design_type": "HFSS",
...         "add_expression": staticmethod(lambda *args, **kwargs: kwargs["name"]),
...         "export": staticmethod(lambda **kwargs: kwargs["output_file"]),
...     },
... )()
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calc)
>>> fx.vector("E").export("out.fld", name="vec_e")
'out.fld'

```
Copy to clipboard
# export 

ScalarReal.export(_output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _** kwargs_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Register and export this expression to a field file.
Extra keyword arguments are forwarded to `FieldsCalculator.export`(``solution`()`, `sample_points`, `grid_type`, `intrinsics` …). `is_vector` is set automatically. 

Parameters: 
     

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path and name to save the file to. The default is `None`, in which case the file is exported to the working directory. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Solution name, for example `"Setup1 : LastAdaptive"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
The path to the exported field file when successful, `False` when failed.
Examples
Export a field quantity through the bound calculator.

```
>>> calc = type(
...     "Calc",
...     (),
...     {
...         "design_type": "HFSS",
...         "add_expression": staticmethod(lambda *args, **kwargs: kwargs["name"]),
...         "export": staticmethod(lambda **kwargs: kwargs["output_file"]),
...     },
... )()
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calc)
>>> fx.vector("E").export("out.fld", name="vec_e")
'out.fld'

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.export.rst.txt)

# export 

ScalarReal.export(_output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _** kwargs_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Register and export this expression to a field file.
Extra keyword arguments are forwarded to `FieldsCalculator.export`(``solution`()`, `sample_points`, `grid_type`, `intrinsics` …). `is_vector` is set automatically. 

Parameters: 
     

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path and name to save the file to. The default is `None`, in which case the file is exported to the working directory. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Solution name, for example `"Setup1 : LastAdaptive"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
The path to the exported field file when successful, `False` when failed.
Examples
Export a field quantity through the bound calculator.

```
>>> calc = type(
...     "Calc",
...     (),
...     {
...         "design_type": "HFSS",
...         "add_expression": staticmethod(lambda *args, **kwargs: kwargs["name"]),
...         "export": staticmethod(lambda **kwargs: kwargs["output_file"]),
...     },
... )()
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calc)
>>> fx.vector("E").export("out.fld", name="vec_e")
'out.fld'

```
Copy to clipboard