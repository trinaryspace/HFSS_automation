---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.modeler.advanced_cad.osm.TerrainPrep.get_terrain.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# get_terrain 

TerrainPrep.get_terrain(_center_lat_lon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]_, _max_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 500_, _grid_size : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _buffer_percent : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Generate the terrain stl file. 

Parameters: 
     

**center_lat_lon**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Latitude and longitude. 

**max_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Radius around latitude and longitude. 

**grid_size**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Grid size in meters. 

**buffer_percent**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Buffer extra size over the radius. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Info of generated stl file.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.osm import TerrainPrep
>>> obj = TerrainPrep()
>>> obj.get_terrain(center_lat_lon=[1, 2, 3])

```
Copy to clipboard
# get_terrain 

TerrainPrep.get_terrain(_center_lat_lon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]_, _max_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 500_, _grid_size : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _buffer_percent : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Generate the terrain stl file. 

Parameters: 
     

**center_lat_lon**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Latitude and longitude. 

**max_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Radius around latitude and longitude. 

**grid_size**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Grid size in meters. 

**buffer_percent**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Buffer extra size over the radius. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Info of generated stl file.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.osm import TerrainPrep
>>> obj = TerrainPrep()
>>> obj.get_terrain(center_lat_lon=[1, 2, 3])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.modeler.advanced_cad.osm.TerrainPrep.get_terrain.rst.txt)

# get_terrain 

TerrainPrep.get_terrain(_center_lat_lon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]_, _max_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 500_, _grid_size : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _buffer_percent : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Generate the terrain stl file. 

Parameters: 
     

**center_lat_lon**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Latitude and longitude. 

**max_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Radius around latitude and longitude. 

**grid_size**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Grid size in meters. 

**buffer_percent**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Buffer extra size over the radius. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Info of generated stl file.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.osm import TerrainPrep
>>> obj = TerrainPrep()
>>> obj.get_terrain(center_lat_lon=[1, 2, 3])

```
Copy to clipboard