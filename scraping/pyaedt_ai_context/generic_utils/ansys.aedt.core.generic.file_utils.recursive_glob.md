---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.file_utils.recursive_glob.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# recursive_glob 

ansys.aedt.core.generic.file_utils.recursive_glob(_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _file_pattern : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) 
    
Get a list of files matching a pattern, searching recursively from a start path. 

Parameters: 
     

**path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Starting path. 

**file_pattern**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
File pattern to match. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of files matching the given pattern.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import recursive_glob
>>> recursive_glob(r"C:\Temp\Projects", "*.aedt")

```
Copy to clipboard
# recursive_glob 

ansys.aedt.core.generic.file_utils.recursive_glob(_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _file_pattern : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) 
    
Get a list of files matching a pattern, searching recursively from a start path. 

Parameters: 
     

**path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Starting path. 

**file_pattern**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
File pattern to match. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of files matching the given pattern.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import recursive_glob
>>> recursive_glob(r"C:\Temp\Projects", "*.aedt")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.file_utils.recursive_glob.rst.txt)

# recursive_glob 

ansys.aedt.core.generic.file_utils.recursive_glob(_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _file_pattern : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) 
    
Get a list of files matching a pattern, searching recursively from a start path. 

Parameters: 
     

**path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Starting path. 

**file_pattern**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
File pattern to match. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of files matching the given pattern.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import recursive_glob
>>> recursive_glob(r"C:\Temp\Projects", "*.aedt")

```
Copy to clipboard