---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_icepak.PostProcessorIcepak.create_fieldplot_line.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# create_fieldplot_line 

PostProcessorIcepak.create_fieldplot_line(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]_, _quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _intrinsics : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _field_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'DC R/L Fields'_) → [FieldPlot](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.html#ansys.aedt.core.visualization.post.field_data.FieldPlot "ansys.aedt.core.visualization.post.field_data.FieldPlot") 
    
Create a field plot of the line. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of polylines to plot. 

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the quantity to plot. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string. If it is a dictionary, keys depend on the solution type and can be expressed in lower or camel case as: - `"Freq"` or `"Frequency"`. - `"Time"`. - `"Phase"`. If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the field plot to create. 

**field_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Field type to plot. Valid only for Q3D Field plots. 

Returns: 
     

[`type`](https://docs.python.org/3.11/library/functions.html#type "\(in Python v3.11\)")
    
Plot object.
References

```
>>> oModule.CreateFieldPlot

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> # Intrinsics is provided as a dictionary.
>>> intrinsics = {"Freq": "5GHz", "Phase": "180deg"}
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name, intrinsics=intrinsics)
>>> plot1 = aedtapp.post.create_fieldplot_line("Polyline1", quantity_name, setup_name, intrinsics=intrinsics)
>>> # Intrinsics is provided as a string. Phase is automatically assigned to 0deg.
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name, intrinsics="5GHz")
>>> plot1 = aedtapp.post.create_fieldplot_line("Polyline1", quantity_name, setup_name, intrinsics="5GHz")
>>> # Intrinsics is provided as a dictionary. Phase is automatically assigned to 0deg.
>>> intrinsics = {"Freq": "5GHz"}
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name, intrinsics=intrinsics)
>>> plot1 = aedtapp.post.create_fieldplot_line("Polyline1", quantity_name, setup_name, intrinsics=intrinsics)
>>> # Intrinsics is not provided and is computed from the setup.
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name)
>>> plot1 = aedtapp.post.create_fieldplot_line("Polyline1", quantity_name, setup_name)

```
Copy to clipboard
# create_fieldplot_line 

PostProcessorIcepak.create_fieldplot_line(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]_, _quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _intrinsics : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _field_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'DC R/L Fields'_) → [FieldPlot](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.html#ansys.aedt.core.visualization.post.field_data.FieldPlot "ansys.aedt.core.visualization.post.field_data.FieldPlot") 
    
Create a field plot of the line. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of polylines to plot. 

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the quantity to plot. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string. If it is a dictionary, keys depend on the solution type and can be expressed in lower or camel case as: - `"Freq"` or `"Frequency"`. - `"Time"`. - `"Phase"`. If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the field plot to create. 

**field_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Field type to plot. Valid only for Q3D Field plots. 

Returns: 
     

[`type`](https://docs.python.org/3.11/library/functions.html#type "\(in Python v3.11\)")
    
Plot object.
References

```
>>> oModule.CreateFieldPlot

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> # Intrinsics is provided as a dictionary.
>>> intrinsics = {"Freq": "5GHz", "Phase": "180deg"}
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name, intrinsics=intrinsics)
>>> plot1 = aedtapp.post.create_fieldplot_line("Polyline1", quantity_name, setup_name, intrinsics=intrinsics)
>>> # Intrinsics is provided as a string. Phase is automatically assigned to 0deg.
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name, intrinsics="5GHz")
>>> plot1 = aedtapp.post.create_fieldplot_line("Polyline1", quantity_name, setup_name, intrinsics="5GHz")
>>> # Intrinsics is provided as a dictionary. Phase is automatically assigned to 0deg.
>>> intrinsics = {"Freq": "5GHz"}
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name, intrinsics=intrinsics)
>>> plot1 = aedtapp.post.create_fieldplot_line("Polyline1", quantity_name, setup_name, intrinsics=intrinsics)
>>> # Intrinsics is not provided and is computed from the setup.
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name)
>>> plot1 = aedtapp.post.create_fieldplot_line("Polyline1", quantity_name, setup_name)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_icepak.PostProcessorIcepak.create_fieldplot_line.rst.txt)

# create_fieldplot_line 

PostProcessorIcepak.create_fieldplot_line(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]_, _quantity : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _intrinsics : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _field_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'DC R/L Fields'_) → [FieldPlot](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.html#ansys.aedt.core.visualization.post.field_data.FieldPlot "ansys.aedt.core.visualization.post.field_data.FieldPlot") 
    
Create a field plot of the line. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of polylines to plot. 

**quantity**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the quantity to plot. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the `nominal_adaptive` setup is used. Be sure to build a setup string in the form of `"SetupName : SetupSweep"`, where `SetupSweep` is the sweep name to use in the export or `LastAdaptive`. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Intrinsic variables required to compute the field before the export. These are typically: frequency, time and phase. It can be provided either as a dictionary or as a string. If it is a dictionary, keys depend on the solution type and can be expressed in lower or camel case as: - `"Freq"` or `"Frequency"`. - `"Time"`. - `"Phase"`. If it is a string, it can either be `"Freq"` or `"Time"` depending on the solution type. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the field plot to create. 

**field_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Field type to plot. Valid only for Q3D Field plots. 

Returns: 
     

[`type`](https://docs.python.org/3.11/library/functions.html#type "\(in Python v3.11\)")
    
Plot object.
References

```
>>> oModule.CreateFieldPlot

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> # Intrinsics is provided as a dictionary.
>>> intrinsics = {"Freq": "5GHz", "Phase": "180deg"}
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name, intrinsics=intrinsics)
>>> plot1 = aedtapp.post.create_fieldplot_line("Polyline1", quantity_name, setup_name, intrinsics=intrinsics)
>>> # Intrinsics is provided as a string. Phase is automatically assigned to 0deg.
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name, intrinsics="5GHz")
>>> plot1 = aedtapp.post.create_fieldplot_line("Polyline1", quantity_name, setup_name, intrinsics="5GHz")
>>> # Intrinsics is provided as a dictionary. Phase is automatically assigned to 0deg.
>>> intrinsics = {"Freq": "5GHz"}
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name, intrinsics=intrinsics)
>>> plot1 = aedtapp.post.create_fieldplot_line("Polyline1", quantity_name, setup_name, intrinsics=intrinsics)
>>> # Intrinsics is not provided and is computed from the setup.
>>> min_value = aedtapp.post.get_scalar_field_value(quantity_name, "Minimum", setup_name)
>>> plot1 = aedtapp.post.create_fieldplot_line("Polyline1", quantity_name, setup_name)

```
Copy to clipboard