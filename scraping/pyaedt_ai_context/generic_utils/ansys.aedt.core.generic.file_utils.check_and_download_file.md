---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.file_utils.check_and_download_file.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# check_and_download_file 

ansys.aedt.core.generic.file_utils.check_and_download_file(_remote_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Check if a file is remote. Download it or return the path. 

Parameters: 
     

**remote_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Path to the remote file. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to overwrite the file if it already exists locally. The default is `True`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Path to the remote file.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import check_and_download_file
>>> check_and_download_file(r"C:\Projects\Motor\meshstats.ms")

```
Copy to clipboard
# check_and_download_file 

ansys.aedt.core.generic.file_utils.check_and_download_file(_remote_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Check if a file is remote. Download it or return the path. 

Parameters: 
     

**remote_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Path to the remote file. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to overwrite the file if it already exists locally. The default is `True`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Path to the remote file.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import check_and_download_file
>>> check_and_download_file(r"C:\Projects\Motor\meshstats.ms")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.file_utils.check_and_download_file.rst.txt)

# check_and_download_file 

ansys.aedt.core.generic.file_utils.check_and_download_file(_remote_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Check if a file is remote. Download it or return the path. 

Parameters: 
     

**remote_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Path to the remote file. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to overwrite the file if it already exists locally. The default is `True`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Path to the remote file.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import check_and_download_file
>>> check_and_download_file(r"C:\Projects\Motor\meshstats.ms")

```
Copy to clipboard