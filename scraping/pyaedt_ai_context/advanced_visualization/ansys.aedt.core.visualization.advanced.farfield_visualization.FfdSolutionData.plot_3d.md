---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData.plot_3d.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# plot_3d 

FfdSolutionData.plot_3d(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'RealizedGain'_, _quantity_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'dB10'_, _rotation : np.ndarray = None_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_as_standalone : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _pyvista_object : Plotter = None_, _background : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _scale_farfield : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _show_beam_slider : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_geometry : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | Plotter 
    
Create a 3D polar plot of the geometry with a radiation pattern in PyVista. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Quantity to plot. The default is `"RealizedGain"`. Available quantities are: `"RealizedGain"`, `"RealizedGain_Theta"`, `"RealizedGain_Phi"`, `"rETotal"`, `"rETheta"`, and `"rEPhi"`. 

**quantity_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Conversion data function. Available functions are: `"abs"`, `"ang"`, `"dB10"`, `"dB20"`, `"deg"`, `"imag"`, `"norm"`, and `"real"`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path for the image file. The default is `None`, in which case a file is not exported. 

**rotation**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Far field rotation matrix. The matrix contains three vectors, around x, y, and z axes. The default is `[[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]`. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot. The default is `True`. 

**show_as_standalone**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show a plot as standalone. The default is `False`. 

**pyvista_object**`Pyvista.Plotter` , `optional` 
    
PyVista instance defined externally. The default is `None`. 

**background**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Background color if a list is passed or background picture if a string is passed. The default is `None`. 

**scale_farfield**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List with minimum and maximum values of the scale slider. The default is `None`. 

**show_beam_slider**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the Theta and Phi scan slider is active. The default is `True`. 

**show_geometry**
    
Whether to show the geometry. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or `Pyvista.Plotter` 
    
`True` when successful. The `Pyvista.Plotter` is returned when `show` and `image_path` are `False`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss(version="2026.1", design="Antenna")
>>> setup_name = "Setup1 : LastAdaptive"
>>> frequencies = [77e9]
>>> sphere = "3D"
>>> data = app.get_antenna_data(setup=setup_name, sphere=sphere)
>>> data.plot_3d(quantity_format="dB10")

```
Copy to clipboard
# plot_3d 

FfdSolutionData.plot_3d(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'RealizedGain'_, _quantity_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'dB10'_, _rotation : np.ndarray = None_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_as_standalone : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _pyvista_object : Plotter = None_, _background : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _scale_farfield : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _show_beam_slider : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_geometry : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | Plotter 
    
Create a 3D polar plot of the geometry with a radiation pattern in PyVista. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Quantity to plot. The default is `"RealizedGain"`. Available quantities are: `"RealizedGain"`, `"RealizedGain_Theta"`, `"RealizedGain_Phi"`, `"rETotal"`, `"rETheta"`, and `"rEPhi"`. 

**quantity_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Conversion data function. Available functions are: `"abs"`, `"ang"`, `"dB10"`, `"dB20"`, `"deg"`, `"imag"`, `"norm"`, and `"real"`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path for the image file. The default is `None`, in which case a file is not exported. 

**rotation**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Far field rotation matrix. The matrix contains three vectors, around x, y, and z axes. The default is `[[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]`. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot. The default is `True`. 

**show_as_standalone**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show a plot as standalone. The default is `False`. 

**pyvista_object**`Pyvista.Plotter` , `optional` 
    
PyVista instance defined externally. The default is `None`. 

**background**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Background color if a list is passed or background picture if a string is passed. The default is `None`. 

**scale_farfield**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List with minimum and maximum values of the scale slider. The default is `None`. 

**show_beam_slider**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the Theta and Phi scan slider is active. The default is `True`. 

**show_geometry**
    
Whether to show the geometry. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or `Pyvista.Plotter` 
    
`True` when successful. The `Pyvista.Plotter` is returned when `show` and `image_path` are `False`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss(version="2026.1", design="Antenna")
>>> setup_name = "Setup1 : LastAdaptive"
>>> frequencies = [77e9]
>>> sphere = "3D"
>>> data = app.get_antenna_data(setup=setup_name, sphere=sphere)
>>> data.plot_3d(quantity_format="dB10")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.farfield_visualization.FfdSolutionData.plot_3d.rst.txt)

# plot_3d 

FfdSolutionData.plot_3d(_quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'RealizedGain'_, _quantity_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'dB10'_, _rotation : np.ndarray = None_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _show : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_as_standalone : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _pyvista_object : Plotter = None_, _background : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _scale_farfield : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _show_beam_slider : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _show_geometry : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | Plotter 
    
Create a 3D polar plot of the geometry with a radiation pattern in PyVista. 

Parameters: 
     

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Quantity to plot. The default is `"RealizedGain"`. Available quantities are: `"RealizedGain"`, `"RealizedGain_Theta"`, `"RealizedGain_Phi"`, `"rETotal"`, `"rETheta"`, and `"rEPhi"`. 

**quantity_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Conversion data function. Available functions are: `"abs"`, `"ang"`, `"dB10"`, `"dB20"`, `"deg"`, `"imag"`, `"norm"`, and `"real"`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path for the image file. The default is `None`, in which case a file is not exported. 

**rotation**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Far field rotation matrix. The matrix contains three vectors, around x, y, and z axes. The default is `[[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]`. 

**show**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show the plot. The default is `True`. 

**show_as_standalone**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to show a plot as standalone. The default is `False`. 

**pyvista_object**`Pyvista.Plotter` , `optional` 
    
PyVista instance defined externally. The default is `None`. 

**background**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Background color if a list is passed or background picture if a string is passed. The default is `None`. 

**scale_farfield**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List with minimum and maximum values of the scale slider. The default is `None`. 

**show_beam_slider**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the Theta and Phi scan slider is active. The default is `True`. 

**show_geometry**
    
Whether to show the geometry. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or `Pyvista.Plotter` 
    
`True` when successful. The `Pyvista.Plotter` is returned when `show` and `image_path` are `False`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss(version="2026.1", design="Antenna")
>>> setup_name = "Setup1 : LastAdaptive"
>>> frequencies = [77e9]
>>> sphere = "3D"
>>> data = app.get_antenna_data(setup=setup_name, sphere=sphere)
>>> data.plot_3d(quantity_format="dB10")

```
Copy to clipboard