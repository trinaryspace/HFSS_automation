---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_common_3d.PostProcessor3D.create_report.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# create_report 

PostProcessor3D.create_report(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup_sweep_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _domain : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Sweep'_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _primary_sweep_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _secondary_sweep_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _report_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _plot_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Rectangular Plot'_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _subdesign_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _polyline_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1001_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _matplotlib : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _hide_legend : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 800_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 450_) → [Standard](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.standard.Standard.html#ansys.aedt.core.visualization.report.standard.Standard "ansys.aedt.core.visualization.report.standard.Standard") | [AMIEyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIEyeDiagram.html#ansys.aedt.core.visualization.report.eye.AMIEyeDiagram "ansys.aedt.core.visualization.report.eye.AMIEyeDiagram") | [AMIConturEyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram.html#ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram "ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram") | [EMIReceiver](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.emi.EMIReceiver.html#ansys.aedt.core.visualization.report.emi.EMIReceiver "ansys.aedt.core.visualization.report.emi.EMIReceiver") | [EyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.EyeDiagram.html#ansys.aedt.core.visualization.report.eye.EyeDiagram "ansys.aedt.core.visualization.report.eye.EyeDiagram") | CircuitNetlistReport | [Fields](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.Fields.html#ansys.aedt.core.visualization.report.field.Fields "ansys.aedt.core.visualization.report.field.Fields") | [FarField](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.FarField.html#ansys.aedt.core.visualization.report.field.FarField "ansys.aedt.core.visualization.report.field.FarField") | [NearField](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.NearField.html#ansys.aedt.core.visualization.report.field.NearField "ansys.aedt.core.visualization.report.field.NearField") | [Spectral](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.standard.Spectral.html#ansys.aedt.core.visualization.report.standard.Spectral "ansys.aedt.core.visualization.report.standard.Spectral") | [ReportPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a report in AEDT or in Matplotlib. It can be a 2D plot, 3D plot, polar plot, or a data table. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more formulas to add to the report. Example is value = `"dB(S(1,1))"`. 

**setup_sweep_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Setup name with the sweep. The default is `None`, in which case the first setup and sweep is selected. For Circuit Netlist designs only, specify the solution name as listed in `ansys.aedt.core.generic.aedt_constants.CircuitNetlistConstants`. 

**domain**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot Domain. Options are “Sweep”, “Time”, “DCIR”. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all families including the primary sweep. The default is `{"Freq": ["All"]}`. 

**primary_sweep_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the primary sweep. The default is `"Freq"`. 

**secondary_sweep_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the secondary sweep variable in 3D Plots. 

**report_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Category of the Report to be created. If None default data Report is used. The Report Category can be one of the types available for creating a report depend on the simulation setup. For example for a Far Field Plot in HFSS the UI shows the report category as “Create Far Fields Report”. The report category is “Far Fields” in this case. Depending on the setup different categories are available. If `None` default category is used (the first item in the Results drop down menu in AEDT). 

**plot_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The format of Data Visualization. Default is `Rectangular Plot`. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
The default is `None`. - For HFSS 3D Layout, options are `"Bondwires"`, `"Differential Pairs"`, `None`, `"Probes"`, `"RL"`, `"Sources"`, and `"Vias"`. - For Q2D or Q3D, specify the name of a reduced matrix. - For a far fields plot, specify the name of an infinite sphere. - For Maxwell 2D/3D Eddy Current solution types this can be provided as a dictionary where the key is the matrix name and value the reduced matrix. - For Circuit Design, this can provide the plots’ time range as a dictionary where the keys are `"time_start"` and `"time_stop"`. By default `"time_start"` is 0ps and the `"time_stop"` is 10ns. - For TDR analysis some dictionary options are “pulse_rise_time”,”step_time”, “time_windowing”,”maximum_time”,”use_pulse_in_tdr”,”differential_pairs”. The default values are as they appear manually in the UI. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the plot. The default is `None`. 

**polyline_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), optional, 
    
Number of points to create the report for plots on polylines on. 

**subdesign_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Specify a subdesign ID to export a Touchstone file of this subdesign. Valid for Circuit Only. The default value is `None`. 

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
     

`report_standard.Standard`
    
`True` when successful, `False` when failed.
References

