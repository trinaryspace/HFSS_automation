---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIEyeDiagram.export_mask_violation.html"
category: "reports"
domain: "PyAEDT / HFSS"
---

# export_mask_violation 

AMIEyeDiagram.export_mask_violation(_output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export the eye diagram mask violations to a TAB file. 

Parameters: 
     

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the TAB file. The default is `None`, in which case the violations are exported to a TAB file in the working directory. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Output file path if a TAB file is created.
Examples

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> rep = circuit.post.reports_by_category.eye_diagram("AEYEPROBE(OutputEye)", "QuickEyeAnalysis")
>>> rep.create()
>>> rep.export_mask_violation()

```
Copy to clipboard
# export_mask_violation 

AMIEyeDiagram.export_mask_violation(_output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export the eye diagram mask violations to a TAB file. 

Parameters: 
     

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the TAB file. The default is `None`, in which case the violations are exported to a TAB file in the working directory. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Output file path if a TAB file is created.
Examples

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> rep = circuit.post.reports_by_category.eye_diagram("AEYEPROBE(OutputEye)", "QuickEyeAnalysis")
>>> rep.create()
>>> rep.export_mask_violation()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIEyeDiagram.export_mask_violation.rst.txt)

# export_mask_violation 

AMIEyeDiagram.export_mask_violation(_output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export the eye diagram mask violations to a TAB file. 

Parameters: 
     

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the TAB file. The default is `None`, in which case the violations are exported to a TAB file in the working directory. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Output file path if a TAB file is created.
Examples

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> rep = circuit.post.reports_by_category.eye_diagram("AEYEPROBE(OutputEye)", "QuickEyeAnalysis")
>>> rep.create()
>>> rep.export_mask_violation()

```
Copy to clipboard