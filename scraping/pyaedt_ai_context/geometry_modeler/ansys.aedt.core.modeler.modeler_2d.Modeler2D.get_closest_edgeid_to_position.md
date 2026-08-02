---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.get_closest_edgeid_to_position.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# get_closest_edgeid_to_position 

Modeler2D.get_closest_edgeid_to_position(_position : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Get the edge ID closest to a given position. 

Parameters: 
     

**position**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x,y,z]` coordinates for the position. 

**units**
    
Units for the position, such as `"m"`. The default is `None`, which means the model units are used. 

Returns: 
     

[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")
    
Edge ID of the edge closest to this position.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_closest_edgeid_to_position(position=[0, 0, 0])

```
Copy to clipboard
# get_closest_edgeid_to_position 

Modeler2D.get_closest_edgeid_to_position(_position : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Get the edge ID closest to a given position. 

Parameters: 
     

**position**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x,y,z]` coordinates for the position. 

**units**
    
Units for the position, such as `"m"`. The default is `None`, which means the model units are used. 

Returns: 
     

[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")
    
Edge ID of the edge closest to this position.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_closest_edgeid_to_position(position=[0, 0, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.get_closest_edgeid_to_position.rst.txt)

# get_closest_edgeid_to_position 

Modeler2D.get_closest_edgeid_to_position(_position : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Get the edge ID closest to a given position. 

Parameters: 
     

**position**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x,y,z]` coordinates for the position. 

**units**
    
Units for the position, such as `"m"`. The default is `None`, which means the model units are used. 

Returns: 
     

[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")
    
Edge ID of the edge closest to this position.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_closest_edgeid_to_position(position=[0, 0, 0])

```
Copy to clipboard