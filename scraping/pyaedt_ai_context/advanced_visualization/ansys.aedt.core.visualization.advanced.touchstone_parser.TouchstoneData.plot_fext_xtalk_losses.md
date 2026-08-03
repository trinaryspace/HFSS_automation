---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.touchstone_parser.TouchstoneData.plot_fext_xtalk_losses.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# plot_fext_xtalk_losses 

TouchstoneData.plot_fext_xtalk_losses(_tx_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _rx_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _skip_same_index_couples : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Plot all fext crosstalk curves. 

Parameters: 
     

**tx_prefix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Prefix for TX (eg. “DIE”). 

**rx_prefix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Prefix for RX (eg. “BGA”). 

**skip_same_index_couples**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Boolean ignore TX and RX couple with same index. The default value is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.plot_fext_xtalk_losses(tx_prefix=1, rx_prefix=1)

```
Copy to clipboard
# plot_fext_xtalk_losses 

TouchstoneData.plot_fext_xtalk_losses(_tx_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _rx_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _skip_same_index_couples : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Plot all fext crosstalk curves. 

Parameters: 
     

**tx_prefix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Prefix for TX (eg. “DIE”). 

**rx_prefix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Prefix for RX (eg. “BGA”). 

**skip_same_index_couples**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Boolean ignore TX and RX couple with same index. The default value is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.plot_fext_xtalk_losses(tx_prefix=1, rx_prefix=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.touchstone_parser.TouchstoneData.plot_fext_xtalk_losses.rst.txt)

# plot_fext_xtalk_losses 

TouchstoneData.plot_fext_xtalk_losses(_tx_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _rx_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _skip_same_index_couples : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Plot all fext crosstalk curves. 

Parameters: 
     

**tx_prefix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Prefix for TX (eg. “DIE”). 

**rx_prefix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Prefix for RX (eg. “BGA”). 

**skip_same_index_couples**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Boolean ignore TX and RX couple with same index. The default value is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.plot_fext_xtalk_losses(tx_prefix=1, rx_prefix=1)

```
Copy to clipboard