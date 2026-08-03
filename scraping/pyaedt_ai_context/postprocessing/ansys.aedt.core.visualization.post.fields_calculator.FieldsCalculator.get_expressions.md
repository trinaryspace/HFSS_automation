---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.get_expressions.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# get_expressions 

FieldsCalculator.get_expressions(_field_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Get dictionary of available Field Calculator expressions. 

Parameters: 
     

**field_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Field type. Options are `"Fields"` or `"Time Averaged Fields"`. The default is `None`, in which case all expressions are returned. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Field Calculator expressions. Where key is the named expression and value is the expression string.
References

```
>>> oModule.GetFieldsCalculatorExpressions

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.fields_calculator import FieldsCalculator
>>> obj = FieldsCalculator()
>>> obj.get_expressions(field_type=1)

```
Copy to clipboard
# get_expressions 

FieldsCalculator.get_expressions(_field_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Get dictionary of available Field Calculator expressions. 

Parameters: 
     

**field_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Field type. Options are `"Fields"` or `"Time Averaged Fields"`. The default is `None`, in which case all expressions are returned. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Field Calculator expressions. Where key is the named expression and value is the expression string.
References

```
>>> oModule.GetFieldsCalculatorExpressions

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.fields_calculator import FieldsCalculator
>>> obj = FieldsCalculator()
>>> obj.get_expressions(field_type=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.get_expressions.rst.txt)

# get_expressions 

FieldsCalculator.get_expressions(_field_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Get dictionary of available Field Calculator expressions. 

Parameters: 
     

**field_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Field type. Options are `"Fields"` or `"Time Averaged Fields"`. The default is `None`, in which case all expressions are returned. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Field Calculator expressions. Where key is the named expression and value is the expression string.
References

```
>>> oModule.GetFieldsCalculatorExpressions

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.fields_calculator import FieldsCalculator
>>> obj = FieldsCalculator()
>>> obj.get_expressions(field_type=1)

```
Copy to clipboard