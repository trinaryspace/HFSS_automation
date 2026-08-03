---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_circuit.PostProcessorCircuit.export_report_to_jpg.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# export_report_to_jpg 

PostProcessorCircuit.export_report_to_jpg(_project_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 800_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 450_, _image_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'jpg'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export plot to an image file. 

Parameters: 
     

**project_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the project directory or full path to the file. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the plot to export. 

**width**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Image width. Default is `800` which takes Desktop size or 800 pixel. 

**height**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Image height. Default is `450` which takes Desktop size or 450 pixel. 

**image_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Format of the image file. The default is `"jpg"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.ExportImageToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.common import PostProcessorCommon
>>> obj = PostProcessorCommon()
>>> obj.export_report_to_jpg("my_dir", "my_plot")

```
Copy to clipboard
# export_report_to_jpg 

PostProcessorCircuit.export_report_to_jpg(_project_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 800_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 450_, _image_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'jpg'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export plot to an image file. 

Parameters: 
     

**project_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the project directory or full path to the file. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the plot to export. 

**width**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Image width. Default is `800` which takes Desktop size or 800 pixel. 

**height**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Image height. Default is `450` which takes Desktop size or 450 pixel. 

**image_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Format of the image file. The default is `"jpg"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.ExportImageToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.common import PostProcessorCommon
>>> obj = PostProcessorCommon()
>>> obj.export_report_to_jpg("my_dir", "my_plot")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_circuit.PostProcessorCircuit.export_report_to_jpg.rst.txt)

# export_report_to_jpg 

PostProcessorCircuit.export_report_to_jpg(_project_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _plot_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 800_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 450_, _image_format : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'jpg'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Export plot to an image file. 

Parameters: 
     

**project_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to the project directory or full path to the file. 

**plot_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the plot to export. 

**width**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Image width. Default is `800` which takes Desktop size or 800 pixel. 

**height**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Image height. Default is `450` which takes Desktop size or 450 pixel. 

**image_format**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Format of the image file. The default is `"jpg"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.ExportImageToFile

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.visualization.post.common import PostProcessorCommon
>>> obj = PostProcessorCommon()
>>> obj.export_report_to_jpg("my_dir", "my_plot")

```
Copy to clipboard