```
>>> oModule.CreateReport

```
Copy to clipboard
Examples
HFSS Example >>> from ansys.aedt.core import Hfss >>> hfss = Hfss() >>> hfss.post.create_report(“dB(S(1,1))”) >>> variations = hfss.available_variations.nominal_values >>> variations[“Theta”] = [“All”] >>> variations[“Phi”] = [“All”] >>> variations[“Freq”] = [“30GHz”] >>> hfss.post.create_report( … expressions=”db(GainTotal)”, … setup_sweep_name=hfss.nominal_adaptive, … variations=variations, … primary_sweep_variable=”Phi”, … secondary_sweep_variable=”Theta”, … report_category=”Far Fields”, … plot_type=”3D Polar Plot”, … context=”3D”, … ) >>> hfss.post.create_report(“S(1,1)”, hfss.nominal_sweep, variations=variations, plot_type=”Smith Chart”) >>> hfss.desktop_class.release_desktop(False, False)
Maxwell 2D Example - Field report on a polyline >>> from ansys.aedt.core import Maxwell2d >>> m2d = Maxwell2d(version=”2026.1”) Setup model >>> circ = m2d.modeler.create_circle(origin=[0, 0, 0], radius=5, material=”copper”) >>> poly = m2d.modeler.create_polyline(points=[[8, 8, 0], [8, -10, 0]], name=”Poly1”) >>> m2d.assign_current(assignment=circ.name, amplitude=5) >>> region = m2d.modeler.create_region(pad_value=100) >>> m2d.assign_balloon(assignment=region.edges) >>> setup = m2d.create_setup() >>> m2d.analyze_setup(setup.name) Create a field report on the polyline >>> report = m2d.post.create_report( … expressions=”Mag_B”, … setup_sweep_name=m2d.nominal_adaptive, … plot_type=”Rectangular Plot”, … report_category=”Fields”, … context=poly.name, … primary_sweep_variable=”Distance”, … ) >>> m2d.release_desktop(False, False)
Circuit Netlist Example >>> from ansys.aedt.core import CircuitNetlist >>> from ansys.aedt.core.generic.aedt_constants import CircuitNetlistConstants >>> cir = CircuitNetlist(version=”2026.1”) To get the available report solution there are two options: >>> solutions = cir.post.available_report_solutions()[0] or >>> solutions = CircuitNetlistConstants.solution_types[“NexximLNA”][“name”] Get the available report categories >>> categories = cir.post.available_report_types(solution=solutions)[0] Get the available report quantities for a specific category and solution >>> quantities = cir.post.available_report_quantities(quantities_category=”Noise”, solution=solution) Create the report for each quantity >>> for quantity in quantities: … cir.post.create_report( … expressions=f”dB({quantity})”, … setup_sweep_name=”NexximLNA”, … plot_type=”Rectangular Plot”, … report_category=”Noise”, … domain=”Sweep”, … primary_sweep_variable=”Freq”, … ) >>> cir.desktop_class.release_desktop(False, False)
# create_report 

