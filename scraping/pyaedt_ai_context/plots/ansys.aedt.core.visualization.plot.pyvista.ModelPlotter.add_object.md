---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_object.html"
category: "plots"
domain: "PyAEDT / HFSS"
---

# add_object 

ModelPlotter.add_object(_cad_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _cad_color : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'dodgerblue'_, _opacity : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'mm'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a mesh file to the scenario.
The mesh file can be an object or any of the PyVista supported files. 

Parameters: 
     

**cad_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the file. 

**cad_color**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Can be a string with color name or a tuple with (r,g,b) values. The default value is `"dodgerblue"`. 

**opacity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Value between 0 to 1 of opacity. The default value is `1`. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Model units. The default value is `"mm"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.visualization.plot.pyvista import ModelPlotter
>>> obj = ModelPlotter()
>>> obj.add_object(cad_path="example.stl")

```
Copy to clipboard
# add_object 

ModelPlotter.add_object(_cad_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _cad_color : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'dodgerblue'_, _opacity : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'mm'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a mesh file to the scenario.
The mesh file can be an object or any of the PyVista supported files. 

Parameters: 
     

**cad_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the file. 

**cad_color**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Can be a string with color name or a tuple with (r,g,b) values. The default value is `"dodgerblue"`. 

**opacity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Value between 0 to 1 of opacity. The default value is `1`. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Model units. The default value is `"mm"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.visualization.plot.pyvista import ModelPlotter
>>> obj = ModelPlotter()
>>> obj.add_object(cad_path="example.stl")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_object.rst.txt)

# add_object 

ModelPlotter.add_object(_cad_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _cad_color : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'dodgerblue'_, _opacity : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'mm'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Add a mesh file to the scenario.
The mesh file can be an object or any of the PyVista supported files. 

Parameters: 
     

**cad_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path to the file. 

**cad_color**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
Can be a string with color name or a tuple with (r,g,b) values. The default value is `"dodgerblue"`. 

**opacity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Value between 0 to 1 of opacity. The default value is `1`. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Model units. The default value is `"mm"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.visualization.plot.pyvista import ModelPlotter
>>> obj = ModelPlotter()
>>> obj.add_object(cad_path="example.stl")

```
Copy to clipboard