---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.animate_contour.html"
category: "plots"
domain: "PyAEDT / HFSS"
---

# animate_contour 

ReportPlotter.animate_contour(_trace : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _polar : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _levels : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 64_, _max_theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 180_, _min_theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _color_bar : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _figure : [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "\(in Matplotlib v3.11.0\)") = None_, _is_spherical : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _normalize : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "\(in Matplotlib v3.11.0\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create an animated Matplotlib figure contour based on a list of data. 

Parameters: 
     

**trace**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Trace index on which create the 3D Plot. 

**polar**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Generate the plot in polar coordinates. The default is `True`. If `False`, the plot generated is rectangular. 

**levels**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Color map levels. The default is `64`. 

**max_theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum theta angle for plotting. It applies only for polar plots. The default is `180`, which plots the data for all angles. Setting `max_theta` to 90 limits the displayed data to the upper hemisphere, that is (0 < theta < 90). 

**min_theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Minimum theta angle for plotting. It applies only for polar plots. The default is `0`. 

**color_bar**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Color bar title. The default is `None` in which case the color bar is not included. 

**snapshot_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to image file if a snapshot is needed. The default value is `None`. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot or return the matplotlib object. Default is `True`. 

**figure**`matplotlib.pyplot.Figure` , `optional` 
    
An existing Matplotlib Figure to which the plot is added. If not provided, a new Figure and Axes object are created. 

**is_spherical**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use spherical or cartesian data. 

**normalize**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Normalize the color scale using the provided `[vmin, vmax]` values. If not provided or invalid, automatic normalization is applied. 

Returns: 
     

`matplotlib.pyplot.Figure`
    
Matplotlib figure object.
Examples

```
>>> from ansys.aedt.core.visualization.plot.matplotlib import ReportPlotter
>>> obj = ReportPlotter()
>>> obj.animate_contour()

```
Copy to clipboard
# animate_contour 

ReportPlotter.animate_contour(_trace : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _polar : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _levels : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 64_, _max_theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 180_, _min_theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _color_bar : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _figure : [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "\(in Matplotlib v3.11.0\)") = None_, _is_spherical : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _normalize : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "\(in Matplotlib v3.11.0\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create an animated Matplotlib figure contour based on a list of data. 

Parameters: 
     

**trace**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Trace index on which create the 3D Plot. 

**polar**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Generate the plot in polar coordinates. The default is `True`. If `False`, the plot generated is rectangular. 

**levels**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Color map levels. The default is `64`. 

**max_theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum theta angle for plotting. It applies only for polar plots. The default is `180`, which plots the data for all angles. Setting `max_theta` to 90 limits the displayed data to the upper hemisphere, that is (0 < theta < 90). 

**min_theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Minimum theta angle for plotting. It applies only for polar plots. The default is `0`. 

**color_bar**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Color bar title. The default is `None` in which case the color bar is not included. 

**snapshot_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to image file if a snapshot is needed. The default value is `None`. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot or return the matplotlib object. Default is `True`. 

**figure**`matplotlib.pyplot.Figure` , `optional` 
    
An existing Matplotlib Figure to which the plot is added. If not provided, a new Figure and Axes object are created. 

**is_spherical**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use spherical or cartesian data. 

**normalize**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Normalize the color scale using the provided `[vmin, vmax]` values. If not provided or invalid, automatic normalization is applied. 

Returns: 
     

`matplotlib.pyplot.Figure`
    
Matplotlib figure object.
Examples

```
>>> from ansys.aedt.core.visualization.plot.matplotlib import ReportPlotter
>>> obj = ReportPlotter()
>>> obj.animate_contour()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.animate_contour.rst.txt)

# animate_contour 

ReportPlotter.animate_contour(_trace : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _polar : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _levels : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 64_, _max_theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 180_, _min_theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _color_bar : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _figure : [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "\(in Matplotlib v3.11.0\)") = None_, _is_spherical : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _normalize : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "\(in Matplotlib v3.11.0\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create an animated Matplotlib figure contour based on a list of data. 

Parameters: 
     

**trace**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Trace index on which create the 3D Plot. 

**polar**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Generate the plot in polar coordinates. The default is `True`. If `False`, the plot generated is rectangular. 

**levels**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Color map levels. The default is `64`. 

**max_theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum theta angle for plotting. It applies only for polar plots. The default is `180`, which plots the data for all angles. Setting `max_theta` to 90 limits the displayed data to the upper hemisphere, that is (0 < theta < 90). 

**min_theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Minimum theta angle for plotting. It applies only for polar plots. The default is `0`. 

**color_bar**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Color bar title. The default is `None` in which case the color bar is not included. 

**snapshot_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to image file if a snapshot is needed. The default value is `None`. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot or return the matplotlib object. Default is `True`. 

**figure**`matplotlib.pyplot.Figure` , `optional` 
    
An existing Matplotlib Figure to which the plot is added. If not provided, a new Figure and Axes object are created. 

**is_spherical**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use spherical or cartesian data. 

**normalize**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Normalize the color scale using the provided `[vmin, vmax]` values. If not provided or invalid, automatic normalization is applied. 

Returns: 
     

`matplotlib.pyplot.Figure`
    
Matplotlib figure object.
Examples

```
>>> from ansys.aedt.core.visualization.plot.matplotlib import ReportPlotter
>>> obj = ReportPlotter()
>>> obj.animate_contour()

```
Copy to clipboard