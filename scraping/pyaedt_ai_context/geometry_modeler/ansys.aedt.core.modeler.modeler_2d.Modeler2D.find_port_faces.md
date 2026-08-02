---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.find_port_faces.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# find_port_faces 

Modeler2D.find_port_faces(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Find the vacuums given a list of input sheets.
Starting from a list of input sheets, this method creates a list of output sheets that represent the blank parts (vacuums) and the tool parts of all the intersections of solids on the sheets. After a vacuum on a sheet is found, a port can be created on it. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of input sheets names. 

Returns: 
     

`List`
    
List of output sheets (2x len(port_sheets)).
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.find_port_faces(assignment="Box1")

```
Copy to clipboard
# find_port_faces 

Modeler2D.find_port_faces(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Find the vacuums given a list of input sheets.
Starting from a list of input sheets, this method creates a list of output sheets that represent the blank parts (vacuums) and the tool parts of all the intersections of solids on the sheets. After a vacuum on a sheet is found, a port can be created on it. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of input sheets names. 

Returns: 
     

`List`
    
List of output sheets (2x len(port_sheets)).
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.find_port_faces(assignment="Box1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.find_port_faces.rst.txt)

# find_port_faces 

Modeler2D.find_port_faces(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Find the vacuums given a list of input sheets.
Starting from a list of input sheets, this method creates a list of output sheets that represent the blank parts (vacuums) and the tool parts of all the intersections of solids on the sheets. After a vacuum on a sheet is found, a port can be created on it. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of input sheets names. 

Returns: 
     

`List`
    
List of output sheets (2x len(port_sheets)).
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.find_port_faces(assignment="Box1")

```
Copy to clipboard