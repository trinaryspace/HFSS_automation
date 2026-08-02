---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.copy_design_from.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# copy_design_from 

Hfss3dLayout.copy_design_from(_project : [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _design : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _save_project : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _set_active_design : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Copy a design from a project into the active project. 

Parameters: 
     

**project**[`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path and name for the project containing the design to copy. The active design is maintained. 

**design**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the design to copy into the active design. If a design with this name is already present in the destination project, AEDT automatically changes the name. 

**save_project**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Save the project after the design has been copied. Default value is True. 

**set_active_design**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Set the design active after it has been copied. Default value is True. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name of the copied design name when successful or `None` when failed. Failure is generally a result of the name specified for `design_name` not existing in the project specified for `project_fullname`.
References

```
>>> oProject.CopyDesign
>>> oProject.Paste

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.copy_design_from(r"C:\temp\source_project.aedt", "HFSSDesign1")

```
Copy to clipboard
# copy_design_from 

Hfss3dLayout.copy_design_from(_project : [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _design : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _save_project : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _set_active_design : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Copy a design from a project into the active project. 

Parameters: 
     

**project**[`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path and name for the project containing the design to copy. The active design is maintained. 

**design**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the design to copy into the active design. If a design with this name is already present in the destination project, AEDT automatically changes the name. 

**save_project**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Save the project after the design has been copied. Default value is True. 

**set_active_design**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Set the design active after it has been copied. Default value is True. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name of the copied design name when successful or `None` when failed. Failure is generally a result of the name specified for `design_name` not existing in the project specified for `project_fullname`.
References

```
>>> oProject.CopyDesign
>>> oProject.Paste

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.copy_design_from(r"C:\temp\source_project.aedt", "HFSSDesign1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.copy_design_from.rst.txt)

# copy_design_from 

Hfss3dLayout.copy_design_from(_project : [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _design : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _save_project : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _set_active_design : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Copy a design from a project into the active project. 

Parameters: 
     

**project**[`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path and name for the project containing the design to copy. The active design is maintained. 

**design**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the design to copy into the active design. If a design with this name is already present in the destination project, AEDT automatically changes the name. 

**save_project**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Save the project after the design has been copied. Default value is True. 

**set_active_design**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Set the design active after it has been copied. Default value is True. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name of the copied design name when successful or `None` when failed. Failure is generally a result of the name specified for `design_name` not existing in the project specified for `project_fullname`.
References

```
>>> oProject.CopyDesign
>>> oProject.Paste

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.copy_design_from(r"C:\temp\source_project.aedt", "HFSSDesign1")

```
Copy to clipboard