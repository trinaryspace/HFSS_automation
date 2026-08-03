---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# FRTMPlotter 

class ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter(_frtm_data_) 
    
Provides range doppler data.
Read FRTM data and return the Python interface to analyze the range doppler data. All units are in SI. 

Parameters: 
     

**frtm_data**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") or [`FRTMData`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMData.html#ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMData "ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMData") 
    
Dictionary with multiple FRTMData objects or one single FRTMData.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.doppler_range_visualization import RangeDopplerData
>>> file = "RxSignal.frtm"
>>> data = RangeDopplerData(file)

```
Copy to clipboard
Methods  
| [`FRTMPlotter.plot_range_angle_map`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_angle_map.html#ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_angle_map "ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_angle_map")([frame, ...])  | Create range-angle map contour plot.  |  
| --- | --- |  
| [`FRTMPlotter.plot_range_doppler`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_doppler.html#ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_doppler "ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_doppler")([channel, ...])  | Create range-Doppler contour plot.  |  
| [`FRTMPlotter.plot_range_profile`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_profile.html#ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_profile "ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_profile")([channel, ...])  | Create a 2D plot of the range profile.  |  
Attributes  
| [`FRTMPlotter.all_data`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.all_data.html#ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.all_data "ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.all_data")  | RCS data object.  |  
| --- | --- |  
| [`FRTMPlotter.frames`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.frames.html#ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.frames "ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.frames")  | Frames.  |  
| [`FRTMPlotter.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.public_dir.html#ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.public_dir "ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.public_dir")  | Shortcut for dir(self).  |  
# FRTMPlotter 

class ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter(_frtm_data_) 
    
Provides range doppler data.
Read FRTM data and return the Python interface to analyze the range doppler data. All units are in SI. 

Parameters: 
     

**frtm_data**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") or [`FRTMData`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMData.html#ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMData "ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMData") 
    
Dictionary with multiple FRTMData objects or one single FRTMData.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.doppler_range_visualization import RangeDopplerData
>>> file = "RxSignal.frtm"
>>> data = RangeDopplerData(file)

```
Copy to clipboard
Methods  
| [`FRTMPlotter.plot_range_angle_map`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_angle_map.html#ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_angle_map "ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_angle_map")([frame, ...])  | Create range-angle map contour plot.  |  
| --- | --- |  
| [`FRTMPlotter.plot_range_doppler`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_doppler.html#ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_doppler "ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_doppler")([channel, ...])  | Create range-Doppler contour plot.  |  
| [`FRTMPlotter.plot_range_profile`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_profile.html#ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_profile "ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_profile")([channel, ...])  | Create a 2D plot of the range profile.  |  
Attributes  
| [`FRTMPlotter.all_data`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.all_data.html#ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.all_data "ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.all_data")  | RCS data object.  |  
| --- | --- |  
| [`FRTMPlotter.frames`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.frames.html#ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.frames "ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.frames")  | Frames.  |  
| [`FRTMPlotter.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.public_dir.html#ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.public_dir "ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.rst.txt)

# FRTMPlotter 

class ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter(_frtm_data_) 
    
Provides range doppler data.
Read FRTM data and return the Python interface to analyze the range doppler data. All units are in SI. 

Parameters: 
     

**frtm_data**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") or [`FRTMData`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMData.html#ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMData "ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMData") 
    
Dictionary with multiple FRTMData objects or one single FRTMData.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.doppler_range_visualization import RangeDopplerData
>>> file = "RxSignal.frtm"
>>> data = RangeDopplerData(file)

```
Copy to clipboard
Methods  
| [`FRTMPlotter.plot_range_angle_map`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_angle_map.html#ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_angle_map "ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_angle_map")([frame, ...])  | Create range-angle map contour plot.  |  
| --- | --- |  
| [`FRTMPlotter.plot_range_doppler`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_doppler.html#ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_doppler "ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_doppler")([channel, ...])  | Create range-Doppler contour plot.  |  
| [`FRTMPlotter.plot_range_profile`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_profile.html#ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_profile "ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_profile")([channel, ...])  | Create a 2D plot of the range profile.  |  
Attributes  
| [`FRTMPlotter.all_data`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.all_data.html#ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.all_data "ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.all_data")  | RCS data object.  |  
| --- | --- |  
| [`FRTMPlotter.frames`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.frames.html#ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.frames "ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.frames")  | Frames.  |  
| [`FRTMPlotter.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.public_dir.html#ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.public_dir "ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.public_dir")  | Shortcut for dir(self).  |