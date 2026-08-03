---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.syslib.nastran_import.nastran_to_stl.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# nastran_to_stl 

ansys.aedt.core.syslib.nastran_import.nastran_to_stl(_* args_, _** kwargs_) 
    
Convert a Nastran file to STL format. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the input Nastran file. 

**output_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path to the output folder where the STL files will be saved. If `None`, the directory of the input file is used. 

**decimation**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
The decimation factor for mesh simplification. Default is `0` (no decimation). 

**enable_planar_merge**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to enable or not planar merge. It can be `"True"`, `"False"` or `"Auto"`. `"Auto"` will disable the planar merge if stl contains more than 50000 triangles. 

**preview**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to generate a preview of the STL files using PyVista. Default is `False`. 

**remove_multiple_connections**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to remove multiple connections in the mesh. Default is `False`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
     

A tuple containing:
    
  * A list of paths to the generated STL files.
  * A dictionary representing the parsed Nastran data.
  * A boolean indicating whether planar merging was enabled.

Examples

```
>>> from ansys.aedt.core.syslib.nastran_import import nastran_to_stl
>>> nastran_to_stl(input_file="my_file.nas", decimation=0, preview=True)

```
Copy to clipboard
# nastran_to_stl 

ansys.aedt.core.syslib.nastran_import.nastran_to_stl(_* args_, _** kwargs_) 
    
Convert a Nastran file to STL format. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the input Nastran file. 

**output_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path to the output folder where the STL files will be saved. If `None`, the directory of the input file is used. 

**decimation**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
The decimation factor for mesh simplification. Default is `0` (no decimation). 

**enable_planar_merge**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to enable or not planar merge. It can be `"True"`, `"False"` or `"Auto"`. `"Auto"` will disable the planar merge if stl contains more than 50000 triangles. 

**preview**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to generate a preview of the STL files using PyVista. Default is `False`. 

**remove_multiple_connections**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to remove multiple connections in the mesh. Default is `False`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
     

A tuple containing:
    
  * A list of paths to the generated STL files.
  * A dictionary representing the parsed Nastran data.
  * A boolean indicating whether planar merging was enabled.

Examples

```
>>> from ansys.aedt.core.syslib.nastran_import import nastran_to_stl
>>> nastran_to_stl(input_file="my_file.nas", decimation=0, preview=True)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.syslib.nastran_import.nastran_to_stl.rst.txt)

# nastran_to_stl 

ansys.aedt.core.syslib.nastran_import.nastran_to_stl(_* args_, _** kwargs_) 
    
Convert a Nastran file to STL format. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the input Nastran file. 

**output_folder**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Path to the output folder where the STL files will be saved. If `None`, the directory of the input file is used. 

**decimation**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
The decimation factor for mesh simplification. Default is `0` (no decimation). 

**enable_planar_merge**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to enable or not planar merge. It can be `"True"`, `"False"` or `"Auto"`. `"Auto"` will disable the planar merge if stl contains more than 50000 triangles. 

**preview**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to generate a preview of the STL files using PyVista. Default is `False`. 

**remove_multiple_connections**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to remove multiple connections in the mesh. Default is `False`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
     

A tuple containing:
    
  * A list of paths to the generated STL files.
  * A dictionary representing the parsed Nastran data.
  * A boolean indicating whether planar merging was enabled.

Examples

```
>>> from ansys.aedt.core.syslib.nastran_import import nastran_to_stl
>>> nastran_to_stl(input_file="my_file.nas", decimation=0, preview=True)

```
Copy to clipboard