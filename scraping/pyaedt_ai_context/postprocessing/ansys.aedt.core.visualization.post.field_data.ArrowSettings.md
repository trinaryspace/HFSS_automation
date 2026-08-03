---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ArrowSettings.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# ArrowSettings 

class ansys.aedt.core.visualization.post.field_data.ArrowSettings(_arrow_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Line'_, _arrow_size : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.005_, _map_size : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _map_color : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_arrow_tail : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _magnitude_filtering : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _magnitude_threshold : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _min_magnitude : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _max_magnitude : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.5_) 
    
Provides methods and variables for editing arrow folder settings. 

Parameters: 
     

**arrow_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The type of arrows to use. Must be one of the allowed types (“Line”, “Cylinder”, “Umbrella”). Default is “Line”. 

**arrow_size**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Size of the arrow. Default is 0.005. 

**map_size**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to map the field magnitude to the arrow type. Default is False. 

**map_color**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to map the field magnitude to the arrow color. Default is True. 

**show_arrow_tail**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the arrow tail. Default is False. 

**magnitude_filtering**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to filter the field magnitude for plotting vectors. Default is False. 

**magnitude_threshold**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Threshold value for plotting vectors. Default is 0. 

**min_magnitude**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Minimum value for plotting vectors. Default is 0. 

**max_magnitude**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Maximum value for plotting vectors. Default is 0.5.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import ArrowSettings
>>> obj = ArrowSettings()

```
Copy to clipboard
Methods  
| [`ArrowSettings.from_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ArrowSettings.from_dict.html#ansys.aedt.core.visualization.post.field_data.ArrowSettings.from_dict "ansys.aedt.core.visualization.post.field_data.ArrowSettings.from_dict")(dictionary)  | Initialize the arrow settings of the field plot settings from a dictionary.  |  
| --- | --- |  
| [`ArrowSettings.to_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ArrowSettings.to_dict.html#ansys.aedt.core.visualization.post.field_data.ArrowSettings.to_dict "ansys.aedt.core.visualization.post.field_data.ArrowSettings.to_dict")()  | Convert the arrow settings to a dictionary.  |  
Attributes  
| [`ArrowSettings.arrow_type`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ArrowSettings.arrow_type.html#ansys.aedt.core.visualization.post.field_data.ArrowSettings.arrow_type "ansys.aedt.core.visualization.post.field_data.ArrowSettings.arrow_type")  | Get the type of arrows used in the field plot.  |  
| --- | --- |  
| [`ArrowSettings.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ArrowSettings.public_dir.html#ansys.aedt.core.visualization.post.field_data.ArrowSettings.public_dir "ansys.aedt.core.visualization.post.field_data.ArrowSettings.public_dir")  | Shortcut for dir(self).  |  
# ArrowSettings 

class ansys.aedt.core.visualization.post.field_data.ArrowSettings(_arrow_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Line'_, _arrow_size : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.005_, _map_size : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _map_color : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_arrow_tail : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _magnitude_filtering : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _magnitude_threshold : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _min_magnitude : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _max_magnitude : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.5_) 
    
Provides methods and variables for editing arrow folder settings. 

Parameters: 
     

**arrow_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The type of arrows to use. Must be one of the allowed types (“Line”, “Cylinder”, “Umbrella”). Default is “Line”. 

**arrow_size**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Size of the arrow. Default is 0.005. 

**map_size**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to map the field magnitude to the arrow type. Default is False. 

**map_color**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to map the field magnitude to the arrow color. Default is True. 

**show_arrow_tail**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the arrow tail. Default is False. 

**magnitude_filtering**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to filter the field magnitude for plotting vectors. Default is False. 

**magnitude_threshold**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Threshold value for plotting vectors. Default is 0. 

**min_magnitude**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Minimum value for plotting vectors. Default is 0. 

**max_magnitude**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Maximum value for plotting vectors. Default is 0.5.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import ArrowSettings
>>> obj = ArrowSettings()

```
Copy to clipboard
Methods  
| [`ArrowSettings.from_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ArrowSettings.from_dict.html#ansys.aedt.core.visualization.post.field_data.ArrowSettings.from_dict "ansys.aedt.core.visualization.post.field_data.ArrowSettings.from_dict")(dictionary)  | Initialize the arrow settings of the field plot settings from a dictionary.  |  
| --- | --- |  
| [`ArrowSettings.to_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ArrowSettings.to_dict.html#ansys.aedt.core.visualization.post.field_data.ArrowSettings.to_dict "ansys.aedt.core.visualization.post.field_data.ArrowSettings.to_dict")()  | Convert the arrow settings to a dictionary.  |  
Attributes  
| [`ArrowSettings.arrow_type`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ArrowSettings.arrow_type.html#ansys.aedt.core.visualization.post.field_data.ArrowSettings.arrow_type "ansys.aedt.core.visualization.post.field_data.ArrowSettings.arrow_type")  | Get the type of arrows used in the field plot.  |  
| --- | --- |  
| [`ArrowSettings.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ArrowSettings.public_dir.html#ansys.aedt.core.visualization.post.field_data.ArrowSettings.public_dir "ansys.aedt.core.visualization.post.field_data.ArrowSettings.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ArrowSettings.rst.txt)

# ArrowSettings 

class ansys.aedt.core.visualization.post.field_data.ArrowSettings(_arrow_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Line'_, _arrow_size : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.005_, _map_size : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _map_color : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_arrow_tail : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _magnitude_filtering : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _magnitude_threshold : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _min_magnitude : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _max_magnitude : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.5_) 
    
Provides methods and variables for editing arrow folder settings. 

Parameters: 
     

**arrow_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The type of arrows to use. Must be one of the allowed types (“Line”, “Cylinder”, “Umbrella”). Default is “Line”. 

**arrow_size**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Size of the arrow. Default is 0.005. 

**map_size**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to map the field magnitude to the arrow type. Default is False. 

**map_color**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to map the field magnitude to the arrow color. Default is True. 

**show_arrow_tail**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the arrow tail. Default is False. 

**magnitude_filtering**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to filter the field magnitude for plotting vectors. Default is False. 

**magnitude_threshold**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Threshold value for plotting vectors. Default is 0. 

**min_magnitude**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Minimum value for plotting vectors. Default is 0. 

**max_magnitude**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Maximum value for plotting vectors. Default is 0.5.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import ArrowSettings
>>> obj = ArrowSettings()

```
Copy to clipboard
Methods  
| [`ArrowSettings.from_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ArrowSettings.from_dict.html#ansys.aedt.core.visualization.post.field_data.ArrowSettings.from_dict "ansys.aedt.core.visualization.post.field_data.ArrowSettings.from_dict")(dictionary)  | Initialize the arrow settings of the field plot settings from a dictionary.  |  
| --- | --- |  
| [`ArrowSettings.to_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ArrowSettings.to_dict.html#ansys.aedt.core.visualization.post.field_data.ArrowSettings.to_dict "ansys.aedt.core.visualization.post.field_data.ArrowSettings.to_dict")()  | Convert the arrow settings to a dictionary.  |  
Attributes  
| [`ArrowSettings.arrow_type`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ArrowSettings.arrow_type.html#ansys.aedt.core.visualization.post.field_data.ArrowSettings.arrow_type "ansys.aedt.core.visualization.post.field_data.ArrowSettings.arrow_type")  | Get the type of arrows used in the field plot.  |  
| --- | --- |  
| [`ArrowSettings.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ArrowSettings.public_dir.html#ansys.aedt.core.visualization.post.field_data.ArrowSettings.public_dir "ansys.aedt.core.visualization.post.field_data.ArrowSettings.public_dir")  | Shortcut for dir(self).  |