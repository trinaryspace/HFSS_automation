---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.touchstone_parser.TouchstoneData.get_insertion_loss_index.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# get_insertion_loss_index 

TouchstoneData.get_insertion_loss_index(_threshold : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = -3_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get all insertion losses.
The first frequency point is used to determine whether two ports are shorted. 

Parameters: 
     

**threshold**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Threshold to determine shorted ports in dB. The default value is `-3`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of index couples representing insertion losses of excitations.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.get_insertion_loss_index(threshold=1.0)

```
Copy to clipboard
# get_insertion_loss_index 

TouchstoneData.get_insertion_loss_index(_threshold : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = -3_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get all insertion losses.
The first frequency point is used to determine whether two ports are shorted. 

Parameters: 
     

**threshold**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Threshold to determine shorted ports in dB. The default value is `-3`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of index couples representing insertion losses of excitations.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.get_insertion_loss_index(threshold=1.0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.touchstone_parser.TouchstoneData.get_insertion_loss_index.rst.txt)

# get_insertion_loss_index 

TouchstoneData.get_insertion_loss_index(_threshold : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = -3_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get all insertion losses.
The first frequency point is used to determine whether two ports are shorted. 

Parameters: 
     

**threshold**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Threshold to determine shorted ports in dB. The default value is `-3`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of index couples representing insertion losses of excitations.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.get_insertion_loss_index(threshold=1.0)

```
Copy to clipboard