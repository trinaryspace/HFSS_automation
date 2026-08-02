---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# VertexPrimitive 

class ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive(_object3d_ , _objid_ , _position =None_) 
    
Contains the vertex object within the AEDT Desktop Modeler. 

Parameters: 
     

**object3d**[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Pointer to the calling object that provides additional functionality. 

**objid**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Object ID as determined by the parent object.
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import VertexPrimitive
>>> obj = VertexPrimitive()

```
Copy to clipboard
Methods  
| [`VertexPrimitive.chamfer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.chamfer.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.chamfer "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.chamfer")([left_distance, ...])  | Add a chamfer to the selected edges in 3D/vertices in 2D.  |  
| --- | --- |  
| [`VertexPrimitive.fillet`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.fillet.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.fillet "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.fillet")([radius, setback])  | Add a fillet to the selected edges in 3D/vertices in 2D.  |  
Attributes  
| [`VertexPrimitive.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.name.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.name "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.name")  | Name of the object.  |  
| --- | --- |  
| [`VertexPrimitive.position`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.position.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.position "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.position")  | Position of the vertex.  |  
| [`VertexPrimitive.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.public_dir.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.public_dir "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.public_dir")  | Shortcut for dir(self).  |  
# VertexPrimitive 

class ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive(_object3d_ , _objid_ , _position =None_) 
    
Contains the vertex object within the AEDT Desktop Modeler. 

Parameters: 
     

**object3d**[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Pointer to the calling object that provides additional functionality. 

**objid**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Object ID as determined by the parent object.
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import VertexPrimitive
>>> obj = VertexPrimitive()

```
Copy to clipboard
Methods  
| [`VertexPrimitive.chamfer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.chamfer.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.chamfer "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.chamfer")([left_distance, ...])  | Add a chamfer to the selected edges in 3D/vertices in 2D.  |  
| --- | --- |  
| [`VertexPrimitive.fillet`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.fillet.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.fillet "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.fillet")([radius, setback])  | Add a fillet to the selected edges in 3D/vertices in 2D.  |  
Attributes  
| [`VertexPrimitive.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.name.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.name "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.name")  | Name of the object.  |  
| --- | --- |  
| [`VertexPrimitive.position`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.position.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.position "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.position")  | Position of the vertex.  |  
| [`VertexPrimitive.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.public_dir.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.public_dir "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.rst.txt)

# VertexPrimitive 

class ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive(_object3d_ , _objid_ , _position =None_) 
    
Contains the vertex object within the AEDT Desktop Modeler. 

Parameters: 
     

**object3d**[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Pointer to the calling object that provides additional functionality. 

**objid**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Object ID as determined by the parent object.
Examples

```
>>> from ansys.aedt.core.modeler.cad.elements_3d import VertexPrimitive
>>> obj = VertexPrimitive()

```
Copy to clipboard
Methods  
| [`VertexPrimitive.chamfer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.chamfer.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.chamfer "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.chamfer")([left_distance, ...])  | Add a chamfer to the selected edges in 3D/vertices in 2D.  |  
| --- | --- |  
| [`VertexPrimitive.fillet`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.fillet.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.fillet "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.fillet")([radius, setback])  | Add a fillet to the selected edges in 3D/vertices in 2D.  |  
Attributes  
| [`VertexPrimitive.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.name.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.name "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.name")  | Name of the object.  |  
| --- | --- |  
| [`VertexPrimitive.position`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.position.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.position "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.position")  | Position of the vertex.  |  
| [`VertexPrimitive.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.public_dir.html#ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.public_dir "ansys.aedt.core.modeler.cad.elements_3d.VertexPrimitive.public_dir")  | Shortcut for dir(self).  |