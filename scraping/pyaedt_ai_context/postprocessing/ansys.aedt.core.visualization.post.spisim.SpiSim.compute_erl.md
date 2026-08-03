---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.compute_erl.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# compute_erl 

SpiSim.compute_erl(_config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _port_order : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _specify_through_ports : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _bandwidth : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _tdr_duration : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _z_terminations : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _transition_time : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _fixture_delay : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _input_amplitude : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _ber : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _pdf_bin_size : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _signal_loss_factor : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _permitted_reflection : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _reflections_length : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _modulation_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _compute_retries : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 3_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Compute effective return loss (ERL) using Ansys SPISIM from S-parameter file.
Warning
Do not execute this function with untrusted function argument, environment variables or pyaedt global settings. See the [security guide](https://aedt.docs.pyansys.com/version/stable/User_guide/security_consideration.html#ref-security-consideration) for details. 

Parameters: 
     

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Configuration file to use as a reference. The default is `None`, in which case this parameter is ignored. 

**port_order**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to use “`EvenOdd`” or “`Incremental`” numbering for S4P files. The default is `None`. This parameter is ignored if there are more than four ports. 

**specify_through_ports**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Input and output ports to compute the ERL on. Those are ordered like `[inp, inneg, outp, outneg]`. The default is `None`. This parameter is ignored if there are more than four ports. 

**bandwidth**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Application bandwidth in hertz (Hz), which is the inverse of one UI (unit interval). The value can be a float or a string with the unit (“m”, “g”). The default is `30e9`. 

**tdr_duration**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Time domain reflectometry (TDR) duration in seconds, meaning how long the TDR tailed data should be applied. The default is `5`. 

**z_terminations**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Z-terminations (Z11 and Z22) when TDR is calculated. The default is `50`. 

**transition_time**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Transition time: how fast (slew rate) input pulse transit from 0 to Vcc volt. The default is “`10p`”. 

**fixture_delay**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Fixture delay: delay when input starts transition from 0 to Vcc. The default is `500e-12`. 

**input_amplitude**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Input amplitude: Vcc volt of step input. The default is `1.0`. 

**ber**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Specified BER: At what threshold ERL is calculated. The default is `1e-4`. 

**pdf_bin_size**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
PDF bin size: how to quantize the superimposed value. The default is `1e-5`. 

**signal_loss_factor**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Signal loss factor (Beta). For more information, see the SPISIM Help. The default is `1.7e9`. 

**permitted_reflection**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Permitted reflection (Rho). For more information, see the SPISIM Help. The default is `0.18`. 

**reflections_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Length of the reflections: how many UI will be used to calculate ERL. The default is `1000`. 

**modulation_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Modulations type: signal modulation type “`NRZ`” or “`PAM4`”. The default is “`NRZ`”. 

**compute_retries**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of retries to compute ERL. The default is `3`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Effective return loss from the SPISIM executable command, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.post.spisim import SpiSim
>>> obj = SpiSim()
>>> obj.compute_erl(config_file="example.cfg", port_order="EvenOdd")

```
Copy to clipboard
# compute_erl 

SpiSim.compute_erl(_config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _port_order : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _specify_through_ports : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _bandwidth : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _tdr_duration : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _z_terminations : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _transition_time : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _fixture_delay : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _input_amplitude : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _ber : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _pdf_bin_size : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _signal_loss_factor : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _permitted_reflection : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _reflections_length : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _modulation_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _compute_retries : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 3_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Compute effective return loss (ERL) using Ansys SPISIM from S-parameter file.
Warning
Do not execute this function with untrusted function argument, environment variables or pyaedt global settings. See the [security guide](https://aedt.docs.pyansys.com/version/stable/User_guide/security_consideration.html#ref-security-consideration) for details. 

Parameters: 
     

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Configuration file to use as a reference. The default is `None`, in which case this parameter is ignored. 

**port_order**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to use “`EvenOdd`” or “`Incremental`” numbering for S4P files. The default is `None`. This parameter is ignored if there are more than four ports. 

**specify_through_ports**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Input and output ports to compute the ERL on. Those are ordered like `[inp, inneg, outp, outneg]`. The default is `None`. This parameter is ignored if there are more than four ports. 

**bandwidth**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Application bandwidth in hertz (Hz), which is the inverse of one UI (unit interval). The value can be a float or a string with the unit (“m”, “g”). The default is `30e9`. 

**tdr_duration**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Time domain reflectometry (TDR) duration in seconds, meaning how long the TDR tailed data should be applied. The default is `5`. 

**z_terminations**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Z-terminations (Z11 and Z22) when TDR is calculated. The default is `50`. 

**transition_time**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Transition time: how fast (slew rate) input pulse transit from 0 to Vcc volt. The default is “`10p`”. 

**fixture_delay**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Fixture delay: delay when input starts transition from 0 to Vcc. The default is `500e-12`. 

**input_amplitude**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Input amplitude: Vcc volt of step input. The default is `1.0`. 

**ber**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Specified BER: At what threshold ERL is calculated. The default is `1e-4`. 

**pdf_bin_size**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
PDF bin size: how to quantize the superimposed value. The default is `1e-5`. 

**signal_loss_factor**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Signal loss factor (Beta). For more information, see the SPISIM Help. The default is `1.7e9`. 

**permitted_reflection**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Permitted reflection (Rho). For more information, see the SPISIM Help. The default is `0.18`. 

**reflections_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Length of the reflections: how many UI will be used to calculate ERL. The default is `1000`. 

**modulation_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Modulations type: signal modulation type “`NRZ`” or “`PAM4`”. The default is “`NRZ`”. 

**compute_retries**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of retries to compute ERL. The default is `3`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Effective return loss from the SPISIM executable command, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.post.spisim import SpiSim
>>> obj = SpiSim()
>>> obj.compute_erl(config_file="example.cfg", port_order="EvenOdd")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.compute_erl.rst.txt)

# compute_erl 

SpiSim.compute_erl(_config_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _port_order : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _specify_through_ports : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _bandwidth : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _tdr_duration : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _z_terminations : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _transition_time : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _fixture_delay : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _input_amplitude : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _ber : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _pdf_bin_size : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _signal_loss_factor : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _permitted_reflection : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _reflections_length : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _modulation_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _compute_retries : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 3_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Compute effective return loss (ERL) using Ansys SPISIM from S-parameter file.
Warning
Do not execute this function with untrusted function argument, environment variables or pyaedt global settings. See the [security guide](https://aedt.docs.pyansys.com/version/stable/User_guide/security_consideration.html#ref-security-consideration) for details. 

Parameters: 
     

**config_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Configuration file to use as a reference. The default is `None`, in which case this parameter is ignored. 

**port_order**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to use “`EvenOdd`” or “`Incremental`” numbering for S4P files. The default is `None`. This parameter is ignored if there are more than four ports. 

**specify_through_ports**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
Input and output ports to compute the ERL on. Those are ordered like `[inp, inneg, outp, outneg]`. The default is `None`. This parameter is ignored if there are more than four ports. 

**bandwidth**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Application bandwidth in hertz (Hz), which is the inverse of one UI (unit interval). The value can be a float or a string with the unit (“m”, “g”). The default is `30e9`. 

**tdr_duration**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Time domain reflectometry (TDR) duration in seconds, meaning how long the TDR tailed data should be applied. The default is `5`. 

**z_terminations**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Z-terminations (Z11 and Z22) when TDR is calculated. The default is `50`. 

**transition_time**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Transition time: how fast (slew rate) input pulse transit from 0 to Vcc volt. The default is “`10p`”. 

**fixture_delay**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Fixture delay: delay when input starts transition from 0 to Vcc. The default is `500e-12`. 

**input_amplitude**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Input amplitude: Vcc volt of step input. The default is `1.0`. 

**ber**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Specified BER: At what threshold ERL is calculated. The default is `1e-4`. 

**pdf_bin_size**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
PDF bin size: how to quantize the superimposed value. The default is `1e-5`. 

**signal_loss_factor**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Signal loss factor (Beta). For more information, see the SPISIM Help. The default is `1.7e9`. 

**permitted_reflection**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Permitted reflection (Rho). For more information, see the SPISIM Help. The default is `0.18`. 

**reflections_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Length of the reflections: how many UI will be used to calculate ERL. The default is `1000`. 

**modulation_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Modulations type: signal modulation type “`NRZ`” or “`PAM4`”. The default is “`NRZ`”. 

**compute_retries**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of retries to compute ERL. The default is `3`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Effective return loss from the SPISIM executable command, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.post.spisim import SpiSim
>>> obj = SpiSim()
>>> obj.compute_erl(config_file="example.cfg", port_order="EvenOdd")

```
Copy to clipboard