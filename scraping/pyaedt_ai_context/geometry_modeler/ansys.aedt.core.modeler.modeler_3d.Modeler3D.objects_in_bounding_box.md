---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.objects_in_bounding_box.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# objects_in_bounding_box 

Modeler3D.objects_in_bounding_box(_bounding_box : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _check_solids : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _check_lines : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _check_sheets : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")['Object3d'] 
    
Given a bounding box checks if objects, sheets and lines are inside it. 

Parameters: 
     

**bounding_box**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of coordinates of bounding box vertices. Bounding box is provided as [xmin, ymin, zmin, xmax, ymax, zmax]. 

**check_solids**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Check solid objects. 

**check_lines**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Check line objects. 

**check_sheets**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Check sheet objects. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")]
    
Examples

```
>>> from ansys.aedt.core.modeler.modeler_3d import Modeler3D
>>> obj = Modeler3D()
>>> obj.objects_in_bounding_box(bounding_box=["Box1"])

```
Copy to clipboard
# objects_in_bounding_box 

Modeler3D.objects_in_bounding_box(_bounding_box : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _check_solids : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _check_lines : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _check_sheets : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")['Object3d'] 
    
Given a bounding box checks if objects, sheets and lines are inside it. 

Parameters: 
     

**bounding_box**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of coordinates of bounding box vertices. Bounding box is provided as [xmin, ymin, zmin, xmax, ymax, zmax]. 

**check_solids**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Check solid objects. 

**check_lines**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Check line objects. 

**check_sheets**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Check sheet objects. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")]
    
Examples

```
>>> from ansys.aedt.core.modeler.modeler_3d import Modeler3D
>>> obj = Modeler3D()
>>> obj.objects_in_bounding_box(bounding_box=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.objects_in_bounding_box.rst.txt)

# objects_in_bounding_box 

Modeler3D.objects_in_bounding_box(_bounding_box : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _check_solids : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _check_lines : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _check_sheets : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")['Object3d'] 
    
Given a bounding box checks if objects, sheets and lines are inside it. 

Parameters: 
     

**bounding_box**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of coordinates of bounding box vertices. Bounding box is provided as [xmin, ymin, zmin, xmax, ymax, zmax]. 

**check_solids**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Check solid objects. 

**check_lines**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Check line objects. 

**check_sheets**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Check sheet objects. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")]
    
Examples

```
>>> from ansys.aedt.core.modeler.modeler_3d import Modeler3D
>>> obj = Modeler3D()
>>> obj.objects_in_bounding_box(bounding_box=["Box1"])

```
Copy to clipboard