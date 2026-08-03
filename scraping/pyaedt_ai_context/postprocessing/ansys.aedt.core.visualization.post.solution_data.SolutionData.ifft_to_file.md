---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.solution_data.SolutionData.ifft_to_file.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# ifft_to_file 

SolutionData.ifft_to_file(_u_axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '_u'_, _v_axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '_v'_, _coord_system_center : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _db_val : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _num_frames : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _csv_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _csv_file_header : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'res_'_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Save IFFT matrix to a list of CSV files (one per time step). 

Parameters: 
     

**u_axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
U Axis name. Default is Hfss name “_u” 

**v_axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
V Axis name. Default is Hfss name “_v” 

**coord_system_center**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of UV GlobalCS Center. 

**db_val**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether data must be exported into a database. The default is `False`. 

**num_frames**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of frames to export. The default is `None`. 

**csv_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Output path. The default is `None`. 

**csv_file_header**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
CSV file header. The default is `"res_"`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Path to file containing the list of csv files.
Examples

```
>>> from ansys.aedt.core.visualization.post.solution_data import SolutionData
>>> obj = SolutionData()
>>> obj.ifft_to_file(u_axis=["Box1"], v_axis=["Box1"])

```
Copy to clipboard
# ifft_to_file 

SolutionData.ifft_to_file(_u_axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '_u'_, _v_axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '_v'_, _coord_system_center : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _db_val : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _num_frames : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _csv_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _csv_file_header : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'res_'_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Save IFFT matrix to a list of CSV files (one per time step). 

Parameters: 
     

**u_axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
U Axis name. Default is Hfss name “_u” 

**v_axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
V Axis name. Default is Hfss name “_v” 

**coord_system_center**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of UV GlobalCS Center. 

**db_val**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether data must be exported into a database. The default is `False`. 

**num_frames**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of frames to export. The default is `None`. 

**csv_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Output path. The default is `None`. 

**csv_file_header**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
CSV file header. The default is `"res_"`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Path to file containing the list of csv files.
Examples

```
>>> from ansys.aedt.core.visualization.post.solution_data import SolutionData
>>> obj = SolutionData()
>>> obj.ifft_to_file(u_axis=["Box1"], v_axis=["Box1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.solution_data.SolutionData.ifft_to_file.rst.txt)

# ifft_to_file 

SolutionData.ifft_to_file(_u_axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '_u'_, _v_axis : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '_v'_, _coord_system_center : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _db_val : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _num_frames : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _csv_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _csv_file_header : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'res_'_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Save IFFT matrix to a list of CSV files (one per time step). 

Parameters: 
     

**u_axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
U Axis name. Default is Hfss name “_u” 

**v_axis**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
V Axis name. Default is Hfss name “_v” 

**coord_system_center**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of UV GlobalCS Center. 

**db_val**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether data must be exported into a database. The default is `False`. 

**num_frames**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of frames to export. The default is `None`. 

**csv_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Output path. The default is `None`. 

**csv_file_header**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
CSV file header. The default is `"res_"`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Path to file containing the list of csv files.
Examples

```
>>> from ansys.aedt.core.visualization.post.solution_data import SolutionData
>>> obj = SolutionData()
>>> obj.ifft_to_file(u_axis=["Box1"], v_axis=["Box1"])

```
Copy to clipboard