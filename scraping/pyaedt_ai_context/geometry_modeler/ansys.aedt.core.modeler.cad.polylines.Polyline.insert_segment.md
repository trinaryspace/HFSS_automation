---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.Polyline.insert_segment.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# insert_segment 

Polyline.insert_segment(_points : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _segment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [PolylineSegment](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.PolylineSegment.html#ansys.aedt.core.modeler.cad.polylines.PolylineSegment "ansys.aedt.core.modeler.cad.object_3d.PolylineSegment") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a segment to an existing polyline. 

Parameters: 
     

**points**`List` 
    
List of positions of the points that define the segment to insert. Either the starting point or ending point of the segment list must match one of the vertices of the existing polyline. 

**segment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or `ansys.aedt.core.modeler.cad.primitives.PolylineSegment`, `optional` 
    
Definition of the segment to insert. For the types `"Line"` and `"Arc"`, use their string values `"Line"` and `"Arc"`. For the types `"AngularArc"` and `"Spline"`, use the `ansys.aedt.core.modeler.cad.primitives.PolylineSegment` object to define the segment precisely. The default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.InsertPolylineSegment

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.insert_segment(points=[0, 0, 0])

```
Copy to clipboard
# insert_segment 

Polyline.insert_segment(_points : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _segment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [PolylineSegment](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.PolylineSegment.html#ansys.aedt.core.modeler.cad.polylines.PolylineSegment "ansys.aedt.core.modeler.cad.object_3d.PolylineSegment") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a segment to an existing polyline. 

Parameters: 
     

**points**`List` 
    
List of positions of the points that define the segment to insert. Either the starting point or ending point of the segment list must match one of the vertices of the existing polyline. 

**segment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or `ansys.aedt.core.modeler.cad.primitives.PolylineSegment`, `optional` 
    
Definition of the segment to insert. For the types `"Line"` and `"Arc"`, use their string values `"Line"` and `"Arc"`. For the types `"AngularArc"` and `"Spline"`, use the `ansys.aedt.core.modeler.cad.primitives.PolylineSegment` object to define the segment precisely. The default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.InsertPolylineSegment

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.insert_segment(points=[0, 0, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.Polyline.insert_segment.rst.txt)

# insert_segment 

Polyline.insert_segment(_points : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _segment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [PolylineSegment](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.PolylineSegment.html#ansys.aedt.core.modeler.cad.polylines.PolylineSegment "ansys.aedt.core.modeler.cad.object_3d.PolylineSegment") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a segment to an existing polyline. 

Parameters: 
     

**points**`List` 
    
List of positions of the points that define the segment to insert. Either the starting point or ending point of the segment list must match one of the vertices of the existing polyline. 

**segment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or `ansys.aedt.core.modeler.cad.primitives.PolylineSegment`, `optional` 
    
Definition of the segment to insert. For the types `"Line"` and `"Arc"`, use their string values `"Line"` and `"Arc"`. For the types `"AngularArc"` and `"Spline"`, use the `ansys.aedt.core.modeler.cad.primitives.PolylineSegment` object to define the segment precisely. The default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.InsertPolylineSegment

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.insert_segment(points=[0, 0, 0])

```
Copy to clipboard