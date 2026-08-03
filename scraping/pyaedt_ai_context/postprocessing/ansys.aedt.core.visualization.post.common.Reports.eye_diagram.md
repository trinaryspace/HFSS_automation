---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.eye_diagram.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# eye_diagram 

Reports.eye_diagram(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _quantity_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 3_, _statistical_analysis : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _unit_interval : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1ns'_) → [EyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.EyeDiagram.html#ansys.aedt.core.visualization.report.eye.EyeDiagram "ansys.aedt.core.visualization.report.eye.EyeDiagram") | [AMIEyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIEyeDiagram.html#ansys.aedt.core.visualization.report.eye.AMIEyeDiagram "ansys.aedt.core.visualization.report.eye.AMIEyeDiagram") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Create a Standard or Default Report object. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Expression to add into the report. The expression can be any of the available formula you can enter into the Electronics Desktop Report Editor. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**quantity_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
For AMI Analysis only, specify the quantity type. Options are: 0 for Initial Wave, 1 for Wave after Source, 2 for Wave after Channel and 3 for Wave after Probe. Default is 3. 

**statistical_analysis**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
For AMI Analysis only, whether to plot the statistical eye plot or transient eye plot. The default is `True`. 

**unit_interval**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Unit interval for the eye diagram. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.AMIEyeDiagram` or [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Examples

```
>>> from ansys.aedt.core import Circuit
>>> cir = Circuit()
>>> new_eye = cir.post.reports_by_category.eye_diagram("V(Vout)")
>>> new_eye.unit_interval = "1e-9s"
>>> new_eye.time_stop = "100ns"
>>> new_eye.create()

```
Copy to clipboard
# eye_diagram 

Reports.eye_diagram(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _quantity_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 3_, _statistical_analysis : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _unit_interval : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1ns'_) → [EyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.EyeDiagram.html#ansys.aedt.core.visualization.report.eye.EyeDiagram "ansys.aedt.core.visualization.report.eye.EyeDiagram") | [AMIEyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIEyeDiagram.html#ansys.aedt.core.visualization.report.eye.AMIEyeDiagram "ansys.aedt.core.visualization.report.eye.AMIEyeDiagram") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Create a Standard or Default Report object. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Expression to add into the report. The expression can be any of the available formula you can enter into the Electronics Desktop Report Editor. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**quantity_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
For AMI Analysis only, specify the quantity type. Options are: 0 for Initial Wave, 1 for Wave after Source, 2 for Wave after Channel and 3 for Wave after Probe. Default is 3. 

**statistical_analysis**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
For AMI Analysis only, whether to plot the statistical eye plot or transient eye plot. The default is `True`. 

**unit_interval**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Unit interval for the eye diagram. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.AMIEyeDiagram` or [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Examples

```
>>> from ansys.aedt.core import Circuit
>>> cir = Circuit()
>>> new_eye = cir.post.reports_by_category.eye_diagram("V(Vout)")
>>> new_eye.unit_interval = "1e-9s"
>>> new_eye.time_stop = "100ns"
>>> new_eye.create()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.eye_diagram.rst.txt)

# eye_diagram 

Reports.eye_diagram(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _quantity_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 3_, _statistical_analysis : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _unit_interval : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1ns'_) → [EyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.EyeDiagram.html#ansys.aedt.core.visualization.report.eye.EyeDiagram "ansys.aedt.core.visualization.report.eye.EyeDiagram") | [AMIEyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIEyeDiagram.html#ansys.aedt.core.visualization.report.eye.AMIEyeDiagram "ansys.aedt.core.visualization.report.eye.AMIEyeDiagram") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Create a Standard or Default Report object. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Expression to add into the report. The expression can be any of the available formula you can enter into the Electronics Desktop Report Editor. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**quantity_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
For AMI Analysis only, specify the quantity type. Options are: 0 for Initial Wave, 1 for Wave after Source, 2 for Wave after Channel and 3 for Wave after Probe. Default is 3. 

**statistical_analysis**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
For AMI Analysis only, whether to plot the statistical eye plot or transient eye plot. The default is `True`. 

**unit_interval**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Unit interval for the eye diagram. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.AMIEyeDiagram` or [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Examples

```
>>> from ansys.aedt.core import Circuit
>>> cir = Circuit()
>>> new_eye = cir.post.reports_by_category.eye_diagram("V(Vout)")
>>> new_eye.unit_interval = "1e-9s"
>>> new_eye.time_stop = "100ns"
>>> new_eye.create()

```
Copy to clipboard