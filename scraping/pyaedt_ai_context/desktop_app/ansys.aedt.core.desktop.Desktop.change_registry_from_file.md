---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.change_registry_from_file.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# change_registry_from_file 

Desktop.change_registry_from_file(_registry_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _make_active : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Apply desktop registry settings from an ACF file.
One way to get an ACF file is to export a configuration from the AEDT UI and then edit and reuse it. 

Parameters: 
     

**registry_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the ACF file. 

**make_active**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to set the imported configuration as active. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Desktop
>>> desktop = Desktop(version="2026.1")
>>> desktop.change_registry_from_file(registry_file=r"C:\Configs\DesktopConfig.acf")

```
Copy to clipboard
# change_registry_from_file 

Desktop.change_registry_from_file(_registry_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _make_active : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Apply desktop registry settings from an ACF file.
One way to get an ACF file is to export a configuration from the AEDT UI and then edit and reuse it. 

Parameters: 
     

**registry_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the ACF file. 

**make_active**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to set the imported configuration as active. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Desktop
>>> desktop = Desktop(version="2026.1")
>>> desktop.change_registry_from_file(registry_file=r"C:\Configs\DesktopConfig.acf")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.desktop.Desktop.change_registry_from_file.rst.txt)

# change_registry_from_file 

Desktop.change_registry_from_file(_registry_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _make_active : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Apply desktop registry settings from an ACF file.
One way to get an ACF file is to export a configuration from the AEDT UI and then edit and reuse it. 

Parameters: 
     

**registry_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the ACF file. 

**make_active**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to set the imported configuration as active. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Desktop
>>> desktop = Desktop(version="2026.1")
>>> desktop.change_registry_from_file(registry_file=r"C:\Configs\DesktopConfig.acf")

```
Copy to clipboard