---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_3dcomponent.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_3dcomponent 

Modeler3D.create_3dcomponent(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variables_to_include : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _boundaries : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _excitations : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _coordinate_systems : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _reference_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _is_encrypted : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _allow_edit : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _security_message : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _password : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _edit_password : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _password_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'UserSuppliedPassword'_, _hide_contents : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _replace_names : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _component_outline : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'BoundingBox'_, _export_auxiliary : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _monitor_objects : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _datasets : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _native_components : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _create_folder : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a 3D component file. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the A3DCOMP file. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the component. The default is `None`. 

**variables_to_include**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of variables to include. The default is all variables. 

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of object names to export. The default is all object names. 

**boundaries**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Boundaries names to export. The default is all boundaries. 

**excitations**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Excitation names to export. The default is all excitations. 

**coordinate_systems**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Coordinate Systems to export. The default is the `reference_cs`. 

**reference_coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The Coordinate System reference. The default is `"Global"`. 

**is_encrypted**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the component has encrypted protection. The default is `False`. 

**allow_edit**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the component is editable with encrypted protection. The default is `False`. 

**security_message**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Security message to display when component is inserted. The default value is an empty string. 

**password**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Security password needed when adding the component. The default value is `None`. 

**edit_password**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Edit password. The default value is `None`. 

**password_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Password type. Options are `UserSuppliedPassword` and `InternalPassword`. The default is `UserSuppliedPassword`. 

**hide_contents**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of object names to hide when the component is encrypted. If set to an empty list or `False`, all objects are visible. 

**replace_names**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to replace objects and material names. The default is `False`. 

**component_outline**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Component outline. Value can either be `BoundingBox` or `None`. The default is `BoundingBox`. 

**export_auxiliary**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to export the auxiliary file containing information about defined datasets and Icepak monitor objects. A destination file can be specified using a string. The default is `False`. 

**monitor_objects**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of monitor objects’ names to export. The default is the names of all monitor objects. This argument is relevant only if `auxiliary_dict_file` is not set to `False`. 

**datasets**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
     

List of dataset names to export. The default is all datasets. This argument
    
is relevant only if `auxiliary_dict_file` is set to `True`. 

**native_components**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of native_components names to export. The default is all native_components. This argument is relevant only if `auxiliary_dict_file` is set to `True`. 

**create_folder**`Bool` , `optional` 
    
If the specified path to the folder where the 3D component should be saved does not exist, then create the folder. Default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.Create3DComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.modeler_3d import Modeler3D
>>> obj = Modeler3D()
>>> obj.create_3dcomponent(input_file="example.txt")

```
Copy to clipboard
# create_3dcomponent 

Modeler3D.create_3dcomponent(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variables_to_include : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _boundaries : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _excitations : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _coordinate_systems : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _reference_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _is_encrypted : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _allow_edit : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _security_message : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _password : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _edit_password : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _password_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'UserSuppliedPassword'_, _hide_contents : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _replace_names : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _component_outline : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'BoundingBox'_, _export_auxiliary : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _monitor_objects : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _datasets : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _native_components : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _create_folder : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a 3D component file. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the A3DCOMP file. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the component. The default is `None`. 

**variables_to_include**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of variables to include. The default is all variables. 

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of object names to export. The default is all object names. 

**boundaries**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Boundaries names to export. The default is all boundaries. 

**excitations**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Excitation names to export. The default is all excitations. 

**coordinate_systems**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Coordinate Systems to export. The default is the `reference_cs`. 

**reference_coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The Coordinate System reference. The default is `"Global"`. 

**is_encrypted**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the component has encrypted protection. The default is `False`. 

**allow_edit**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the component is editable with encrypted protection. The default is `False`. 

**security_message**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Security message to display when component is inserted. The default value is an empty string. 

**password**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Security password needed when adding the component. The default value is `None`. 

**edit_password**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Edit password. The default value is `None`. 

**password_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Password type. Options are `UserSuppliedPassword` and `InternalPassword`. The default is `UserSuppliedPassword`. 

**hide_contents**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of object names to hide when the component is encrypted. If set to an empty list or `False`, all objects are visible. 

**replace_names**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to replace objects and material names. The default is `False`. 

**component_outline**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Component outline. Value can either be `BoundingBox` or `None`. The default is `BoundingBox`. 

**export_auxiliary**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to export the auxiliary file containing information about defined datasets and Icepak monitor objects. A destination file can be specified using a string. The default is `False`. 

**monitor_objects**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of monitor objects’ names to export. The default is the names of all monitor objects. This argument is relevant only if `auxiliary_dict_file` is not set to `False`. 

**datasets**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
     

List of dataset names to export. The default is all datasets. This argument
    
is relevant only if `auxiliary_dict_file` is set to `True`. 

**native_components**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of native_components names to export. The default is all native_components. This argument is relevant only if `auxiliary_dict_file` is set to `True`. 

**create_folder**`Bool` , `optional` 
    
If the specified path to the folder where the 3D component should be saved does not exist, then create the folder. Default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.Create3DComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.modeler_3d import Modeler3D
>>> obj = Modeler3D()
>>> obj.create_3dcomponent(input_file="example.txt")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_3dcomponent.rst.txt)

# create_3dcomponent 

Modeler3D.create_3dcomponent(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variables_to_include : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _boundaries : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _excitations : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _coordinate_systems : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _reference_coordinate_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _is_encrypted : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _allow_edit : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _security_message : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _password : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _edit_password : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _password_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'UserSuppliedPassword'_, _hide_contents : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _replace_names : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _component_outline : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'BoundingBox'_, _export_auxiliary : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _monitor_objects : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _datasets : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _native_components : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _create_folder : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a 3D component file. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the A3DCOMP file. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the component. The default is `None`. 

**variables_to_include**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of variables to include. The default is all variables. 

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of object names to export. The default is all object names. 

**boundaries**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Boundaries names to export. The default is all boundaries. 

**excitations**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Excitation names to export. The default is all excitations. 

**coordinate_systems**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of Coordinate Systems to export. The default is the `reference_cs`. 

**reference_coordinate_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The Coordinate System reference. The default is `"Global"`. 

**is_encrypted**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the component has encrypted protection. The default is `False`. 

**allow_edit**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the component is editable with encrypted protection. The default is `False`. 

**security_message**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Security message to display when component is inserted. The default value is an empty string. 

**password**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Security password needed when adding the component. The default value is `None`. 

**edit_password**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Edit password. The default value is `None`. 

**password_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Password type. Options are `UserSuppliedPassword` and `InternalPassword`. The default is `UserSuppliedPassword`. 

**hide_contents**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of object names to hide when the component is encrypted. If set to an empty list or `False`, all objects are visible. 

**replace_names**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to replace objects and material names. The default is `False`. 

**component_outline**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Component outline. Value can either be `BoundingBox` or `None`. The default is `BoundingBox`. 

**export_auxiliary**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to export the auxiliary file containing information about defined datasets and Icepak monitor objects. A destination file can be specified using a string. The default is `False`. 

**monitor_objects**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of monitor objects’ names to export. The default is the names of all monitor objects. This argument is relevant only if `auxiliary_dict_file` is not set to `False`. 

**datasets**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
     

List of dataset names to export. The default is all datasets. This argument
    
is relevant only if `auxiliary_dict_file` is set to `True`. 

**native_components**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of native_components names to export. The default is all native_components. This argument is relevant only if `auxiliary_dict_file` is set to `True`. 

**create_folder**`Bool` , `optional` 
    
If the specified path to the folder where the 3D component should be saved does not exist, then create the folder. Default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.Create3DComponent

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.modeler_3d import Modeler3D
>>> obj = Modeler3D()
>>> obj.create_3dcomponent(input_file="example.txt")

```
Copy to clipboard