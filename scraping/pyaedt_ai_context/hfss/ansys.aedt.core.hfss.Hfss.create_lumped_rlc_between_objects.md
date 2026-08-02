---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_lumped_rlc_between_objects.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# create_lumped_rlc_between_objects 

Hfss.create_lumped_rlc_between_objects(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _reference : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")_, _start_direction : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Gravity](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Gravity "ansys.aedt.core.generic.constants.Gravity") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _rlc_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Parallel'_, _resistance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _inductance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _capacitance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_boundary_on_plane : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a lumped RLC taking the closest edges of two objects. 

Parameters: 
     

**assignment**
    
Starting object for the integration line. 

**reference**
    
Ending object for the integration line. 

**start_direction**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `ansys.aedt.core.application.analysis.Analysis.axis_directions`, `optional` 
    
Start direction for the boundary location.. It should be one of the values for `Application.axis_directions`, which are: `XNeg`, `YNeg`, `ZNeg`, `XPos`, `YPos`, and `ZPos`. The default is `Application.axis_directions.XNeg`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Perfect H name. The default is `None`, in which case a name is automatically assigned. 

**rlc_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the RLC. Options are `"Parallel"` and `"Serial"`. The default is `"Parallel"`. 

**resistance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Resistance value in ohms. The default is `None`, in which case this parameter is disabled. 

**inductance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Inductance value in H. The default is `None`, in which case this parameter is disabled. 

**capacitance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Capacitance value in F. The default is `None`, in which case this parameter is disabled. 

**is_boundary_on_plane**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create the boundary on the plane orthogonal to `axis_directions`. The default is `True`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Boundary object if successful, `False` otherwise.
References

```
>>> oModule.AssignLumpedRLC

```
Copy to clipboard
Examples
Create two boxes for creating a lumped RLC named `'LumpedRLC'`.

```
>>> box1 = hfss.modeler.create_box([0, 0, 50], [10, 10, 5], "rlc1", "copper")
>>> box2 = hfss.modeler.create_box([0, 0, 60], [10, 10, 5], "rlc2", "copper")
>>> rlc = hfss.create_lumped_rlc_between_objects(
...     "rlc1",
...     "rlc2",
...     hfss.axis_directions.XPos,
...     "Lumped RLC",
...     resistance=50,
...     inductance=1e-9,
...     capacitance=1e-6,
... )
PyAEDT INFO: Connection Correctly created

```
Copy to clipboard
# create_lumped_rlc_between_objects 

Hfss.create_lumped_rlc_between_objects(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _reference : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")_, _start_direction : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Gravity](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Gravity "ansys.aedt.core.generic.constants.Gravity") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _rlc_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Parallel'_, _resistance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _inductance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _capacitance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_boundary_on_plane : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a lumped RLC taking the closest edges of two objects. 

Parameters: 
     

**assignment**
    
Starting object for the integration line. 

**reference**
    
Ending object for the integration line. 

**start_direction**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `ansys.aedt.core.application.analysis.Analysis.axis_directions`, `optional` 
    
Start direction for the boundary location.. It should be one of the values for `Application.axis_directions`, which are: `XNeg`, `YNeg`, `ZNeg`, `XPos`, `YPos`, and `ZPos`. The default is `Application.axis_directions.XNeg`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Perfect H name. The default is `None`, in which case a name is automatically assigned. 

**rlc_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the RLC. Options are `"Parallel"` and `"Serial"`. The default is `"Parallel"`. 

**resistance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Resistance value in ohms. The default is `None`, in which case this parameter is disabled. 

**inductance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Inductance value in H. The default is `None`, in which case this parameter is disabled. 

**capacitance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Capacitance value in F. The default is `None`, in which case this parameter is disabled. 

**is_boundary_on_plane**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create the boundary on the plane orthogonal to `axis_directions`. The default is `True`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Boundary object if successful, `False` otherwise.
References

```
>>> oModule.AssignLumpedRLC

```
Copy to clipboard
Examples
Create two boxes for creating a lumped RLC named `'LumpedRLC'`.

```
>>> box1 = hfss.modeler.create_box([0, 0, 50], [10, 10, 5], "rlc1", "copper")
>>> box2 = hfss.modeler.create_box([0, 0, 60], [10, 10, 5], "rlc2", "copper")
>>> rlc = hfss.create_lumped_rlc_between_objects(
...     "rlc1",
...     "rlc2",
...     hfss.axis_directions.XPos,
...     "Lumped RLC",
...     resistance=50,
...     inductance=1e-9,
...     capacitance=1e-6,
... )
PyAEDT INFO: Connection Correctly created

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_lumped_rlc_between_objects.rst.txt)

# create_lumped_rlc_between_objects 

Hfss.create_lumped_rlc_between_objects(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _reference : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")_, _start_direction : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Gravity](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Gravity "ansys.aedt.core.generic.constants.Gravity") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _rlc_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Parallel'_, _resistance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _inductance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _capacitance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_boundary_on_plane : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a lumped RLC taking the closest edges of two objects. 

Parameters: 
     

**assignment**
    
Starting object for the integration line. 

**reference**
    
Ending object for the integration line. 

**start_direction**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `ansys.aedt.core.application.analysis.Analysis.axis_directions`, `optional` 
    
Start direction for the boundary location.. It should be one of the values for `Application.axis_directions`, which are: `XNeg`, `YNeg`, `ZNeg`, `XPos`, `YPos`, and `ZPos`. The default is `Application.axis_directions.XNeg`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Perfect H name. The default is `None`, in which case a name is automatically assigned. 

**rlc_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the RLC. Options are `"Parallel"` and `"Serial"`. The default is `"Parallel"`. 

**resistance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Resistance value in ohms. The default is `None`, in which case this parameter is disabled. 

**inductance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Inductance value in H. The default is `None`, in which case this parameter is disabled. 

**capacitance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Capacitance value in F. The default is `None`, in which case this parameter is disabled. 

**is_boundary_on_plane**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create the boundary on the plane orthogonal to `axis_directions`. The default is `True`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Boundary object if successful, `False` otherwise.
References

```
>>> oModule.AssignLumpedRLC

```
Copy to clipboard
Examples
Create two boxes for creating a lumped RLC named `'LumpedRLC'`.

```
>>> box1 = hfss.modeler.create_box([0, 0, 50], [10, 10, 5], "rlc1", "copper")
>>> box2 = hfss.modeler.create_box([0, 0, 60], [10, 10, 5], "rlc2", "copper")
>>> rlc = hfss.create_lumped_rlc_between_objects(
...     "rlc1",
...     "rlc2",
...     hfss.axis_directions.XPos,
...     "Lumped RLC",
...     resistance=50,
...     inductance=1e-9,
...     capacitance=1e-6,
... )
PyAEDT INFO: Connection Correctly created

```
Copy to clipboard