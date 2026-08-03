---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.file_utils.check_and_download_folder.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# check_and_download_folder 

ansys.aedt.core.generic.file_utils.check_and_download_folder(_local_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _remote_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Download remote folder. 

Parameters: 
     

**local_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Local path to save the folder to. 

**remote_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Path to the remote folder. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to overwrite the folder if it already exists locally. The default is `True`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Path to the local folder if downloaded, otherwise the remote path.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import check_and_download_folder
>>> check_and_download_folder(r"C:\Projects\LocalCopy", r"C:\Projects\RemoteCopy")

```
Copy to clipboard
# check_and_download_folder 

ansys.aedt.core.generic.file_utils.check_and_download_folder(_local_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _remote_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Download remote folder. 

Parameters: 
     

**local_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Local path to save the folder to. 

**remote_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Path to the remote folder. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to overwrite the folder if it already exists locally. The default is `True`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Path to the local folder if downloaded, otherwise the remote path.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import check_and_download_folder
>>> check_and_download_folder(r"C:\Projects\LocalCopy", r"C:\Projects\RemoteCopy")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.file_utils.check_and_download_folder.rst.txt)

# check_and_download_folder 

ansys.aedt.core.generic.file_utils.check_and_download_folder(_local_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _remote_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Download remote folder. 

Parameters: 
     

**local_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Local path to save the folder to. 

**remote_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Path to the remote folder. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to overwrite the folder if it already exists locally. The default is `True`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Path to the local folder if downloaded, otherwise the remote path.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import check_and_download_folder
>>> check_and_download_folder(r"C:\Projects\LocalCopy", r"C:\Projects\RemoteCopy")

```
Copy to clipboard