---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_lumped_rlc_to_sheet.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# assign_lumped_rlc_to_sheet 

Hfss.assign_lumped_rlc_to_sheet(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _start_direction : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [Gravity](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Gravity "ansys.aedt.core.generic.constants.Gravity") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _rlc_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Parallel'_, _resistance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _inductance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _capacitance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a lumped RLC taking one sheet. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the sheet to apply the boundary to. 

**start_direction**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `ansys.aedt.core.application.analysis.Analysis.axis_directions` or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Direction of the integration line. It should be one of the values for `Application.axis_directions`, which are: `XNeg`, `YNeg`, `ZNeg`, `XPos`, `YPos`, and `ZPos`. It also accepts the list of the start point and end point with the format [[xstart, ystart, zstart], [xend, yend, zend]] The default is `Application.axis_directions.XNeg`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Lumped RLC name. The default is `None`. 

**rlc_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the RLC. Options are `"Parallel"` and `"Serial"`. The default is `"Parallel"`. 

**resistance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Resistance value in ohms. The default is `None`, in which case this parameter is disabled. 

**inductance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Inductance value in Henry (H). The default is `None`, in which case this parameter is disabled. 

**capacitance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Capacitance value in farads (F). The default is `None`, in which case this parameter is disabled. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object if successful, `False` otherwise.
References

```
>>> oModule.AssignLumpedRLC

```
Copy to clipboard
Examples
Create a sheet and use it to create a lumped RLC.

```
>>> from ansys.aedt.core.generic.constants import Plane
>>> sheet = hfss.modeler.create_rectangle(Plane.XY, [0, 0, -90], [10, 2], name="RLCSheet", material="Copper")
>>> lumped_rlc_to_sheet = hfss.assign_lumped_rlc_to_sheet(
...     sheet.name, hfss.axis_directions.XPos, resistance=50, inductance=1e-9, capacitance=1e-6
... )
>>> type(lumped_rlc_to_sheet)
<class 'from ansys.aedt.core.modules.boundary.common.BoundaryObject'>
>>> h2 = hfss.assign_lumped_rlc_to_sheet(
...     sheet.name,
...     [sheet.bottom_edge_x.midpoint, sheet.bottom_edge_y.midpoint],
...     resistance=50,
...     inductance=1e-9,
...     capacitance=1e-6,
... )

```
Copy to clipboard
# assign_lumped_rlc_to_sheet 

Hfss.assign_lumped_rlc_to_sheet(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _start_direction : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [Gravity](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Gravity "ansys.aedt.core.generic.constants.Gravity") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _rlc_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Parallel'_, _resistance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _inductance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _capacitance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a lumped RLC taking one sheet. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the sheet to apply the boundary to. 

**start_direction**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `ansys.aedt.core.application.analysis.Analysis.axis_directions` or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Direction of the integration line. It should be one of the values for `Application.axis_directions`, which are: `XNeg`, `YNeg`, `ZNeg`, `XPos`, `YPos`, and `ZPos`. It also accepts the list of the start point and end point with the format [[xstart, ystart, zstart], [xend, yend, zend]] The default is `Application.axis_directions.XNeg`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Lumped RLC name. The default is `None`. 

**rlc_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the RLC. Options are `"Parallel"` and `"Serial"`. The default is `"Parallel"`. 

**resistance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Resistance value in ohms. The default is `None`, in which case this parameter is disabled. 

**inductance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Inductance value in Henry (H). The default is `None`, in which case this parameter is disabled. 

**capacitance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Capacitance value in farads (F). The default is `None`, in which case this parameter is disabled. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object if successful, `False` otherwise.
References

```
>>> oModule.AssignLumpedRLC

```
Copy to clipboard
Examples
Create a sheet and use it to create a lumped RLC.

```
>>> from ansys.aedt.core.generic.constants import Plane
>>> sheet = hfss.modeler.create_rectangle(Plane.XY, [0, 0, -90], [10, 2], name="RLCSheet", material="Copper")
>>> lumped_rlc_to_sheet = hfss.assign_lumped_rlc_to_sheet(
...     sheet.name, hfss.axis_directions.XPos, resistance=50, inductance=1e-9, capacitance=1e-6
... )
>>> type(lumped_rlc_to_sheet)
<class 'from ansys.aedt.core.modules.boundary.common.BoundaryObject'>
>>> h2 = hfss.assign_lumped_rlc_to_sheet(
...     sheet.name,
...     [sheet.bottom_edge_x.midpoint, sheet.bottom_edge_y.midpoint],
...     resistance=50,
...     inductance=1e-9,
...     capacitance=1e-6,
... )

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_lumped_rlc_to_sheet.rst.txt)

# assign_lumped_rlc_to_sheet 

Hfss.assign_lumped_rlc_to_sheet(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _start_direction : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [Gravity](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Gravity "ansys.aedt.core.generic.constants.Gravity") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _rlc_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Parallel'_, _resistance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _inductance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _capacitance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a lumped RLC taking one sheet. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the sheet to apply the boundary to. 

**start_direction**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `ansys.aedt.core.application.analysis.Analysis.axis_directions` or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Direction of the integration line. It should be one of the values for `Application.axis_directions`, which are: `XNeg`, `YNeg`, `ZNeg`, `XPos`, `YPos`, and `ZPos`. It also accepts the list of the start point and end point with the format [[xstart, ystart, zstart], [xend, yend, zend]] The default is `Application.axis_directions.XNeg`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Lumped RLC name. The default is `None`. 

**rlc_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the RLC. Options are `"Parallel"` and `"Serial"`. The default is `"Parallel"`. 

**resistance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Resistance value in ohms. The default is `None`, in which case this parameter is disabled. 

**inductance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Inductance value in Henry (H). The default is `None`, in which case this parameter is disabled. 

**capacitance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Capacitance value in farads (F). The default is `None`, in which case this parameter is disabled. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object if successful, `False` otherwise.
References

```
>>> oModule.AssignLumpedRLC

```
Copy to clipboard
Examples
Create a sheet and use it to create a lumped RLC.

```
>>> from ansys.aedt.core.generic.constants import Plane
>>> sheet = hfss.modeler.create_rectangle(Plane.XY, [0, 0, -90], [10, 2], name="RLCSheet", material="Copper")
>>> lumped_rlc_to_sheet = hfss.assign_lumped_rlc_to_sheet(
...     sheet.name, hfss.axis_directions.XPos, resistance=50, inductance=1e-9, capacitance=1e-6
... )
>>> type(lumped_rlc_to_sheet)
<class 'from ansys.aedt.core.modules.boundary.common.BoundaryObject'>
>>> h2 = hfss.assign_lumped_rlc_to_sheet(
...     sheet.name,
...     [sheet.bottom_edge_x.midpoint, sheet.bottom_edge_y.midpoint],
...     resistance=50,
...     inductance=1e-9,
...     capacitance=1e-6,
... )

```
Copy to clipboard