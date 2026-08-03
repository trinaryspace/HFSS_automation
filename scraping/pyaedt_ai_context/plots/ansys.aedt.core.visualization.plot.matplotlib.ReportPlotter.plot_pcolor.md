---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.plot_pcolor.html"
category: "plots"
domain: "PyAEDT / HFSS"
---

# plot_pcolor 

ReportPlotter.plot_pcolor(_trace : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _color_bar : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _figure : [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "\(in Matplotlib v3.11.0\)") = None_) → [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "\(in Matplotlib v3.11.0\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a Matplotlib figure pseudo color plot with a non-regular rectangular grid based on a list of data. 

Parameters: 
     

**trace**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Trace index on which create the 3D Plot. 

**color_bar**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Color bar title. The default is `None` in which case the color bar is not included. 

**snapshot_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to image file if a snapshot is needed. The default value is `None`. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot or return the matplotlib object. Default is `True`. 

**figure**`matplotlib.pyplot.Figure` , `optional` 
    
An existing Matplotlib Figure to which the plot is added. If not provided, a new Figure and Axes object are created. 

Returns: 
     

`matplotlib.pyplot.Figure`
    
Matplotlib figure object.
Examples

```
>>> from ansys.aedt.core.visualization.plot.matplotlib import ReportPlotter
>>> obj = ReportPlotter()
>>> obj.plot_pcolor()

```
Copy to clipboard
# plot_pcolor 

ReportPlotter.plot_pcolor(_trace : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _color_bar : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _figure : [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "\(in Matplotlib v3.11.0\)") = None_) → [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "\(in Matplotlib v3.11.0\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a Matplotlib figure pseudo color plot with a non-regular rectangular grid based on a list of data. 

Parameters: 
     

**trace**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Trace index on which create the 3D Plot. 

**color_bar**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Color bar title. The default is `None` in which case the color bar is not included. 

**snapshot_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to image file if a snapshot is needed. The default value is `None`. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot or return the matplotlib object. Default is `True`. 

**figure**`matplotlib.pyplot.Figure` , `optional` 
    
An existing Matplotlib Figure to which the plot is added. If not provided, a new Figure and Axes object are created. 

Returns: 
     

`matplotlib.pyplot.Figure`
    
Matplotlib figure object.
Examples

```
>>> from ansys.aedt.core.visualization.plot.matplotlib import ReportPlotter
>>> obj = ReportPlotter()
>>> obj.plot_pcolor()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.plot_pcolor.rst.txt)

# plot_pcolor 

ReportPlotter.plot_pcolor(_trace : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _color_bar : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _figure : [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "\(in Matplotlib v3.11.0\)") = None_) → [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "\(in Matplotlib v3.11.0\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a Matplotlib figure pseudo color plot with a non-regular rectangular grid based on a list of data. 

Parameters: 
     

**trace**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Trace index on which create the 3D Plot. 

**color_bar**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Color bar title. The default is `None` in which case the color bar is not included. 

**snapshot_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to image file if a snapshot is needed. The default value is `None`. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot or return the matplotlib object. Default is `True`. 

**figure**`matplotlib.pyplot.Figure` , `optional` 
    
An existing Matplotlib Figure to which the plot is added. If not provided, a new Figure and Axes object are created. 

Returns: 
     

`matplotlib.pyplot.Figure`
    
Matplotlib figure object.
Examples

```
>>> from ansys.aedt.core.visualization.plot.matplotlib import ReportPlotter
>>> obj = ReportPlotter()
>>> obj.plot_pcolor()

```
Copy to clipboard