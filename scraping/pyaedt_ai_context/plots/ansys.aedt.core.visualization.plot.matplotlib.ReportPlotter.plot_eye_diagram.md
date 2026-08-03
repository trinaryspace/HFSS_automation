---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.plot_eye_diagram.html"
category: "plots"
domain: "PyAEDT / HFSS"
---

# plot_eye_diagram 

ReportPlotter.plot_eye_diagram(_snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _is_contour =False_, _filter_colormap =1e-06_, _plot_max_height =True_, _plot_eye_mask =True_) 
    
Plot Eye diagram and contour plot. 

Parameters: 
     

**snapshot_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path to output image file. If not provided, the plot will not be saved. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the plot. Default is True. 

**is_contour**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot is a BET contour plot. 

**filter_colormap**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Whether to filter the contour data and start from a specific BER. 

**plot_max_height**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot the maximum height lines on the eye diagram. Doesn’t apply to contour plot. 

**plot_eye_mask**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot the eye mask on the eye diagram.
Examples

```
>>> from ansys.aedt.core.visualization.plot.matplotlib import ReportPlotter
>>> obj = ReportPlotter()
>>> obj.plot_eye_diagram()

```
Copy to clipboard
# plot_eye_diagram 

ReportPlotter.plot_eye_diagram(_snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _is_contour =False_, _filter_colormap =1e-06_, _plot_max_height =True_, _plot_eye_mask =True_) 
    
Plot Eye diagram and contour plot. 

Parameters: 
     

**snapshot_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path to output image file. If not provided, the plot will not be saved. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the plot. Default is True. 

**is_contour**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot is a BET contour plot. 

**filter_colormap**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Whether to filter the contour data and start from a specific BER. 

**plot_max_height**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot the maximum height lines on the eye diagram. Doesn’t apply to contour plot. 

**plot_eye_mask**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot the eye mask on the eye diagram.
Examples

```
>>> from ansys.aedt.core.visualization.plot.matplotlib import ReportPlotter
>>> obj = ReportPlotter()
>>> obj.plot_eye_diagram()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.plot_eye_diagram.rst.txt)

# plot_eye_diagram 

ReportPlotter.plot_eye_diagram(_snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _is_contour =False_, _filter_colormap =1e-06_, _plot_max_height =True_, _plot_eye_mask =True_) 
    
Plot Eye diagram and contour plot. 

Parameters: 
     

**snapshot_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path to output image file. If not provided, the plot will not be saved. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to display the plot. Default is True. 

**is_contour**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot is a BET contour plot. 

**filter_colormap**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Whether to filter the contour data and start from a specific BER. 

**plot_max_height**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot the maximum height lines on the eye diagram. Doesn’t apply to contour plot. 

**plot_eye_mask**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot the eye mask on the eye diagram.
Examples

```
>>> from ansys.aedt.core.visualization.plot.matplotlib import ReportPlotter
>>> obj = ReportPlotter()
>>> obj.plot_eye_diagram()

```
Copy to clipboard