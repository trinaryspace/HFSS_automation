---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.file_utils.write_configuration_file.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# write_configuration_file 

ansys.aedt.core.generic.file_utils.write_configuration_file(_input_data : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a configuration file in JSON or TOML format from a dictionary. 

Parameters: 
     

**input_data**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary to write the file to. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to the file, including its extension. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import write_configuration_file
>>> write_configuration_file({"units": "mm"}, r"C:\Temp\settings.json")

```
Copy to clipboard
# write_configuration_file 

ansys.aedt.core.generic.file_utils.write_configuration_file(_input_data : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a configuration file in JSON or TOML format from a dictionary. 

Parameters: 
     

**input_data**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary to write the file to. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to the file, including its extension. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import write_configuration_file
>>> write_configuration_file({"units": "mm"}, r"C:\Temp\settings.json")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.file_utils.write_configuration_file.rst.txt)

# write_configuration_file 

ansys.aedt.core.generic.file_utils.write_configuration_file(_input_data : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a configuration file in JSON or TOML format from a dictionary. 

Parameters: 
     

**input_data**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary to write the file to. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to the file, including its extension. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import write_configuration_file
>>> write_configuration_file({"units": "mm"}, r"C:\Temp\settings.json")

```
Copy to clipboard