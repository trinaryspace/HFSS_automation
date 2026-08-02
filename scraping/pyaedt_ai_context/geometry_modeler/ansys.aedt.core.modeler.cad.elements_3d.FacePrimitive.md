---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# FacePrimitive 

class ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive(_object3d_ , _obj_id_) 
    
Contains the face object within the AEDT Desktop Modeler. 

Parameters: 
     

**object3d**[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
     

**obj_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import FacePrimitive
>>> obj = FacePrimitive()

```
Copy to clipboard
Methods  
| [`FacePrimitive.create_object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.create_object.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.create_object "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.create_object")([non_model])  | Return a new object from the selected face.  |  
| --- | --- |  
| [`FacePrimitive.is_on_bounding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.is_on_bounding.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.is_on_bounding "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.is_on_bounding")([tolerance])  | Check if the face is on bounding box or Not.  |  
| [`FacePrimitive.move_with_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.move_with_offset.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.move_with_offset "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.move_with_offset")([offset])  | Move the face along the normal.  |  
| [`FacePrimitive.move_with_vector`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.move_with_vector.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.move_with_vector "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.move_with_vector")(vector)  | Move the face along a vector.  |  
Attributes  
| [`FacePrimitive.area`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.area.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.area "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.area")  | Face area.  |  
| --- | --- |  
| [`FacePrimitive.bottom_edge_x`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_x.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_x "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_x")  | Bottom edge in the X direction of the object.  |  
| [`FacePrimitive.bottom_edge_y`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_y.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_y "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_y")  | Bottom edge in the X direction of the object.  |  
| [`FacePrimitive.bottom_edge_z`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_z.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_z "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_z")  | Bottom edge in the Z direction of the object.  |  
| [`FacePrimitive.center`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.center.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.center "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.center")  | Face center in model units.  |  
| [`FacePrimitive.center_from_aedt`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.center_from_aedt.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.center_from_aedt "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.center_from_aedt")  | Face center for a planar face in model units.  |  
| [`FacePrimitive.edges`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.edges.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.edges "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.edges")  | Edges lists.  |  
| [`FacePrimitive.id`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.id.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.id "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.id")  | Face ID.  |  
| [`FacePrimitive.is_planar`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.is_planar.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.is_planar "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.is_planar")  | Check if a face is planar or not.  |  
| [`FacePrimitive.logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.logger.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.logger "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.logger")  | Logger.  |  
| [`FacePrimitive.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.name.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.name "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.name")  | Name of the object.  |  
| [`FacePrimitive.normal`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.normal.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.normal "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.normal")  | Face normal.  |  
| [`FacePrimitive.oeditor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.oeditor.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.oeditor "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.oeditor")  | Oeditor Module.  |  
| [`FacePrimitive.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.public_dir.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.public_dir "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.public_dir")  | Shortcut for dir(self).  |  
| [`FacePrimitive.top_edge_x`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_x.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_x "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_x")  | Top edge in the X direction of the object.  |  
| [`FacePrimitive.top_edge_y`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_y.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_y "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_y")  | Top edge in the Y direction of the object.  |  
| [`FacePrimitive.top_edge_z`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_z.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_z "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_z")  | Top edge in the Z direction of the object.  |  
| [`FacePrimitive.touching_objects`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.touching_objects.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.touching_objects "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.touching_objects")  | Get the objects that touch one of the vertex, edge midpoint or the actual face.  |  
| [`FacePrimitive.vertices`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.vertices.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.vertices "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.vertices")  | Vertices lists.  |  
# FacePrimitive 

class ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive(_object3d_ , _obj_id_) 
    
Contains the face object within the AEDT Desktop Modeler. 

Parameters: 
     

