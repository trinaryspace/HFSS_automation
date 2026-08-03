---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_circuit.PostProcessorCircuit.sample_waveform.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# sample_waveform 

PostProcessorCircuit.sample_waveform(_waveform_data : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | Series_, _waveform_sweep : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | Series_, _waveform_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'V'_, _waveform_sweep_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 's'_, _unit_interval : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-09_, _clock_tics : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _pandas_enabled : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | Series 
    
Sampling a waveform at clock times plus half unit interval. 

Parameters: 
     

**waveform_data**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`pandas.Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "\(in pandas v3.0.4\)") 
    
Waveform data. 

**waveform_sweep**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`pandas.Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "\(in pandas v3.0.4\)") 
    
Waveform sweep data. 

**waveform_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Waveform units. The default values is `V`. 

**waveform_sweep_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Time units. The default value is `s`. 

**unit_interval**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Unit interval in seconds. The default is `1e-9`. 

**clock_tics**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List with clock tics. The default is `None`, in which case the clock tics from the AMI receiver are used. 

**pandas_enabled**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable the Pandas data format. The default is `False`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`pandas.Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "\(in pandas v3.0.4\)") 
    
Sampled waveform in `Volts` at different times in `seconds`.
Examples

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> circuit.post.sample_ami_waveform(name, probe_name, source_name, circuit.available_variations.nominal)

```
Copy to clipboard
# sample_waveform 

PostProcessorCircuit.sample_waveform(_waveform_data : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | Series_, _waveform_sweep : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | Series_, _waveform_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'V'_, _waveform_sweep_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 's'_, _unit_interval : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-09_, _clock_tics : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _pandas_enabled : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | Series 
    
Sampling a waveform at clock times plus half unit interval. 

Parameters: 
     

**waveform_data**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`pandas.Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "\(in pandas v3.0.4\)") 
    
Waveform data. 

**waveform_sweep**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`pandas.Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "\(in pandas v3.0.4\)") 
    
Waveform sweep data. 

**waveform_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Waveform units. The default values is `V`. 

**waveform_sweep_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Time units. The default value is `s`. 

**unit_interval**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Unit interval in seconds. The default is `1e-9`. 

**clock_tics**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List with clock tics. The default is `None`, in which case the clock tics from the AMI receiver are used. 

**pandas_enabled**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable the Pandas data format. The default is `False`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`pandas.Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "\(in pandas v3.0.4\)") 
    
Sampled waveform in `Volts` at different times in `seconds`.
Examples

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> circuit.post.sample_ami_waveform(name, probe_name, source_name, circuit.available_variations.nominal)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_circuit.PostProcessorCircuit.sample_waveform.rst.txt)

# sample_waveform 

PostProcessorCircuit.sample_waveform(_waveform_data : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | Series_, _waveform_sweep : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | Series_, _waveform_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'V'_, _waveform_sweep_unit : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 's'_, _unit_interval : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-09_, _clock_tics : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _pandas_enabled : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | Series 
    
Sampling a waveform at clock times plus half unit interval. 

Parameters: 
     

**waveform_data**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`pandas.Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "\(in pandas v3.0.4\)") 
    
Waveform data. 

**waveform_sweep**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`pandas.Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "\(in pandas v3.0.4\)") 
    
Waveform sweep data. 

**waveform_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Waveform units. The default values is `V`. 

**waveform_sweep_unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Time units. The default value is `s`. 

**unit_interval**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Unit interval in seconds. The default is `1e-9`. 

**clock_tics**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List with clock tics. The default is `None`, in which case the clock tics from the AMI receiver are used. 

**pandas_enabled**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable the Pandas data format. The default is `False`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") or [`pandas.Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "\(in pandas v3.0.4\)") 
    
Sampled waveform in `Volts` at different times in `seconds`.
Examples

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> circuit.post.sample_ami_waveform(name, probe_name, source_name, circuit.available_variations.nominal)

```
Copy to clipboard