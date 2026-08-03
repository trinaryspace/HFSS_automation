---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.plot_polar.html"
category: "plots"
domain: "PyAEDT / HFSS"
---

# plot_polar 

ReportPlotter.plot_polar(_traces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _to_polar : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _is_degree : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _figure : [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "\(in Matplotlib v3.11.0\)") = None_) → [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "\(in Matplotlib v3.11.0\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a Matplotlib polar plot based on a list of data. 

Parameters: 
     

**traces**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Trace or traces to be plotted. It can be the trace name, the trace id or a list of those. 

**to_polar**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if cartesian data has to be converted to polar before the plot or can be used as is. 

**snapshot_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the image file if a snapshot is needed. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to render the figure. The default is `True`. If `False`, the figure is not drawn. 

**is_degree**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if data source are in degree or not. Default is `True`. 

**figure**`matplotlib.pyplot.Figure` , `optional` 
    
An existing Matplotlib Figure to which the plot is added. If not provided, a new Figure and Axes object are created. 

Returns: 
     

`matplotlib.pyplot.Figure`
    
Matplotlib figure object.
Examples

```
>>> from ansys.aedt.core.visualization.plot.matplotlib import ReportPlotter
>>> obj = ReportPlotter()
>>> obj.plot_polar()

```
Copy to clipboard
# plot_polar 

ReportPlotter.plot_polar(_traces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _to_polar : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _is_degree : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _figure : [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "\(in Matplotlib v3.11.0\)") = None_) → [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "\(in Matplotlib v3.11.0\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a Matplotlib polar plot based on a list of data. 

Parameters: 
     

**traces**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Trace or traces to be plotted. It can be the trace name, the trace id or a list of those. 

**to_polar**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if cartesian data has to be converted to polar before the plot or can be used as is. 

**snapshot_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the image file if a snapshot is needed. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to render the figure. The default is `True`. If `False`, the figure is not drawn. 

**is_degree**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if data source are in degree or not. Default is `True`. 

**figure**`matplotlib.pyplot.Figure` , `optional` 
    
An existing Matplotlib Figure to which the plot is added. If not provided, a new Figure and Axes object are created. 

Returns: 
     

`matplotlib.pyplot.Figure`
    
Matplotlib figure object.
Examples

```
>>> from ansys.aedt.core.visualization.plot.matplotlib import ReportPlotter
>>> obj = ReportPlotter()
>>> obj.plot_polar()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.plot_polar.rst.txt)

# plot_polar 

ReportPlotter.plot_polar(_traces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _to_polar : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _is_degree : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _figure : [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "\(in Matplotlib v3.11.0\)") = None_) → [Figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure "\(in Matplotlib v3.11.0\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a Matplotlib polar plot based on a list of data. 

Parameters: 
     

**traces**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Trace or traces to be plotted. It can be the trace name, the trace id or a list of those. 

**to_polar**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if cartesian data has to be converted to polar before the plot or can be used as is. 

**snapshot_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the image file if a snapshot is needed. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to render the figure. The default is `True`. If `False`, the figure is not drawn. 

**is_degree**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if data source are in degree or not. Default is `True`. 

**figure**`matplotlib.pyplot.Figure` , `optional` 
    
An existing Matplotlib Figure to which the plot is added. If not provided, a new Figure and Axes object are created. 

Returns: 
     

`matplotlib.pyplot.Figure`
    
Matplotlib figure object.
Examples

```
>>> from ansys.aedt.core.visualization.plot.matplotlib import ReportPlotter
>>> obj = ReportPlotter()
>>> obj.plot_polar()

```
Copy to clipboard