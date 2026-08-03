---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.point_cloud.html"
category: "plots"
domain: "PyAEDT / HFSS"
---

# point_cloud 

ModelPlotter.point_cloud(_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 10_, _in_volume =False_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Generate point cloud with available objects. 

Parameters: 
     

**points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of points to generate. The default is `10`. 

**in_volume**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot inside the volume of selected object or on the surface. If `True`, generate points in volume. If `False`, generate points on surface. The default value is `False`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary containing the point cloud for each object. Each entry has the object name as the key and a list with two elements: the path to the output `.pts` file and the `pyvista.PolyData` object.
Examples

```
>>> from ansys.aedt.core.visualization.plot.pyvista import ModelPlotter
>>> obj = ModelPlotter()
>>> obj.point_cloud(points=[0, 0, 0])

```
Copy to clipboard
# point_cloud 

ModelPlotter.point_cloud(_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 10_, _in_volume =False_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Generate point cloud with available objects. 

Parameters: 
     

**points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of points to generate. The default is `10`. 

**in_volume**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot inside the volume of selected object or on the surface. If `True`, generate points in volume. If `False`, generate points on surface. The default value is `False`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary containing the point cloud for each object. Each entry has the object name as the key and a list with two elements: the path to the output `.pts` file and the `pyvista.PolyData` object.
Examples

```
>>> from ansys.aedt.core.visualization.plot.pyvista import ModelPlotter
>>> obj = ModelPlotter()
>>> obj.point_cloud(points=[0, 0, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.point_cloud.rst.txt)

# point_cloud 

ModelPlotter.point_cloud(_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 10_, _in_volume =False_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Generate point cloud with available objects. 

Parameters: 
     

**points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of points to generate. The default is `10`. 

**in_volume**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to plot inside the volume of selected object or on the surface. If `True`, generate points in volume. If `False`, generate points on surface. The default value is `False`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary containing the point cloud for each object. Each entry has the object name as the key and a list with two elements: the path to the output `.pts` file and the `pyvista.PolyData` object.
Examples

```
>>> from ansys.aedt.core.visualization.plot.pyvista import ModelPlotter
>>> obj = ModelPlotter()
>>> obj.point_cloud(points=[0, 0, 0])

```
Copy to clipboard