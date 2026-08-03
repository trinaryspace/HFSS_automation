---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.modeler.advanced_cad.osm.BuildingsPrep.generate_buildings.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# generate_buildings 

BuildingsPrep.generate_buildings(_center_lat_lon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]_, _terrain_mesh_ , _max_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 500_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Generate the buildings stl file. 

Parameters: 
     

**center_lat_lon**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Latitude and longitude. 

**terrain_mesh**`pyvista.PolyData` 
    
Terrain mesh. 

**max_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Radius around latitude and longitude. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Info of generated stl file.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.osm import BuildingsPrep
>>> obj = BuildingsPrep()
>>> obj.generate_buildings(center_lat_lon=[1, 2, 3], terrain_mesh=1)

```
Copy to clipboard
# generate_buildings 

BuildingsPrep.generate_buildings(_center_lat_lon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]_, _terrain_mesh_ , _max_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 500_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Generate the buildings stl file. 

Parameters: 
     

**center_lat_lon**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Latitude and longitude. 

**terrain_mesh**`pyvista.PolyData` 
    
Terrain mesh. 

**max_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Radius around latitude and longitude. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Info of generated stl file.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.osm import BuildingsPrep
>>> obj = BuildingsPrep()
>>> obj.generate_buildings(center_lat_lon=[1, 2, 3], terrain_mesh=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.modeler.advanced_cad.osm.BuildingsPrep.generate_buildings.rst.txt)

# generate_buildings 

BuildingsPrep.generate_buildings(_center_lat_lon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]_, _terrain_mesh_ , _max_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 500_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Generate the buildings stl file. 

Parameters: 
     

**center_lat_lon**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Latitude and longitude. 

**terrain_mesh**`pyvista.PolyData` 
    
Terrain mesh. 

**max_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Radius around latitude and longitude. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Info of generated stl file.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.osm import BuildingsPrep
>>> obj = BuildingsPrep()
>>> obj.generate_buildings(center_lat_lon=[1, 2, 3], terrain_mesh=1)

```
Copy to clipboard