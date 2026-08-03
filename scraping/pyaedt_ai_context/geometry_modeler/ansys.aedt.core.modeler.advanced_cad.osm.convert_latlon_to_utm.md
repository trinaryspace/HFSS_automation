---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.modeler.advanced_cad.osm.convert_latlon_to_utm.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# convert_latlon_to_utm 

ansys.aedt.core.modeler.advanced_cad.osm.convert_latlon_to_utm(_latitude : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _longitude : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _zone_letter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _zone_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")] 
    
Convert latitude and longitude to UTM (Universal Transverse Mercator) coordinates. 

Parameters: 
     

**latitude**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Latitude value in decimal degrees. 

**longitude**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Longitude value in decimal degrees. 

**zone_letter: str, optional**
    
UTM zone designators. The default is `None`. The valid zone letters are `"CDEFGHJKLMNPQRSTUVWXX"` 

**zone_number: int, optional**
    
Global map numbers of a UTM zone numbers map. The default is `None`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
Tuple containing UTM East coordinate, North coordinate, zone letter, and zone number.
Notes
[1]
<https://mapref.org/UTM-ProjectionSystem.html>
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.osm import convert_latlon_to_utm
>>> convert_latlon_to_utm(latitude=1.0, longitude=1.0)

```
Copy to clipboard
# convert_latlon_to_utm 

ansys.aedt.core.modeler.advanced_cad.osm.convert_latlon_to_utm(_latitude : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _longitude : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _zone_letter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _zone_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")] 
    
Convert latitude and longitude to UTM (Universal Transverse Mercator) coordinates. 

Parameters: 
     

**latitude**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Latitude value in decimal degrees. 

**longitude**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Longitude value in decimal degrees. 

**zone_letter: str, optional**
    
UTM zone designators. The default is `None`. The valid zone letters are `"CDEFGHJKLMNPQRSTUVWXX"` 

**zone_number: int, optional**
    
Global map numbers of a UTM zone numbers map. The default is `None`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
Tuple containing UTM East coordinate, North coordinate, zone letter, and zone number.
Notes
[1]
<https://mapref.org/UTM-ProjectionSystem.html>
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.osm import convert_latlon_to_utm
>>> convert_latlon_to_utm(latitude=1.0, longitude=1.0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.modeler.advanced_cad.osm.convert_latlon_to_utm.rst.txt)

# convert_latlon_to_utm 

ansys.aedt.core.modeler.advanced_cad.osm.convert_latlon_to_utm(_latitude : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _longitude : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _zone_letter : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _zone_number : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")] 
    
Convert latitude and longitude to UTM (Universal Transverse Mercator) coordinates. 

Parameters: 
     

**latitude**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Latitude value in decimal degrees. 

**longitude**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Longitude value in decimal degrees. 

**zone_letter: str, optional**
    
UTM zone designators. The default is `None`. The valid zone letters are `"CDEFGHJKLMNPQRSTUVWXX"` 

**zone_number: int, optional**
    
Global map numbers of a UTM zone numbers map. The default is `None`. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
Tuple containing UTM East coordinate, North coordinate, zone letter, and zone number.
Notes
[1]
<https://mapref.org/UTM-ProjectionSystem.html>
Examples

```
>>> from ansys.aedt.core.modeler.advanced_cad.osm import convert_latlon_to_utm
>>> convert_latlon_to_utm(latitude=1.0, longitude=1.0)

```
Copy to clipboard