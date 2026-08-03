---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.vector.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# vector 

FieldExpressions.vector(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'E'_, _is_complex : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [VectorReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal") | [VectorComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex") 
    
Start from a fundamental vector quantity. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
AEDT field quantity name, for example `"E"` or `"H"`. 

**is_complex**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the quantity should be treated as complex. The default is `True`, which matches most frequency-domain vector fields. 

Returns: 
     

[`VectorReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal") | [`VectorComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex") 
    
Typed vector expression seeded with `Fundamental_Quantity('<quantity>')`.
Examples

```
>>> fx = FieldExpressions(calculator=None)
>>> e_vector = fx.vector("E")
>>> e_mag = e_vector.magnitude()
>>> e_mag.operations
["Fundamental_Quantity('E')", "Operation('Mag')"]

```
Copy to clipboard
# vector 

FieldExpressions.vector(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'E'_, _is_complex : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [VectorReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal") | [VectorComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex") 
    
Start from a fundamental vector quantity. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
AEDT field quantity name, for example `"E"` or `"H"`. 

**is_complex**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the quantity should be treated as complex. The default is `True`, which matches most frequency-domain vector fields. 

Returns: 
     

[`VectorReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal") | [`VectorComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex") 
    
Typed vector expression seeded with `Fundamental_Quantity('<quantity>')`.
Examples

```
>>> fx = FieldExpressions(calculator=None)
>>> e_vector = fx.vector("E")
>>> e_mag = e_vector.magnitude()
>>> e_mag.operations
["Fundamental_Quantity('E')", "Operation('Mag')"]

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.vector.rst.txt)

# vector 

FieldExpressions.vector(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'E'_, _is_complex : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [VectorReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal") | [VectorComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex") 
    
Start from a fundamental vector quantity. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
AEDT field quantity name, for example `"E"` or `"H"`. 

**is_complex**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the quantity should be treated as complex. The default is `True`, which matches most frequency-domain vector fields. 

Returns: 
     

[`VectorReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal") | [`VectorComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex") 
    
Typed vector expression seeded with `Fundamental_Quantity('<quantity>')`.
Examples

```
>>> fx = FieldExpressions(calculator=None)
>>> e_vector = fx.vector("E")
>>> e_mag = e_vector.magnitude()
>>> e_mag.operations
["Fundamental_Quantity('E')", "Operation('Mag')"]

```
Copy to clipboard