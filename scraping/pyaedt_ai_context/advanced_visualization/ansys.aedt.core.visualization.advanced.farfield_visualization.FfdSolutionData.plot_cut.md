---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData.plot_cut.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# plot_cut 

FfdSolutionData.plot_cut(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'RealizedGain'_, _primary_sweep : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'phi'_, _secondary_sweep_value : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _phi : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _title : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Far Field Cut'_, _quantity_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'dB10'_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _is_polar : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _show_legend : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [ReportPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter") 
    
Create a 2D plot of a specified quantity in Matplotlib. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Quantity to plot. The default is `"RealizedGain"`. Available quantities are: `"RealizedGain"`, `"RealizedGain_Theta"`, `"RealizedGain_Phi"`, `"rETotal"`, `"rETheta"`, and `"rEPhi"`. 

**primary_sweep**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), optional. 
    
X-axis variable. The default is `"phi"`. Options are `"phi"` and `"theta"`. 

**secondary_sweep_value**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
List of cuts on the secondary sweep to plot. The default is `0`. Options are “all”, a single value float, or a list of float values. 

**phi**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Phi scan angle in degrees. The default is `0`. 

**theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Theta scan angle in degrees. The default is `0`. 

**title**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot title. The default is `"RectangularPlot"`. 

**quantity_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Conversion data function. Available functions are: `"abs"`, `"ang"`, `"dB10"`, `"dB20"`, `"deg"`, `"imag"`, `"norm"`, and `"real"`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path for the image file. The default is `None`, in which case an image in not exported. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot. The default is `True`. If `False`, the Matplotlib instance of the plot is shown. 

**is_polar**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether this plot is a polar plot. The default is `True`. 

**show_legend**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the legend or not. The default is `True`. 

Returns: 
     

[`ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter")
    
Matplotlib figure object. If `show=True`, a Matplotlib figure instance of the plot is returned. If `show=False`, the plotted curve is returned.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss(version="2026.1", design="Antenna")
>>> setup_name = "Setup1 : LastAdaptive"
>>> frequencies = [77e9]
>>> sphere = "3D"
>>> data = app.get_antenna_data(frequencies, setup_name, sphere)
>>> data.plot_cut(theta=20)

```
Copy to clipboard
# plot_cut 

FfdSolutionData.plot_cut(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'RealizedGain'_, _primary_sweep : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'phi'_, _secondary_sweep_value : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _phi : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _title : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Far Field Cut'_, _quantity_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'dB10'_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _is_polar : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _show_legend : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [ReportPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter") 
    
Create a 2D plot of a specified quantity in Matplotlib. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Quantity to plot. The default is `"RealizedGain"`. Available quantities are: `"RealizedGain"`, `"RealizedGain_Theta"`, `"RealizedGain_Phi"`, `"rETotal"`, `"rETheta"`, and `"rEPhi"`. 

**primary_sweep**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), optional. 
    
X-axis variable. The default is `"phi"`. Options are `"phi"` and `"theta"`. 

**secondary_sweep_value**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
List of cuts on the secondary sweep to plot. The default is `0`. Options are “all”, a single value float, or a list of float values. 

**phi**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Phi scan angle in degrees. The default is `0`. 

**theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Theta scan angle in degrees. The default is `0`. 

**title**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot title. The default is `"RectangularPlot"`. 

**quantity_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Conversion data function. Available functions are: `"abs"`, `"ang"`, `"dB10"`, `"dB20"`, `"deg"`, `"imag"`, `"norm"`, and `"real"`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path for the image file. The default is `None`, in which case an image in not exported. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot. The default is `True`. If `False`, the Matplotlib instance of the plot is shown. 

**is_polar**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether this plot is a polar plot. The default is `True`. 

**show_legend**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the legend or not. The default is `True`. 

Returns: 
     

[`ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter")
    
Matplotlib figure object. If `show=True`, a Matplotlib figure instance of the plot is returned. If `show=False`, the plotted curve is returned.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss(version="2026.1", design="Antenna")
>>> setup_name = "Setup1 : LastAdaptive"
>>> frequencies = [77e9]
>>> sphere = "3D"
>>> data = app.get_antenna_data(frequencies, setup_name, sphere)
>>> data.plot_cut(theta=20)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData.plot_cut.rst.txt)

# plot_cut 

FfdSolutionData.plot_cut(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'RealizedGain'_, _primary_sweep : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'phi'_, _secondary_sweep_value : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _phi : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _title : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Far Field Cut'_, _quantity_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'dB10'_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _is_polar : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _show_legend : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [ReportPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter") 
    
Create a 2D plot of a specified quantity in Matplotlib. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Quantity to plot. The default is `"RealizedGain"`. Available quantities are: `"RealizedGain"`, `"RealizedGain_Theta"`, `"RealizedGain_Phi"`, `"rETotal"`, `"rETheta"`, and `"rEPhi"`. 

**primary_sweep**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), optional. 
    
X-axis variable. The default is `"phi"`. Options are `"phi"` and `"theta"`. 

**secondary_sweep_value**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
List of cuts on the secondary sweep to plot. The default is `0`. Options are “all”, a single value float, or a list of float values. 

**phi**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Phi scan angle in degrees. The default is `0`. 

**theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Theta scan angle in degrees. The default is `0`. 

**title**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot title. The default is `"RectangularPlot"`. 

**quantity_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Conversion data function. Available functions are: `"abs"`, `"ang"`, `"dB10"`, `"dB20"`, `"deg"`, `"imag"`, `"norm"`, and `"real"`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path for the image file. The default is `None`, in which case an image in not exported. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot. The default is `True`. If `False`, the Matplotlib instance of the plot is shown. 

**is_polar**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether this plot is a polar plot. The default is `True`. 

**show_legend**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the legend or not. The default is `True`. 

Returns: 
     

[`ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter")
    
Matplotlib figure object. If `show=True`, a Matplotlib figure instance of the plot is returned. If `show=False`, the plotted curve is returned.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss(version="2026.1", design="Antenna")
>>> setup_name = "Setup1 : LastAdaptive"
>>> frequencies = [77e9]
>>> sphere = "3D"
>>> data = app.get_antenna_data(frequencies, setup_name, sphere)
>>> data.plot_cut(theta=20)

```
Copy to clipboard