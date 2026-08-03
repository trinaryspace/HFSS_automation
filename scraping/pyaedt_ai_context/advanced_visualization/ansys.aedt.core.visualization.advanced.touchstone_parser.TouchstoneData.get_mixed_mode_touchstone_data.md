---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.touchstone_parser.TouchstoneData.get_mixed_mode_touchstone_data.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# get_mixed_mode_touchstone_data 

TouchstoneData.get_mixed_mode_touchstone_data(_num_of_diff_ports : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _port_ordering : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1234'_) → TouchstoneData 
    
Transform network from single ended parameters to generalized mixed mode parameters. 

Parameters: 
     

**num_of_diff_ports**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
The number of differential ports. 

**port_ordering**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The current port ordering. Options are `"1234"`, `"1324"`. The default is `1234`. 

Returns: 
     

class:ansys.aedt.core.generic.touchstone_parser.TouchstoneData 
    
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.get_mixed_mode_touchstone_data(num_of_diff_ports=[1, 2, 3], port_ordering=1)

```
Copy to clipboard
# get_mixed_mode_touchstone_data 

TouchstoneData.get_mixed_mode_touchstone_data(_num_of_diff_ports : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _port_ordering : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1234'_) → TouchstoneData 
    
Transform network from single ended parameters to generalized mixed mode parameters. 

Parameters: 
     

**num_of_diff_ports**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
The number of differential ports. 

**port_ordering**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The current port ordering. Options are `"1234"`, `"1324"`. The default is `1234`. 

Returns: 
     

class:ansys.aedt.core.generic.touchstone_parser.TouchstoneData 
    
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.get_mixed_mode_touchstone_data(num_of_diff_ports=[1, 2, 3], port_ordering=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.touchstone_parser.TouchstoneData.get_mixed_mode_touchstone_data.rst.txt)

# get_mixed_mode_touchstone_data 

TouchstoneData.get_mixed_mode_touchstone_data(_num_of_diff_ports : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _port_ordering : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1234'_) → TouchstoneData 
    
Transform network from single ended parameters to generalized mixed mode parameters. 

Parameters: 
     

**num_of_diff_ports**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
The number of differential ports. 

**port_ordering**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The current port ordering. Options are `"1234"`, `"1324"`. The default is `1234`. 

Returns: 
     

class:ansys.aedt.core.generic.touchstone_parser.TouchstoneData 
    
Examples

```
>>> from ansys.aedt.core.visualization.advanced.touchstone_parser import TouchstoneData
>>> obj = TouchstoneData()
>>> obj.get_mixed_mode_touchstone_data(num_of_diff_ports=[1, 2, 3], port_ordering=1)

```
Copy to clipboard