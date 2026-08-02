---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_perfecte_to_sheets.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# assign_perfecte_to_sheets 

Hfss.assign_perfecte_to_sheets(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_infinite_ground : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Create a Perfect E taking one sheet. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more names of the sheets to apply the boundary to. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the Perfect E source. The default is `None`. 

**is_infinite_ground**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the Perfect E is an infinite ground. The default is `False`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignPerfectE

```
Copy to clipboard
Examples
Create a sheet and use it to create a Perfect E. >>> from ansys.aedt.core.generic.constants import Plane >>> >>> sheet = hfss.modeler.create_rectangle( … Plane.XY, [0, 0, -90], [10, 2], name=”PerfectESheet”, material=”Copper” … ) >>> perfect_e_from_sheet = hfss.assign_perfecte_to_sheets(sheet.name, “PerfectEFromSheet”) >>> type(perfect_e_from_sheet) <class ‘from ansys.aedt.core.modules.boundary.common.BoundaryObject’>
# assign_perfecte_to_sheets 

Hfss.assign_perfecte_to_sheets(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_infinite_ground : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Create a Perfect E taking one sheet. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more names of the sheets to apply the boundary to. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the Perfect E source. The default is `None`. 

**is_infinite_ground**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the Perfect E is an infinite ground. The default is `False`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignPerfectE

```
Copy to clipboard
Examples
Create a sheet and use it to create a Perfect E. >>> from ansys.aedt.core.generic.constants import Plane >>> >>> sheet = hfss.modeler.create_rectangle( … Plane.XY, [0, 0, -90], [10, 2], name=”PerfectESheet”, material=”Copper” … ) >>> perfect_e_from_sheet = hfss.assign_perfecte_to_sheets(sheet.name, “PerfectEFromSheet”) >>> type(perfect_e_from_sheet) <class ‘from ansys.aedt.core.modules.boundary.common.BoundaryObject’>
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_perfecte_to_sheets.rst.txt)

# assign_perfecte_to_sheets 

Hfss.assign_perfecte_to_sheets(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_infinite_ground : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Create a Perfect E taking one sheet. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more names of the sheets to apply the boundary to. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the Perfect E source. The default is `None`. 

**is_infinite_ground**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the Perfect E is an infinite ground. The default is `False`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignPerfectE

```
Copy to clipboard
Examples
Create a sheet and use it to create a Perfect E. >>> from ansys.aedt.core.generic.constants import Plane >>> >>> sheet = hfss.modeler.create_rectangle( … Plane.XY, [0, 0, -90], [10, 2], name=”PerfectESheet”, material=”Copper” … ) >>> perfect_e_from_sheet = hfss.assign_perfecte_to_sheets(sheet.name, “PerfectEFromSheet”) >>> type(perfect_e_from_sheet) <class ‘from ansys.aedt.core.modules.boundary.common.BoundaryObject’>