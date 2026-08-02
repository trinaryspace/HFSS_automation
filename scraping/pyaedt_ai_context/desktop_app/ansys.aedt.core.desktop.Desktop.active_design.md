---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.active_design.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# active_design 

Desktop.active_design(_project_object : [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _design_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Get the active design. 

Parameters: 
     

**project_object**`optional` 
    
AEDT project object. The default is `None`, in which case the active project is used. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the design to make active. The default is `None`, in which case the active design is returned. 

**design_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the active design to make active. The default is `None`, in which case the active design is returned.
References

```
>>> oProject.GetActiveDesign
>>> oProject.SetActiveDesign

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Desktop
>>> desktop = Desktop(version="2026.1")
>>> project = desktop.active_project()
>>> desktop.active_design(project)

```
Copy to clipboard
# active_design 

Desktop.active_design(_project_object : [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _design_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Get the active design. 

Parameters: 
     

**project_object**`optional` 
    
AEDT project object. The default is `None`, in which case the active project is used. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the design to make active. The default is `None`, in which case the active design is returned. 

**design_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the active design to make active. The default is `None`, in which case the active design is returned.
References

```
>>> oProject.GetActiveDesign
>>> oProject.SetActiveDesign

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Desktop
>>> desktop = Desktop(version="2026.1")
>>> project = desktop.active_project()
>>> desktop.active_design(project)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.desktop.Desktop.active_design.rst.txt)

# active_design 

Desktop.active_design(_project_object : [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _design_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Get the active design. 

Parameters: 
     

**project_object**`optional` 
    
AEDT project object. The default is `None`, in which case the active project is used. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the design to make active. The default is `None`, in which case the active design is returned. 

**design_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the active design to make active. The default is `None`, in which case the active design is returned.
References

```
>>> oProject.GetActiveDesign
>>> oProject.SetActiveDesign

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Desktop
>>> desktop = Desktop(version="2026.1")
>>> project = desktop.active_project()
>>> desktop.active_design(project)

```
Copy to clipboard