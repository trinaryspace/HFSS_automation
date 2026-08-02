---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.get_property_value.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# get_property_value 

Hfss.get_property_value(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → any 
    
Retrieve a property value. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the object. 

**property_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the property. 

**property_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the property. Options are `"boundary"`, `"excitation"`, `"setup",` and `"mesh"`. The default is `None`. 

Returns: 
     

[`type`](https://docs.python.org/3.11/library/functions.html#type "\(in Python v3.11\)")
    
Value of the property.
References

```
>>> oDesign.GetPropertyValue

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.get_property_value("Box1", "Material", "boundary")

```
Copy to clipboard
# get_property_value 

Hfss.get_property_value(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → any 
    
Retrieve a property value. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the object. 

**property_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the property. 

**property_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the property. Options are `"boundary"`, `"excitation"`, `"setup",` and `"mesh"`. The default is `None`. 

Returns: 
     

[`type`](https://docs.python.org/3.11/library/functions.html#type "\(in Python v3.11\)")
    
Value of the property.
References

```
>>> oDesign.GetPropertyValue

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.get_property_value("Box1", "Material", "boundary")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.get_property_value.rst.txt)

# get_property_value 

Hfss.get_property_value(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → any 
    
Retrieve a property value. 

Parameters: 
     

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the object. 

**property_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the property. 

**property_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the property. Options are `"boundary"`, `"excitation"`, `"setup",` and `"mesh"`. The default is `None`. 

Returns: 
     

[`type`](https://docs.python.org/3.11/library/functions.html#type "\(in Python v3.11\)")
    
Value of the property.
References

```
>>> oDesign.GetPropertyValue

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.get_property_value("Box1", "Material", "boundary")

```
Copy to clipboard