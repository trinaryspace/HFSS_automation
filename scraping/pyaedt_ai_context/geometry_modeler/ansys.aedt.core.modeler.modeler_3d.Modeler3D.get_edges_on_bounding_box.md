---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.get_edges_on_bounding_box.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# get_edges_on_bounding_box 

Modeler3D.get_edges_on_bounding_box(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _return_colinear : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-06_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve the edges of the sheets passed in the input that are lying on the bounding box.
This method creates new lines for the detected edges and returns the IDs of these lines. If required, only colinear edges are returned. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `or` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
ID or name for one or more sheets. 

**return_colinear**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to return only colinear edges. The default is `True`. If `False`, all edges on the bounding box are returned. 

**tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Geometric tolerance. The default is `1e-6`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of edge IDs lying on the bounding box.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_edges_on_bounding_box(assignment="Box1")

```
Copy to clipboard
# get_edges_on_bounding_box 

Modeler3D.get_edges_on_bounding_box(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _return_colinear : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-06_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve the edges of the sheets passed in the input that are lying on the bounding box.
This method creates new lines for the detected edges and returns the IDs of these lines. If required, only colinear edges are returned. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `or` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
ID or name for one or more sheets. 

**return_colinear**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to return only colinear edges. The default is `True`. If `False`, all edges on the bounding box are returned. 

**tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Geometric tolerance. The default is `1e-6`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of edge IDs lying on the bounding box.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_edges_on_bounding_box(assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.get_edges_on_bounding_box.rst.txt)

# get_edges_on_bounding_box 

Modeler3D.get_edges_on_bounding_box(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _return_colinear : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-06_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve the edges of the sheets passed in the input that are lying on the bounding box.
This method creates new lines for the detected edges and returns the IDs of these lines. If required, only colinear edges are returned. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `or` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
ID or name for one or more sheets. 

**return_colinear**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to return only colinear edges. The default is `True`. If `False`, all edges on the bounding box are returned. 

**tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Geometric tolerance. The default is `1e-6`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of edge IDs lying on the bounding box.
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.get_edges_on_bounding_box(assignment="Box1")

```
Copy to clipboard