PostProcessor3D.create_report(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup_sweep_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _domain : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Sweep'_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _primary_sweep_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _secondary_sweep_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _report_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _plot_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Rectangular Plot'_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _subdesign_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _polyline_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1001_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _matplotlib : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _hide_legend : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 800_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 450_) → [Standard](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.standard.Standard.html#ansys.aedt.core.visualization.report.standard.Standard "ansys.aedt.core.visualization.report.standard.Standard") | [AMIEyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIEyeDiagram.html#ansys.aedt.core.visualization.report.eye.AMIEyeDiagram "ansys.aedt.core.visualization.report.eye.AMIEyeDiagram") | [AMIConturEyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram.html#ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram "ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram") | [EMIReceiver](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.emi.EMIReceiver.html#ansys.aedt.core.visualization.report.emi.EMIReceiver "ansys.aedt.core.visualization.report.emi.EMIReceiver") | [EyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.EyeDiagram.html#ansys.aedt.core.visualization.report.eye.EyeDiagram "ansys.aedt.core.visualization.report.eye.EyeDiagram") | CircuitNetlistReport | [Fields](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.Fields.html#ansys.aedt.core.visualization.report.field.Fields "ansys.aedt.core.visualization.report.field.Fields") | [FarField](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.FarField.html#ansys.aedt.core.visualization.report.field.FarField "ansys.aedt.core.visualization.report.field.FarField") | [NearField](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.NearField.html#ansys.aedt.core.visualization.report.field.NearField "ansys.aedt.core.visualization.report.field.NearField") | [Spectral](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.standard.Spectral.html#ansys.aedt.core.visualization.report.standard.Spectral "ansys.aedt.core.visualization.report.standard.Spectral") | [ReportPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a report in AEDT or in Matplotlib. It can be a 2D plot, 3D plot, polar plot, or a data table. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more formulas to add to the report. Example is value = `"dB(S(1,1))"`. 

**setup_sweep_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Setup name with the sweep. The default is `None`, in which case the first setup and sweep is selected. For Circuit Netlist designs only, specify the solution name as listed in `ansys.aedt.core.generic.aedt_constants.CircuitNetlistConstants`. 

**domain**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot Domain. Options are “Sweep”, “Time”, “DCIR”. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all families including the primary sweep. The default is `{"Freq": ["All"]}`. 

**primary_sweep_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the primary sweep. The default is `"Freq"`. 

**secondary_sweep_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the secondary sweep variable in 3D Plots. 

**report_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Category of the Report to be created. If None default data Report is used. The Report Category can be one of the types available for creating a report depend on the simulation setup. For example for a Far Field Plot in HFSS the UI shows the report category as “Create Far Fields Report”. The report category is “Far Fields” in this case. Depending on the setup different categories are available. If `None` default category is used (the first item in the Results drop down menu in AEDT). 

**plot_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The format of Data Visualization. Default is `Rectangular Plot`. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
The default is `None`. - For HFSS 3D Layout, options are `"Bondwires"`, `"Differential Pairs"`, `None`, `"Probes"`, `"RL"`, `"Sources"`, and `"Vias"`. - For Q2D or Q3D, specify the name of a reduced matrix. - For a far fields plot, specify the name of an infinite sphere. - For Maxwell 2D/3D Eddy Current solution types this can be provided as a dictionary where the key is the matrix name and value the reduced matrix. - For Circuit Design, this can provide the plots’ time range as a dictionary where the keys are `"time_start"` and `"time_stop"`. By default `"time_start"` is 0ps and the `"time_stop"` is 10ns. - For TDR analysis some dictionary options are “pulse_rise_time”,”step_time”, “time_windowing”,”maximum_time”,”use_pulse_in_tdr”,”differential_pairs”. The default values are as they appear manually in the UI. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the plot. The default is `None`. 

**polyline_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), optional, 
    
Number of points to create the report for plots on polylines on. 

**subdesign_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Specify a subdesign ID to export a Touchstone file of this subdesign. Valid for Circuit Only. The default value is `None`. 

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
     

`report_standard.Standard`
    
`True` when successful, `False` when failed.
References

```
>>> oModule.CreateReport

```
Copy to clipboard
Examples
HFSS Example >>> from ansys.aedt.core import Hfss >>> hfss = Hfss() >>> hfss.post.create_report(“dB(S(1,1))”) >>> variations = hfss.available_variations.nominal_values >>> variations[“Theta”] = [“All”] >>> variations[“Phi”] = [“All”] >>> variations[“Freq”] = [“30GHz”] >>> hfss.post.create_report( … expressions=”db(GainTotal)”, … setup_sweep_name=hfss.nominal_adaptive, … variations=variations, … primary_sweep_variable=”Phi”, … secondary_sweep_variable=”Theta”, … report_category=”Far Fields”, … plot_type=”3D Polar Plot”, … context=”3D”, … ) >>> hfss.post.create_report(“S(1,1)”, hfss.nominal_sweep, variations=variations, plot_type=”Smith Chart”) >>> hfss.desktop_class.release_desktop(False, False)
Maxwell 2D Example - Field report on a polyline >>> from ansys.aedt.core import Maxwell2d >>> m2d = Maxwell2d(version=”2026.1”) Setup model >>> circ = m2d.modeler.create_circle(origin=[0, 0, 0], radius=5, material=”copper”) >>> poly = m2d.modeler.create_polyline(points=[[8, 8, 0], [8, -10, 0]], name=”Poly1”) >>> m2d.assign_current(assignment=circ.name, amplitude=5) >>> region = m2d.modeler.create_region(pad_value=100) >>> m2d.assign_balloon(assignment=region.edges) >>> setup = m2d.create_setup() >>> m2d.analyze_setup(setup.name) Create a field report on the polyline >>> report = m2d.post.create_report( … expressions=”Mag_B”, … setup_sweep_name=m2d.nominal_adaptive, … plot_type=”Rectangular Plot”, … report_category=”Fields”, … context=poly.name, … primary_sweep_variable=”Distance”, … ) >>> m2d.release_desktop(False, False)
Circuit Netlist Example >>> from ansys.aedt.core import CircuitNetlist >>> from ansys.aedt.core.generic.aedt_constants import CircuitNetlistConstants >>> cir = CircuitNetlist(version=”2026.1”) To get the available report solution there are two options: >>> solutions = cir.post.available_report_solutions()[0] or >>> solutions = CircuitNetlistConstants.solution_types[“NexximLNA”][“name”] Get the available report categories >>> categories = cir.post.available_report_types(solution=solutions)[0] Get the available report quantities for a specific category and solution >>> quantities = cir.post.available_report_quantities(quantities_category=”Noise”, solution=solution) Create the report for each quantity >>> for quantity in quantities: … cir.post.create_report( … expressions=f”dB({quantity})”, … setup_sweep_name=”NexximLNA”, … plot_type=”Rectangular Plot”, … report_category=”Noise”, … domain=”Sweep”, … primary_sweep_variable=”Freq”, … ) >>> cir.desktop_class.release_desktop(False, False)
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_common_3d.PostProcessor3D.create_report.rst.txt)

