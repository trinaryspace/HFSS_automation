---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.Polyline.remove_segments.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# remove_segments 

Polyline.remove_segments(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")]_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Remove a segment from an existing polyline by segment id.
You must enter the segment id or the list of the segment ids you want to remove. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `List` `of` [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
One or more edge IDs within the total number of edges of the polyline. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.DeletePolylinePoint

```
Copy to clipboard
Examples

```
>>> P = modeler.create_polyline([[0, 1, 2], [0, 2, 3], [2, 1, 4]])
>>> P.remove_segments(assignment=0)

```
Copy to clipboard
# remove_segments 

Polyline.remove_segments(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")]_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Remove a segment from an existing polyline by segment id.
You must enter the segment id or the list of the segment ids you want to remove. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `List` `of` [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
One or more edge IDs within the total number of edges of the polyline. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.DeletePolylinePoint

```
Copy to clipboard
Examples

```
>>> P = modeler.create_polyline([[0, 1, 2], [0, 2, 3], [2, 1, 4]])
>>> P.remove_segments(assignment=0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.Polyline.remove_segments.rst.txt)

# remove_segments 

Polyline.remove_segments(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")]_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Remove a segment from an existing polyline by segment id.
You must enter the segment id or the list of the segment ids you want to remove. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or `List` `of` [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
One or more edge IDs within the total number of edges of the polyline. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.DeletePolylinePoint

```
Copy to clipboard
Examples

```
>>> P = modeler.create_polyline([[0, 1, 2], [0, 2, 3], [2, 1, 4]])
>>> P.remove_segments(assignment=0)

```
Copy to clipboard