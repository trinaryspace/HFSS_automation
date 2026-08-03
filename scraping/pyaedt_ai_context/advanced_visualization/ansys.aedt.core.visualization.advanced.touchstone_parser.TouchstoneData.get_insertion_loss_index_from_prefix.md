---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.touchstone_parser.TouchstoneData.get_insertion_loss_index_from_prefix.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# get_insertion_loss_index_from_prefix 

TouchstoneData.get_insertion_loss_index_from_prefix(_tx_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _rx_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get the list of all the insertion losses from prefix. 

Parameters: 
     

**tx_prefix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Prefix for TX (eg. “DIE”). 

**rx_prefix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Prefix for RX (eg. “BGA”). 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of index couples representing Insertion Losses of excitations.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.get_insertion_loss_index_from_prefix(tx_prefix=1, rx_prefix=1)

```
Copy to clipboard
# get_insertion_loss_index_from_prefix 

TouchstoneData.get_insertion_loss_index_from_prefix(_tx_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _rx_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get the list of all the insertion losses from prefix. 

Parameters: 
     

**tx_prefix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Prefix for TX (eg. “DIE”). 

**rx_prefix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Prefix for RX (eg. “BGA”). 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of index couples representing Insertion Losses of excitations.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.get_insertion_loss_index_from_prefix(tx_prefix=1, rx_prefix=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.touchstone_parser.TouchstoneData.get_insertion_loss_index_from_prefix.rst.txt)

# get_insertion_loss_index_from_prefix 

TouchstoneData.get_insertion_loss_index_from_prefix(_tx_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _rx_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get the list of all the insertion losses from prefix. 

Parameters: 
     

**tx_prefix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Prefix for TX (eg. “DIE”). 

**rx_prefix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Prefix for RX (eg. “BGA”). 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of index couples representing Insertion Losses of excitations.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.get_insertion_loss_index_from_prefix(tx_prefix=1, rx_prefix=1)

```
Copy to clipboard