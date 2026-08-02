---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.value_with_units.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# value_with_units 

Hfss3dLayout.value_with_units(_value : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _units_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Length'_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Combine a number and a string containing the modeler length unit in a single string e.g. “1.2mm”.
If the units are not specified, the model units are used. If value is a string (like containing an expression), it is returned as is. 

Parameters: 
     

**value**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Value of the number or string containing an expression. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units to combine with value. Valid values are defined in the native API documentation. Some common examples are: “in”: inches “cm”: centimeter “um”: micron “mm”: millimeter “meter”: meters “mil”: 0.001 inches (mils) “km”: kilometer “ft”: feet 

**units_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Unit system. Default is “Length”. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
String that combines the value and the units (e.g. “1.2mm”).
References

```
>>> oEditor.GetDefaultUnit
>>> oEditor.GetModelUnits
>>> oEditor.GetActiveUnits

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.value_with_units(1.2, "mm")
'1.2mm'

```
Copy to clipboard
# value_with_units 

Hfss3dLayout.value_with_units(_value : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _units_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Length'_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Combine a number and a string containing the modeler length unit in a single string e.g. “1.2mm”.
If the units are not specified, the model units are used. If value is a string (like containing an expression), it is returned as is. 

Parameters: 
     

**value**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Value of the number or string containing an expression. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units to combine with value. Valid values are defined in the native API documentation. Some common examples are: “in”: inches “cm”: centimeter “um”: micron “mm”: millimeter “meter”: meters “mil”: 0.001 inches (mils) “km”: kilometer “ft”: feet 

**units_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Unit system. Default is “Length”. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
String that combines the value and the units (e.g. “1.2mm”).
References

```
>>> oEditor.GetDefaultUnit
>>> oEditor.GetModelUnits
>>> oEditor.GetActiveUnits

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.value_with_units(1.2, "mm")
'1.2mm'

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.value_with_units.rst.txt)

# value_with_units 

Hfss3dLayout.value_with_units(_value : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _units_system : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Length'_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Combine a number and a string containing the modeler length unit in a single string e.g. “1.2mm”.
If the units are not specified, the model units are used. If value is a string (like containing an expression), it is returned as is. 

Parameters: 
     

**value**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Value of the number or string containing an expression. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Units to combine with value. Valid values are defined in the native API documentation. Some common examples are: “in”: inches “cm”: centimeter “um”: micron “mm”: millimeter “meter”: meters “mil”: 0.001 inches (mils) “km”: kilometer “ft”: feet 

**units_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Unit system. Default is “Length”. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
String that combines the value and the units (e.g. “1.2mm”).
References

```
>>> oEditor.GetDefaultUnit
>>> oEditor.GetModelUnits
>>> oEditor.GetActiveUnits

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.value_with_units(1.2, "mm")
'1.2mm'

```
Copy to clipboard