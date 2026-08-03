---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.standard.Spectral.create.html"
category: "reports"
domain: "PyAEDT / HFSS"
---

# create 

Spectral.create(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
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
>>> new_report = circuit.post.reports_by_category.spectral(["dB(V(net_11))"], "Transient")
>>> new_report.window = "Hanning"
>>> new_report.max_freq = "1GHz"
>>> new_report.time_start = "1ns"
>>> new_report.time_stop = "190ns"
>>> new_report.create()

```
Copy to clipboard
# create 

Spectral.create(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
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
>>> new_report = circuit.post.reports_by_category.spectral(["dB(V(net_11))"], "Transient")
>>> new_report.window = "Hanning"
>>> new_report.max_freq = "1GHz"
>>> new_report.time_start = "1ns"
>>> new_report.time_stop = "190ns"
>>> new_report.create()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.report.standard.Spectral.create.rst.txt)

# create 

Spectral.create(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
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
>>> new_report = circuit.post.reports_by_category.spectral(["dB(V(net_11))"], "Transient")
>>> new_report.window = "Hanning"
>>> new_report.max_freq = "1GHz"
>>> new_report.time_start = "1ns"
>>> new_report.time_stop = "190ns"
>>> new_report.create()

```
Copy to clipboard