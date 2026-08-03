---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram.eye_mask.html"
category: "reports"
domain: "PyAEDT / HFSS"
---

# eye_mask 

AMIConturEyeDiagram.eye_mask(_points : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _x_units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'ns'_, _y_units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'mV'_, _enable_limits : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _upper_limit : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 500_, _lower_limit : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = -500_, _color : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (0, 255, 0)_, _x_offset : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0ns'_, _y_offset : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0V'_, _transparency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.3_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create an eye diagram in the plot. 

Parameters: 
     

**points**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Points of the eye mask in the format `[[x1,y1,],[x2,y2],...]`. 

**x_units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
X points units. The default is `"ns"`. 

**y_units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Y points units. The default is `"mV"`. 

**enable_limits**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable the upper and lower limits. The default is `False`. 

**upper_limit**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Upper limit if limits are enabled. The default is `500`. 

**lower_limit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Lower limit if limits are enabled. The default is `-500`. 

**color**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), `optional` 
    
Mask in (R, G, B) color. The default is `(0, 255, 0)`. Each color value must be an integer in a range from 0 to 255. 

**x_offset**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Mask time offset with units. The default is `"0ns"`. 

**y_offset**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Mask value offset with units. The default is `"0V"`. 

**transparency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Mask transparency. The default is `0.3`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.report.eye import AMIConturEyeDiagram
>>> obj = AMIConturEyeDiagram.__new__(AMIConturEyeDiagram)
>>> obj.eye_mask([[0, 0], [1, 1]])

```
Copy to clipboard
# eye_mask 

AMIConturEyeDiagram.eye_mask(_points : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _x_units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'ns'_, _y_units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'mV'_, _enable_limits : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _upper_limit : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 500_, _lower_limit : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = -500_, _color : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (0, 255, 0)_, _x_offset : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0ns'_, _y_offset : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0V'_, _transparency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.3_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create an eye diagram in the plot. 

Parameters: 
     

**points**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Points of the eye mask in the format `[[x1,y1,],[x2,y2],...]`. 

**x_units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
X points units. The default is `"ns"`. 

**y_units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Y points units. The default is `"mV"`. 

**enable_limits**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable the upper and lower limits. The default is `False`. 

**upper_limit**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Upper limit if limits are enabled. The default is `500`. 

**lower_limit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Lower limit if limits are enabled. The default is `-500`. 

**color**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), `optional` 
    
Mask in (R, G, B) color. The default is `(0, 255, 0)`. Each color value must be an integer in a range from 0 to 255. 

**x_offset**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Mask time offset with units. The default is `"0ns"`. 

**y_offset**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Mask value offset with units. The default is `"0V"`. 

**transparency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Mask transparency. The default is `0.3`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.report.eye import AMIConturEyeDiagram
>>> obj = AMIConturEyeDiagram.__new__(AMIConturEyeDiagram)
>>> obj.eye_mask([[0, 0], [1, 1]])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram.eye_mask.rst.txt)

# eye_mask 

AMIConturEyeDiagram.eye_mask(_points : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _x_units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'ns'_, _y_units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'mV'_, _enable_limits : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _upper_limit : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 500_, _lower_limit : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = -500_, _color : [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") = (0, 255, 0)_, _x_offset : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0ns'_, _y_offset : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0V'_, _transparency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.3_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create an eye diagram in the plot. 

Parameters: 
     

**points**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Points of the eye mask in the format `[[x1,y1,],[x2,y2],...]`. 

**x_units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
X points units. The default is `"ns"`. 

**y_units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Y points units. The default is `"mV"`. 

**enable_limits**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to enable the upper and lower limits. The default is `False`. 

**upper_limit**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Upper limit if limits are enabled. The default is `500`. 

**lower_limit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Lower limit if limits are enabled. The default is `-500`. 

**color**[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), `optional` 
    
Mask in (R, G, B) color. The default is `(0, 255, 0)`. Each color value must be an integer in a range from 0 to 255. 

**x_offset**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Mask time offset with units. The default is `"0ns"`. 

**y_offset**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Mask value offset with units. The default is `"0V"`. 

**transparency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Mask transparency. The default is `0.3`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> from ansys.aedt.core.visualization.report.eye import AMIConturEyeDiagram
>>> obj = AMIConturEyeDiagram.__new__(AMIConturEyeDiagram)
>>> obj.eye_mask([[0, 0], [1, 1]])

```
Copy to clipboard