---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.get_points_value.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# get_points_value 

FieldPlot.get_points_value(_points : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _filename : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _visibility : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | pd.DataFrame 
    
Get points data from field plot.
Note
This method is working only if the associated field plot is currently visible.
Note
This method does not work in non-graphical mode. 

Parameters: 
     

**points**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` `lists` or [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
List with [x,y,z] coordinates of a point or list of lists of points or dictionary with keys containing point names and for each key the point coordinates [x,y,z]. 

**filename**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)"), `optional` 
    
Full path or relative path with filename. Default is `None` in which case no file is exported. 

**visibility**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to keep the markers visible in the UI. Default is `False`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") or `pd.DataFrame` 
    
Dict containing 5 keys: point names, x,y,z coordinates and the quantity probed. Each key is associated with a list with the same length of the argument points. If pandas is installed, the output is a pandas DataFrame with point names as index and coordinates and quantity as columns.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import FieldPlot
>>> obj = FieldPlot()
>>> obj.get_points_value(points={"Name": "Value"})

```
Copy to clipboard
# get_points_value 

FieldPlot.get_points_value(_points : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _filename : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _visibility : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | pd.DataFrame 
    
Get points data from field plot.
Note
This method is working only if the associated field plot is currently visible.
Note
This method does not work in non-graphical mode. 

Parameters: 
     

**points**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` `lists` or [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
List with [x,y,z] coordinates of a point or list of lists of points or dictionary with keys containing point names and for each key the point coordinates [x,y,z]. 

**filename**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)"), `optional` 
    
Full path or relative path with filename. Default is `None` in which case no file is exported. 

**visibility**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to keep the markers visible in the UI. Default is `False`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") or `pd.DataFrame` 
    
Dict containing 5 keys: point names, x,y,z coordinates and the quantity probed. Each key is associated with a list with the same length of the argument points. If pandas is installed, the output is a pandas DataFrame with point names as index and coordinates and quantity as columns.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import FieldPlot
>>> obj = FieldPlot()
>>> obj.get_points_value(points={"Name": "Value"})

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_data.FieldPlot.get_points_value.rst.txt)

# get_points_value 

FieldPlot.get_points_value(_points : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _filename : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _visibility : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | pd.DataFrame 
    
Get points data from field plot.
Note
This method is working only if the associated field plot is currently visible.
Note
This method does not work in non-graphical mode. 

Parameters: 
     

**points**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` `lists` or [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
List with [x,y,z] coordinates of a point or list of lists of points or dictionary with keys containing point names and for each key the point coordinates [x,y,z]. 

**filename**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)"), `optional` 
    
Full path or relative path with filename. Default is `None` in which case no file is exported. 

**visibility**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to keep the markers visible in the UI. Default is `False`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") or `pd.DataFrame` 
    
Dict containing 5 keys: point names, x,y,z coordinates and the quantity probed. Each key is associated with a list with the same length of the argument points. If pandas is installed, the output is a pandas DataFrame with point names as index and coordinates and quantity as columns.
Examples

```
>>> from ansys.aedt.core.visualization.post.field_data import FieldPlot
>>> obj = FieldPlot()
>>> obj.get_points_value(points={"Name": "Value"})

```
Copy to clipboard