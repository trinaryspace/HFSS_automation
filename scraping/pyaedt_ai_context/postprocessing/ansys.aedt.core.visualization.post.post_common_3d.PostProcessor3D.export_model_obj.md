---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_common_3d.PostProcessor3D.export_model_obj.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# export_model_obj 

PostProcessor3D.export_model_obj(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _export_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") = None_, _export_as_multiple_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _air_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Export the model. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
List of strings with names of objects to export. Default is `None` in which case export every model object except 3D ones and vacuum and air objects. 

**export_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path of the exported OBJ file. 

**export_as_multiple_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export the model as multiple objects or not. Default is `False` in which case the model is exported as single object. 

**air_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export air and vacuum objects. The default is `False`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
Paths for OBJ files.
Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.export_model_obj(assignment="Box1", export_path="directory")

```
Copy to clipboard
# export_model_obj 

PostProcessor3D.export_model_obj(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _export_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") = None_, _export_as_multiple_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _air_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Export the model. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
List of strings with names of objects to export. Default is `None` in which case export every model object except 3D ones and vacuum and air objects. 

**export_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path of the exported OBJ file. 

**export_as_multiple_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export the model as multiple objects or not. Default is `False` in which case the model is exported as single object. 

**air_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export air and vacuum objects. The default is `False`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
Paths for OBJ files.
Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.export_model_obj(assignment="Box1", export_path="directory")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.post_common_3d.PostProcessor3D.export_model_obj.rst.txt)

# export_model_obj 

PostProcessor3D.export_model_obj(_assignment : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] = None_, _export_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") = None_, _export_as_multiple_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _air_objects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Export the model. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
List of strings with names of objects to export. Default is `None` in which case export every model object except 3D ones and vacuum and air objects. 

**export_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Full path of the exported OBJ file. 

**export_as_multiple_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export the model as multiple objects or not. Default is `False` in which case the model is exported as single object. 

**air_objects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to export air and vacuum objects. The default is `False`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
Paths for OBJ files.
Examples

```
>>> from ansys.aedt.core.visualization.post.post_common_3d import PostProcessor3D
>>> obj = PostProcessor3D()
>>> obj.export_model_obj(assignment="Box1", export_path="directory")

```
Copy to clipboard