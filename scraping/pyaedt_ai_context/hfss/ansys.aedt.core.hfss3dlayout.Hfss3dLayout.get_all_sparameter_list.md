---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.get_all_sparameter_list.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# get_all_sparameter_list 

property Hfss3dLayout.get_all_sparameter_list: [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of all S parameters for a list of excitations. 

Parameters: 
     

**excitation_names**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of excitations. The default is `None`, in which case the S parameters for all excitations are to be provided. For example, `["1", "2"]`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
Strings representing the S parameters of the excitations. For example, `["S(1, 1)", "S(1, 2)", S(2, 2)]`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.get_all_sparameter_list

```
Copy to clipboard
# get_all_sparameter_list 

property Hfss3dLayout.get_all_sparameter_list: [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of all S parameters for a list of excitations. 

Parameters: 
     

**excitation_names**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of excitations. The default is `None`, in which case the S parameters for all excitations are to be provided. For example, `["1", "2"]`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
Strings representing the S parameters of the excitations. For example, `["S(1, 1)", "S(1, 2)", S(2, 2)]`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.get_all_sparameter_list

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.get_all_sparameter_list.rst.txt)

# get_all_sparameter_list 

property Hfss3dLayout.get_all_sparameter_list: [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of all S parameters for a list of excitations. 

Parameters: 
     

**excitation_names**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of excitations. The default is `None`, in which case the S parameters for all excitations are to be provided. For example, `["1", "2"]`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
Strings representing the S parameters of the excitations. For example, `["S(1, 1)", "S(1, 2)", S(2, 2)]`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.get_all_sparameter_list

```
Copy to clipboard