---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_impedance_to_sheet.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# assign_impedance_to_sheet 

Hfss.assign_impedance_to_sheet(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _resistance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 50.0_, _reactance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0.0_, _is_infinite_ground : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Global'_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create an impedance taking one sheet. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more names of the sheets to apply the boundary to. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the impedance. The default is `None`. 

**resistance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Resistance value in ohms. The default is `50.0`. If a list of four elements is passed, an anisotropic impedance is assigned with the following order, [`Zxx`, `Zxy`, `Zyx`, `Zyy`]. 

**reactance**`optional` 
    
Reactance value in ohms. The default is `0.0`. If a list of four elements is passed, an anisotropic impedance is assigned with the following order, [`Zxx`, `Zxy`, `Zyx`, `Zyy`]. 

**is_infinite_ground**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the impedance is an infinite ground. The default is `False`. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system for the XY plane. The default is `"Global"`. This parameter is only used for anisotropic impedance assignment. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object if successful, `False` otherwise.
References

```
>>> oModule.AssignImpedance

```
Copy to clipboard
Examples
Create a sheet and use it to create an impedance.

```
>>> from ansys.aedt.core.generic.constants import Plane
>>> sheet = hfss.modeler.create_rectangle(
...     Plane.XY, [0, 0, -90], [10, 2], name="ImpedanceSheet", material="Copper"
... )
>>> impedance_to_sheet = hfss.assign_impedance_to_sheet(sheet.name, "ImpedanceFromSheet", 100, 50)

```
Copy to clipboard
Create a sheet and use it to create an anisotropic impedance.

```
>>> sheet = hfss.modeler.create_rectangle(
...     Plane.XY, [0, 0, -90], [10, 2], name="ImpedanceSheet", material="Copper"
... )
>>> anistropic_impedance_to_sheet = hfss.assign_impedance_to_sheet(
...     sheet.name, "ImpedanceFromSheet", [377, 0, 0, 377], [0, 50, 0, 0]
... )

```
Copy to clipboard
# assign_impedance_to_sheet 

Hfss.assign_impedance_to_sheet(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _resistance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 50.0_, _reactance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0.0_, _is_infinite_ground : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Global'_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create an impedance taking one sheet. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more names of the sheets to apply the boundary to. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the impedance. The default is `None`. 

**resistance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Resistance value in ohms. The default is `50.0`. If a list of four elements is passed, an anisotropic impedance is assigned with the following order, [`Zxx`, `Zxy`, `Zyx`, `Zyy`]. 

**reactance**`optional` 
    
Reactance value in ohms. The default is `0.0`. If a list of four elements is passed, an anisotropic impedance is assigned with the following order, [`Zxx`, `Zxy`, `Zyx`, `Zyy`]. 

**is_infinite_ground**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the impedance is an infinite ground. The default is `False`. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system for the XY plane. The default is `"Global"`. This parameter is only used for anisotropic impedance assignment. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object if successful, `False` otherwise.
References

```
>>> oModule.AssignImpedance

```
Copy to clipboard
Examples
Create a sheet and use it to create an impedance.

```
>>> from ansys.aedt.core.generic.constants import Plane
>>> sheet = hfss.modeler.create_rectangle(
...     Plane.XY, [0, 0, -90], [10, 2], name="ImpedanceSheet", material="Copper"
... )
>>> impedance_to_sheet = hfss.assign_impedance_to_sheet(sheet.name, "ImpedanceFromSheet", 100, 50)

```
Copy to clipboard
Create a sheet and use it to create an anisotropic impedance.

```
>>> sheet = hfss.modeler.create_rectangle(
...     Plane.XY, [0, 0, -90], [10, 2], name="ImpedanceSheet", material="Copper"
... )
>>> anistropic_impedance_to_sheet = hfss.assign_impedance_to_sheet(
...     sheet.name, "ImpedanceFromSheet", [377, 0, 0, 377], [0, 50, 0, 0]
... )

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_impedance_to_sheet.rst.txt)

# assign_impedance_to_sheet 

Hfss.assign_impedance_to_sheet(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _resistance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 50.0_, _reactance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0.0_, _is_infinite_ground : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Global'_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create an impedance taking one sheet. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
One or more names of the sheets to apply the boundary to. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the impedance. The default is `None`. 

**resistance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Resistance value in ohms. The default is `50.0`. If a list of four elements is passed, an anisotropic impedance is assigned with the following order, [`Zxx`, `Zxy`, `Zyx`, `Zyy`]. 

**reactance**`optional` 
    
Reactance value in ohms. The default is `0.0`. If a list of four elements is passed, an anisotropic impedance is assigned with the following order, [`Zxx`, `Zxy`, `Zyx`, `Zyy`]. 

**is_infinite_ground**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the impedance is an infinite ground. The default is `False`. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system for the XY plane. The default is `"Global"`. This parameter is only used for anisotropic impedance assignment. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object if successful, `False` otherwise.
References

```
>>> oModule.AssignImpedance

```
Copy to clipboard
Examples
Create a sheet and use it to create an impedance.

```
>>> from ansys.aedt.core.generic.constants import Plane
>>> sheet = hfss.modeler.create_rectangle(
...     Plane.XY, [0, 0, -90], [10, 2], name="ImpedanceSheet", material="Copper"
... )
>>> impedance_to_sheet = hfss.assign_impedance_to_sheet(sheet.name, "ImpedanceFromSheet", 100, 50)

```
Copy to clipboard
Create a sheet and use it to create an anisotropic impedance.

```
>>> sheet = hfss.modeler.create_rectangle(
...     Plane.XY, [0, 0, -90], [10, 2], name="ImpedanceSheet", material="Copper"
... )
>>> anistropic_impedance_to_sheet = hfss.assign_impedance_to_sheet(
...     sheet.name, "ImpedanceFromSheet", [377, 0, 0, 377], [0, 50, 0, 0]
... )

```
Copy to clipboard