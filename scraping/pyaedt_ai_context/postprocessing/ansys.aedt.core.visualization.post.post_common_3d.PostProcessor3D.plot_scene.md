---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_common_3d.PostProcessor3D.plot_scene.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# plot_scene 

PostProcessor3D.plot_scene(_frames : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _gif_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _norm_index : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _dy_rng : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _fps : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 30_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _view : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'yz'_, _zoom : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 2.0_, _convert_fields_in_db : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _log_multiplier : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 10.0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Plot the current model 3D scene with overlapping animation coming from a file list and save the gif. 

Parameters: 
     

**frames**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
File list containing animation frames to plot in CSV format or path to a text index file containing the full path to CSV files. 

**gif_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path for outputting the GIF file. 

**norm_index**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Frame to use to normalize your images. Data is already saved as dB : 100 for usual traffic scenes. 

**dy_rng**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Specify how many dB below you would like to specify the range_min. Tweak this a couple of times with small number of frames. 

**fps**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Frames per Second. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if show or only export gif. 

**view**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
View to export. Options are `"isometric"`, `"xy"`, `"xz"`, and `"yz"`. The default is `"isometric"`. 

**zoom**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Default zoom. Default Value is 2. 

**convert_fields_in_db**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if convert the fields before plotting in dB. Default Value is False. 

**log_multiplier**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Field multiplier if field in dB. Default Value is 10.0. 

Returns: 
    
Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.plot_scene(frames=["Box1"], gif_path="directory")

```
Copy to clipboard
# plot_scene 

PostProcessor3D.plot_scene(_frames : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _gif_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _norm_index : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _dy_rng : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _fps : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 30_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _view : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'yz'_, _zoom : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 2.0_, _convert_fields_in_db : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _log_multiplier : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 10.0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Plot the current model 3D scene with overlapping animation coming from a file list and save the gif. 

Parameters: 
     

**frames**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
File list containing animation frames to plot in CSV format or path to a text index file containing the full path to CSV files. 

**gif_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path for outputting the GIF file. 

**norm_index**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Frame to use to normalize your images. Data is already saved as dB : 100 for usual traffic scenes. 

**dy_rng**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Specify how many dB below you would like to specify the range_min. Tweak this a couple of times with small number of frames. 

**fps**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Frames per Second. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if show or only export gif. 

**view**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
View to export. Options are `"isometric"`, `"xy"`, `"xz"`, and `"yz"`. The default is `"isometric"`. 

**zoom**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Default zoom. Default Value is 2. 

**convert_fields_in_db**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if convert the fields before plotting in dB. Default Value is False. 

**log_multiplier**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Field multiplier if field in dB. Default Value is 10.0. 

Returns: 
    
Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.plot_scene(frames=["Box1"], gif_path="directory")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_common_3d.PostProcessor3D.plot_scene.rst.txt)

# plot_scene 

PostProcessor3D.plot_scene(_frames : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _gif_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _norm_index : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _dy_rng : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _fps : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 30_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _view : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'yz'_, _zoom : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 2.0_, _convert_fields_in_db : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _log_multiplier : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 10.0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Plot the current model 3D scene with overlapping animation coming from a file list and save the gif. 

Parameters: 
     

**frames**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
File list containing animation frames to plot in CSV format or path to a text index file containing the full path to CSV files. 

**gif_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path for outputting the GIF file. 

**norm_index**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Frame to use to normalize your images. Data is already saved as dB : 100 for usual traffic scenes. 

**dy_rng**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Specify how many dB below you would like to specify the range_min. Tweak this a couple of times with small number of frames. 

**fps**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Frames per Second. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if show or only export gif. 

**view**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
View to export. Options are `"isometric"`, `"xy"`, `"xz"`, and `"yz"`. The default is `"isometric"`. 

**zoom**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Default zoom. Default Value is 2. 

**convert_fields_in_db**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if convert the fields before plotting in dB. Default Value is False. 

**log_multiplier**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Field multiplier if field in dB. Default Value is 10.0. 

Returns: 
    
Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.plot_scene(frames=["Box1"], gif_path="directory")

```
Copy to clipboard