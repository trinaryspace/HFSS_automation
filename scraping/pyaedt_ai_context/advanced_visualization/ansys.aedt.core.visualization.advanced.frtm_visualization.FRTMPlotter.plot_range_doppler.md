---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_doppler.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# plot_range_doppler 

FRTMPlotter.plot_range_doppler(_channel : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _frame : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _range_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _doppler_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _quantity_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _title : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Doppler Velocity-Range'_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_legend : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _size : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (1920, 1440)_, _figure : Figure = None_) → [ReportPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter") 
    
Create range-Doppler contour plot. 

Parameters: 
     

**channel**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Channel name. The default is `None`, in which case the first channel is used. 

**frame**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Frame number. The default is `None`, in which case all frames are used. 

**range_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of output bins in range (frequency) dimension. If not specified, uses the original number of frequencies. 

**doppler_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
     

Number of output bins in Doppler (pulse/time) dimension.
    
If not specified, uses the original number of CPI frames. 

**window: str, optional**
    
Type of window. The default is `None`. Available options are `"Hann"`, `"Hamming"`, and `"Flat"`. 

**quantity_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Conversion data function. The default is `None`. Available functions are: `"abs"`, `"ang"`, `"dB10"`, `"dB20"`, `"deg"`, `"imag"`, `"norm"`, and `"real"`. 

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
>>> frtm_plotter.plot_range_doppler(frame=frame_number)
>>> frtm_plotter.plot_range_doppler(output_file="range_doppler.gif", animation=True, show=False)

```
Copy to clipboard
# plot_range_doppler 

FRTMPlotter.plot_range_doppler(_channel : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _frame : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _range_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _doppler_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _quantity_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _title : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Doppler Velocity-Range'_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_legend : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _size : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (1920, 1440)_, _figure : Figure = None_) → [ReportPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter") 
    
Create range-Doppler contour plot. 

Parameters: 
     

**channel**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Channel name. The default is `None`, in which case the first channel is used. 

**frame**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Frame number. The default is `None`, in which case all frames are used. 

**range_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of output bins in range (frequency) dimension. If not specified, uses the original number of frequencies. 

**doppler_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
     

Number of output bins in Doppler (pulse/time) dimension.
    
If not specified, uses the original number of CPI frames. 

**window: str, optional**
    
Type of window. The default is `None`. Available options are `"Hann"`, `"Hamming"`, and `"Flat"`. 

**quantity_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Conversion data function. The default is `None`. Available functions are: `"abs"`, `"ang"`, `"dB10"`, `"dB20"`, `"deg"`, `"imag"`, `"norm"`, and `"real"`. 

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
>>> frtm_plotter.plot_range_doppler(frame=frame_number)
>>> frtm_plotter.plot_range_doppler(output_file="range_doppler.gif", animation=True, show=False)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.frtm_visualization.FRTMPlotter.plot_range_doppler.rst.txt)

# plot_range_doppler 

FRTMPlotter.plot_range_doppler(_channel : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _frame : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _range_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _doppler_bins : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _quantity_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _title : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Doppler Velocity-Range'_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_legend : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _size : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (1920, 1440)_, _figure : Figure = None_) → [ReportPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter") 
    
Create range-Doppler contour plot. 

Parameters: 
     

**channel**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Channel name. The default is `None`, in which case the first channel is used. 

**frame**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Frame number. The default is `None`, in which case all frames are used. 

**range_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of output bins in range (frequency) dimension. If not specified, uses the original number of frequencies. 

**doppler_bins**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
     

Number of output bins in Doppler (pulse/time) dimension.
    
If not specified, uses the original number of CPI frames. 

**window: str, optional**
    
Type of window. The default is `None`. Available options are `"Hann"`, `"Hamming"`, and `"Flat"`. 

**quantity_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Conversion data function. The default is `None`. Available functions are: `"abs"`, `"ang"`, `"dB10"`, `"dB20"`, `"deg"`, `"imag"`, `"norm"`, and `"real"`. 

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
>>> frtm_plotter.plot_range_doppler(frame=frame_number)
>>> frtm_plotter.plot_range_doppler(output_file="range_doppler.gif", animation=True, show=False)

```
Copy to clipboard