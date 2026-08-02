---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.import_gds_3d.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# import_gds_3d 

Hfss.import_gds_3d(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _mapping_layers : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'um'_, _import_method : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Import a GDSII file. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the GDS file. 

**mapping_layers**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
The dictionary uses GDS layer numbers as keys. Each value is either a tuple containing the elevation and thickness, or a list consisting of that tuple along with a string representing the layer name. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Length unit values. The default is `"um"`. 

**import_method**`integer` , `optional` 
    
GDSII import method. The default is `1`. Options are:
  * `0` for script.
  * `1` for Parasolid.

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful.
References

```
>>> oEditor.ImportGDSII

```
Copy to clipboard
Examples
Import a GDS file in an HFSS 3D project.

```
>>> gds_path = r"gds1.gds"
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> gds_number = {7: (100, 10), 9: [(110, 5), "my_layer"]}
>>> hfss.import_gds_3d(gds_path, gds_number, units="um", import_method=1)

```
Copy to clipboard
# import_gds_3d 

Hfss.import_gds_3d(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _mapping_layers : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'um'_, _import_method : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Import a GDSII file. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the GDS file. 

**mapping_layers**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
The dictionary uses GDS layer numbers as keys. Each value is either a tuple containing the elevation and thickness, or a list consisting of that tuple along with a string representing the layer name. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Length unit values. The default is `"um"`. 

**import_method**`integer` , `optional` 
    
GDSII import method. The default is `1`. Options are:
  * `0` for script.
  * `1` for Parasolid.

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful.
References

```
>>> oEditor.ImportGDSII

```
Copy to clipboard
Examples
Import a GDS file in an HFSS 3D project.

```
>>> gds_path = r"gds1.gds"
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> gds_number = {7: (100, 10), 9: [(110, 5), "my_layer"]}
>>> hfss.import_gds_3d(gds_path, gds_number, units="um", import_method=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.import_gds_3d.rst.txt)

# import_gds_3d 

Hfss.import_gds_3d(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _mapping_layers : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'um'_, _import_method : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Import a GDSII file. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the GDS file. 

**mapping_layers**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
The dictionary uses GDS layer numbers as keys. Each value is either a tuple containing the elevation and thickness, or a list consisting of that tuple along with a string representing the layer name. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Length unit values. The default is `"um"`. 

**import_method**`integer` , `optional` 
    
GDSII import method. The default is `1`. Options are:
  * `0` for script.
  * `1` for Parasolid.

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful.
References

```
>>> oEditor.ImportGDSII

```
Copy to clipboard
Examples
Import a GDS file in an HFSS 3D project.

```
>>> gds_path = r"gds1.gds"
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> gds_number = {7: (100, 10), 9: [(110, 5), "my_layer"]}
>>> hfss.import_gds_3d(gds_path, gds_number, units="um", import_method=1)

```
Copy to clipboard