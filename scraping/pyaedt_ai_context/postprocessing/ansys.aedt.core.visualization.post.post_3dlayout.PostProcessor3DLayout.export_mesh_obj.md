---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_3dlayout.PostProcessor3DLayout.export_mesh_obj.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# export_mesh_obj 

PostProcessor3DLayout.export_mesh_obj(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _intrinsics : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _export_air_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _on_surfaces : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Export the mesh in AEDTPLT format.
The mesh has to be available in the selected setup. If a parametric model is provided, you can choose the mesh to export by providing a specific set of variations. This method applies only to `Hfss`, `Q3d`, `Q2D`, `Maxwell3d`, `Maxwell2d`, `Icepak` and `Mechanical` objects. This method is calling `create_fieldplot_surface` to create a mesh plot and `export_field_plot` to export it as `aedtplt` file. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string. If it is a dictionary, keys depend on the solution type and can be expressed in lower or camel case as: - `"Freq"` or `"Frequency"`. - `"Time"`. - `"Phase"`. If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**export_air_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to include vacuum objects for the copied objects. The default is `False`. 

**on_surfaces**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create a mesh on surfaces or on the volume. The default is `True`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
File Generated with full path.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.analyze()
>>> # Export report using defaults.
>>> hfss.post.export_mesh_obj(setup=None, intrinsics=None)
>>> # Export report using arguments.
>>> hfss.post.export_mesh_obj(setup="MySetup : LastAdaptive", intrinsics={"w1": "5mm", "l1": "3mm"})

```
Copy to clipboard
# export_mesh_obj 

PostProcessor3DLayout.export_mesh_obj(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _intrinsics : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _export_air_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _on_surfaces : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Export the mesh in AEDTPLT format.
The mesh has to be available in the selected setup. If a parametric model is provided, you can choose the mesh to export by providing a specific set of variations. This method applies only to `Hfss`, `Q3d`, `Q2D`, `Maxwell3d`, `Maxwell2d`, `Icepak` and `Mechanical` objects. This method is calling `create_fieldplot_surface` to create a mesh plot and `export_field_plot` to export it as `aedtplt` file. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string. If it is a dictionary, keys depend on the solution type and can be expressed in lower or camel case as: - `"Freq"` or `"Frequency"`. - `"Time"`. - `"Phase"`. If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**export_air_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to include vacuum objects for the copied objects. The default is `False`. 

**on_surfaces**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create a mesh on surfaces or on the volume. The default is `True`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
File Generated with full path.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.analyze()
>>> # Export report using defaults.
>>> hfss.post.export_mesh_obj(setup=None, intrinsics=None)
>>> # Export report using arguments.
>>> hfss.post.export_mesh_obj(setup="MySetup : LastAdaptive", intrinsics={"w1": "5mm", "l1": "3mm"})

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_3dlayout.PostProcessor3DLayout.export_mesh_obj.rst.txt)

# export_mesh_obj 

PostProcessor3DLayout.export_mesh_obj(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _intrinsics : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _export_air_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _on_surfaces : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Export the mesh in AEDTPLT format.
The mesh has to be available in the selected setup. If a parametric model is provided, you can choose the mesh to export by providing a specific set of variations. This method applies only to `Hfss`, `Q3d`, `Q2D`, `Maxwell3d`, `Maxwell2d`, `Icepak` and `Mechanical` objects. This method is calling `create_fieldplot_surface` to create a mesh plot and `export_field_plot` to export it as `aedtplt` file. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string. If it is a dictionary, keys depend on the solution type and can be expressed in lower or camel case as: - `"Freq"` or `"Frequency"`. - `"Time"`. - `"Phase"`. If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**export_air_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to include vacuum objects for the copied objects. The default is `False`. 

**on_surfaces**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create a mesh on surfaces or on the volume. The default is `True`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
File Generated with full path.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.analyze()
>>> # Export report using defaults.
>>> hfss.post.export_mesh_obj(setup=None, intrinsics=None)
>>> # Export report using arguments.
>>> hfss.post.export_mesh_obj(setup="MySetup : LastAdaptive", intrinsics={"w1": "5mm", "l1": "3mm"})

```
Copy to clipboard