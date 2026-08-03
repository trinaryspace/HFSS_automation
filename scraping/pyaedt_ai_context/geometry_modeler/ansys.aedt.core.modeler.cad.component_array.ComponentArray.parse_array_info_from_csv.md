---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.parse_array_info_from_csv.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# parse_array_info_from_csv 

ComponentArray.parse_array_info_from_csv(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Parse component array information from the CSV file. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the CSV file. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Ordered dictionary of the properties of the component array.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss(project="Array.aedt")
>>> array_names = aedtapp.component_array_names[0]
>>> array = aedtapp.component_array[array_names[0]]
>>> array_csv = array.export_array_info()
>>> array_info = array.array_info_parser(array_csv)

```
Copy to clipboard
# parse_array_info_from_csv 

ComponentArray.parse_array_info_from_csv(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Parse component array information from the CSV file. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the CSV file. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Ordered dictionary of the properties of the component array.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss(project="Array.aedt")
>>> array_names = aedtapp.component_array_names[0]
>>> array = aedtapp.component_array[array_names[0]]
>>> array_csv = array.export_array_info()
>>> array_info = array.array_info_parser(array_csv)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.component_array.ComponentArray.parse_array_info_from_csv.rst.txt)

# parse_array_info_from_csv 

ComponentArray.parse_array_info_from_csv(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Parse component array information from the CSV file. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the CSV file. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Ordered dictionary of the properties of the component array.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss(project="Array.aedt")
>>> array_names = aedtapp.component_array_names[0]
>>> array = aedtapp.component_array[array_names[0]]
>>> array_csv = array.export_array_info()
>>> array_info = array.array_info_parser(array_csv)

```
Copy to clipboard