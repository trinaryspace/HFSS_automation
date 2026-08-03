---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.FarField.apply_report_template.html"
category: "reports"
domain: "PyAEDT / HFSS"
---

# apply_report_template 

FarField.apply_report_template(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Graphical'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Apply report template.
Note
This method works in only in graphical mode. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path for the file to import. The extension supported is `".rpt"`. 

**property_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Property types to apply. Options are `"Graphical"`, `"Data"`, and `"All"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.ApplyReportTemplate

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.apply_report_template("template.rpt", property_type="Graphical")

```
Copy to clipboard
# apply_report_template 

FarField.apply_report_template(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Graphical'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Apply report template.
Note
This method works in only in graphical mode. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path for the file to import. The extension supported is `".rpt"`. 

**property_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Property types to apply. Options are `"Graphical"`, `"Data"`, and `"All"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.ApplyReportTemplate

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.apply_report_template("template.rpt", property_type="Graphical")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.FarField.apply_report_template.rst.txt)

# apply_report_template 

FarField.apply_report_template(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _property_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Graphical'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Apply report template.
Note
This method works in only in graphical mode. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path for the file to import. The extension supported is `".rpt"`. 

**property_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Property types to apply. Options are `"Graphical"`, `"Data"`, and `"All"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.ApplyReportTemplate

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.apply_report_template("template.rpt", property_type="Graphical")

```
Copy to clipboard