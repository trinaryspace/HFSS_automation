---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMData.convert_frequency_range.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# convert_frequency_range 

FRTMData.convert_frequency_range(_pulse : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _size : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Convert frequency domain radar data to range domain using IFFT with optional windowing and resampling.
This method applies a window to the frequency-domain radar data, scales it for energy preservation, and then computes the IFFT to convert to range domain. It supports optional up and down-sampling to a specified size. 

pulse: int, optional
    
Index of the pulse to extract. The default is `None` in which case the center pulse (middle index) is used. 

window: str, optional
    
Type of window. The default is `None`. Available options are `"Hann"`, `"Hamming"`, and `"Flat"`. 

size: int, optional
    
Output number of samples. The default is `None`. 

Returns: 
     

[`numpy.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")
    
Range domain data.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMData
>>> file = "RxSignal.frtm"
>>> data = RangeDopplerData(file)
>>> data_range = data.convert_frequency_range()

```
Copy to clipboard
# convert_frequency_range 

FRTMData.convert_frequency_range(_pulse : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _size : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Convert frequency domain radar data to range domain using IFFT with optional windowing and resampling.
This method applies a window to the frequency-domain radar data, scales it for energy preservation, and then computes the IFFT to convert to range domain. It supports optional up and down-sampling to a specified size. 

pulse: int, optional
    
Index of the pulse to extract. The default is `None` in which case the center pulse (middle index) is used. 

window: str, optional
    
Type of window. The default is `None`. Available options are `"Hann"`, `"Hamming"`, and `"Flat"`. 

size: int, optional
    
Output number of samples. The default is `None`. 

Returns: 
     

[`numpy.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")
    
Range domain data.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMData
>>> file = "RxSignal.frtm"
>>> data = RangeDopplerData(file)
>>> data_range = data.convert_frequency_range()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMData.convert_frequency_range.rst.txt)

# convert_frequency_range 

FRTMData.convert_frequency_range(_pulse : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _size : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Convert frequency domain radar data to range domain using IFFT with optional windowing and resampling.
This method applies a window to the frequency-domain radar data, scales it for energy preservation, and then computes the IFFT to convert to range domain. It supports optional up and down-sampling to a specified size. 

pulse: int, optional
    
Index of the pulse to extract. The default is `None` in which case the center pulse (middle index) is used. 

window: str, optional
    
Type of window. The default is `None`. Available options are `"Hann"`, `"Hamming"`, and `"Flat"`. 

size: int, optional
    
Output number of samples. The default is `None`. 

Returns: 
     

[`numpy.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")
    
Range domain data.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMData
>>> file = "RxSignal.frtm"
>>> data = RangeDopplerData(file)
>>> data_range = data.convert_frequency_range()

```
Copy to clipboard