---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.get_edgeid_from_position.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# get_edgeid_from_position 

Modeler3D.get_edgeid_from_position(_position : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Get an edge ID from a position. 

Parameters: 
     

**position**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the position. 

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the object. The default is `None`, in which case all objects are searched. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the position, such as `"m"`. The default is `None`, in which case the model units are used. 

Returns: 
     

[`type`](https://docs.python.org/3.11/library/functions.html#type "\(in Python v3.11\)")
    
Edge ID of the first object touching this position.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_edgeid_from_position(position=[0, 0, 0])

```
Copy to clipboard
# get_edgeid_from_position 

Modeler3D.get_edgeid_from_position(_position : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Get an edge ID from a position. 

Parameters: 
     

**position**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the position. 

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the object. The default is `None`, in which case all objects are searched. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the position, such as `"m"`. The default is `None`, in which case the model units are used. 

Returns: 
     

[`type`](https://docs.python.org/3.11/library/functions.html#type "\(in Python v3.11\)")
    
Edge ID of the first object touching this position.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_edgeid_from_position(position=[0, 0, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.get_edgeid_from_position.rst.txt)

# get_edgeid_from_position 

Modeler3D.get_edgeid_from_position(_position : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Get an edge ID from a position. 

Parameters: 
     

**position**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the position. 

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the object. The default is `None`, in which case all objects are searched. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units for the position, such as `"m"`. The default is `None`, in which case the model units are used. 

Returns: 
     

[`type`](https://docs.python.org/3.11/library/functions.html#type "\(in Python v3.11\)")
    
Edge ID of the first object touching this position.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_edgeid_from_position(position=[0, 0, 0])

```
Copy to clipboard