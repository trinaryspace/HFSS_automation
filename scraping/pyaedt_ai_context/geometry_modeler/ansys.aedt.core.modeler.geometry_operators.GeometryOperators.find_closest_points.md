---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.find_closest_points.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# find_closest_points 

static GeometryOperators.find_closest_points(_points_list : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _reference_point : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-06_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Given a list of points, finds the closest points to a reference point. It returns a list of points because more than one can be found. It works with 2D or 3D points. The tolerance used to evaluate the distance to the reference point can be specified. 

Parameters: 
     

**points_list**`List` `of` `List` 
    
List of points. The points can be defined in 2D or 3D space. 

**reference_point**`List` 
    
The reference point. The point can be defined in 2D or 3D space (same as points_list). 

**tol**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
The tolerance used to evaluate the distance. Default is `1e-6`. 

Returns: 
     

`List` `of` `List` 
    
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.find_closest_points(points_list=[0, 0, 0], reference_point=[0, 0, 0])

```
Copy to clipboard
# find_closest_points 

static GeometryOperators.find_closest_points(_points_list : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _reference_point : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-06_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Given a list of points, finds the closest points to a reference point. It returns a list of points because more than one can be found. It works with 2D or 3D points. The tolerance used to evaluate the distance to the reference point can be specified. 

Parameters: 
     

**points_list**`List` `of` `List` 
    
List of points. The points can be defined in 2D or 3D space. 

**reference_point**`List` 
    
The reference point. The point can be defined in 2D or 3D space (same as points_list). 

**tol**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
The tolerance used to evaluate the distance. Default is `1e-6`. 

Returns: 
     

`List` `of` `List` 
    
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.find_closest_points(points_list=[0, 0, 0], reference_point=[0, 0, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.geometry_operators.GeometryOperators.find_closest_points.rst.txt)

# find_closest_points 

static GeometryOperators.find_closest_points(_points_list : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _reference_point : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tol : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-06_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Given a list of points, finds the closest points to a reference point. It returns a list of points because more than one can be found. It works with 2D or 3D points. The tolerance used to evaluate the distance to the reference point can be specified. 

Parameters: 
     

**points_list**`List` `of` `List` 
    
List of points. The points can be defined in 2D or 3D space. 

**reference_point**`List` 
    
The reference point. The point can be defined in 2D or 3D space (same as points_list). 

**tol**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
The tolerance used to evaluate the distance. Default is `1e-6`. 

Returns: 
     

`List` `of` `List` 
    
Examples

```
>>> from ansys.aedt.core.modeler.geometry_operators import GeometryOperators
>>> obj = GeometryOperators()
>>> obj.find_closest_points(points_list=[0, 0, 0], reference_point=[0, 0, 0])

```
Copy to clipboard