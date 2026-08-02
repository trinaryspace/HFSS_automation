---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_symmetry.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# assign_symmetry 

Hfss.assign_symmetry(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_perfect_e : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Assign symmetry to planar entities. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of IDs or [`ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive"). 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the boundary. If a name is not provided, one is automatically generated. 

**is_perfect_e**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Type of symmetry plane the boundary represents: Perfect E or Perfect H. The default value is `True` (Perfect E). 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignSymmetry

```
Copy to clipboard
Examples
Create a box. Select the faces of this box and assign a symmetry.

```
>>> symmetry_box = hfss.modeler.create_box([0, -100, 0], [200, 200, 200], name="SymmetryForFaces")
>>> ids = [i.id for i in hfss.modeler["SymmetryForFaces"].faces]
>>> symmetry = hfss.assign_symmetry(ids)
>>> type(symmetry)
<class 'from ansys.aedt.core.modules.boundary.common.BoundaryObject'>

```
Copy to clipboard
# assign_symmetry 

Hfss.assign_symmetry(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_perfect_e : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Assign symmetry to planar entities. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of IDs or [`ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive"). 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the boundary. If a name is not provided, one is automatically generated. 

**is_perfect_e**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Type of symmetry plane the boundary represents: Perfect E or Perfect H. The default value is `True` (Perfect E). 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignSymmetry

```
Copy to clipboard
Examples
Create a box. Select the faces of this box and assign a symmetry.

```
>>> symmetry_box = hfss.modeler.create_box([0, -100, 0], [200, 200, 200], name="SymmetryForFaces")
>>> ids = [i.id for i in hfss.modeler["SymmetryForFaces"].faces]
>>> symmetry = hfss.assign_symmetry(ids)
>>> type(symmetry)
<class 'from ansys.aedt.core.modules.boundary.common.BoundaryObject'>

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.assign_symmetry.rst.txt)

# assign_symmetry 

Hfss.assign_symmetry(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_perfect_e : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Assign symmetry to planar entities. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of IDs or [`ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive"). 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the boundary. If a name is not provided, one is automatically generated. 

**is_perfect_e**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Type of symmetry plane the boundary represents: Perfect E or Perfect H. The default value is `True` (Perfect E). 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.AssignSymmetry

```
Copy to clipboard
Examples
Create a box. Select the faces of this box and assign a symmetry.

```
>>> symmetry_box = hfss.modeler.create_box([0, -100, 0], [200, 200, 200], name="SymmetryForFaces")
>>> ids = [i.id for i in hfss.modeler["SymmetryForFaces"].faces]
>>> symmetry = hfss.assign_symmetry(ids)
>>> type(symmetry)
<class 'from ansys.aedt.core.modules.boundary.common.BoundaryObject'>

```
Copy to clipboard