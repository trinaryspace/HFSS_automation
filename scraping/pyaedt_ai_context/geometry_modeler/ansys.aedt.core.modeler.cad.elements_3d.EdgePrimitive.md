---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# EdgePrimitive 

class ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive(_object3d_ , _edge_id_) 
    
Contains the edge object within the AEDT Desktop Modeler. 

Parameters: 
     

**object3d**[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Pointer to the calling object that provides additional functionality. 

**edge_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Object ID as determined by the parent object.
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import EdgePrimitive
>>> obj = EdgePrimitive()

```
Copy to clipboard
Methods  
| [`EdgePrimitive.chamfer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.chamfer.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.chamfer "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.chamfer")([left_distance, ...])  | Add a chamfer to the selected edges in 3D/vertices in 2D.  |  
| --- | --- |  
| [`EdgePrimitive.create_object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.create_object.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.create_object "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.create_object")([non_model])  | Return a new object from the selected edge.  |  
| [`EdgePrimitive.fillet`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.fillet.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.fillet "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.fillet")([radius, setback])  | Add a fillet to the selected edges in 3D/vertices in 2D.  |  
| [`EdgePrimitive.move_along_normal`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.move_along_normal.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.move_along_normal "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.move_along_normal")([offset])  | Move this edge.  |  
Attributes  
| [`EdgePrimitive.length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.length.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.length "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.length")  | Length of the edge.  |  
| --- | --- |  
| [`EdgePrimitive.midpoint`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.midpoint.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.midpoint "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.midpoint")  | Midpoint coordinates of the edge.  |  
| [`EdgePrimitive.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.name.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.name "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.name")  | Name of the object.  |  
| [`EdgePrimitive.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.public_dir.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.public_dir "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.public_dir")  | Shortcut for dir(self).  |  
| [`EdgePrimitive.segment_info`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.segment_info.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.segment_info "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.segment_info")  | Compute segment information using the object-oriented method (from AEDT 2021 R2 with beta options).  |  
| [`EdgePrimitive.vertices`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.vertices.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.vertices "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.vertices")  | Vertices list.  |  
# EdgePrimitive 

class ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive(_object3d_ , _edge_id_) 
    
Contains the edge object within the AEDT Desktop Modeler. 

Parameters: 
     

**object3d**[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Pointer to the calling object that provides additional functionality. 

**edge_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Object ID as determined by the parent object.
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import EdgePrimitive
>>> obj = EdgePrimitive()

```
Copy to clipboard
Methods  
| [`EdgePrimitive.chamfer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.chamfer.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.chamfer "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.chamfer")([left_distance, ...])  | Add a chamfer to the selected edges in 3D/vertices in 2D.  |  
| --- | --- |  
| [`EdgePrimitive.create_object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.create_object.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.create_object "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.create_object")([non_model])  | Return a new object from the selected edge.  |  
| [`EdgePrimitive.fillet`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.fillet.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.fillet "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.fillet")([radius, setback])  | Add a fillet to the selected edges in 3D/vertices in 2D.  |  
| [`EdgePrimitive.move_along_normal`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.move_along_normal.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.move_along_normal "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.move_along_normal")([offset])  | Move this edge.  |  
Attributes  
| [`EdgePrimitive.length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.length.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.length "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.length")  | Length of the edge.  |  
| --- | --- |  
| [`EdgePrimitive.midpoint`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.midpoint.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.midpoint "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.midpoint")  | Midpoint coordinates of the edge.  |  
| [`EdgePrimitive.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.name.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.name "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.name")  | Name of the object.  |  
| [`EdgePrimitive.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.public_dir.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.public_dir "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.public_dir")  | Shortcut for dir(self).  |  
| [`EdgePrimitive.segment_info`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.segment_info.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.segment_info "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.segment_info")  | Compute segment information using the object-oriented method (from AEDT 2021 R2 with beta options).  |  
| [`EdgePrimitive.vertices`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.vertices.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.vertices "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.vertices")  | Vertices list.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.rst.txt)

# EdgePrimitive 

class ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive(_object3d_ , _edge_id_) 
    
Contains the edge object within the AEDT Desktop Modeler. 

Parameters: 
     

**object3d**[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Pointer to the calling object that provides additional functionality. 

**edge_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Object ID as determined by the parent object.
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import EdgePrimitive
>>> obj = EdgePrimitive()

```
Copy to clipboard
Methods  
| [`EdgePrimitive.chamfer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.chamfer.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.chamfer "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.chamfer")([left_distance, ...])  | Add a chamfer to the selected edges in 3D/vertices in 2D.  |  
| --- | --- |  
| [`EdgePrimitive.create_object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.create_object.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.create_object "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.create_object")([non_model])  | Return a new object from the selected edge.  |  
| [`EdgePrimitive.fillet`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.fillet.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.fillet "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.fillet")([radius, setback])  | Add a fillet to the selected edges in 3D/vertices in 2D.  |  
| [`EdgePrimitive.move_along_normal`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.move_along_normal.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.move_along_normal "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.move_along_normal")([offset])  | Move this edge.  |  
Attributes  
| [`EdgePrimitive.length`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.length.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.length "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.length")  | Length of the edge.  |  
| --- | --- |  
| [`EdgePrimitive.midpoint`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.midpoint.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.midpoint "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.midpoint")  | Midpoint coordinates of the edge.  |  
| [`EdgePrimitive.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.name.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.name "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.name")  | Name of the object.  |  
| [`EdgePrimitive.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.public_dir.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.public_dir "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.public_dir")  | Shortcut for dir(self).  |  
| [`EdgePrimitive.segment_info`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.segment_info.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.segment_info "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.segment_info")  | Compute segment information using the object-oriented method (from AEDT 2021 R2 with beta options).  |  
| [`EdgePrimitive.vertices`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.vertices.html#ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.vertices "ansys.aedt.core.modeler.cad.elements_3d.EdgePrimitive.vertices")  | Vertices list.  |