---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_3dlayout.PostProcessor3DLayout.export_report_to_csv.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# export_report_to_csv 

PostProcessor3DLayout.export_report_to_csv(_project_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _uniform : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _start : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _end : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _step : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _use_trace_number_format : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export the 2D Plot data to a CSV file.
This method leaves the data in the plot (as data) as a reference for the Plot after the loops. 

Parameters: 
     

**project_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the project directory. The CSV file is plot_name.csv. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the plot to export. 

**uniform**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the export uniform points to the file. The default is `False`. 

**start**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Start range with units for the sweep if the `uniform` parameter is set to `True`. 

**end**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
End range with units for the sweep if the `uniform` parameter is set to `True`. 

**step**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Step range with units for the sweep if the `uniform` parameter is set to `True`. 

**use_trace_number_format**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use trace number formats. The default is `False`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Path of exported file.
References

```
>>> oModule.ExportReportDataToFile
>>> oModule.ExportToFile
>>> oModule.ExportUniformPointsToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.common import PostProcessorCommon
>>> obj = PostProcessorCommon()
>>> obj.export_report_to_csv("my_dir", "my_plot")

```
Copy to clipboard
# export_report_to_csv 

PostProcessor3DLayout.export_report_to_csv(_project_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _uniform : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _start : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _end : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _step : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _use_trace_number_format : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export the 2D Plot data to a CSV file.
This method leaves the data in the plot (as data) as a reference for the Plot after the loops. 

Parameters: 
     

**project_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the project directory. The CSV file is plot_name.csv. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the plot to export. 

**uniform**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the export uniform points to the file. The default is `False`. 

**start**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Start range with units for the sweep if the `uniform` parameter is set to `True`. 

**end**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
End range with units for the sweep if the `uniform` parameter is set to `True`. 

**step**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Step range with units for the sweep if the `uniform` parameter is set to `True`. 

**use_trace_number_format**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use trace number formats. The default is `False`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Path of exported file.
References

```
>>> oModule.ExportReportDataToFile
>>> oModule.ExportToFile
>>> oModule.ExportUniformPointsToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.common import PostProcessorCommon
>>> obj = PostProcessorCommon()
>>> obj.export_report_to_csv("my_dir", "my_plot")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_3dlayout.PostProcessor3DLayout.export_report_to_csv.rst.txt)

# export_report_to_csv 

PostProcessor3DLayout.export_report_to_csv(_project_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _uniform : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _start : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _end : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _step : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _use_trace_number_format : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export the 2D Plot data to a CSV file.
This method leaves the data in the plot (as data) as a reference for the Plot after the loops. 

Parameters: 
     

**project_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the project directory. The CSV file is plot_name.csv. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the plot to export. 

**uniform**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the export uniform points to the file. The default is `False`. 

**start**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Start range with units for the sweep if the `uniform` parameter is set to `True`. 

**end**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
End range with units for the sweep if the `uniform` parameter is set to `True`. 

**step**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Step range with units for the sweep if the `uniform` parameter is set to `True`. 

**use_trace_number_format**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use trace number formats. The default is `False`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Path of exported file.
References

```
>>> oModule.ExportReportDataToFile
>>> oModule.ExportToFile
>>> oModule.ExportUniformPointsToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.common import PostProcessorCommon
>>> obj = PostProcessorCommon()
>>> obj.export_report_to_csv("my_dir", "my_plot")

```
Copy to clipboard