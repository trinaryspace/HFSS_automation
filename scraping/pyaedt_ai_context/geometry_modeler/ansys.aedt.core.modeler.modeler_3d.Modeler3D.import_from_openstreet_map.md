---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.import_from_openstreet_map.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# import_from_openstreet_map 

Modeler3D.import_from_openstreet_map(_latitude_longitude : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]_, _env_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'default'_, _terrain_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 500_, _include_osm_buildings : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _including_osm_roads : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _import_in_aedt : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _plot_before_importing : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _z_offset : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _road_step : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 3_, _road_width : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 8_, _create_lightweight_part : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Import OpenStreet Maps into AEDT. 

Parameters: 
     

**latitude_longitude**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Latitude and longitude. 

**env_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the environment used to create the scene. The default value is `"default"`. 

**terrain_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Radius to take around center. The default value is `500`. 

**include_osm_buildings**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if include or not 3D Buildings. Default is `True`. 

**including_osm_roads**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if include or not road. Default is `True`. 

**import_in_aedt**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if import stl after generation or not. Default is `True`. 

**plot_before_importing**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if plot before importing or not. Default is `True`. 

**z_offset**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Road elevation offset. Default is `0`. 

**road_step**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Road simplification steps in meter. Default is `3`. 

**road_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Road width in meter. Default is `8`. 

**create_lightweight_part**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if import as lightweight object or not. Default is `True`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary of generated infos.
Notes
Please note that elevation is not computed anymore in this method. Please check the example `https://examples.aedt.docs.pyansys.com/version/dev/examples/high_frequency/antenna/large_scenarios/city.html` to compute also elevation.
Examples

```
>>> from ansys.aedt.core.modeler.modeler_3d import Modeler3D
>>> obj = Modeler3D()
>>> obj.import_from_openstreet_map(latitude_longitude=[1, 2, 3])

```
Copy to clipboard
# import_from_openstreet_map 

Modeler3D.import_from_openstreet_map(_latitude_longitude : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]_, _env_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'default'_, _terrain_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 500_, _include_osm_buildings : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _including_osm_roads : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _import_in_aedt : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _plot_before_importing : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _z_offset : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _road_step : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 3_, _road_width : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 8_, _create_lightweight_part : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Import OpenStreet Maps into AEDT. 

Parameters: 
     

**latitude_longitude**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Latitude and longitude. 

**env_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the environment used to create the scene. The default value is `"default"`. 

**terrain_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Radius to take around center. The default value is `500`. 

**include_osm_buildings**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if include or not 3D Buildings. Default is `True`. 

**including_osm_roads**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if include or not road. Default is `True`. 

**import_in_aedt**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if import stl after generation or not. Default is `True`. 

**plot_before_importing**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if plot before importing or not. Default is `True`. 

**z_offset**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Road elevation offset. Default is `0`. 

**road_step**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Road simplification steps in meter. Default is `3`. 

**road_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Road width in meter. Default is `8`. 

**create_lightweight_part**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if import as lightweight object or not. Default is `True`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary of generated infos.
Notes
Please note that elevation is not computed anymore in this method. Please check the example `https://examples.aedt.docs.pyansys.com/version/dev/examples/high_frequency/antenna/large_scenarios/city.html` to compute also elevation.
Examples

```
>>> from ansys.aedt.core.modeler.modeler_3d import Modeler3D
>>> obj = Modeler3D()
>>> obj.import_from_openstreet_map(latitude_longitude=[1, 2, 3])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.import_from_openstreet_map.rst.txt)

# import_from_openstreet_map 

Modeler3D.import_from_openstreet_map(_latitude_longitude : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")]_, _env_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'default'_, _terrain_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 500_, _include_osm_buildings : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _including_osm_roads : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _import_in_aedt : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _plot_before_importing : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _z_offset : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 2_, _road_step : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 3_, _road_width : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 8_, _create_lightweight_part : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Import OpenStreet Maps into AEDT. 

Parameters: 
     

**latitude_longitude**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Latitude and longitude. 

**env_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the environment used to create the scene. The default value is `"default"`. 

**terrain_radius**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Radius to take around center. The default value is `500`. 

**include_osm_buildings**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if include or not 3D Buildings. Default is `True`. 

**including_osm_roads**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if include or not road. Default is `True`. 

**import_in_aedt**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if import stl after generation or not. Default is `True`. 

**plot_before_importing**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if plot before importing or not. Default is `True`. 

**z_offset**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Road elevation offset. Default is `0`. 

**road_step**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Road simplification steps in meter. Default is `3`. 

**road_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Road width in meter. Default is `8`. 

**create_lightweight_part**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Either if import as lightweight object or not. Default is `True`. 

Returns: 
     

[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")
    
Dictionary of generated infos.
Notes
Please note that elevation is not computed anymore in this method. Please check the example `https://examples.aedt.docs.pyansys.com/version/dev/examples/high_frequency/antenna/large_scenarios/city.html` to compute also elevation.
Examples

```
>>> from ansys.aedt.core.modeler.modeler_3d import Modeler3D
>>> obj = Modeler3D()
>>> obj.import_from_openstreet_map(latitude_longitude=[1, 2, 3])

```
Copy to clipboard