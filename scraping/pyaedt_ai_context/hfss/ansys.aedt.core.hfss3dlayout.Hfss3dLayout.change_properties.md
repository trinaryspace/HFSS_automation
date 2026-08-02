---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.change_properties.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# change_properties 

Hfss3dLayout.change_properties(_aedt_object : [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _tab_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_object : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_names : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _property_values : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _property_types : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Change multiple properties. 

Parameters: 
     

**aedt_object**
    
AEDT object. It can be oproject, odesign, oeditor or any of the objects to which the property belongs. 

**tab_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the tab to update. Options are `BaseElementTab`, `EM Design`, and `FieldsPostProcessorTab`. The default is `BaseElementTab`. 

**property_object**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the property object. 

**property_names**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of property names. For example, `["prop1", "prop2"]`. 

**property_values**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of property values corresponding to the property names. 

**property_types**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of property types corresponding to the property names. Values are `"Value"`, `"ButtonText"`, `"Hidden"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.ChangeProperty

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.change_properties(hfss.oeditor, "BaseElementTab", "Box1", ["Xpos", "Ypos"], ["0mm", "1mm"])

```
Copy to clipboard
# change_properties 

Hfss3dLayout.change_properties(_aedt_object : [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _tab_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_object : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_names : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _property_values : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _property_types : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Change multiple properties. 

Parameters: 
     

**aedt_object**
    
AEDT object. It can be oproject, odesign, oeditor or any of the objects to which the property belongs. 

**tab_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the tab to update. Options are `BaseElementTab`, `EM Design`, and `FieldsPostProcessorTab`. The default is `BaseElementTab`. 

**property_object**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the property object. 

**property_names**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of property names. For example, `["prop1", "prop2"]`. 

**property_values**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of property values corresponding to the property names. 

**property_types**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of property types corresponding to the property names. Values are `"Value"`, `"ButtonText"`, `"Hidden"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.ChangeProperty

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.change_properties(hfss.oeditor, "BaseElementTab", "Box1", ["Xpos", "Ypos"], ["0mm", "1mm"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.change_properties.rst.txt)

# change_properties 

Hfss3dLayout.change_properties(_aedt_object : [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _tab_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_object : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_names : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _property_values : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _property_types : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Change multiple properties. 

Parameters: 
     

**aedt_object**
    
AEDT object. It can be oproject, odesign, oeditor or any of the objects to which the property belongs. 

**tab_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the tab to update. Options are `BaseElementTab`, `EM Design`, and `FieldsPostProcessorTab`. The default is `BaseElementTab`. 

**property_object**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the property object. 

**property_names**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of property names. For example, `["prop1", "prop2"]`. 

**property_values**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of property values corresponding to the property names. 

**property_types**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of property types corresponding to the property names. Values are `"Value"`, `"ButtonText"`, `"Hidden"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.ChangeProperty

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.change_properties(hfss.oeditor, "BaseElementTab", "Box1", ["Xpos", "Ypos"], ["0mm", "1mm"])

```
Copy to clipboard