---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.release_desktop.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# release_desktop 

Desktop.release_desktop(_close_projects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _close_on_exit : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Release AEDT. 

Parameters: 
     

**close_projects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to close the AEDT projects that are open in the session. The default is `True`. 

**close_on_exit**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to close the active AEDT session on exiting AEDT. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> import ansys.aedt.core
>>> desktop = ansys.aedt.core.Desktop("2026.1")
PyAEDT INFO: pyaedt v...
PyAEDT INFO: Python version ...
>>> desktop.release_desktop(close_projects=False)

```
Copy to clipboard
# release_desktop 

Desktop.release_desktop(_close_projects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _close_on_exit : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Release AEDT. 

Parameters: 
     

**close_projects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to close the AEDT projects that are open in the session. The default is `True`. 

**close_on_exit**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to close the active AEDT session on exiting AEDT. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> import ansys.aedt.core
>>> desktop = ansys.aedt.core.Desktop("2026.1")
PyAEDT INFO: pyaedt v...
PyAEDT INFO: Python version ...
>>> desktop.release_desktop(close_projects=False)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.desktop.Desktop.release_desktop.rst.txt)

# release_desktop 

Desktop.release_desktop(_close_projects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _close_on_exit : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Release AEDT. 

Parameters: 
     

**close_projects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to close the AEDT projects that are open in the session. The default is `True`. 

**close_on_exit**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to close the active AEDT session on exiting AEDT. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> import ansys.aedt.core
>>> desktop = ansys.aedt.core.Desktop("2026.1")
PyAEDT INFO: pyaedt v...
PyAEDT INFO: Python version ...
>>> desktop.release_desktop(close_projects=False)

```
Copy to clipboard