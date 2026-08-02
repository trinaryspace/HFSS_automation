---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.import_dxf.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# import_dxf 

Hfss.import_dxf(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _layers : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]_, _auto_detect_close : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _self_stitch : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _self_stitch_tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _scale : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.001_, _defeature_geometry : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _defeature_distance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _round_coordinates : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _round_num_digits : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 4_, _write_poly_with_width_as_filled_poly : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _import_method : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = 1_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Import a DXF file. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Path to the DXF file. 

**layers**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of layer names to import. To get the dxf_layers in the DXF file, you can call the `get_dxf_layers` method. 

**auto_detect_close**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to check polylines to see if they are closed. The default is `True`. If a polyline is closed, the modeler creates a polygon in the design. 

**self_stitch**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to join multiple straight line segments to form polylines. The default is `True`. 

**self_stitch_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Self stitch tolerance value. If negative, let importer use its default tolerance. The default is `0`. 

**scale**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Scaling factor. The default is `0.001`. The units are `mm`. 

**defeature_geometry**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to defeature the geometry to reduce complexity. The default is `False`. 

**defeature_distance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Defeature tolerance distance. The default is `0`. 

**round_coordinates**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to round all imported data to the number of decimal points specified by the next parameter. The default is `False`. 

**round_num_digits**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of digits to which to round all imported data. The default is `4`. 

**write_poly_with_width_as_filled_poly**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Imports wide polylines as polygons. The default is `False`. 

**import_method**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the import method is `Script` or `Parasolid`. The default is `1`, which means that the `Parasolid` is used. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.ImportDXF

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.import_dxf("layout.dxf", layers=["Layer1"])

```
Copy to clipboard
# import_dxf 

Hfss.import_dxf(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _layers : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]_, _auto_detect_close : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _self_stitch : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _self_stitch_tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _scale : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.001_, _defeature_geometry : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _defeature_distance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _round_coordinates : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _round_num_digits : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 4_, _write_poly_with_width_as_filled_poly : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _import_method : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = 1_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Import a DXF file. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Path to the DXF file. 

**layers**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of layer names to import. To get the dxf_layers in the DXF file, you can call the `get_dxf_layers` method. 

**auto_detect_close**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to check polylines to see if they are closed. The default is `True`. If a polyline is closed, the modeler creates a polygon in the design. 

**self_stitch**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to join multiple straight line segments to form polylines. The default is `True`. 

**self_stitch_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Self stitch tolerance value. If negative, let importer use its default tolerance. The default is `0`. 

**scale**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Scaling factor. The default is `0.001`. The units are `mm`. 

**defeature_geometry**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to defeature the geometry to reduce complexity. The default is `False`. 

**defeature_distance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Defeature tolerance distance. The default is `0`. 

**round_coordinates**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to round all imported data to the number of decimal points specified by the next parameter. The default is `False`. 

**round_num_digits**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of digits to which to round all imported data. The default is `4`. 

**write_poly_with_width_as_filled_poly**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Imports wide polylines as polygons. The default is `False`. 

**import_method**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the import method is `Script` or `Parasolid`. The default is `1`, which means that the `Parasolid` is used. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.ImportDXF

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.import_dxf("layout.dxf", layers=["Layer1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.import_dxf.rst.txt)

# import_dxf 

Hfss.import_dxf(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")_, _layers : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")]_, _auto_detect_close : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _self_stitch : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _self_stitch_tolerance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _scale : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.001_, _defeature_geometry : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _defeature_distance : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.0_, _round_coordinates : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _round_num_digits : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 4_, _write_poly_with_width_as_filled_poly : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _import_method : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = 1_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Import a DXF file. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Path to the DXF file. 

**layers**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of layer names to import. To get the dxf_layers in the DXF file, you can call the `get_dxf_layers` method. 

**auto_detect_close**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to check polylines to see if they are closed. The default is `True`. If a polyline is closed, the modeler creates a polygon in the design. 

**self_stitch**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to join multiple straight line segments to form polylines. The default is `True`. 

**self_stitch_tolerance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Self stitch tolerance value. If negative, let importer use its default tolerance. The default is `0`. 

**scale**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Scaling factor. The default is `0.001`. The units are `mm`. 

**defeature_geometry**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to defeature the geometry to reduce complexity. The default is `False`. 

**defeature_distance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Defeature tolerance distance. The default is `0`. 

**round_coordinates**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to round all imported data to the number of decimal points specified by the next parameter. The default is `False`. 

**round_num_digits**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of digits to which to round all imported data. The default is `4`. 

**write_poly_with_width_as_filled_poly**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Imports wide polylines as polygons. The default is `False`. 

**import_method**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") or [bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the import method is `Script` or `Parasolid`. The default is `1`, which means that the `Parasolid` is used. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.ImportDXF

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.import_dxf("layout.dxf", layers=["Layer1"])

```
Copy to clipboard