---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_common_3d.PostProcessor3D.get_solution_data.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# get_solution_data 

PostProcessor3D.get_solution_data(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup_sweep_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _domain : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _primary_sweep_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _report_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _subdesign_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _polyline_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1001_, _math_formula : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [SolutionData](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.solution_data.SolutionData.html#ansys.aedt.core.visualization.post.solution_data.SolutionData "ansys.aedt.core.visualization.post.solution_data.SolutionData") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Get a simulation result from a solved setup and cast it in a `SolutionData` object.
Data to be retrieved from Electronics Desktop are any simulation results available in that specific simulation context. Most of the argument have some defaults which works for most of the `Standard` report quantities. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more formulas to add to the report. Example is value `"dB(S(1,1))"` or a list of values. Default is `None` which returns all traces. 

**setup_sweep_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**domain**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot Domain. Options are “Sweep” for frequency domain related results and “Time” for transient related data. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all families including the primary sweep. The default is `None` which uses the nominal variations of the setup. 

**primary_sweep_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the primary sweep. The default is `"None"` which, depending on the context, internally assigns the primary sweep to: 1. `Freq` for frequency domain results, 2. `Time` for transient results, 3. `Theta` for radiation patterns, 4. `distance` for field plot over a polyline. 

**report_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Category of the Report to be created. If `None` default data Report is used. The Report Category can be one of the types available for creating a report depend on the simulation setup. For example for a Far Field Plot in HFSS the UI shows the report category as “Create Far Fields Report”. The report category is “Far Fields” in this case. Depending on the setup different categories are available. If `None` default category is used (the first item in the Results drop down menu in AEDT). To get the list of available categories user can use method `available_report_types`. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
This is the context of the report. The default is `None`. It can be: 1. None 2. `"Differential Pairs"` 3. Reduce Matrix Name for Q2d/Q3d solution 4. Infinite Sphere name for Far Fields Plot. 5. Dictionary. If dictionary is passed, key is the report property name and value is property value. 6. For Maxwell 2D/3D eddy current solution types, this can be provided as a dictionary, where the key is the matrix name and value the reduced matrix. 

**subdesign_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Subdesign ID for exporting a Touchstone file of this subdesign. This parameter is valid for `Circuit` only. The default value is `None`. 

**polyline_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of points on which to create the report for plots on polylines. This parameter is valid for `Fields` plot only. 

**math_formula**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
One of the available AEDT mathematical formulas to apply. For example, `abs, dB`. 

Returns: 
     

[`ansys.aedt.core.visualization.post.solution_data.SolutionData`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.solution_data.SolutionData.html#ansys.aedt.core.visualization.post.solution_data.SolutionData "ansys.aedt.core.visualization.post.solution_data.SolutionData")
    
Solution Data object.
References

```
>>> oModule.GetSolutionDataPerVariation

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.post.create_report("dB(S(1,1))")
>>> variations = hfss.available_variations.nominal_values
>>> variations["Theta"] = ["All"]
>>> variations["Phi"] = ["All"]
>>> variations["Freq"] = ["30GHz"]
>>> data1 = hfss.post.get_solution_data(
...     "GainTotal",
...     hfss.nominal_adaptive,
...     variations=variations,
...     primary_sweep_variable="Phi",
...     context="3D",
...     report_category="Far Fields",
... )

```
Copy to clipboard

```
>>> data2 = hfss.post.get_solution_data(
...     "S(1,1)",
...     hfss.nominal_sweep,
...     variations=variations,
... )
>>> data2.plot()
>>> hfss.desktop_class.release_desktop(False, False)

```
Copy to clipboard

```
>>> from ansys.aedt.core import Maxwell2d
>>> m2d = Maxwell2d()
>>> data3 = m2d.post.get_solution_data(
...     "InputCurrent(PHA)",
...     domain="Time",
...     primary_sweep_variable="Time",
... )
>>> data3.plot("InputCurrent(PHA)")
>>> m2d.desktop_class.release_desktop(False, False)

```
Copy to clipboard

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> context = {"algorithm": "FFT", "max_frequency": "100MHz", "time_stop": "2.5us", "time_start": "0ps"}
>>> spectralPlotData = circuit.post.get_solution_data(
...     expressions="V(Vprobe1)", domain="Spectral", primary_sweep_variable="Spectrum", context=context
... )
>>> circuit.desktop_class.release_desktop(False, False)

```
Copy to clipboard

```
>>> from ansys.aedt.core import Maxwell3d
>>> m3d = Maxwell3d(solution_type="EddyCurrent")
>>> rectangle1 = m3d.modeler.create_rectangle(0, [0.5, 1.5, 0], [2.5, 5], name="Sheet1")
>>> rectangle2 = m3d.modeler.create_rectangle(0, [9, 1.5, 0], [2.5, 5], name="Sheet2")
>>> rectangle3 = m3d.modeler.create_rectangle(0, [16.5, 1.5, 0], [2.5, 5], name="Sheet3")
>>> m3d.assign_current(rectangle1.faces[0], amplitude=1, name="Cur1")
>>> m3d.assign_current(rectangle2.faces[0], amplitude=1, name="Cur2")
>>> m3d.assign_current(rectangle3.faces[0], amplitude=1, name="Cur3")
>>> L = m3d.assign_matrix(assignment=["Cur1", "Cur2", "Cur3"], matrix_name="Matrix1")
>>> out = L.join_series(sources=["Cur1", "Cur2"], matrix_name="ReducedMatrix1")
>>> expressions = m3d.post.available_report_quantities(
...     report_category="EddyCurrent", display_type="Data Table", context={"Matrix1": "ReducedMatrix1"}
... )
>>> data = m3d.post.get_solution_data(expressions=expressions, context={"Matrix1": "ReducedMatrix1"})
>>> m3d.desktop_class.release_desktop(False, False)

```
Copy to clipboard
# get_solution_data 

PostProcessor3D.get_solution_data(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup_sweep_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _domain : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _primary_sweep_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _report_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _subdesign_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _polyline_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1001_, _math_formula : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [SolutionData](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.solution_data.SolutionData.html#ansys.aedt.core.visualization.post.solution_data.SolutionData "ansys.aedt.core.visualization.post.solution_data.SolutionData") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Get a simulation result from a solved setup and cast it in a `SolutionData` object.
Data to be retrieved from Electronics Desktop are any simulation results available in that specific simulation context. Most of the argument have some defaults which works for most of the `Standard` report quantities. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more formulas to add to the report. Example is value `"dB(S(1,1))"` or a list of values. Default is `None` which returns all traces. 

**setup_sweep_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**domain**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot Domain. Options are “Sweep” for frequency domain related results and “Time” for transient related data. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all families including the primary sweep. The default is `None` which uses the nominal variations of the setup. 

**primary_sweep_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the primary sweep. The default is `"None"` which, depending on the context, internally assigns the primary sweep to: 1. `Freq` for frequency domain results, 2. `Time` for transient results, 3. `Theta` for radiation patterns, 4. `distance` for field plot over a polyline. 

**report_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Category of the Report to be created. If `None` default data Report is used. The Report Category can be one of the types available for creating a report depend on the simulation setup. For example for a Far Field Plot in HFSS the UI shows the report category as “Create Far Fields Report”. The report category is “Far Fields” in this case. Depending on the setup different categories are available. If `None` default category is used (the first item in the Results drop down menu in AEDT). To get the list of available categories user can use method `available_report_types`. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
This is the context of the report. The default is `None`. It can be: 1. None 2. `"Differential Pairs"` 3. Reduce Matrix Name for Q2d/Q3d solution 4. Infinite Sphere name for Far Fields Plot. 5. Dictionary. If dictionary is passed, key is the report property name and value is property value. 6. For Maxwell 2D/3D eddy current solution types, this can be provided as a dictionary, where the key is the matrix name and value the reduced matrix. 

**subdesign_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Subdesign ID for exporting a Touchstone file of this subdesign. This parameter is valid for `Circuit` only. The default value is `None`. 

**polyline_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of points on which to create the report for plots on polylines. This parameter is valid for `Fields` plot only. 

**math_formula**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
One of the available AEDT mathematical formulas to apply. For example, `abs, dB`. 

Returns: 
     

[`ansys.aedt.core.visualization.post.solution_data.SolutionData`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.solution_data.SolutionData.html#ansys.aedt.core.visualization.post.solution_data.SolutionData "ansys.aedt.core.visualization.post.solution_data.SolutionData")
    
Solution Data object.
References

```
>>> oModule.GetSolutionDataPerVariation

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.post.create_report("dB(S(1,1))")
>>> variations = hfss.available_variations.nominal_values
>>> variations["Theta"] = ["All"]
>>> variations["Phi"] = ["All"]
>>> variations["Freq"] = ["30GHz"]
>>> data1 = hfss.post.get_solution_data(
...     "GainTotal",
...     hfss.nominal_adaptive,
...     variations=variations,
...     primary_sweep_variable="Phi",
...     context="3D",
...     report_category="Far Fields",
... )

```
Copy to clipboard

```
>>> data2 = hfss.post.get_solution_data(
...     "S(1,1)",
...     hfss.nominal_sweep,
...     variations=variations,
... )
>>> data2.plot()
>>> hfss.desktop_class.release_desktop(False, False)

```
Copy to clipboard

```
>>> from ansys.aedt.core import Maxwell2d
>>> m2d = Maxwell2d()
>>> data3 = m2d.post.get_solution_data(
...     "InputCurrent(PHA)",
...     domain="Time",
...     primary_sweep_variable="Time",
... )
>>> data3.plot("InputCurrent(PHA)")
>>> m2d.desktop_class.release_desktop(False, False)

```
Copy to clipboard

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> context = {"algorithm": "FFT", "max_frequency": "100MHz", "time_stop": "2.5us", "time_start": "0ps"}
>>> spectralPlotData = circuit.post.get_solution_data(
...     expressions="V(Vprobe1)", domain="Spectral", primary_sweep_variable="Spectrum", context=context
... )
>>> circuit.desktop_class.release_desktop(False, False)

```
Copy to clipboard

```
>>> from ansys.aedt.core import Maxwell3d
>>> m3d = Maxwell3d(solution_type="EddyCurrent")
>>> rectangle1 = m3d.modeler.create_rectangle(0, [0.5, 1.5, 0], [2.5, 5], name="Sheet1")
>>> rectangle2 = m3d.modeler.create_rectangle(0, [9, 1.5, 0], [2.5, 5], name="Sheet2")
>>> rectangle3 = m3d.modeler.create_rectangle(0, [16.5, 1.5, 0], [2.5, 5], name="Sheet3")
>>> m3d.assign_current(rectangle1.faces[0], amplitude=1, name="Cur1")
>>> m3d.assign_current(rectangle2.faces[0], amplitude=1, name="Cur2")
>>> m3d.assign_current(rectangle3.faces[0], amplitude=1, name="Cur3")
>>> L = m3d.assign_matrix(assignment=["Cur1", "Cur2", "Cur3"], matrix_name="Matrix1")
>>> out = L.join_series(sources=["Cur1", "Cur2"], matrix_name="ReducedMatrix1")
>>> expressions = m3d.post.available_report_quantities(
...     report_category="EddyCurrent", display_type="Data Table", context={"Matrix1": "ReducedMatrix1"}
... )
>>> data = m3d.post.get_solution_data(expressions=expressions, context={"Matrix1": "ReducedMatrix1"})
>>> m3d.desktop_class.release_desktop(False, False)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_common_3d.PostProcessor3D.get_solution_data.rst.txt)

# get_solution_data 

PostProcessor3D.get_solution_data(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup_sweep_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _domain : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _primary_sweep_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _report_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _subdesign_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _polyline_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1001_, _math_formula : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [SolutionData](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.solution_data.SolutionData.html#ansys.aedt.core.visualization.post.solution_data.SolutionData "ansys.aedt.core.visualization.post.solution_data.SolutionData") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Get a simulation result from a solved setup and cast it in a `SolutionData` object.
Data to be retrieved from Electronics Desktop are any simulation results available in that specific simulation context. Most of the argument have some defaults which works for most of the `Standard` report quantities. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more formulas to add to the report. Example is value `"dB(S(1,1))"` or a list of values. Default is `None` which returns all traces. 

**setup_sweep_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**domain**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot Domain. Options are “Sweep” for frequency domain related results and “Time” for transient related data. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all families including the primary sweep. The default is `None` which uses the nominal variations of the setup. 

**primary_sweep_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the primary sweep. The default is `"None"` which, depending on the context, internally assigns the primary sweep to: 1. `Freq` for frequency domain results, 2. `Time` for transient results, 3. `Theta` for radiation patterns, 4. `distance` for field plot over a polyline. 

**report_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Category of the Report to be created. If `None` default data Report is used. The Report Category can be one of the types available for creating a report depend on the simulation setup. For example for a Far Field Plot in HFSS the UI shows the report category as “Create Far Fields Report”. The report category is “Far Fields” in this case. Depending on the setup different categories are available. If `None` default category is used (the first item in the Results drop down menu in AEDT). To get the list of available categories user can use method `available_report_types`. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
This is the context of the report. The default is `None`. It can be: 1. None 2. `"Differential Pairs"` 3. Reduce Matrix Name for Q2d/Q3d solution 4. Infinite Sphere name for Far Fields Plot. 5. Dictionary. If dictionary is passed, key is the report property name and value is property value. 6. For Maxwell 2D/3D eddy current solution types, this can be provided as a dictionary, where the key is the matrix name and value the reduced matrix. 

**subdesign_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Subdesign ID for exporting a Touchstone file of this subdesign. This parameter is valid for `Circuit` only. The default value is `None`. 

**polyline_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of points on which to create the report for plots on polylines. This parameter is valid for `Fields` plot only. 

**math_formula**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
One of the available AEDT mathematical formulas to apply. For example, `abs, dB`. 

Returns: 
     

[`ansys.aedt.core.visualization.post.solution_data.SolutionData`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.solution_data.SolutionData.html#ansys.aedt.core.visualization.post.solution_data.SolutionData "ansys.aedt.core.visualization.post.solution_data.SolutionData")
    
Solution Data object.
References

```
>>> oModule.GetSolutionDataPerVariation

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.post.create_report("dB(S(1,1))")
>>> variations = hfss.available_variations.nominal_values
>>> variations["Theta"] = ["All"]
>>> variations["Phi"] = ["All"]
>>> variations["Freq"] = ["30GHz"]
>>> data1 = hfss.post.get_solution_data(
...     "GainTotal",
...     hfss.nominal_adaptive,
...     variations=variations,
...     primary_sweep_variable="Phi",
...     context="3D",
...     report_category="Far Fields",
... )

```
Copy to clipboard

```
>>> data2 = hfss.post.get_solution_data(
...     "S(1,1)",
...     hfss.nominal_sweep,
...     variations=variations,
... )
>>> data2.plot()
>>> hfss.desktop_class.release_desktop(False, False)

```
Copy to clipboard

```
>>> from ansys.aedt.core import Maxwell2d
>>> m2d = Maxwell2d()
>>> data3 = m2d.post.get_solution_data(
...     "InputCurrent(PHA)",
...     domain="Time",
...     primary_sweep_variable="Time",
... )
>>> data3.plot("InputCurrent(PHA)")
>>> m2d.desktop_class.release_desktop(False, False)

```
Copy to clipboard

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> context = {"algorithm": "FFT", "max_frequency": "100MHz", "time_stop": "2.5us", "time_start": "0ps"}
>>> spectralPlotData = circuit.post.get_solution_data(
...     expressions="V(Vprobe1)", domain="Spectral", primary_sweep_variable="Spectrum", context=context
... )
>>> circuit.desktop_class.release_desktop(False, False)

```
Copy to clipboard

```
>>> from ansys.aedt.core import Maxwell3d
>>> m3d = Maxwell3d(solution_type="EddyCurrent")
>>> rectangle1 = m3d.modeler.create_rectangle(0, [0.5, 1.5, 0], [2.5, 5], name="Sheet1")
>>> rectangle2 = m3d.modeler.create_rectangle(0, [9, 1.5, 0], [2.5, 5], name="Sheet2")
>>> rectangle3 = m3d.modeler.create_rectangle(0, [16.5, 1.5, 0], [2.5, 5], name="Sheet3")
>>> m3d.assign_current(rectangle1.faces[0], amplitude=1, name="Cur1")
>>> m3d.assign_current(rectangle2.faces[0], amplitude=1, name="Cur2")
>>> m3d.assign_current(rectangle3.faces[0], amplitude=1, name="Cur3")
>>> L = m3d.assign_matrix(assignment=["Cur1", "Cur2", "Cur3"], matrix_name="Matrix1")
>>> out = L.join_series(sources=["Cur1", "Cur2"], matrix_name="ReducedMatrix1")
>>> expressions = m3d.post.available_report_quantities(
...     report_category="EddyCurrent", display_type="Data Table", context={"Matrix1": "ReducedMatrix1"}
... )
>>> data = m3d.post.get_solution_data(expressions=expressions, context={"Matrix1": "ReducedMatrix1"})
>>> m3d.desktop_class.release_desktop(False, False)

```
Copy to clipboard