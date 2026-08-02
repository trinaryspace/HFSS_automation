---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_perfecth_to_sheets.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# assign_perfecth_to_sheets 

Hfss.assign_perfecth_to_sheets(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Assign a Perfect H to sheets. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of sheets to apply the boundary to. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Perfect H name. The default is `None`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignPerfectH

```
Copy to clipboard
Examples
Create a sheet and use it to create a Perfect H.

```
>>> from ansys.aedt.core.generic.constants import Plane
>>> sheet = hfss.modeler.create_rectangle(
...     Plane.XY, [0, 0, -90], [10, 2], name="PerfectHSheet", material="Copper"
... )
>>> perfect_h_from_sheet = hfss.assign_perfecth_to_sheets(sheet.name, "PerfectHFromSheet")
>>> type(perfect_h_from_sheet)
<class 'from ansys.aedt.core.modules.boundary.common.BoundaryObject'>

```
Copy to clipboard
# assign_perfecth_to_sheets 

Hfss.assign_perfecth_to_sheets(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Assign a Perfect H to sheets. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of sheets to apply the boundary to. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Perfect H name. The default is `None`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignPerfectH

```
Copy to clipboard
Examples
Create a sheet and use it to create a Perfect H.

```
>>> from ansys.aedt.core.generic.constants import Plane
>>> sheet = hfss.modeler.create_rectangle(
...     Plane.XY, [0, 0, -90], [10, 2], name="PerfectHSheet", material="Copper"
... )
>>> perfect_h_from_sheet = hfss.assign_perfecth_to_sheets(sheet.name, "PerfectHFromSheet")
>>> type(perfect_h_from_sheet)
<class 'from ansys.aedt.core.modules.boundary.common.BoundaryObject'>

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_perfecth_to_sheets.rst.txt)

# assign_perfecth_to_sheets 

Hfss.assign_perfecth_to_sheets(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Assign a Perfect H to sheets. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of sheets to apply the boundary to. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Perfect H name. The default is `None`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignPerfectH

```
Copy to clipboard
Examples
Create a sheet and use it to create a Perfect H.

```
>>> from ansys.aedt.core.generic.constants import Plane
>>> sheet = hfss.modeler.create_rectangle(
...     Plane.XY, [0, 0, -90], [10, 2], name="PerfectHSheet", material="Copper"
... )
>>> perfect_h_from_sheet = hfss.assign_perfecth_to_sheets(sheet.name, "PerfectHFromSheet")
>>> type(perfect_h_from_sheet)
<class 'from ansys.aedt.core.modules.boundary.common.BoundaryObject'>

```
Copy to clipboard