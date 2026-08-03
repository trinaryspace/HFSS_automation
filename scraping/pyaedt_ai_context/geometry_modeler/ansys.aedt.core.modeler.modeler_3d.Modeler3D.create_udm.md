---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_udm.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_udm 

Modeler3D.create_udm(_udm_full_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _parameters : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _library : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'syslib'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a user-defined model. 

Parameters: 
     

**udm_full_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full name for the user-defined model, including the folder name. 

**parameters**
    
List of user-defined object pairs for the model. 

**library**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the library for the user-defined model. The default is `"syslib"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the user-defined model. The default is `None``. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `ansys.aedt.core.modeler.components_3d.UserDefinedComponent` 
    
User-defined component object or `False` if it fails.
References

```
>>> oEditor.CreateUserDefinedModel

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives_3d import Primitives3D
>>> obj = Primitives3D()
>>> obj.create_udm(udm_full_name=1, parameters={"Name": "Value"})

```
Copy to clipboard
# create_udm 

Modeler3D.create_udm(_udm_full_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _parameters : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _library : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'syslib'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a user-defined model. 

Parameters: 
     

**udm_full_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full name for the user-defined model, including the folder name. 

**parameters**
    
List of user-defined object pairs for the model. 

**library**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the library for the user-defined model. The default is `"syslib"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the user-defined model. The default is `None``. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `ansys.aedt.core.modeler.components_3d.UserDefinedComponent` 
    
User-defined component object or `False` if it fails.
References

```
>>> oEditor.CreateUserDefinedModel

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives_3d import Primitives3D
>>> obj = Primitives3D()
>>> obj.create_udm(udm_full_name=1, parameters={"Name": "Value"})

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_udm.rst.txt)

# create_udm 

Modeler3D.create_udm(_udm_full_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _parameters : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _library : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'syslib'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [UserDefinedComponent](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.html#ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent "ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a user-defined model. 

Parameters: 
     

**udm_full_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full name for the user-defined model, including the folder name. 

**parameters**
    
List of user-defined object pairs for the model. 

**library**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the library for the user-defined model. The default is `"syslib"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the user-defined model. The default is `None``. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `ansys.aedt.core.modeler.components_3d.UserDefinedComponent` 
    
User-defined component object or `False` if it fails.
References

```
>>> oEditor.CreateUserDefinedModel

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives_3d import Primitives3D
>>> obj = Primitives3D()
>>> obj.create_udm(udm_full_name=1, parameters={"Name": "Value"})

```
Copy to clipboard