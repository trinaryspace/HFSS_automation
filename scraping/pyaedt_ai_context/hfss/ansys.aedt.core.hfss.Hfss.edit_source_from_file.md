---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.edit_source_from_file.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# edit_source_from_file 

Hfss.edit_source_from_file(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_time_domain : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _x_scale : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 1_, _y_scale : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 1_, _impedance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 50_, _data_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Power'_, _encoding : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'utf-8'_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'hamming'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Edit a source from file data.
File data is a CSV containing either frequency data or time domain data that will be converted through FFT. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full name of the input file. If `assignment` is `None`, it loads directly the file, in this case the file must have AEDT format. 

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Port name and mode. For example, `"Port1:1"`. The port name must be defined if the solution type is other than Eigenmodal. 

**is_time_domain**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the input data is time-based or frequency-based. Frequency based data are Mag/Phase (deg). 

**x_scale**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
     

Scaling factor for the x axis. This argument is ignored if the algorithm
    
identifies the format from the file header. 

**y_scale**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
     

Scaling factor for the y axis. This argument is ignored if the algorithm
    
identifies the format from the file header. 

**impedance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Excitation impedance. Default is 50. 

**data_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Data format. Options are `"Current"`, `"Power"`, and `"Voltage"`. This argument is ignored if the algoritmm identifies the format from the file header. 

**encoding**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
CSV file encoding. 

**window**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Fft window. Options are `"hamming"`, `"hanning"`, `"blackman"`, `"bartlett"` or `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> box1 = hfss.modeler.create_box([0, 0, 0], [10, 20, 20])
>>> hfss.wave_port(assignment=box1.bottom_face_x, create_port_sheet=False, name="Port1")
>>> hfss.create_setup()
>>> hfss.edit_source_from_file(assignment=hfss.excitation_names[0], input_file="file.csv")

```
Copy to clipboard
# edit_source_from_file 

Hfss.edit_source_from_file(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_time_domain : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _x_scale : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 1_, _y_scale : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 1_, _impedance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 50_, _data_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Power'_, _encoding : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'utf-8'_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'hamming'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Edit a source from file data.
File data is a CSV containing either frequency data or time domain data that will be converted through FFT. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full name of the input file. If `assignment` is `None`, it loads directly the file, in this case the file must have AEDT format. 

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Port name and mode. For example, `"Port1:1"`. The port name must be defined if the solution type is other than Eigenmodal. 

**is_time_domain**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the input data is time-based or frequency-based. Frequency based data are Mag/Phase (deg). 

**x_scale**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
     

Scaling factor for the x axis. This argument is ignored if the algorithm
    
identifies the format from the file header. 

**y_scale**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
     

Scaling factor for the y axis. This argument is ignored if the algorithm
    
identifies the format from the file header. 

**impedance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Excitation impedance. Default is 50. 

**data_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Data format. Options are `"Current"`, `"Power"`, and `"Voltage"`. This argument is ignored if the algoritmm identifies the format from the file header. 

**encoding**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
CSV file encoding. 

**window**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Fft window. Options are `"hamming"`, `"hanning"`, `"blackman"`, `"bartlett"` or `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> box1 = hfss.modeler.create_box([0, 0, 0], [10, 20, 20])
>>> hfss.wave_port(assignment=box1.bottom_face_x, create_port_sheet=False, name="Port1")
>>> hfss.create_setup()
>>> hfss.edit_source_from_file(assignment=hfss.excitation_names[0], input_file="file.csv")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.edit_source_from_file.rst.txt)

# edit_source_from_file 

Hfss.edit_source_from_file(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_time_domain : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _x_scale : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 1_, _y_scale : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 1_, _impedance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 50_, _data_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'Power'_, _encoding : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'utf-8'_, _window : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'hamming'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Edit a source from file data.
File data is a CSV containing either frequency data or time domain data that will be converted through FFT. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full name of the input file. If `assignment` is `None`, it loads directly the file, in this case the file must have AEDT format. 

**assignment**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Port name and mode. For example, `"Port1:1"`. The port name must be defined if the solution type is other than Eigenmodal. 

**is_time_domain**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the input data is time-based or frequency-based. Frequency based data are Mag/Phase (deg). 

**x_scale**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
     

Scaling factor for the x axis. This argument is ignored if the algorithm
    
identifies the format from the file header. 

**y_scale**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
     

Scaling factor for the y axis. This argument is ignored if the algorithm
    
identifies the format from the file header. 

**impedance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Excitation impedance. Default is 50. 

**data_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Data format. Options are `"Current"`, `"Power"`, and `"Voltage"`. This argument is ignored if the algoritmm identifies the format from the file header. 

**encoding**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
CSV file encoding. 

**window**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Fft window. Options are `"hamming"`, `"hanning"`, `"blackman"`, `"bartlett"` or `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> box1 = hfss.modeler.create_box([0, 0, 0], [10, 20, 20])
>>> hfss.wave_port(assignment=box1.bottom_face_x, create_port_sheet=False, name="Port1")
>>> hfss.create_setup()
>>> hfss.edit_source_from_file(assignment=hfss.excitation_names[0], input_file="file.csv")

```
Copy to clipboard