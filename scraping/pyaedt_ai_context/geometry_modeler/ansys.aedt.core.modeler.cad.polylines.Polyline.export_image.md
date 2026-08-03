---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.Polyline.export_image.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# export_image 

Polyline.export_image(_output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export the current object to a specified file path.
Note
Works from AEDT 2021.2 in CPython only. PyVista has to be installed. 

Parameters: 
     

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)"), `optional` 
    
File name with full path. If None the exported image will be a `png` file that will be saved in `working_directory`. To access the `working_directory` the use `app.working_directory` property. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
File path.
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.export_image(output_file=r"example.txt")

```
Copy to clipboard
# export_image 

Polyline.export_image(_output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export the current object to a specified file path.
Note
Works from AEDT 2021.2 in CPython only. PyVista has to be installed. 

Parameters: 
     

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)"), `optional` 
    
File name with full path. If None the exported image will be a `png` file that will be saved in `working_directory`. To access the `working_directory` the use `app.working_directory` property. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
File path.
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.export_image(output_file=r"example.txt")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.Polyline.export_image.rst.txt)

# export_image 

Polyline.export_image(_output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export the current object to a specified file path.
Note
Works from AEDT 2021.2 in CPython only. PyVista has to be installed. 

Parameters: 
     

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)"), `optional` 
    
File name with full path. If None the exported image will be a `png` file that will be saved in `working_directory`. To access the `working_directory` the use `app.working_directory` property. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
File path.
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.export_image(output_file=r"example.txt")

```
Copy to clipboard