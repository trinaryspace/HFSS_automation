---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.plot_3d.html"
category: "plots"
domain: "PyAEDT / HFSS"
---

# plot_3d 

ReportPlotter.plot_3d(_trace : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _color_map_limits : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _is_polar : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "\(in Matplotlib v3.11.0\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a Matplotlib 3D plot based on a list of data. 

Parameters: 
     

**trace**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") `optional` 
    
Trace index or name on which create the 3D Plot. 

**snapshot_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to image file if a snapshot is needed. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot or return the matplotlib object. Default is True. 

**color_map_limits**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Color map minimum and maximum values. 

**is_polar**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if the plot will be polar or not. Polar plot will hide axes and grids. Default is `True`. 

Returns: 
     

`matplotlib.pyplot.Figure`
    
Matplotlib figure object.
Examples

```
>>> from ansys.aedt.core.visualization.plot.matplotlib import ReportPlotter
>>> obj = ReportPlotter()
>>> obj.plot_3d()

```
Copy to clipboard
# plot_3d 

ReportPlotter.plot_3d(_trace : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _color_map_limits : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _is_polar : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "\(in Matplotlib v3.11.0\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a Matplotlib 3D plot based on a list of data. 

Parameters: 
     

**trace**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") `optional` 
    
Trace index or name on which create the 3D Plot. 

**snapshot_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to image file if a snapshot is needed. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot or return the matplotlib object. Default is True. 

**color_map_limits**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Color map minimum and maximum values. 

**is_polar**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if the plot will be polar or not. Polar plot will hide axes and grids. Default is `True`. 

Returns: 
     

`matplotlib.pyplot.Figure`
    
Matplotlib figure object.
Examples

```
>>> from ansys.aedt.core.visualization.plot.matplotlib import ReportPlotter
>>> obj = ReportPlotter()
>>> obj.plot_3d()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.plot_3d.rst.txt)

# plot_3d 

ReportPlotter.plot_3d(_trace : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _color_map_limits : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _is_polar : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "\(in Matplotlib v3.11.0\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a Matplotlib 3D plot based on a list of data. 

Parameters: 
     

**trace**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") `optional` 
    
Trace index or name on which create the 3D Plot. 

**snapshot_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to image file if a snapshot is needed. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot or return the matplotlib object. Default is True. 

**color_map_limits**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Color map minimum and maximum values. 

**is_polar**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if the plot will be polar or not. Polar plot will hide axes and grids. Default is `True`. 

Returns: 
     

`matplotlib.pyplot.Figure`
    
Matplotlib figure object.
Examples

```
>>> from ansys.aedt.core.visualization.plot.matplotlib import ReportPlotter
>>> obj = ReportPlotter()
>>> obj.plot_3d()

```
Copy to clipboard