---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.convert_segments_to_line.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# convert_segments_to_line 

Modeler3D.convert_segments_to_line(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Convert a CreatePolyline list of segments to lines.
This method applies to splines and 3-point arguments. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `or` [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Specified for the object. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful, `False` if it fails.
References

```
>>> oEditor.ChangeProperty

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> edge_object = aedtapp.modeler.create_object_from_edge("my_edge")
>>> aedtapp.modeler.generate_object_history(edge_object)
>>> aedtapp.modeler.convert_segments_to_line(edge_object.name)

```
Copy to clipboard
# convert_segments_to_line 

Modeler3D.convert_segments_to_line(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Convert a CreatePolyline list of segments to lines.
This method applies to splines and 3-point arguments. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `or` [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Specified for the object. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful, `False` if it fails.
References

```
>>> oEditor.ChangeProperty

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> edge_object = aedtapp.modeler.create_object_from_edge("my_edge")
>>> aedtapp.modeler.generate_object_history(edge_object)
>>> aedtapp.modeler.convert_segments_to_line(edge_object.name)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.convert_segments_to_line.rst.txt)

# convert_segments_to_line 

Modeler3D.convert_segments_to_line(_assignment : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Convert a CreatePolyline list of segments to lines.
This method applies to splines and 3-point arguments. 

Parameters: 
     

**assignment**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `or` [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Specified for the object. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful, `False` if it fails.
References

```
>>> oEditor.ChangeProperty

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> edge_object = aedtapp.modeler.create_object_from_edge("my_edge")
>>> aedtapp.modeler.generate_object_history(edge_object)
>>> aedtapp.modeler.convert_segments_to_line(edge_object.name)

```
Copy to clipboard