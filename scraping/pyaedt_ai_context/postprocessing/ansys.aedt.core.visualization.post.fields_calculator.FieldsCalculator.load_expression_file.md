---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.load_expression_file.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# load_expression_file 

FieldsCalculator.load_expression_file(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Load expressions from an external TOML file. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the file. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary of available expressions.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> my_toml = str(Path("my_path_to_toml") / "my_toml.toml")
>>> new_catalog = hfss.post.fields_calculator.load_expression_file(my_toml)
>>> hfss.desktop_class.release_desktop(False, False)

```
Copy to clipboard
# load_expression_file 

FieldsCalculator.load_expression_file(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Load expressions from an external TOML file. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the file. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary of available expressions.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> my_toml = str(Path("my_path_to_toml") / "my_toml.toml")
>>> new_catalog = hfss.post.fields_calculator.load_expression_file(my_toml)
>>> hfss.desktop_class.release_desktop(False, False)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.load_expression_file.rst.txt)

# load_expression_file 

FieldsCalculator.load_expression_file(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Load expressions from an external TOML file. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the file. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary of available expressions.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> my_toml = str(Path("my_path_to_toml") / "my_toml.toml")
>>> new_catalog = hfss.post.fields_calculator.load_expression_file(my_toml)
>>> hfss.desktop_class.release_desktop(False, False)

```
Copy to clipboard