---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_icepak.PostProcessorIcepak.power_budget.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# power_budget 

PostProcessorIcepak.power_budget(_units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'W'_, _temperature : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 22_, _output_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'component'_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Power budget calculation. 

Parameters: 
     

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Output power units. The default is `"W"`. 

**temperature**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Temperature to calculate the power. The default is `22`. 

**output_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Output data presentation. The default is `"component"`. The options are `"component"`, or `"boundary"`. `"component"` returns the power based on each component. `"boundary"` returns the power based on each boundary. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Dictionary with the power introduced on each boundary and total power.
References

```
>>> oEditor.ChangeProperty

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.post_icepak import PostProcessorIcepak
>>> obj = PostProcessorIcepak()
>>> obj.power_budget(units="mm", temperature=1)

```
Copy to clipboard
# power_budget 

PostProcessorIcepak.power_budget(_units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'W'_, _temperature : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 22_, _output_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'component'_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Power budget calculation. 

Parameters: 
     

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Output power units. The default is `"W"`. 

**temperature**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Temperature to calculate the power. The default is `22`. 

**output_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Output data presentation. The default is `"component"`. The options are `"component"`, or `"boundary"`. `"component"` returns the power based on each component. `"boundary"` returns the power based on each boundary. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Dictionary with the power introduced on each boundary and total power.
References

```
>>> oEditor.ChangeProperty

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.post_icepak import PostProcessorIcepak
>>> obj = PostProcessorIcepak()
>>> obj.power_budget(units="mm", temperature=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_icepak.PostProcessorIcepak.power_budget.rst.txt)

# power_budget 

PostProcessorIcepak.power_budget(_units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'W'_, _temperature : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 22_, _output_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'component'_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Power budget calculation. 

Parameters: 
     

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Output power units. The default is `"W"`. 

**temperature**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Temperature to calculate the power. The default is `22`. 

**output_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Output data presentation. The default is `"component"`. The options are `"component"`, or `"boundary"`. `"component"` returns the power based on each component. `"boundary"` returns the power based on each boundary. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Dictionary with the power introduced on each boundary and total power.
References

```
>>> oEditor.ChangeProperty

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.post_icepak import PostProcessorIcepak
>>> obj = PostProcessorIcepak()
>>> obj.power_budget(units="mm", temperature=1)

```
Copy to clipboard