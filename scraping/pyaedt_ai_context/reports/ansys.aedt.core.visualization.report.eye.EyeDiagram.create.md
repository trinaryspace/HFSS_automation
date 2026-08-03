---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.EyeDiagram.create.html"
category: "reports"
domain: "PyAEDT / HFSS"
---

# create 

EyeDiagram.create(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create an eye diagram report. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot name. The default is `None`, in which case the default name is used. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> rep = circuit.post.reports_by_category.eye_diagram("AEYEPROBE(OutputEye)", "QuickEyeAnalysis")
>>> rep.time_start = "0ps"
>>> rep.time_stop = "50us"
>>> rep.unit_interval = "1e-9"
>>> rep.create()

```
Copy to clipboard
# create 

EyeDiagram.create(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create an eye diagram report. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot name. The default is `None`, in which case the default name is used. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> rep = circuit.post.reports_by_category.eye_diagram("AEYEPROBE(OutputEye)", "QuickEyeAnalysis")
>>> rep.time_start = "0ps"
>>> rep.time_stop = "50us"
>>> rep.unit_interval = "1e-9"
>>> rep.create()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.EyeDiagram.create.rst.txt)

# create 

EyeDiagram.create(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create an eye diagram report. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot name. The default is `None`, in which case the default name is used. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> rep = circuit.post.reports_by_category.eye_diagram("AEYEPROBE(OutputEye)", "QuickEyeAnalysis")
>>> rep.time_start = "0ps"
>>> rep.time_stop = "50us"
>>> rep.unit_interval = "1e-9"
>>> rep.create()

```
Copy to clipboard