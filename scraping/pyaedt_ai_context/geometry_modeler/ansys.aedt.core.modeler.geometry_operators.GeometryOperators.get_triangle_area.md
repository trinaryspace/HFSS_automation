---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.get_triangle_area.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# get_triangle_area 

static GeometryOperators.get_triangle_area(_v1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _v2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _v3 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Evaluate the area of a triangle defined by its three vertices. 

Parameters: 
     

**v1**`List` 
    
List of `[x, y, z]` coordinates for the first vertex. 

**v2**`List` 
    
List of `[x, y, z]` coordinates for the second vertex. 

**v3**`List` 
    
List of `[x, y, z]` coordinates for the third vertex. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Area of the triangle.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.get_triangle_area(v1=[0, 0, 0], v2=[10, 0, 0], v3=[0, 10, 0])

```
Copy to clipboard
# get_triangle_area 

static GeometryOperators.get_triangle_area(_v1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _v2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _v3 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Evaluate the area of a triangle defined by its three vertices. 

Parameters: 
     

**v1**`List` 
    
List of `[x, y, z]` coordinates for the first vertex. 

**v2**`List` 
    
List of `[x, y, z]` coordinates for the second vertex. 

**v3**`List` 
    
List of `[x, y, z]` coordinates for the third vertex. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Area of the triangle.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.get_triangle_area(v1=[0, 0, 0], v2=[10, 0, 0], v3=[0, 10, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.get_triangle_area.rst.txt)

# get_triangle_area 

static GeometryOperators.get_triangle_area(_v1 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _v2 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _v3 : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Evaluate the area of a triangle defined by its three vertices. 

Parameters: 
     

**v1**`List` 
    
List of `[x, y, z]` coordinates for the first vertex. 

**v2**`List` 
    
List of `[x, y, z]` coordinates for the second vertex. 

**v3**`List` 
    
List of `[x, y, z]` coordinates for the third vertex. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Area of the triangle.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.get_triangle_area(v1=[0, 0, 0], v2=[10, 0, 0], v3=[0, 10, 0])

```
Copy to clipboard