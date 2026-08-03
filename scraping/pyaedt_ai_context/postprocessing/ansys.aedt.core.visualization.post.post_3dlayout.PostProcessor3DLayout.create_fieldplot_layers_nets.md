---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_3dlayout.PostProcessor3DLayout.create_fieldplot_layers_nets.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# create_fieldplot_layers_nets 

PostProcessor3DLayout.create_fieldplot_layers_nets(_layers_nets : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _intrinsics : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _plot_on_surface : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [FieldPlot](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.html#ansys.aedt.core.visualization.post.field_data.FieldPlot "ansys.aedt.core.visualization.post.field_data.FieldPlot") 
    
Create a field plot of stacked layer plot on specified matrix of layers and nets.
This plot is valid from AEDT 2023 R2 and later in HFSS 3D Layout and any modeler where a layout component is used. 

Parameters: 
     

**layers_nets**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of layers and nets to plot. For example: `[["Layer1", "GND", "PWR"], ["Layer2", "VCC"], ...]`. If `"no-layer"` is provided as first argument, all layers are considered. If `"no-net"` is provided or the list contains only layer name, all the nets are automatically considered. 

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the quantity to plot. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Make sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string. If it is a dictionary, keys depend on the solution type and can be expressed in lower or camel case as:
  * `"Freq"` or `"Frequency"`.
  * `"Time"`.
  * `"Phase"`.

If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**plot_on_surface**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if the plot has to be on surfaces or inside the objects. It is applicable only to layout components. Default is `True`. 

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
>>> from ansys.aedt.core.visualization.post.post_3dlayout import PostProcessor3DLayout
>>> obj = PostProcessor3DLayout()
>>> obj.create_fieldplot_layers_nets(layers_nets=["TOP"], quantity=1)

```
Copy to clipboard
# create_fieldplot_layers_nets 

PostProcessor3DLayout.create_fieldplot_layers_nets(_layers_nets : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _intrinsics : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _plot_on_surface : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [FieldPlot](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.html#ansys.aedt.core.visualization.post.field_data.FieldPlot "ansys.aedt.core.visualization.post.field_data.FieldPlot") 
    
Create a field plot of stacked layer plot on specified matrix of layers and nets.
This plot is valid from AEDT 2023 R2 and later in HFSS 3D Layout and any modeler where a layout component is used. 

Parameters: 
     

**layers_nets**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of layers and nets to plot. For example: `[["Layer1", "GND", "PWR"], ["Layer2", "VCC"], ...]`. If `"no-layer"` is provided as first argument, all layers are considered. If `"no-net"` is provided or the list contains only layer name, all the nets are automatically considered. 

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the quantity to plot. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Make sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string. If it is a dictionary, keys depend on the solution type and can be expressed in lower or camel case as:
  * `"Freq"` or `"Frequency"`.
  * `"Time"`.
  * `"Phase"`.

If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**plot_on_surface**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if the plot has to be on surfaces or inside the objects. It is applicable only to layout components. Default is `True`. 

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
>>> from ansys.aedt.core.visualization.post.post_3dlayout import PostProcessor3DLayout
>>> obj = PostProcessor3DLayout()
>>> obj.create_fieldplot_layers_nets(layers_nets=["TOP"], quantity=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_3dlayout.PostProcessor3DLayout.create_fieldplot_layers_nets.rst.txt)

# create_fieldplot_layers_nets 

PostProcessor3DLayout.create_fieldplot_layers_nets(_layers_nets : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _intrinsics : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _plot_on_surface : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [FieldPlot](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.html#ansys.aedt.core.visualization.post.field_data.FieldPlot "ansys.aedt.core.visualization.post.field_data.FieldPlot") 
    
Create a field plot of stacked layer plot on specified matrix of layers and nets.
This plot is valid from AEDT 2023 R2 and later in HFSS 3D Layout and any modeler where a layout component is used. 

Parameters: 
     

**layers_nets**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of layers and nets to plot. For example: `[["Layer1", "GND", "PWR"], ["Layer2", "VCC"], ...]`. If `"no-layer"` is provided as first argument, all layers are considered. If `"no-net"` is provided or the list contains only layer name, all the nets are automatically considered. 

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the quantity to plot. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Make sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string. If it is a dictionary, keys depend on the solution type and can be expressed in lower or camel case as:
  * `"Freq"` or `"Frequency"`.
  * `"Time"`.
  * `"Phase"`.

If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**plot_on_surface**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether if the plot has to be on surfaces or inside the objects. It is applicable only to layout components. Default is `True`. 

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
>>> from ansys.aedt.core.visualization.post.post_3dlayout import PostProcessor3DLayout
>>> obj = PostProcessor3DLayout()
>>> obj.create_fieldplot_layers_nets(layers_nets=["TOP"], quantity=1)

```
Copy to clipboard