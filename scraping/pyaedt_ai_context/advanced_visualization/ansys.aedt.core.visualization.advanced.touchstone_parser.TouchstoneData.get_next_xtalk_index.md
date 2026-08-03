---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.touchstone_parser.TouchstoneData.get_next_xtalk_index.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# get_next_xtalk_index 

TouchstoneData.get_next_xtalk_index(_tx_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get the list of all the Near End XTalk a list of excitation.
Optionally prefix can be used to retrieve driver names. Example: excitation_names [“1”, “2”, “3”] output [“S(1,2)”, “S(1,3)”, “S(2,3)”]. 

Parameters: 
     

**tx_prefix :str, optional**
    
Prefix for TX (eg. “DIE”). The default value is `""`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of index couples representing Near End XTalks.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.get_next_xtalk_index(tx_prefix=1)

```
Copy to clipboard
# get_next_xtalk_index 

TouchstoneData.get_next_xtalk_index(_tx_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get the list of all the Near End XTalk a list of excitation.
Optionally prefix can be used to retrieve driver names. Example: excitation_names [“1”, “2”, “3”] output [“S(1,2)”, “S(1,3)”, “S(2,3)”]. 

Parameters: 
     

**tx_prefix :str, optional**
    
Prefix for TX (eg. “DIE”). The default value is `""`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of index couples representing Near End XTalks.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.get_next_xtalk_index(tx_prefix=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.touchstone_parser.TouchstoneData.get_next_xtalk_index.rst.txt)

# get_next_xtalk_index 

TouchstoneData.get_next_xtalk_index(_tx_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get the list of all the Near End XTalk a list of excitation.
Optionally prefix can be used to retrieve driver names. Example: excitation_names [“1”, “2”, “3”] output [“S(1,2)”, “S(1,3)”, “S(2,3)”]. 

Parameters: 
     

**tx_prefix :str, optional**
    
Prefix for TX (eg. “DIE”). The default value is `""`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of index couples representing Near End XTalks.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.get_next_xtalk_index(tx_prefix=1)

```
Copy to clipboard