---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIEyeDiagram.clear_all_eye_measurements.html"
category: "reports"
domain: "PyAEDT / HFSS"
---

# clear_all_eye_measurements 

AMIEyeDiagram.clear_all_eye_measurements() → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Clear all eye measurements from the plot. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> rep = circuit.post.reports_by_category.eye_diagram("AEYEPROBE(OutputEye)", "QuickEyeAnalysis")
>>> rep.create()
>>> rep.clear_all_eye_measurements()

```
Copy to clipboard
# clear_all_eye_measurements 

AMIEyeDiagram.clear_all_eye_measurements() → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Clear all eye measurements from the plot. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> rep = circuit.post.reports_by_category.eye_diagram("AEYEPROBE(OutputEye)", "QuickEyeAnalysis")
>>> rep.create()
>>> rep.clear_all_eye_measurements()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIEyeDiagram.clear_all_eye_measurements.rst.txt)

# clear_all_eye_measurements 

AMIEyeDiagram.clear_all_eye_measurements() → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Clear all eye measurements from the plot. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> rep = circuit.post.reports_by_category.eye_diagram("AEYEPROBE(OutputEye)", "QuickEyeAnalysis")
>>> rep.create()
>>> rep.clear_all_eye_measurements()

```
Copy to clipboard