---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_icepak.PostProcessorIcepak.get_model_plotter_geometries.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# get_model_plotter_geometries 

PostProcessorIcepak.get_model_plotter_geometries(_objects : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _plot_as_separate_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _plot_air_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _force_opacity_value : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _array_coordinates : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]] = None_, _generate_mesh : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _get_objects_from_aedt : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [ModelPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter") 
    
Initialize the Model Plotter object with actual modeler objects and return it. 

Parameters: 
     

**objects**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Optional list of objects to plot. If None all objects will be exported. 

**plot_as_separate_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Plot each object separately. It may require more time to export from AEDT. 

**plot_air_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Plot also air and vacuum objects. 

**force_opacity_value**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Opacity value between 0 and 1 to be applied to all model. If None aedt opacity will be applied to each object. 

**array_coordinates**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of array element centers. The modeler objects will be duplicated and translated. List of [[x1,y1,z1], [x2,y2,z2]…]. 

**generate_mesh**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to generate the mesh after importing objects. The default is `True`. 

**get_objects_from_aedt**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export objects from AEDT and initialize them. The default is `True`. 

Returns: 
     

`ansys.aedt.core.generic.plot.ModelPlotter`
    
Model Object.
Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.get_model_plotter_geometries(objects=["Box1"], plot_as_separate_objects=True)

```
Copy to clipboard
# get_model_plotter_geometries 

PostProcessorIcepak.get_model_plotter_geometries(_objects : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _plot_as_separate_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _plot_air_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _force_opacity_value : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _array_coordinates : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]] = None_, _generate_mesh : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _get_objects_from_aedt : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [ModelPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter") 
    
Initialize the Model Plotter object with actual modeler objects and return it. 

Parameters: 
     

**objects**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Optional list of objects to plot. If None all objects will be exported. 

**plot_as_separate_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Plot each object separately. It may require more time to export from AEDT. 

**plot_air_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Plot also air and vacuum objects. 

**force_opacity_value**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Opacity value between 0 and 1 to be applied to all model. If None aedt opacity will be applied to each object. 

**array_coordinates**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of array element centers. The modeler objects will be duplicated and translated. List of [[x1,y1,z1], [x2,y2,z2]…]. 

**generate_mesh**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to generate the mesh after importing objects. The default is `True`. 

**get_objects_from_aedt**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export objects from AEDT and initialize them. The default is `True`. 

Returns: 
     

`ansys.aedt.core.generic.plot.ModelPlotter`
    
Model Object.
Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.get_model_plotter_geometries(objects=["Box1"], plot_as_separate_objects=True)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_icepak.PostProcessorIcepak.get_model_plotter_geometries.rst.txt)

# get_model_plotter_geometries 

PostProcessorIcepak.get_model_plotter_geometries(_objects : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _plot_as_separate_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _plot_air_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _force_opacity_value : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _array_coordinates : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]] = None_, _generate_mesh : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _get_objects_from_aedt : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [ModelPlotter](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter") 
    
Initialize the Model Plotter object with actual modeler objects and return it. 

Parameters: 
     

**objects**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Optional list of objects to plot. If None all objects will be exported. 

**plot_as_separate_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Plot each object separately. It may require more time to export from AEDT. 

**plot_air_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Plot also air and vacuum objects. 

**force_opacity_value**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Opacity value between 0 and 1 to be applied to all model. If None aedt opacity will be applied to each object. 

**array_coordinates**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of array element centers. The modeler objects will be duplicated and translated. List of [[x1,y1,z1], [x2,y2,z2]…]. 

**generate_mesh**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to generate the mesh after importing objects. The default is `True`. 

**get_objects_from_aedt**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export objects from AEDT and initialize them. The default is `True`. 

Returns: 
     

`ansys.aedt.core.generic.plot.ModelPlotter`
    
Model Object.
Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.get_model_plotter_geometries(objects=["Box1"], plot_as_separate_objects=True)

```
Copy to clipboard