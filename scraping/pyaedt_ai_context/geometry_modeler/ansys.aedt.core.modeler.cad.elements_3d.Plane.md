---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# Plane 

class ansys.aedt.core.modeler.cad.elements_3d.Plane(_primitives_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) 
    
Manages plane attributes for the AEDT 3D Modeler. 

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
Create a plane, to return an [`ansys.aedt.core.modeler.cad.elements_3d.Plane`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.html#ansys.aedt.core.modeler.cad.elements_3d.Plane "ansys.aedt.core.modeler.cad.elements_3d.Plane").

```
>>> plane = primitives.create_plane("my_plane", "-0.7mm", "0.3mm", "0mm", "0.7mm", "-0.3mm", "0mm", "(0, 195, 255)")
>>> my_plane = primitives.planes[plane.name]

```
Copy to clipboard
Methods  
| [`Plane.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.delete.html#ansys.aedt.core.modeler.cad.elements_3d.Plane.delete "ansys.aedt.core.modeler.cad.elements_3d.Plane.delete")()  | Delete the plane.  |  
| --- | --- |  
| [`Plane.set_color`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.set_color.html#ansys.aedt.core.modeler.cad.elements_3d.Plane.set_color "ansys.aedt.core.modeler.cad.elements_3d.Plane.set_color")(color_value)  | Set symbol color.  |  
Attributes  
| [`Plane.coordinate_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.coordinate_system.html#ansys.aedt.core.modeler.cad.elements_3d.Plane.coordinate_system "ansys.aedt.core.modeler.cad.elements_3d.Plane.coordinate_system")  | Coordinate system of the plane.  |  
| --- | --- |  
| [`Plane.logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.logger.html#ansys.aedt.core.modeler.cad.elements_3d.Plane.logger "ansys.aedt.core.modeler.cad.elements_3d.Plane.logger")  | Logger.  |  
| [`Plane.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.name.html#ansys.aedt.core.modeler.cad.elements_3d.Plane.name "ansys.aedt.core.modeler.cad.elements_3d.Plane.name")  | Name of the plane as a string value.  |  
| [`Plane.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.public_dir.html#ansys.aedt.core.modeler.cad.elements_3d.Plane.public_dir "ansys.aedt.core.modeler.cad.elements_3d.Plane.public_dir")  | Shortcut for dir(self).  |  
| [`Plane.valid_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.valid_properties.html#ansys.aedt.core.modeler.cad.elements_3d.Plane.valid_properties "ansys.aedt.core.modeler.cad.elements_3d.Plane.valid_properties")  | Valid properties.  |  
# Plane 

class ansys.aedt.core.modeler.cad.elements_3d.Plane(_primitives_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) 
    
Manages plane attributes for the AEDT 3D Modeler. 

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
Create a plane, to return an [`ansys.aedt.core.modeler.cad.elements_3d.Plane`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.html#ansys.aedt.core.modeler.cad.elements_3d.Plane "ansys.aedt.core.modeler.cad.elements_3d.Plane").

```
>>> plane = primitives.create_plane("my_plane", "-0.7mm", "0.3mm", "0mm", "0.7mm", "-0.3mm", "0mm", "(0, 195, 255)")
>>> my_plane = primitives.planes[plane.name]

```
Copy to clipboard
Methods  
| [`Plane.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.delete.html#ansys.aedt.core.modeler.cad.elements_3d.Plane.delete "ansys.aedt.core.modeler.cad.elements_3d.Plane.delete")()  | Delete the plane.  |  
| --- | --- |  
| [`Plane.set_color`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.set_color.html#ansys.aedt.core.modeler.cad.elements_3d.Plane.set_color "ansys.aedt.core.modeler.cad.elements_3d.Plane.set_color")(color_value)  | Set symbol color.  |  
Attributes  
| [`Plane.coordinate_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.coordinate_system.html#ansys.aedt.core.modeler.cad.elements_3d.Plane.coordinate_system "ansys.aedt.core.modeler.cad.elements_3d.Plane.coordinate_system")  | Coordinate system of the plane.  |  
| --- | --- |  
| [`Plane.logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.logger.html#ansys.aedt.core.modeler.cad.elements_3d.Plane.logger "ansys.aedt.core.modeler.cad.elements_3d.Plane.logger")  | Logger.  |  
| [`Plane.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.name.html#ansys.aedt.core.modeler.cad.elements_3d.Plane.name "ansys.aedt.core.modeler.cad.elements_3d.Plane.name")  | Name of the plane as a string value.  |  
| [`Plane.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.public_dir.html#ansys.aedt.core.modeler.cad.elements_3d.Plane.public_dir "ansys.aedt.core.modeler.cad.elements_3d.Plane.public_dir")  | Shortcut for dir(self).  |  
| [`Plane.valid_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.valid_properties.html#ansys.aedt.core.modeler.cad.elements_3d.Plane.valid_properties "ansys.aedt.core.modeler.cad.elements_3d.Plane.valid_properties")  | Valid properties.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.rst.txt)

# Plane 

class ansys.aedt.core.modeler.cad.elements_3d.Plane(_primitives_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) 
    
Manages plane attributes for the AEDT 3D Modeler. 

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
Create a plane, to return an [`ansys.aedt.core.modeler.cad.elements_3d.Plane`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.html#ansys.aedt.core.modeler.cad.elements_3d.Plane "ansys.aedt.core.modeler.cad.elements_3d.Plane").

```
>>> plane = primitives.create_plane("my_plane", "-0.7mm", "0.3mm", "0mm", "0.7mm", "-0.3mm", "0mm", "(0, 195, 255)")
>>> my_plane = primitives.planes[plane.name]

```
Copy to clipboard
Methods  
| [`Plane.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.delete.html#ansys.aedt.core.modeler.cad.elements_3d.Plane.delete "ansys.aedt.core.modeler.cad.elements_3d.Plane.delete")()  | Delete the plane.  |  
| --- | --- |  
| [`Plane.set_color`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.set_color.html#ansys.aedt.core.modeler.cad.elements_3d.Plane.set_color "ansys.aedt.core.modeler.cad.elements_3d.Plane.set_color")(color_value)  | Set symbol color.  |  
Attributes  
| [`Plane.coordinate_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.coordinate_system.html#ansys.aedt.core.modeler.cad.elements_3d.Plane.coordinate_system "ansys.aedt.core.modeler.cad.elements_3d.Plane.coordinate_system")  | Coordinate system of the plane.  |  
| --- | --- |  
| [`Plane.logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.logger.html#ansys.aedt.core.modeler.cad.elements_3d.Plane.logger "ansys.aedt.core.modeler.cad.elements_3d.Plane.logger")  | Logger.  |  
| [`Plane.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.name.html#ansys.aedt.core.modeler.cad.elements_3d.Plane.name "ansys.aedt.core.modeler.cad.elements_3d.Plane.name")  | Name of the plane as a string value.  |  
| [`Plane.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.public_dir.html#ansys.aedt.core.modeler.cad.elements_3d.Plane.public_dir "ansys.aedt.core.modeler.cad.elements_3d.Plane.public_dir")  | Shortcut for dir(self).  |  
| [`Plane.valid_properties`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.Plane.valid_properties.html#ansys.aedt.core.modeler.cad.elements_3d.Plane.valid_properties "ansys.aedt.core.modeler.cad.elements_3d.Plane.valid_properties")  | Valid properties.  |