# create_report 

PostProcessor3D.create_report(_expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _setup_sweep_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _domain : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Sweep'_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _primary_sweep_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _secondary_sweep_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _report_category : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _plot_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Rectangular Plot'_, _context : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _subdesign_id : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _polyline_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1001_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _matplotlib : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _hide_legend : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 800_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 450_) → [Standard](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.standard.Standard.html#ansys.aedt.core.visualization.report.standard.Standard "ansys.aedt.core.visualization.report.standard.Standard") | [AMIEyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIEyeDiagram.html#ansys.aedt.core.visualization.report.eye.AMIEyeDiagram "ansys.aedt.core.visualization.report.eye.AMIEyeDiagram") | [AMIConturEyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram.html#ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram "ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram") | [EMIReceiver](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.emi.EMIReceiver.html#ansys.aedt.core.visualization.report.emi.EMIReceiver "ansys.aedt.core.visualization.report.emi.EMIReceiver") | [EyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.EyeDiagram.html#ansys.aedt.core.visualization.report.eye.EyeDiagram "ansys.aedt.core.visualization.report.eye.EyeDiagram") | CircuitNetlistReport | [Fields](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.Fields.html#ansys.aedt.core.visualization.report.field.Fields "ansys.aedt.core.visualization.report.field.Fields") | [FarField](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.FarField.html#ansys.aedt.core.visualization.report.field.FarField "ansys.aedt.core.visualization.report.field.FarField") | [NearField](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.NearField.html#ansys.aedt.core.visualization.report.field.NearField "ansys.aedt.core.visualization.report.field.NearField") | [Spectral](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.standard.Spectral.html#ansys.aedt.core.visualization.report.standard.Spectral "ansys.aedt.core.visualization.report.standard.Spectral") | [ReportPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a report in AEDT or in Matplotlib. It can be a 2D plot, 3D plot, polar plot, or a data table. 

Parameters: 
     

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more formulas to add to the report. Example is value = `"dB(S(1,1))"`. 

**setup_sweep_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Setup name with the sweep. The default is `None`, in which case the first setup and sweep is selected. For Circuit Netlist designs only, specify the solution name as listed in `ansys.aedt.core.generic.aedt_constants.CircuitNetlistConstants`. 

**domain**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Plot Domain. Options are “Sweep”, “Time”, “DCIR”. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all families including the primary sweep. The default is `{"Freq": ["All"]}`. 

**primary_sweep_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the primary sweep. The default is `"Freq"`. 

**secondary_sweep_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the secondary sweep variable in 3D Plots. 

**report_category**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Category of the Report to be created. If None default data Report is used. The Report Category can be one of the types available for creating a report depend on the simulation setup. For example for a Far Field Plot in HFSS the UI shows the report category as “Create Far Fields Report”. The report category is “Far Fields” in this case. Depending on the setup different categories are available. If `None` default category is used (the first item in the Results drop down menu in AEDT). 

**plot_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The format of Data Visualization. Default is `Rectangular Plot`. 

**context**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
The default is `None`. - For HFSS 3D Layout, options are `"Bondwires"`, `"Differential Pairs"`, `None`, `"Probes"`, `"RL"`, `"Sources"`, and `"Vias"`. - For Q2D or Q3D, specify the name of a reduced matrix. - For a far fields plot, specify the name of an infinite sphere. - For Maxwell 2D/3D Eddy Current solution types this can be provided as a dictionary where the key is the matrix name and value the reduced matrix. - For Circuit Design, this can provide the plots’ time range as a dictionary where the keys are `"time_start"` and `"time_stop"`. By default `"time_start"` is 0ps and the `"time_stop"` is 10ns. - For TDR analysis some dictionary options are “pulse_rise_time”,”step_time”, “time_windowing”,”maximum_time”,”use_pulse_in_tdr”,”differential_pairs”. The default values are as they appear manually in the UI. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the plot. The default is `None`. 

**polyline_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), optional, 
    
