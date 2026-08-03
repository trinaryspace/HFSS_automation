---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.statistical_eye_contour.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# statistical_eye_contour 

Reports.statistical_eye_contour(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _quantity_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 3_) → [AMIConturEyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram.html#ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram "ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a standard statistical AMI contour plot. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Expression to add into the report. The expression can be any of the available formula you can enter into the Electronics Desktop Report Editor. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is either the sweep name to use in the export or `LastAdaptive`. 

**quantity_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
For AMI analysis only, the quantity type. The default is `3`. Options are:
  * `0` for Initial Wave
  * `1` for Wave after Source
  * `2` for Wave after Channel
  * `3` for Wave after Probe.

Returns: 
     

`ansys.aedt.core.modules.report_templates.AMIConturEyeDiagram`
    
Examples

```
>>> from ansys.aedt.core import Circuit
>>> cir = Circuit()
>>> new_eye = cir.post.reports_by_category.statistical_eye_contour("V(Vout)")
>>> new_eye.unit_interval = "1e-9s"
>>> new_eye.time_stop = "100ns"
>>> new_eye.create()

```
Copy to clipboard
# statistical_eye_contour 

Reports.statistical_eye_contour(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _quantity_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 3_) → [AMIConturEyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram.html#ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram "ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a standard statistical AMI contour plot. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Expression to add into the report. The expression can be any of the available formula you can enter into the Electronics Desktop Report Editor. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is either the sweep name to use in the export or `LastAdaptive`. 

**quantity_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
For AMI analysis only, the quantity type. The default is `3`. Options are:
  * `0` for Initial Wave
  * `1` for Wave after Source
  * `2` for Wave after Channel
  * `3` for Wave after Probe.

Returns: 
     

`ansys.aedt.core.modules.report_templates.AMIConturEyeDiagram`
    
Examples

```
>>> from ansys.aedt.core import Circuit
>>> cir = Circuit()
>>> new_eye = cir.post.reports_by_category.statistical_eye_contour("V(Vout)")
>>> new_eye.unit_interval = "1e-9s"
>>> new_eye.time_stop = "100ns"
>>> new_eye.create()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.statistical_eye_contour.rst.txt)

# statistical_eye_contour 

Reports.statistical_eye_contour(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _quantity_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 3_) → [AMIConturEyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram.html#ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram "ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a standard statistical AMI contour plot. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Expression to add into the report. The expression can be any of the available formula you can enter into the Electronics Desktop Report Editor. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is either the sweep name to use in the export or `LastAdaptive`. 

**quantity_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
For AMI analysis only, the quantity type. The default is `3`. Options are:
  * `0` for Initial Wave
  * `1` for Wave after Source
  * `2` for Wave after Channel
  * `3` for Wave after Probe.

Returns: 
     

`ansys.aedt.core.modules.report_templates.AMIConturEyeDiagram`
    
Examples

```
>>> from ansys.aedt.core import Circuit
>>> cir = Circuit()
>>> new_eye = cir.post.reports_by_category.statistical_eye_contour("V(Vout)")
>>> new_eye.unit_interval = "1e-9s"
>>> new_eye.time_stop = "100ns"
>>> new_eye.create()

```
Copy to clipboard