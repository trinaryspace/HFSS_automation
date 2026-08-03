---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_common_3d.PostProcessor3D.create_fieldplot_volume.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# create_fieldplot_volume 

PostProcessor3D.create_fieldplot_volume(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]_, _quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _intrinsics : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _field_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'DC R/L Fields'_) → [FieldPlot](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.html#ansys.aedt.core.visualization.post.field_data.FieldPlot "ansys.aedt.core.visualization.post.field_data.FieldPlot") 
    
Create a field plot of volumes. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of volumes to plot. 

**quantity**
    
Name of the quantity to plot. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string. If it is a dictionary, keys depend on the solution type and can be expressed in lower or camel case as: - `"Freq"` or `"Frequency"`. - `"Time"`. - `"Phase"`. If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the field plot to create. 

Returns: 
     

:class:`ansys.aedt.core.modules.solutions.FieldPlot` 
    
Plot object.
References

```
>>> oModule.CreateFieldPlot

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.create_fieldplot_volume(assignment="Box1", quantity=1)

```
Copy to clipboard
# create_fieldplot_volume 

PostProcessor3D.create_fieldplot_volume(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]_, _quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _intrinsics : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _field_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'DC R/L Fields'_) → [FieldPlot](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.html#ansys.aedt.core.visualization.post.field_data.FieldPlot "ansys.aedt.core.visualization.post.field_data.FieldPlot") 
    
Create a field plot of volumes. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of volumes to plot. 

**quantity**
    
Name of the quantity to plot. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string. If it is a dictionary, keys depend on the solution type and can be expressed in lower or camel case as: - `"Freq"` or `"Frequency"`. - `"Time"`. - `"Phase"`. If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the field plot to create. 

Returns: 
     

:class:`ansys.aedt.core.modules.solutions.FieldPlot` 
    
Plot object.
References

```
>>> oModule.CreateFieldPlot

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.create_fieldplot_volume(assignment="Box1", quantity=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_common_3d.PostProcessor3D.create_fieldplot_volume.rst.txt)

# create_fieldplot_volume 

PostProcessor3D.create_fieldplot_volume(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]_, _quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _intrinsics : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _field_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'DC R/L Fields'_) → [FieldPlot](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.html#ansys.aedt.core.visualization.post.field_data.FieldPlot "ansys.aedt.core.visualization.post.field_data.FieldPlot") 
    
Create a field plot of volumes. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of volumes to plot. 

**quantity**
    
Name of the quantity to plot. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string. If it is a dictionary, keys depend on the solution type and can be expressed in lower or camel case as: - `"Freq"` or `"Frequency"`. - `"Time"`. - `"Phase"`. If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the field plot to create. 

Returns: 
     

:class:`ansys.aedt.core.modules.solutions.FieldPlot` 
    
Plot object.
References

```
>>> oModule.CreateFieldPlot

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.create_fieldplot_volume(assignment="Box1", quantity=1)

```
Copy to clipboard