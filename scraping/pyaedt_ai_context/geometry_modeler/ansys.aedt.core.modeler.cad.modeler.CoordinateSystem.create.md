---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.create.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create 

CoordinateSystem.create(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _reference_cs : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _mode : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'axis'_, _view : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'iso'_, _x_pointing : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _y_pointing : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _phi : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _psi : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _u : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a coordinate system. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the origin of the coordinate system. The default is `None`, in which case `[0, 0, 0]` is used. 

**reference_cs**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the reference coordinate system. The default is `"Global"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the coordinate system. The default is `None`. 

**mode**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Definition mode. Options are `"view"`, `"axis"`, `"zxz"`, `"zyz"`, and `"axisrotation"`. The default is `"axis"`.
  * If `mode="view"`, specify `view`.
  * If `mode="axis"`, specify `x_pointing` and `y_pointing`.
  * If `mode="zxz"` or `mode="zyz"`, specify `phi`, `theta`, and `psi`.
  * If `mode="axisrotation"`, specify `theta` and `u`.

Parameters not needed by the specified mode are ignored. For back compatibility, `view="rotate"` is the same as `mode="axis"`. The mode `"axisrotation"` is a coordinate system parallel to the global coordinate system centered in the global origin. 

**view**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
View for the coordinate system if `mode="view"`. Options are `"XY"`, `"XZ"`, `"XY"`, `"iso"`, `None`, and `"rotate"` (obsolete). The default is `"iso"`.
Note
Because the `"rotate"` option is obsolete, use `mode="axis"` instead. 

**x_pointing**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of the `[x, y, z]` coordinates specifying the X axis pointing in the local coordinate system if `mode="axis"`. The default is `[1, 0, 0]`. 

**y_pointing**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of the `[x, y, z]` coordinates specifying the Y axis pointing in the local coordinate system if `mode="axis"`. The default is `[0, 1, 0]`. 

**phi**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Euler angle phi in degrees if `mode="zxz"` or `mode="zyz"`. The default is `0`. 

**theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Euler angle theta or rotation angle in degrees if `mode="zxz"`, `mode="zyz"`, or `mode="axisrotation"`. The default is `0`. 

**psi**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Euler angle psi in degrees if `mode="zxz"` or `mode="zyz"`. The default is `0`. 

**u**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[ux, uy, uz]` coordinates for the rotation axis if `mode="zxz"`. The default is `[1, 0, 0]`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.cad.modeler import CoordinateSystem
>>> obj = CoordinateSystem()
>>> obj.create(name="MyObject", origin=[0, 0, 0])

```
Copy to clipboard
# create 

CoordinateSystem.create(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _reference_cs : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _mode : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'axis'_, _view : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'iso'_, _x_pointing : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _y_pointing : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _phi : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _psi : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _u : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a coordinate system. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the origin of the coordinate system. The default is `None`, in which case `[0, 0, 0]` is used. 

**reference_cs**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the reference coordinate system. The default is `"Global"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the coordinate system. The default is `None`. 

**mode**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Definition mode. Options are `"view"`, `"axis"`, `"zxz"`, `"zyz"`, and `"axisrotation"`. The default is `"axis"`.
  * If `mode="view"`, specify `view`.
  * If `mode="axis"`, specify `x_pointing` and `y_pointing`.
  * If `mode="zxz"` or `mode="zyz"`, specify `phi`, `theta`, and `psi`.
  * If `mode="axisrotation"`, specify `theta` and `u`.

Parameters not needed by the specified mode are ignored. For back compatibility, `view="rotate"` is the same as `mode="axis"`. The mode `"axisrotation"` is a coordinate system parallel to the global coordinate system centered in the global origin. 

**view**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
View for the coordinate system if `mode="view"`. Options are `"XY"`, `"XZ"`, `"XY"`, `"iso"`, `None`, and `"rotate"` (obsolete). The default is `"iso"`.
Note
Because the `"rotate"` option is obsolete, use `mode="axis"` instead. 

**x_pointing**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of the `[x, y, z]` coordinates specifying the X axis pointing in the local coordinate system if `mode="axis"`. The default is `[1, 0, 0]`. 

**y_pointing**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of the `[x, y, z]` coordinates specifying the Y axis pointing in the local coordinate system if `mode="axis"`. The default is `[0, 1, 0]`. 

**phi**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Euler angle phi in degrees if `mode="zxz"` or `mode="zyz"`. The default is `0`. 

**theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Euler angle theta or rotation angle in degrees if `mode="zxz"`, `mode="zyz"`, or `mode="axisrotation"`. The default is `0`. 

**psi**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Euler angle psi in degrees if `mode="zxz"` or `mode="zyz"`. The default is `0`. 

**u**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[ux, uy, uz]` coordinates for the rotation axis if `mode="zxz"`. The default is `[1, 0, 0]`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.cad.modeler import CoordinateSystem
>>> obj = CoordinateSystem()
>>> obj.create(name="MyObject", origin=[0, 0, 0])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.create.rst.txt)

# create 

CoordinateSystem.create(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _reference_cs : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Global'_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _mode : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'axis'_, _view : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'iso'_, _x_pointing : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _y_pointing : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _phi : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _theta : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _psi : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _u : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create a coordinate system. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of `[x, y, z]` coordinates for the origin of the coordinate system. The default is `None`, in which case `[0, 0, 0]` is used. 

**reference_cs**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the reference coordinate system. The default is `"Global"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the coordinate system. The default is `None`. 

**mode**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Definition mode. Options are `"view"`, `"axis"`, `"zxz"`, `"zyz"`, and `"axisrotation"`. The default is `"axis"`.
  * If `mode="view"`, specify `view`.
  * If `mode="axis"`, specify `x_pointing` and `y_pointing`.
  * If `mode="zxz"` or `mode="zyz"`, specify `phi`, `theta`, and `psi`.
  * If `mode="axisrotation"`, specify `theta` and `u`.

Parameters not needed by the specified mode are ignored. For back compatibility, `view="rotate"` is the same as `mode="axis"`. The mode `"axisrotation"` is a coordinate system parallel to the global coordinate system centered in the global origin. 

**view**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
View for the coordinate system if `mode="view"`. Options are `"XY"`, `"XZ"`, `"XY"`, `"iso"`, `None`, and `"rotate"` (obsolete). The default is `"iso"`.
Note
Because the `"rotate"` option is obsolete, use `mode="axis"` instead. 

**x_pointing**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of the `[x, y, z]` coordinates specifying the X axis pointing in the local coordinate system if `mode="axis"`. The default is `[1, 0, 0]`. 

**y_pointing**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of the `[x, y, z]` coordinates specifying the Y axis pointing in the local coordinate system if `mode="axis"`. The default is `[0, 1, 0]`. 

**phi**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Euler angle phi in degrees if `mode="zxz"` or `mode="zyz"`. The default is `0`. 

**theta**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Euler angle theta or rotation angle in degrees if `mode="zxz"`, `mode="zyz"`, or `mode="axisrotation"`. The default is `0`. 

**psi**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Euler angle psi in degrees if `mode="zxz"` or `mode="zyz"`. The default is `0`. 

**u**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the `[ux, uy, uz]` coordinates for the rotation axis if `mode="zxz"`. The default is `[1, 0, 0]`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.modeler.cad.modeler import CoordinateSystem
>>> obj = CoordinateSystem()
>>> obj.create(name="MyObject", origin=[0, 0, 0])

```
Copy to clipboard