Number of points to create the report for plots on polylines on. 

**subdesign_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Specify a subdesign ID to export a Touchstone file of this subdesign. Valid for Circuit Only. The default value is `None`. 

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
     

`report_standard.Standard`
    
`True` when successful, `False` when failed.
References

```
>>> oModule.CreateReport

```
Copy to clipboard
Examples
HFSS Example >>> from ansys.aedt.core import Hfss >>> hfss = Hfss() >>> hfss.post.create_report(“dB(S(1,1))”) >>> variations = hfss.available_variations.nominal_values >>> variations[“Theta”] = [“All”] >>> variations[“Phi”] = [“All”] >>> variations[“Freq”] = [“30GHz”] >>> hfss.post.create_report( … expressions=”db(GainTotal)”, … setup_sweep_name=hfss.nominal_adaptive, … variations=variations, … primary_sweep_variable=”Phi”, … secondary_sweep_variable=”Theta”, … report_category=”Far Fields”, … plot_type=”3D Polar Plot”, … context=”3D”, … ) >>> hfss.post.create_report(“S(1,1)”, hfss.nominal_sweep, variations=variations, plot_type=”Smith Chart”) >>> hfss.desktop_class.release_desktop(False, False)
Maxwell 2D Example - Field report on a polyline >>> from ansys.aedt.core import Maxwell2d >>> m2d = Maxwell2d(version=”2026.1”) Setup model >>> circ = m2d.modeler.create_circle(origin=[0, 0, 0], radius=5, material=”copper”) >>> poly = m2d.modeler.create_polyline(points=[[8, 8, 0], [8, -10, 0]], name=”Poly1”) >>> m2d.assign_current(assignment=circ.name, amplitude=5) >>> region = m2d.modeler.create_region(pad_value=100) >>> m2d.assign_balloon(assignment=region.edges) >>> setup = m2d.create_setup() >>> m2d.analyze_setup(setup.name) Create a field report on the polyline >>> report = m2d.post.create_report( … expressions=”Mag_B”, … setup_sweep_name=m2d.nominal_adaptive, … plot_type=”Rectangular Plot”, … report_category=”Fields”, … context=poly.name, … primary_sweep_variable=”Distance”, … ) >>> m2d.release_desktop(False, False)
Circuit Netlist Example >>> from ansys.aedt.core import CircuitNetlist >>> from ansys.aedt.core.generic.aedt_constants import CircuitNetlistConstants >>> cir = CircuitNetlist(version=”2026.1”) To get the available report solution there are two options: >>> solutions = cir.post.available_report_solutions()[0] or >>> solutions = CircuitNetlistConstants.solution_types[“NexximLNA”][“name”] Get the available report categories >>> categories = cir.post.available_report_types(solution=solutions)[0] Get the available report quantities for a specific category and solution >>> quantities = cir.post.available_report_quantities(quantities_category=”Noise”, solution=solution) Create the report for each quantity >>> for quantity in quantities: … cir.post.create_report( … expressions=f”dB({quantity})”, … setup_sweep_name=”NexximLNA”, … plot_type=”Rectangular Plot”, … report_category=”Noise”, … domain=”Sweep”, … primary_sweep_variable=”Freq”, … ) >>> cir.desktop_class.release_desktop(False, False)