---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_report.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# create_report 

SetupHFSS.create_report(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _domain : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Sweep'_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _primary_sweep_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _secondary_sweep_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _report_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _plot_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Rectangular Plot'_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _subdesign_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _polyline_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1001_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _sweep : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _matplotlib : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _hide_legend : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 800_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 450_) → [Standard](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.standard.Standard.html#ansys.aedt.core.visualization.report.standard.Standard "ansys.aedt.core.visualization.report.standard.Standard") 
    
Create a report in AEDT. It can be a 2D plot, 3D plot, polar plot, or data table. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more formulas to add to the report. Example is value = `"dB(S(1,1))"`. 

**domain**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot Domain. Options are “Sweep”, “Time”, “DCIR”. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all families including the primary sweep. The default is `{"Freq": ["All"]}`. 

**primary_sweep_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the primary sweep. The default is `"Freq"`. 

**secondary_sweep_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the secondary sweep variable in 3D Plots. 

**report_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Category of the Report to be created. If None default data Report will be used. The Report Category can be one of the types available for creating a report depend on the simulation setup. For example for a Far Field Plot in HFSS the UI shows the report category as “Create Far Fields Report”. The report category will be in this case “Far Fields”. Depending on the setup different categories are available. If None default category will be used (the first item in the Results drop down menu in AEDT). 

**plot_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The format of Data Visualization. Default is `Rectangular Plot`. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The default is `None`. It can be None, “Differential Pairs”,`”RL”, `”Sources”, “Vias”,`”Bondwires”, `”Probes” for Hfss3dLayout or Reduce Matrix Name for Q2d/Q3d solution or Infinite Sphere name for Far Fields Plot. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the plot. The default is `None`. 

**polyline_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), optional, 
    
Number of points for creating the report for plots on polylines. 

**subdesign_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Specify a subdesign ID to export a Touchstone file of this subdesign to. This parameter is valid only for a circuit. The default value is `None`. 

**sweep**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sweep adaptive setup to get solutions from. The default is `LastAdaptive`. 

**matplotlib**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use AEDT or ReportPlotter to generate the plot. Eye diagrams are not supported. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot when using ReportPlotter. The default is `True`. If matplotlib is `False`, this parameter is ignored. 

**hide_legend**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to hide the legend when using AEDT reporter. The default is `False`. 

**snapshot_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to image file if a snapshot is needed. The default is `None`. 

**width**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Snapshot image width. Default is `800` which takes Desktop size or 800 pixel. 

**height**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Snapshot image height. Default is `450` which takes Desktop size or 450 pixel. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.Standard`
    
`True` when successful, `False` when failed.
References

```
>>> oModule.CreateReport

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Circuit
>>> aedtapp = Circuit()
>>> aedtapp.post.create_report("dB(S(1,1))")

```
Copy to clipboard

```
>>> variations = aedtapp.available_variations.nominal_values
>>> aedtapp.post.setups[0].create_report("dB(S(1,1))", variations=variations, primary_sweep_variable="Freq")

```
Copy to clipboard

```
>>> aedtapp.post.create_report("S(1,1)", variations=variations, plot_type="Smith Chart")

```
Copy to clipboard
# create_report 

SetupHFSS.create_report(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _domain : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Sweep'_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _primary_sweep_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _secondary_sweep_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _report_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _plot_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Rectangular Plot'_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _subdesign_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _polyline_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1001_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _sweep : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _matplotlib : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _hide_legend : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 800_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 450_) → [Standard](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.standard.Standard.html#ansys.aedt.core.visualization.report.standard.Standard "ansys.aedt.core.visualization.report.standard.Standard") 
    
Create a report in AEDT. It can be a 2D plot, 3D plot, polar plot, or data table. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more formulas to add to the report. Example is value = `"dB(S(1,1))"`. 

**domain**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot Domain. Options are “Sweep”, “Time”, “DCIR”. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all families including the primary sweep. The default is `{"Freq": ["All"]}`. 

**primary_sweep_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the primary sweep. The default is `"Freq"`. 

**secondary_sweep_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the secondary sweep variable in 3D Plots. 

**report_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Category of the Report to be created. If None default data Report will be used. The Report Category can be one of the types available for creating a report depend on the simulation setup. For example for a Far Field Plot in HFSS the UI shows the report category as “Create Far Fields Report”. The report category will be in this case “Far Fields”. Depending on the setup different categories are available. If None default category will be used (the first item in the Results drop down menu in AEDT). 

**plot_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The format of Data Visualization. Default is `Rectangular Plot`. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The default is `None`. It can be None, “Differential Pairs”,`”RL”, `”Sources”, “Vias”,`”Bondwires”, `”Probes” for Hfss3dLayout or Reduce Matrix Name for Q2d/Q3d solution or Infinite Sphere name for Far Fields Plot. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the plot. The default is `None`. 

**polyline_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), optional, 
    
Number of points for creating the report for plots on polylines. 

**subdesign_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Specify a subdesign ID to export a Touchstone file of this subdesign to. This parameter is valid only for a circuit. The default value is `None`. 

**sweep**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sweep adaptive setup to get solutions from. The default is `LastAdaptive`. 

**matplotlib**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use AEDT or ReportPlotter to generate the plot. Eye diagrams are not supported. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot when using ReportPlotter. The default is `True`. If matplotlib is `False`, this parameter is ignored. 

**hide_legend**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to hide the legend when using AEDT reporter. The default is `False`. 

**snapshot_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to image file if a snapshot is needed. The default is `None`. 

**width**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Snapshot image width. Default is `800` which takes Desktop size or 800 pixel. 

**height**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Snapshot image height. Default is `450` which takes Desktop size or 450 pixel. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.Standard`
    
