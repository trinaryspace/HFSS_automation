---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_angle_map.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# plot_range_angle_map 

FRTMPlotter.plot_range_angle_map(_frame : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _pulse : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _range_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _cross_range_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _doa_method : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _field_of_view : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _dynamic_range : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _quantity_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _polar : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _title : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Angle vs Range (Azimuth)'_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_legend : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _size : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (1920, 1440)_, _figure : Figure = None_) → [ReportPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter") 
    
Create range-angle map contour plot. 

Parameters: 
     

**frame**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Frame number. The default is `None`, in which case all frames are used. 

**pulse: int, optional**
    
Index of the pulse to extract. The default is `None` in which case the center pulse (middle index) is used. 

**window: str, optional**
    
Type of window. The default is `None`. Available options are `"Hann"`, `"Hamming"`, and `"Flat"`. 

**range_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of bins to use in the range (frequency) dimension. If `None`, number of channels is used. 

**cross_range_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of bins in the angular (azimuth) dimension. If `None`, `181` bins are used. 

**doa_method**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Method used for direction of arrival estimation. Available options are: `"Bartlett"`, `"Capon"`, and `"Music"`. The default is `None`, in which case `"Bartlett"` is selected. 

**field_of_view**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Azimuth angular span in degrees to plot. The default is `[-90, 90]`. 

**dynamic_range**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
     

Dynamic range in dB.
    
If provided, the color map is clipped between the max power and max - dynamic_range. 

**quantity_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Conversion data function. The default is `None`. Available functions are: `"abs"`, `"ang"`, `"dB10"`, `"dB20"`, `"deg"`, `"imag"`, `"norm"`, and `"real"`. 

**polar**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Generate the plot in polar coordinates. The default is `True`. If `False`, the plot generated is rectangular. 

**title**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Title of the plot. The default is `"Range profile"`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)"), `optional` 
    
Full path for the image file. The default is `None`, in which case an image in not exported. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot. The default is `True`. If `False`, the Matplotlib instance of the plot is shown. 

**show_legend**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the legend or not. The default is `True`. 

**size**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), `optional` 
    
Image size in pixel (width, height). 

**figure**`matplotlib.pyplot.Figure` , `optional` 
    
An existing Matplotlib Figure to which the plot is added. If not provided, a new Figure and Axes objects are created. Default is `None`. 

Returns: 
     

[`ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter")
    
PyAEDT matplotlib figure object.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import get_results_files
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMData
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMPlotter
>>> output_directory = "directory.results"
>>> frames_dict = get_results_files(directory)
>>> for frame, data_frame in frames_dict.items():
>>>     doppler_data = FRTMData(data_frame)
>>>     data[frame] = doppler_data
>>> frtm_plotter = FRTMPlotter(data)
>>> frame_number = frtm_plotter.frames[0]
>>> frtm_plotter.plot_range_angle_map(frame=frame_number)
>>> frtm_plotter.plot_range_angle_map(output_file="range_angle_map.gif", animation=True, show=False)

```
Copy to clipboard
# plot_range_angle_map 

FRTMPlotter.plot_range_angle_map(_frame : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _pulse : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _range_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _cross_range_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _doa_method : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _field_of_view : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _dynamic_range : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _quantity_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _polar : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _title : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Angle vs Range (Azimuth)'_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_legend : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _size : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (1920, 1440)_, _figure : Figure = None_) → [ReportPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter") 
    
Create range-angle map contour plot. 

Parameters: 
     

**frame**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Frame number. The default is `None`, in which case all frames are used. 

**pulse: int, optional**
    
Index of the pulse to extract. The default is `None` in which case the center pulse (middle index) is used. 

**window: str, optional**
    
Type of window. The default is `None`. Available options are `"Hann"`, `"Hamming"`, and `"Flat"`. 

**range_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of bins to use in the range (frequency) dimension. If `None`, number of channels is used. 

**cross_range_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of bins in the angular (azimuth) dimension. If `None`, `181` bins are used. 

**doa_method**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Method used for direction of arrival estimation. Available options are: `"Bartlett"`, `"Capon"`, and `"Music"`. The default is `None`, in which case `"Bartlett"` is selected. 

**field_of_view**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Azimuth angular span in degrees to plot. The default is `[-90, 90]`. 

**dynamic_range**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
     

Dynamic range in dB.
    
If provided, the color map is clipped between the max power and max - dynamic_range. 

**quantity_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Conversion data function. The default is `None`. Available functions are: `"abs"`, `"ang"`, `"dB10"`, `"dB20"`, `"deg"`, `"imag"`, `"norm"`, and `"real"`. 

**polar**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Generate the plot in polar coordinates. The default is `True`. If `False`, the plot generated is rectangular. 

**title**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Title of the plot. The default is `"Range profile"`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)"), `optional` 
    
Full path for the image file. The default is `None`, in which case an image in not exported. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot. The default is `True`. If `False`, the Matplotlib instance of the plot is shown. 

**show_legend**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the legend or not. The default is `True`. 

**size**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), `optional` 
    
