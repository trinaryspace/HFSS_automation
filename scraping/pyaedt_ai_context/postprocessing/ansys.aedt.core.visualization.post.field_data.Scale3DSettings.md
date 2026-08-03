---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.Scale3DSettings.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# Scale3DSettings 

class ansys.aedt.core.visualization.post.field_data.Scale3DSettings(_scale_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Auto'_, _scale_settings =AutoScale(n_levels=10, limit_precision_digits=False, precision_digits=3, use_current_scale_for_animation=False)_, _log : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _db : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _unit : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _number_format : [NumberFormat](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.NumberFormat.html#ansys.aedt.core.visualization.post.field_data.NumberFormat "ansys.aedt.core.visualization.post.field_data.NumberFormat") = NumberFormat(format_type=Automatic, width=4, precision=4)_) 
    
Provides methods and variables for editing scale folder settings. 

Parameters: 
     

**scale_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Scale type. Default is “Auto”. 

**scale_settings**`ansys.aedt.core.modules.post_general.AutoScale` , 
    
> `ansys.aedt.core.modules.post_general.MinMaxScale` or `ansys.aedt.core.modules.post_general.SpecifiedScale`, optional
Scale settings. Default is AutoScale(). 

**log**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use a log scale. Default is False. 

**db**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use dB scale. Default is False. 

**unit**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Unit to use in the scale. Default is None. 

**number_format**`ansys.aedt.core.modules.post_general.NumberFormat` , `optional` 
    
Number format settings. Default is NumberFormat().
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import Scale3DSettings
>>> obj = Scale3DSettings()

```
Copy to clipboard
Methods  
| [`Scale3DSettings.from_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.Scale3DSettings.from_dict.html#ansys.aedt.core.visualization.post.field_data.Scale3DSettings.from_dict "ansys.aedt.core.visualization.post.field_data.Scale3DSettings.from_dict")(dictionary)  | Initialize the scale settings of the field plot settings from a dictionary.  |  
| --- | --- |  
| [`Scale3DSettings.to_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.Scale3DSettings.to_dict.html#ansys.aedt.core.visualization.post.field_data.Scale3DSettings.to_dict "ansys.aedt.core.visualization.post.field_data.Scale3DSettings.to_dict")()  | Convert the scale settings to a dictionary.  |  
Attributes  
| [`Scale3DSettings.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.Scale3DSettings.public_dir.html#ansys.aedt.core.visualization.post.field_data.Scale3DSettings.public_dir "ansys.aedt.core.visualization.post.field_data.Scale3DSettings.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |  
| [`Scale3DSettings.scale_settings`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.Scale3DSettings.scale_settings.html#ansys.aedt.core.visualization.post.field_data.Scale3DSettings.scale_settings "ansys.aedt.core.visualization.post.field_data.Scale3DSettings.scale_settings")  | Get the current scale settings based on the scale type.  |  
| [`Scale3DSettings.scale_type`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.Scale3DSettings.scale_type.html#ansys.aedt.core.visualization.post.field_data.Scale3DSettings.scale_type "ansys.aedt.core.visualization.post.field_data.Scale3DSettings.scale_type")  | Get type of scale used for the field plot.  |  
| [`Scale3DSettings.unit`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.Scale3DSettings.unit.html#ansys.aedt.core.visualization.post.field_data.Scale3DSettings.unit "ansys.aedt.core.visualization.post.field_data.Scale3DSettings.unit")  | Get unit used in the plot.  |  
# Scale3DSettings 

class ansys.aedt.core.visualization.post.field_data.Scale3DSettings(_scale_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Auto'_, _scale_settings =AutoScale(n_levels=10, limit_precision_digits=False, precision_digits=3, use_current_scale_for_animation=False)_, _log : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _db : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _unit : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _number_format : [NumberFormat](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.NumberFormat.html#ansys.aedt.core.visualization.post.field_data.NumberFormat "ansys.aedt.core.visualization.post.field_data.NumberFormat") = NumberFormat(format_type=Automatic, width=4, precision=4)_) 
    
Provides methods and variables for editing scale folder settings. 

Parameters: 
     

**scale_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Scale type. Default is “Auto”. 

**scale_settings**`ansys.aedt.core.modules.post_general.AutoScale` , 
    
> `ansys.aedt.core.modules.post_general.MinMaxScale` or `ansys.aedt.core.modules.post_general.SpecifiedScale`, optional
Scale settings. Default is AutoScale(). 

**log**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use a log scale. Default is False. 

**db**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use dB scale. Default is False. 

**unit**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Unit to use in the scale. Default is None. 

**number_format**`ansys.aedt.core.modules.post_general.NumberFormat` , `optional` 
    
Number format settings. Default is NumberFormat().
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import Scale3DSettings
>>> obj = Scale3DSettings()

```
Copy to clipboard
Methods  
| [`Scale3DSettings.from_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.Scale3DSettings.from_dict.html#ansys.aedt.core.visualization.post.field_data.Scale3DSettings.from_dict "ansys.aedt.core.visualization.post.field_data.Scale3DSettings.from_dict")(dictionary)  | Initialize the scale settings of the field plot settings from a dictionary.  |  
| --- | --- |  
| [`Scale3DSettings.to_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.Scale3DSettings.to_dict.html#ansys.aedt.core.visualization.post.field_data.Scale3DSettings.to_dict "ansys.aedt.core.visualization.post.field_data.Scale3DSettings.to_dict")()  | Convert the scale settings to a dictionary.  |  
Attributes  
| [`Scale3DSettings.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.Scale3DSettings.public_dir.html#ansys.aedt.core.visualization.post.field_data.Scale3DSettings.public_dir "ansys.aedt.core.visualization.post.field_data.Scale3DSettings.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |  
| [`Scale3DSettings.scale_settings`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.Scale3DSettings.scale_settings.html#ansys.aedt.core.visualization.post.field_data.Scale3DSettings.scale_settings "ansys.aedt.core.visualization.post.field_data.Scale3DSettings.scale_settings")  | Get the current scale settings based on the scale type.  |  
| [`Scale3DSettings.scale_type`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.Scale3DSettings.scale_type.html#ansys.aedt.core.visualization.post.field_data.Scale3DSettings.scale_type "ansys.aedt.core.visualization.post.field_data.Scale3DSettings.scale_type")  | Get type of scale used for the field plot.  |  
| [`Scale3DSettings.unit`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.Scale3DSettings.unit.html#ansys.aedt.core.visualization.post.field_data.Scale3DSettings.unit "ansys.aedt.core.visualization.post.field_data.Scale3DSettings.unit")  | Get unit used in the plot.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.Scale3DSettings.rst.txt)

# Scale3DSettings 

class ansys.aedt.core.visualization.post.field_data.Scale3DSettings(_scale_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Auto'_, _scale_settings =AutoScale(n_levels=10, limit_precision_digits=False, precision_digits=3, use_current_scale_for_animation=False)_, _log : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _db : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _unit : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _number_format : [NumberFormat](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.NumberFormat.html#ansys.aedt.core.visualization.post.field_data.NumberFormat "ansys.aedt.core.visualization.post.field_data.NumberFormat") = NumberFormat(format_type=Automatic, width=4, precision=4)_) 
    
Provides methods and variables for editing scale folder settings. 

Parameters: 
     

**scale_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Scale type. Default is “Auto”. 

**scale_settings**`ansys.aedt.core.modules.post_general.AutoScale` , 
    
> `ansys.aedt.core.modules.post_general.MinMaxScale` or `ansys.aedt.core.modules.post_general.SpecifiedScale`, optional
Scale settings. Default is AutoScale(). 

**log**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use a log scale. Default is False. 

**db**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use dB scale. Default is False. 

**unit**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Unit to use in the scale. Default is None. 

**number_format**`ansys.aedt.core.modules.post_general.NumberFormat` , `optional` 
    
Number format settings. Default is NumberFormat().
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import Scale3DSettings
>>> obj = Scale3DSettings()

```
Copy to clipboard
Methods  
| [`Scale3DSettings.from_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.Scale3DSettings.from_dict.html#ansys.aedt.core.visualization.post.field_data.Scale3DSettings.from_dict "ansys.aedt.core.visualization.post.field_data.Scale3DSettings.from_dict")(dictionary)  | Initialize the scale settings of the field plot settings from a dictionary.  |  
| --- | --- |  
| [`Scale3DSettings.to_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.Scale3DSettings.to_dict.html#ansys.aedt.core.visualization.post.field_data.Scale3DSettings.to_dict "ansys.aedt.core.visualization.post.field_data.Scale3DSettings.to_dict")()  | Convert the scale settings to a dictionary.  |  
Attributes  
| [`Scale3DSettings.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.Scale3DSettings.public_dir.html#ansys.aedt.core.visualization.post.field_data.Scale3DSettings.public_dir "ansys.aedt.core.visualization.post.field_data.Scale3DSettings.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |  
| [`Scale3DSettings.scale_settings`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.Scale3DSettings.scale_settings.html#ansys.aedt.core.visualization.post.field_data.Scale3DSettings.scale_settings "ansys.aedt.core.visualization.post.field_data.Scale3DSettings.scale_settings")  | Get the current scale settings based on the scale type.  |  
| [`Scale3DSettings.scale_type`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.Scale3DSettings.scale_type.html#ansys.aedt.core.visualization.post.field_data.Scale3DSettings.scale_type "ansys.aedt.core.visualization.post.field_data.Scale3DSettings.scale_type")  | Get type of scale used for the field plot.  |  
| [`Scale3DSettings.unit`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.Scale3DSettings.unit.html#ansys.aedt.core.visualization.post.field_data.Scale3DSettings.unit "ansys.aedt.core.visualization.post.field_data.Scale3DSettings.unit")  | Get unit used in the plot.  |