---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_icepak.PostProcessorIcepak.evaluate_object_quantity.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# evaluate_object_quantity 

PostProcessorIcepak.evaluate_object_quantity(_object_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _quantity_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _side : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Default'_, _volume : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _setup_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _ref_temperature : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _time : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0s'_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Export the field output on or in an object. 

Parameters: 
     

**object_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of object to perform the computation on. 

**quantity_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the quantity to export. 

**side**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Side of the mesh face to use. The default is `"Default"`. Options are `"Adjacent"`, `"Combined"`, and `"Default"`. 

**volume**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to compute the quantity on the volume or on the surface. The default is `False`. 

**setup_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup and name of the sweep. For example, `"IcepakSetup1 : SteatyState"`. The default is `None`, in which case the active setup and active sweep are used. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of parameters defined for the specific setup with values. The default is `{}`. 

**ref_temperature**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Reference temperature to use for heat transfer coefficient computation. The default is `""`. 

**time**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Timestep to get the data from. Default is `"0s"`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Output dictionary, which depending on the quantity chosen, contains one of these sets of keys:
  * `"Min"`, `"Max"`, `"Mean"`, `"Stdev"`, and `"Unit"`
  * `"Total"` and `"Unit"`

References

```
>>> oModule.ExportFieldsSummary

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.post_icepak import PostProcessorIcepak
>>> obj = PostProcessorIcepak()
>>> obj.evaluate_object_quantity(object_name=1, quantity_name=1)

```
Copy to clipboard
# evaluate_object_quantity 

PostProcessorIcepak.evaluate_object_quantity(_object_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _quantity_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _side : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Default'_, _volume : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _setup_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _ref_temperature : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _time : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0s'_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Export the field output on or in an object. 

Parameters: 
     

**object_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of object to perform the computation on. 

**quantity_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the quantity to export. 

**side**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Side of the mesh face to use. The default is `"Default"`. Options are `"Adjacent"`, `"Combined"`, and `"Default"`. 

**volume**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to compute the quantity on the volume or on the surface. The default is `False`. 

**setup_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup and name of the sweep. For example, `"IcepakSetup1 : SteatyState"`. The default is `None`, in which case the active setup and active sweep are used. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of parameters defined for the specific setup with values. The default is `{}`. 

**ref_temperature**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Reference temperature to use for heat transfer coefficient computation. The default is `""`. 

**time**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Timestep to get the data from. Default is `"0s"`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Output dictionary, which depending on the quantity chosen, contains one of these sets of keys:
  * `"Min"`, `"Max"`, `"Mean"`, `"Stdev"`, and `"Unit"`
  * `"Total"` and `"Unit"`

References

```
>>> oModule.ExportFieldsSummary

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.post_icepak import PostProcessorIcepak
>>> obj = PostProcessorIcepak()
>>> obj.evaluate_object_quantity(object_name=1, quantity_name=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_icepak.PostProcessorIcepak.evaluate_object_quantity.rst.txt)

# evaluate_object_quantity 

PostProcessorIcepak.evaluate_object_quantity(_object_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _quantity_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _side : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Default'_, _volume : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _setup_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _ref_temperature : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _time : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0s'_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Export the field output on or in an object. 

Parameters: 
     

**object_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of object to perform the computation on. 

**quantity_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the quantity to export. 

**side**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Side of the mesh face to use. The default is `"Default"`. Options are `"Adjacent"`, `"Combined"`, and `"Default"`. 

**volume**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to compute the quantity on the volume or on the surface. The default is `False`. 

**setup_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup and name of the sweep. For example, `"IcepakSetup1 : SteatyState"`. The default is `None`, in which case the active setup and active sweep are used. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of parameters defined for the specific setup with values. The default is `{}`. 

**ref_temperature**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Reference temperature to use for heat transfer coefficient computation. The default is `""`. 

**time**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Timestep to get the data from. Default is `"0s"`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Output dictionary, which depending on the quantity chosen, contains one of these sets of keys:
  * `"Min"`, `"Max"`, `"Mean"`, `"Stdev"`, and `"Unit"`
  * `"Total"` and `"Unit"`

References

```
>>> oModule.ExportFieldsSummary

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.post_icepak import PostProcessorIcepak
>>> obj = PostProcessorIcepak()
>>> obj.evaluate_object_quantity(object_name=1, quantity_name=1)

```
Copy to clipboard