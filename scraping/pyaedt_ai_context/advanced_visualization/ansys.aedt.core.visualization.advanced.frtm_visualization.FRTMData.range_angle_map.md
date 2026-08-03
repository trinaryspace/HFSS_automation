---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMData.range_angle_map.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# range_angle_map 

FRTMData.range_angle_map(_pulse : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _range_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _cross_range_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _doa_method : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _field_of_view : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _range_bin_index : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Compute the range-angle map using direction of arrival estimation methods. 

Parameters: 
     

**pulse: int, optional**
    
Index of the pulse to extract. The default is `None` in which case the center pulse (middle index) is used. 

**window: str, optional**
    
Type of window. The default is `None`. Available options are `"Hann"`, `"Hamming"`, and `"Flat"`. 

**range_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of bins to use in the range (frequency) dimension. If `None`, number of channels is used. 

**cross_range_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of bins in the angular (azimuth) dimension. If `None`, `181` bins are used. 

**doa_method**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Direction of arrival estimation method. Options are `"Bartlett"`, `"Capon"`, and `"MUSIC"`. The default is `"Bartlett"`. 

**field_of_view**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Azimuth angular span in degrees to analyze. The default is `[-90, 90]`. 

**range_bin_index**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Specific range bin index to extract the angular profile. If provided, only that bin is used. 

Returns: 
     

[`np.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")
    
Data representing the range-angle intensity map.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMData
>>> file = "RxSignal.frtm"
>>> data = RangeDopplerData(file)
>>> range_angle_map = data.range_angle_map()

```
Copy to clipboard
# range_angle_map 

FRTMData.range_angle_map(_pulse : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _range_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _cross_range_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _doa_method : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _field_of_view : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _range_bin_index : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Compute the range-angle map using direction of arrival estimation methods. 

Parameters: 
     

**pulse: int, optional**
    
Index of the pulse to extract. The default is `None` in which case the center pulse (middle index) is used. 

**window: str, optional**
    
Type of window. The default is `None`. Available options are `"Hann"`, `"Hamming"`, and `"Flat"`. 

**range_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of bins to use in the range (frequency) dimension. If `None`, number of channels is used. 

**cross_range_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of bins in the angular (azimuth) dimension. If `None`, `181` bins are used. 

**doa_method**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Direction of arrival estimation method. Options are `"Bartlett"`, `"Capon"`, and `"MUSIC"`. The default is `"Bartlett"`. 

**field_of_view**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Azimuth angular span in degrees to analyze. The default is `[-90, 90]`. 

**range_bin_index**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Specific range bin index to extract the angular profile. If provided, only that bin is used. 

Returns: 
     

[`np.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")
    
Data representing the range-angle intensity map.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMData
>>> file = "RxSignal.frtm"
>>> data = RangeDopplerData(file)
>>> range_angle_map = data.range_angle_map()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMData.range_angle_map.rst.txt)

# range_angle_map 

FRTMData.range_angle_map(_pulse : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _range_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _cross_range_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _doa_method : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _field_of_view : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _range_bin_index : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Compute the range-angle map using direction of arrival estimation methods. 

Parameters: 
     

**pulse: int, optional**
    
Index of the pulse to extract. The default is `None` in which case the center pulse (middle index) is used. 

**window: str, optional**
    
Type of window. The default is `None`. Available options are `"Hann"`, `"Hamming"`, and `"Flat"`. 

**range_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of bins to use in the range (frequency) dimension. If `None`, number of channels is used. 

**cross_range_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of bins in the angular (azimuth) dimension. If `None`, `181` bins are used. 

**doa_method**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Direction of arrival estimation method. Options are `"Bartlett"`, `"Capon"`, and `"MUSIC"`. The default is `"Bartlett"`. 

**field_of_view**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Azimuth angular span in degrees to analyze. The default is `[-90, 90]`. 

**range_bin_index**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Specific range bin index to extract the angular profile. If provided, only that bin is used. 

Returns: 
     

[`np.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")
    
Data representing the range-angle intensity map.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMData
>>> file = "RxSignal.frtm"
>>> data = RangeDopplerData(file)
>>> range_angle_map = data.range_angle_map()

```
Copy to clipboard