---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.file_utils.tech_to_control_file.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# tech_to_control_file 

ansys.aedt.core.generic.file_utils.tech_to_control_file(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'nm'_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") = None_) 
    
Convert a TECH file to an XML file for use in a GDS or DXF import. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to the TECH file. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Tech units. If specified in tech file this parameter will not be used. Default is `"nm"`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)"), `optional` 
    
Path for outputting the XML file. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Output file path.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import tech_to_control_file
>>> tech_to_control_file(r"C:\Temp\layers.tech")

```
Copy to clipboard
# tech_to_control_file 

ansys.aedt.core.generic.file_utils.tech_to_control_file(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'nm'_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") = None_) 
    
Convert a TECH file to an XML file for use in a GDS or DXF import. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to the TECH file. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Tech units. If specified in tech file this parameter will not be used. Default is `"nm"`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)"), `optional` 
    
Path for outputting the XML file. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Output file path.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import tech_to_control_file
>>> tech_to_control_file(r"C:\Temp\layers.tech")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.file_utils.tech_to_control_file.rst.txt)

# tech_to_control_file 

ansys.aedt.core.generic.file_utils.tech_to_control_file(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'nm'_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") = None_) 
    
Convert a TECH file to an XML file for use in a GDS or DXF import. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to the TECH file. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Tech units. If specified in tech file this parameter will not be used. Default is `"nm"`. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)"), `optional` 
    
Path for outputting the XML file. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Output file path.
Examples

```
>>> from ansys.aedt.core.generic.file_utils import tech_to_control_file
>>> tech_to_control_file(r"C:\Temp\layers.tech")

```
Copy to clipboard