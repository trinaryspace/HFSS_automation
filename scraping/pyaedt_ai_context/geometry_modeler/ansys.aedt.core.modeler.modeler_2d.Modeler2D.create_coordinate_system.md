---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.create_coordinate_system.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_coordinate_system 

Modeler2D.create_coordinate_system(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _reference_cs : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _mode : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'axis'_, _view : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'iso'_, _x_pointing : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _y_pointing : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _psi : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _phi : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _u : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [CoordinateSystem](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem") 
    
Create a coordinate system. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of `[x, y, z]` coordinates for the origin of the coordinate system. The default is `None`, in which case `[0, 0, 0]` is used. 

**reference_cs**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the reference coordinate system. The default is `"Global"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system. The default is `None`. 

**mode**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Definition mode. Options are `"axis"`, `"axisrotation"`, `"view"`, `"zxz"`, and `"zyz"` The default is `"axis"`. You can also use the `ansys.aedt.core.generic.constants.CSMode` enumerator.
  * If `mode="axis"`, specify the `x_pointing` and `y_pointing` parameters.
  * If `mode="axisrotation"`, specify the `theta` and `u` parameters.
  * If `mode="view"`, specify the `view` parameter.
  * If `mode="zxz"` or `mode="zyz"`, specify the `phi`, `theta`, and `psi` parameters.

Parameters not needed by the specified mode are ignored. The default mode, `"axis"`, is a coordinate system parallel to the global coordinate system centered in the global origin. 

**view**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") `optional` 
    
View for the coordinate system if `mode="view"`. Options are `"iso"`, `None`, `"XY"`, `"XZ"`, and `"XY"`. The default is `"iso"`. The `"rotate"` option is obsolete. You can also use the `ansys.aedt.core.generic.constants.View` enumerator.
Note
For backward compatibility, `mode="view", view="rotate"` are the same as `mode="axis"`. Because the “rotate” option in the “view” mode is obsolete, use `mode="axis"` instead. 

**x_pointing**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of the `[x, y, z]` coordinates specifying the X axis pointing in the global coordinate system if `mode="axis"`. The default is `[1, 0, 0]`. 

**y_pointing**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of the `[x, y, z]` coordinates specifying the Y axis pointing in the global coordinate system if `mode="axis"`. The default is `[0, 1, 0]`. 

**phi**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Euler angle phi in degrees if `mode="zxz"` or `mode="zyz"`. The default is `0`. 

**theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Euler angle theta or rotation angle in degrees if `mode="zxz"`, `mode="zyz"`, or `mode="axisrotation"`. The default is `0`. 

**psi**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Euler angle psi in degrees if `mode="zxz"` or `mode="zyz"`. The default is `0`. 

**u**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[ux, uy, uz]` coordinates for the rotation axis if `mode="zxz"`. The default is `[1, 0, 0]`. 

Returns: 
     

`ansys.aedt.core.modeler.Modeler.CoordinateSystem`
    
Created coordinate system.
References

```
>>> oEditor.CreateRelativeCS

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_coordinate_system(origin=[0, 0, 0], name="CS1")

```
Copy to clipboard
# create_coordinate_system 

Modeler2D.create_coordinate_system(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _reference_cs : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _mode : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'axis'_, _view : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'iso'_, _x_pointing : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _y_pointing : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _psi : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _phi : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _u : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [CoordinateSystem](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem") 
    
Create a coordinate system. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of `[x, y, z]` coordinates for the origin of the coordinate system. The default is `None`, in which case `[0, 0, 0]` is used. 

**reference_cs**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the reference coordinate system. The default is `"Global"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system. The default is `None`. 

**mode**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Definition mode. Options are `"axis"`, `"axisrotation"`, `"view"`, `"zxz"`, and `"zyz"` The default is `"axis"`. You can also use the `ansys.aedt.core.generic.constants.CSMode` enumerator.
  * If `mode="axis"`, specify the `x_pointing` and `y_pointing` parameters.
  * If `mode="axisrotation"`, specify the `theta` and `u` parameters.
  * If `mode="view"`, specify the `view` parameter.
  * If `mode="zxz"` or `mode="zyz"`, specify the `phi`, `theta`, and `psi` parameters.

Parameters not needed by the specified mode are ignored. The default mode, `"axis"`, is a coordinate system parallel to the global coordinate system centered in the global origin. 

**view**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") `optional` 
    
View for the coordinate system if `mode="view"`. Options are `"iso"`, `None`, `"XY"`, `"XZ"`, and `"XY"`. The default is `"iso"`. The `"rotate"` option is obsolete. You can also use the `ansys.aedt.core.generic.constants.View` enumerator.
Note
For backward compatibility, `mode="view", view="rotate"` are the same as `mode="axis"`. Because the “rotate” option in the “view” mode is obsolete, use `mode="axis"` instead. 

**x_pointing**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of the `[x, y, z]` coordinates specifying the X axis pointing in the global coordinate system if `mode="axis"`. The default is `[1, 0, 0]`. 

**y_pointing**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of the `[x, y, z]` coordinates specifying the Y axis pointing in the global coordinate system if `mode="axis"`. The default is `[0, 1, 0]`. 

**phi**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Euler angle phi in degrees if `mode="zxz"` or `mode="zyz"`. The default is `0`. 

**theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Euler angle theta or rotation angle in degrees if `mode="zxz"`, `mode="zyz"`, or `mode="axisrotation"`. The default is `0`. 

**psi**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Euler angle psi in degrees if `mode="zxz"` or `mode="zyz"`. The default is `0`. 

**u**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[ux, uy, uz]` coordinates for the rotation axis if `mode="zxz"`. The default is `[1, 0, 0]`. 

Returns: 
     

`ansys.aedt.core.modeler.Modeler.CoordinateSystem`
    
Created coordinate system.
References

```
>>> oEditor.CreateRelativeCS

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_coordinate_system(origin=[0, 0, 0], name="CS1")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.create_coordinate_system.rst.txt)

# create_coordinate_system 

Modeler2D.create_coordinate_system(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _reference_cs : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _mode : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'axis'_, _view : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'iso'_, _x_pointing : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _y_pointing : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _psi : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _phi : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _u : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [CoordinateSystem](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem") 
    
Create a coordinate system. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of `[x, y, z]` coordinates for the origin of the coordinate system. The default is `None`, in which case `[0, 0, 0]` is used. 

**reference_cs**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the reference coordinate system. The default is `"Global"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the coordinate system. The default is `None`. 

**mode**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Definition mode. Options are `"axis"`, `"axisrotation"`, `"view"`, `"zxz"`, and `"zyz"` The default is `"axis"`. You can also use the `ansys.aedt.core.generic.constants.CSMode` enumerator.
  * If `mode="axis"`, specify the `x_pointing` and `y_pointing` parameters.
  * If `mode="axisrotation"`, specify the `theta` and `u` parameters.
  * If `mode="view"`, specify the `view` parameter.
  * If `mode="zxz"` or `mode="zyz"`, specify the `phi`, `theta`, and `psi` parameters.

Parameters not needed by the specified mode are ignored. The default mode, `"axis"`, is a coordinate system parallel to the global coordinate system centered in the global origin. 

**view**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") `optional` 
    
View for the coordinate system if `mode="view"`. Options are `"iso"`, `None`, `"XY"`, `"XZ"`, and `"XY"`. The default is `"iso"`. The `"rotate"` option is obsolete. You can also use the `ansys.aedt.core.generic.constants.View` enumerator.
Note
For backward compatibility, `mode="view", view="rotate"` are the same as `mode="axis"`. Because the “rotate” option in the “view” mode is obsolete, use `mode="axis"` instead. 

**x_pointing**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of the `[x, y, z]` coordinates specifying the X axis pointing in the global coordinate system if `mode="axis"`. The default is `[1, 0, 0]`. 

**y_pointing**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of the `[x, y, z]` coordinates specifying the Y axis pointing in the global coordinate system if `mode="axis"`. The default is `[0, 1, 0]`. 

**phi**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Euler angle phi in degrees if `mode="zxz"` or `mode="zyz"`. The default is `0`. 

**theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Euler angle theta or rotation angle in degrees if `mode="zxz"`, `mode="zyz"`, or `mode="axisrotation"`. The default is `0`. 

**psi**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Euler angle psi in degrees if `mode="zxz"` or `mode="zyz"`. The default is `0`. 

**u**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[ux, uy, uz]` coordinates for the rotation axis if `mode="zxz"`. The default is `[1, 0, 0]`. 

Returns: 
     

`ansys.aedt.core.modeler.Modeler.CoordinateSystem`
    
Created coordinate system.
References

```
>>> oEditor.CreateRelativeCS

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.primitives import GeometryModeler
>>> obj = GeometryModeler()
>>> obj.create_coordinate_system(origin=[0, 0, 0], name="CS1")

```
Copy to clipboard