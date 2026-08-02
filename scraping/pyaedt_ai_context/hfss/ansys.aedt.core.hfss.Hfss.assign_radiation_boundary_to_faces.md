---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_radiation_boundary_to_faces.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# assign_radiation_boundary_to_faces 

Hfss.assign_radiation_boundary_to_faces(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Assign a radiation boundary to one or more faces. 

Parameters: 
     

**assignment**
    
Face ID to assign the boundary condition to. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the boundary. The default is `None`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignRadiation

```
Copy to clipboard
Examples
Create a box. Select the faces of this box and assign a radiation boundary to them.

```
>>> radiation_box = hfss.modeler.create_box([0, -100, 0], [200, 200, 200], name="RadiationForFaces")
>>> ids = [i.id for i in hfss.modeler["RadiationForFaces"].faces]
>>> radiation = hfss.assign_radiation_boundary_to_faces(ids)
>>> type(radiation)
<class 'from ansys.aedt.core.modules.boundary.common.BoundaryObject'>

```
Copy to clipboard
# assign_radiation_boundary_to_faces 

Hfss.assign_radiation_boundary_to_faces(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Assign a radiation boundary to one or more faces. 

Parameters: 
     

**assignment**
    
Face ID to assign the boundary condition to. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the boundary. The default is `None`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignRadiation

```
Copy to clipboard
Examples
Create a box. Select the faces of this box and assign a radiation boundary to them.

```
>>> radiation_box = hfss.modeler.create_box([0, -100, 0], [200, 200, 200], name="RadiationForFaces")
>>> ids = [i.id for i in hfss.modeler["RadiationForFaces"].faces]
>>> radiation = hfss.assign_radiation_boundary_to_faces(ids)
>>> type(radiation)
<class 'from ansys.aedt.core.modules.boundary.common.BoundaryObject'>

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_radiation_boundary_to_faces.rst.txt)

# assign_radiation_boundary_to_faces 

Hfss.assign_radiation_boundary_to_faces(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Assign a radiation boundary to one or more faces. 

Parameters: 
     

**assignment**
    
Face ID to assign the boundary condition to. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the boundary. The default is `None`. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignRadiation

```
Copy to clipboard
Examples
Create a box. Select the faces of this box and assign a radiation boundary to them.

```
>>> radiation_box = hfss.modeler.create_box([0, -100, 0], [200, 200, 200], name="RadiationForFaces")
>>> ids = [i.id for i in hfss.modeler["RadiationForFaces"].faces]
>>> radiation = hfss.assign_radiation_boundary_to_faces(ids)
>>> type(radiation)
<class 'from ansys.aedt.core.modules.boundary.common.BoundaryObject'>

```
Copy to clipboard