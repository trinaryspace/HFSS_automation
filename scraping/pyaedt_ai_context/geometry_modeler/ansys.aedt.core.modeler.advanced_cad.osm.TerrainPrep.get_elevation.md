---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.modeler.advanced_cad.osm.TerrainPrep.get_elevation.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# get_elevation 

static TerrainPrep.get_elevation(_center_lat_lon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]_, _max_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 500_, _grid_size : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 3_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[NDArray[float64], NDArray[float64], NDArray[float64]] 
    
Get Elevation map. 

Parameters: 
     

**center_lat_lon**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Latitude and longitude. 

**max_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Radius around latitude and longitude. 

**grid_size**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Grid size in meters. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.osm import TerrainPrep
>>> obj = TerrainPrep()
>>> obj.get_elevation(center_lat_lon=[1, 2, 3])

```
Copy to clipboard
# get_elevation 

static TerrainPrep.get_elevation(_center_lat_lon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]_, _max_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 500_, _grid_size : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 3_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[NDArray[float64], NDArray[float64], NDArray[float64]] 
    
Get Elevation map. 

Parameters: 
     

**center_lat_lon**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Latitude and longitude. 

**max_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Radius around latitude and longitude. 

**grid_size**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Grid size in meters. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.osm import TerrainPrep
>>> obj = TerrainPrep()
>>> obj.get_elevation(center_lat_lon=[1, 2, 3])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.modeler.advanced_cad.osm.TerrainPrep.get_elevation.rst.txt)

# get_elevation 

static TerrainPrep.get_elevation(_center_lat_lon : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]_, _max_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 500_, _grid_size : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 3_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[NDArray[float64], NDArray[float64], NDArray[float64]] 
    
Get Elevation map. 

Parameters: 
     

**center_lat_lon**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Latitude and longitude. 

**max_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Radius around latitude and longitude. 

**grid_size**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Grid size in meters. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.osm import TerrainPrep
>>> obj = TerrainPrep()
>>> obj.get_elevation(center_lat_lon=[1, 2, 3])

```
Copy to clipboard