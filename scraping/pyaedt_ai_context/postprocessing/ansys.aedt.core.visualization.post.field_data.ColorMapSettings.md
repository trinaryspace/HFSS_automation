---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ColorMapSettings.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# ColorMapSettings 

class ansys.aedt.core.visualization.post.field_data.ColorMapSettings(_map_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Spectrum'_, _color : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Rainbow'_) 
    
Provides methods and variables for editing color map folder settings. 

Parameters: 
     

**map_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The type of colormap to use. Must be one of the allowed types (“Spectrum”, “Ramp”, “Uniform”). Default is “Spectrum”. 

**color**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")], `optional` 
    
Color to use. If “Spectrum” color map, a string is expected. Else a list of 3 values (R,G,B). Default is “Rainbow”.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import ColorMapSettings
>>> obj = ColorMapSettings()

```
Copy to clipboard
Methods  
| [`ColorMapSettings.from_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ColorMapSettings.from_dict.html#ansys.aedt.core.visualization.post.field_data.ColorMapSettings.from_dict "ansys.aedt.core.visualization.post.field_data.ColorMapSettings.from_dict")(settings)  | Initialize the number format settings of the colormap settings from a dictionary.  |  
| --- | --- |  
| [`ColorMapSettings.to_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ColorMapSettings.to_dict.html#ansys.aedt.core.visualization.post.field_data.ColorMapSettings.to_dict "ansys.aedt.core.visualization.post.field_data.ColorMapSettings.to_dict")()  | Convert the color map settings to a dictionary.  |  
Attributes  
| [`ColorMapSettings.color`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ColorMapSettings.color.html#ansys.aedt.core.visualization.post.field_data.ColorMapSettings.color "ansys.aedt.core.visualization.post.field_data.ColorMapSettings.color")  | Get the color based on the map type.  |  
| --- | --- |  
| [`ColorMapSettings.map_type`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ColorMapSettings.map_type.html#ansys.aedt.core.visualization.post.field_data.ColorMapSettings.map_type "ansys.aedt.core.visualization.post.field_data.ColorMapSettings.map_type")  | Get the color map type for the field plot.  |  
| [`ColorMapSettings.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ColorMapSettings.public_dir.html#ansys.aedt.core.visualization.post.field_data.ColorMapSettings.public_dir "ansys.aedt.core.visualization.post.field_data.ColorMapSettings.public_dir")  | Shortcut for dir(self).  |  
# ColorMapSettings 

class ansys.aedt.core.visualization.post.field_data.ColorMapSettings(_map_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Spectrum'_, _color : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Rainbow'_) 
    
Provides methods and variables for editing color map folder settings. 

Parameters: 
     

**map_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The type of colormap to use. Must be one of the allowed types (“Spectrum”, “Ramp”, “Uniform”). Default is “Spectrum”. 

**color**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")], `optional` 
    
Color to use. If “Spectrum” color map, a string is expected. Else a list of 3 values (R,G,B). Default is “Rainbow”.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import ColorMapSettings
>>> obj = ColorMapSettings()

```
Copy to clipboard
Methods  
| [`ColorMapSettings.from_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ColorMapSettings.from_dict.html#ansys.aedt.core.visualization.post.field_data.ColorMapSettings.from_dict "ansys.aedt.core.visualization.post.field_data.ColorMapSettings.from_dict")(settings)  | Initialize the number format settings of the colormap settings from a dictionary.  |  
| --- | --- |  
| [`ColorMapSettings.to_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ColorMapSettings.to_dict.html#ansys.aedt.core.visualization.post.field_data.ColorMapSettings.to_dict "ansys.aedt.core.visualization.post.field_data.ColorMapSettings.to_dict")()  | Convert the color map settings to a dictionary.  |  
Attributes  
| [`ColorMapSettings.color`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ColorMapSettings.color.html#ansys.aedt.core.visualization.post.field_data.ColorMapSettings.color "ansys.aedt.core.visualization.post.field_data.ColorMapSettings.color")  | Get the color based on the map type.  |  
| --- | --- |  
| [`ColorMapSettings.map_type`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ColorMapSettings.map_type.html#ansys.aedt.core.visualization.post.field_data.ColorMapSettings.map_type "ansys.aedt.core.visualization.post.field_data.ColorMapSettings.map_type")  | Get the color map type for the field plot.  |  
| [`ColorMapSettings.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ColorMapSettings.public_dir.html#ansys.aedt.core.visualization.post.field_data.ColorMapSettings.public_dir "ansys.aedt.core.visualization.post.field_data.ColorMapSettings.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ColorMapSettings.rst.txt)

# ColorMapSettings 

class ansys.aedt.core.visualization.post.field_data.ColorMapSettings(_map_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Spectrum'_, _color : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Rainbow'_) 
    
Provides methods and variables for editing color map folder settings. 

Parameters: 
     

**map_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The type of colormap to use. Must be one of the allowed types (“Spectrum”, “Ramp”, “Uniform”). Default is “Spectrum”. 

**color**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")], `optional` 
    
Color to use. If “Spectrum” color map, a string is expected. Else a list of 3 values (R,G,B). Default is “Rainbow”.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import ColorMapSettings
>>> obj = ColorMapSettings()

```
Copy to clipboard
Methods  
| [`ColorMapSettings.from_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ColorMapSettings.from_dict.html#ansys.aedt.core.visualization.post.field_data.ColorMapSettings.from_dict "ansys.aedt.core.visualization.post.field_data.ColorMapSettings.from_dict")(settings)  | Initialize the number format settings of the colormap settings from a dictionary.  |  
| --- | --- |  
| [`ColorMapSettings.to_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ColorMapSettings.to_dict.html#ansys.aedt.core.visualization.post.field_data.ColorMapSettings.to_dict "ansys.aedt.core.visualization.post.field_data.ColorMapSettings.to_dict")()  | Convert the color map settings to a dictionary.  |  
Attributes  
| [`ColorMapSettings.color`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ColorMapSettings.color.html#ansys.aedt.core.visualization.post.field_data.ColorMapSettings.color "ansys.aedt.core.visualization.post.field_data.ColorMapSettings.color")  | Get the color based on the map type.  |  
| --- | --- |  
| [`ColorMapSettings.map_type`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ColorMapSettings.map_type.html#ansys.aedt.core.visualization.post.field_data.ColorMapSettings.map_type "ansys.aedt.core.visualization.post.field_data.ColorMapSettings.map_type")  | Get the color map type for the field plot.  |  
| [`ColorMapSettings.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.ColorMapSettings.public_dir.html#ansys.aedt.core.visualization.post.field_data.ColorMapSettings.public_dir "ansys.aedt.core.visualization.post.field_data.ColorMapSettings.public_dir")  | Shortcut for dir(self).  |