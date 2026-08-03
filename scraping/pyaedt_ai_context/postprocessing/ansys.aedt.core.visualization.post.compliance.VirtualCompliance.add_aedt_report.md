---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_aedt_report.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# add_aedt_report 

VirtualCompliance.add_aedt_report(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _report_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _design_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _traces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _setup_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _pass_fail : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _pass_fail_criteria =None_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Add a new custom aedt report to the compliance. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the report. 

**report_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Report type. Options are “contour eye diagram”, “eye diagram”, “frequency”, “statistical eye”, and “time”. 

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the config file. 

**design_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the AEDT design to be used to create the project. 

**traces**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Traces to be added. 

**setup_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup to use. If None, the nominal sweep will be used. 

**pass_fail**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if the pass/fail criteria has to be used to check the compliance or not. 

**pass_fail_criteria**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Pass/fail criteria to be used. If None, no criteria will be used. 

Returns: 
    
Examples

```
>>> from ansys.aedt.core.visualization.post.compliance import VirtualCompliance
>>> obj = VirtualCompliance()
>>> obj.add_aedt_report(
...     name="MyObject", report_type=1, config_file="project.cfg", design_name=1, traces=["Box1"]
... )

```
Copy to clipboard
# add_aedt_report 

VirtualCompliance.add_aedt_report(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _report_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _design_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _traces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _setup_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _pass_fail : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _pass_fail_criteria =None_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Add a new custom aedt report to the compliance. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the report. 

**report_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Report type. Options are “contour eye diagram”, “eye diagram”, “frequency”, “statistical eye”, and “time”. 

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the config file. 

**design_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the AEDT design to be used to create the project. 

**traces**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Traces to be added. 

**setup_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup to use. If None, the nominal sweep will be used. 

**pass_fail**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if the pass/fail criteria has to be used to check the compliance or not. 

**pass_fail_criteria**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Pass/fail criteria to be used. If None, no criteria will be used. 

Returns: 
    
Examples

```
>>> from ansys.aedt.core.visualization.post.compliance import VirtualCompliance
>>> obj = VirtualCompliance()
>>> obj.add_aedt_report(
...     name="MyObject", report_type=1, config_file="project.cfg", design_name=1, traces=["Box1"]
... )

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_aedt_report.rst.txt)

# add_aedt_report 

VirtualCompliance.add_aedt_report(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _report_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _design_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _traces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _setup_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _pass_fail : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _pass_fail_criteria =None_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Add a new custom aedt report to the compliance. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the report. 

**report_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Report type. Options are “contour eye diagram”, “eye diagram”, “frequency”, “statistical eye”, and “time”. 

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the config file. 

**design_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the AEDT design to be used to create the project. 

**traces**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Traces to be added. 

**setup_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup to use. If None, the nominal sweep will be used. 

**pass_fail**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if the pass/fail criteria has to be used to check the compliance or not. 

**pass_fail_criteria**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Pass/fail criteria to be used. If None, no criteria will be used. 

Returns: 
    
Examples

```
>>> from ansys.aedt.core.visualization.post.compliance import VirtualCompliance
>>> obj = VirtualCompliance()
>>> obj.add_aedt_report(
...     name="MyObject", report_type=1, config_file="project.cfg", design_name=1, traces=["Box1"]
... )

```
Copy to clipboard