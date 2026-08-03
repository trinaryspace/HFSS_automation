---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.move.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# move 

UserDefinedComponent.move(_vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_) → [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Move component from a list. 

Parameters: 
     

**vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Vector of the direction move. It can be a list of the `[x, y, z]` coordinates or a `Position` object. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent"), [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object when successful, `False` when failed.
References

```
>>> oEditor.Move

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.components_3d import UserDefinedComponent
>>> obj = UserDefinedComponent()
>>> obj.move(vector=[1, 0, 0])

```
Copy to clipboard
# move 

UserDefinedComponent.move(_vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_) → [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Move component from a list. 

Parameters: 
     

**vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Vector of the direction move. It can be a list of the `[x, y, z]` coordinates or a `Position` object. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent"), [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object when successful, `False` when failed.
References

```
>>> oEditor.Move

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.components_3d import UserDefinedComponent
>>> obj = UserDefinedComponent()
>>> obj.move(vector=[1, 0, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.move.rst.txt)

# move 

UserDefinedComponent.move(_vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_) → [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Move component from a list. 

Parameters: 
     

**vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Vector of the direction move. It can be a list of the `[x, y, z]` coordinates or a `Position` object. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent"), [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object when successful, `False` when failed.
References

```
>>> oEditor.Move

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.components_3d import UserDefinedComponent
>>> obj = UserDefinedComponent()
>>> obj.move(vector=[1, 0, 0])

```
Copy to clipboard