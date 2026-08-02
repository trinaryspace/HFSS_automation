---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.get_all_return_loss_list.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# get_all_return_loss_list 

Hfss.get_all_return_loss_list(_excitations : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _excitation_name_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _math_formula : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _nets : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get a list of all return losses for a list of excitations. 

Parameters: 
     

**excitations**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of excitations. The default is `None`, in which case the return losses for all excitations are provided. For example `["1", "2"]`. 

**excitation_name_prefix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Prefix to add to the excitation names. The default is `""`, 

**math_formula**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
One of the available AEDT mathematical formulas to apply. For example, `abs, dB`. 

**nets**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of nets to filter the output. The default is `None`, in which case all parameters are returned. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of strings representing the return losses of the excitations. For example, `["S(1, 1)", S(2, 2)]`.
References

```
>>> oEditor.GetAllPorts

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.get_all_return_loss_list(math_formula="dB")

```
Copy to clipboard
# get_all_return_loss_list 

Hfss.get_all_return_loss_list(_excitations : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _excitation_name_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _math_formula : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _nets : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get a list of all return losses for a list of excitations. 

Parameters: 
     

**excitations**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of excitations. The default is `None`, in which case the return losses for all excitations are provided. For example `["1", "2"]`. 

**excitation_name_prefix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Prefix to add to the excitation names. The default is `""`, 

**math_formula**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
One of the available AEDT mathematical formulas to apply. For example, `abs, dB`. 

**nets**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of nets to filter the output. The default is `None`, in which case all parameters are returned. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of strings representing the return losses of the excitations. For example, `["S(1, 1)", S(2, 2)]`.
References

```
>>> oEditor.GetAllPorts

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.get_all_return_loss_list(math_formula="dB")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.get_all_return_loss_list.rst.txt)

# get_all_return_loss_list 

Hfss.get_all_return_loss_list(_excitations : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _excitation_name_prefix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _math_formula : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _nets : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get a list of all return losses for a list of excitations. 

Parameters: 
     

**excitations**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of excitations. The default is `None`, in which case the return losses for all excitations are provided. For example `["1", "2"]`. 

**excitation_name_prefix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Prefix to add to the excitation names. The default is `""`, 

**math_formula**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
One of the available AEDT mathematical formulas to apply. For example, `abs, dB`. 

**nets**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of nets to filter the output. The default is `None`, in which case all parameters are returned. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
List of strings representing the return losses of the excitations. For example, `["S(1, 1)", S(2, 2)]`.
References

```
>>> oEditor.GetAllPorts

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.get_all_return_loss_list(math_formula="dB")

```
Copy to clipboard