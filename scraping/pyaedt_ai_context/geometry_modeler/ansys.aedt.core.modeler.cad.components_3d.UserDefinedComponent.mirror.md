---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.mirror.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# mirror 

UserDefinedComponent.mirror(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_) → [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Mirror a selection. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `Position` 
    
List of the `[x, y, z]` coordinates or the Application.Position object for the selection. 

**vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `Position` 
    
List of the `[x1, y1, z1]` coordinates or the Application.Position object for the vector. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent"), [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object when successful, `False` when failed.
References

```
>>> oEditor.Mirror

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.components_3d import UserDefinedComponent
>>> obj = UserDefinedComponent()
>>> obj.mirror(origin=[0, 0, 0], vector=[1, 0, 0])

```
Copy to clipboard
# mirror 

UserDefinedComponent.mirror(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_) → [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Mirror a selection. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `Position` 
    
List of the `[x, y, z]` coordinates or the Application.Position object for the selection. 

**vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `Position` 
    
List of the `[x1, y1, z1]` coordinates or the Application.Position object for the vector. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent"), [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object when successful, `False` when failed.
References

```
>>> oEditor.Mirror

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.components_3d import UserDefinedComponent
>>> obj = UserDefinedComponent()
>>> obj.mirror(origin=[0, 0, 0], vector=[1, 0, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.mirror.rst.txt)

# mirror 

UserDefinedComponent.mirror(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_) → [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Mirror a selection. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `Position` 
    
List of the `[x, y, z]` coordinates or the Application.Position object for the selection. 

**vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `Position` 
    
List of the `[x1, y1, z1]` coordinates or the Application.Position object for the vector. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent"), [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
3D object when successful, `False` when failed.
References

```
>>> oEditor.Mirror

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.components_3d import UserDefinedComponent
>>> obj = UserDefinedComponent()
>>> obj.mirror(origin=[0, 0, 0], vector=[1, 0, 0])

```
Copy to clipboard