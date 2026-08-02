---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.objects_in_bounding_box.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# objects_in_bounding_box 

Modeler2D.objects_in_bounding_box(_bounding_box : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _check_lines : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _check_sheets : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Given a 2D bounding box, check if sheets and lines are inside it. 

Parameters: 
     

**bounding_box**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of either the 4 or 6 coordinates of the bounding box vertices. Bounding box is provided as [xmin, ymin, zmin, xmax, ymax, zmax]. 

**check_lines**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to check line objects. The default is `True`. 

**check_sheets**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to check sheet objects. The default is `True`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")]
    
Examples

```
>>> from ansys.aedt.core.modeler.modeler_2d import Modeler2D
>>> obj = Modeler2D()
>>> obj.objects_in_bounding_box(bounding_box=["Box1"])

```
Copy to clipboard
# objects_in_bounding_box 

Modeler2D.objects_in_bounding_box(_bounding_box : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _check_lines : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _check_sheets : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Given a 2D bounding box, check if sheets and lines are inside it. 

Parameters: 
     

**bounding_box**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of either the 4 or 6 coordinates of the bounding box vertices. Bounding box is provided as [xmin, ymin, zmin, xmax, ymax, zmax]. 

**check_lines**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to check line objects. The default is `True`. 

**check_sheets**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to check sheet objects. The default is `True`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")]
    
Examples

```
>>> from ansys.aedt.core.modeler.modeler_2d import Modeler2D
>>> obj = Modeler2D()
>>> obj.objects_in_bounding_box(bounding_box=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.objects_in_bounding_box.rst.txt)

# objects_in_bounding_box 

Modeler2D.objects_in_bounding_box(_bounding_box : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _check_lines : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _check_sheets : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Given a 2D bounding box, check if sheets and lines are inside it. 

Parameters: 
     

**bounding_box**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of either the 4 or 6 coordinates of the bounding box vertices. Bounding box is provided as [xmin, ymin, zmin, xmax, ymax, zmax]. 

**check_lines**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to check line objects. The default is `True`. 

**check_sheets**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to check sheet objects. The default is `True`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")]
    
Examples

```
>>> from ansys.aedt.core.modeler.modeler_2d import Modeler2D
>>> obj = Modeler2D()
>>> obj.objects_in_bounding_box(bounding_box=["Box1"])

```
Copy to clipboard