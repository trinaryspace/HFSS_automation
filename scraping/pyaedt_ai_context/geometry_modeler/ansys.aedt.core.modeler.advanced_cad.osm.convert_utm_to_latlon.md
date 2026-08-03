---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.modeler.advanced_cad.osm.convert_utm_to_latlon.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# convert_utm_to_latlon 

ansys.aedt.core.modeler.advanced_cad.osm.convert_utm_to_latlon(_east : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _north : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _zone_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _zone_letter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _northern : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = None_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] 
    
Convert UTM (Universal Transverse Mercator) coordinates to latitude and longitude. 

Parameters: 
     

**east**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
East value of UTM coordinates. 

**north**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
North value of UTM coordinates. 

**zone_number: int, optional**
    
Global map numbers of a UTM zone numbers map. 

**zone_letter: str, optional**
    
UTM zone designators. The default is `None`. The valid zone letters are `"CDEFGHJKLMNPQRSTUVWXX"` 

**northern: bool, optional**
    
Indicates whether the UTM coordinates are in the Northern Hemisphere. If `True`, the coordinates are treated as being north of the equator, if `False`, they are treated as being south of the equator. The default is `None` in which case the method determines the hemisphere using `zone_letter`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
Tuple containing latitude and longitude.
Notes
[1]
<https://mapref.org/UTM-ProjectionSystem.html>
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.osm import convert_utm_to_latlon
>>> convert_utm_to_latlon(east=1.0, north=1.0, zone_number=1)

```
Copy to clipboard
# convert_utm_to_latlon 

ansys.aedt.core.modeler.advanced_cad.osm.convert_utm_to_latlon(_east : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _north : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _zone_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _zone_letter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _northern : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = None_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] 
    
Convert UTM (Universal Transverse Mercator) coordinates to latitude and longitude. 

Parameters: 
     

**east**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
East value of UTM coordinates. 

**north**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
North value of UTM coordinates. 

**zone_number: int, optional**
    
Global map numbers of a UTM zone numbers map. 

**zone_letter: str, optional**
    
UTM zone designators. The default is `None`. The valid zone letters are `"CDEFGHJKLMNPQRSTUVWXX"` 

**northern: bool, optional**
    
Indicates whether the UTM coordinates are in the Northern Hemisphere. If `True`, the coordinates are treated as being north of the equator, if `False`, they are treated as being south of the equator. The default is `None` in which case the method determines the hemisphere using `zone_letter`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
Tuple containing latitude and longitude.
Notes
[1]
<https://mapref.org/UTM-ProjectionSystem.html>
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.osm import convert_utm_to_latlon
>>> convert_utm_to_latlon(east=1.0, north=1.0, zone_number=1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.modeler.advanced_cad.osm.convert_utm_to_latlon.rst.txt)

# convert_utm_to_latlon 

ansys.aedt.core.modeler.advanced_cad.osm.convert_utm_to_latlon(_east : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _north : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _zone_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _zone_letter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _northern : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = None_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")] 
    
Convert UTM (Universal Transverse Mercator) coordinates to latitude and longitude. 

Parameters: 
     

**east**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
East value of UTM coordinates. 

**north**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
North value of UTM coordinates. 

**zone_number: int, optional**
    
Global map numbers of a UTM zone numbers map. 

**zone_letter: str, optional**
    
UTM zone designators. The default is `None`. The valid zone letters are `"CDEFGHJKLMNPQRSTUVWXX"` 

**northern: bool, optional**
    
Indicates whether the UTM coordinates are in the Northern Hemisphere. If `True`, the coordinates are treated as being north of the equator, if `False`, they are treated as being south of the equator. The default is `None` in which case the method determines the hemisphere using `zone_letter`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
Tuple containing latitude and longitude.
Notes
[1]
<https://mapref.org/UTM-ProjectionSystem.html>
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.osm import convert_utm_to_latlon
>>> convert_utm_to_latlon(east=1.0, north=1.0, zone_number=1)

```
Copy to clipboard