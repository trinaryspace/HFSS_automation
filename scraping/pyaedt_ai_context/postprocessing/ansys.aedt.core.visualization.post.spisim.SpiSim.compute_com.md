---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.compute_com.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# compute_com 

SpiSim.compute_com(_standard : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _port_order : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'EvenOdd'_, _fext_s4p : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _next_s4p : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _out_folder : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Compute Channel Operating Margin. Only COM ver3.4 is supported.
Warning
Do not execute this function with untrusted function argument, environment variables or pyaedt global settings. See the [security guide](https://aedt.docs.pyansys.com/version/stable/User_guide/security_consideration.html#ref-security-consideration) for details. 

Parameters: 
     

**standard**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Name of the standard to apply. Supported stdnards are as below. COM_CUSTOM = 0 COM_50GAUI_1_C2C = 1 COM_100GAUI_2_C2C = 2 COM_200GAUI_4 = 3 COM_400GAUI_8 = 4 COM_100GBASE_KR4 = 5 COM_100GBASE_KP4 = 6 

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `Path`, `optional` 
    
Config file to use. 

**port_order**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to use “`EvenOdd`” or “`Incremental`” numbering for S4P files. The default is `EvenOdd`. The default is `None`. This parameter is ignored if there are more than four ports. 

**fext_s4p**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Fext touchstone file to use. 

**next_s4p**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Next touchstone file to use. 

**out_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Output folder where to save report. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Examples

```
>>> from ansys.aedt.core.visualization.post.spisim import SpiSim
>>> obj = SpiSim()
>>> obj.compute_com(standard=1, config_file="example.cfg")

```
Copy to clipboard
# compute_com 

SpiSim.compute_com(_standard : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _port_order : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'EvenOdd'_, _fext_s4p : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _next_s4p : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _out_folder : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Compute Channel Operating Margin. Only COM ver3.4 is supported.
Warning
Do not execute this function with untrusted function argument, environment variables or pyaedt global settings. See the [security guide](https://aedt.docs.pyansys.com/version/stable/User_guide/security_consideration.html#ref-security-consideration) for details. 

Parameters: 
     

**standard**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Name of the standard to apply. Supported stdnards are as below. COM_CUSTOM = 0 COM_50GAUI_1_C2C = 1 COM_100GAUI_2_C2C = 2 COM_200GAUI_4 = 3 COM_400GAUI_8 = 4 COM_100GBASE_KR4 = 5 COM_100GBASE_KP4 = 6 

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `Path`, `optional` 
    
Config file to use. 

**port_order**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to use “`EvenOdd`” or “`Incremental`” numbering for S4P files. The default is `EvenOdd`. The default is `None`. This parameter is ignored if there are more than four ports. 

**fext_s4p**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Fext touchstone file to use. 

**next_s4p**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Next touchstone file to use. 

**out_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Output folder where to save report. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Examples

```
>>> from ansys.aedt.core.visualization.post.spisim import SpiSim
>>> obj = SpiSim()
>>> obj.compute_com(standard=1, config_file="example.cfg")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.compute_com.rst.txt)

# compute_com 

SpiSim.compute_com(_standard : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _port_order : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'EvenOdd'_, _fext_s4p : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _next_s4p : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_, _out_folder : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Compute Channel Operating Margin. Only COM ver3.4 is supported.
Warning
Do not execute this function with untrusted function argument, environment variables or pyaedt global settings. See the [security guide](https://aedt.docs.pyansys.com/version/stable/User_guide/security_consideration.html#ref-security-consideration) for details. 

Parameters: 
     

**standard**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Name of the standard to apply. Supported stdnards are as below. COM_CUSTOM = 0 COM_50GAUI_1_C2C = 1 COM_100GAUI_2_C2C = 2 COM_200GAUI_4 = 3 COM_400GAUI_8 = 4 COM_100GBASE_KR4 = 5 COM_100GBASE_KP4 = 6 

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `Path`, `optional` 
    
Config file to use. 

**port_order**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to use “`EvenOdd`” or “`Incremental`” numbering for S4P files. The default is `EvenOdd`. The default is `None`. This parameter is ignored if there are more than four ports. 

**fext_s4p**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Fext touchstone file to use. 

**next_s4p**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Next touchstone file to use. 

**out_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Output folder where to save report. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Examples

```
>>> from ansys.aedt.core.visualization.post.spisim import SpiSim
>>> obj = SpiSim()
>>> obj.compute_com(standard=1, config_file="example.cfg")

```
Copy to clipboard