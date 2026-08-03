---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_icepak.PostProcessorIcepak.export_report_to_file.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# export_report_to_file 

PostProcessorIcepak.export_report_to_file(_output_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _extension : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _unique_file : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _uniform : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _start : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _end : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _step : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _use_trace_number_format : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export a 2D Plot data to a file.
This method leaves the data in the plot (as data) as a reference for the Plot after the loops. 

Parameters: 
     

**output_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the directory of exported report 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the plot to export. 

**extension**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
     

Extension of export , one of
    
  * (CSV) .csv
  * (Tab delimited) .tab
  * (Post processor format) .txt
  * (Ensight XY data) .exy
  * (Anosft Plot Data) .dat
  * (Ansoft Report Data Files) .rdat

**unique_file**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
If set to True, generates unique file in output_dit 

**uniform**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the export uniform points to the file. The default is `False`. 

**start**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Start range with units for the sweep if the `uniform` parameter is set to `True`. 

**end**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
End range with units for the sweep if the `uniform` parameter is set to `True`. 

**step**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Step range with units for the sweep if the `uniform` parameter is set to `True`. 

**use_trace_number_format**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use trace number formats and use separate columns for curve. The default is `False`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Path of exported file.
References

```
>>> oModule.ExportReportDataToFile
>>> oModule.ExportUniformPointsToFile
>>> oModule.ExportToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Circuit
>>> cir = Circuit("my_project.aedt")
>>> report = cir.post.create_report("MyScattering")
>>> cir.post.export_report_to_file("C:\temp", "MyTestScattering", ".csv")

```
Copy to clipboard
# export_report_to_file 

PostProcessorIcepak.export_report_to_file(_output_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _extension : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _unique_file : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _uniform : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _start : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _end : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _step : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _use_trace_number_format : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export a 2D Plot data to a file.
This method leaves the data in the plot (as data) as a reference for the Plot after the loops. 

Parameters: 
     

**output_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the directory of exported report 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the plot to export. 

**extension**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
     

Extension of export , one of
    
  * (CSV) .csv
  * (Tab delimited) .tab
  * (Post processor format) .txt
  * (Ensight XY data) .exy
  * (Anosft Plot Data) .dat
  * (Ansoft Report Data Files) .rdat

**unique_file**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
If set to True, generates unique file in output_dit 

**uniform**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the export uniform points to the file. The default is `False`. 

**start**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Start range with units for the sweep if the `uniform` parameter is set to `True`. 

**end**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
End range with units for the sweep if the `uniform` parameter is set to `True`. 

**step**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Step range with units for the sweep if the `uniform` parameter is set to `True`. 

**use_trace_number_format**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use trace number formats and use separate columns for curve. The default is `False`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Path of exported file.
References

```
>>> oModule.ExportReportDataToFile
>>> oModule.ExportUniformPointsToFile
>>> oModule.ExportToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Circuit
>>> cir = Circuit("my_project.aedt")
>>> report = cir.post.create_report("MyScattering")
>>> cir.post.export_report_to_file("C:\temp", "MyTestScattering", ".csv")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_icepak.PostProcessorIcepak.export_report_to_file.rst.txt)

# export_report_to_file 

PostProcessorIcepak.export_report_to_file(_output_dir : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _extension : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _unique_file : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _uniform : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _start : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _end : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _step : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _use_trace_number_format : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export a 2D Plot data to a file.
This method leaves the data in the plot (as data) as a reference for the Plot after the loops. 

Parameters: 
     

**output_dir**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the directory of exported report 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the plot to export. 

**extension**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
     

Extension of export , one of
    
  * (CSV) .csv
  * (Tab delimited) .tab
  * (Post processor format) .txt
  * (Ensight XY data) .exy
  * (Anosft Plot Data) .dat
  * (Ansoft Report Data Files) .rdat

**unique_file**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
If set to True, generates unique file in output_dit 

**uniform**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the export uniform points to the file. The default is `False`. 

**start**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Start range with units for the sweep if the `uniform` parameter is set to `True`. 

**end**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
End range with units for the sweep if the `uniform` parameter is set to `True`. 

**step**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Step range with units for the sweep if the `uniform` parameter is set to `True`. 

**use_trace_number_format**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use trace number formats and use separate columns for curve. The default is `False`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Path of exported file.
References

```
>>> oModule.ExportReportDataToFile
>>> oModule.ExportUniformPointsToFile
>>> oModule.ExportToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Circuit
>>> cir = Circuit("my_project.aedt")
>>> report = cir.post.create_report("MyScattering")
>>> cir.post.export_report_to_file("C:\temp", "MyTestScattering", ".csv")

```
Copy to clipboard