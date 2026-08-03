---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_polyline.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_polyline 

Modeler3D.create_polyline(_points : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _segment_type : [PolylineSegment](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.PolylineSegment.html#ansys.aedt.core.modeler.cad.polylines.PolylineSegment "ansys.aedt.core.modeler.cad.object_3d.PolylineSegment") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _cover_surface : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _close_surface : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _xsection_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _xsection_orient : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _xsection_width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _xsection_topwidth : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _xsection_height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _xsection_num_seg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _xsection_bend_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _non_model : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [Polyline](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.Polyline.html#ansys.aedt.core.modeler.cad.polylines.Polyline "ansys.aedt.core.modeler.cad.polylines.Polyline") 
    
Draw a polyline object in the 3D modeler.
This method retrieves the `ansys.aedt.core.modeler.cad.primitives.Polyline` object, which has additional methods for manipulating the polyline. For example, you can use `ansys.aedt.core.modeler.cad.primitives.Polyline.insert_segment()` to insert a segment or `ansys.aedt.core.modeler.cad.primitives.Polyline.id` to retrieve the ID of the polyline object. 

Parameters: 
     

**points**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Array of positions of each point of the polyline. A position is a list of 2D or 3D coordinates. Position coordinate values can be numbers or valid AEDT string expressions. For example, `[0, 1, 2]`, `["0mm", "5mm", "1mm"]`, or `["x1", "y1", "z1"]`. 

**segment_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or `PolylineSegment` or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
The default behavior is to connect all points as `"Line"` segments. The default is `None`. Use a `"PolylineSegment"`, for `"Line"`, `"Arc"`, `"Spline"`, or `"AngularArc"`. A list of segment types (str or `ansys.aedt.core.modeler.cad.primitives.PolylineSegment`) is valid for a compound polyline. 

**cover_surface**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `False`. 

**close_surface**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `False`, which automatically joins the starting and ending points. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the polyline. The default is `None`. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. 

**xsection_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the cross-section. Options are `"Line"`, `"Circle"`, `"Rectangle"`, and `"Isosceles Trapezoid"`. The default is `None`. 

**xsection_orient**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Direction of the normal vector to the width of the cross-section. Options are `"X"`, `"Y"`, `"Z"`, and `"Auto"`. The default is `None`, which sets the direction to `"Auto"`. 

**xsection_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Width or diameter of the cross-section for all types. The default is `1`. 

**xsection_topwidth**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Top width of the cross-section for type `"Isosceles Trapezoid"` only. The default is `1`. 

**xsection_height**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Height of the cross-section for type `"Rectangle"` or `"Isosceles Trapezoid"` only. The default is `1`. 

**xsection_num_seg**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments in the cross-section surface for type `"Circle"`, `"Rectangle"`, or `"Isosceles Trapezoid"`. The default is `0`. The value must be `0` or greater than `2`. 

**xsection_bend_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the bend for the cross-section. The default is `None`, in which case the bend type is set to `"Corner"`. For the type `"Circle"`, the bend type should be set to `"Curved"`. 

**non_model**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if the polyline will be created as model or unmodel object. 

Returns: 
     

`ansys.aedt.core.modeler.polylines.Polyline`
    
Polyline object.
References

```
>>> oEditor.CreatePolyline

```
Copy to clipboard
Examples
Set up the desktop environment.

```
>>> from ansys.aedt.core.modeler.cad.polylines import PolylineSegment
>>> from ansys.aedt.core import Desktop
>>> from ansys.aedt.core import Maxwell3d
>>> desktop = Desktop(version="2026.1", new_desktop=False)
>>> m3d = Maxwell3d()
>>> m3d.modeler.model_units = "mm"

```
Copy to clipboard
Define some test data points.

```
>>> test_points = [
...     ["0mm", "0mm", "0mm"],
...     ["100mm", "20mm", "0mm"],
...     ["71mm", "71mm", "0mm"],
...     ["0mm", "100mm", "0mm"],
... ]

```
Copy to clipboard
The default behavior assumes that all points are to be connected by line segments. Optionally specify the name.

```
>>> P1 = m3d.modeler.create_polyline(test_points, name="PL_line_segments")

```
Copy to clipboard
Specify that the first segment is a line and the last three points define a three-point arc.

```
>>> P2 = m3d.modeler.create_polyline(test_points, segment_type=["Line", "Arc"], name="PL_line_plus_arc")

```
Copy to clipboard
Redraw the 3-point arc alone from the last three points and additionally specify five segments using `PolylineSegment`.

```
>>> P3 = m3d.modeler.create_polyline(
...     test_points[1:], segment_type=PolylineSegment(segment_type="Arc", num_seg=7), name="PL_segmented_arc"
... )

```
Copy to clipboard
Specify that the four points form a spline and add a circular cross-section with a diameter of 1 mm.

```
>>> P4 = m3d.modeler.create_polyline(
...     test_points, segment_type="Spline", name="PL_spline", xsection_type="Circle", xsection_width="1mm"
... )

```
Copy to clipboard
Use the `PolylineSegment` object to specify more detail about the individual segments. Create a center point arc starting from the position `test_points[1]`, rotating about the center point position `test_points[0]` in the XY plane.

```
>>> start_point = test_points[1]
>>> center_point = test_points[0]
>>> segment_def = PolylineSegment(
...     segment_type="AngularArc", arc_center=center_point, arc_angle="90deg", arc_plane="XY"
... )
>>> m3d.modeler.create_polyline(start_point, segment_type=segment_def, name="PL_center_point_arc")

```
Copy to clipboard
Create a spline using a list of variables for the coordinates of the points.

```
>>> x0, y0, z0 = "0", "0", "1"
>>> x1, y1, z1 = "1", "3", "1"
>>> x2, y2, z2 = "2", "2", "1"
>>> P5 = m3d.modeler.create_polyline(
...     points=[[x0, y0, z0], [x1, y1, z1], [x2, y2, z2]], segment_type="Spline", name="polyline_with_variables"
... )

```
Copy to clipboard
Create a closed geometry by specifying in `segment_type` a list of `PolylineSegments` including `AngularArc` segments.

```
>>> test_points_1 = [[0.4, 0, 0], [-0.4, -0.6, 0], [0.4, 0, 0]]
>>> P6 = m3d.modeler.create_polyline(
...     points=test_points_1,
...     segment_type=[
...         PolylineSegment(
...             segment_type="AngularArc", arc_center=[0, 0, 0], arc_angle="180deg", arc_plane="XY"
...         ),
...         PolylineSegment(segment_type="Line"),
...         PolylineSegment(
...             segment_type="AngularArc", arc_center=[0, -0.6, 0], arc_angle="180deg", arc_plane="XY"
...         ),
...         PolylineSegment(segment_type="Line"),
...     ],
... )

```
Copy to clipboard
# create_polyline 

Modeler3D.create_polyline(_points : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _segment_type : [PolylineSegment](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.PolylineSegment.html#ansys.aedt.core.modeler.cad.polylines.PolylineSegment "ansys.aedt.core.modeler.cad.object_3d.PolylineSegment") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _cover_surface : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _close_surface : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _xsection_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _xsection_orient : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _xsection_width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _xsection_topwidth : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _xsection_height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _xsection_num_seg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _xsection_bend_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _non_model : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [Polyline](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.Polyline.html#ansys.aedt.core.modeler.cad.polylines.Polyline "ansys.aedt.core.modeler.cad.polylines.Polyline") 
    
Draw a polyline object in the 3D modeler.
This method retrieves the `ansys.aedt.core.modeler.cad.primitives.Polyline` object, which has additional methods for manipulating the polyline. For example, you can use `ansys.aedt.core.modeler.cad.primitives.Polyline.insert_segment()` to insert a segment or `ansys.aedt.core.modeler.cad.primitives.Polyline.id` to retrieve the ID of the polyline object. 

Parameters: 
     

**points**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Array of positions of each point of the polyline. A position is a list of 2D or 3D coordinates. Position coordinate values can be numbers or valid AEDT string expressions. For example, `[0, 1, 2]`, `["0mm", "5mm", "1mm"]`, or `["x1", "y1", "z1"]`. 

**segment_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or `PolylineSegment` or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
The default behavior is to connect all points as `"Line"` segments. The default is `None`. Use a `"PolylineSegment"`, for `"Line"`, `"Arc"`, `"Spline"`, or `"AngularArc"`. A list of segment types (str or `ansys.aedt.core.modeler.cad.primitives.PolylineSegment`) is valid for a compound polyline. 

**cover_surface**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `False`. 

**close_surface**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `False`, which automatically joins the starting and ending points. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the polyline. The default is `None`. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. 

**xsection_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the cross-section. Options are `"Line"`, `"Circle"`, `"Rectangle"`, and `"Isosceles Trapezoid"`. The default is `None`. 

**xsection_orient**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Direction of the normal vector to the width of the cross-section. Options are `"X"`, `"Y"`, `"Z"`, and `"Auto"`. The default is `None`, which sets the direction to `"Auto"`. 

**xsection_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Width or diameter of the cross-section for all types. The default is `1`. 

**xsection_topwidth**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Top width of the cross-section for type `"Isosceles Trapezoid"` only. The default is `1`. 

**xsection_height**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Height of the cross-section for type `"Rectangle"` or `"Isosceles Trapezoid"` only. The default is `1`. 

**xsection_num_seg**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments in the cross-section surface for type `"Circle"`, `"Rectangle"`, or `"Isosceles Trapezoid"`. The default is `0`. The value must be `0` or greater than `2`. 

**xsection_bend_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the bend for the cross-section. The default is `None`, in which case the bend type is set to `"Corner"`. For the type `"Circle"`, the bend type should be set to `"Curved"`. 

**non_model**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if the polyline will be created as model or unmodel object. 

Returns: 
     

`ansys.aedt.core.modeler.polylines.Polyline`
    
Polyline object.
References

```
>>> oEditor.CreatePolyline

```
Copy to clipboard
Examples
Set up the desktop environment.

```
>>> from ansys.aedt.core.modeler.cad.polylines import PolylineSegment
>>> from ansys.aedt.core import Desktop
>>> from ansys.aedt.core import Maxwell3d
>>> desktop = Desktop(version="2026.1", new_desktop=False)
>>> m3d = Maxwell3d()
>>> m3d.modeler.model_units = "mm"

```
Copy to clipboard
Define some test data points.

```
>>> test_points = [
...     ["0mm", "0mm", "0mm"],
...     ["100mm", "20mm", "0mm"],
...     ["71mm", "71mm", "0mm"],
...     ["0mm", "100mm", "0mm"],
... ]

```
Copy to clipboard
The default behavior assumes that all points are to be connected by line segments. Optionally specify the name.

```
>>> P1 = m3d.modeler.create_polyline(test_points, name="PL_line_segments")

```
Copy to clipboard
Specify that the first segment is a line and the last three points define a three-point arc.

```
>>> P2 = m3d.modeler.create_polyline(test_points, segment_type=["Line", "Arc"], name="PL_line_plus_arc")

```
Copy to clipboard
Redraw the 3-point arc alone from the last three points and additionally specify five segments using `PolylineSegment`.

```
>>> P3 = m3d.modeler.create_polyline(
...     test_points[1:], segment_type=PolylineSegment(segment_type="Arc", num_seg=7), name="PL_segmented_arc"
... )

```
Copy to clipboard
Specify that the four points form a spline and add a circular cross-section with a diameter of 1 mm.

```
>>> P4 = m3d.modeler.create_polyline(
...     test_points, segment_type="Spline", name="PL_spline", xsection_type="Circle", xsection_width="1mm"
... )

```
Copy to clipboard
Use the `PolylineSegment` object to specify more detail about the individual segments. Create a center point arc starting from the position `test_points[1]`, rotating about the center point position `test_points[0]` in the XY plane.

```
>>> start_point = test_points[1]
>>> center_point = test_points[0]
>>> segment_def = PolylineSegment(
...     segment_type="AngularArc", arc_center=center_point, arc_angle="90deg", arc_plane="XY"
... )
>>> m3d.modeler.create_polyline(start_point, segment_type=segment_def, name="PL_center_point_arc")

```
Copy to clipboard
Create a spline using a list of variables for the coordinates of the points.

```
>>> x0, y0, z0 = "0", "0", "1"
>>> x1, y1, z1 = "1", "3", "1"
>>> x2, y2, z2 = "2", "2", "1"
>>> P5 = m3d.modeler.create_polyline(
...     points=[[x0, y0, z0], [x1, y1, z1], [x2, y2, z2]], segment_type="Spline", name="polyline_with_variables"
... )

```
Copy to clipboard
Create a closed geometry by specifying in `segment_type` a list of `PolylineSegments` including `AngularArc` segments.

```
>>> test_points_1 = [[0.4, 0, 0], [-0.4, -0.6, 0], [0.4, 0, 0]]
>>> P6 = m3d.modeler.create_polyline(
...     points=test_points_1,
...     segment_type=[
...         PolylineSegment(
...             segment_type="AngularArc", arc_center=[0, 0, 0], arc_angle="180deg", arc_plane="XY"
...         ),
...         PolylineSegment(segment_type="Line"),
...         PolylineSegment(
...             segment_type="AngularArc", arc_center=[0, -0.6, 0], arc_angle="180deg", arc_plane="XY"
...         ),
...         PolylineSegment(segment_type="Line"),
...     ],
... )

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_polyline.rst.txt)

# create_polyline 

Modeler3D.create_polyline(_points : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _segment_type : [PolylineSegment](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.PolylineSegment.html#ansys.aedt.core.modeler.cad.polylines.PolylineSegment "ansys.aedt.core.modeler.cad.object_3d.PolylineSegment") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _cover_surface : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _close_surface : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _xsection_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _xsection_orient : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _xsection_width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _xsection_topwidth : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _xsection_height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _xsection_num_seg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _xsection_bend_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _non_model : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [Polyline](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.Polyline.html#ansys.aedt.core.modeler.cad.polylines.Polyline "ansys.aedt.core.modeler.cad.polylines.Polyline") 
    
Draw a polyline object in the 3D modeler.
This method retrieves the `ansys.aedt.core.modeler.cad.primitives.Polyline` object, which has additional methods for manipulating the polyline. For example, you can use `ansys.aedt.core.modeler.cad.primitives.Polyline.insert_segment()` to insert a segment or `ansys.aedt.core.modeler.cad.primitives.Polyline.id` to retrieve the ID of the polyline object. 

Parameters: 
     

**points**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Array of positions of each point of the polyline. A position is a list of 2D or 3D coordinates. Position coordinate values can be numbers or valid AEDT string expressions. For example, `[0, 1, 2]`, `["0mm", "5mm", "1mm"]`, or `["x1", "y1", "z1"]`. 

**segment_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or `PolylineSegment` or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
The default behavior is to connect all points as `"Line"` segments. The default is `None`. Use a `"PolylineSegment"`, for `"Line"`, `"Arc"`, `"Spline"`, or `"AngularArc"`. A list of segment types (str or `ansys.aedt.core.modeler.cad.primitives.PolylineSegment`) is valid for a compound polyline. 

**cover_surface**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `False`. 

**close_surface**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
The default is `False`, which automatically joins the starting and ending points. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the polyline. The default is `None`. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. 

**xsection_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the cross-section. Options are `"Line"`, `"Circle"`, `"Rectangle"`, and `"Isosceles Trapezoid"`. The default is `None`. 

**xsection_orient**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Direction of the normal vector to the width of the cross-section. Options are `"X"`, `"Y"`, `"Z"`, and `"Auto"`. The default is `None`, which sets the direction to `"Auto"`. 

**xsection_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Width or diameter of the cross-section for all types. The default is `1`. 

**xsection_topwidth**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Top width of the cross-section for type `"Isosceles Trapezoid"` only. The default is `1`. 

**xsection_height**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Height of the cross-section for type `"Rectangle"` or `"Isosceles Trapezoid"` only. The default is `1`. 

**xsection_num_seg**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments in the cross-section surface for type `"Circle"`, `"Rectangle"`, or `"Isosceles Trapezoid"`. The default is `0`. The value must be `0` or greater than `2`. 

**xsection_bend_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the bend for the cross-section. The default is `None`, in which case the bend type is set to `"Corner"`. For the type `"Circle"`, the bend type should be set to `"Curved"`. 

**non_model**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if the polyline will be created as model or unmodel object. 

Returns: 
     

`ansys.aedt.core.modeler.polylines.Polyline`
    
Polyline object.
References

```
>>> oEditor.CreatePolyline

```
Copy to clipboard
Examples
Set up the desktop environment.

```
>>> from ansys.aedt.core.modeler.cad.polylines import PolylineSegment
>>> from ansys.aedt.core import Desktop
>>> from ansys.aedt.core import Maxwell3d
>>> desktop = Desktop(version="2026.1", new_desktop=False)
>>> m3d = Maxwell3d()
>>> m3d.modeler.model_units = "mm"

```
Copy to clipboard
Define some test data points.

```
>>> test_points = [
...     ["0mm", "0mm", "0mm"],
...     ["100mm", "20mm", "0mm"],
...     ["71mm", "71mm", "0mm"],
...     ["0mm", "100mm", "0mm"],
... ]

```
Copy to clipboard
The default behavior assumes that all points are to be connected by line segments. Optionally specify the name.

```
>>> P1 = m3d.modeler.create_polyline(test_points, name="PL_line_segments")

```
Copy to clipboard
Specify that the first segment is a line and the last three points define a three-point arc.

```
>>> P2 = m3d.modeler.create_polyline(test_points, segment_type=["Line", "Arc"], name="PL_line_plus_arc")

```
Copy to clipboard
Redraw the 3-point arc alone from the last three points and additionally specify five segments using `PolylineSegment`.

```
>>> P3 = m3d.modeler.create_polyline(
...     test_points[1:], segment_type=PolylineSegment(segment_type="Arc", num_seg=7), name="PL_segmented_arc"
... )

```
Copy to clipboard
Specify that the four points form a spline and add a circular cross-section with a diameter of 1 mm.

```
>>> P4 = m3d.modeler.create_polyline(
...     test_points, segment_type="Spline", name="PL_spline", xsection_type="Circle", xsection_width="1mm"
... )

```
Copy to clipboard
Use the `PolylineSegment` object to specify more detail about the individual segments. Create a center point arc starting from the position `test_points[1]`, rotating about the center point position `test_points[0]` in the XY plane.

```
>>> start_point = test_points[1]
>>> center_point = test_points[0]
>>> segment_def = PolylineSegment(
...     segment_type="AngularArc", arc_center=center_point, arc_angle="90deg", arc_plane="XY"
... )
>>> m3d.modeler.create_polyline(start_point, segment_type=segment_def, name="PL_center_point_arc")

```
Copy to clipboard
Create a spline using a list of variables for the coordinates of the points.

```
>>> x0, y0, z0 = "0", "0", "1"
>>> x1, y1, z1 = "1", "3", "1"
>>> x2, y2, z2 = "2", "2", "1"
>>> P5 = m3d.modeler.create_polyline(
...     points=[[x0, y0, z0], [x1, y1, z1], [x2, y2, z2]], segment_type="Spline", name="polyline_with_variables"
... )

```
Copy to clipboard
Create a closed geometry by specifying in `segment_type` a list of `PolylineSegments` including `AngularArc` segments.

```
>>> test_points_1 = [[0.4, 0, 0], [-0.4, -0.6, 0], [0.4, 0, 0]]
>>> P6 = m3d.modeler.create_polyline(
...     points=test_points_1,
...     segment_type=[
...         PolylineSegment(
...             segment_type="AngularArc", arc_center=[0, 0, 0], arc_angle="180deg", arc_plane="XY"
...         ),
...         PolylineSegment(segment_type="Line"),
...         PolylineSegment(
...             segment_type="AngularArc", arc_center=[0, -0.6, 0], arc_angle="180deg", arc_plane="XY"
...         ),
...         PolylineSegment(segment_type="Line"),
...     ],
... )

```
Copy to clipboard