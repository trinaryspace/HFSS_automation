---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIEyeDiagram.rectangular_plot.html"
category: "reports"
domain: "PyAEDT / HFSS"
---

# rectangular_plot 

AMIEyeDiagram.rectangular_plot(_enable : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Enable or disable the rectangular plot on the chart. 

Parameters: 
     

**enable**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether to enable the rectangular plot. The default is `True`. When `False`, the rectangular plot is disabled. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> rep = circuit.post.reports_by_category.eye_diagram("AEYEPROBE(OutputEye)", "QuickEyeAnalysis")
>>> rep.create()
>>> rep.rectangular_plot(False)

```
Copy to clipboard
# rectangular_plot 

AMIEyeDiagram.rectangular_plot(_enable : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Enable or disable the rectangular plot on the chart. 

Parameters: 
     

**enable**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether to enable the rectangular plot. The default is `True`. When `False`, the rectangular plot is disabled. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> rep = circuit.post.reports_by_category.eye_diagram("AEYEPROBE(OutputEye)", "QuickEyeAnalysis")
>>> rep.create()
>>> rep.rectangular_plot(False)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIEyeDiagram.rectangular_plot.rst.txt)

# rectangular_plot 

AMIEyeDiagram.rectangular_plot(_enable : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Enable or disable the rectangular plot on the chart. 

Parameters: 
     

**enable**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether to enable the rectangular plot. The default is `True`. When `False`, the rectangular plot is disabled. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> rep = circuit.post.reports_by_category.eye_diagram("AEYEPROBE(OutputEye)", "QuickEyeAnalysis")
>>> rep.create()
>>> rep.rectangular_plot(False)

```
Copy to clipboard