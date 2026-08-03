---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.spectral.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# spectral 

Reports.spectral(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [Spectral](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.standard.Spectral.html#ansys.aedt.core.visualization.report.standard.Spectral "ansys.aedt.core.visualization.report.standard.Spectral") 
    
Create a Spectral Report object. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Expression List to add into the report. The expression can be any of the available formula you can enter into the Electronics Desktop Report Editor. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.Spectrum`
    
Examples

```
>>> from ansys.aedt.core import Circuit
>>> cir = Circuit()
>>> new_eye = cir.post.reports_by_category.spectral("V(Vout)")
>>> new_eye.create()

```
Copy to clipboard
# spectral 

Reports.spectral(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [Spectral](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.standard.Spectral.html#ansys.aedt.core.visualization.report.standard.Spectral "ansys.aedt.core.visualization.report.standard.Spectral") 
    
Create a Spectral Report object. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Expression List to add into the report. The expression can be any of the available formula you can enter into the Electronics Desktop Report Editor. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.Spectrum`
    
Examples

```
>>> from ansys.aedt.core import Circuit
>>> cir = Circuit()
>>> new_eye = cir.post.reports_by_category.spectral("V(Vout)")
>>> new_eye.create()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.spectral.rst.txt)

# spectral 

Reports.spectral(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [Spectral](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.standard.Spectral.html#ansys.aedt.core.visualization.report.standard.Spectral "ansys.aedt.core.visualization.report.standard.Spectral") 
    
Create a Spectral Report object. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Expression List to add into the report. The expression can be any of the available formula you can enter into the Electronics Desktop Report Editor. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.Spectrum`
    
Examples

```
>>> from ansys.aedt.core import Circuit
>>> cir = Circuit()
>>> new_eye = cir.post.reports_by_category.spectral("V(Vout)")
>>> new_eye.create()

```
Copy to clipboard