`True` when successful, `False` when failed.
References

```
>>> oModule.CreateReport

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Circuit
>>> aedtapp = Circuit()
>>> aedtapp.post.create_report("dB(S(1,1))")

```
Copy to clipboard

```
>>> variations = aedtapp.available_variations.nominal_values
>>> aedtapp.post.setups[0].create_report("dB(S(1,1))", variations=variations, primary_sweep_variable="Freq")

```
Copy to clipboard

```
>>> aedtapp.post.create_report("S(1,1)", variations=variations, plot_type="Smith Chart")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.create_report.rst.txt)

# create_report 

SetupHFSS.create_report(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _domain : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Sweep'_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _primary_sweep_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _secondary_sweep_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _report_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _plot_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Rectangular Plot'_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _subdesign_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _polyline_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1001_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _sweep : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _matplotlib : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _hide_legend : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 800_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 450_) → [Standard](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.standard.Standard.html#ansys.aedt.core.visualization.report.standard.Standard "ansys.aedt.core.visualization.report.standard.Standard") 
    
Create a report in AEDT. It can be a 2D plot, 3D plot, polar plot, or data table. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more formulas to add to the report. Example is value = `"dB(S(1,1))"`. 

**domain**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot Domain. Options are “Sweep”, “Time”, “DCIR”. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all families including the primary sweep. The default is `{"Freq": ["All"]}`. 

**primary_sweep_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the primary sweep. The default is `"Freq"`. 

**secondary_sweep_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the secondary sweep variable in 3D Plots. 

**report_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Category of the Report to be created. If None default data Report will be used. The Report Category can be one of the types available for creating a report depend on the simulation setup. For example for a Far Field Plot in HFSS the UI shows the report category as “Create Far Fields Report”. The report category will be in this case “Far Fields”. Depending on the setup different categories are available. If None default category will be used (the first item in the Results drop down menu in AEDT). 

**plot_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The format of Data Visualization. Default is `Rectangular Plot`. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The default is `None`. It can be None, “Differential Pairs”,`”RL”, `”Sources”, “Vias”,`”Bondwires”, `”Probes” for Hfss3dLayout or Reduce Matrix Name for Q2d/Q3d solution or Infinite Sphere name for Far Fields Plot. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the plot. The default is `None`. 

**polyline_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), optional, 
    
Number of points for creating the report for plots on polylines. 

**subdesign_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Specify a subdesign ID to export a Touchstone file of this subdesign to. This parameter is valid only for a circuit. The default value is `None`. 

**sweep**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the sweep adaptive setup to get solutions from. The default is `LastAdaptive`. 

**matplotlib**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use AEDT or ReportPlotter to generate the plot. Eye diagrams are not supported. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot when using ReportPlotter. The default is `True`. If matplotlib is `False`, this parameter is ignored. 

**hide_legend**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to hide the legend when using AEDT reporter. The default is `False`. 

**snapshot_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to image file if a snapshot is needed. The default is `None`. 

**width**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Snapshot image width. Default is `800` which takes Desktop size or 800 pixel. 

**height**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Snapshot image height. Default is `450` which takes Desktop size or 450 pixel. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.Standard`
    
`True` when successful, `False` when failed.
References

```
>>> oModule.CreateReport

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Circuit
>>> aedtapp = Circuit()
>>> aedtapp.post.create_report("dB(S(1,1))")

```
Copy to clipboard

```
>>> variations = aedtapp.available_variations.nominal_values
>>> aedtapp.post.setups[0].create_report("dB(S(1,1))", variations=variations, primary_sweep_variable="Freq")

```
Copy to clipboard

```
>>> aedtapp.post.create_report("S(1,1)", variations=variations, plot_type="Smith Chart")

```
Copy to clipboard