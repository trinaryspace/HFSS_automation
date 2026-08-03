---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.mirror.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# mirror 

Modeler3D.mirror(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _duplicate : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _is_3d_comp : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _duplicate_assignment : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Mirror a selection. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `or` `Object3d` 
    
Name or ID of the object. 

**origin**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates or the `Application.Position` object for the selection. 

**duplicate**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if duplicate the object before mirror or not. Default is `False`. 

**is_3d_comp**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the component is 3D. The default is `False`. If `True`, the method tries to return the duplicated list of 3D components. 

**vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[x1, y1, z1]` coordinates or the `Application.Position` object for the vector. 

**duplicate_assignment**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to duplicate selection assignments. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects created or `True` when successful, `False` when failed.
References

```
>>> oEditor.Mirror
>>> oEditor.DuplicateMirror

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.mirror(assignment="Box1", origin=[0, 0, 0], vector=[1, 0, 0])

```
Copy to clipboard
# mirror 

Modeler3D.mirror(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _duplicate : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _is_3d_comp : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _duplicate_assignment : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Mirror a selection. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `or` `Object3d` 
    
Name or ID of the object. 

**origin**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates or the `Application.Position` object for the selection. 

**duplicate**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if duplicate the object before mirror or not. Default is `False`. 

**is_3d_comp**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the component is 3D. The default is `False`. If `True`, the method tries to return the duplicated list of 3D components. 

**vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[x1, y1, z1]` coordinates or the `Application.Position` object for the vector. 

**duplicate_assignment**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to duplicate selection assignments. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects created or `True` when successful, `False` when failed.
References

```
>>> oEditor.Mirror
>>> oEditor.DuplicateMirror

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.mirror(assignment="Box1", origin=[0, 0, 0], vector=[1, 0, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.mirror.rst.txt)

# mirror 

Modeler3D.mirror(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")_, _origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _duplicate : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _is_3d_comp : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _duplicate_assignment : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Mirror a selection. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `or` `Object3d` 
    
Name or ID of the object. 

**origin**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates or the `Application.Position` object for the selection. 

**duplicate**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if duplicate the object before mirror or not. Default is `False`. 

**is_3d_comp**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the component is 3D. The default is `False`. If `True`, the method tries to return the duplicated list of 3D components. 

**vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[x1, y1, z1]` coordinates or the `Application.Position` object for the vector. 

**duplicate_assignment**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to duplicate selection assignments. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of objects created or `True` when successful, `False` when failed.
References

```
>>> oEditor.Mirror
>>> oEditor.DuplicateMirror

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.mirror(assignment="Box1", origin=[0, 0, 0], vector=[1, 0, 0])

```
Copy to clipboard