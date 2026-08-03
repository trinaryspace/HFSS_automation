---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.compute_icn.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# compute_icn 

SpiSim.compute_icn(_config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _port_order : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'EVENODD'_, _next_s4p : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _fext_s4p : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _bandwidth : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _use_pcie_icn : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _compute_retries : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 3_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Compute the integrated crosstalk noise (ICN) in volts using Ansys SPISIM from S-parameter file.
Warning
Do not execute this function with untrusted function argument, environment variables or pyaedt global settings. See the [security guide](https://aedt.docs.pyansys.com/version/stable/User_guide/security_consideration.html#ref-security-consideration) for details. 

Parameters: 
     

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Configuration file to use as a reference. The default is `None`, in which case this parameter is ignored. 

**port_order**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to use “`EvenOdd`” or “`Incremental`” numbering for S4P files. The default is `None`. This parameter is ignored if there are more than four ports. 

**next_s4p**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Near End `s4p` or list of `s4p`. The default is `None`. 

**fext_s4p**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Far End `s4p` or list of `s4p`. The default is `None`. 

**use_pcie_icn**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use `PCIE` or `COM` method to compute `ICN`. The default is `COM`. 

**bandwidth**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Application bandwidth in hertz (Hz), which is the inverse of one UI (unit interval). The value can be a float or a string with the unit (“m”, “g”). The default is `25e9`. 

**compute_retries**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of retries to compute ICN. The default is `3`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
ICN in volts from the SPISIM executable command, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.post.spisim import SpiSim
>>> fext_s4p = "fext_s4p.s4p"
>>> next_s4p = "next_s4p.s4p"
>>> spisim = SpiSim()
>>> spisim.working_directory = test_tmp_dir
>>> icn = spisim.compute_icn(port_order="EvenOdd", fext_s4p=fext_s4p, next_s4p=next_s4p, bandwidth=10e9)

```
Copy to clipboard
# compute_icn 

SpiSim.compute_icn(_config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _port_order : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'EVENODD'_, _next_s4p : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _fext_s4p : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _bandwidth : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _use_pcie_icn : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _compute_retries : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 3_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Compute the integrated crosstalk noise (ICN) in volts using Ansys SPISIM from S-parameter file.
Warning
Do not execute this function with untrusted function argument, environment variables or pyaedt global settings. See the [security guide](https://aedt.docs.pyansys.com/version/stable/User_guide/security_consideration.html#ref-security-consideration) for details. 

Parameters: 
     

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Configuration file to use as a reference. The default is `None`, in which case this parameter is ignored. 

**port_order**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to use “`EvenOdd`” or “`Incremental`” numbering for S4P files. The default is `None`. This parameter is ignored if there are more than four ports. 

**next_s4p**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Near End `s4p` or list of `s4p`. The default is `None`. 

**fext_s4p**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Far End `s4p` or list of `s4p`. The default is `None`. 

**use_pcie_icn**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use `PCIE` or `COM` method to compute `ICN`. The default is `COM`. 

**bandwidth**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Application bandwidth in hertz (Hz), which is the inverse of one UI (unit interval). The value can be a float or a string with the unit (“m”, “g”). The default is `25e9`. 

**compute_retries**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of retries to compute ICN. The default is `3`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
ICN in volts from the SPISIM executable command, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.post.spisim import SpiSim
>>> fext_s4p = "fext_s4p.s4p"
>>> next_s4p = "next_s4p.s4p"
>>> spisim = SpiSim()
>>> spisim.working_directory = test_tmp_dir
>>> icn = spisim.compute_icn(port_order="EvenOdd", fext_s4p=fext_s4p, next_s4p=next_s4p, bandwidth=10e9)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.compute_icn.rst.txt)

# compute_icn 

SpiSim.compute_icn(_config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _port_order : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'EVENODD'_, _next_s4p : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _fext_s4p : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _bandwidth : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _use_pcie_icn : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _compute_retries : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 3_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Compute the integrated crosstalk noise (ICN) in volts using Ansys SPISIM from S-parameter file.
Warning
Do not execute this function with untrusted function argument, environment variables or pyaedt global settings. See the [security guide](https://aedt.docs.pyansys.com/version/stable/User_guide/security_consideration.html#ref-security-consideration) for details. 

Parameters: 
     

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Configuration file to use as a reference. The default is `None`, in which case this parameter is ignored. 

**port_order**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to use “`EvenOdd`” or “`Incremental`” numbering for S4P files. The default is `None`. This parameter is ignored if there are more than four ports. 

**next_s4p**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Near End `s4p` or list of `s4p`. The default is `None`. 

**fext_s4p**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Far End `s4p` or list of `s4p`. The default is `None`. 

**use_pcie_icn**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to use `PCIE` or `COM` method to compute `ICN`. The default is `COM`. 

**bandwidth**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Application bandwidth in hertz (Hz), which is the inverse of one UI (unit interval). The value can be a float or a string with the unit (“m”, “g”). The default is `25e9`. 

**compute_retries**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of retries to compute ICN. The default is `3`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
ICN in volts from the SPISIM executable command, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.post.spisim import SpiSim
>>> fext_s4p = "fext_s4p.s4p"
>>> next_s4p = "next_s4p.s4p"
>>> spisim = SpiSim()
>>> spisim.working_directory = test_tmp_dir
>>> icn = spisim.compute_icn(port_order="EvenOdd", fext_s4p=fext_s4p, next_s4p=next_s4p, bandwidth=10e9)

```
Copy to clipboard