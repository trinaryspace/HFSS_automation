---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# FolderPlotSettings 

class ansys.aedt.core.visualization.post.field_data.FolderPlotSettings(_postprocessor_ , _folder_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _arrow_settings : [ArrowSettings](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ArrowSettings.html#ansys.aedt.core.visualization.post.field_data.ArrowSettings "ansys.aedt.core.visualization.post.field_data.ArrowSettings") = None_, _marker_settings : [MarkerSettings](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.MarkerSettings.html#ansys.aedt.core.visualization.post.field_data.MarkerSettings "ansys.aedt.core.visualization.post.field_data.MarkerSettings") = None_, _scale_settings : [Scale3DSettings](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.Scale3DSettings.html#ansys.aedt.core.visualization.post.field_data.Scale3DSettings "ansys.aedt.core.visualization.post.field_data.Scale3DSettings") = None_, _color_map_settings : [ColorMapSettings](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ColorMapSettings.html#ansys.aedt.core.visualization.post.field_data.ColorMapSettings "ansys.aedt.core.visualization.post.field_data.ColorMapSettings") = None_) 
    
Provides methods and variables for editing field plots folder settings. 

Parameters: 
     

**postprocessor**`ansys.aedt.core.modules.post_general.PostProcessor` 
     

**folder_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the plot field folder. 

**arrow_settings**`ansys.aedt.core.modules.solution.ArrowSettings` , `optional` 
    
Arrow settings. Default is None. 

**marker_settings**`ansys.aedt.core.modules.solution.MarkerSettings` , `optional` 
    
Marker settings. Default is None. 

**scale_settings**`ansys.aedt.core.modules.solution.Scale3DSettings` , `optional` 
    
Scale settings. Default is None. 

**color_map_settings**`ansys.aedt.core.modules.solution.ColorMapSettings` , `optional` 
    
Colormap settings. Default is None.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import FolderPlotSettings
>>> obj = FolderPlotSettings()

```
Copy to clipboard
Methods  
| [`FolderPlotSettings.from_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.from_dict.html#ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.from_dict "ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.from_dict")(dictionary)  | Initialize the field plot settings from a dictionary.  |  
| --- | --- |  
| [`FolderPlotSettings.to_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.to_dict.html#ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.to_dict "ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.to_dict")()  | Convert the field plot settings to a dictionary.  |  
| [`FolderPlotSettings.update`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.update.html#ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.update "ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.update")()  | Update folder plot settings.  |  
Attributes  
| [`FolderPlotSettings.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.public_dir.html#ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.public_dir "ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |  
# FolderPlotSettings 

class ansys.aedt.core.visualization.post.field_data.FolderPlotSettings(_postprocessor_ , _folder_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _arrow_settings : [ArrowSettings](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ArrowSettings.html#ansys.aedt.core.visualization.post.field_data.ArrowSettings "ansys.aedt.core.visualization.post.field_data.ArrowSettings") = None_, _marker_settings : [MarkerSettings](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.MarkerSettings.html#ansys.aedt.core.visualization.post.field_data.MarkerSettings "ansys.aedt.core.visualization.post.field_data.MarkerSettings") = None_, _scale_settings : [Scale3DSettings](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.Scale3DSettings.html#ansys.aedt.core.visualization.post.field_data.Scale3DSettings "ansys.aedt.core.visualization.post.field_data.Scale3DSettings") = None_, _color_map_settings : [ColorMapSettings](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ColorMapSettings.html#ansys.aedt.core.visualization.post.field_data.ColorMapSettings "ansys.aedt.core.visualization.post.field_data.ColorMapSettings") = None_) 
    
Provides methods and variables for editing field plots folder settings. 

Parameters: 
     

**postprocessor**`ansys.aedt.core.modules.post_general.PostProcessor` 
     

**folder_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the plot field folder. 

**arrow_settings**`ansys.aedt.core.modules.solution.ArrowSettings` , `optional` 
    
Arrow settings. Default is None. 

**marker_settings**`ansys.aedt.core.modules.solution.MarkerSettings` , `optional` 
    
Marker settings. Default is None. 

**scale_settings**`ansys.aedt.core.modules.solution.Scale3DSettings` , `optional` 
    
Scale settings. Default is None. 

**color_map_settings**`ansys.aedt.core.modules.solution.ColorMapSettings` , `optional` 
    
Colormap settings. Default is None.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import FolderPlotSettings
>>> obj = FolderPlotSettings()

```
Copy to clipboard
Methods  
| [`FolderPlotSettings.from_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.from_dict.html#ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.from_dict "ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.from_dict")(dictionary)  | Initialize the field plot settings from a dictionary.  |  
| --- | --- |  
| [`FolderPlotSettings.to_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.to_dict.html#ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.to_dict "ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.to_dict")()  | Convert the field plot settings to a dictionary.  |  
| [`FolderPlotSettings.update`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.update.html#ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.update "ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.update")()  | Update folder plot settings.  |  
Attributes  
| [`FolderPlotSettings.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.public_dir.html#ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.public_dir "ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.rst.txt)

# FolderPlotSettings 

class ansys.aedt.core.visualization.post.field_data.FolderPlotSettings(_postprocessor_ , _folder_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _arrow_settings : [ArrowSettings](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ArrowSettings.html#ansys.aedt.core.visualization.post.field_data.ArrowSettings "ansys.aedt.core.visualization.post.field_data.ArrowSettings") = None_, _marker_settings : [MarkerSettings](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.MarkerSettings.html#ansys.aedt.core.visualization.post.field_data.MarkerSettings "ansys.aedt.core.visualization.post.field_data.MarkerSettings") = None_, _scale_settings : [Scale3DSettings](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.Scale3DSettings.html#ansys.aedt.core.visualization.post.field_data.Scale3DSettings "ansys.aedt.core.visualization.post.field_data.Scale3DSettings") = None_, _color_map_settings : [ColorMapSettings](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ColorMapSettings.html#ansys.aedt.core.visualization.post.field_data.ColorMapSettings "ansys.aedt.core.visualization.post.field_data.ColorMapSettings") = None_) 
    
Provides methods and variables for editing field plots folder settings. 

Parameters: 
     

**postprocessor**`ansys.aedt.core.modules.post_general.PostProcessor` 
     

**folder_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the plot field folder. 

**arrow_settings**`ansys.aedt.core.modules.solution.ArrowSettings` , `optional` 
    
Arrow settings. Default is None. 

**marker_settings**`ansys.aedt.core.modules.solution.MarkerSettings` , `optional` 
    
Marker settings. Default is None. 

**scale_settings**`ansys.aedt.core.modules.solution.Scale3DSettings` , `optional` 
    
Scale settings. Default is None. 

**color_map_settings**`ansys.aedt.core.modules.solution.ColorMapSettings` , `optional` 
    
Colormap settings. Default is None.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import FolderPlotSettings
>>> obj = FolderPlotSettings()

```
Copy to clipboard
Methods  
| [`FolderPlotSettings.from_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.from_dict.html#ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.from_dict "ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.from_dict")(dictionary)  | Initialize the field plot settings from a dictionary.  |  
| --- | --- |  
| [`FolderPlotSettings.to_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.to_dict.html#ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.to_dict "ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.to_dict")()  | Convert the field plot settings to a dictionary.  |  
| [`FolderPlotSettings.update`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.update.html#ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.update "ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.update")()  | Update folder plot settings.  |  
Attributes  
| [`FolderPlotSettings.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.public_dir.html#ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.public_dir "ansys.aedt.core.visualization.post.field_data.FolderPlotSettings.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |