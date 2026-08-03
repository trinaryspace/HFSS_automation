---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_rectangle.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_rectangle 

Modeler3D.create_rectangle(_orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Plane](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Plane "ansys.aedt.core.generic.constants.Plane")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _sizes : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _is_covered : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a rectangle. 

Parameters: 
     

**orientation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `Plane` 
    
Coordinate system plane for orienting the rectangle. [`ansys.aedt.core.generic.constants.Plane`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Plane "ansys.aedt.core.generic.constants.Plane") Enumerator can be used as input. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or `Position` 
    
List of `[x, y, z]` coordinates of the lower-left corner of the rectangle or the position ApplicationName.modeler.Position(x,y,z) object. 

**sizes**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[width, height]` dimensions. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the rectangle. The default is `None`, in which case the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. 

**is_covered**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the rectangle is covered. The default is `True`. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object or `False` if it fails.
References

```
>>> oEditor.CreateRectangle

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives_3d import Primitives3D
>>> obj = Primitives3D()
>>> obj.create_rectangle(orientation=1, origin=[0, 0, 0], sizes=["Box1"])

```
Copy to clipboard
# create_rectangle 

Modeler3D.create_rectangle(_orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Plane](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Plane "ansys.aedt.core.generic.constants.Plane")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _sizes : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _is_covered : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a rectangle. 

Parameters: 
     

**orientation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `Plane` 
    
Coordinate system plane for orienting the rectangle. [`ansys.aedt.core.generic.constants.Plane`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Plane "ansys.aedt.core.generic.constants.Plane") Enumerator can be used as input. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or `Position` 
    
List of `[x, y, z]` coordinates of the lower-left corner of the rectangle or the position ApplicationName.modeler.Position(x,y,z) object. 

**sizes**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[width, height]` dimensions. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the rectangle. The default is `None`, in which case the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. 

**is_covered**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the rectangle is covered. The default is `True`. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object or `False` if it fails.
References

```
>>> oEditor.CreateRectangle

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives_3d import Primitives3D
>>> obj = Primitives3D()
>>> obj.create_rectangle(orientation=1, origin=[0, 0, 0], sizes=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_rectangle.rst.txt)

# create_rectangle 

Modeler3D.create_rectangle(_orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [Plane](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Plane "ansys.aedt.core.generic.constants.Plane")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _sizes : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _is_covered : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a rectangle. 

Parameters: 
     

**orientation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `Plane` 
    
Coordinate system plane for orienting the rectangle. [`ansys.aedt.core.generic.constants.Plane`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Plane "ansys.aedt.core.generic.constants.Plane") Enumerator can be used as input. 

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or `Position` 
    
List of `[x, y, z]` coordinates of the lower-left corner of the rectangle or the position ApplicationName.modeler.Position(x,y,z) object. 

**sizes**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[width, height]` dimensions. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the rectangle. The default is `None`, in which case the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. 

**is_covered**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the rectangle is covered. The default is `True`. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object or `False` if it fails.
References

```
>>> oEditor.CreateRectangle

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives_3d import Primitives3D
>>> obj = Primitives3D()
>>> obj.create_rectangle(orientation=1, origin=[0, 0, 0], sizes=["Box1"])

```
Copy to clipboard