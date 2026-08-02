---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.polyline_segment.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# polyline_segment 

Modeler2D.polyline_segment(_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _num_seg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _num_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _arc_angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _arc_center : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _arc_plane : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_) → [PolylineSegment](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.PolylineSegment.html#ansys.aedt.core.modeler.cad.polylines.PolylineSegment "ansys.aedt.core.modeler.cad.object_3d.PolylineSegment") 
    
New segment of a polyline. 

Parameters: 
     

**type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the object. Choices are `"Line"`, `"Arc"`, `"Spline"`, and `"AngularArc"`. 

**num_seg**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments for the types `"Arc"`, `"Spline"`, and `"AngularArc"`. The default is `0`. For the type `Line`, this parameter is ignored. 

**num_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of control points for the type `Spline`. For other types, this parameter is defined automatically. 

**arc_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Sweep angle in radians or a valid value string. For example, `"35deg"` or `"Specific to type AngularArc"`. 

**arc_center**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
List of values in model units or a valid value string. For example, a list of `[x, y, z]` coordinates or `"Specific to type AngularArc"`. 

**arc_plane**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") `optional` 
    
Plane in which the arc sweep is performed in the active coordinate system `"XY"`, `"YZ"` or `"ZX"`. The default is `None`, in which case the plane is determined automatically by the first coordinate for which the starting point and center point have the same value. 

Returns: 
     

`ansys.aedt.core.modeler.polylines.PolylineSegment`
    
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.polyline_segment(type=1)

```
Copy to clipboard
# polyline_segment 

Modeler2D.polyline_segment(_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _num_seg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _num_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _arc_angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _arc_center : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _arc_plane : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_) → [PolylineSegment](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.PolylineSegment.html#ansys.aedt.core.modeler.cad.polylines.PolylineSegment "ansys.aedt.core.modeler.cad.object_3d.PolylineSegment") 
    
New segment of a polyline. 

Parameters: 
     

**type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the object. Choices are `"Line"`, `"Arc"`, `"Spline"`, and `"AngularArc"`. 

**num_seg**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments for the types `"Arc"`, `"Spline"`, and `"AngularArc"`. The default is `0`. For the type `Line`, this parameter is ignored. 

**num_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of control points for the type `Spline`. For other types, this parameter is defined automatically. 

**arc_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Sweep angle in radians or a valid value string. For example, `"35deg"` or `"Specific to type AngularArc"`. 

**arc_center**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
List of values in model units or a valid value string. For example, a list of `[x, y, z]` coordinates or `"Specific to type AngularArc"`. 

**arc_plane**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") `optional` 
    
Plane in which the arc sweep is performed in the active coordinate system `"XY"`, `"YZ"` or `"ZX"`. The default is `None`, in which case the plane is determined automatically by the first coordinate for which the starting point and center point have the same value. 

Returns: 
     

`ansys.aedt.core.modeler.polylines.PolylineSegment`
    
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.polyline_segment(type=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.polyline_segment.rst.txt)

# polyline_segment 

Modeler2D.polyline_segment(_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _num_seg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _num_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _arc_angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _arc_center : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _arc_plane : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_) → [PolylineSegment](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.PolylineSegment.html#ansys.aedt.core.modeler.cad.polylines.PolylineSegment "ansys.aedt.core.modeler.cad.object_3d.PolylineSegment") 
    
New segment of a polyline. 

Parameters: 
     

**type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the object. Choices are `"Line"`, `"Arc"`, `"Spline"`, and `"AngularArc"`. 

**num_seg**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments for the types `"Arc"`, `"Spline"`, and `"AngularArc"`. The default is `0`. For the type `Line`, this parameter is ignored. 

**num_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of control points for the type `Spline`. For other types, this parameter is defined automatically. 

**arc_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Sweep angle in radians or a valid value string. For example, `"35deg"` or `"Specific to type AngularArc"`. 

**arc_center**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
List of values in model units or a valid value string. For example, a list of `[x, y, z]` coordinates or `"Specific to type AngularArc"`. 

**arc_plane**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") `optional` 
    
Plane in which the arc sweep is performed in the active coordinate system `"XY"`, `"YZ"` or `"ZX"`. The default is `None`, in which case the plane is determined automatically by the first coordinate for which the starting point and center point have the same value. 

Returns: 
     

`ansys.aedt.core.modeler.polylines.PolylineSegment`
    
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.polyline_segment(type=1)

```
Copy to clipboard