---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.point_in_polygon.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# point_in_polygon 

static GeometryOperators.point_in_polygon(_point : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _polygon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-08_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Determine if a point is inside, outside the polygon or at exactly at the border.
The method implements the radial algorithm (<https://es.wikipedia.org/wiki/Algoritmo_radial>)
This version supports also self-intersecting polygons. 

pointList 
    
List of `[x, y]` coordinates. 

polygonList 
    
[[x1, x2, …, xn],[y1, y2, …, yn]] 

tolerancefloat 
    
tolerance used for the algorithm. Default value is 1e-8. 

Returns: 
     

[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")
    
  * `-1` When the point is outside the polygon.
  * `0` When the point is exactly on one of the sides of the polygon.
  * `1` When the point is inside the polygon.

Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.point_in_polygon(point=[0, 0, 0], polygon=["Box1"])

```
Copy to clipboard
# point_in_polygon 

static GeometryOperators.point_in_polygon(_point : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _polygon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-08_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Determine if a point is inside, outside the polygon or at exactly at the border.
The method implements the radial algorithm (<https://es.wikipedia.org/wiki/Algoritmo_radial>)
This version supports also self-intersecting polygons. 

pointList 
    
List of `[x, y]` coordinates. 

polygonList 
    
[[x1, x2, …, xn],[y1, y2, …, yn]] 

tolerancefloat 
    
tolerance used for the algorithm. Default value is 1e-8. 

Returns: 
     

[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")
    
  * `-1` When the point is outside the polygon.
  * `0` When the point is exactly on one of the sides of the polygon.
  * `1` When the point is inside the polygon.

Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.point_in_polygon(point=[0, 0, 0], polygon=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.point_in_polygon.rst.txt)

# point_in_polygon 

static GeometryOperators.point_in_polygon(_point : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _polygon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-08_) → [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Determine if a point is inside, outside the polygon or at exactly at the border.
The method implements the radial algorithm (<https://es.wikipedia.org/wiki/Algoritmo_radial>)
This version supports also self-intersecting polygons. 

pointList 
    
List of `[x, y]` coordinates. 

polygonList 
    
[[x1, x2, …, xn],[y1, y2, …, yn]] 

tolerancefloat 
    
tolerance used for the algorithm. Default value is 1e-8. 

Returns: 
     

[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")
    
  * `-1` When the point is outside the polygon.
  * `0` When the point is exactly on one of the sides of the polygon.
  * `1` When the point is inside the polygon.

Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.point_in_polygon(point=[0, 0, 0], polygon=["Box1"])

```
Copy to clipboard