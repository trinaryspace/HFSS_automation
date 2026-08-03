---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.create_pdf.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# create_pdf 

VirtualCompliance.create_pdf(_file_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _close_project : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Create the PDF report after the method `compute_report_data` is called. 

Parameters: 
     

**file_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Output file name. 

**close_project**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to close the project at the end of the report generation or not. Default is True. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Path to the output file.
Examples

```
>>> from ansys.aedt.core.visualization.post.compliance import VirtualCompliance
>>> obj = VirtualCompliance()
>>> obj.create_pdf(file_name="example.pdf")

```
Copy to clipboard
# create_pdf 

VirtualCompliance.create_pdf(_file_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _close_project : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Create the PDF report after the method `compute_report_data` is called. 

Parameters: 
     

**file_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Output file name. 

**close_project**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to close the project at the end of the report generation or not. Default is True. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Path to the output file.
Examples

```
>>> from ansys.aedt.core.visualization.post.compliance import VirtualCompliance
>>> obj = VirtualCompliance()
>>> obj.create_pdf(file_name="example.pdf")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.create_pdf.rst.txt)

# create_pdf 

VirtualCompliance.create_pdf(_file_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _close_project : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Create the PDF report after the method `compute_report_data` is called. 

Parameters: 
     

**file_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Output file name. 

**close_project**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to close the project at the end of the report generation or not. Default is True. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Path to the output file.
Examples

```
>>> from ansys.aedt.core.visualization.post.compliance import VirtualCompliance
>>> obj = VirtualCompliance()
>>> obj.create_pdf(file_name="example.pdf")

```
Copy to clipboard