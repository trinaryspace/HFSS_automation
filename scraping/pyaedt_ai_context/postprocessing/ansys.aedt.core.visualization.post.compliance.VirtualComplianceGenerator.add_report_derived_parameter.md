---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualComplianceGenerator.add_report_derived_parameter.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# add_report_derived_parameter 

VirtualComplianceGenerator.add_report_derived_parameter(_design_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _parameter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _traces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _report_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _pass_fail_criteria : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _project : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Add report derived parameters computed by AEDT and python into the configuration. 

Parameters: 
     

**design_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Design name. 

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to `cfg` file. 

**parameter: str,**
    
Parameter name. Allowed value are `"skew"`. 

**traces**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of traces to compute com parameters. 

**report_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Report Type. 

**pass_fail_criteria**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Pass fail criterial for parameter. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the report. 

**project**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the project to use for the computation of this report. If `None` the default project will be used.
Examples

```
>>> from ansys.aedt.core.visualization.post.compliance import VirtualComplianceGenerator
>>> obj = VirtualComplianceGenerator()
>>> obj.add_report_derived_parameter(
...     design_name=1,
...     config_file="example.cfg",
...     parameter=1,
...     traces=["Box1"],
...     report_type=1,
...     pass_fail_criteria=1.0,
...     name="MyObject",
... )

```
Copy to clipboard
# add_report_derived_parameter 

VirtualComplianceGenerator.add_report_derived_parameter(_design_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _parameter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _traces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _report_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _pass_fail_criteria : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _project : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Add report derived parameters computed by AEDT and python into the configuration. 

Parameters: 
     

**design_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Design name. 

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to `cfg` file. 

**parameter: str,**
    
Parameter name. Allowed value are `"skew"`. 

**traces**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of traces to compute com parameters. 

**report_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Report Type. 

**pass_fail_criteria**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Pass fail criterial for parameter. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the report. 

**project**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the project to use for the computation of this report. If `None` the default project will be used.
Examples

```
>>> from ansys.aedt.core.visualization.post.compliance import VirtualComplianceGenerator
>>> obj = VirtualComplianceGenerator()
>>> obj.add_report_derived_parameter(
...     design_name=1,
...     config_file="example.cfg",
...     parameter=1,
...     traces=["Box1"],
...     report_type=1,
...     pass_fail_criteria=1.0,
...     name="MyObject",
... )

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualComplianceGenerator.add_report_derived_parameter.rst.txt)

# add_report_derived_parameter 

VirtualComplianceGenerator.add_report_derived_parameter(_design_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _parameter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _traces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _report_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _pass_fail_criteria : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _project : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Add report derived parameters computed by AEDT and python into the configuration. 

Parameters: 
     

**design_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Design name. 

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to `cfg` file. 

**parameter: str,**
    
Parameter name. Allowed value are `"skew"`. 

**traces**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of traces to compute com parameters. 

**report_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Report Type. 

**pass_fail_criteria**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Pass fail criterial for parameter. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the report. 

**project**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the project to use for the computation of this report. If `None` the default project will be used.
Examples

```
>>> from ansys.aedt.core.visualization.post.compliance import VirtualComplianceGenerator
>>> obj = VirtualComplianceGenerator()
>>> obj.add_report_derived_parameter(
...     design_name=1,
...     config_file="example.cfg",
...     parameter=1,
...     traces=["Box1"],
...     report_type=1,
...     pass_fail_criteria=1.0,
...     name="MyObject",
... )

```
Copy to clipboard