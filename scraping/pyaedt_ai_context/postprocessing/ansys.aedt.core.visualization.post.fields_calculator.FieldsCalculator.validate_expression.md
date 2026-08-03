---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.validate_expression.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# validate_expression 

FieldsCalculator.validate_expression(_expression : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Validate expression file against the schema.
The default schema can be found in `src/ansys/aedt/core/misc/config.schema.json`. 

Parameters: 
     

**expression**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Expression defined as a dictionary. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Expression if the input expression is valid, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.visualization.post.fields_calculator import FieldsCalculator
>>> obj = FieldsCalculator()
>>> obj.validate_expression(expression="dB(S(1,1))")

```
Copy to clipboard
# validate_expression 

FieldsCalculator.validate_expression(_expression : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Validate expression file against the schema.
The default schema can be found in `src/ansys/aedt/core/misc/config.schema.json`. 

Parameters: 
     

**expression**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Expression defined as a dictionary. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Expression if the input expression is valid, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.visualization.post.fields_calculator import FieldsCalculator
>>> obj = FieldsCalculator()
>>> obj.validate_expression(expression="dB(S(1,1))")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.validate_expression.rst.txt)

# validate_expression 

FieldsCalculator.validate_expression(_expression : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Validate expression file against the schema.
The default schema can be found in `src/ansys/aedt/core/misc/config.schema.json`. 

Parameters: 
     

**expression**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Expression defined as a dictionary. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Expression if the input expression is valid, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.visualization.post.fields_calculator import FieldsCalculator
>>> obj = FieldsCalculator()
>>> obj.validate_expression(expression="dB(S(1,1))")

```
Copy to clipboard