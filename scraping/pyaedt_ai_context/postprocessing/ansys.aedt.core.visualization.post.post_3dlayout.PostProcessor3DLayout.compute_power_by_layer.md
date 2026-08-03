---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_3dlayout.PostProcessor3DLayout.compute_power_by_layer.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# compute_power_by_layer 

PostProcessor3DLayout.compute_power_by_layer(_layers : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Compute the power by layer.
This applies only to SIwave DC Analysis. 

Parameters: 
     

**layers**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Layers to include in power calculation. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
SIwave DCIR solution. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Power by layer.
Examples

```
>>> from ansys.aedt.core.visualization.post.post_3dlayout import PostProcessor3DLayout
>>> obj = PostProcessor3DLayout()
>>> obj.compute_power_by_layer(layers=["TOP"], solution=1)

```
Copy to clipboard
# compute_power_by_layer 

PostProcessor3DLayout.compute_power_by_layer(_layers : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Compute the power by layer.
This applies only to SIwave DC Analysis. 

Parameters: 
     

**layers**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Layers to include in power calculation. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
SIwave DCIR solution. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Power by layer.
Examples

```
>>> from ansys.aedt.core.visualization.post.post_3dlayout import PostProcessor3DLayout
>>> obj = PostProcessor3DLayout()
>>> obj.compute_power_by_layer(layers=["TOP"], solution=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_3dlayout.PostProcessor3DLayout.compute_power_by_layer.rst.txt)

# compute_power_by_layer 

PostProcessor3DLayout.compute_power_by_layer(_layers : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Compute the power by layer.
This applies only to SIwave DC Analysis. 

Parameters: 
     

**layers**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Layers to include in power calculation. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
SIwave DCIR solution. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Power by layer.
Examples

```
>>> from ansys.aedt.core.visualization.post.post_3dlayout import PostProcessor3DLayout
>>> obj = PostProcessor3DLayout()
>>> obj.compute_power_by_layer(layers=["TOP"], solution=1)

```
Copy to clipboard