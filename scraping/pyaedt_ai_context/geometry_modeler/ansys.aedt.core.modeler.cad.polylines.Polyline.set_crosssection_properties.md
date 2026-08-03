---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.Polyline.set_crosssection_properties.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# set_crosssection_properties 

Polyline.set_crosssection_properties(_section : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _orient : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _topwidth : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _num_seg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _bend_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set the properties of an existing polyline object. 

Parameters: 
     

**section**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Types of the cross-sections. Options are `"Line"`, `"Circle"`, `"Rectangle"`, and `"Isosceles Trapezoid"`. The default is `None`. 

**orient**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Direction of the normal vector to the width of the cross-section. Options are `"X"`, `"Y"`, `"Z"`, and `"Auto"`. The default is `None`, which sets the orientation to `"Auto"`. 

**width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Width or diameter of the cross-section for all types. The default is `0`. 

**topwidth**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Top width of the cross-section for the type `"Isosceles Trapezoid"` only. The default is `0`. 

**height**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Height of the cross-section for the types `"Rectangle"` and “Isosceles Trapezoid”` only. The default is `0`. 

**num_seg**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments in the cross-section surface for the types `"Circle"`, `"Rectangle"`, and `"Isosceles Trapezoid"`. The default is `0`. The value must be `0` or greater than `2`. 

**bend_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the bend. The default is `None`, in which case the bend type is set to `"Corner"`. For the type `"Circle"`, the bend type should be set to `"Curved"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.ChangeProperty

```
Copy to clipboard
Examples

```
>>> P = modeler.create_polyline([[0, 1, 2], [0, 2, 3], [2, 1, 4]])
>>> P.set_crosssection_properties(section="Circle", width="1mm")

```
Copy to clipboard
# set_crosssection_properties 

Polyline.set_crosssection_properties(_section : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _orient : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _topwidth : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _num_seg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _bend_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set the properties of an existing polyline object. 

Parameters: 
     

**section**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Types of the cross-sections. Options are `"Line"`, `"Circle"`, `"Rectangle"`, and `"Isosceles Trapezoid"`. The default is `None`. 

**orient**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Direction of the normal vector to the width of the cross-section. Options are `"X"`, `"Y"`, `"Z"`, and `"Auto"`. The default is `None`, which sets the orientation to `"Auto"`. 

**width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Width or diameter of the cross-section for all types. The default is `0`. 

**topwidth**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Top width of the cross-section for the type `"Isosceles Trapezoid"` only. The default is `0`. 

**height**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Height of the cross-section for the types `"Rectangle"` and “Isosceles Trapezoid”` only. The default is `0`. 

**num_seg**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments in the cross-section surface for the types `"Circle"`, `"Rectangle"`, and `"Isosceles Trapezoid"`. The default is `0`. The value must be `0` or greater than `2`. 

**bend_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the bend. The default is `None`, in which case the bend type is set to `"Corner"`. For the type `"Circle"`, the bend type should be set to `"Curved"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.ChangeProperty

```
Copy to clipboard
Examples

```
>>> P = modeler.create_polyline([[0, 1, 2], [0, 2, 3], [2, 1, 4]])
>>> P.set_crosssection_properties(section="Circle", width="1mm")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.polylines.Polyline.set_crosssection_properties.rst.txt)

# set_crosssection_properties 

Polyline.set_crosssection_properties(_section : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _orient : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _width : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _topwidth : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _height : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _num_seg : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _bend_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set the properties of an existing polyline object. 

Parameters: 
     

**section**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Types of the cross-sections. Options are `"Line"`, `"Circle"`, `"Rectangle"`, and `"Isosceles Trapezoid"`. The default is `None`. 

**orient**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Direction of the normal vector to the width of the cross-section. Options are `"X"`, `"Y"`, `"Z"`, and `"Auto"`. The default is `None`, which sets the orientation to `"Auto"`. 

**width**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Width or diameter of the cross-section for all types. The default is `0`. 

**topwidth**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Top width of the cross-section for the type `"Isosceles Trapezoid"` only. The default is `0`. 

**height**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Height of the cross-section for the types `"Rectangle"` and “Isosceles Trapezoid”` only. The default is `0`. 

**num_seg**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments in the cross-section surface for the types `"Circle"`, `"Rectangle"`, and `"Isosceles Trapezoid"`. The default is `0`. The value must be `0` or greater than `2`. 

**bend_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of the bend. The default is `None`, in which case the bend type is set to `"Corner"`. For the type `"Circle"`, the bend type should be set to `"Curved"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.ChangeProperty

```
Copy to clipboard
Examples

```
>>> P = modeler.create_polyline([[0, 1, 2], [0, 2, 3], [2, 1, 4]])
>>> P.set_crosssection_properties(section="Circle", width="1mm")

```
Copy to clipboard