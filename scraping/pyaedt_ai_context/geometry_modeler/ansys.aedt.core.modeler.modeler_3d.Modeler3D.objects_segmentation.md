---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.objects_segmentation.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# objects_segmentation 

Modeler3D.objects_segmentation(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _segmentation_thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _segments : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _apply_mesh_sheets : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _mesh_sheets : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Get segmentation of an object given the segmentation thickness or number of segments. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of objects to apply the segmentation to. It can either be a list of strings (object names), integers (object IDs), or a list[[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")] classes. 

**segmentation_thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Segmentation thickness. Model units are automatically assigned. The default is `None`. 

**segments**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments to segment the object to. The default is `None`. 

**apply_mesh_sheets**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to apply mesh sheets to selected objects. Mesh sheets are needed in case the user would like to have additional layers inside the objects for a finer mesh and more accurate results. The default is `False`. 

**mesh_sheets**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of mesh sheets within one magnet segment. If nothing is provided and `apply_mesh_sheets=True`, the default value is `2`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Depending on value `apply_mesh_sheets` it returns either a dictionary or a tuple. If mesh sheets are applied the method returns a tuple where: - First dictionary is the segments that the object has been divided into. - Second dictionary is the mesh sheets eventually needed to apply the mesh. to inside the object. Keys are the object names, and values are respectively segments sheets and mesh sheets of the [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") class. If mesh sheets are not applied the method returns only the dictionary of segments that the object has been divided into. `False` is returned if the method fails.
Examples

```
>>> from ansys.aedt.core.modeler.modeler_3d import Modeler3D
>>> obj = Modeler3D()
>>> obj.objects_segmentation(assignment="Box1")

```
Copy to clipboard
# objects_segmentation 

Modeler3D.objects_segmentation(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _segmentation_thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _segments : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _apply_mesh_sheets : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _mesh_sheets : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Get segmentation of an object given the segmentation thickness or number of segments. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of objects to apply the segmentation to. It can either be a list of strings (object names), integers (object IDs), or a list[[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")] classes. 

**segmentation_thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Segmentation thickness. Model units are automatically assigned. The default is `None`. 

**segments**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments to segment the object to. The default is `None`. 

**apply_mesh_sheets**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to apply mesh sheets to selected objects. Mesh sheets are needed in case the user would like to have additional layers inside the objects for a finer mesh and more accurate results. The default is `False`. 

**mesh_sheets**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of mesh sheets within one magnet segment. If nothing is provided and `apply_mesh_sheets=True`, the default value is `2`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Depending on value `apply_mesh_sheets` it returns either a dictionary or a tuple. If mesh sheets are applied the method returns a tuple where: - First dictionary is the segments that the object has been divided into. - Second dictionary is the mesh sheets eventually needed to apply the mesh. to inside the object. Keys are the object names, and values are respectively segments sheets and mesh sheets of the [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") class. If mesh sheets are not applied the method returns only the dictionary of segments that the object has been divided into. `False` is returned if the method fails.
Examples

```
>>> from ansys.aedt.core.modeler.modeler_3d import Modeler3D
>>> obj = Modeler3D()
>>> obj.objects_segmentation(assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.objects_segmentation.rst.txt)

# objects_segmentation 

Modeler3D.objects_segmentation(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _segmentation_thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _segments : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _apply_mesh_sheets : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _mesh_sheets : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Get segmentation of an object given the segmentation thickness or number of segments. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of objects to apply the segmentation to. It can either be a list of strings (object names), integers (object IDs), or a list[[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")] classes. 

**segmentation_thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Segmentation thickness. Model units are automatically assigned. The default is `None`. 

**segments**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments to segment the object to. The default is `None`. 

**apply_mesh_sheets**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to apply mesh sheets to selected objects. Mesh sheets are needed in case the user would like to have additional layers inside the objects for a finer mesh and more accurate results. The default is `False`. 

**mesh_sheets**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of mesh sheets within one magnet segment. If nothing is provided and `apply_mesh_sheets=True`, the default value is `2`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Depending on value `apply_mesh_sheets` it returns either a dictionary or a tuple. If mesh sheets are applied the method returns a tuple where: - First dictionary is the segments that the object has been divided into. - Second dictionary is the mesh sheets eventually needed to apply the mesh. to inside the object. Keys are the object names, and values are respectively segments sheets and mesh sheets of the [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") class. If mesh sheets are not applied the method returns only the dictionary of segments that the object has been divided into. `False` is returned if the method fails.
Examples

```
>>> from ansys.aedt.core.modeler.modeler_3d import Modeler3D
>>> obj = Modeler3D()
>>> obj.objects_segmentation(assignment="Box1")

```
Copy to clipboard