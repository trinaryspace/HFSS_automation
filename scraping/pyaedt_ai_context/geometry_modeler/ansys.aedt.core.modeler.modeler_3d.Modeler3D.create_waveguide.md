---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_waveguide.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_waveguide 

Modeler3D.create_waveguide(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _wg_direction_axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _wgmodel : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'WG0'_, _wg_length : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 100_, _wg_thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _wg_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'aluminum'_, _parametrize_w : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _parametrize_h : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _create_sheets_on_openings : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")['Object3d', 'Object3d'] 
    
Create a standard waveguide and optionally parametrize W and H.
Available models are WG0.0, WG0, WG1, WG2, WG3, WG4, WG5, WG6, WG7, WG8, WG9, WG9A, WG10, WG11, WG11A, WG12, WG13, WG14, WG15, WR102, WG16, WG17, WG18, WG19, WG20, WG21, WG22, WG24, WG25, WG26, WG27, WG28, WG29, WG29, WG30, WG31, and WG32. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the original position. 

**wg_direction_axis**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Coordinate system axis (integer `0` for X, `1` for Y, `2` for Z) or the [`ansys.aedt.core.generic.constants.Axis`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis") enumerator. 

**wgmodel**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Waveguide model. The default is `"WG0"`. 

**wg_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Waveguide length. The default is `100`. 

**wg_thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Waveguide thickness. The default is `None`, in which case the thickness is wg_height/20. 

**wg_material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Waveguide material. The default is `"aluminum"`. 

**parametrize_w**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to parametrize W. The default is `False`. 

**parametrize_h**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to parametrize H. The default is `False`. 

**create_sheets_on_openings**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create sheets on both openings. The default is `False`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the waveguide. The default is `None`. 

Returns: 
     

`Tuple`[[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")]
    
Objects created by the waveguide.
References

```
>>> oEditor.CreateBox
>>> oEditor.AssignMaterial

```
Copy to clipboard
Examples
This example shows how to create a WG9 waveguide.

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.generic.constants import Axis
>>> app = Hfss()
>>> position = [0, 0, 0]
>>> wg1 = app.modeler.create_waveguide(position, Axis.X, wgmodel="WG9", wg_length=2000)

```
Copy to clipboard
# create_waveguide 

Modeler3D.create_waveguide(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _wg_direction_axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _wgmodel : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'WG0'_, _wg_length : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 100_, _wg_thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _wg_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'aluminum'_, _parametrize_w : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _parametrize_h : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _create_sheets_on_openings : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")['Object3d', 'Object3d'] 
    
Create a standard waveguide and optionally parametrize W and H.
Available models are WG0.0, WG0, WG1, WG2, WG3, WG4, WG5, WG6, WG7, WG8, WG9, WG9A, WG10, WG11, WG11A, WG12, WG13, WG14, WG15, WR102, WG16, WG17, WG18, WG19, WG20, WG21, WG22, WG24, WG25, WG26, WG27, WG28, WG29, WG29, WG30, WG31, and WG32. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the original position. 

**wg_direction_axis**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Coordinate system axis (integer `0` for X, `1` for Y, `2` for Z) or the [`ansys.aedt.core.generic.constants.Axis`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis") enumerator. 

**wgmodel**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Waveguide model. The default is `"WG0"`. 

**wg_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Waveguide length. The default is `100`. 

**wg_thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Waveguide thickness. The default is `None`, in which case the thickness is wg_height/20. 

**wg_material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Waveguide material. The default is `"aluminum"`. 

**parametrize_w**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to parametrize W. The default is `False`. 

**parametrize_h**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to parametrize H. The default is `False`. 

**create_sheets_on_openings**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create sheets on both openings. The default is `False`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the waveguide. The default is `None`. 

Returns: 
     

`Tuple`[[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")]
    
Objects created by the waveguide.
References

```
>>> oEditor.CreateBox
>>> oEditor.AssignMaterial

```
Copy to clipboard
Examples
This example shows how to create a WG9 waveguide.

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.generic.constants import Axis
>>> app = Hfss()
>>> position = [0, 0, 0]
>>> wg1 = app.modeler.create_waveguide(position, Axis.X, wgmodel="WG9", wg_length=2000)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_waveguide.rst.txt)

# create_waveguide 

Modeler3D.create_waveguide(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _wg_direction_axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _wgmodel : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'WG0'_, _wg_length : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 100_, _wg_thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_, _wg_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'aluminum'_, _parametrize_w : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _parametrize_h : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _create_sheets_on_openings : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")['Object3d', 'Object3d'] 
    
Create a standard waveguide and optionally parametrize W and H.
Available models are WG0.0, WG0, WG1, WG2, WG3, WG4, WG5, WG6, WG7, WG8, WG9, WG9A, WG10, WG11, WG11A, WG12, WG13, WG14, WG15, WR102, WG16, WG17, WG18, WG19, WG20, WG21, WG22, WG24, WG25, WG26, WG27, WG28, WG29, WG29, WG30, WG31, and WG32. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the original position. 

**wg_direction_axis**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Coordinate system axis (integer `0` for X, `1` for Y, `2` for Z) or the [`ansys.aedt.core.generic.constants.Axis`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis") enumerator. 

**wgmodel**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Waveguide model. The default is `"WG0"`. 

**wg_length**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Waveguide length. The default is `100`. 

**wg_thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Waveguide thickness. The default is `None`, in which case the thickness is wg_height/20. 

**wg_material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Waveguide material. The default is `"aluminum"`. 

**parametrize_w**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to parametrize W. The default is `False`. 

**parametrize_h**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to parametrize H. The default is `False`. 

**create_sheets_on_openings**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create sheets on both openings. The default is `False`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the waveguide. The default is `None`. 

Returns: 
     

`Tuple`[[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")]
    
Objects created by the waveguide.
References

```
>>> oEditor.CreateBox
>>> oEditor.AssignMaterial

```
Copy to clipboard
Examples
This example shows how to create a WG9 waveguide.

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.generic.constants import Axis
>>> app = Hfss()
>>> position = [0, 0, 0]
>>> wg1 = app.modeler.create_waveguide(position, Axis.X, wgmodel="WG9", wg_length=2000)

```
Copy to clipboard