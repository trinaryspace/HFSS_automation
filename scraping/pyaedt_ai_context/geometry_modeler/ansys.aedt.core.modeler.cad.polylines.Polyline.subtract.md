---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.Polyline.subtract.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# subtract 

Polyline.subtract(_tool_list : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")]_, _keep_originals : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Subtract one or more parts from the object. 

Parameters: 
     

**tool_list**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `Object3d`, `or` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") `and` Object3d. 
    
List of parts to subtract from this part. 

**keep_originals**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to keep the tool parts after subtraction. The default is `True`. If `False`, the parts are deleted. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
Modified 3D object following the subtraction.
References

```
>>> oEditor.Subtract

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.subtract(tool_list=["Box1"])

```
Copy to clipboard
# subtract 

Polyline.subtract(_tool_list : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")]_, _keep_originals : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Subtract one or more parts from the object. 

Parameters: 
     

**tool_list**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `Object3d`, `or` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") `and` Object3d. 
    
List of parts to subtract from this part. 

**keep_originals**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to keep the tool parts after subtraction. The default is `True`. If `False`, the parts are deleted. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
Modified 3D object following the subtraction.
References

```
>>> oEditor.Subtract

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.subtract(tool_list=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.Polyline.subtract.rst.txt)

# subtract 

Polyline.subtract(_tool_list : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")]_, _keep_originals : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Subtract one or more parts from the object. 

Parameters: 
     

**tool_list**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `Object3d`, `or` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") `and` Object3d. 
    
List of parts to subtract from this part. 

**keep_originals**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to keep the tool parts after subtraction. The default is `True`. If `False`, the parts are deleted. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
Modified 3D object following the subtraction.
References

```
>>> oEditor.Subtract

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.subtract(tool_list=["Box1"])

```
Copy to clipboard