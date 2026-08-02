---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_sbr_custom_array_file.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# create_sbr_custom_array_file 

Hfss.create_sbr_custom_array_file(_output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _frequencies : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _element_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _state_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _position : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _x_axis : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")] | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _y_axis : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")] | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _weight : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")] | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create custom array file with sarr format. 

Parameters: 
     

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path and name for the file. The default is `None`, in which case the file is exported to the working directory. 

**frequencies**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of frequencies in GHz. The default is `[1.0]`. 

**element_number**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of elements in the array. The default is `1`. 

**state_number**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of states. The default is `1`. 

**position**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates for each element. The default is `[1, 0, 0]`. 

**x_axis**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of X, Y, Z components of X-axis unit vector. 

**y_axis**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of X, Y, Z components of Y-axis unit vector. The default is `[0, 1, 0]`. 

**weight**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Weight of each element. The default is `None` in which case all elements have uniform weight. The second dimension contains the weights for each element, organized as follows: The first `frequencies` entries correspond to the weights for that element at each of the `frequencies`, for the first state. If there are multiple states, the next `frequencies` entries represent the weights for the second state, and so on. For example, for 3 frequencies `(f1, f2, f3)`, 2 elements `(e1, e2)`, and 2 states `(s1, s2)`, the weight would be represented as: `[[w_f1_e1_s1, w_f1_e2_s1], [w_f2_e1_s1, w_f2_e2_s1], [w_f3_e1_s1, w_f3_e2_s1], [w_f1_e1_s2, w_f1_e2_s2], [w_f2_e1_s2, w_f2_e2_s2], [w_f3_e1_s2, w_f3_e2_s2]]`. [``](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_sbr_custom_array_file.html#id1)[`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_sbr_custom_array_file.html#id3) 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
File name when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.create_sbr_custom_array_file()
>>> hfss.desktop_class.close_desktop()

```
Copy to clipboard
# create_sbr_custom_array_file 

Hfss.create_sbr_custom_array_file(_output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _frequencies : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _element_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _state_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _position : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _x_axis : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")] | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _y_axis : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")] | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _weight : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")] | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create custom array file with sarr format. 

Parameters: 
     

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path and name for the file. The default is `None`, in which case the file is exported to the working directory. 

**frequencies**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of frequencies in GHz. The default is `[1.0]`. 

**element_number**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of elements in the array. The default is `1`. 

**state_number**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of states. The default is `1`. 

**position**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates for each element. The default is `[1, 0, 0]`. 

**x_axis**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of X, Y, Z components of X-axis unit vector. 

**y_axis**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of X, Y, Z components of Y-axis unit vector. The default is `[0, 1, 0]`. 

**weight**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Weight of each element. The default is `None` in which case all elements have uniform weight. The second dimension contains the weights for each element, organized as follows: The first `frequencies` entries correspond to the weights for that element at each of the `frequencies`, for the first state. If there are multiple states, the next `frequencies` entries represent the weights for the second state, and so on. For example, for 3 frequencies `(f1, f2, f3)`, 2 elements `(e1, e2)`, and 2 states `(s1, s2)`, the weight would be represented as: `[[w_f1_e1_s1, w_f1_e2_s1], [w_f2_e1_s1, w_f2_e2_s1], [w_f3_e1_s1, w_f3_e2_s1], [w_f1_e1_s2, w_f1_e2_s2], [w_f2_e1_s2, w_f2_e2_s2], [w_f3_e1_s2, w_f3_e2_s2]]`. [``](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_sbr_custom_array_file.html#id1)[`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_sbr_custom_array_file.html#id3) 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
File name when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.create_sbr_custom_array_file()
>>> hfss.desktop_class.close_desktop()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_sbr_custom_array_file.rst.txt)

# create_sbr_custom_array_file 

Hfss.create_sbr_custom_array_file(_output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _frequencies : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _element_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _state_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _position : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _x_axis : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")] | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _y_axis : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")] | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _weight : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")] | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create custom array file with sarr format. 

Parameters: 
     

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path and name for the file. The default is `None`, in which case the file is exported to the working directory. 

**frequencies**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of frequencies in GHz. The default is `[1.0]`. 

**element_number**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of elements in the array. The default is `1`. 

**state_number**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of states. The default is `1`. 

**position**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[x, y, z]` coordinates for each element. The default is `[1, 0, 0]`. 

**x_axis**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of X, Y, Z components of X-axis unit vector. 

**y_axis**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of X, Y, Z components of Y-axis unit vector. The default is `[0, 1, 0]`. 

**weight**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Weight of each element. The default is `None` in which case all elements have uniform weight. The second dimension contains the weights for each element, organized as follows: The first `frequencies` entries correspond to the weights for that element at each of the `frequencies`, for the first state. If there are multiple states, the next `frequencies` entries represent the weights for the second state, and so on. For example, for 3 frequencies `(f1, f2, f3)`, 2 elements `(e1, e2)`, and 2 states `(s1, s2)`, the weight would be represented as: `[[w_f1_e1_s1, w_f1_e2_s1], [w_f2_e1_s1, w_f2_e2_s1], [w_f3_e1_s1, w_f3_e2_s1], [w_f1_e1_s2, w_f1_e2_s2], [w_f2_e1_s2, w_f2_e2_s2], [w_f3_e1_s2, w_f3_e2_s2]]`. [``](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_sbr_custom_array_file.html#id1)[`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_sbr_custom_array_file.html#id3) 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
File name when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.create_sbr_custom_array_file()
>>> hfss.desktop_class.close_desktop()

```
Copy to clipboard