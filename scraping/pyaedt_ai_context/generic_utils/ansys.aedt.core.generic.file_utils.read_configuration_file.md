---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.file_utils.read_configuration_file.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# read_configuration_file 

ansys.aedt.core.generic.file_utils.read_configuration_file(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Parse a file and return the information in a list or dictionary. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to the file. Supported formats are `"csv"`, `"json"`, `"tab"`, `"toml"`, and `"xlsx"`. 

Returns: 
     

`Union`[`Dict`, `List`]
    
Dictionary if configuration file is `"toml"` or `"json"`, List is `"csv"`, `"tab"` or `"xlsx"`.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import read_configuration_file
>>> read_configuration_file(r"C:\Temp\settings.json")

```
Copy to clipboard
# read_configuration_file 

ansys.aedt.core.generic.file_utils.read_configuration_file(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Parse a file and return the information in a list or dictionary. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to the file. Supported formats are `"csv"`, `"json"`, `"tab"`, `"toml"`, and `"xlsx"`. 

Returns: 
     

`Union`[`Dict`, `List`]
    
Dictionary if configuration file is `"toml"` or `"json"`, List is `"csv"`, `"tab"` or `"xlsx"`.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import read_configuration_file
>>> read_configuration_file(r"C:\Temp\settings.json")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.file_utils.read_configuration_file.rst.txt)

# read_configuration_file 

ansys.aedt.core.generic.file_utils.read_configuration_file(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Parse a file and return the information in a list or dictionary. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to the file. Supported formats are `"csv"`, `"json"`, `"tab"`, `"toml"`, and `"xlsx"`. 

Returns: 
     

`Union`[`Dict`, `List`]
    
Dictionary if configuration file is `"toml"` or `"json"`, List is `"csv"`, `"tab"` or `"xlsx"`.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import read_configuration_file
>>> read_configuration_file(r"C:\Temp\settings.json")

```
Copy to clipboard