---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_faceted_bondwire_from_true_surface.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_faceted_bondwire_from_true_surface 

Modeler3D.create_faceted_bondwire_from_true_surface(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _direction : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _min_size : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.2_, _number_of_segments : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 8_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a faceted bondwire from an existing true surface bondwire. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the bondwire to replace. 

**direction**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates for the axis direction of the bondwire. For example, `[0, 1, 2]`. 

**min_size**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Minimum size of the subsegment of the new polyline. The default is `0.2`. 

**number_of_segments**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments. The default is `8`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name of the bondwire created.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_faceted_bondwire_from_true_surface(assignment="Box1", direction=[0, 0, 1])

```
Copy to clipboard
# create_faceted_bondwire_from_true_surface 

Modeler3D.create_faceted_bondwire_from_true_surface(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _direction : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _min_size : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.2_, _number_of_segments : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 8_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a faceted bondwire from an existing true surface bondwire. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the bondwire to replace. 

**direction**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates for the axis direction of the bondwire. For example, `[0, 1, 2]`. 

**min_size**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Minimum size of the subsegment of the new polyline. The default is `0.2`. 

**number_of_segments**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments. The default is `8`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name of the bondwire created.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_faceted_bondwire_from_true_surface(assignment="Box1", direction=[0, 0, 1])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_faceted_bondwire_from_true_surface.rst.txt)

# create_faceted_bondwire_from_true_surface 

Modeler3D.create_faceted_bondwire_from_true_surface(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _direction : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _min_size : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.2_, _number_of_segments : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 8_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a faceted bondwire from an existing true surface bondwire. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the bondwire to replace. 

**direction**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates for the axis direction of the bondwire. For example, `[0, 1, 2]`. 

**min_size**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Minimum size of the subsegment of the new polyline. The default is `0.2`. 

**number_of_segments**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments. The default is `8`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Name of the bondwire created.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_faceted_bondwire_from_true_surface(assignment="Box1", direction=[0, 0, 1])

```
Copy to clipboard