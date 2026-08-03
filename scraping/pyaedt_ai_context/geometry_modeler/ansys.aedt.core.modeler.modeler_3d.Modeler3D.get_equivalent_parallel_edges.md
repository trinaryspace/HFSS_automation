---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.get_equivalent_parallel_edges.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# get_equivalent_parallel_edges 

Modeler3D.get_equivalent_parallel_edges(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _port_on_plane : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _start_object : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _end_object : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Create two new edges that are parallel and equal to the smallest edge given a parallel couple of edges. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of two parallel edges. 

**port_on_plane**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether edges are to be on the plane orthogonal to the axis direction. The default is `True`. 

**axis**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Axis direction. Choices are `0` through `5`. The default is `0`. 

**start_object**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the starting object. The default is `""`. 

**end_object**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the ending object. The default is `""`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of two created edges.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_equivalent_parallel_edges(assignment="Box1")

```
Copy to clipboard
# get_equivalent_parallel_edges 

Modeler3D.get_equivalent_parallel_edges(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _port_on_plane : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _start_object : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _end_object : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Create two new edges that are parallel and equal to the smallest edge given a parallel couple of edges. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of two parallel edges. 

**port_on_plane**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether edges are to be on the plane orthogonal to the axis direction. The default is `True`. 

**axis**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Axis direction. Choices are `0` through `5`. The default is `0`. 

**start_object**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the starting object. The default is `""`. 

**end_object**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the ending object. The default is `""`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of two created edges.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_equivalent_parallel_edges(assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.get_equivalent_parallel_edges.rst.txt)

# get_equivalent_parallel_edges 

Modeler3D.get_equivalent_parallel_edges(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _port_on_plane : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _start_object : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _end_object : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Create two new edges that are parallel and equal to the smallest edge given a parallel couple of edges. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of two parallel edges. 

**port_on_plane**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether edges are to be on the plane orthogonal to the axis direction. The default is `True`. 

**axis**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Axis direction. Choices are `0` through `5`. The default is `0`. 

**start_object**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the starting object. The default is `""`. 

**end_object**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the ending object. The default is `""`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of two created edges.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_equivalent_parallel_edges(assignment="Box1")

```
Copy to clipboard