---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualComplianceGenerator.add_report_from_folder.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# add_report_from_folder 

VirtualComplianceGenerator.add_report_from_folder(_input_folder : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _design_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _group_plots : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _project : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Add multiple reports from a folder. 

Parameters: 
     

**input_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to the folder containing configuration files. 

**design_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of design to apply the configuration. 

**group_plots**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether to group plot traces or not.
Examples

```
>>> from ansys.aedt.core.visualization.post.compliance import VirtualComplianceGenerator
>>> obj = VirtualComplianceGenerator()
>>> obj.add_report_from_folder(input_folder="example.cfg", design_name=1)

```
Copy to clipboard
# add_report_from_folder 

VirtualComplianceGenerator.add_report_from_folder(_input_folder : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _design_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _group_plots : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _project : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Add multiple reports from a folder. 

Parameters: 
     

**input_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to the folder containing configuration files. 

**design_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of design to apply the configuration. 

**group_plots**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether to group plot traces or not.
Examples

```
>>> from ansys.aedt.core.visualization.post.compliance import VirtualComplianceGenerator
>>> obj = VirtualComplianceGenerator()
>>> obj.add_report_from_folder(input_folder="example.cfg", design_name=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualComplianceGenerator.add_report_from_folder.rst.txt)

# add_report_from_folder 

VirtualComplianceGenerator.add_report_from_folder(_input_folder : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _design_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _group_plots : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _project : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Add multiple reports from a folder. 

Parameters: 
     

**input_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to the folder containing configuration files. 

**design_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of design to apply the configuration. 

**group_plots**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether to group plot traces or not.
Examples

```
>>> from ansys.aedt.core.visualization.post.compliance import VirtualComplianceGenerator
>>> obj = VirtualComplianceGenerator()
>>> obj.add_report_from_folder(input_folder="example.cfg", design_name=1)

```
Copy to clipboard