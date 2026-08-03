---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualComplianceGenerator.add_erl_parameters.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# add_erl_parameters 

VirtualComplianceGenerator.add_erl_parameters(_design_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _traces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _pins : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _pass_fail : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)")_, _pass_fail_criteria : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'ERL'_, _project : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Add Com parameters computed by SpiSim into the configuration. 

Parameters: 
     

**design_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Design name. 

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to `cfg` file. 

**traces**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of traces to compute com parameters. 

**pins**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of list containing input pints and output pins on which compute com parameters. Pins can be names or numbers. 

**pass_fail**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether if to compute pass fail on this parameter or not. If True, then the parameter `pass_fail_criteria` has to be set accordingly. 

**pass_fail_criteria**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
If the criteria is greater 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the report. 

**project**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the project to use for the computation of this report. If `None` the default project will be used.
Examples

```
>>> from ansys.aedt.core.visualization.post.compliance import VirtualComplianceGenerator
>>> obj = VirtualComplianceGenerator()
>>> obj.add_erl_parameters(
...     design_name=1, config_file="example.cfg", traces=["Box1"], pins=["Box1"], pass_fail=True
... )

```
Copy to clipboard
# add_erl_parameters 

VirtualComplianceGenerator.add_erl_parameters(_design_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _traces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _pins : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _pass_fail : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)")_, _pass_fail_criteria : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'ERL'_, _project : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Add Com parameters computed by SpiSim into the configuration. 

Parameters: 
     

**design_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Design name. 

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to `cfg` file. 

**traces**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of traces to compute com parameters. 

**pins**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of list containing input pints and output pins on which compute com parameters. Pins can be names or numbers. 

**pass_fail**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether if to compute pass fail on this parameter or not. If True, then the parameter `pass_fail_criteria` has to be set accordingly. 

**pass_fail_criteria**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
If the criteria is greater 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the report. 

**project**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the project to use for the computation of this report. If `None` the default project will be used.
Examples

```
>>> from ansys.aedt.core.visualization.post.compliance import VirtualComplianceGenerator
>>> obj = VirtualComplianceGenerator()
>>> obj.add_erl_parameters(
...     design_name=1, config_file="example.cfg", traces=["Box1"], pins=["Box1"], pass_fail=True
... )

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualComplianceGenerator.add_erl_parameters.rst.txt)

# add_erl_parameters 

VirtualComplianceGenerator.add_erl_parameters(_design_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _traces : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _pins : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _pass_fail : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)")_, _pass_fail_criteria : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'ERL'_, _project : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Add Com parameters computed by SpiSim into the configuration. 

Parameters: 
     

**design_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Design name. 

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to `cfg` file. 

**traces**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of traces to compute com parameters. 

**pins**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of list containing input pints and output pins on which compute com parameters. Pins can be names or numbers. 

**pass_fail**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether if to compute pass fail on this parameter or not. If True, then the parameter `pass_fail_criteria` has to be set accordingly. 

**pass_fail_criteria**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
If the criteria is greater 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the report. 

**project**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to the project to use for the computation of this report. If `None` the default project will be used.
Examples

```
>>> from ansys.aedt.core.visualization.post.compliance import VirtualComplianceGenerator
>>> obj = VirtualComplianceGenerator()
>>> obj.add_erl_parameters(
...     design_name=1, config_file="example.cfg", traces=["Box1"], pins=["Box1"], pass_fail=True
... )

```
Copy to clipboard