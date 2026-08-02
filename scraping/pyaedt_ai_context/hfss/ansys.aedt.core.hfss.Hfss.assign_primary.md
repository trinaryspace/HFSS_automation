---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_primary.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# assign_primary 

Hfss.assign_primary(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")_, _u_start : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _u_end : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _reverse_v : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Assign the primary boundary condition. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `FacePrimitive` 
    
Face to assign the lattice pair to. 

**u_start**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x,y,z]` values for the starting point of the U vector. 

**u_end**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x,y,z]` values for the ending point of the U vector. 

**reverse_v**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to reverse the V vector. The default is False. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system for the U coordinates. The default is `"Global"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the boundary. The default is `None`, in which case a name is automatically assigned. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignPrimary

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
# assign_primary 

Hfss.assign_primary(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")_, _u_start : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _u_end : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _reverse_v : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Assign the primary boundary condition. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `FacePrimitive` 
    
Face to assign the lattice pair to. 

**u_start**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x,y,z]` values for the starting point of the U vector. 

**u_end**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x,y,z]` values for the ending point of the U vector. 

**reverse_v**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to reverse the V vector. The default is False. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system for the U coordinates. The default is `"Global"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the boundary. The default is `None`, in which case a name is automatically assigned. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignPrimary

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
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_primary.rst.txt)

# assign_primary 

Hfss.assign_primary(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [FacePrimitive](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive")_, _u_start : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _u_end : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _reverse_v : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Assign the primary boundary condition. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `FacePrimitive` 
    
Face to assign the lattice pair to. 

**u_start**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x,y,z]` values for the starting point of the U vector. 

**u_end**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x,y,z]` values for the ending point of the U vector. 

**reverse_v**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to reverse the V vector. The default is False. 

**coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system for the U coordinates. The default is `"Global"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the boundary. The default is `None`, in which case a name is automatically assigned. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignPrimary

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