**object3d**[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
     

**obj_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import FacePrimitive
>>> obj = FacePrimitive()

```
Copy to clipboard
Methods  
| [`FacePrimitive.create_object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.create_object.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.create_object "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.create_object")([non_model])  | Return a new object from the selected face.  |  
| --- | --- |  
| [`FacePrimitive.is_on_bounding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.is_on_bounding.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.is_on_bounding "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.is_on_bounding")([tolerance])  | Check if the face is on bounding box or Not.  |  
| [`FacePrimitive.move_with_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.move_with_offset.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.move_with_offset "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.move_with_offset")([offset])  | Move the face along the normal.  |  
| [`FacePrimitive.move_with_vector`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.move_with_vector.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.move_with_vector "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.move_with_vector")(vector)  | Move the face along a vector.  |  
Attributes  
| [`FacePrimitive.area`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.area.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.area "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.area")  | Face area.  |  
| --- | --- |  
| [`FacePrimitive.bottom_edge_x`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_x.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_x "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_x")  | Bottom edge in the X direction of the object.  |  
| [`FacePrimitive.bottom_edge_y`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_y.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_y "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_y")  | Bottom edge in the X direction of the object.  |  
| [`FacePrimitive.bottom_edge_z`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_z.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_z "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_z")  | Bottom edge in the Z direction of the object.  |  
| [`FacePrimitive.center`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.center.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.center "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.center")  | Face center in model units.  |  
| [`FacePrimitive.center_from_aedt`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.center_from_aedt.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.center_from_aedt "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.center_from_aedt")  | Face center for a planar face in model units.  |  
| [`FacePrimitive.edges`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.edges.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.edges "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.edges")  | Edges lists.  |  
| [`FacePrimitive.id`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.id.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.id "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.id")  | Face ID.  |  
| [`FacePrimitive.is_planar`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.is_planar.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.is_planar "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.is_planar")  | Check if a face is planar or not.  |  
| [`FacePrimitive.logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.logger.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.logger "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.logger")  | Logger.  |  
| [`FacePrimitive.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.name.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.name "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.name")  | Name of the object.  |  
| [`FacePrimitive.normal`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.normal.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.normal "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.normal")  | Face normal.  |  
| [`FacePrimitive.oeditor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.oeditor.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.oeditor "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.oeditor")  | Oeditor Module.  |  
| [`FacePrimitive.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.public_dir.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.public_dir "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.public_dir")  | Shortcut for dir(self).  |  
| [`FacePrimitive.top_edge_x`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_x.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_x "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_x")  | Top edge in the X direction of the object.  |  
| [`FacePrimitive.top_edge_y`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_y.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_y "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_y")  | Top edge in the Y direction of the object.  |  
| [`FacePrimitive.top_edge_z`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_z.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_z "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_z")  | Top edge in the Z direction of the object.  |  
| [`FacePrimitive.touching_objects`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.touching_objects.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.touching_objects "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.touching_objects")  | Get the objects that touch one of the vertex, edge midpoint or the actual face.  |  
| [`FacePrimitive.vertices`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.vertices.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.vertices "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.vertices")  | Vertices lists.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.rst.txt)

# FacePrimitive 

class ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive(_object3d_ , _obj_id_) 
    
Contains the face object within the AEDT Desktop Modeler. 

Parameters: 
     

**object3d**[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
     

**obj_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import FacePrimitive
>>> obj = FacePrimitive()

```
Copy to clipboard
Methods  
| [`FacePrimitive.create_object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.create_object.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.create_object "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.create_object")([non_model])  | Return a new object from the selected face.  |  
| --- | --- |  
| [`FacePrimitive.is_on_bounding`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.is_on_bounding.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.is_on_bounding "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.is_on_bounding")([tolerance])  | Check if the face is on bounding box or Not.  |  
| [`FacePrimitive.move_with_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.move_with_offset.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.move_with_offset "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.move_with_offset")([offset])  | Move the face along the normal.  |  
| [`FacePrimitive.move_with_vector`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.move_with_vector.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.move_with_vector "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.move_with_vector")(vector)  | Move the face along a vector.  |  
Attributes  
| [`FacePrimitive.area`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.area.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.area "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.area")  | Face area.  |  
| --- | --- |  
| [`FacePrimitive.bottom_edge_x`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_x.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_x "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_x")  | Bottom edge in the X direction of the object.  |  
| [`FacePrimitive.bottom_edge_y`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_y.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_y "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_y")  | Bottom edge in the X direction of the object.  |  
| [`FacePrimitive.bottom_edge_z`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_z.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_z "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.bottom_edge_z")  | Bottom edge in the Z direction of the object.  |  
| [`FacePrimitive.center`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.center.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.center "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.center")  | Face center in model units.  |  
| [`FacePrimitive.center_from_aedt`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.center_from_aedt.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.center_from_aedt "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.center_from_aedt")  | Face center for a planar face in model units.  |  
| [`FacePrimitive.edges`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.edges.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.edges "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.edges")  | Edges lists.  |  
| [`FacePrimitive.id`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.id.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.id "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.id")  | Face ID.  |  
| [`FacePrimitive.is_planar`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.is_planar.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.is_planar "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.is_planar")  | Check if a face is planar or not.  |  
| [`FacePrimitive.logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.logger.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.logger "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.logger")  | Logger.  |  
| [`FacePrimitive.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.name.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.name "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.name")  | Name of the object.  |  
| [`FacePrimitive.normal`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.normal.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.normal "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.normal")  | Face normal.  |  
| [`FacePrimitive.oeditor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.oeditor.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.oeditor "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.oeditor")  | Oeditor Module.  |  
| [`FacePrimitive.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.public_dir.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.public_dir "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.public_dir")  | Shortcut for dir(self).  |  
| [`FacePrimitive.top_edge_x`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_x.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_x "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_x")  | Top edge in the X direction of the object.  |  
| [`FacePrimitive.top_edge_y`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_y.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_y "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_y")  | Top edge in the Y direction of the object.  |  
| [`FacePrimitive.top_edge_z`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_z.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_z "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.top_edge_z")  | Top edge in the Z direction of the object.  |  
| [`FacePrimitive.touching_objects`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.touching_objects.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.touching_objects "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.touching_objects")  | Get the objects that touch one of the vertex, edge midpoint or the actual face.  |  
| [`FacePrimitive.vertices`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.vertices.html#ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.vertices "ansys.aedt.core.modeler.cad.elements_3d.FacePrimitive.vertices")  | Vertices lists.  |