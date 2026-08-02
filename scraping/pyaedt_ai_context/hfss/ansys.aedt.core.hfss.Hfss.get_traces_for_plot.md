---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.get_traces_for_plot.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# get_traces_for_plot 

Hfss.get_traces_for_plot(_get_self_terms : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _get_mutual_terms : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _first_element_filter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _second_element_filter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'dB(S'_, _differential_pairs : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve a list of traces of specified designs ready to use in plot reports. 

Parameters: 
     

**get_self_terms**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to return self terms. The default is `True`. 

**get_mutual_terms**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to return mutual terms. The default is `True`. 

**first_element_filter**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Filter to apply to the first element of the equation. This parameter accepts `*` and `?` as special characters. The default is `None`. 

**second_element_filter**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Filter to apply to the second element of the equation. This parameter accepts `*` and `?` as special characters. The default is `None`. 

**category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot category name as in the report (including operator). The default is `"dB(S)"`, which is the plot category name for capacitance. 

**differential_pairs**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Differential pairs defined. The default is `None` in which case an empty list is set. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of traces of specified designs ready to use in plot reports.
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss = Hfss3dLayout(project_path)
>>> hfss.get_traces_for_plot(first_element_filter="Bo?1", second_element_filter="GND*", category="dB(S")
>>> hfss.get_traces_for_plot(
...     differential_pairs=["Diff_U0_data0", "Diff_U1_data0", "Diff_U1_data1"],
...     first_element_filter="*_U1_data?",
...     second_element_filter="*_U0_*",
...     category="dB(S",
... )

```
Copy to clipboard
# get_traces_for_plot 

Hfss.get_traces_for_plot(_get_self_terms : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _get_mutual_terms : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _first_element_filter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _second_element_filter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'dB(S'_, _differential_pairs : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve a list of traces of specified designs ready to use in plot reports. 

Parameters: 
     

**get_self_terms**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to return self terms. The default is `True`. 

**get_mutual_terms**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to return mutual terms. The default is `True`. 

**first_element_filter**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Filter to apply to the first element of the equation. This parameter accepts `*` and `?` as special characters. The default is `None`. 

**second_element_filter**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Filter to apply to the second element of the equation. This parameter accepts `*` and `?` as special characters. The default is `None`. 

**category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot category name as in the report (including operator). The default is `"dB(S)"`, which is the plot category name for capacitance. 

**differential_pairs**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Differential pairs defined. The default is `None` in which case an empty list is set. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of traces of specified designs ready to use in plot reports.
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss = Hfss3dLayout(project_path)
>>> hfss.get_traces_for_plot(first_element_filter="Bo?1", second_element_filter="GND*", category="dB(S")
>>> hfss.get_traces_for_plot(
...     differential_pairs=["Diff_U0_data0", "Diff_U1_data0", "Diff_U1_data1"],
...     first_element_filter="*_U1_data?",
...     second_element_filter="*_U0_*",
...     category="dB(S",
... )

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.get_traces_for_plot.rst.txt)

# get_traces_for_plot 

Hfss.get_traces_for_plot(_get_self_terms : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _get_mutual_terms : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _first_element_filter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _second_element_filter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'dB(S'_, _differential_pairs : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Retrieve a list of traces of specified designs ready to use in plot reports. 

Parameters: 
     

**get_self_terms**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to return self terms. The default is `True`. 

**get_mutual_terms**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to return mutual terms. The default is `True`. 

**first_element_filter**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Filter to apply to the first element of the equation. This parameter accepts `*` and `?` as special characters. The default is `None`. 

**second_element_filter**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Filter to apply to the second element of the equation. This parameter accepts `*` and `?` as special characters. The default is `None`. 

**category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot category name as in the report (including operator). The default is `"dB(S)"`, which is the plot category name for capacitance. 

**differential_pairs**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Differential pairs defined. The default is `None` in which case an empty list is set. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of traces of specified designs ready to use in plot reports.
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss = Hfss3dLayout(project_path)
>>> hfss.get_traces_for_plot(first_element_filter="Bo?1", second_element_filter="GND*", category="dB(S")
>>> hfss.get_traces_for_plot(
...     differential_pairs=["Diff_U0_data0", "Diff_U1_data0", "Diff_U1_data1"],
...     first_element_filter="*_U1_data?",
...     second_element_filter="*_U0_*",
...     category="dB(S",
... )

```
Copy to clipboard