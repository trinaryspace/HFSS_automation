---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.touchstone_parser.TouchstoneData.get_return_loss_index.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# get_return_loss_index 

TouchstoneData.get_return_loss_index(_excitation_name_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get the list of all the return loss from a list of excitations.
If no excitation is provided it will provide a full list of return losses.
Example: excitation_names [“1”,”2”] is_touchstone_expression=False output [“S(1,1)”, S(2,2)] Example: excitation_names [“S(1,1)”,”S(1,2)”, S(2,2)] is_touchstone_expression=True output [“S(1,1)”, S(2,2)] 

Parameters: 
     

**excitation_name_prefix :str, optional**
    
Prefix of the excitation. The default value is `""`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of index couples representing return losses of excitations.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.get_return_loss_index(excitation_name_prefix=1)

```
Copy to clipboard
# get_return_loss_index 

TouchstoneData.get_return_loss_index(_excitation_name_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get the list of all the return loss from a list of excitations.
If no excitation is provided it will provide a full list of return losses.
Example: excitation_names [“1”,”2”] is_touchstone_expression=False output [“S(1,1)”, S(2,2)] Example: excitation_names [“S(1,1)”,”S(1,2)”, S(2,2)] is_touchstone_expression=True output [“S(1,1)”, S(2,2)] 

Parameters: 
     

**excitation_name_prefix :str, optional**
    
Prefix of the excitation. The default value is `""`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of index couples representing return losses of excitations.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.get_return_loss_index(excitation_name_prefix=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.touchstone_parser.TouchstoneData.get_return_loss_index.rst.txt)

# get_return_loss_index 

TouchstoneData.get_return_loss_index(_excitation_name_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get the list of all the return loss from a list of excitations.
If no excitation is provided it will provide a full list of return losses.
Example: excitation_names [“1”,”2”] is_touchstone_expression=False output [“S(1,1)”, S(2,2)] Example: excitation_names [“S(1,1)”,”S(1,2)”, S(2,2)] is_touchstone_expression=True output [“S(1,1)”, S(2,2)] 

Parameters: 
     

**excitation_name_prefix :str, optional**
    
Prefix of the excitation. The default value is `""`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of index couples representing return losses of excitations.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.get_return_loss_index(excitation_name_prefix=1)

```
Copy to clipboard