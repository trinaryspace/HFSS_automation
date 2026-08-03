---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.find_closest_edges.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# find_closest_edges 

Modeler3D.find_closest_edges(_start_object : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _end_object : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _direction : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve the two closest edges that are not perpendicular for two objects. 

Parameters: 
     

**start_object**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the starting object. 

**end_object**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the ending object. 

**direction**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Direction of the port to which to give edges precedence when more than two couples are at the same distance. For example, for a coax or microstrip, precedence is given to the edges that are on the given axis direction, such as `"XNeg"`. Options are `"XNeg"`, `"XPos"`, `"YNeg"`, `"YPos`"`, `"ZNeg"`, and `"ZPos"`. The default is `0`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List with two edges if present.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.find_closest_edges(start_object=1, end_object=1)

```
Copy to clipboard
# find_closest_edges 

Modeler3D.find_closest_edges(_start_object : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _end_object : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _direction : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve the two closest edges that are not perpendicular for two objects. 

Parameters: 
     

**start_object**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the starting object. 

**end_object**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the ending object. 

**direction**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Direction of the port to which to give edges precedence when more than two couples are at the same distance. For example, for a coax or microstrip, precedence is given to the edges that are on the given axis direction, such as `"XNeg"`. Options are `"XNeg"`, `"XPos"`, `"YNeg"`, `"YPos`"`, `"ZNeg"`, and `"ZPos"`. The default is `0`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List with two edges if present.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.find_closest_edges(start_object=1, end_object=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.find_closest_edges.rst.txt)

# find_closest_edges 

Modeler3D.find_closest_edges(_start_object : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _end_object : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _direction : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve the two closest edges that are not perpendicular for two objects. 

Parameters: 
     

**start_object**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the starting object. 

**end_object**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the ending object. 

**direction**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Direction of the port to which to give edges precedence when more than two couples are at the same distance. For example, for a coax or microstrip, precedence is given to the edges that are on the given axis direction, such as `"XNeg"`. Options are `"XNeg"`, `"XPos"`, `"YNeg"`, `"YPos`"`, `"ZNeg"`, and `"ZPos"`. The default is `0`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List with two edges if present.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.find_closest_edges(start_object=1, end_object=1)

```
Copy to clipboard