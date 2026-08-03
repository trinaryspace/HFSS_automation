---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.delete_expression.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# delete_expression 

FieldsCalculator.delete_expression(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete a named expression. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the named expression. The default is `None`, in which case all named expressions are deleted. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> poly = hfss.modeler.create_polyline([[0, 0, 0], [1, 0, 1]], name="Polyline1")
>>> expr_name = hfss.post.fields_calculator.add_expression("voltage_line", "Polyline1")
>>> hfss.post.fields_calculator.delete_expression(expr_name)
>>> hfss.desktop_class.release_desktop(False, False)

```
Copy to clipboard
# delete_expression 

FieldsCalculator.delete_expression(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete a named expression. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the named expression. The default is `None`, in which case all named expressions are deleted. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> poly = hfss.modeler.create_polyline([[0, 0, 0], [1, 0, 1]], name="Polyline1")
>>> expr_name = hfss.post.fields_calculator.add_expression("voltage_line", "Polyline1")
>>> hfss.post.fields_calculator.delete_expression(expr_name)
>>> hfss.desktop_class.release_desktop(False, False)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.delete_expression.rst.txt)

# delete_expression 

FieldsCalculator.delete_expression(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Delete a named expression. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the named expression. The default is `None`, in which case all named expressions are deleted. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> poly = hfss.modeler.create_polyline([[0, 0, 0], [1, 0, 1]], name="Polyline1")
>>> expr_name = hfss.post.fields_calculator.add_expression("voltage_line", "Polyline1")
>>> hfss.post.fields_calculator.delete_expression(expr_name)
>>> hfss.desktop_class.release_desktop(False, False)

```
Copy to clipboard