---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_3dlayout.PostProcessor3DLayout.compute_power_by_net.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# compute_power_by_net 

PostProcessor3DLayout.compute_power_by_net(_nets : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Compute the power by nets. This applies only to SIwave DC Analysis. 

Parameters: 
     

**nets**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Layers to include in power calculation. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
SIwave DCIR solution. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Power by nets.
Examples

```
>>> from ansys.aedt.core.visualization.post.post_3dlayout import PostProcessor3DLayout
>>> obj = PostProcessor3DLayout()
>>> obj.compute_power_by_net(nets=["VCC"], solution=1)

```
Copy to clipboard
# compute_power_by_net 

PostProcessor3DLayout.compute_power_by_net(_nets : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Compute the power by nets. This applies only to SIwave DC Analysis. 

Parameters: 
     

**nets**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Layers to include in power calculation. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
SIwave DCIR solution. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Power by nets.
Examples

```
>>> from ansys.aedt.core.visualization.post.post_3dlayout import PostProcessor3DLayout
>>> obj = PostProcessor3DLayout()
>>> obj.compute_power_by_net(nets=["VCC"], solution=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_3dlayout.PostProcessor3DLayout.compute_power_by_net.rst.txt)

# compute_power_by_net 

PostProcessor3DLayout.compute_power_by_net(_nets : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Compute the power by nets. This applies only to SIwave DC Analysis. 

Parameters: 
     

**nets**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Layers to include in power calculation. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
SIwave DCIR solution. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Power by nets.
Examples

```
>>> from ansys.aedt.core.visualization.post.post_3dlayout import PostProcessor3DLayout
>>> obj = PostProcessor3DLayout()
>>> obj.compute_power_by_net(nets=["VCC"], solution=1)

```
Copy to clipboard