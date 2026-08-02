---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_current_source_to_sheet.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# assign_current_source_to_sheet 

Hfss.assign_current_source_to_sheet(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _start_direction : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [Gravity](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Gravity "ansys.aedt.core.generic.constants.Gravity") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Create a current source taking one sheet. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the sheet to apply the boundary to. 

**start_direction**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `ansys.aedt.core.application.analysis.Analysis.axis_directions` or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Direction of the integration line. It should be one of the values for `Application.axis_directions`, which are: `XNeg`, `YNeg`, `ZNeg`, `XPos`, `YPos`, and `ZPos`. It also accepts the list of the start point and end point with the format [[xstart, ystart, zstart], [xend, yend, zend]] The default is `Application.axis_directions.XNeg`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the source. The default is `None`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignCurrent

```
Copy to clipboard
Examples
Create a sheet and assign some current to it.

```
>>> from ansys.aedt.core.generic.constants import Plane
>>> sheet = hfss.modeler.create_rectangle(Plane.XY, [0, 0, -50], [5, 1], name="CurrentSheet", material="copper")
>>> hfss.assign_current_source_to_sheet(sheet.name, hfss.axis_directions.XNeg, "CurrentSheetExample")
'CurrentSheetExample'
>>> c1 = hfss.assign_current_source_to_sheet(
...     sheet.name, [sheet.bottom_edge_x.midpoint, sheet.bottom_edge_y.midpoint]
... )

```
Copy to clipboard
# assign_current_source_to_sheet 

Hfss.assign_current_source_to_sheet(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _start_direction : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [Gravity](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Gravity "ansys.aedt.core.generic.constants.Gravity") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Create a current source taking one sheet. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the sheet to apply the boundary to. 

**start_direction**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `ansys.aedt.core.application.analysis.Analysis.axis_directions` or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Direction of the integration line. It should be one of the values for `Application.axis_directions`, which are: `XNeg`, `YNeg`, `ZNeg`, `XPos`, `YPos`, and `ZPos`. It also accepts the list of the start point and end point with the format [[xstart, ystart, zstart], [xend, yend, zend]] The default is `Application.axis_directions.XNeg`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the source. The default is `None`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignCurrent

```
Copy to clipboard
Examples
Create a sheet and assign some current to it.

```
>>> from ansys.aedt.core.generic.constants import Plane
>>> sheet = hfss.modeler.create_rectangle(Plane.XY, [0, 0, -50], [5, 1], name="CurrentSheet", material="copper")
>>> hfss.assign_current_source_to_sheet(sheet.name, hfss.axis_directions.XNeg, "CurrentSheetExample")
'CurrentSheetExample'
>>> c1 = hfss.assign_current_source_to_sheet(
...     sheet.name, [sheet.bottom_edge_x.midpoint, sheet.bottom_edge_y.midpoint]
... )

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_current_source_to_sheet.rst.txt)

# assign_current_source_to_sheet 

Hfss.assign_current_source_to_sheet(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _start_direction : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [Gravity](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Gravity "ansys.aedt.core.generic.constants.Gravity") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Create a current source taking one sheet. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the sheet to apply the boundary to. 

**start_direction**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `ansys.aedt.core.application.analysis.Analysis.axis_directions` or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Direction of the integration line. It should be one of the values for `Application.axis_directions`, which are: `XNeg`, `YNeg`, `ZNeg`, `XPos`, `YPos`, and `ZPos`. It also accepts the list of the start point and end point with the format [[xstart, ystart, zstart], [xend, yend, zend]] The default is `Application.axis_directions.XNeg`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the source. The default is `None`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignCurrent

```
Copy to clipboard
Examples
Create a sheet and assign some current to it.

```
>>> from ansys.aedt.core.generic.constants import Plane
>>> sheet = hfss.modeler.create_rectangle(Plane.XY, [0, 0, -50], [5, 1], name="CurrentSheet", material="copper")
>>> hfss.assign_current_source_to_sheet(sheet.name, hfss.axis_directions.XNeg, "CurrentSheetExample")
'CurrentSheetExample'
>>> c1 = hfss.assign_current_source_to_sheet(
...     sheet.name, [sheet.bottom_edge_x.midpoint, sheet.bottom_edge_y.midpoint]
... )

```
Copy to clipboard