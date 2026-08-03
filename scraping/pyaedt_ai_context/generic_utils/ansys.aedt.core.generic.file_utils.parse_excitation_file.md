---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.file_utils.parse_excitation_file.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# parse_excitation_file 

ansys.aedt.core.generic.file_utils.parse_excitation_file(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _is_time_domain : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _x_scale : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.0_, _y_scale : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1_, _impedance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 50.0_, _data_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Power'_, _encoding : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'utf-8'_, _out_mag : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Voltage'_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'hamming'_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Parse a csv file and convert data in list that can be applied to Hfss and Hfss3dLayout sources. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full name of the input file. 

**is_time_domain**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if the input data is Time based or Frequency Based. Frequency based data are Mag/Phase (deg). 

**x_scale**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Scaling factor for x axis. 

**y_scale**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Scaling factor for y axis. 

**data_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Either “Power”, “Current” or “Voltage”. 

**impedance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Excitation impedance. Default is 50. 

**encoding**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Csv file encoding. 

**out_mag**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Output magnitude format. It can be “Voltage” or “Power” depending on Hfss solution. 

**window**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Fft window. Options are `"hamming"`, `"hanning"`, `"blackman"`, `"bartlett"` or `None`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Frequency, magnitude and phase.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import parse_excitation_file
>>> parse_excitation_file(r"C:\Temp\source.csv", is_time_domain=True)

```
Copy to clipboard
# parse_excitation_file 

ansys.aedt.core.generic.file_utils.parse_excitation_file(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _is_time_domain : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _x_scale : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.0_, _y_scale : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1_, _impedance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 50.0_, _data_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Power'_, _encoding : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'utf-8'_, _out_mag : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Voltage'_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'hamming'_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Parse a csv file and convert data in list that can be applied to Hfss and Hfss3dLayout sources. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full name of the input file. 

**is_time_domain**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if the input data is Time based or Frequency Based. Frequency based data are Mag/Phase (deg). 

**x_scale**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Scaling factor for x axis. 

**y_scale**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Scaling factor for y axis. 

**data_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Either “Power”, “Current” or “Voltage”. 

**impedance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Excitation impedance. Default is 50. 

**encoding**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Csv file encoding. 

**out_mag**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Output magnitude format. It can be “Voltage” or “Power” depending on Hfss solution. 

**window**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Fft window. Options are `"hamming"`, `"hanning"`, `"blackman"`, `"bartlett"` or `None`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Frequency, magnitude and phase.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import parse_excitation_file
>>> parse_excitation_file(r"C:\Temp\source.csv", is_time_domain=True)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.file_utils.parse_excitation_file.rst.txt)

# parse_excitation_file 

ansys.aedt.core.generic.file_utils.parse_excitation_file(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _is_time_domain : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _x_scale : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1.0_, _y_scale : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1_, _impedance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 50.0_, _data_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Power'_, _encoding : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'utf-8'_, _out_mag : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Voltage'_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'hamming'_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Parse a csv file and convert data in list that can be applied to Hfss and Hfss3dLayout sources. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full name of the input file. 

**is_time_domain**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Either if the input data is Time based or Frequency Based. Frequency based data are Mag/Phase (deg). 

**x_scale**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Scaling factor for x axis. 

**y_scale**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Scaling factor for y axis. 

**data_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Either “Power”, “Current” or “Voltage”. 

**impedance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Excitation impedance. Default is 50. 

**encoding**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Csv file encoding. 

**out_mag**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Output magnitude format. It can be “Voltage” or “Power” depending on Hfss solution. 

**window**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Fft window. Options are `"hamming"`, `"hanning"`, `"blackman"`, `"bartlett"` or `None`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Frequency, magnitude and phase.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import parse_excitation_file
>>> parse_excitation_file(r"C:\Temp\source.csv", is_time_domain=True)

```
Copy to clipboard