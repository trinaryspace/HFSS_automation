---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# FfdSolutionDataExporter 

class ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter(_app_ , _sphere_name_ , _setup_name_ , _frequencies_ , _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _export_touchstone : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _set_phase_center_per_port : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Class to enable export of embedded element pattern data from HFSS.
An instance of this class is returned from the `ansys.aedt.core.Hfss.get_antenna_data()` method. This method allows creation of the embedded element pattern files for an antenna that have been solved in HFSS. The `metadata_file` properties can then be passed as arguments to instantiate an instance of the [`ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData.html#ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData "ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData") class for subsequent analysis and postprocessing of the array data.
Note that this class is derived from the `FfdSolutionData` class and can be used directly for far-field postprocessing and array analysis, but it remains a property of the `ansys.aedt.core.Hfss` application. 

Parameters: 
     

**app**`ansys.aedt.core.Hfss` 
    
HFSS application instance. 

**sphere_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Infinite sphere to use. 

**setup_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. Make sure to build a setup string in the form of `"SetupName : SetupSweep"`. 

**frequencies**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Frequency list to export. Specify either a list of strings with units or a list of floats in Hertz units. For example, `["9GHz", 9e9]`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all families including the primary sweep. The default value is `None`. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to overwrite the existing far field solution data. The default is `True`. 

**export_touchstone**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export touchstone file. The default is `False`. Working from 2024 R1. 

**set_phase_center_per_port**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Set phase center per port location. The default is `True`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss(version="2026.1", design="Antenna")
>>> setup_name = "Setup1 : LastAdaptive"
>>> frequencies = [77e9]
>>> sphere = "3D"
>>> data = app.get_antenna_data(frequencies, setup_name, sphere)
>>> data.plot_3d(quantity_format="dB10")

```
Copy to clipboard
Methods  
| [`FfdSolutionDataExporter.export_farfield`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.export_farfield.html#ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.export_farfield "ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.export_farfield")()  | Export far field solution data of each element.  |  
| --- | --- |  
Attributes  
| [`FfdSolutionDataExporter.farfield_data`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.farfield_data.html#ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.farfield_data "ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.farfield_data")  | Farfield data.  |  
| --- | --- |  
| [`FfdSolutionDataExporter.metadata_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.metadata_file.html#ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.metadata_file "ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.metadata_file")  | Metadata file.  |  
| [`FfdSolutionDataExporter.model_info`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.model_info.html#ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.model_info "ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.model_info")  | List of models.  |  
| [`FfdSolutionDataExporter.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.public_dir.html#ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.public_dir "ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.public_dir")  | Shortcut for dir(self).  |  
# FfdSolutionDataExporter 

class ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter(_app_ , _sphere_name_ , _setup_name_ , _frequencies_ , _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _export_touchstone : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _set_phase_center_per_port : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Class to enable export of embedded element pattern data from HFSS.
An instance of this class is returned from the `ansys.aedt.core.Hfss.get_antenna_data()` method. This method allows creation of the embedded element pattern files for an antenna that have been solved in HFSS. The `metadata_file` properties can then be passed as arguments to instantiate an instance of the [`ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData.html#ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData "ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData") class for subsequent analysis and postprocessing of the array data.
Note that this class is derived from the `FfdSolutionData` class and can be used directly for far-field postprocessing and array analysis, but it remains a property of the `ansys.aedt.core.Hfss` application. 

Parameters: 
     

**app**`ansys.aedt.core.Hfss` 
    
HFSS application instance. 

**sphere_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Infinite sphere to use. 

**setup_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. Make sure to build a setup string in the form of `"SetupName : SetupSweep"`. 

**frequencies**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Frequency list to export. Specify either a list of strings with units or a list of floats in Hertz units. For example, `["9GHz", 9e9]`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all families including the primary sweep. The default value is `None`. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to overwrite the existing far field solution data. The default is `True`. 

**export_touchstone**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export touchstone file. The default is `False`. Working from 2024 R1. 

**set_phase_center_per_port**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Set phase center per port location. The default is `True`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss(version="2026.1", design="Antenna")
>>> setup_name = "Setup1 : LastAdaptive"
>>> frequencies = [77e9]
>>> sphere = "3D"
>>> data = app.get_antenna_data(frequencies, setup_name, sphere)
>>> data.plot_3d(quantity_format="dB10")

```
Copy to clipboard
Methods  
| [`FfdSolutionDataExporter.export_farfield`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.export_farfield.html#ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.export_farfield "ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.export_farfield")()  | Export far field solution data of each element.  |  
| --- | --- |  
Attributes  
| [`FfdSolutionDataExporter.farfield_data`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.farfield_data.html#ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.farfield_data "ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.farfield_data")  | Farfield data.  |  
| --- | --- |  
| [`FfdSolutionDataExporter.metadata_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.metadata_file.html#ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.metadata_file "ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.metadata_file")  | Metadata file.  |  
| [`FfdSolutionDataExporter.model_info`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.model_info.html#ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.model_info "ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.model_info")  | List of models.  |  
| [`FfdSolutionDataExporter.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.public_dir.html#ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.public_dir "ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.rst.txt)

# FfdSolutionDataExporter 

class ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter(_app_ , _sphere_name_ , _setup_name_ , _frequencies_ , _variations : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _overwrite : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _export_touchstone : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _set_phase_center_per_port : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) 
    
Class to enable export of embedded element pattern data from HFSS.
An instance of this class is returned from the `ansys.aedt.core.Hfss.get_antenna_data()` method. This method allows creation of the embedded element pattern files for an antenna that have been solved in HFSS. The `metadata_file` properties can then be passed as arguments to instantiate an instance of the [`ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData.html#ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData "ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData") class for subsequent analysis and postprocessing of the array data.
Note that this class is derived from the `FfdSolutionData` class and can be used directly for far-field postprocessing and array analysis, but it remains a property of the `ansys.aedt.core.Hfss` application. 

Parameters: 
     

**app**`ansys.aedt.core.Hfss` 
    
HFSS application instance. 

**sphere_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Infinite sphere to use. 

**setup_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. Make sure to build a setup string in the form of `"SetupName : SetupSweep"`. 

**frequencies**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Frequency list to export. Specify either a list of strings with units or a list of floats in Hertz units. For example, `["9GHz", 9e9]`. 

**variations**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), `optional` 
    
Dictionary of all families including the primary sweep. The default value is `None`. 

**overwrite**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to overwrite the existing far field solution data. The default is `True`. 

**export_touchstone**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export touchstone file. The default is `False`. Working from 2024 R1. 

**set_phase_center_per_port**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Set phase center per port location. The default is `True`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss(version="2026.1", design="Antenna")
>>> setup_name = "Setup1 : LastAdaptive"
>>> frequencies = [77e9]
>>> sphere = "3D"
>>> data = app.get_antenna_data(frequencies, setup_name, sphere)
>>> data.plot_3d(quantity_format="dB10")

```
Copy to clipboard
Methods  
| [`FfdSolutionDataExporter.export_farfield`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.export_farfield.html#ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.export_farfield "ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.export_farfield")()  | Export far field solution data of each element.  |  
| --- | --- |  
Attributes  
| [`FfdSolutionDataExporter.farfield_data`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.farfield_data.html#ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.farfield_data "ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.farfield_data")  | Farfield data.  |  
| --- | --- |  
| [`FfdSolutionDataExporter.metadata_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.metadata_file.html#ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.metadata_file "ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.metadata_file")  | Metadata file.  |  
| [`FfdSolutionDataExporter.model_info`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.model_info.html#ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.model_info "ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.model_info")  | List of models.  |  
| [`FfdSolutionDataExporter.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.public_dir.html#ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.public_dir "ansys.aedt.core.visualization.post.farfield_exporter.FfdSolutionDataExporter.public_dir")  | Shortcut for dir(self).  |