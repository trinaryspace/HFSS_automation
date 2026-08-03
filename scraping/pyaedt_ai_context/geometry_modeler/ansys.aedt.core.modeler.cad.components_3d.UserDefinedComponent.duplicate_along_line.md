---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_along_line.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# duplicate_along_line 

UserDefinedComponent.duplicate_along_line(_vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _clones : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _attach : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _** kwargs_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Duplicate the object along a line. 

Parameters: 
     

**vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x1 ,y1, z1]` coordinates for the vector or the Application.Position object. 

**clones**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of clones. The default is `2`. 

**attach**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to attach the object. The default is `False`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of names of the newly added objects.
References

```
>>> oEditor.DuplicateAlongLine

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.components_3d import UserDefinedComponent
>>> obj = UserDefinedComponent()
>>> obj.duplicate_along_line(vector=[1, 0, 0])

```
Copy to clipboard
# duplicate_along_line 

UserDefinedComponent.duplicate_along_line(_vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _clones : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _attach : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _** kwargs_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Duplicate the object along a line. 

Parameters: 
     

**vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x1 ,y1, z1]` coordinates for the vector or the Application.Position object. 

**clones**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of clones. The default is `2`. 

**attach**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to attach the object. The default is `False`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of names of the newly added objects.
References

```
>>> oEditor.DuplicateAlongLine

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.components_3d import UserDefinedComponent
>>> obj = UserDefinedComponent()
>>> obj.duplicate_along_line(vector=[1, 0, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.duplicate_along_line.rst.txt)

# duplicate_along_line 

UserDefinedComponent.duplicate_along_line(_vector : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _clones : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _attach : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _** kwargs_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Duplicate the object along a line. 

Parameters: 
     

**vector**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x1 ,y1, z1]` coordinates for the vector or the Application.Position object. 

**clones**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of clones. The default is `2`. 

**attach**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to attach the object. The default is `False`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of names of the newly added objects.
References

```
>>> oEditor.DuplicateAlongLine

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.components_3d import UserDefinedComponent
>>> obj = UserDefinedComponent()
>>> obj.duplicate_along_line(vector=[1, 0, 0])

```
Copy to clipboard