---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_icepak.PostProcessorIcepak.get_fans_operating_point.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# get_fans_operating_point 

PostProcessorIcepak.get_fans_operating_point(_export_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _setup_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _time_step : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get the operating point of the fans in the design. 

Parameters: 
     

**export_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the file to save the operating point of the fans to. The default is `None`, in which case the filename is automatically generated. 

**setup_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Setup name to determine the operating point of the fans. The default is `None`, in which case the first available setup is used. 

**time_step**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Time, with units, at which to determine the operating point of the fans. The default is `None`, in which case the first available timestep is used. This parameter is only relevant in transient simulations. 

**variation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Design variation to determine the operating point of the fans from. The default is `None`, in which case the nominal variation is used. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
First element of the list is the CSV filename. The second and third elements are the quantities with units describing the operating point of the fans. The fourth element is a dictionary with the names of the fan instances as keys and lists with volumetric flow rates and pressure rise floats associated with the operating point as values.
References

```
>>> oModule.ExportFanOperatingPoint

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Icepak
>>> ipk = Icepak()
>>> ipk.create_fan()
>>> filename, vol_flow_name, p_rise_name, op_dict = ipk.get_fans_operating_point()

```
Copy to clipboard
# get_fans_operating_point 

PostProcessorIcepak.get_fans_operating_point(_export_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _setup_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _time_step : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get the operating point of the fans in the design. 

Parameters: 
     

**export_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the file to save the operating point of the fans to. The default is `None`, in which case the filename is automatically generated. 

**setup_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Setup name to determine the operating point of the fans. The default is `None`, in which case the first available setup is used. 

**time_step**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Time, with units, at which to determine the operating point of the fans. The default is `None`, in which case the first available timestep is used. This parameter is only relevant in transient simulations. 

**variation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Design variation to determine the operating point of the fans from. The default is `None`, in which case the nominal variation is used. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
First element of the list is the CSV filename. The second and third elements are the quantities with units describing the operating point of the fans. The fourth element is a dictionary with the names of the fan instances as keys and lists with volumetric flow rates and pressure rise floats associated with the operating point as values.
References

```
>>> oModule.ExportFanOperatingPoint

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Icepak
>>> ipk = Icepak()
>>> ipk.create_fan()
>>> filename, vol_flow_name, p_rise_name, op_dict = ipk.get_fans_operating_point()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_icepak.PostProcessorIcepak.get_fans_operating_point.rst.txt)

# get_fans_operating_point 

PostProcessorIcepak.get_fans_operating_point(_export_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _setup_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _time_step : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _variation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get the operating point of the fans in the design. 

Parameters: 
     

**export_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the file to save the operating point of the fans to. The default is `None`, in which case the filename is automatically generated. 

**setup_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Setup name to determine the operating point of the fans. The default is `None`, in which case the first available setup is used. 

**time_step**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Time, with units, at which to determine the operating point of the fans. The default is `None`, in which case the first available timestep is used. This parameter is only relevant in transient simulations. 

**variation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Design variation to determine the operating point of the fans from. The default is `None`, in which case the nominal variation is used. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
First element of the list is the CSV filename. The second and third elements are the quantities with units describing the operating point of the fans. The fourth element is a dictionary with the names of the fan instances as keys and lists with volumetric flow rates and pressure rise floats associated with the operating point as values.
References

```
>>> oModule.ExportFanOperatingPoint

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Icepak
>>> ipk = Icepak()
>>> ipk.create_fan()
>>> filename, vol_flow_name, p_rise_name, op_dict = ipk.get_fans_operating_point()

```
Copy to clipboard