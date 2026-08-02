---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.set_oo_property_value.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# set_oo_property_value 

Hfss.set_oo_property_value(_aedt_object : [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _object_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _prop_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _value : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Change the property value of the object-oriented AEDT object. 

Parameters: 
     

**aedt_object**[`object`](https://docs.python.org/3.11/library/functions.html#object "\(in Python v3.11\)") 
    
AEDT object to search for the property on. It can be any oProperty. For example, oDesign. 

**object_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the object list. 

**prop_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Property name. 

**value**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Property value. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Values returned by method if any.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.set_oo_property_value(app.odesign, "Design Settings", "ModelDepth", "1mm")

```
Copy to clipboard
# set_oo_property_value 

Hfss.set_oo_property_value(_aedt_object : [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _object_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _prop_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _value : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Change the property value of the object-oriented AEDT object. 

Parameters: 
     

**aedt_object**[`object`](https://docs.python.org/3.11/library/functions.html#object "\(in Python v3.11\)") 
    
AEDT object to search for the property on. It can be any oProperty. For example, oDesign. 

**object_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the object list. 

**prop_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Property name. 

**value**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Property value. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Values returned by method if any.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.set_oo_property_value(app.odesign, "Design Settings", "ModelDepth", "1mm")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.set_oo_property_value.rst.txt)

# set_oo_property_value 

Hfss.set_oo_property_value(_aedt_object : [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _object_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _prop_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _value : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Change the property value of the object-oriented AEDT object. 

Parameters: 
     

**aedt_object**[`object`](https://docs.python.org/3.11/library/functions.html#object "\(in Python v3.11\)") 
    
AEDT object to search for the property on. It can be any oProperty. For example, oDesign. 

**object_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the object list. 

**prop_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Property name. 

**value**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Property value. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Values returned by method if any.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.set_oo_property_value(app.odesign, "Design Settings", "ModelDepth", "1mm")

```
Copy to clipboard