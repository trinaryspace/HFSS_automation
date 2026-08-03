---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.misc.convert_nearfield_data.html"
category: "advanced_visualization"
domain: "PyAEDT / HFSS"
---

# convert_nearfield_data 

ansys.aedt.core.visualization.advanced.misc.convert_nearfield_data(_dat_folder : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _frequency : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 6_, _invert_phase_for_lower_faces : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _output_folder : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Convert a near field data folder to hfss nfd file and link it to and file. 

Parameters: 
     

**dat_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the folder containing near fields data. Folder will contain 24 files in the following format: data_Ex_ymin.dat. Same for H Fields. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Frequency in GHz. 

**invert_phase_for_lower_faces**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Add 180 deg for all fields at ‘negative’ faces (xmin, ymin, zmin). 

**output_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Output folder where files will be saved. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Full path to .and file.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.misc import convert_nearfield_data
>>> convert_nearfield_data(dat_folder="example.txt")

```
Copy to clipboard
# convert_nearfield_data 

ansys.aedt.core.visualization.advanced.misc.convert_nearfield_data(_dat_folder : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _frequency : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 6_, _invert_phase_for_lower_faces : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _output_folder : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Convert a near field data folder to hfss nfd file and link it to and file. 

Parameters: 
     

**dat_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the folder containing near fields data. Folder will contain 24 files in the following format: data_Ex_ymin.dat. Same for H Fields. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Frequency in GHz. 

**invert_phase_for_lower_faces**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Add 180 deg for all fields at ‘negative’ faces (xmin, ymin, zmin). 

**output_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Output folder where files will be saved. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Full path to .and file.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.misc import convert_nearfield_data
>>> convert_nearfield_data(dat_folder="example.txt")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.advanced.misc.convert_nearfield_data.rst.txt)

# convert_nearfield_data 

ansys.aedt.core.visualization.advanced.misc.convert_nearfield_data(_dat_folder : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _frequency : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 6_, _invert_phase_for_lower_faces : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _output_folder : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Convert a near field data folder to hfss nfd file and link it to and file. 

Parameters: 
     

**dat_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the folder containing near fields data. Folder will contain 24 files in the following format: data_Ex_ymin.dat. Same for H Fields. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Frequency in GHz. 

**invert_phase_for_lower_faces**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Add 180 deg for all fields at ‘negative’ faces (xmin, ymin, zmin). 

**output_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Output folder where files will be saved. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Full path to .and file.
Examples

```
>>> from ansys.aedt.core.visualization.advanced.misc import convert_nearfield_data
>>> convert_nearfield_data(dat_folder="example.txt")

```
Copy to clipboard