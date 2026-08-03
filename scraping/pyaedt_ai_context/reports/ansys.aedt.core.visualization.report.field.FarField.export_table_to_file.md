---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.FarField.export_table_to_file.html"
category: "reports"
domain: "PyAEDT / HFSS"
---

# export_table_to_file 

FarField.export_table_to_file(_plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _table_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Marker'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export a marker table or a legend (with trace characteristics result) from a report to a file. 

Parameters: 
     

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Plot name. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path of the outputted file. Valid extensions for the output file are: `.tab`, `.csv` 

**table_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Valid table types are: `Marker`, `DeltaMarker`, `Legend`. Default table_type is `Marker`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.ExportTableToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.export_table_to_file("MyPlot", "output.csv", table_type="Marker")

```
Copy to clipboard
# export_table_to_file 

FarField.export_table_to_file(_plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _table_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Marker'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export a marker table or a legend (with trace characteristics result) from a report to a file. 

Parameters: 
     

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Plot name. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path of the outputted file. Valid extensions for the output file are: `.tab`, `.csv` 

**table_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Valid table types are: `Marker`, `DeltaMarker`, `Legend`. Default table_type is `Marker`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.ExportTableToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.export_table_to_file("MyPlot", "output.csv", table_type="Marker")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.FarField.export_table_to_file.rst.txt)

# export_table_to_file 

FarField.export_table_to_file(_plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _table_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Marker'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export a marker table or a legend (with trace characteristics result) from a report to a file. 

Parameters: 
     

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Plot name. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path of the outputted file. Valid extensions for the output file are: `.tab`, `.csv` 

**table_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Valid table types are: `Marker`, `DeltaMarker`, `Legend`. Default table_type is `Marker`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.ExportTableToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.export_table_to_file("MyPlot", "output.csv", table_type="Marker")

```
Copy to clipboard