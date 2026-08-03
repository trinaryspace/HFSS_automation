---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.find_largest_rectangle_inside_polygon.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# find_largest_rectangle_inside_polygon 

static GeometryOperators.find_largest_rectangle_inside_polygon(_polygon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _partition_max_order : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 16_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Find the largest area rectangles of arbitrary orientation in a polygon.
Implements the algorithm described by Rubén Molano, et al. _“Finding the largest area rectangle of arbitrary orientation in a closed contour”_ , published in _Applied Mathematics and Computation_. <https://doi.org/10.1016/j.amc.2012.03.063>. (<https://www.sciencedirect.com/science/article/pii/S0096300312003207>) 

Parameters: 
     

**polygon**`List` 
    
[[x1, x2, …, xn],[y1, y2, …, yn]] 

**partition_max_order**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Order of the lattice partition used to find the quasi-lattice polygon that approximates `polygon`. Default is `16`. 

Returns: 
     

`List` `of` `List` 
    
List containing the rectangles points. Return all rectangles found. List is in the form: [[[x1, y1],[x2, y2],…],[[x1, y1],[x2, y2],…],…].
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.find_largest_rectangle_inside_polygon(polygon=["Box1"])

```
Copy to clipboard
# find_largest_rectangle_inside_polygon 

static GeometryOperators.find_largest_rectangle_inside_polygon(_polygon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _partition_max_order : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 16_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Find the largest area rectangles of arbitrary orientation in a polygon.
Implements the algorithm described by Rubén Molano, et al. _“Finding the largest area rectangle of arbitrary orientation in a closed contour”_ , published in _Applied Mathematics and Computation_. <https://doi.org/10.1016/j.amc.2012.03.063>. (<https://www.sciencedirect.com/science/article/pii/S0096300312003207>) 

Parameters: 
     

**polygon**`List` 
    
[[x1, x2, …, xn],[y1, y2, …, yn]] 

**partition_max_order**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Order of the lattice partition used to find the quasi-lattice polygon that approximates `polygon`. Default is `16`. 

Returns: 
     

`List` `of` `List` 
    
List containing the rectangles points. Return all rectangles found. List is in the form: [[[x1, y1],[x2, y2],…],[[x1, y1],[x2, y2],…],…].
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.find_largest_rectangle_inside_polygon(polygon=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.find_largest_rectangle_inside_polygon.rst.txt)

# find_largest_rectangle_inside_polygon 

static GeometryOperators.find_largest_rectangle_inside_polygon(_polygon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _partition_max_order : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 16_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Find the largest area rectangles of arbitrary orientation in a polygon.
Implements the algorithm described by Rubén Molano, et al. _“Finding the largest area rectangle of arbitrary orientation in a closed contour”_ , published in _Applied Mathematics and Computation_. <https://doi.org/10.1016/j.amc.2012.03.063>. (<https://www.sciencedirect.com/science/article/pii/S0096300312003207>) 

Parameters: 
     

**polygon**`List` 
    
[[x1, x2, …, xn],[y1, y2, …, yn]] 

**partition_max_order**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Order of the lattice partition used to find the quasi-lattice polygon that approximates `polygon`. Default is `16`. 

Returns: 
     

`List` `of` `List` 
    
List containing the rectangles points. Return all rectangles found. List is in the form: [[[x1, y1],[x2, y2],…],[[x1, y1],[x2, y2],…],…].
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.find_largest_rectangle_inside_polygon(polygon=["Box1"])

```
Copy to clipboard