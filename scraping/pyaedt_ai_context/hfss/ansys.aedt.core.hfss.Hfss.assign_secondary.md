---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_secondary.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# assign_secondary 

Hfss.assign_secondary(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")_, _primary : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _u_start : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _u_end : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _reverse_v : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _phase_delay : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'UseScanAngle'_, _phase_delay_param1 : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = '0deg'_, _phase_delay_param2 : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = '0deg'_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Assign the secondary boundary condition. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `FacePrimitive` 
    
Face to assign the lattice pair to. 

**primary**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the primary boundary to couple. 

**u_start**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x,y,z]` values for the starting point of the U vector. 

**u_end**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x,y,z]` values for the ending point of the U vector. 

**reverse_v**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to reverse the V vector. The default is `False`. 

**phase_delay**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Phase delay approach. Options are `"UseScanAngle"`, `"UseScanUV"`, and `"InputPhaseDelay"`. The default is `"UseScanAngle"`. 

**phase_delay_param1**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Value for the first phase delay parameter, which depends on the approach:
  * Phi angle if the approach is `"UseScanAngle"`.
  * U value if the approach is `"UseScanUV"`.
  * Phase if the approach is `"InputPhaseDelay"`.

The default is `0deg`. 

**phase_delay_param2**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Value for the second phase delay parameter, which depends on the approach:
  * Theta angle if the approach is “`UseScanAngle"`.
  * V value if the approach is `"UseScanUV"`.

The default is `0deg`. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system for U coordinates. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the boundary. The default is `None`, in which case a name is automatically assigned. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignSecondary

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> box1 = hfss.modeler.create_box([-100, -100, -100], [200, 200, 200])
>>> primary = hfss.assign_primary(box1.faces[4], [100, -100, -100], [100, 100, -100])
>>> secondary = hfss.assign_secondary(box1.faces[0], primary.name, [100, -100, 100], [100, 100, 100])

```
Copy to clipboard
# assign_secondary 

Hfss.assign_secondary(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")_, _primary : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _u_start : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _u_end : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _reverse_v : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _phase_delay : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'UseScanAngle'_, _phase_delay_param1 : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = '0deg'_, _phase_delay_param2 : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = '0deg'_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Assign the secondary boundary condition. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `FacePrimitive` 
    
Face to assign the lattice pair to. 

**primary**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the primary boundary to couple. 

**u_start**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x,y,z]` values for the starting point of the U vector. 

**u_end**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x,y,z]` values for the ending point of the U vector. 

**reverse_v**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to reverse the V vector. The default is `False`. 

**phase_delay**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Phase delay approach. Options are `"UseScanAngle"`, `"UseScanUV"`, and `"InputPhaseDelay"`. The default is `"UseScanAngle"`. 

**phase_delay_param1**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Value for the first phase delay parameter, which depends on the approach:
  * Phi angle if the approach is `"UseScanAngle"`.
  * U value if the approach is `"UseScanUV"`.
  * Phase if the approach is `"InputPhaseDelay"`.

The default is `0deg`. 

**phase_delay_param2**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Value for the second phase delay parameter, which depends on the approach:
  * Theta angle if the approach is “`UseScanAngle"`.
  * V value if the approach is `"UseScanUV"`.

The default is `0deg`. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system for U coordinates. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the boundary. The default is `None`, in which case a name is automatically assigned. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignSecondary

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> box1 = hfss.modeler.create_box([-100, -100, -100], [200, 200, 200])
>>> primary = hfss.assign_primary(box1.faces[4], [100, -100, -100], [100, 100, -100])
>>> secondary = hfss.assign_secondary(box1.faces[0], primary.name, [100, -100, 100], [100, 100, 100])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_secondary.rst.txt)

# assign_secondary 

Hfss.assign_secondary(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")_, _primary : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _u_start : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _u_end : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _reverse_v : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _phase_delay : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'UseScanAngle'_, _phase_delay_param1 : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = '0deg'_, _phase_delay_param2 : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = '0deg'_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Assign the secondary boundary condition. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `FacePrimitive` 
    
Face to assign the lattice pair to. 

**primary**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the primary boundary to couple. 

**u_start**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x,y,z]` values for the starting point of the U vector. 

**u_end**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x,y,z]` values for the ending point of the U vector. 

**reverse_v**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to reverse the V vector. The default is `False`. 

**phase_delay**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Phase delay approach. Options are `"UseScanAngle"`, `"UseScanUV"`, and `"InputPhaseDelay"`. The default is `"UseScanAngle"`. 

**phase_delay_param1**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Value for the first phase delay parameter, which depends on the approach:
  * Phi angle if the approach is `"UseScanAngle"`.
  * U value if the approach is `"UseScanUV"`.
  * Phase if the approach is `"InputPhaseDelay"`.

The default is `0deg`. 

**phase_delay_param2**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Value for the second phase delay parameter, which depends on the approach:
  * Theta angle if the approach is “`UseScanAngle"`.
  * V value if the approach is `"UseScanUV"`.

The default is `0deg`. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system for U coordinates. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the boundary. The default is `None`, in which case a name is automatically assigned. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignSecondary

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> box1 = hfss.modeler.create_box([-100, -100, -100], [200, 200, 200])
>>> primary = hfss.assign_primary(box1.faces[4], [100, -100, -100], [100, 100, -100])
>>> secondary = hfss.assign_secondary(box1.faces[0], primary.name, [100, -100, 100], [100, 100, 100])

```
Copy to clipboard