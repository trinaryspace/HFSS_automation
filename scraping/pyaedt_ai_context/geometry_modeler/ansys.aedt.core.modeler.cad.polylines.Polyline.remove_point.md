---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.Polyline.remove_point.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# remove_point 

Polyline.remove_point(_position : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-09_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Remove a point from an existing polyline by position.
You must enter the exact position of the vertex as a list of `[x, y, z]` coordinates in the object’s coordinate system. 

Parameters: 
     

**position**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates specifying the vertex to remove. 

**tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Absolute tolerance of the comparison of a specified position to the vertex positions. The default is `1e-9`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.DeletePolylinePoint

```
Copy to clipboard
Examples
Use floating point values for the vertex positions.

```
>>> P = modeler.create_polyline([[0, 1, 2], [0, 2, 3], [2, 1, 4]])
>>> P.remove_point([0, 1, 2])

```
Copy to clipboard
Use string expressions for the vertex position.

```
>>> P = modeler.create_polyline([[0, 1, 2], [0, 2, 3], [2, 1, 4]])
>>> P.remove_point(["0mm", "1mm", "2mm"])

```
Copy to clipboard
Use string expressions for the vertex position and include an absolute tolerance when searching for the vertex to be removed.

```
>>> P = modeler.create_polyline([[0, 1, 2], [0, 2, 3], [2, 1, 4]])
>>> P.remove_point(["0mm", "1mm", "2mm"], tolerance=1e-6)

```
Copy to clipboard
# remove_point 

Polyline.remove_point(_position : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-09_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Remove a point from an existing polyline by position.
You must enter the exact position of the vertex as a list of `[x, y, z]` coordinates in the object’s coordinate system. 

Parameters: 
     

**position**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates specifying the vertex to remove. 

**tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Absolute tolerance of the comparison of a specified position to the vertex positions. The default is `1e-9`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.DeletePolylinePoint

```
Copy to clipboard
Examples
Use floating point values for the vertex positions.

```
>>> P = modeler.create_polyline([[0, 1, 2], [0, 2, 3], [2, 1, 4]])
>>> P.remove_point([0, 1, 2])

```
Copy to clipboard
Use string expressions for the vertex position.

```
>>> P = modeler.create_polyline([[0, 1, 2], [0, 2, 3], [2, 1, 4]])
>>> P.remove_point(["0mm", "1mm", "2mm"])

```
Copy to clipboard
Use string expressions for the vertex position and include an absolute tolerance when searching for the vertex to be removed.

```
>>> P = modeler.create_polyline([[0, 1, 2], [0, 2, 3], [2, 1, 4]])
>>> P.remove_point(["0mm", "1mm", "2mm"], tolerance=1e-6)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.Polyline.remove_point.rst.txt)

# remove_point 

Polyline.remove_point(_position : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-09_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Remove a point from an existing polyline by position.
You must enter the exact position of the vertex as a list of `[x, y, z]` coordinates in the object’s coordinate system. 

Parameters: 
     

**position**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates specifying the vertex to remove. 

**tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Absolute tolerance of the comparison of a specified position to the vertex positions. The default is `1e-9`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.DeletePolylinePoint

```
Copy to clipboard
Examples
Use floating point values for the vertex positions.

```
>>> P = modeler.create_polyline([[0, 1, 2], [0, 2, 3], [2, 1, 4]])
>>> P.remove_point([0, 1, 2])

```
Copy to clipboard
Use string expressions for the vertex position.

```
>>> P = modeler.create_polyline([[0, 1, 2], [0, 2, 3], [2, 1, 4]])
>>> P.remove_point(["0mm", "1mm", "2mm"])

```
Copy to clipboard
Use string expressions for the vertex position and include an absolute tolerance when searching for the vertex to be removed.

```
>>> P = modeler.create_polyline([[0, 1, 2], [0, 2, 3], [2, 1, 4]])
>>> P.remove_point(["0mm", "1mm", "2mm"], tolerance=1e-6)

```
Copy to clipboard