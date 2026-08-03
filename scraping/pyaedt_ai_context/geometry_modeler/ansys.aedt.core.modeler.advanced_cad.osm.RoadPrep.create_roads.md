---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.modeler.advanced_cad.osm.RoadPrep.create_roads.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_roads 

RoadPrep.create_roads(_center_lat_lon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]_, _terrain_mesh_ , _max_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1000_, _z_offset : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _road_step : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 10_, _road_width : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Generate the road stl file. 

Parameters: 
     

**center_lat_lon**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Latitude and longitude. 

**terrain_mesh**`pyvista.PolygonData` 
    
Terrain mesh. 

**max_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Radius around latitude and longitude. 

**z_offset**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Elevation offset of the road. 

**road_step**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Road computation steps in meters. 

**road_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Road width in meter. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Info of generated stl file.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.osm import RoadPrep
>>> obj = RoadPrep()
>>> obj.create_roads(center_lat_lon=[1, 2, 3], terrain_mesh=1)

```
Copy to clipboard
# create_roads 

RoadPrep.create_roads(_center_lat_lon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]_, _terrain_mesh_ , _max_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1000_, _z_offset : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _road_step : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 10_, _road_width : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Generate the road stl file. 

Parameters: 
     

**center_lat_lon**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Latitude and longitude. 

**terrain_mesh**`pyvista.PolygonData` 
    
Terrain mesh. 

**max_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Radius around latitude and longitude. 

**z_offset**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Elevation offset of the road. 

**road_step**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Road computation steps in meters. 

**road_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Road width in meter. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Info of generated stl file.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.osm import RoadPrep
>>> obj = RoadPrep()
>>> obj.create_roads(center_lat_lon=[1, 2, 3], terrain_mesh=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.modeler.advanced_cad.osm.RoadPrep.create_roads.rst.txt)

# create_roads 

RoadPrep.create_roads(_center_lat_lon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]_, _terrain_mesh_ , _max_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1000_, _z_offset : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _road_step : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 10_, _road_width : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Generate the road stl file. 

Parameters: 
     

**center_lat_lon**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Latitude and longitude. 

**terrain_mesh**`pyvista.PolygonData` 
    
Terrain mesh. 

**max_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Radius around latitude and longitude. 

**z_offset**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Elevation offset of the road. 

**road_step**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Road computation steps in meters. 

**road_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Road width in meter. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Info of generated stl file.
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.osm import RoadPrep
>>> obj = RoadPrep()
>>> obj.create_roads(center_lat_lon=[1, 2, 3], terrain_mesh=1)

```
Copy to clipboard