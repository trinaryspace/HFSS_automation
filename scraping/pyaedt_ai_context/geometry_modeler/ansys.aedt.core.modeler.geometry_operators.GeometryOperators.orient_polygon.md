---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.orient_polygon.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# orient_polygon 

static GeometryOperators.orient_polygon(_x : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _y : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _clockwise : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")] 
    
Orient a polygon clockwise or counterclockwise.
The vertices should be already ordered either way. Use this function to change the orientation. The polygon is represented by its vertices coordinates. 

Parameters: 
     

**x**`List` 
    
List of x coordinates of the vertices. Length must be >= 1. Degenerate polygon with only 2 points is also accepted, in this case the points are returned unchanged. 

**y**`List` 
    
List of y coordinates of the vertices. Must be of the same length as x. 

**clockwise**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
If `True` the polygon is oriented clockwise, if `False` it is oriented counterclockwise. Default is `True`. 

Returns: 
     

`List` `of` `List` 
    
Lists of oriented vertices.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.orient_polygon(x=0, y=0)

```
Copy to clipboard
# orient_polygon 

static GeometryOperators.orient_polygon(_x : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _y : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _clockwise : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")] 
    
Orient a polygon clockwise or counterclockwise.
The vertices should be already ordered either way. Use this function to change the orientation. The polygon is represented by its vertices coordinates. 

Parameters: 
     

**x**`List` 
    
List of x coordinates of the vertices. Length must be >= 1. Degenerate polygon with only 2 points is also accepted, in this case the points are returned unchanged. 

**y**`List` 
    
List of y coordinates of the vertices. Must be of the same length as x. 

**clockwise**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
If `True` the polygon is oriented clockwise, if `False` it is oriented counterclockwise. Default is `True`. 

Returns: 
     

`List` `of` `List` 
    
Lists of oriented vertices.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.orient_polygon(x=0, y=0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.orient_polygon.rst.txt)

# orient_polygon 

static GeometryOperators.orient_polygon(_x : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _y : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _clockwise : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")] 
    
Orient a polygon clockwise or counterclockwise.
The vertices should be already ordered either way. Use this function to change the orientation. The polygon is represented by its vertices coordinates. 

Parameters: 
     

**x**`List` 
    
List of x coordinates of the vertices. Length must be >= 1. Degenerate polygon with only 2 points is also accepted, in this case the points are returned unchanged. 

**y**`List` 
    
List of y coordinates of the vertices. Must be of the same length as x. 

**clockwise**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
If `True` the polygon is oriented clockwise, if `False` it is oriented counterclockwise. Default is `True`. 

Returns: 
     

`List` `of` `List` 
    
Lists of oriented vertices.
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.orient_polygon(x=0, y=0)

```
Copy to clipboard