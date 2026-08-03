---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMData.range_doppler.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# range_doppler 

FRTMData.range_doppler(_channel : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Hann'_, _range_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _doppler_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Calculate the range-Doppler map of a frame. 

Parameters: 
     

**channel**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Channel name. The default is the first one. 

**window**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of window to apply in both Doppler and Range dimensions. The default is `"Hann"`. Options are `"Hann"`, `"Hamming"`, `"Flat"`, etc. 

**range_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of output bins in range (frequency) dimension. If not specified, uses the original number of frequencies. 

**doppler_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
     

Number of output bins in Doppler (pulse/time) dimension.
    
If not specified, uses the original number of CPI frames. 

Returns: 
     

[`numpy.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")
    
Range doppler array of shape (doppler_bins, range_bins), where: - Each column corresponds to a Doppler velocity bin. - Each row corresponds to a range bin.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMData
>>> file = "RxSignal.frtm"
>>> data = RangeDopplerData(file)
>>> channel_name = data.channel_names[0]
>>> range_doppler = data.range_doppler(channel_name)

```
Copy to clipboard
# range_doppler 

FRTMData.range_doppler(_channel : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Hann'_, _range_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _doppler_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Calculate the range-Doppler map of a frame. 

Parameters: 
     

**channel**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Channel name. The default is the first one. 

**window**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of window to apply in both Doppler and Range dimensions. The default is `"Hann"`. Options are `"Hann"`, `"Hamming"`, `"Flat"`, etc. 

**range_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of output bins in range (frequency) dimension. If not specified, uses the original number of frequencies. 

**doppler_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
     

Number of output bins in Doppler (pulse/time) dimension.
    
If not specified, uses the original number of CPI frames. 

Returns: 
     

[`numpy.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")
    
Range doppler array of shape (doppler_bins, range_bins), where: - Each column corresponds to a Doppler velocity bin. - Each row corresponds to a range bin.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMData
>>> file = "RxSignal.frtm"
>>> data = RangeDopplerData(file)
>>> channel_name = data.channel_names[0]
>>> range_doppler = data.range_doppler(channel_name)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMData.range_doppler.rst.txt)

# range_doppler 

FRTMData.range_doppler(_channel : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Hann'_, _range_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _doppler_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Calculate the range-Doppler map of a frame. 

Parameters: 
     

**channel**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Channel name. The default is the first one. 

**window**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of window to apply in both Doppler and Range dimensions. The default is `"Hann"`. Options are `"Hann"`, `"Hamming"`, `"Flat"`, etc. 

**range_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of output bins in range (frequency) dimension. If not specified, uses the original number of frequencies. 

**doppler_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
     

Number of output bins in Doppler (pulse/time) dimension.
    
If not specified, uses the original number of CPI frames. 

Returns: 
     

[`numpy.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")
    
Range doppler array of shape (doppler_bins, range_bins), where: - Each column corresponds to a Doppler velocity bin. - Each row corresponds to a range bin.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMData
>>> file = "RxSignal.frtm"
>>> data = RangeDopplerData(file)
>>> channel_name = data.channel_names[0]
>>> range_doppler = data.range_doppler(channel_name)

```
Copy to clipboard