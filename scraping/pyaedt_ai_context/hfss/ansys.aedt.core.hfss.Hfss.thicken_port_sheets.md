---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.thicken_port_sheets.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# thicken_port_sheets 

Hfss.thicken_port_sheets(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _value : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _extrude_internally : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _internal_extrusion : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 1_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Create thickened sheets over a list of input port sheets.
This method is built to work with the output of `modeler.find_port_faces`. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the sheets to thicken. 

**value**
    
Value in millimeters for thickening the faces. 

**extrude_internally**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to extrude the sheets internally (going into the model). The default is `True`. 

**internal_extrusion**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Value in millimeters for thickening the sheets internally if `internalExtr=True`. The default is `1`. 

Returns: 
     

`Dict`
    
For each input sheet, returns the port IDs where thickened sheets were created if the name contains the word “Vacuum”.
References

```
>>> oEditor.ThickenSheet

```
Copy to clipboard
Examples
Create a circle sheet and use it to create a wave port. Set the thickness of this circle sheet to `"2 mm"`.

```
>>> from ansys.aedt.core.generic.constants import Plane
>>> sheet_for_thickness = hfss.modeler.create_circle(Plane.YZ, [60, 60, 60], 10, name="SheetForThickness")
>>> port_for_thickness = hfss.create_wave_port_from_sheet(
...     sheet_for_thickness, 5, hfss.axis_directions.XNeg, 40, 2, "WavePortForThickness", True
... )
>>> hfss.thicken_port_sheets(["SheetForThickness"], 2)
PyAEDT INFO: done
{}

```
Copy to clipboard
# thicken_port_sheets 

Hfss.thicken_port_sheets(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _value : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _extrude_internally : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _internal_extrusion : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 1_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Create thickened sheets over a list of input port sheets.
This method is built to work with the output of `modeler.find_port_faces`. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the sheets to thicken. 

**value**
    
Value in millimeters for thickening the faces. 

**extrude_internally**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to extrude the sheets internally (going into the model). The default is `True`. 

**internal_extrusion**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Value in millimeters for thickening the sheets internally if `internalExtr=True`. The default is `1`. 

Returns: 
     

`Dict`
    
For each input sheet, returns the port IDs where thickened sheets were created if the name contains the word “Vacuum”.
References

```
>>> oEditor.ThickenSheet

```
Copy to clipboard
Examples
Create a circle sheet and use it to create a wave port. Set the thickness of this circle sheet to `"2 mm"`.

```
>>> from ansys.aedt.core.generic.constants import Plane
>>> sheet_for_thickness = hfss.modeler.create_circle(Plane.YZ, [60, 60, 60], 10, name="SheetForThickness")
>>> port_for_thickness = hfss.create_wave_port_from_sheet(
...     sheet_for_thickness, 5, hfss.axis_directions.XNeg, 40, 2, "WavePortForThickness", True
... )
>>> hfss.thicken_port_sheets(["SheetForThickness"], 2)
PyAEDT INFO: done
{}

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.thicken_port_sheets.rst.txt)

# thicken_port_sheets 

Hfss.thicken_port_sheets(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _value : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _extrude_internally : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _internal_extrusion : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 1_) → [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Create thickened sheets over a list of input port sheets.
This method is built to work with the output of `modeler.find_port_faces`. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
List of the sheets to thicken. 

**value**
    
Value in millimeters for thickening the faces. 

**extrude_internally**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to extrude the sheets internally (going into the model). The default is `True`. 

**internal_extrusion**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Value in millimeters for thickening the sheets internally if `internalExtr=True`. The default is `1`. 

Returns: 
     

`Dict`
    
For each input sheet, returns the port IDs where thickened sheets were created if the name contains the word “Vacuum”.
References

```
>>> oEditor.ThickenSheet

```
Copy to clipboard
Examples
Create a circle sheet and use it to create a wave port. Set the thickness of this circle sheet to `"2 mm"`.

```
>>> from ansys.aedt.core.generic.constants import Plane
>>> sheet_for_thickness = hfss.modeler.create_circle(Plane.YZ, [60, 60, 60], 10, name="SheetForThickness")
>>> port_for_thickness = hfss.create_wave_port_from_sheet(
...     sheet_for_thickness, 5, hfss.axis_directions.XNeg, 40, 2, "WavePortForThickness", True
... )
>>> hfss.thicken_port_sheets(["SheetForThickness"], 2)
PyAEDT INFO: done
{}

```
Copy to clipboard