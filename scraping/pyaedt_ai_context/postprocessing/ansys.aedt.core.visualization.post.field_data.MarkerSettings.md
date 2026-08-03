---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.MarkerSettings.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# MarkerSettings 

class ansys.aedt.core.visualization.post.field_data.MarkerSettings(_marker_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Box'_, _map_size : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _map_color : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _marker_size : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.005_) 
    
Provides methods and variables for editing marker folder settings. 

Parameters: 
     

**marker_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The type of maker to use. Must be one of the allowed types (“Octahedron”, “Tetrahedron”, “Sphere”, “Box”, “Arrow”). Default is “Box”. 

**marker_size**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Size of the marker. Default is 0.005. 

**map_size**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to map the field magnitude to the arrow type. Default is False. 

**map_color**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to map the field magnitude to the arrow color. Default is True.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import MarkerSettings
>>> obj = MarkerSettings()

```
Copy to clipboard
Methods  
| [`MarkerSettings.from_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.MarkerSettings.from_dict.html#ansys.aedt.core.visualization.post.field_data.MarkerSettings.from_dict "ansys.aedt.core.visualization.post.field_data.MarkerSettings.from_dict")(dictionary)  | Initialize the marker settings of the field plot settings from a dictionary.  |  
| --- | --- |  
| [`MarkerSettings.to_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.MarkerSettings.to_dict.html#ansys.aedt.core.visualization.post.field_data.MarkerSettings.to_dict "ansys.aedt.core.visualization.post.field_data.MarkerSettings.to_dict")()  | Convert the marker settings to a dictionary.  |  
Attributes  
| [`MarkerSettings.marker_type`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.MarkerSettings.marker_type.html#ansys.aedt.core.visualization.post.field_data.MarkerSettings.marker_type "ansys.aedt.core.visualization.post.field_data.MarkerSettings.marker_type")  | Get the type of maker to use.  |  
| --- | --- |  
| [`MarkerSettings.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.MarkerSettings.public_dir.html#ansys.aedt.core.visualization.post.field_data.MarkerSettings.public_dir "ansys.aedt.core.visualization.post.field_data.MarkerSettings.public_dir")  | Shortcut for dir(self).  |  
# MarkerSettings 

class ansys.aedt.core.visualization.post.field_data.MarkerSettings(_marker_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Box'_, _map_size : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _map_color : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _marker_size : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.005_) 
    
Provides methods and variables for editing marker folder settings. 

Parameters: 
     

**marker_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The type of maker to use. Must be one of the allowed types (“Octahedron”, “Tetrahedron”, “Sphere”, “Box”, “Arrow”). Default is “Box”. 

**marker_size**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Size of the marker. Default is 0.005. 

**map_size**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to map the field magnitude to the arrow type. Default is False. 

**map_color**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to map the field magnitude to the arrow color. Default is True.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import MarkerSettings
>>> obj = MarkerSettings()

```
Copy to clipboard
Methods  
| [`MarkerSettings.from_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.MarkerSettings.from_dict.html#ansys.aedt.core.visualization.post.field_data.MarkerSettings.from_dict "ansys.aedt.core.visualization.post.field_data.MarkerSettings.from_dict")(dictionary)  | Initialize the marker settings of the field plot settings from a dictionary.  |  
| --- | --- |  
| [`MarkerSettings.to_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.MarkerSettings.to_dict.html#ansys.aedt.core.visualization.post.field_data.MarkerSettings.to_dict "ansys.aedt.core.visualization.post.field_data.MarkerSettings.to_dict")()  | Convert the marker settings to a dictionary.  |  
Attributes  
| [`MarkerSettings.marker_type`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.MarkerSettings.marker_type.html#ansys.aedt.core.visualization.post.field_data.MarkerSettings.marker_type "ansys.aedt.core.visualization.post.field_data.MarkerSettings.marker_type")  | Get the type of maker to use.  |  
| --- | --- |  
| [`MarkerSettings.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.MarkerSettings.public_dir.html#ansys.aedt.core.visualization.post.field_data.MarkerSettings.public_dir "ansys.aedt.core.visualization.post.field_data.MarkerSettings.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.MarkerSettings.rst.txt)

# MarkerSettings 

class ansys.aedt.core.visualization.post.field_data.MarkerSettings(_marker_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Box'_, _map_size : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _map_color : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _marker_size : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.005_) 
    
Provides methods and variables for editing marker folder settings. 

Parameters: 
     

**marker_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The type of maker to use. Must be one of the allowed types (“Octahedron”, “Tetrahedron”, “Sphere”, “Box”, “Arrow”). Default is “Box”. 

**marker_size**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Size of the marker. Default is 0.005. 

**map_size**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to map the field magnitude to the arrow type. Default is False. 

**map_color**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to map the field magnitude to the arrow color. Default is True.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import MarkerSettings
>>> obj = MarkerSettings()

```
Copy to clipboard
Methods  
| [`MarkerSettings.from_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.MarkerSettings.from_dict.html#ansys.aedt.core.visualization.post.field_data.MarkerSettings.from_dict "ansys.aedt.core.visualization.post.field_data.MarkerSettings.from_dict")(dictionary)  | Initialize the marker settings of the field plot settings from a dictionary.  |  
| --- | --- |  
| [`MarkerSettings.to_dict`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.MarkerSettings.to_dict.html#ansys.aedt.core.visualization.post.field_data.MarkerSettings.to_dict "ansys.aedt.core.visualization.post.field_data.MarkerSettings.to_dict")()  | Convert the marker settings to a dictionary.  |  
Attributes  
| [`MarkerSettings.marker_type`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.MarkerSettings.marker_type.html#ansys.aedt.core.visualization.post.field_data.MarkerSettings.marker_type "ansys.aedt.core.visualization.post.field_data.MarkerSettings.marker_type")  | Get the type of maker to use.  |  
| --- | --- |  
| [`MarkerSettings.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.MarkerSettings.public_dir.html#ansys.aedt.core.visualization.post.field_data.MarkerSettings.public_dir "ansys.aedt.core.visualization.post.field_data.MarkerSettings.public_dir")  | Shortcut for dir(self).  |