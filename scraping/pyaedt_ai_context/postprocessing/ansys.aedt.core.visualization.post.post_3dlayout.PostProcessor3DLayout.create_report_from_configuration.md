---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_3dlayout.PostProcessor3DLayout.create_report_from_configuration.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# create_report_from_configuration 

PostProcessor3DLayout.create_report_from_configuration(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _report_settings : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _solution_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _matplotlib : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _hide_legend : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 800_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 450_) → [Standard](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.standard.Standard.html#ansys.aedt.core.visualization.report.standard.Standard "ansys.aedt.core.visualization.report.standard.Standard") | [AMIEyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIEyeDiagram.html#ansys.aedt.core.visualization.report.eye.AMIEyeDiagram "ansys.aedt.core.visualization.report.eye.AMIEyeDiagram") | [AMIConturEyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram.html#ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram "ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram") | [EMIReceiver](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.emi.EMIReceiver.html#ansys.aedt.core.visualization.report.emi.EMIReceiver "ansys.aedt.core.visualization.report.emi.EMIReceiver") | [EyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.EyeDiagram.html#ansys.aedt.core.visualization.report.eye.EyeDiagram "ansys.aedt.core.visualization.report.eye.EyeDiagram") | CircuitNetlistReport | [Fields](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.Fields.html#ansys.aedt.core.visualization.report.field.Fields "ansys.aedt.core.visualization.report.field.Fields") | [FarField](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.FarField.html#ansys.aedt.core.visualization.report.field.FarField "ansys.aedt.core.visualization.report.field.FarField") | [NearField](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.NearField.html#ansys.aedt.core.visualization.report.field.NearField "ansys.aedt.core.visualization.report.field.NearField") | [Spectral](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.standard.Spectral.html#ansys.aedt.core.visualization.report.standard.Spectral "ansys.aedt.core.visualization.report.standard.Spectral") | [ReportPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a report based on a JSON file, TOML file, RPT file, or dictionary of properties. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path to the JSON, TOML, or RPT file containing report settings. 

**report_settings**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary containing report settings. 

**solution_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Setup name to use. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report name. The default is `None`, in which case the default name is used. 

**matplotlib**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use AEDT or ReportPlotter to generate the plot. Eye diagrams are not supported. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot when using ReportPlotter. The default is `True`. If matplotlib is `False`, this parameter is ignored. 

**hide_legend**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to hide the legend when using AEDT reporter. The default is `False`. 

**snapshot_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to image file if a snapshot is needed. The default is `None`. 

**width**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Image width. Default is `800` which takes Desktop size or 800 pixel. 

**height**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Image height. Default is `450` which takes Desktop size or 450 pixel. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.Standard` or [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Report object if succeeded.
Examples
Create report from JSON file. >>> from ansys.aedt.core import Hfss >>> hfss = Hfss() >>> hfss.post.create_report_from_configuration( … r”C:tempmy_report.json”, solution_name=”Setup1 : LastAdpative” … )
Create report from RPT file. >>> from ansys.aedt.core import Hfss >>> hfss = Hfss() >>> hfss.post.create_report_from_configuration(r”C:tempmy_report.rpt”)
Create report from dictionary. >>> from ansys.aedt.core import Hfss >>> from ansys.aedt.core.generic.file_utils import read_json >>> hfss = Hfss() >>> dict_vals = read_json(“Report_Simple.json”) >>> hfss.post.create_report_from_configuration(report_settings=dict_vals)
# create_report_from_configuration 

PostProcessor3DLayout.create_report_from_configuration(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _report_settings : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _solution_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _matplotlib : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _hide_legend : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 800_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 450_) → [Standard](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.standard.Standard.html#ansys.aedt.core.visualization.report.standard.Standard "ansys.aedt.core.visualization.report.standard.Standard") | [AMIEyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIEyeDiagram.html#ansys.aedt.core.visualization.report.eye.AMIEyeDiagram "ansys.aedt.core.visualization.report.eye.AMIEyeDiagram") | [AMIConturEyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram.html#ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram "ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram") | [EMIReceiver](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.emi.EMIReceiver.html#ansys.aedt.core.visualization.report.emi.EMIReceiver "ansys.aedt.core.visualization.report.emi.EMIReceiver") | [EyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.EyeDiagram.html#ansys.aedt.core.visualization.report.eye.EyeDiagram "ansys.aedt.core.visualization.report.eye.EyeDiagram") | CircuitNetlistReport | [Fields](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.Fields.html#ansys.aedt.core.visualization.report.field.Fields "ansys.aedt.core.visualization.report.field.Fields") | [FarField](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.FarField.html#ansys.aedt.core.visualization.report.field.FarField "ansys.aedt.core.visualization.report.field.FarField") | [NearField](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.NearField.html#ansys.aedt.core.visualization.report.field.NearField "ansys.aedt.core.visualization.report.field.NearField") | [Spectral](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.standard.Spectral.html#ansys.aedt.core.visualization.report.standard.Spectral "ansys.aedt.core.visualization.report.standard.Spectral") | [ReportPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a report based on a JSON file, TOML file, RPT file, or dictionary of properties. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path to the JSON, TOML, or RPT file containing report settings. 

**report_settings**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary containing report settings. 

**solution_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Setup name to use. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report name. The default is `None`, in which case the default name is used. 

**matplotlib**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use AEDT or ReportPlotter to generate the plot. Eye diagrams are not supported. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot when using ReportPlotter. The default is `True`. If matplotlib is `False`, this parameter is ignored. 

**hide_legend**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to hide the legend when using AEDT reporter. The default is `False`. 

**snapshot_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to image file if a snapshot is needed. The default is `None`. 

**width**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Image width. Default is `800` which takes Desktop size or 800 pixel. 

**height**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Image height. Default is `450` which takes Desktop size or 450 pixel. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.Standard` or [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Report object if succeeded.
Examples
Create report from JSON file. >>> from ansys.aedt.core import Hfss >>> hfss = Hfss() >>> hfss.post.create_report_from_configuration( … r”C:tempmy_report.json”, solution_name=”Setup1 : LastAdpative” … )
Create report from RPT file. >>> from ansys.aedt.core import Hfss >>> hfss = Hfss() >>> hfss.post.create_report_from_configuration(r”C:tempmy_report.rpt”)
Create report from dictionary. >>> from ansys.aedt.core import Hfss >>> from ansys.aedt.core.generic.file_utils import read_json >>> hfss = Hfss() >>> dict_vals = read_json(“Report_Simple.json”) >>> hfss.post.create_report_from_configuration(report_settings=dict_vals)
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_3dlayout.PostProcessor3DLayout.create_report_from_configuration.rst.txt)

# create_report_from_configuration 

PostProcessor3DLayout.create_report_from_configuration(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _report_settings : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_, _solution_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _matplotlib : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _hide_legend : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _snapshot_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 800_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 450_) → [Standard](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.standard.Standard.html#ansys.aedt.core.visualization.report.standard.Standard "ansys.aedt.core.visualization.report.standard.Standard") | [AMIEyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIEyeDiagram.html#ansys.aedt.core.visualization.report.eye.AMIEyeDiagram "ansys.aedt.core.visualization.report.eye.AMIEyeDiagram") | [AMIConturEyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram.html#ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram "ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram") | [EMIReceiver](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.emi.EMIReceiver.html#ansys.aedt.core.visualization.report.emi.EMIReceiver "ansys.aedt.core.visualization.report.emi.EMIReceiver") | [EyeDiagram](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.EyeDiagram.html#ansys.aedt.core.visualization.report.eye.EyeDiagram "ansys.aedt.core.visualization.report.eye.EyeDiagram") | CircuitNetlistReport | [Fields](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.Fields.html#ansys.aedt.core.visualization.report.field.Fields "ansys.aedt.core.visualization.report.field.Fields") | [FarField](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.FarField.html#ansys.aedt.core.visualization.report.field.FarField "ansys.aedt.core.visualization.report.field.FarField") | [NearField](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.field.NearField.html#ansys.aedt.core.visualization.report.field.NearField "ansys.aedt.core.visualization.report.field.NearField") | [Spectral](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.standard.Spectral.html#ansys.aedt.core.visualization.report.standard.Spectral "ansys.aedt.core.visualization.report.standard.Spectral") | [ReportPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter.html#ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter "ansys.aedt.core.visualization.plot.matplotlib.ReportPlotter") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a report based on a JSON file, TOML file, RPT file, or dictionary of properties. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path to the JSON, TOML, or RPT file containing report settings. 

**report_settings**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary containing report settings. 

**solution_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Setup name to use. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report name. The default is `None`, in which case the default name is used. 

**matplotlib**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use AEDT or ReportPlotter to generate the plot. Eye diagrams are not supported. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot when using ReportPlotter. The default is `True`. If matplotlib is `False`, this parameter is ignored. 

**hide_legend**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to hide the legend when using AEDT reporter. The default is `False`. 

**snapshot_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path to image file if a snapshot is needed. The default is `None`. 

**width**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Image width. Default is `800` which takes Desktop size or 800 pixel. 

**height**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Image height. Default is `450` which takes Desktop size or 450 pixel. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.Standard` or [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Report object if succeeded.
Examples
Create report from JSON file. >>> from ansys.aedt.core import Hfss >>> hfss = Hfss() >>> hfss.post.create_report_from_configuration( … r”C:tempmy_report.json”, solution_name=”Setup1 : LastAdpative” … )
Create report from RPT file. >>> from ansys.aedt.core import Hfss >>> hfss = Hfss() >>> hfss.post.create_report_from_configuration(r”C:tempmy_report.rpt”)
Create report from dictionary. >>> from ansys.aedt.core import Hfss >>> from ansys.aedt.core.generic.file_utils import read_json >>> hfss = Hfss() >>> dict_vals = read_json(“Report_Simple.json”) >>> hfss.post.create_report_from_configuration(report_settings=dict_vals)