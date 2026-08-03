---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.named_expression.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# named_expression 

FieldExpressions.named_expression(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _is_vector : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _is_complex : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → FieldExpression 
    
Start from a previously defined named expression. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Existing AEDT named-expression name. 

**is_vector**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the named expression returns a vector quantity. 

**is_complex**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the named expression returns a complex quantity. 

Returns: 
     

`FieldExpression`
    
Typed expression seeded with `NameOfExpression('<name>')`.
Examples
Reuse a named expression as a new starting point.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.named_expression("Poynting", is_vector=True).operations
["NameOfExpression('Poynting')"]

```
Copy to clipboard
# named_expression 

FieldExpressions.named_expression(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _is_vector : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _is_complex : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → FieldExpression 
    
Start from a previously defined named expression. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Existing AEDT named-expression name. 

**is_vector**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the named expression returns a vector quantity. 

**is_complex**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the named expression returns a complex quantity. 

Returns: 
     

`FieldExpression`
    
Typed expression seeded with `NameOfExpression('<name>')`.
Examples
Reuse a named expression as a new starting point.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.named_expression("Poynting", is_vector=True).operations
["NameOfExpression('Poynting')"]

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.named_expression.rst.txt)

# named_expression 

FieldExpressions.named_expression(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _is_vector : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _is_complex : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → FieldExpression 
    
Start from a previously defined named expression. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Existing AEDT named-expression name. 

**is_vector**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the named expression returns a vector quantity. 

**is_complex**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the named expression returns a complex quantity. 

Returns: 
     

`FieldExpression`
    
Typed expression seeded with `NameOfExpression('<name>')`.
Examples
Reuse a named expression as a new starting point.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.named_expression("Poynting", is_vector=True).operations
["NameOfExpression('Poynting')"]

```
Copy to clipboard