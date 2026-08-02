---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.PolylineSegment.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# PolylineSegment 

class ansys.aedt.core.modeler.cad.polylines.PolylineSegment(_segment_type_ , _num_seg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _num_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _arc_angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _arc_center =None_, _arc_plane =None_) 
    
Creates and manipulates a segment of a polyline. 

Parameters: 
     

**segment_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the object. Choices are `"Line"`, `"Arc"`, `"Spline"`, and `"AngularArc"`. 

**num_seg**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments for the types `"Arc"`, `"Spline"`, and `"AngularArc"`. The default is `0`. For the type `Line`, this parameter is ignored. 

**num_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of control points for the type `Spline`. For other types, this parameter is defined automatically. 

**arc_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Sweep angle in radians or a valid value string. For example, `"35deg"` or `0.25`. This argument is Specific to type AngularArc. 

**arc_center**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
List of values in model units or a valid value string. For example, a list of `[x, y, z]` coordinates. This argument is Specific to type AngularArc. 

**arc_plane**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") `optional` 
    
Plane in which the arc sweep is performed in the active coordinate system `"XY"`, `"YZ"` or `"ZX"`. The default is `None`, in which case the plane is determined automatically by the first coordinate for which the starting point and center point have the same value. This argument is Specific to type AngularArc.
Examples
See `ansys.aedt.core.Primitives.Polyline`.
Attributes  
| [`PolylineSegment.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.PolylineSegment.public_dir.html#ansys.aedt.core.modeler.cad.polylines.PolylineSegment.public_dir "ansys.aedt.core.modeler.cad.polylines.PolylineSegment.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |  
# PolylineSegment 

class ansys.aedt.core.modeler.cad.polylines.PolylineSegment(_segment_type_ , _num_seg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _num_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _arc_angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _arc_center =None_, _arc_plane =None_) 
    
Creates and manipulates a segment of a polyline. 

Parameters: 
     

**segment_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the object. Choices are `"Line"`, `"Arc"`, `"Spline"`, and `"AngularArc"`. 

**num_seg**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments for the types `"Arc"`, `"Spline"`, and `"AngularArc"`. The default is `0`. For the type `Line`, this parameter is ignored. 

**num_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of control points for the type `Spline`. For other types, this parameter is defined automatically. 

**arc_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Sweep angle in radians or a valid value string. For example, `"35deg"` or `0.25`. This argument is Specific to type AngularArc. 

**arc_center**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
List of values in model units or a valid value string. For example, a list of `[x, y, z]` coordinates. This argument is Specific to type AngularArc. 

**arc_plane**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") `optional` 
    
Plane in which the arc sweep is performed in the active coordinate system `"XY"`, `"YZ"` or `"ZX"`. The default is `None`, in which case the plane is determined automatically by the first coordinate for which the starting point and center point have the same value. This argument is Specific to type AngularArc.
Examples
See `ansys.aedt.core.Primitives.Polyline`.
Attributes  
| [`PolylineSegment.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.PolylineSegment.public_dir.html#ansys.aedt.core.modeler.cad.polylines.PolylineSegment.public_dir "ansys.aedt.core.modeler.cad.polylines.PolylineSegment.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.PolylineSegment.rst.txt)

# PolylineSegment 

class ansys.aedt.core.modeler.cad.polylines.PolylineSegment(_segment_type_ , _num_seg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _num_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _arc_angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _arc_center =None_, _arc_plane =None_) 
    
Creates and manipulates a segment of a polyline. 

Parameters: 
     

**segment_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Type of the object. Choices are `"Line"`, `"Arc"`, `"Spline"`, and `"AngularArc"`. 

**num_seg**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments for the types `"Arc"`, `"Spline"`, and `"AngularArc"`. The default is `0`. For the type `Line`, this parameter is ignored. 

**num_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of control points for the type `Spline`. For other types, this parameter is defined automatically. 

**arc_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Sweep angle in radians or a valid value string. For example, `"35deg"` or `0.25`. This argument is Specific to type AngularArc. 

**arc_center**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
List of values in model units or a valid value string. For example, a list of `[x, y, z]` coordinates. This argument is Specific to type AngularArc. 

**arc_plane**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") `optional` 
    
Plane in which the arc sweep is performed in the active coordinate system `"XY"`, `"YZ"` or `"ZX"`. The default is `None`, in which case the plane is determined automatically by the first coordinate for which the starting point and center point have the same value. This argument is Specific to type AngularArc.
Examples
See `ansys.aedt.core.Primitives.Polyline`.
Attributes  
| [`PolylineSegment.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.PolylineSegment.public_dir.html#ansys.aedt.core.modeler.cad.polylines.PolylineSegment.public_dir "ansys.aedt.core.modeler.cad.polylines.PolylineSegment.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |