---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.file_utils.check_if_path_exists.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# check_if_path_exists 

ansys.aedt.core.generic.file_utils.check_if_path_exists(_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check whether a path exists on a local or on a remote machine (for remote sessions only). 

Parameters: 
     

**path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Local or remote path to check. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when exist, `False` when fails.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import check_if_path_exists
>>> check_if_path_exists(r"C:\Projects\Motor\test.aedt")

```
Copy to clipboard
# check_if_path_exists 

ansys.aedt.core.generic.file_utils.check_if_path_exists(_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check whether a path exists on a local or on a remote machine (for remote sessions only). 

Parameters: 
     

**path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Local or remote path to check. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when exist, `False` when fails.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import check_if_path_exists
>>> check_if_path_exists(r"C:\Projects\Motor\test.aedt")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.file_utils.check_if_path_exists.rst.txt)

# check_if_path_exists 

ansys.aedt.core.generic.file_utils.check_if_path_exists(_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Check whether a path exists on a local or on a remote machine (for remote sessions only). 

Parameters: 
     

**path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Local or remote path to check. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when exist, `False` when fails.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import check_if_path_exists
>>> check_if_path_exists(r"C:\Projects\Motor\test.aedt")

```
Copy to clipboard