---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.create_compliance_report.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# create_compliance_report 

VirtualCompliance.create_compliance_report(_file_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'compliance_test.pdf'_, _close_project : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Create the Virtual Compliance report. 

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
>>> obj.create_compliance_report(file_name="example.pdf", close_project=True)

```
Copy to clipboard
# create_compliance_report 

VirtualCompliance.create_compliance_report(_file_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'compliance_test.pdf'_, _close_project : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Create the Virtual Compliance report. 

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
>>> obj.create_compliance_report(file_name="example.pdf", close_project=True)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.create_compliance_report.rst.txt)

# create_compliance_report 

VirtualCompliance.create_compliance_report(_file_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'compliance_test.pdf'_, _close_project : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Create the Virtual Compliance report. 

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
>>> obj.create_compliance_report(file_name="example.pdf", close_project=True)

```
Copy to clipboard