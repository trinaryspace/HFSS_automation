---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.add_trace.html"
category: "plots"
domain: "PyAEDT / HFSS"
---

# add_trace 

ReportPlotter.add_trace(_plot_data : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _data_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _properties : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a new trace to the chart. 

Parameters: 
     

**plot_data**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Data to be inserted. 

**data_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Data format. `0` for cartesian, `1` for spherical data. 

**properties**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Properties of the trace. {x_label:prop, y_label:prop, z_label:prop, trace_style : “-“, trace_width : 1.5, trace_color : None, show_symbol : False, symbol_style : ‘v’, fill_symbol : None, symbol_color : “C0” } 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Trace name. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.visualization.plot.matplotlib import ReportPlotter
>>> obj = ReportPlotter()
>>> obj.add_trace([[0, 1], [0, 1]], data_type=0)

```
Copy to clipboard
# add_trace 

ReportPlotter.add_trace(_plot_data : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _data_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _properties : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a new trace to the chart. 

Parameters: 
     

**plot_data**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Data to be inserted. 

**data_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Data format. `0` for cartesian, `1` for spherical data. 

**properties**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Properties of the trace. {x_label:prop, y_label:prop, z_label:prop, trace_style : “-“, trace_width : 1.5, trace_color : None, show_symbol : False, symbol_style : ‘v’, fill_symbol : None, symbol_color : “C0” } 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Trace name. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.visualization.plot.matplotlib import ReportPlotter
>>> obj = ReportPlotter()
>>> obj.add_trace([[0, 1], [0, 1]], data_type=0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.add_trace.rst.txt)

# add_trace 

ReportPlotter.add_trace(_plot_data : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _data_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _properties : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a new trace to the chart. 

Parameters: 
     

**plot_data**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Data to be inserted. 

**data_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Data format. `0` for cartesian, `1` for spherical data. 

**properties**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Properties of the trace. {x_label:prop, y_label:prop, z_label:prop, trace_style : “-“, trace_width : 1.5, trace_color : None, show_symbol : False, symbol_style : ‘v’, fill_symbol : None, symbol_color : “C0” } 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Trace name. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.visualization.plot.matplotlib import ReportPlotter
>>> obj = ReportPlotter()
>>> obj.add_trace([[0, 1], [0, 1]], data_type=0)

```
Copy to clipboard