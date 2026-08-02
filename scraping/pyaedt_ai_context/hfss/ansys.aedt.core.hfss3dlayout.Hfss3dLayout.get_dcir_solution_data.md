---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.get_dcir_solution_data.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# get_dcir_solution_data 

Hfss3dLayout.get_dcir_solution_data(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _show : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'RL'_, _category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Loop_Resistance'_) → [SolutionData](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.solution_data.SolutionData.html#ansys.aedt.core.visualization.post.solution_data.SolutionData "ansys.aedt.core.visualization.post.solution_data.SolutionData") 
    
Retrieve dcir solution data. Available element_names are dependent on element_type as below.
Sources [“Voltage”, “Current”, “Power”] “RL” [‘Loop Resistance’, ‘Path Resistance’, ‘Resistance’, ‘Inductance’] “Vias” [‘X’, ‘Y’, ‘Current’, ‘Limit’, ‘Resistance’, ‘IR Drop’, ‘Power’] “Bondwires” [‘Current’, ‘Limit’, ‘Resistance’, ‘IR Drop’] “Probes” [‘Voltage’]. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

**show**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the element. Options are `"Sources"`, ``"RL"`, ``"Vias"`, `"Bondwires"`, and `"Probes"`. 

**category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the element. Options are `"Voltage"`, ``"Current"`, ``"Power"`, `"Loop_Resistance"`, `"Path_Resistance"`, `"Resistance"`, `"Inductance"`, `"X"`, `"Y"`, `"Limit"` and `"IR Drop"`. 

Returns: 
     

`from` `ansys.aedt.core.modules.solutions.SolutionData` 
    
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss3d = Hfss3dLayout()
>>> solution_data = hfss3d.get_dcir_solution_data(setup="Setup1")

```
Copy to clipboard
# get_dcir_solution_data 

Hfss3dLayout.get_dcir_solution_data(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _show : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'RL'_, _category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Loop_Resistance'_) → [SolutionData](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.solution_data.SolutionData.html#ansys.aedt.core.visualization.post.solution_data.SolutionData "ansys.aedt.core.visualization.post.solution_data.SolutionData") 
    
Retrieve dcir solution data. Available element_names are dependent on element_type as below.
Sources [“Voltage”, “Current”, “Power”] “RL” [‘Loop Resistance’, ‘Path Resistance’, ‘Resistance’, ‘Inductance’] “Vias” [‘X’, ‘Y’, ‘Current’, ‘Limit’, ‘Resistance’, ‘IR Drop’, ‘Power’] “Bondwires” [‘Current’, ‘Limit’, ‘Resistance’, ‘IR Drop’] “Probes” [‘Voltage’]. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

**show**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the element. Options are `"Sources"`, ``"RL"`, ``"Vias"`, `"Bondwires"`, and `"Probes"`. 

**category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the element. Options are `"Voltage"`, ``"Current"`, ``"Power"`, `"Loop_Resistance"`, `"Path_Resistance"`, `"Resistance"`, `"Inductance"`, `"X"`, `"Y"`, `"Limit"` and `"IR Drop"`. 

Returns: 
     

`from` `ansys.aedt.core.modules.solutions.SolutionData` 
    
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss3d = Hfss3dLayout()
>>> solution_data = hfss3d.get_dcir_solution_data(setup="Setup1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.get_dcir_solution_data.rst.txt)

# get_dcir_solution_data 

Hfss3dLayout.get_dcir_solution_data(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _show : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'RL'_, _category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Loop_Resistance'_) → [SolutionData](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.solution_data.SolutionData.html#ansys.aedt.core.visualization.post.solution_data.SolutionData "ansys.aedt.core.visualization.post.solution_data.SolutionData") 
    
Retrieve dcir solution data. Available element_names are dependent on element_type as below.
Sources [“Voltage”, “Current”, “Power”] “RL” [‘Loop Resistance’, ‘Path Resistance’, ‘Resistance’, ‘Inductance’] “Vias” [‘X’, ‘Y’, ‘Current’, ‘Limit’, ‘Resistance’, ‘IR Drop’, ‘Power’] “Bondwires” [‘Current’, ‘Limit’, ‘Resistance’, ‘IR Drop’] “Probes” [‘Voltage’]. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

**show**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the element. Options are `"Sources"`, ``"RL"`, ``"Vias"`, `"Bondwires"`, and `"Probes"`. 

**category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the element. Options are `"Voltage"`, ``"Current"`, ``"Power"`, `"Loop_Resistance"`, `"Path_Resistance"`, `"Resistance"`, `"Inductance"`, `"X"`, `"Y"`, `"Limit"` and `"IR Drop"`. 

Returns: 
     

`from` `ansys.aedt.core.modules.solutions.SolutionData` 
    
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> hfss3d = Hfss3dLayout()
>>> solution_data = hfss3d.get_dcir_solution_data(setup="Setup1")

```
Copy to clipboard