Image size in pixel (width, height). 

**figure**`matplotlib.pyplot.Figure` , `optional` 
    
An existing Matplotlib Figure to which the plot is added. If not provided, a new Figure and Axes objects are created. Default is `None`. 

Returns: 
     

[`ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter")
    
PyAEDT matplotlib figure object.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import get_results_files
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMData
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMPlotter
>>> output_directory = "directory.results"
>>> frames_dict = get_results_files(directory)
>>> for frame, data_frame in frames_dict.items():
>>>     doppler_data = FRTMData(data_frame)
>>>     data[frame] = doppler_data
>>> frtm_plotter = FRTMPlotter(data)
>>> frame_number = frtm_plotter.frames[0]
>>> frtm_plotter.plot_range_angle_map(frame=frame_number)
>>> frtm_plotter.plot_range_angle_map(output_file="range_angle_map.gif", animation=True, show=False)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_angle_map.rst.txt)

# plot_range_angle_map 

FRTMPlotter.plot_range_angle_map(_frame : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _pulse : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _range_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _cross_range_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _doa_method : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _field_of_view : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _dynamic_range : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _quantity_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _polar : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _title : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Angle vs Range (Azimuth)'_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_legend : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _size : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (1920, 1440)_, _figure : Figure = None_) → [ReportPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter") 
    
Create range-angle map contour plot. 

Parameters: 
     

**frame**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Frame number. The default is `None`, in which case all frames are used. 

**pulse: int, optional**
    
Index of the pulse to extract. The default is `None` in which case the center pulse (middle index) is used. 

**window: str, optional**
    
Type of window. The default is `None`. Available options are `"Hann"`, `"Hamming"`, and `"Flat"`. 

**range_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of bins to use in the range (frequency) dimension. If `None`, number of channels is used. 

**cross_range_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of bins in the angular (azimuth) dimension. If `None`, `181` bins are used. 

**doa_method**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Method used for direction of arrival estimation. Available options are: `"Bartlett"`, `"Capon"`, and `"Music"`. The default is `None`, in which case `"Bartlett"` is selected. 

**field_of_view**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Azimuth angular span in degrees to plot. The default is `[-90, 90]`. 

**dynamic_range**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
     

Dynamic range in dB.
    
If provided, the color map is clipped between the max power and max - dynamic_range. 

**quantity_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Conversion data function. The default is `None`. Available functions are: `"abs"`, `"ang"`, `"dB10"`, `"dB20"`, `"deg"`, `"imag"`, `"norm"`, and `"real"`. 

**polar**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Generate the plot in polar coordinates. The default is `True`. If `False`, the plot generated is rectangular. 

**title**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Title of the plot. The default is `"Range profile"`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)"), `optional` 
    
Full path for the image file. The default is `None`, in which case an image in not exported. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot. The default is `True`. If `False`, the Matplotlib instance of the plot is shown. 

**show_legend**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the legend or not. The default is `True`. 

**size**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), `optional` 
    
Image size in pixel (width, height). 

**figure**`matplotlib.pyplot.Figure` , `optional` 
    
An existing Matplotlib Figure to which the plot is added. If not provided, a new Figure and Axes objects are created. Default is `None`. 

Returns: 
     

[`ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter")
    
PyAEDT matplotlib figure object.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import get_results_files
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMData
>>> from ansys.aedt.core.visualization.advanced.frtm_visualization import FRTMPlotter
>>> output_directory = "directory.results"
>>> frames_dict = get_results_files(directory)
>>> for frame, data_frame in frames_dict.items():
>>>     doppler_data = FRTMData(data_frame)
>>>     data[frame] = doppler_data
>>> frtm_plotter = FRTMPlotter(data)
>>> frame_number = frtm_plotter.frames[0]
>>> frtm_plotter.plot_range_angle_map(frame=frame_number)
>>> frtm_plotter.plot_range_angle_map(output_file="range_angle_map.gif", animation=True, show=False)

```
Copy to clipboard