---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.change_property.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# change_property 

Hfss.change_property(_aedt_object : [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _tab_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_object : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_value : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Change a property. 

Parameters: 
     

**aedt_object**
    
AEDT object. It can be oproject, odesign, oeditor or any of the objects to which the property belongs. 

**tab_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the tab to update. Options are `BaseElementTab`, `EM Design`, and `FieldsPostProcessorTab`. The default is `BaseElementTab`. 

**property_object**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the property object. It can be the name of an excitation or field reporter. For example, `Excitations:Port1` or `FieldsReporter:Mag_H`. 

**property_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the property. 

**property_value**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Value of the property. It is a string for a single value and a list of three elements for `[x,y,z]` coordianates. If property_name is a list, this should be a list of corresponding values. 

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
>>> hfss.change_property(hfss.oeditor, "BaseElementTab", "Box1", "Xpos", "0mm")

```
Copy to clipboard
# change_property 

Hfss.change_property(_aedt_object : [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _tab_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_object : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_value : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Change a property. 

Parameters: 
     

**aedt_object**
    
AEDT object. It can be oproject, odesign, oeditor or any of the objects to which the property belongs. 

**tab_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the tab to update. Options are `BaseElementTab`, `EM Design`, and `FieldsPostProcessorTab`. The default is `BaseElementTab`. 

**property_object**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the property object. It can be the name of an excitation or field reporter. For example, `Excitations:Port1` or `FieldsReporter:Mag_H`. 

**property_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the property. 

**property_value**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Value of the property. It is a string for a single value and a list of three elements for `[x,y,z]` coordianates. If property_name is a list, this should be a list of corresponding values. 

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
>>> hfss.change_property(hfss.oeditor, "BaseElementTab", "Box1", "Xpos", "0mm")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.change_property.rst.txt)

# change_property 

Hfss.change_property(_aedt_object : [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _tab_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_object : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_value : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Change a property. 

Parameters: 
     

**aedt_object**
    
AEDT object. It can be oproject, odesign, oeditor or any of the objects to which the property belongs. 

**tab_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the tab to update. Options are `BaseElementTab`, `EM Design`, and `FieldsPostProcessorTab`. The default is `BaseElementTab`. 

**property_object**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the property object. It can be the name of an excitation or field reporter. For example, `Excitations:Port1` or `FieldsReporter:Mag_H`. 

**property_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the property. 

**property_value**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Value of the property. It is a string for a single value and a list of three elements for `[x,y,z]` coordianates. If property_name is a list, this should be a list of corresponding values. 

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
>>> hfss.change_property(hfss.oeditor, "BaseElementTab", "Box1", "Xpos", "0mm")

```
Copy to clipboard