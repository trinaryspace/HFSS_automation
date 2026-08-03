---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.emi.EMIReceiver.create.html"
category: "reports"
domain: "PyAEDT / HFSS"
---

# create 

EMIReceiver.create(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [EMIReceiver](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.emi.EMIReceiver.html#ansys.aedt.core.visualization.report.emi.EMIReceiver "ansys.aedt.core.visualization.report.emi.EMIReceiver") 
    
Create an EMI receiver report. 

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
>>> new_report = circuit.post.reports_by_category.emi_receiver()
>>> new_report.band = "2"
>>> new_report.emission = "RE"
>>> new_report.time_start = "1ns"
>>> new_report.time_stop = "2us"
>>> new_report.create()

```
Copy to clipboard
# create 

EMIReceiver.create(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [EMIReceiver](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.emi.EMIReceiver.html#ansys.aedt.core.visualization.report.emi.EMIReceiver "ansys.aedt.core.visualization.report.emi.EMIReceiver") 
    
Create an EMI receiver report. 

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
>>> new_report = circuit.post.reports_by_category.emi_receiver()
>>> new_report.band = "2"
>>> new_report.emission = "RE"
>>> new_report.time_start = "1ns"
>>> new_report.time_stop = "2us"
>>> new_report.create()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.report.emi.EMIReceiver.create.rst.txt)

# create 

EMIReceiver.create(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [EMIReceiver](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.emi.EMIReceiver.html#ansys.aedt.core.visualization.report.emi.EMIReceiver "ansys.aedt.core.visualization.report.emi.EMIReceiver") 
    
Create an EMI receiver report. 

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
>>> new_report = circuit.post.reports_by_category.emi_receiver()
>>> new_report.band = "2"
>>> new_report.emission = "RE"
>>> new_report.time_start = "1ns"
>>> new_report.time_stop = "2us"
>>> new_report.create()

```
Copy to clipboard