---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.touchstone_parser.check_touchstone_files.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# check_touchstone_files 

ansys.aedt.core.visualization.advanced.touchstone_parser.check_touchstone_files(_input_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _passivity : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _causality : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Check passivity and causality for all Touchstone files included in the folder.
Warning
Do not execute this function with untrusted function argument, environment variables or pyaedt global settings. See the [security guide](https://aedt.docs.pyansys.com/version/stable/User_guide/security_consideration.html#ref-security-consideration) for details. 

Parameters: 
     

**input_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or :class:’pathlib.Path’, `optional` 
    
Folder path. The default is `""`. 

**passivity**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the passivity check is enabled, The default is `True`. 

**causality**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the causality check is enabled. The default is `True`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary with the SNP file name as the key and a list if the passivity and/or causality checks are enabled. The first element in the list is a str with `"passivity"` or `"causality"` as a value. The second element is a Boolean that is set to `True` when the criteria passed or `False` otherwise. The last element is a string with the log information.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import check_touchstone_files
>>> check_touchstone_files(input_dir="C:/Temp", passivity=True)

```
Copy to clipboard
# check_touchstone_files 

ansys.aedt.core.visualization.advanced.touchstone_parser.check_touchstone_files(_input_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _passivity : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _causality : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Check passivity and causality for all Touchstone files included in the folder.
Warning
Do not execute this function with untrusted function argument, environment variables or pyaedt global settings. See the [security guide](https://aedt.docs.pyansys.com/version/stable/User_guide/security_consideration.html#ref-security-consideration) for details. 

Parameters: 
     

**input_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or :class:’pathlib.Path’, `optional` 
    
Folder path. The default is `""`. 

**passivity**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the passivity check is enabled, The default is `True`. 

**causality**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the causality check is enabled. The default is `True`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary with the SNP file name as the key and a list if the passivity and/or causality checks are enabled. The first element in the list is a str with `"passivity"` or `"causality"` as a value. The second element is a Boolean that is set to `True` when the criteria passed or `False` otherwise. The last element is a string with the log information.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import check_touchstone_files
>>> check_touchstone_files(input_dir="C:/Temp", passivity=True)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.touchstone_parser.check_touchstone_files.rst.txt)

# check_touchstone_files 

ansys.aedt.core.visualization.advanced.touchstone_parser.check_touchstone_files(_input_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _passivity : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _causality : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Check passivity and causality for all Touchstone files included in the folder.
Warning
Do not execute this function with untrusted function argument, environment variables or pyaedt global settings. See the [security guide](https://aedt.docs.pyansys.com/version/stable/User_guide/security_consideration.html#ref-security-consideration) for details. 

Parameters: 
     

**input_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or :class:’pathlib.Path’, `optional` 
    
Folder path. The default is `""`. 

**passivity**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the passivity check is enabled, The default is `True`. 

**causality**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the causality check is enabled. The default is `True`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary with the SNP file name as the key and a list if the passivity and/or causality checks are enabled. The first element in the list is a str with `"passivity"` or `"causality"` as a value. The second element is a Boolean that is set to `True` when the criteria passed or `False` otherwise. The last element is a string with the log information.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import check_touchstone_files
>>> check_touchstone_files(input_dir="C:/Temp", passivity=True)

```
Copy to clipboard