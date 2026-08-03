---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.file_utils.open_file.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# open_file 

ansys.aedt.core.generic.file_utils.open_file(_file_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _file_options : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'r'_, _encoding : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _override_existing : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [TextIO](https://docs.python.org/3.11/library/typing.html#typing.TextIO "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Open a file and return the object. 

Parameters: 
     

**file_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full absolute path to the file (either local or remote). 

**file_options**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Options for opening the file. 

**encoding**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the encoding used to decode or encode the file. The default is `None`, which means a platform-dependent encoding is used. You can specify any encoding supported by Python. 

**override_existing**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to override an existing file if opening a file in write mode on a remote machine. The default is `True`. 

Returns: 
     

`Union`[`TextIO`, [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)")]
    
Opened file object or `None` if the file or folder does not exist.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import open_file
>>> with open_file(r"C:\Temp\notes.txt", "w") as file_obj:
...     _ = file_obj.write("PyAEDT")

```
Copy to clipboard
# open_file 

ansys.aedt.core.generic.file_utils.open_file(_file_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _file_options : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'r'_, _encoding : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _override_existing : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [TextIO](https://docs.python.org/3.11/library/typing.html#typing.TextIO "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Open a file and return the object. 

Parameters: 
     

**file_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full absolute path to the file (either local or remote). 

**file_options**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Options for opening the file. 

**encoding**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the encoding used to decode or encode the file. The default is `None`, which means a platform-dependent encoding is used. You can specify any encoding supported by Python. 

**override_existing**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to override an existing file if opening a file in write mode on a remote machine. The default is `True`. 

Returns: 
     

`Union`[`TextIO`, [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)")]
    
Opened file object or `None` if the file or folder does not exist.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import open_file
>>> with open_file(r"C:\Temp\notes.txt", "w") as file_obj:
...     _ = file_obj.write("PyAEDT")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.file_utils.open_file.rst.txt)

# open_file 

ansys.aedt.core.generic.file_utils.open_file(_file_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _file_options : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'r'_, _encoding : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _override_existing : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [TextIO](https://docs.python.org/3.11/library/typing.html#typing.TextIO "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Open a file and return the object. 

Parameters: 
     

**file_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full absolute path to the file (either local or remote). 

**file_options**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Options for opening the file. 

**encoding**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the encoding used to decode or encode the file. The default is `None`, which means a platform-dependent encoding is used. You can specify any encoding supported by Python. 

**override_existing**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to override an existing file if opening a file in write mode on a remote machine. The default is `True`. 

Returns: 
     

`Union`[`TextIO`, [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)")]
    
Opened file object or `None` if the file or folder does not exist.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import open_file
>>> with open_file(r"C:\Temp\notes.txt", "w") as file_obj:
...     _ = file_obj.write("PyAEDT")

```
Copy to clipboard