---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.get_all_insertion_loss_list.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# get_all_insertion_loss_list 

Hfss3dLayout.get_all_insertion_loss_list(_drivers : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _receivers : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _drivers_prefix_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _receivers_prefix_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _math_formula : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _nets : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Get a list of all insertion losses from two lists of excitations (driver and receiver). 

Parameters: 
     

**drivers**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of drivers. The default is `[]`. For example, `["1"]`. 

**receivers**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of receivers. The default is `[]`. The number of drivers equals the number of receivers. For example, `["2"]`. 

**drivers_prefix_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Prefix to add to driver names. For example, `"DIE"`. The default is `""`. 

**receivers_prefix_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Prefix to add to receiver names. For example, `"BGA"`. The default is `""`. 

**math_formula**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
One of the available AEDT mathematical formulas to apply. For example, `abs, dB`. 

**nets**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of nets to filter the output. The default is `None`, in which case all parameters are returned. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of strings representing insertion losses of the excitations. For example, `["S(1,2)"]`.
References

```
>>> oEditor.GetAllPorts

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()

```
Copy to clipboard

```
>>> # Example 1: Get insertion loss between specific driver and receiver pairs
>>> hfss.get_all_insertion_loss_list(
...     drivers=["Port1_TX", "Port2_TX", "Port3_TX"],
...     receivers=["Port1_RX", "Port2_RX", "Port3_RX"],
...     math_formula="dB",
... )
['dB(S(Port1_TX,Port1_RX))', 'dB(S(Port2_TX,Port2_RX))', 'dB(S(Port3_TX,Port3_RX))']

```
Copy to clipboard

```
>>> # Example 2: Get insertion loss using prefix filtering
>>> hfss.get_all_insertion_loss_list(drivers_prefix_name="DIE", receivers_prefix_name="BGA")
['S(DIE_Port1,BGA_Port1)', 'S(DIE_Port2,BGA_Port2)']

```
Copy to clipboard
# get_all_insertion_loss_list 

Hfss3dLayout.get_all_insertion_loss_list(_drivers : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _receivers : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _drivers_prefix_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _receivers_prefix_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _math_formula : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _nets : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Get a list of all insertion losses from two lists of excitations (driver and receiver). 

Parameters: 
     

**drivers**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of drivers. The default is `[]`. For example, `["1"]`. 

**receivers**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of receivers. The default is `[]`. The number of drivers equals the number of receivers. For example, `["2"]`. 

**drivers_prefix_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Prefix to add to driver names. For example, `"DIE"`. The default is `""`. 

**receivers_prefix_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Prefix to add to receiver names. For example, `"BGA"`. The default is `""`. 

**math_formula**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
One of the available AEDT mathematical formulas to apply. For example, `abs, dB`. 

**nets**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of nets to filter the output. The default is `None`, in which case all parameters are returned. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of strings representing insertion losses of the excitations. For example, `["S(1,2)"]`.
References

```
>>> oEditor.GetAllPorts

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()

```
Copy to clipboard

```
>>> # Example 1: Get insertion loss between specific driver and receiver pairs
>>> hfss.get_all_insertion_loss_list(
...     drivers=["Port1_TX", "Port2_TX", "Port3_TX"],
...     receivers=["Port1_RX", "Port2_RX", "Port3_RX"],
...     math_formula="dB",
... )
['dB(S(Port1_TX,Port1_RX))', 'dB(S(Port2_TX,Port2_RX))', 'dB(S(Port3_TX,Port3_RX))']

```
Copy to clipboard

```
>>> # Example 2: Get insertion loss using prefix filtering
>>> hfss.get_all_insertion_loss_list(drivers_prefix_name="DIE", receivers_prefix_name="BGA")
['S(DIE_Port1,BGA_Port1)', 'S(DIE_Port2,BGA_Port2)']

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.get_all_insertion_loss_list.rst.txt)

# get_all_insertion_loss_list 

Hfss3dLayout.get_all_insertion_loss_list(_drivers : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _receivers : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _drivers_prefix_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _receivers_prefix_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _math_formula : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _nets : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Get a list of all insertion losses from two lists of excitations (driver and receiver). 

Parameters: 
     

**drivers**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of drivers. The default is `[]`. For example, `["1"]`. 

**receivers**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of receivers. The default is `[]`. The number of drivers equals the number of receivers. For example, `["2"]`. 

**drivers_prefix_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Prefix to add to driver names. For example, `"DIE"`. The default is `""`. 

**receivers_prefix_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Prefix to add to receiver names. For example, `"BGA"`. The default is `""`. 

**math_formula**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
One of the available AEDT mathematical formulas to apply. For example, `abs, dB`. 

**nets**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of nets to filter the output. The default is `None`, in which case all parameters are returned. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of strings representing insertion losses of the excitations. For example, `["S(1,2)"]`.
References

```
>>> oEditor.GetAllPorts

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()

```
Copy to clipboard

```
>>> # Example 1: Get insertion loss between specific driver and receiver pairs
>>> hfss.get_all_insertion_loss_list(
...     drivers=["Port1_TX", "Port2_TX", "Port3_TX"],
...     receivers=["Port1_RX", "Port2_RX", "Port3_RX"],
...     math_formula="dB",
... )
['dB(S(Port1_TX,Port1_RX))', 'dB(S(Port2_TX,Port2_RX))', 'dB(S(Port3_TX,Port3_RX))']

```
Copy to clipboard

```
>>> # Example 2: Get insertion loss using prefix filtering
>>> hfss.get_all_insertion_loss_list(drivers_prefix_name="DIE", receivers_prefix_name="BGA")
['S(DIE_Port1,BGA_Port1)', 'S(DIE_Port2,BGA_Port2)']

```
Copy to clipboard