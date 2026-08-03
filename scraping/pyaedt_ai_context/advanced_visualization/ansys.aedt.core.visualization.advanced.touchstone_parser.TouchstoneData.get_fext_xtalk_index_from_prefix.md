---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.touchstone_parser.TouchstoneData.get_fext_xtalk_index_from_prefix.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# get_fext_xtalk_index_from_prefix 

TouchstoneData.get_fext_xtalk_index_from_prefix(_tx_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _rx_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _skip_same_index_couples : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get the list of all the Far End XTalk from a list of excitations and a prefix that will be used to retrieve driver and receivers names. If skip_same_index_couples is true, the tx and rx with same index position will be considered insertion losses and excluded from the list. 

Parameters: 
     

**tx_prefix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
prefix for TX (eg. “DIE”) 

**rx_prefix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
prefix for RX (eg. “BGA”) 

**skip_same_index_couples**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Boolean ignore TX and RX couple with same index. The default value is `True`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of index couples representing Far End XTalks.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.get_fext_xtalk_index_from_prefix(tx_prefix=1, rx_prefix=1)

```
Copy to clipboard
# get_fext_xtalk_index_from_prefix 

TouchstoneData.get_fext_xtalk_index_from_prefix(_tx_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _rx_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _skip_same_index_couples : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get the list of all the Far End XTalk from a list of excitations and a prefix that will be used to retrieve driver and receivers names. If skip_same_index_couples is true, the tx and rx with same index position will be considered insertion losses and excluded from the list. 

Parameters: 
     

**tx_prefix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
prefix for TX (eg. “DIE”) 

**rx_prefix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
prefix for RX (eg. “BGA”) 

**skip_same_index_couples**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Boolean ignore TX and RX couple with same index. The default value is `True`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of index couples representing Far End XTalks.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.get_fext_xtalk_index_from_prefix(tx_prefix=1, rx_prefix=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.touchstone_parser.TouchstoneData.get_fext_xtalk_index_from_prefix.rst.txt)

# get_fext_xtalk_index_from_prefix 

TouchstoneData.get_fext_xtalk_index_from_prefix(_tx_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _rx_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _skip_same_index_couples : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get the list of all the Far End XTalk from a list of excitations and a prefix that will be used to retrieve driver and receivers names. If skip_same_index_couples is true, the tx and rx with same index position will be considered insertion losses and excluded from the list. 

Parameters: 
     

**tx_prefix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
prefix for TX (eg. “DIE”) 

**rx_prefix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
prefix for RX (eg. “BGA”) 

**skip_same_index_couples**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Boolean ignore TX and RX couple with same index. The default value is `True`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of index couples representing Far End XTalks.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.get_fext_xtalk_index_from_prefix(tx_prefix=1, rx_prefix=1)

```
Copy to clipboard