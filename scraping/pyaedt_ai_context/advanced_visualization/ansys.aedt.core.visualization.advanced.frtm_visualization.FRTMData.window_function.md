---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMData.window_function.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# window_function 

static FRTMData.window_function(_window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Flat'_, _size : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 512_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Window function. 

Parameters: 
     

**window**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), optional. 
    
Window function. The default is `"Flat"`. Options are `"Flat"`, `"Hamming`”, and `"Hann"`. 

**size**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Window size. The default is `512`. 

Returns: 
     

[`numpy.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")
    
The window with the maximum value normalized to one.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMData
>>> file = "RxSignal.frtm"
>>> data = RangeDopplerData(file)
>>> window = data.window_function("Hann")

```
Copy to clipboard
# window_function 

static FRTMData.window_function(_window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Flat'_, _size : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 512_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Window function. 

Parameters: 
     

**window**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), optional. 
    
Window function. The default is `"Flat"`. Options are `"Flat"`, `"Hamming`”, and `"Hann"`. 

**size**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Window size. The default is `512`. 

Returns: 
     

[`numpy.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")
    
The window with the maximum value normalized to one.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMData
>>> file = "RxSignal.frtm"
>>> data = RangeDopplerData(file)
>>> window = data.window_function("Hann")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMData.window_function.rst.txt)

# window_function 

static FRTMData.window_function(_window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Flat'_, _size : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 512_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Window function. 

Parameters: 
     

**window**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), optional. 
    
Window function. The default is `"Flat"`. Options are `"Flat"`, `"Hamming`”, and `"Hann"`. 

**size**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Window size. The default is `512`. 

Returns: 
     

[`numpy.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")
    
The window with the maximum value normalized to one.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMData
>>> file = "RxSignal.frtm"
>>> data = RangeDopplerData(file)
>>> window = data.window_function("Hann")

```
Copy to clipboard