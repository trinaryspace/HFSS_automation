---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.get_solution_data.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# get_solution_data 

Setup.get_solution_data(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _domain : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _primary_sweep_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _report_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _polyline_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1001_, _math_formula : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _sweep : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [SolutionData](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.solution_data.SolutionData.html#ansys.aedt.core.visualization.post.solution_data.SolutionData "ansys.aedt.core.visualization.post.solution_data.SolutionData") 
    
Get a simulation result from a solved setup and cast it in a `SolutionData` object.
Data to be retrieved from Electronics Desktop are any simulation results available in that specific simulation context. Most of the argument have some defaults which works for most of the `Standard` report quantities. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more formulas to add to the report. Example is value `"dB(S(1,1))"` or a list of values. Default is None which will return all traces. 

**domain**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot Domain. Options are “Sweep” for frequency domain related results and “Time” for transient related data. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all families including the primary sweep. The default is `None` which will use the nominal variations of the setup. 

**primary_sweep_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the primary sweep. The default is `"None"` which, depending on the context, will internally assign the primary sweep to: 1. `Freq` for frequency domain results, 2. `Time` for transient results, 3. `Theta` for radiation patterns, 4. `distance` for field plot over a polyline. 

**report_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Category of the Report to be created. If None default data Report will be used. The Report Category can be one of the types available for creating a report depend on the simulation setup. For example for a Far Field Plot in HFSS the UI shows the report category as “Create Far Fields Report”. The report category will be in this case “Far Fields”. Depending on the setup different categories are available. If None default category will be used (the first item in the Results drop down menu in AEDT). To get the list of available categories user can use method `available_report_types`. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
This is the context of the report. The default is `None`. It can be: 1. None 2. Infinite Sphere name for Far Fields Plot. 3. Dictionary. If dictionary is passed, key is the report property name and value is property value. 

**polyline_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of points on which to create the report for plots on polylines. This parameter is valid for `Fields` plot only. 

**math_formula**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
One of the available AEDT mathematical formulas to apply. For example, `abs, dB`. 

**sweep**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sweep adaptive setup to get solutions from. the default is `LastAdaptive`. 

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
>>> aedtapp = Hfss()
>>> aedtapp.post.create_report("dB(S(1,1))")

```
Copy to clipboard

```
>>> variations = aedtapp.available_variations.nominal_values
>>> variations["Theta"] = ["All"]
>>> variations["Phi"] = ["All"]
>>> variations["Freq"] = ["30GHz"]
>>> data1 = aedtapp.post.get_solution_data(
...     "GainTotal",
...     aedtapp.nominal_adaptive,
...     variations=variations,
...     primary_sweep_variable="Phi",
...     report_category="Far Fields",
...     context="3D",
... )

```
Copy to clipboard

```
>>> data2 = aedtapp.post.get_solution_data("S(1,1)", aedtapp.nominal_sweep, variations=variations)
>>> data2.plot()

```
Copy to clipboard

```
>>> from ansys.aedt.core import Maxwell2d
>>> maxwell_2d = Maxwell2d()
>>> data3 = maxwell_2d.post.get_solution_data("InputCurrent(PHA)", domain="Time", primary_sweep_variable="Time")
>>> data3.plot("InputCurrent(PHA)")

```
Copy to clipboard

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> context = {"algorithm": "FFT", "max_frequency": "100MHz", "time_stop": "2.5us", "time_start": "0ps"}
>>> spectralPlotData = circuit.post.get_solution_data(
...     expressions="V(Vprobe1)", domain="Spectral", primary_sweep_variable="Spectrum", context=context
... )

```
Copy to clipboard
# get_solution_data 

Setup.get_solution_data(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _domain : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _primary_sweep_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _report_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _polyline_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1001_, _math_formula : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _sweep : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [SolutionData](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.solution_data.SolutionData.html#ansys.aedt.core.visualization.post.solution_data.SolutionData "ansys.aedt.core.visualization.post.solution_data.SolutionData") 
    
Get a simulation result from a solved setup and cast it in a `SolutionData` object.
Data to be retrieved from Electronics Desktop are any simulation results available in that specific simulation context. Most of the argument have some defaults which works for most of the `Standard` report quantities. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more formulas to add to the report. Example is value `"dB(S(1,1))"` or a list of values. Default is None which will return all traces. 

**domain**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot Domain. Options are “Sweep” for frequency domain related results and “Time” for transient related data. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all families including the primary sweep. The default is `None` which will use the nominal variations of the setup. 

**primary_sweep_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the primary sweep. The default is `"None"` which, depending on the context, will internally assign the primary sweep to: 1. `Freq` for frequency domain results, 2. `Time` for transient results, 3. `Theta` for radiation patterns, 4. `distance` for field plot over a polyline. 

**report_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Category of the Report to be created. If None default data Report will be used. The Report Category can be one of the types available for creating a report depend on the simulation setup. For example for a Far Field Plot in HFSS the UI shows the report category as “Create Far Fields Report”. The report category will be in this case “Far Fields”. Depending on the setup different categories are available. If None default category will be used (the first item in the Results drop down menu in AEDT). To get the list of available categories user can use method `available_report_types`. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
This is the context of the report. The default is `None`. It can be: 1. None 2. Infinite Sphere name for Far Fields Plot. 3. Dictionary. If dictionary is passed, key is the report property name and value is property value. 

**polyline_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of points on which to create the report for plots on polylines. This parameter is valid for `Fields` plot only. 

**math_formula**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
One of the available AEDT mathematical formulas to apply. For example, `abs, dB`. 

**sweep**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sweep adaptive setup to get solutions from. the default is `LastAdaptive`. 

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
>>> aedtapp = Hfss()
>>> aedtapp.post.create_report("dB(S(1,1))")

```
Copy to clipboard

```
>>> variations = aedtapp.available_variations.nominal_values
>>> variations["Theta"] = ["All"]
>>> variations["Phi"] = ["All"]
>>> variations["Freq"] = ["30GHz"]
>>> data1 = aedtapp.post.get_solution_data(
...     "GainTotal",
...     aedtapp.nominal_adaptive,
...     variations=variations,
...     primary_sweep_variable="Phi",
...     report_category="Far Fields",
...     context="3D",
... )

```
Copy to clipboard

```
>>> data2 = aedtapp.post.get_solution_data("S(1,1)", aedtapp.nominal_sweep, variations=variations)
>>> data2.plot()

```
Copy to clipboard

```
>>> from ansys.aedt.core import Maxwell2d
>>> maxwell_2d = Maxwell2d()
>>> data3 = maxwell_2d.post.get_solution_data("InputCurrent(PHA)", domain="Time", primary_sweep_variable="Time")
>>> data3.plot("InputCurrent(PHA)")

```
Copy to clipboard

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> context = {"algorithm": "FFT", "max_frequency": "100MHz", "time_stop": "2.5us", "time_start": "0ps"}
>>> spectralPlotData = circuit.post.get_solution_data(
...     expressions="V(Vprobe1)", domain="Spectral", primary_sweep_variable="Spectrum", context=context
... )

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.get_solution_data.rst.txt)

# get_solution_data 

Setup.get_solution_data(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _domain : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _primary_sweep_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _report_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _polyline_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1001_, _math_formula : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _sweep : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [SolutionData](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.solution_data.SolutionData.html#ansys.aedt.core.visualization.post.solution_data.SolutionData "ansys.aedt.core.visualization.post.solution_data.SolutionData") 
    
Get a simulation result from a solved setup and cast it in a `SolutionData` object.
Data to be retrieved from Electronics Desktop are any simulation results available in that specific simulation context. Most of the argument have some defaults which works for most of the `Standard` report quantities. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more formulas to add to the report. Example is value `"dB(S(1,1))"` or a list of values. Default is None which will return all traces. 

**domain**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot Domain. Options are “Sweep” for frequency domain related results and “Time” for transient related data. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all families including the primary sweep. The default is `None` which will use the nominal variations of the setup. 

**primary_sweep_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the primary sweep. The default is `"None"` which, depending on the context, will internally assign the primary sweep to: 1. `Freq` for frequency domain results, 2. `Time` for transient results, 3. `Theta` for radiation patterns, 4. `distance` for field plot over a polyline. 

**report_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Category of the Report to be created. If None default data Report will be used. The Report Category can be one of the types available for creating a report depend on the simulation setup. For example for a Far Field Plot in HFSS the UI shows the report category as “Create Far Fields Report”. The report category will be in this case “Far Fields”. Depending on the setup different categories are available. If None default category will be used (the first item in the Results drop down menu in AEDT). To get the list of available categories user can use method `available_report_types`. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
This is the context of the report. The default is `None`. It can be: 1. None 2. Infinite Sphere name for Far Fields Plot. 3. Dictionary. If dictionary is passed, key is the report property name and value is property value. 

**polyline_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of points on which to create the report for plots on polylines. This parameter is valid for `Fields` plot only. 

**math_formula**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
One of the available AEDT mathematical formulas to apply. For example, `abs, dB`. 

**sweep**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sweep adaptive setup to get solutions from. the default is `LastAdaptive`. 

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
>>> aedtapp = Hfss()
>>> aedtapp.post.create_report("dB(S(1,1))")

```
Copy to clipboard

```
>>> variations = aedtapp.available_variations.nominal_values
>>> variations["Theta"] = ["All"]
>>> variations["Phi"] = ["All"]
>>> variations["Freq"] = ["30GHz"]
>>> data1 = aedtapp.post.get_solution_data(
...     "GainTotal",
...     aedtapp.nominal_adaptive,
...     variations=variations,
...     primary_sweep_variable="Phi",
...     report_category="Far Fields",
...     context="3D",
... )

```
Copy to clipboard

```
>>> data2 = aedtapp.post.get_solution_data("S(1,1)", aedtapp.nominal_sweep, variations=variations)
>>> data2.plot()

```
Copy to clipboard

```
>>> from ansys.aedt.core import Maxwell2d
>>> maxwell_2d = Maxwell2d()
>>> data3 = maxwell_2d.post.get_solution_data("InputCurrent(PHA)", domain="Time", primary_sweep_variable="Time")
>>> data3.plot("InputCurrent(PHA)")

```
Copy to clipboard

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> context = {"algorithm": "FFT", "max_frequency": "100MHz", "time_stop": "2.5us", "time_start": "0ps"}
>>> spectralPlotData = circuit.post.get_solution_data(
...     expressions="V(Vprobe1)", domain="Spectral", primary_sweep_variable="Spectrum", context=context
... )

```
Copy to clipboard