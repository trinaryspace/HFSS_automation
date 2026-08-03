---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_3dlayout.PostProcessor3DLayout.get_efields_data.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# get_efields_data 

PostProcessor3DLayout.get_efields_data(_setup_sweep_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _ff_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Infinite Sphere1'_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [Any](https://docs.python.org/3.11/library/typing.html#typing.Any "\(in Python v3.11\)")] 
    
Compute Etheta and EPhi.
Warning
This method requires NumPy to be installed on your machine. 

Parameters: 
     

**setup_sweep_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup for computing the report. The default is `""`, in which case the nominal adaptive is applied. 

**ff_setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Far field setup. The default is `"Infinite Sphere1"`. 

Returns: 
     

[`np.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")
    
Numpy array containing `[theta_range, phi_range, Etheta, Ephi]`.
Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.get_efields_data(setup_sweep_name=1, ff_setup=1)

```
Copy to clipboard
# get_efields_data 

PostProcessor3DLayout.get_efields_data(_setup_sweep_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _ff_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Infinite Sphere1'_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [Any](https://docs.python.org/3.11/library/typing.html#typing.Any "\(in Python v3.11\)")] 
    
Compute Etheta and EPhi.
Warning
This method requires NumPy to be installed on your machine. 

Parameters: 
     

**setup_sweep_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup for computing the report. The default is `""`, in which case the nominal adaptive is applied. 

**ff_setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Far field setup. The default is `"Infinite Sphere1"`. 

Returns: 
     

[`np.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")
    
Numpy array containing `[theta_range, phi_range, Etheta, Ephi]`.
Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.get_efields_data(setup_sweep_name=1, ff_setup=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_3dlayout.PostProcessor3DLayout.get_efields_data.rst.txt)

# get_efields_data 

PostProcessor3DLayout.get_efields_data(_setup_sweep_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _ff_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Infinite Sphere1'_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [Any](https://docs.python.org/3.11/library/typing.html#typing.Any "\(in Python v3.11\)")] 
    
Compute Etheta and EPhi.
Warning
This method requires NumPy to be installed on your machine. 

Parameters: 
     

**setup_sweep_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup for computing the report. The default is `""`, in which case the nominal adaptive is applied. 

**ff_setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Far field setup. The default is `"Infinite Sphere1"`. 

Returns: 
     

[`np.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")
    
Numpy array containing `[theta_range, phi_range, Etheta, Ephi]`.
Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.get_efields_data(setup_sweep_name=1, ff_setup=1)

```
Copy to clipboard