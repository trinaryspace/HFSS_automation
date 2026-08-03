---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_equationbased_curve.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_equationbased_curve 

Modeler3D.create_equationbased_curve(_x_t : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _y_t : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _z_t : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _t_start : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _t_end : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _num_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _xsection_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _xsection_orient : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _xsection_width : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 1_, _xsection_topwidth : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 1_, _xsection_height : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 1_, _xsection_num_seg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _xsection_bend_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create an equation-based curve. 

Parameters: 
     

**x_t**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Expression for the X-component of the curve as a function of `"_t"`. For example, `"3 * cos(_t)"`. 

**y_t**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Expression for the Y-component of the curve as a function of `"_t"` 

**z_t**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Expression for the Z-component of the curve as a function of `"_t"` 

**t_start**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Starting value of the parameter `"_t"`. 

**t_end**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Ending value of the parameter `"_t"`. 

**num_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of vertices on the segmented curve. The default is `0`, in which case the curve is non-segmented. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the created curve in the 3D modeler. The default is `None`, in which case the default name is assigned. 

**xsection_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the cross-section. Choices are `"Line"`, `"Circle"`, `"Rectangle"`, and `"Isosceles Trapezoid"`. The default is `None`. 

**xsection_orient**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Direction of the normal vector to the width of the cross-section. Choices are `"X"`, `"Y"`, `"Z"`, and `"Auto"`. The default is `None`, in which case the direction is set to `"Auto"`. 

**xsection_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Width or diameter of the cross-section for all types. The default is `1`. 

**xsection_topwidth**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Top width of the cross-section for type `"Isosceles Trapezoid"` only. The default is `1`. 

**xsection_height**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Height of the cross-section for types `"Rectangle"` and `"Isosceles Trapezoid"` only. The default is `1`. 

**xsection_num_seg**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments in the cross-section surface for types `"Circle"`, `"Rectangle"`, and `"Isosceles Trapezoid"`. The default is `0`. The value must be `0` or greater than `2`. 

**xsection_bend_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the bend for the cross-section. The default is `None`, in which case the bend type is set to `"Corner"`. For the type `"Circle"`, the bend type should be set to `"Curved"`. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object.
References

```
>>> oEditor.CreateEquationCurve

```
Copy to clipboard
Examples
The following example shows how to create an equation- based curve in HFSS. The required parameters are `cs_plane`, `position`, `major_radius`, `ratio`, and `is_covered`. The `cs_plane` parameter provides the plane that the ellipse is designed on. The `position` parameter provides the origin of the ellipse. The `major_radius` parameter provides the radius of the ellipse. The `ratio` parameter is a ratio between the major radius and minor radius of the ellipse. The `is_covered` parameter is a flag indicating if the ellipse is covered.
The optional parameter `matname` allows you to set the material name of the ellipse. The optional parameter `name` allows you to assign a name to the ellipse.
This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> eq_xsection = self.aedtapp.modeler.create_equationbased_curve(x_t="_t",
...                                                               y_t="_t*2",
...                                                               num_points=200,
...                                                               z_t=0,
...                                                               t_start=0.2,
...                                                               t_end=1.2,
...                                                               xsection_type="Circle")

```
Copy to clipboard
# create_equationbased_curve 

Modeler3D.create_equationbased_curve(_x_t : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _y_t : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _z_t : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _t_start : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _t_end : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _num_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _xsection_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _xsection_orient : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _xsection_width : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 1_, _xsection_topwidth : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 1_, _xsection_height : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 1_, _xsection_num_seg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _xsection_bend_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create an equation-based curve. 

Parameters: 
     

**x_t**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Expression for the X-component of the curve as a function of `"_t"`. For example, `"3 * cos(_t)"`. 

**y_t**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Expression for the Y-component of the curve as a function of `"_t"` 

**z_t**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Expression for the Z-component of the curve as a function of `"_t"` 

**t_start**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Starting value of the parameter `"_t"`. 

**t_end**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Ending value of the parameter `"_t"`. 

**num_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of vertices on the segmented curve. The default is `0`, in which case the curve is non-segmented. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the created curve in the 3D modeler. The default is `None`, in which case the default name is assigned. 

**xsection_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the cross-section. Choices are `"Line"`, `"Circle"`, `"Rectangle"`, and `"Isosceles Trapezoid"`. The default is `None`. 

**xsection_orient**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Direction of the normal vector to the width of the cross-section. Choices are `"X"`, `"Y"`, `"Z"`, and `"Auto"`. The default is `None`, in which case the direction is set to `"Auto"`. 

**xsection_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Width or diameter of the cross-section for all types. The default is `1`. 

**xsection_topwidth**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Top width of the cross-section for type `"Isosceles Trapezoid"` only. The default is `1`. 

**xsection_height**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Height of the cross-section for types `"Rectangle"` and `"Isosceles Trapezoid"` only. The default is `1`. 

**xsection_num_seg**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments in the cross-section surface for types `"Circle"`, `"Rectangle"`, and `"Isosceles Trapezoid"`. The default is `0`. The value must be `0` or greater than `2`. 

**xsection_bend_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the bend for the cross-section. The default is `None`, in which case the bend type is set to `"Corner"`. For the type `"Circle"`, the bend type should be set to `"Curved"`. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object.
References

```
>>> oEditor.CreateEquationCurve

```
Copy to clipboard
Examples
The following example shows how to create an equation- based curve in HFSS. The required parameters are `cs_plane`, `position`, `major_radius`, `ratio`, and `is_covered`. The `cs_plane` parameter provides the plane that the ellipse is designed on. The `position` parameter provides the origin of the ellipse. The `major_radius` parameter provides the radius of the ellipse. The `ratio` parameter is a ratio between the major radius and minor radius of the ellipse. The `is_covered` parameter is a flag indicating if the ellipse is covered.
The optional parameter `matname` allows you to set the material name of the ellipse. The optional parameter `name` allows you to assign a name to the ellipse.
This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> eq_xsection = self.aedtapp.modeler.create_equationbased_curve(x_t="_t",
...                                                               y_t="_t*2",
...                                                               num_points=200,
...                                                               z_t=0,
...                                                               t_start=0.2,
...                                                               t_end=1.2,
...                                                               xsection_type="Circle")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_equationbased_curve.rst.txt)

# create_equationbased_curve 

Modeler3D.create_equationbased_curve(_x_t : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _y_t : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _z_t : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _t_start : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _t_end : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _num_points : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _xsection_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _xsection_orient : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _xsection_width : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 1_, _xsection_topwidth : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 1_, _xsection_height : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 1_, _xsection_num_seg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _xsection_bend_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create an equation-based curve. 

Parameters: 
     

**x_t**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Expression for the X-component of the curve as a function of `"_t"`. For example, `"3 * cos(_t)"`. 

**y_t**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Expression for the Y-component of the curve as a function of `"_t"` 

**z_t**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Expression for the Z-component of the curve as a function of `"_t"` 

**t_start**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Starting value of the parameter `"_t"`. 

**t_end**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Ending value of the parameter `"_t"`. 

**num_points**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of vertices on the segmented curve. The default is `0`, in which case the curve is non-segmented. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the created curve in the 3D modeler. The default is `None`, in which case the default name is assigned. 

**xsection_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the cross-section. Choices are `"Line"`, `"Circle"`, `"Rectangle"`, and `"Isosceles Trapezoid"`. The default is `None`. 

**xsection_orient**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Direction of the normal vector to the width of the cross-section. Choices are `"X"`, `"Y"`, `"Z"`, and `"Auto"`. The default is `None`, in which case the direction is set to `"Auto"`. 

**xsection_width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Width or diameter of the cross-section for all types. The default is `1`. 

**xsection_topwidth**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Top width of the cross-section for type `"Isosceles Trapezoid"` only. The default is `1`. 

**xsection_height**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Height of the cross-section for types `"Rectangle"` and `"Isosceles Trapezoid"` only. The default is `1`. 

**xsection_num_seg**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments in the cross-section surface for types `"Circle"`, `"Rectangle"`, and `"Isosceles Trapezoid"`. The default is `0`. The value must be `0` or greater than `2`. 

**xsection_bend_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the bend for the cross-section. The default is `None`, in which case the bend type is set to `"Corner"`. For the type `"Circle"`, the bend type should be set to `"Curved"`. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object.
References

```
>>> oEditor.CreateEquationCurve

```
Copy to clipboard
Examples
The following example shows how to create an equation- based curve in HFSS. The required parameters are `cs_plane`, `position`, `major_radius`, `ratio`, and `is_covered`. The `cs_plane` parameter provides the plane that the ellipse is designed on. The `position` parameter provides the origin of the ellipse. The `major_radius` parameter provides the radius of the ellipse. The `ratio` parameter is a ratio between the major radius and minor radius of the ellipse. The `is_covered` parameter is a flag indicating if the ellipse is covered.
The optional parameter `matname` allows you to set the material name of the ellipse. The optional parameter `name` allows you to assign a name to the ellipse.
This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> eq_xsection = self.aedtapp.modeler.create_equationbased_curve(x_t="_t",
...                                                               y_t="_t*2",
...                                                               num_points=200,
...                                                               z_t=0,
...                                                               t_start=0.2,
...                                                               t_end=1.2,
...                                                               xsection_type="Circle")

```
Copy to clipboard