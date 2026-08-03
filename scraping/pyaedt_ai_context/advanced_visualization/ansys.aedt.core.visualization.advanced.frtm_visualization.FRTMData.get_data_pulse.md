---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMData.get_data_pulse.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# get_data_pulse 

FRTMData.get_data_pulse(_pulse : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Get the data for a specified pulse. 

Parameters: 
     

**pulse: int, optional**
    
Number of points to window. The default is `None`. 

Returns: 
     

[`numpy.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")
    
Data for specified pulse.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMData
>>> file = "RxSignal.frtm"
>>> data = RangeDopplerData(file)
>>> pulse_number = data.cpi_frames
>>> data_pulse = data.get_data_pulse(0)

```
Copy to clipboard
# get_data_pulse 

FRTMData.get_data_pulse(_pulse : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Get the data for a specified pulse. 

Parameters: 
     

**pulse: int, optional**
    
Number of points to window. The default is `None`. 

Returns: 
     

[`numpy.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")
    
Data for specified pulse.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMData
>>> file = "RxSignal.frtm"
>>> data = RangeDopplerData(file)
>>> pulse_number = data.cpi_frames
>>> data_pulse = data.get_data_pulse(0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMData.get_data_pulse.rst.txt)

# get_data_pulse 

FRTMData.get_data_pulse(_pulse : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_) → [ndarray](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)") 
    
Get the data for a specified pulse. 

Parameters: 
     

**pulse: int, optional**
    
Number of points to window. The default is `None`. 

Returns: 
     

[`numpy.ndarray`](https://numpy.org/devdocs/reference/generated/numpy.ndarray.html#numpy.ndarray "\(in NumPy v2.6.dev0\)")
    
Data for specified pulse.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMData
>>> file = "RxSignal.frtm"
>>> data = RangeDopplerData(file)
>>> pulse_number = data.cpi_frames
>>> data_pulse = data.get_data_pulse(0)

```
Copy to clipboard