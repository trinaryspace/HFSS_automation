---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.emi_receiver.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# emi_receiver 

Reports.emi_receiver(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [EMIReceiver](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.emi.EMIReceiver.html#ansys.aedt.core.visualization.report.emi.EMIReceiver "ansys.aedt.core.visualization.report.emi.EMIReceiver") 
    
Create an EMI receiver report. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more expressions to add into the report. An expression can be any of the formulas that can be entered into the Electronics Desktop Report Editor. 

**setup_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is either the sweep name to use in the export or `LastAdaptive`. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.EMIReceiver`
    
Examples

```
>>> from ansys.aedt.core import Circuit
>>> cir = Circuit()
>>> new_eye = cir.post.emi_receiver()
>>> new_eye.create()

```
Copy to clipboard
# emi_receiver 

Reports.emi_receiver(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [EMIReceiver](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.emi.EMIReceiver.html#ansys.aedt.core.visualization.report.emi.EMIReceiver "ansys.aedt.core.visualization.report.emi.EMIReceiver") 
    
Create an EMI receiver report. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more expressions to add into the report. An expression can be any of the formulas that can be entered into the Electronics Desktop Report Editor. 

**setup_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is either the sweep name to use in the export or `LastAdaptive`. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.EMIReceiver`
    
Examples

```
>>> from ansys.aedt.core import Circuit
>>> cir = Circuit()
>>> new_eye = cir.post.emi_receiver()
>>> new_eye.create()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.emi_receiver.rst.txt)

# emi_receiver 

Reports.emi_receiver(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [EMIReceiver](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.emi.EMIReceiver.html#ansys.aedt.core.visualization.report.emi.EMIReceiver "ansys.aedt.core.visualization.report.emi.EMIReceiver") 
    
Create an EMI receiver report. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more expressions to add into the report. An expression can be any of the formulas that can be entered into the Electronics Desktop Report Editor. 

**setup_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is either the sweep name to use in the export or `LastAdaptive`. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.EMIReceiver`
    
Examples

```
>>> from ansys.aedt.core import Circuit
>>> cir = Circuit()
>>> new_eye = cir.post.emi_receiver()
>>> new_eye.create()

```
Copy to clipboard