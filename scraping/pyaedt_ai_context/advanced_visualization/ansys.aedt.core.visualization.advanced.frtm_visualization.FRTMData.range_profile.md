---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMData.range_profile.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# range_profile 

FRTMData.range_profile(_data : [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _size : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Calculate the range profile of a specific CPI frame. 

Parameters: 
     

**data**[`numpy.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Array of complex samples with `frequency_number` elements. 

**window: str, optional**
    
Type of window. The default is `None`. Available options are `"Hann"`, `"Hamming"`, and `"Flat"`. 

**size: int, optional**
    
Output number of samples. The default is `None`. 

Returns: 
     

[`numpy.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")
    
Range profile data.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMData
>>> file = "RxSignal.frtm"
>>> data = RangeDopplerData(file)
>>> channel_name = data.channel_names[0]
>>> data_channel_1 = data.all_data[channel_name]
>>> data_pulse_0 = data_channel_1[0]
>>> range_profile = data.range_profile(data_pulse_0)

```
Copy to clipboard
# range_profile 

FRTMData.range_profile(_data : [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _size : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Calculate the range profile of a specific CPI frame. 

Parameters: 
     

**data**[`numpy.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Array of complex samples with `frequency_number` elements. 

**window: str, optional**
    
Type of window. The default is `None`. Available options are `"Hann"`, `"Hamming"`, and `"Flat"`. 

**size: int, optional**
    
Output number of samples. The default is `None`. 

Returns: 
     

[`numpy.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")
    
Range profile data.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMData
>>> file = "RxSignal.frtm"
>>> data = RangeDopplerData(file)
>>> channel_name = data.channel_names[0]
>>> data_channel_1 = data.all_data[channel_name]
>>> data_pulse_0 = data_channel_1[0]
>>> range_profile = data.range_profile(data_pulse_0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMData.range_profile.rst.txt)

# range_profile 

FRTMData.range_profile(_data : [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _size : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Calculate the range profile of a specific CPI frame. 

Parameters: 
     

**data**[`numpy.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Array of complex samples with `frequency_number` elements. 

**window: str, optional**
    
Type of window. The default is `None`. Available options are `"Hann"`, `"Hamming"`, and `"Flat"`. 

**size: int, optional**
    
Output number of samples. The default is `None`. 

Returns: 
     

[`numpy.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")
    
Range profile data.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMData
>>> file = "RxSignal.frtm"
>>> data = RangeDopplerData(file)
>>> channel_name = data.channel_names[0]
>>> data_channel_1 = data.all_data[channel_name]
>>> data_pulse_0 = data_channel_1[0]
>>> range_profile = data.range_profile(data_pulse_0)

```
Copy to clipboard