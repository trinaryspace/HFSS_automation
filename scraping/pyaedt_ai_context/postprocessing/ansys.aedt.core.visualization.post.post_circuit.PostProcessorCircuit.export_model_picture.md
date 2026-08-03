---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_circuit.PostProcessorCircuit.export_model_picture.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# export_model_picture 

PostProcessorCircuit.export_model_picture(_output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _page : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1920_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1080_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export a snapshot of the schematic to a `JPG` file. 

Parameters: 
     

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full Path for exporting the image file. The default is `None`, in which case working_dir is used. 

**page**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Page number of the schematic. The default is `1`. 

**width**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Export image picture width size in pixels. Default is 1920 which takes the desktop size. 

**height**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Export image picture height size in pixels. Default is 10800 which takes the desktop size. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
File path of the generated JPG file.
References

```
>>> oEditor.ExportImage

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Circuit
>>> app = Circuit(non_graphical=False)
>>> output_file = app.post.export_model_picture(full_name=os.path.join(app.working_directory, "images1.jpg"))

```
Copy to clipboard
# export_model_picture 

PostProcessorCircuit.export_model_picture(_output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _page : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1920_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1080_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export a snapshot of the schematic to a `JPG` file. 

Parameters: 
     

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full Path for exporting the image file. The default is `None`, in which case working_dir is used. 

**page**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Page number of the schematic. The default is `1`. 

**width**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Export image picture width size in pixels. Default is 1920 which takes the desktop size. 

**height**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Export image picture height size in pixels. Default is 10800 which takes the desktop size. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
File path of the generated JPG file.
References

```
>>> oEditor.ExportImage

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Circuit
>>> app = Circuit(non_graphical=False)
>>> output_file = app.post.export_model_picture(full_name=os.path.join(app.working_directory, "images1.jpg"))

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_circuit.PostProcessorCircuit.export_model_picture.rst.txt)

# export_model_picture 

PostProcessorCircuit.export_model_picture(_output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _page : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1920_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1080_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Export a snapshot of the schematic to a `JPG` file. 

Parameters: 
     

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full Path for exporting the image file. The default is `None`, in which case working_dir is used. 

**page**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Page number of the schematic. The default is `1`. 

**width**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Export image picture width size in pixels. Default is 1920 which takes the desktop size. 

**height**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Export image picture height size in pixels. Default is 10800 which takes the desktop size. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
File path of the generated JPG file.
References

```
>>> oEditor.ExportImage

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Circuit
>>> app = Circuit(non_graphical=False)
>>> output_file = app.post.export_model_picture(full_name=os.path.join(app.working_directory, "images1.jpg"))

```
Copy to clipboard