---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# MonostaticRCSExporter 

class ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter(_app : [Hfss](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss")_, _setup_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _frequencies : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [Any](https://docs.python.org/3.11/library/typing.html#typing.Any "\(in Python v3.11\)")] | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Class to enable export of radar cross-section (RCS) data from HFSS.
An instance of this class is returned from the `ansys.aedt.core.Hfss.get_monostatic_rcs()` method. This class creates a `metadata_file` that can be passed as argument to instantiate an instance of the `ansys.aedt.toolkits.radar_explorer.rcs_visualization.MonostaticRCSData` class for subsequent analysis and postprocessing.
Note
This class requires the Radar explorer toolkit for RCS data analysis. Install it with: `pip install ansys-aedt-toolkits-radar-explorer` 

Parameters: 
     

**app**`ansys.aedt.core.Hfss` 
    
HFSS application instance. 

**setup_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. Make sure to build a setup string in the form of `"SetupName : SetupSweep"`. The default is `None`, in which case only the geometry is exported. 

**frequencies**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Frequency list to export. Specify either a list of strings with units or a list of floats in Hertz units. For example, `["9GHz", 9e9]`. The default is `None`, in which case only the geometry is exported. 

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Monostatic expression name. The default value is `"ComplexMonostaticRCSTheta"`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all families including the primary sweep. The default value is `None`. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to overwrite the existing far field solution data. The default is `True`.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Hfss(version="2026.1", design="Antenna")
>>> setup_name = "Setup1 : LastAdaptive"
>>> frequencies = [77e9]
>>> sphere = "3D"
>>> data = app.get_monostatic_rcs(frequencies, setup_name, sphere)
>>> data.plot_3d(quantity_format="dB10")

```
Copy to clipboard
Methods  
| [`MonostaticRCSExporter.export_rcs`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.export_rcs.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.export_rcs "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.export_rcs")([name, ...])  | Export RCS solution data.  |  
| --- | --- |  
| [`MonostaticRCSExporter.get_monostatic_rcs`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.get_monostatic_rcs.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.get_monostatic_rcs "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.get_monostatic_rcs")()  | Get RCS solution data.  |  
Attributes  
| [`MonostaticRCSExporter.column_name`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.column_name.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.column_name "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.column_name")  | Column name.  |  
| --- | --- |  
| [`MonostaticRCSExporter.metadata_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.metadata_file.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.metadata_file "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.metadata_file")  | Metadata file.  |  
| [`MonostaticRCSExporter.model_info`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.model_info.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.model_info "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.model_info")  | List of models.  |  
| [`MonostaticRCSExporter.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.public_dir.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.public_dir "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.public_dir")  | Shortcut for dir(self).  |  
# MonostaticRCSExporter 

class ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter(_app : [Hfss](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss")_, _setup_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _frequencies : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [Any](https://docs.python.org/3.11/library/typing.html#typing.Any "\(in Python v3.11\)")] | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Class to enable export of radar cross-section (RCS) data from HFSS.
An instance of this class is returned from the `ansys.aedt.core.Hfss.get_monostatic_rcs()` method. This class creates a `metadata_file` that can be passed as argument to instantiate an instance of the `ansys.aedt.toolkits.radar_explorer.rcs_visualization.MonostaticRCSData` class for subsequent analysis and postprocessing.
Note
This class requires the Radar explorer toolkit for RCS data analysis. Install it with: `pip install ansys-aedt-toolkits-radar-explorer` 

Parameters: 
     

**app**`ansys.aedt.core.Hfss` 
    
HFSS application instance. 

**setup_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. Make sure to build a setup string in the form of `"SetupName : SetupSweep"`. The default is `None`, in which case only the geometry is exported. 

**frequencies**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Frequency list to export. Specify either a list of strings with units or a list of floats in Hertz units. For example, `["9GHz", 9e9]`. The default is `None`, in which case only the geometry is exported. 

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Monostatic expression name. The default value is `"ComplexMonostaticRCSTheta"`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all families including the primary sweep. The default value is `None`. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to overwrite the existing far field solution data. The default is `True`.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Hfss(version="2026.1", design="Antenna")
>>> setup_name = "Setup1 : LastAdaptive"
>>> frequencies = [77e9]
>>> sphere = "3D"
>>> data = app.get_monostatic_rcs(frequencies, setup_name, sphere)
>>> data.plot_3d(quantity_format="dB10")

```
Copy to clipboard
Methods  
| [`MonostaticRCSExporter.export_rcs`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.export_rcs.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.export_rcs "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.export_rcs")([name, ...])  | Export RCS solution data.  |  
| --- | --- |  
| [`MonostaticRCSExporter.get_monostatic_rcs`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.get_monostatic_rcs.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.get_monostatic_rcs "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.get_monostatic_rcs")()  | Get RCS solution data.  |  
Attributes  
| [`MonostaticRCSExporter.column_name`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.column_name.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.column_name "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.column_name")  | Column name.  |  
| --- | --- |  
| [`MonostaticRCSExporter.metadata_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.metadata_file.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.metadata_file "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.metadata_file")  | Metadata file.  |  
| [`MonostaticRCSExporter.model_info`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.model_info.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.model_info "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.model_info")  | List of models.  |  
| [`MonostaticRCSExporter.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.public_dir.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.public_dir "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.rst.txt)

# MonostaticRCSExporter 

class ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter(_app : [Hfss](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss")_, _setup_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _frequencies : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [Any](https://docs.python.org/3.11/library/typing.html#typing.Any "\(in Python v3.11\)")] | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Class to enable export of radar cross-section (RCS) data from HFSS.
An instance of this class is returned from the `ansys.aedt.core.Hfss.get_monostatic_rcs()` method. This class creates a `metadata_file` that can be passed as argument to instantiate an instance of the `ansys.aedt.toolkits.radar_explorer.rcs_visualization.MonostaticRCSData` class for subsequent analysis and postprocessing.
Note
This class requires the Radar explorer toolkit for RCS data analysis. Install it with: `pip install ansys-aedt-toolkits-radar-explorer` 

Parameters: 
     

**app**`ansys.aedt.core.Hfss` 
    
HFSS application instance. 

**setup_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. Make sure to build a setup string in the form of `"SetupName : SetupSweep"`. The default is `None`, in which case only the geometry is exported. 

**frequencies**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Frequency list to export. Specify either a list of strings with units or a list of floats in Hertz units. For example, `["9GHz", 9e9]`. The default is `None`, in which case only the geometry is exported. 

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Monostatic expression name. The default value is `"ComplexMonostaticRCSTheta"`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all families including the primary sweep. The default value is `None`. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to overwrite the existing far field solution data. The default is `True`.
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Hfss(version="2026.1", design="Antenna")
>>> setup_name = "Setup1 : LastAdaptive"
>>> frequencies = [77e9]
>>> sphere = "3D"
>>> data = app.get_monostatic_rcs(frequencies, setup_name, sphere)
>>> data.plot_3d(quantity_format="dB10")

```
Copy to clipboard
Methods  
| [`MonostaticRCSExporter.export_rcs`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.export_rcs.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.export_rcs "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.export_rcs")([name, ...])  | Export RCS solution data.  |  
| --- | --- |  
| [`MonostaticRCSExporter.get_monostatic_rcs`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.get_monostatic_rcs.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.get_monostatic_rcs "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.get_monostatic_rcs")()  | Get RCS solution data.  |  
Attributes  
| [`MonostaticRCSExporter.column_name`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.column_name.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.column_name "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.column_name")  | Column name.  |  
| --- | --- |  
| [`MonostaticRCSExporter.metadata_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.metadata_file.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.metadata_file "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.metadata_file")  | Metadata file.  |  
| [`MonostaticRCSExporter.model_info`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.model_info.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.model_info "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.model_info")  | List of models.  |  
| [`MonostaticRCSExporter.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.public_dir.html#ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.public_dir "ansys.aedt.core.visualization.post.rcs_exporter.MonostaticRCSExporter.public_dir")  | Shortcut for dir(self).  |