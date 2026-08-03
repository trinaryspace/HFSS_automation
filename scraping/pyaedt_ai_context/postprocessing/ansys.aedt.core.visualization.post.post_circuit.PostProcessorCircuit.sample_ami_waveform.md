---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_circuit.PostProcessorCircuit.sample_ami_waveform.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# sample_ami_waveform 

PostProcessorCircuit.sample_ami_waveform(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _probe : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _source : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _variation_list_w_value : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _unit_interval : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-09_, _ignore_bits : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _plot_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _clock_tics : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Sampling a waveform at clock times plus half unit interval. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

**probe**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the AMI probe. 

**source**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the AMI source. 

**variation_list_w_value**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Variations with relative values. 

**unit_interval**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Unit interval in seconds. The default is `1e-9`. 

**ignore_bits**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of initial bits to ignore. The default is `0`. 

**plot_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report type. The default is `None`, in which case all report types are generated. Options for a specific report type are `"InitialWave"`, `"WaveAfterSource"`, `"WaveAfterChannel"`, and `"WaveAfterProbe"`. 

**clock_tics**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List with clock tics. The default is `None`, in which case the clock tics from the AMI receiver are used. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
Sampled waveform in `Volts` at different times in `seconds`.
Examples

```
>>> circuit = Circuit()
>>> circuit.post.sample_ami_waveform(setupname, probe_name, source_name, circuit.available_variations.nominal)

```
Copy to clipboard
# sample_ami_waveform 

PostProcessorCircuit.sample_ami_waveform(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _probe : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _source : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _variation_list_w_value : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _unit_interval : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-09_, _ignore_bits : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _plot_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _clock_tics : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Sampling a waveform at clock times plus half unit interval. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

**probe**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the AMI probe. 

**source**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the AMI source. 

**variation_list_w_value**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Variations with relative values. 

**unit_interval**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Unit interval in seconds. The default is `1e-9`. 

**ignore_bits**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of initial bits to ignore. The default is `0`. 

**plot_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report type. The default is `None`, in which case all report types are generated. Options for a specific report type are `"InitialWave"`, `"WaveAfterSource"`, `"WaveAfterChannel"`, and `"WaveAfterProbe"`. 

**clock_tics**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List with clock tics. The default is `None`, in which case the clock tics from the AMI receiver are used. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
Sampled waveform in `Volts` at different times in `seconds`.
Examples

```
>>> circuit = Circuit()
>>> circuit.post.sample_ami_waveform(setupname, probe_name, source_name, circuit.available_variations.nominal)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_circuit.PostProcessorCircuit.sample_ami_waveform.rst.txt)

# sample_ami_waveform 

PostProcessorCircuit.sample_ami_waveform(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _probe : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _source : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _variation_list_w_value : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _unit_interval : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-09_, _ignore_bits : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _plot_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _clock_tics : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Sampling a waveform at clock times plus half unit interval. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup. 

**probe**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the AMI probe. 

**source**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the AMI source. 

**variation_list_w_value**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Variations with relative values. 

**unit_interval**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Unit interval in seconds. The default is `1e-9`. 

**ignore_bits**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of initial bits to ignore. The default is `0`. 

**plot_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Report type. The default is `None`, in which case all report types are generated. Options for a specific report type are `"InitialWave"`, `"WaveAfterSource"`, `"WaveAfterChannel"`, and `"WaveAfterProbe"`. 

**clock_tics**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List with clock tics. The default is `None`, in which case the clock tics from the AMI receiver are used. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
Sampled waveform in `Volts` at different times in `seconds`.
Examples

```
>>> circuit = Circuit()
>>> circuit.post.sample_ami_waveform(setupname, probe_name, source_name, circuit.available_variations.nominal)

```
Copy to clipboard