---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# Point 

class ansys.aedt.core.modeler.cad.elements_3d.Point(_primitives_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) 
    
Manages point attributes for the AEDT 3D Modeler. 

Parameters: 
     

**primitives**`ansys.aedt.core.modeler.cad.primitives_3d.Primitives3D` 
    
Inherited parent object. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the point.
Examples
Basic usage demonstrated with an HFSS design:

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> primitives = aedtapp.modeler

```
Copy to clipboard
Create a point, to return an [`ansys.aedt.core.modeler.cad.elements_3d.Point`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.html#ansys.aedt.core.modeler.cad.elements_3d.Point "ansys.aedt.core.modeler.cad.elements_3d.Point").

```
>>> point = primitives.create_point([30, 30, 0], "my_point", (0, 195, 255))
>>> my_point = primitives.points[point.name]

```
Copy to clipboard
Methods  
| [`Point.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.delete.html#ansys.aedt.core.modeler.cad.elements_3d.Point.delete "ansys.aedt.core.modeler.cad.elements_3d.Point.delete")()  | Delete the point.  |  
| --- | --- |  
| [`Point.set_color`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.set_color.html#ansys.aedt.core.modeler.cad.elements_3d.Point.set_color "ansys.aedt.core.modeler.cad.elements_3d.Point.set_color")(color_value)  | Set symbol color.  |  
Attributes  
| [`Point.coordinate_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.coordinate_system.html#ansys.aedt.core.modeler.cad.elements_3d.Point.coordinate_system "ansys.aedt.core.modeler.cad.elements_3d.Point.coordinate_system")  | Coordinate system of the point.  |  
| --- | --- |  
| [`Point.logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.logger.html#ansys.aedt.core.modeler.cad.elements_3d.Point.logger "ansys.aedt.core.modeler.cad.elements_3d.Point.logger")  | Logger.  |  
| [`Point.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.name.html#ansys.aedt.core.modeler.cad.elements_3d.Point.name "ansys.aedt.core.modeler.cad.elements_3d.Point.name")  | Name of the point as a string value.  |  
| [`Point.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.public_dir.html#ansys.aedt.core.modeler.cad.elements_3d.Point.public_dir "ansys.aedt.core.modeler.cad.elements_3d.Point.public_dir")  | Shortcut for dir(self).  |  
| [`Point.valid_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.valid_properties.html#ansys.aedt.core.modeler.cad.elements_3d.Point.valid_properties "ansys.aedt.core.modeler.cad.elements_3d.Point.valid_properties")  | Valid properties.  |  
# Point 

class ansys.aedt.core.modeler.cad.elements_3d.Point(_primitives_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) 
    
Manages point attributes for the AEDT 3D Modeler. 

Parameters: 
     

**primitives**`ansys.aedt.core.modeler.cad.primitives_3d.Primitives3D` 
    
Inherited parent object. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the point.
Examples
Basic usage demonstrated with an HFSS design:

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> primitives = aedtapp.modeler

```
Copy to clipboard
Create a point, to return an [`ansys.aedt.core.modeler.cad.elements_3d.Point`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.html#ansys.aedt.core.modeler.cad.elements_3d.Point "ansys.aedt.core.modeler.cad.elements_3d.Point").

```
>>> point = primitives.create_point([30, 30, 0], "my_point", (0, 195, 255))
>>> my_point = primitives.points[point.name]

```
Copy to clipboard
Methods  
| [`Point.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.delete.html#ansys.aedt.core.modeler.cad.elements_3d.Point.delete "ansys.aedt.core.modeler.cad.elements_3d.Point.delete")()  | Delete the point.  |  
| --- | --- |  
| [`Point.set_color`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.set_color.html#ansys.aedt.core.modeler.cad.elements_3d.Point.set_color "ansys.aedt.core.modeler.cad.elements_3d.Point.set_color")(color_value)  | Set symbol color.  |  
Attributes  
| [`Point.coordinate_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.coordinate_system.html#ansys.aedt.core.modeler.cad.elements_3d.Point.coordinate_system "ansys.aedt.core.modeler.cad.elements_3d.Point.coordinate_system")  | Coordinate system of the point.  |  
| --- | --- |  
| [`Point.logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.logger.html#ansys.aedt.core.modeler.cad.elements_3d.Point.logger "ansys.aedt.core.modeler.cad.elements_3d.Point.logger")  | Logger.  |  
| [`Point.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.name.html#ansys.aedt.core.modeler.cad.elements_3d.Point.name "ansys.aedt.core.modeler.cad.elements_3d.Point.name")  | Name of the point as a string value.  |  
| [`Point.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.public_dir.html#ansys.aedt.core.modeler.cad.elements_3d.Point.public_dir "ansys.aedt.core.modeler.cad.elements_3d.Point.public_dir")  | Shortcut for dir(self).  |  
| [`Point.valid_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.valid_properties.html#ansys.aedt.core.modeler.cad.elements_3d.Point.valid_properties "ansys.aedt.core.modeler.cad.elements_3d.Point.valid_properties")  | Valid properties.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.rst.txt)

# Point 

class ansys.aedt.core.modeler.cad.elements_3d.Point(_primitives_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) 
    
Manages point attributes for the AEDT 3D Modeler. 

Parameters: 
     

**primitives**`ansys.aedt.core.modeler.cad.primitives_3d.Primitives3D` 
    
Inherited parent object. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the point.
Examples
Basic usage demonstrated with an HFSS design:

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> primitives = aedtapp.modeler

```
Copy to clipboard
Create a point, to return an [`ansys.aedt.core.modeler.cad.elements_3d.Point`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.html#ansys.aedt.core.modeler.cad.elements_3d.Point "ansys.aedt.core.modeler.cad.elements_3d.Point").

```
>>> point = primitives.create_point([30, 30, 0], "my_point", (0, 195, 255))
>>> my_point = primitives.points[point.name]

```
Copy to clipboard
Methods  
| [`Point.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.delete.html#ansys.aedt.core.modeler.cad.elements_3d.Point.delete "ansys.aedt.core.modeler.cad.elements_3d.Point.delete")()  | Delete the point.  |  
| --- | --- |  
| [`Point.set_color`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.set_color.html#ansys.aedt.core.modeler.cad.elements_3d.Point.set_color "ansys.aedt.core.modeler.cad.elements_3d.Point.set_color")(color_value)  | Set symbol color.  |  
Attributes  
| [`Point.coordinate_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.coordinate_system.html#ansys.aedt.core.modeler.cad.elements_3d.Point.coordinate_system "ansys.aedt.core.modeler.cad.elements_3d.Point.coordinate_system")  | Coordinate system of the point.  |  
| --- | --- |  
| [`Point.logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.logger.html#ansys.aedt.core.modeler.cad.elements_3d.Point.logger "ansys.aedt.core.modeler.cad.elements_3d.Point.logger")  | Logger.  |  
| [`Point.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.name.html#ansys.aedt.core.modeler.cad.elements_3d.Point.name "ansys.aedt.core.modeler.cad.elements_3d.Point.name")  | Name of the point as a string value.  |  
| [`Point.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.public_dir.html#ansys.aedt.core.modeler.cad.elements_3d.Point.public_dir "ansys.aedt.core.modeler.cad.elements_3d.Point.public_dir")  | Shortcut for dir(self).  |  
| [`Point.valid_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Point.valid_properties.html#ansys.aedt.core.modeler.cad.elements_3d.Point.valid_properties "ansys.aedt.core.modeler.cad.elements_3d.Point.valid_properties")  | Valid properties.  |