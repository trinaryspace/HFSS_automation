---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.operations.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# operations 

property ScalarReal.operations: [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Copy of the calculator operation stack this expression compiles to. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Copy of the reverse-Polish calculator entries for the expression.
Examples
Inspect the generated stack entries for a magnitude expression.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.vector("E").magnitude().operations
["Fundamental_Quantity('E')", "Operation('Mag')"]

```
Copy to clipboard
# operations 

property ScalarReal.operations: [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Copy of the calculator operation stack this expression compiles to. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Copy of the reverse-Polish calculator entries for the expression.
Examples
Inspect the generated stack entries for a magnitude expression.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.vector("E").magnitude().operations
["Fundamental_Quantity('E')", "Operation('Mag')"]

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.operations.rst.txt)

# operations 

property ScalarReal.operations: [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Copy of the calculator operation stack this expression compiles to. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Copy of the reverse-Polish calculator entries for the expression.
Examples
Inspect the generated stack entries for a magnitude expression.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.vector("E").magnitude().operations
["Fundamental_Quantity('E')", "Operation('Mag')"]

```
Copy to clipboard