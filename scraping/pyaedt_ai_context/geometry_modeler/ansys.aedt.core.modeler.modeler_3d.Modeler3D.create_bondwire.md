---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_bondwire.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_bondwire 

Modeler3D.create_bondwire(_start : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _end : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _h1 : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.2_, _h2 : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _alpha : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 80_, _beta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _bond_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _diameter : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.025_, _facets : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 6_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Z'_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a bondwire. 

Parameters: 
     

**start**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the starting position of the bond pad. 

**end**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the ending position of the bond pad. 

**h1** float|str `optional` 
    
Height between the IC die I/O pad and the top of the bondwire. If the height is provided as a parameter, its value has to be provided as value + unit. The default is `0.2`. 

**h2** float|str `optional` 
    
Height of the IC die I/O pad above the lead frame. If the height is provided as a parameter, its value has to be provided as value + unit. The default is `0`. A negative value indicates that the I/O pad is below the lead frame. 

**alpha**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Angle in degrees between the xy plane and the wire bond at the IC die I/O pad. The default is `80`. 

**beta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Angle in degrees between the xy plane and the wire bond at the lead frame. The default is `5`. 

**bond_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Type of the boundwire, which indicates its shape. Options are:
  * ‘’0’’ for JEDEC 5-point
  * `1` for JEDEC 4-point
  * ‘’2`` for Low

The default is ‘’0``. 

**diameter** float|str `optional` 
    
Diameter of the wire. The default is `0.025`. 

**facets**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of wire facets. The default is `6`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the bondwire. The default is `None`, in which case the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. 

**orientation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Coordinate system axis. The default is `"Z"`. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object.
References

```
>>> oEditor.CreateBondwire

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> origin = [0,0,0]
>>> endpos = [10,5,20]
>>> #Material and name are not mandatory fields
>>> object_id = hfss.modeler.create_bondwire(origin,endpos,h1=0.5,h2=0.1,alpha=75,
...                                          beta=4,bond_type=0,name="mybox",material="copper")

```
Copy to clipboard
# create_bondwire 

Modeler3D.create_bondwire(_start : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _end : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _h1 : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.2_, _h2 : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _alpha : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 80_, _beta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _bond_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _diameter : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.025_, _facets : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 6_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Z'_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a bondwire. 

Parameters: 
     

**start**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the starting position of the bond pad. 

**end**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the ending position of the bond pad. 

**h1** float|str `optional` 
    
Height between the IC die I/O pad and the top of the bondwire. If the height is provided as a parameter, its value has to be provided as value + unit. The default is `0.2`. 

**h2** float|str `optional` 
    
Height of the IC die I/O pad above the lead frame. If the height is provided as a parameter, its value has to be provided as value + unit. The default is `0`. A negative value indicates that the I/O pad is below the lead frame. 

**alpha**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Angle in degrees between the xy plane and the wire bond at the IC die I/O pad. The default is `80`. 

**beta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Angle in degrees between the xy plane and the wire bond at the lead frame. The default is `5`. 

**bond_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Type of the boundwire, which indicates its shape. Options are:
  * ‘’0’’ for JEDEC 5-point
  * `1` for JEDEC 4-point
  * ‘’2`` for Low

The default is ‘’0``. 

**diameter** float|str `optional` 
    
Diameter of the wire. The default is `0.025`. 

**facets**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of wire facets. The default is `6`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the bondwire. The default is `None`, in which case the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. 

**orientation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Coordinate system axis. The default is `"Z"`. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object.
References

```
>>> oEditor.CreateBondwire

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> origin = [0,0,0]
>>> endpos = [10,5,20]
>>> #Material and name are not mandatory fields
>>> object_id = hfss.modeler.create_bondwire(origin,endpos,h1=0.5,h2=0.1,alpha=75,
...                                          beta=4,bond_type=0,name="mybox",material="copper")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_bondwire.rst.txt)

# create_bondwire 

Modeler3D.create_bondwire(_start : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _end : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _h1 : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.2_, _h2 : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _alpha : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 80_, _beta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 5_, _bond_type : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _diameter : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.025_, _facets : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 6_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _orientation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Z'_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a bondwire. 

Parameters: 
     

**start**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the starting position of the bond pad. 

**end**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the ending position of the bond pad. 

**h1** float|str `optional` 
    
Height between the IC die I/O pad and the top of the bondwire. If the height is provided as a parameter, its value has to be provided as value + unit. The default is `0.2`. 

**h2** float|str `optional` 
    
Height of the IC die I/O pad above the lead frame. If the height is provided as a parameter, its value has to be provided as value + unit. The default is `0`. A negative value indicates that the I/O pad is below the lead frame. 

**alpha**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Angle in degrees between the xy plane and the wire bond at the IC die I/O pad. The default is `80`. 

**beta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Angle in degrees between the xy plane and the wire bond at the lead frame. The default is `5`. 

**bond_type**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Type of the boundwire, which indicates its shape. Options are:
  * ‘’0’’ for JEDEC 5-point
  * `1` for JEDEC 4-point
  * ‘’2`` for Low

The default is ‘’0``. 

**diameter** float|str `optional` 
    
Diameter of the wire. The default is `0.025`. 

**facets**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of wire facets. The default is `6`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the bondwire. The default is `None`, in which case the default name is assigned. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the material. The default is `None`, in which case the default material is assigned. 

**orientation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Coordinate system axis. The default is `"Z"`. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object.
References

```
>>> oEditor.CreateBondwire

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> origin = [0,0,0]
>>> endpos = [10,5,20]
>>> #Material and name are not mandatory fields
>>> object_id = hfss.modeler.create_bondwire(origin,endpos,h1=0.5,h2=0.1,alpha=75,
...                                          beta=4,bond_type=0,name="mybox",material="copper")

```
Copy to clipboard