---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData.plot_contour.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# plot_contour 

FfdSolutionData.plot_contour(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'RealizedGain'_, _phi : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _title : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _quantity_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'dB10'_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _levels : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 64_, _polar : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _max_theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 180_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [ReportPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter") 
    
Create a contour plot of a specified quantity in Matplotlib. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Far field quantity to plot. The default is `"RealizedGain"`. Available quantities are: `"RealizedGain"`, `"RealizedGain_Phi"`, `"RealizedGain_Theta"`, `"rEPhi"`, `"rETheta"`, and `"rETotal"`. 

**phi**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Phi scan angle in degrees. The default is `0`. 

**theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Theta scan angle in degrees. The default is `0`. 

**title**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot title. The default is `"RectangularPlot"`. 

**quantity_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Conversion data function. Available functions are: `"abs"`, `"ang"`, `"dB10"`, `"dB20"`, `"deg"`, `"imag"`, `"norm"`, and `"real"`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path for the image file. The default is `None`, in which case the file is not exported. 

**levels**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Color map levels. The default is `64`. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot. The default is `True`. If `False`, the Matplotlib instance of the plot is shown. 

**polar**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Generate the plot in polar coordinates. The default is `True`. If `False`, the plot generated is rectangular. 

**max_theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum theta angle for plotting far-field data. The default value is `180`, which plots all angles. Setting `max_theta` to 90 limits the displayed data to the upper hemisphere, that is (0 < theta < 90). 

Returns: 
     

[`ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter")
    
Matplotlib figure object.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss(version="2026.1", design="Antenna")
>>> setup_name = "Setup1 : LastAdaptive"
>>> frequencies = [77e9]
>>> sphere = "3D"
>>> data = app.get_antenna_data(frequencies, setup_name, sphere)
>>> data.plot_contour()

```
Copy to clipboard
# plot_contour 

FfdSolutionData.plot_contour(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'RealizedGain'_, _phi : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _title : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _quantity_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'dB10'_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _levels : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 64_, _polar : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _max_theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 180_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [ReportPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter") 
    
Create a contour plot of a specified quantity in Matplotlib. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Far field quantity to plot. The default is `"RealizedGain"`. Available quantities are: `"RealizedGain"`, `"RealizedGain_Phi"`, `"RealizedGain_Theta"`, `"rEPhi"`, `"rETheta"`, and `"rETotal"`. 

**phi**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Phi scan angle in degrees. The default is `0`. 

**theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Theta scan angle in degrees. The default is `0`. 

**title**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot title. The default is `"RectangularPlot"`. 

**quantity_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Conversion data function. Available functions are: `"abs"`, `"ang"`, `"dB10"`, `"dB20"`, `"deg"`, `"imag"`, `"norm"`, and `"real"`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path for the image file. The default is `None`, in which case the file is not exported. 

**levels**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Color map levels. The default is `64`. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot. The default is `True`. If `False`, the Matplotlib instance of the plot is shown. 

**polar**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Generate the plot in polar coordinates. The default is `True`. If `False`, the plot generated is rectangular. 

**max_theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum theta angle for plotting far-field data. The default value is `180`, which plots all angles. Setting `max_theta` to 90 limits the displayed data to the upper hemisphere, that is (0 < theta < 90). 

Returns: 
     

[`ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter")
    
Matplotlib figure object.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss(version="2026.1", design="Antenna")
>>> setup_name = "Setup1 : LastAdaptive"
>>> frequencies = [77e9]
>>> sphere = "3D"
>>> data = app.get_antenna_data(frequencies, setup_name, sphere)
>>> data.plot_contour()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData.plot_contour.rst.txt)

# plot_contour 

FfdSolutionData.plot_contour(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'RealizedGain'_, _phi : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _title : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _quantity_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'dB10'_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _levels : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 64_, _polar : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _max_theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 180_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [ReportPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter") 
    
Create a contour plot of a specified quantity in Matplotlib. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Far field quantity to plot. The default is `"RealizedGain"`. Available quantities are: `"RealizedGain"`, `"RealizedGain_Phi"`, `"RealizedGain_Theta"`, `"rEPhi"`, `"rETheta"`, and `"rETotal"`. 

**phi**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Phi scan angle in degrees. The default is `0`. 

**theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Theta scan angle in degrees. The default is `0`. 

**title**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot title. The default is `"RectangularPlot"`. 

**quantity_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Conversion data function. Available functions are: `"abs"`, `"ang"`, `"dB10"`, `"dB20"`, `"deg"`, `"imag"`, `"norm"`, and `"real"`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path for the image file. The default is `None`, in which case the file is not exported. 

**levels**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Color map levels. The default is `64`. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot. The default is `True`. If `False`, the Matplotlib instance of the plot is shown. 

**polar**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Generate the plot in polar coordinates. The default is `True`. If `False`, the plot generated is rectangular. 

**max_theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum theta angle for plotting far-field data. The default value is `180`, which plots all angles. Setting `max_theta` to 90 limits the displayed data to the upper hemisphere, that is (0 < theta < 90). 

Returns: 
     

[`ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter")
    
Matplotlib figure object.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss(version="2026.1", design="Antenna")
>>> setup_name = "Setup1 : LastAdaptive"
>>> frequencies = [77e9]
>>> sphere = "3D"
>>> data = app.get_antenna_data(frequencies, setup_name, sphere)
>>> data.plot_contour()

```
Copy to clipboard