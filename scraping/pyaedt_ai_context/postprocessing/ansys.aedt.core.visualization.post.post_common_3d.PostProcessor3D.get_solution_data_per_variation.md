---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_common_3d.PostProcessor3D.get_solution_data_per_variation.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# get_solution_data_per_variation 

PostProcessor3D.get_solution_data_per_variation(_solution_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Far Fields'_, _setup_sweep_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _sweeps : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) → [SolutionData](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.solution_data.SolutionData.html#ansys.aedt.core.visualization.post.solution_data.SolutionData "ansys.aedt.core.visualization.post.solution_data.SolutionData") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Retrieve solution data for each variation. 

Parameters: 
     

**solution_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the solution. For example, `"Far Fields"` or `"Modal Solution Data"`. The default is `"Far Fields"`. 

**setup_sweep_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup for computing the report. The default is `""`, in which case `"nominal adaptive"` is used. 

**context**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of context variables. The default is `None`. 

**sweeps**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of variables and values. The default is `None`, in which case this list is used: `{'Theta': 'All', 'Phi': 'All', 'Freq': 'All'}`. 

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more traces to include. The default is `""`. 

Returns: 
     

`from` `ansys.aedt.core.modules.solutions.SolutionData` 
    
References

```
>>> oModule.GetSolutionDataPerVariation

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.common import PostProcessorCommon
>>> obj = PostProcessorCommon()
>>> obj.get_solution_data_per_variation()

```
Copy to clipboard
# get_solution_data_per_variation 

PostProcessor3D.get_solution_data_per_variation(_solution_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Far Fields'_, _setup_sweep_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _sweeps : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) → [SolutionData](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.solution_data.SolutionData.html#ansys.aedt.core.visualization.post.solution_data.SolutionData "ansys.aedt.core.visualization.post.solution_data.SolutionData") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Retrieve solution data for each variation. 

Parameters: 
     

**solution_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the solution. For example, `"Far Fields"` or `"Modal Solution Data"`. The default is `"Far Fields"`. 

**setup_sweep_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup for computing the report. The default is `""`, in which case `"nominal adaptive"` is used. 

**context**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of context variables. The default is `None`. 

**sweeps**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of variables and values. The default is `None`, in which case this list is used: `{'Theta': 'All', 'Phi': 'All', 'Freq': 'All'}`. 

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more traces to include. The default is `""`. 

Returns: 
     

`from` `ansys.aedt.core.modules.solutions.SolutionData` 
    
References

```
>>> oModule.GetSolutionDataPerVariation

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.common import PostProcessorCommon
>>> obj = PostProcessorCommon()
>>> obj.get_solution_data_per_variation()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_common_3d.PostProcessor3D.get_solution_data_per_variation.rst.txt)

# get_solution_data_per_variation 

PostProcessor3D.get_solution_data_per_variation(_solution_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Far Fields'_, _setup_sweep_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _sweeps : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) → [SolutionData](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.solution_data.SolutionData.html#ansys.aedt.core.visualization.post.solution_data.SolutionData "ansys.aedt.core.visualization.post.solution_data.SolutionData") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Retrieve solution data for each variation. 

Parameters: 
     

**solution_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the solution. For example, `"Far Fields"` or `"Modal Solution Data"`. The default is `"Far Fields"`. 

**setup_sweep_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup for computing the report. The default is `""`, in which case `"nominal adaptive"` is used. 

**context**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of context variables. The default is `None`. 

**sweeps**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of variables and values. The default is `None`, in which case this list is used: `{'Theta': 'All', 'Phi': 'All', 'Freq': 'All'}`. 

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more traces to include. The default is `""`. 

Returns: 
     

`from` `ansys.aedt.core.modules.solutions.SolutionData` 
    
References

```
>>> oModule.GetSolutionDataPerVariation

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.common import PostProcessorCommon
>>> obj = PostProcessorCommon()
>>> obj.get_solution_data_per_variation()

```
Copy to clipboard