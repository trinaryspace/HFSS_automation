---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.is_point_in_polygon.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# is_point_in_polygon 

static GeometryOperators.is_point_in_polygon(_point : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _polygon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Determine if a point is inside or outside a polygon, both located on the same plane.
The method implements the radial algorithm (<https://es.wikipedia.org/wiki/Algoritmo_radial>) 

pointList 
    
List of `[x, y]` coordinates. 

polygonList 
    
[[x1, x2, …, xn],[y1, y2, …, yn]] 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the point is inside the polygon or exactly on one of its sides. `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_point_in_polygon(point=[0, 0, 0], polygon=["Box1"])

```
Copy to clipboard
# is_point_in_polygon 

static GeometryOperators.is_point_in_polygon(_point : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _polygon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Determine if a point is inside or outside a polygon, both located on the same plane.
The method implements the radial algorithm (<https://es.wikipedia.org/wiki/Algoritmo_radial>) 

pointList 
    
List of `[x, y]` coordinates. 

polygonList 
    
[[x1, x2, …, xn],[y1, y2, …, yn]] 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the point is inside the polygon or exactly on one of its sides. `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_point_in_polygon(point=[0, 0, 0], polygon=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.is_point_in_polygon.rst.txt)

# is_point_in_polygon 

static GeometryOperators.is_point_in_polygon(_point : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _polygon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Determine if a point is inside or outside a polygon, both located on the same plane.
The method implements the radial algorithm (<https://es.wikipedia.org/wiki/Algoritmo_radial>) 

pointList 
    
List of `[x, y]` coordinates. 

polygonList 
    
[[x1, x2, …, xn],[y1, y2, …, yn]] 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if the point is inside the polygon or exactly on one of its sides. `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.is_point_in_polygon(point=[0, 0, 0], polygon=["Box1"])

```
Copy to clipboard