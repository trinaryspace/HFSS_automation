---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData.plot_3d_chart.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# plot_3d_chart 

FfdSolutionData.plot_3d_chart(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'RealizedGain'_, _phi : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _title : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '3D Plot'_, _quantity_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'dB10'_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [ReportPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter") 
    
Create a 3D chart of a specified quantity in Matplotlib. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Far field quantity to plot. The default is `"RealizedGain"`. Available quantities are: `"RealizedGain"`, `"RealizedGain_Phi"`, `"RealizedGain_Theta"`, `"rEPhi"`, `"rETheta"`, and `"rETotal"`. 

**phi**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Phi scan angle in degree. The default is `0`. 

**theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Theta scan angle in degree. The default is `0`. 

**title**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot title. The default is `"3D Plot"`. 

**quantity_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Conversion data function. Available functions are: `"abs"`, `"ang"`, `"dB10"`, `"dB20"`, `"deg"`, `"imag"`, `"norm"`, and `"real"`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path for the image file. The default is `None`, in which case a file is not exported. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot. The default is `True`. If `False`, the Matplotlib instance of the plot is not shown. 

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
>>> data.polar_plot_3d(theta=10)

```
Copy to clipboard
# plot_3d_chart 

FfdSolutionData.plot_3d_chart(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'RealizedGain'_, _phi : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _title : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '3D Plot'_, _quantity_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'dB10'_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [ReportPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter") 
    
Create a 3D chart of a specified quantity in Matplotlib. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Far field quantity to plot. The default is `"RealizedGain"`. Available quantities are: `"RealizedGain"`, `"RealizedGain_Phi"`, `"RealizedGain_Theta"`, `"rEPhi"`, `"rETheta"`, and `"rETotal"`. 

**phi**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Phi scan angle in degree. The default is `0`. 

**theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Theta scan angle in degree. The default is `0`. 

**title**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot title. The default is `"3D Plot"`. 

**quantity_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Conversion data function. Available functions are: `"abs"`, `"ang"`, `"dB10"`, `"dB20"`, `"deg"`, `"imag"`, `"norm"`, and `"real"`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path for the image file. The default is `None`, in which case a file is not exported. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot. The default is `True`. If `False`, the Matplotlib instance of the plot is not shown. 

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
>>> data.polar_plot_3d(theta=10)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData.plot_3d_chart.rst.txt)

# plot_3d_chart 

FfdSolutionData.plot_3d_chart(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'RealizedGain'_, _phi : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _title : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '3D Plot'_, _quantity_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'dB10'_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [ReportPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter") 
    
Create a 3D chart of a specified quantity in Matplotlib. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Far field quantity to plot. The default is `"RealizedGain"`. Available quantities are: `"RealizedGain"`, `"RealizedGain_Phi"`, `"RealizedGain_Theta"`, `"rEPhi"`, `"rETheta"`, and `"rETotal"`. 

**phi**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Phi scan angle in degree. The default is `0`. 

**theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Theta scan angle in degree. The default is `0`. 

**title**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot title. The default is `"3D Plot"`. 

**quantity_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Conversion data function. Available functions are: `"abs"`, `"ang"`, `"dB10"`, `"dB20"`, `"deg"`, `"imag"`, `"norm"`, and `"real"`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path for the image file. The default is `None`, in which case a file is not exported. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot. The default is `True`. If `False`, the Matplotlib instance of the plot is not shown. 

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
>>> data.polar_plot_3d(theta=10)

```
Copy to clipboard