---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# Quantity 

class ansys.aedt.core.generic.numbers_utils.Quantity(_expression_ , _unit =None_) 
    
Stores a number with its unit. 

Parameters: 
     

**expression**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Numerical value of the variable with or without units. 

**unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Units for the value.
Examples

```
>>> from ansys.aedt.core.generic.numbers_utils import Quantity
>>> length = Quantity("10mm")
>>> length.unit_system
'Length'

```
Copy to clipboard
Methods  
| [`Quantity.arccos`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.arccos.html#ansys.aedt.core.generic.numbers_utils.Quantity.arccos "ansys.aedt.core.generic.numbers_utils.Quantity.arccos")()  | Arccosine of the value.  |  
| --- | --- |  
| [`Quantity.arcsin`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.arcsin.html#ansys.aedt.core.generic.numbers_utils.Quantity.arcsin "ansys.aedt.core.generic.numbers_utils.Quantity.arcsin")()  | Arcsine of the value.  |  
| [`Quantity.arctan2`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.arctan2.html#ansys.aedt.core.generic.numbers_utils.Quantity.arctan2 "ansys.aedt.core.generic.numbers_utils.Quantity.arctan2")(other)  | Arctangent of the value and another quantity.  |  
| [`Quantity.as_integer_ratio`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.as_integer_ratio.html#ansys.aedt.core.generic.numbers_utils.Quantity.as_integer_ratio "ansys.aedt.core.generic.numbers_utils.Quantity.as_integer_ratio")(/)  | Return a pair of integers, whose ratio is exactly equal to the original float.  |  
| [`Quantity.conjugate`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.conjugate.html#ansys.aedt.core.generic.numbers_utils.Quantity.conjugate "ansys.aedt.core.generic.numbers_utils.Quantity.conjugate")(/)  | Return self, the complex conjugate of any float.  |  
| [`Quantity.cos`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.cos.html#ansys.aedt.core.generic.numbers_utils.Quantity.cos "ansys.aedt.core.generic.numbers_utils.Quantity.cos")()  | Cosine of the value.  |  
| [`Quantity.from_number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.from_number.html#ansys.aedt.core.generic.numbers_utils.Quantity.from_number "ansys.aedt.core.generic.numbers_utils.Quantity.from_number")(number, /)  | Convert real number to a floating-point number.  |  
| [`Quantity.fromhex`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.fromhex.html#ansys.aedt.core.generic.numbers_utils.Quantity.fromhex "ansys.aedt.core.generic.numbers_utils.Quantity.fromhex")(string, /)  | Create a floating-point number from a hexadecimal string.  |  
| [`Quantity.hex`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.hex.html#ansys.aedt.core.generic.numbers_utils.Quantity.hex "ansys.aedt.core.generic.numbers_utils.Quantity.hex")(/)  | Return a hexadecimal representation of a floating-point number.  |  
| [`Quantity.is_integer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.is_integer.html#ansys.aedt.core.generic.numbers_utils.Quantity.is_integer "ansys.aedt.core.generic.numbers_utils.Quantity.is_integer")(/)  | Return True if the float is an integer.  |  
| [`Quantity.log10`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.log10.html#ansys.aedt.core.generic.numbers_utils.Quantity.log10 "ansys.aedt.core.generic.numbers_utils.Quantity.log10")()  | Logarithm base 10 of the value.  |  
| [`Quantity.sin`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.sin.html#ansys.aedt.core.generic.numbers_utils.Quantity.sin "ansys.aedt.core.generic.numbers_utils.Quantity.sin")()  | Sine of the value.  |  
| [`Quantity.sqrt`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.sqrt.html#ansys.aedt.core.generic.numbers_utils.Quantity.sqrt "ansys.aedt.core.generic.numbers_utils.Quantity.sqrt")()  | Square root of the value.  |  
| [`Quantity.tan`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.tan.html#ansys.aedt.core.generic.numbers_utils.Quantity.tan "ansys.aedt.core.generic.numbers_utils.Quantity.tan")()  | Tangent of the value.  |  
| [`Quantity.to`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.to.html#ansys.aedt.core.generic.numbers_utils.Quantity.to "ansys.aedt.core.generic.numbers_utils.Quantity.to")(unit)  | Convert the actual number to new unit.  |  
Attributes  
| [`Quantity.expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.expression.html#ansys.aedt.core.generic.numbers_utils.Quantity.expression "ansys.aedt.core.generic.numbers_utils.Quantity.expression")  | Retrieve expression.  |  
| --- | --- |  
| [`Quantity.imag`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.imag.html#ansys.aedt.core.generic.numbers_utils.Quantity.imag "ansys.aedt.core.generic.numbers_utils.Quantity.imag")  | the imaginary part of a complex number  |  
| [`Quantity.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.public_dir.html#ansys.aedt.core.generic.numbers_utils.Quantity.public_dir "ansys.aedt.core.generic.numbers_utils.Quantity.public_dir")  | Shortcut for dir(self).  |  
| [`Quantity.real`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.real.html#ansys.aedt.core.generic.numbers_utils.Quantity.real "ansys.aedt.core.generic.numbers_utils.Quantity.real")  | the real part of a complex number  |  
| [`Quantity.unit`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.unit.html#ansys.aedt.core.generic.numbers_utils.Quantity.unit "ansys.aedt.core.generic.numbers_utils.Quantity.unit")  | Value unit.  |  
| [`Quantity.unit_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.unit_system.html#ansys.aedt.core.generic.numbers_utils.Quantity.unit_system "ansys.aedt.core.generic.numbers_utils.Quantity.unit_system")  | Value unit system.  |  
| [`Quantity.value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.value.html#ansys.aedt.core.generic.numbers_utils.Quantity.value "ansys.aedt.core.generic.numbers_utils.Quantity.value")  | Value number.  |  
# Quantity 

class ansys.aedt.core.generic.numbers_utils.Quantity(_expression_ , _unit =None_) 
    
Stores a number with its unit. 

Parameters: 
     

**expression**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Numerical value of the variable with or without units. 

**unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Units for the value.
Examples

```
>>> from ansys.aedt.core.generic.numbers_utils import Quantity
>>> length = Quantity("10mm")
>>> length.unit_system
'Length'

```
Copy to clipboard
Methods  
| [`Quantity.arccos`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.arccos.html#ansys.aedt.core.generic.numbers_utils.Quantity.arccos "ansys.aedt.core.generic.numbers_utils.Quantity.arccos")()  | Arccosine of the value.  |  
| --- | --- |  
| [`Quantity.arcsin`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.arcsin.html#ansys.aedt.core.generic.numbers_utils.Quantity.arcsin "ansys.aedt.core.generic.numbers_utils.Quantity.arcsin")()  | Arcsine of the value.  |  
| [`Quantity.arctan2`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.arctan2.html#ansys.aedt.core.generic.numbers_utils.Quantity.arctan2 "ansys.aedt.core.generic.numbers_utils.Quantity.arctan2")(other)  | Arctangent of the value and another quantity.  |  
| [`Quantity.as_integer_ratio`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.as_integer_ratio.html#ansys.aedt.core.generic.numbers_utils.Quantity.as_integer_ratio "ansys.aedt.core.generic.numbers_utils.Quantity.as_integer_ratio")(/)  | Return a pair of integers, whose ratio is exactly equal to the original float.  |  
| [`Quantity.conjugate`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.conjugate.html#ansys.aedt.core.generic.numbers_utils.Quantity.conjugate "ansys.aedt.core.generic.numbers_utils.Quantity.conjugate")(/)  | Return self, the complex conjugate of any float.  |  
| [`Quantity.cos`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.cos.html#ansys.aedt.core.generic.numbers_utils.Quantity.cos "ansys.aedt.core.generic.numbers_utils.Quantity.cos")()  | Cosine of the value.  |  
| [`Quantity.from_number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.from_number.html#ansys.aedt.core.generic.numbers_utils.Quantity.from_number "ansys.aedt.core.generic.numbers_utils.Quantity.from_number")(number, /)  | Convert real number to a floating-point number.  |  
| [`Quantity.fromhex`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.fromhex.html#ansys.aedt.core.generic.numbers_utils.Quantity.fromhex "ansys.aedt.core.generic.numbers_utils.Quantity.fromhex")(string, /)  | Create a floating-point number from a hexadecimal string.  |  
| [`Quantity.hex`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.hex.html#ansys.aedt.core.generic.numbers_utils.Quantity.hex "ansys.aedt.core.generic.numbers_utils.Quantity.hex")(/)  | Return a hexadecimal representation of a floating-point number.  |  
| [`Quantity.is_integer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.is_integer.html#ansys.aedt.core.generic.numbers_utils.Quantity.is_integer "ansys.aedt.core.generic.numbers_utils.Quantity.is_integer")(/)  | Return True if the float is an integer.  |  
| [`Quantity.log10`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.log10.html#ansys.aedt.core.generic.numbers_utils.Quantity.log10 "ansys.aedt.core.generic.numbers_utils.Quantity.log10")()  | Logarithm base 10 of the value.  |  
| [`Quantity.sin`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.sin.html#ansys.aedt.core.generic.numbers_utils.Quantity.sin "ansys.aedt.core.generic.numbers_utils.Quantity.sin")()  | Sine of the value.  |  
| [`Quantity.sqrt`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.sqrt.html#ansys.aedt.core.generic.numbers_utils.Quantity.sqrt "ansys.aedt.core.generic.numbers_utils.Quantity.sqrt")()  | Square root of the value.  |  
| [`Quantity.tan`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.tan.html#ansys.aedt.core.generic.numbers_utils.Quantity.tan "ansys.aedt.core.generic.numbers_utils.Quantity.tan")()  | Tangent of the value.  |  
| [`Quantity.to`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.to.html#ansys.aedt.core.generic.numbers_utils.Quantity.to "ansys.aedt.core.generic.numbers_utils.Quantity.to")(unit)  | Convert the actual number to new unit.  |  
Attributes  
| [`Quantity.expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.expression.html#ansys.aedt.core.generic.numbers_utils.Quantity.expression "ansys.aedt.core.generic.numbers_utils.Quantity.expression")  | Retrieve expression.  |  
| --- | --- |  
| [`Quantity.imag`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.imag.html#ansys.aedt.core.generic.numbers_utils.Quantity.imag "ansys.aedt.core.generic.numbers_utils.Quantity.imag")  | the imaginary part of a complex number  |  
| [`Quantity.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.public_dir.html#ansys.aedt.core.generic.numbers_utils.Quantity.public_dir "ansys.aedt.core.generic.numbers_utils.Quantity.public_dir")  | Shortcut for dir(self).  |  
| [`Quantity.real`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.real.html#ansys.aedt.core.generic.numbers_utils.Quantity.real "ansys.aedt.core.generic.numbers_utils.Quantity.real")  | the real part of a complex number  |  
| [`Quantity.unit`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.unit.html#ansys.aedt.core.generic.numbers_utils.Quantity.unit "ansys.aedt.core.generic.numbers_utils.Quantity.unit")  | Value unit.  |  
| [`Quantity.unit_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.unit_system.html#ansys.aedt.core.generic.numbers_utils.Quantity.unit_system "ansys.aedt.core.generic.numbers_utils.Quantity.unit_system")  | Value unit system.  |  
| [`Quantity.value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.value.html#ansys.aedt.core.generic.numbers_utils.Quantity.value "ansys.aedt.core.generic.numbers_utils.Quantity.value")  | Value number.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.rst.txt)

# Quantity 

class ansys.aedt.core.generic.numbers_utils.Quantity(_expression_ , _unit =None_) 
    
Stores a number with its unit. 

Parameters: 
     

**expression**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Numerical value of the variable with or without units. 

**unit**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Units for the value.
Examples

```
>>> from ansys.aedt.core.generic.numbers_utils import Quantity
>>> length = Quantity("10mm")
>>> length.unit_system
'Length'

```
Copy to clipboard
Methods  
| [`Quantity.arccos`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.arccos.html#ansys.aedt.core.generic.numbers_utils.Quantity.arccos "ansys.aedt.core.generic.numbers_utils.Quantity.arccos")()  | Arccosine of the value.  |  
| --- | --- |  
| [`Quantity.arcsin`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.arcsin.html#ansys.aedt.core.generic.numbers_utils.Quantity.arcsin "ansys.aedt.core.generic.numbers_utils.Quantity.arcsin")()  | Arcsine of the value.  |  
| [`Quantity.arctan2`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.arctan2.html#ansys.aedt.core.generic.numbers_utils.Quantity.arctan2 "ansys.aedt.core.generic.numbers_utils.Quantity.arctan2")(other)  | Arctangent of the value and another quantity.  |  
| [`Quantity.as_integer_ratio`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.as_integer_ratio.html#ansys.aedt.core.generic.numbers_utils.Quantity.as_integer_ratio "ansys.aedt.core.generic.numbers_utils.Quantity.as_integer_ratio")(/)  | Return a pair of integers, whose ratio is exactly equal to the original float.  |  
| [`Quantity.conjugate`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.conjugate.html#ansys.aedt.core.generic.numbers_utils.Quantity.conjugate "ansys.aedt.core.generic.numbers_utils.Quantity.conjugate")(/)  | Return self, the complex conjugate of any float.  |  
| [`Quantity.cos`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.cos.html#ansys.aedt.core.generic.numbers_utils.Quantity.cos "ansys.aedt.core.generic.numbers_utils.Quantity.cos")()  | Cosine of the value.  |  
| [`Quantity.from_number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.from_number.html#ansys.aedt.core.generic.numbers_utils.Quantity.from_number "ansys.aedt.core.generic.numbers_utils.Quantity.from_number")(number, /)  | Convert real number to a floating-point number.  |  
| [`Quantity.fromhex`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.fromhex.html#ansys.aedt.core.generic.numbers_utils.Quantity.fromhex "ansys.aedt.core.generic.numbers_utils.Quantity.fromhex")(string, /)  | Create a floating-point number from a hexadecimal string.  |  
| [`Quantity.hex`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.hex.html#ansys.aedt.core.generic.numbers_utils.Quantity.hex "ansys.aedt.core.generic.numbers_utils.Quantity.hex")(/)  | Return a hexadecimal representation of a floating-point number.  |  
| [`Quantity.is_integer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.is_integer.html#ansys.aedt.core.generic.numbers_utils.Quantity.is_integer "ansys.aedt.core.generic.numbers_utils.Quantity.is_integer")(/)  | Return True if the float is an integer.  |  
| [`Quantity.log10`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.log10.html#ansys.aedt.core.generic.numbers_utils.Quantity.log10 "ansys.aedt.core.generic.numbers_utils.Quantity.log10")()  | Logarithm base 10 of the value.  |  
| [`Quantity.sin`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.sin.html#ansys.aedt.core.generic.numbers_utils.Quantity.sin "ansys.aedt.core.generic.numbers_utils.Quantity.sin")()  | Sine of the value.  |  
| [`Quantity.sqrt`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.sqrt.html#ansys.aedt.core.generic.numbers_utils.Quantity.sqrt "ansys.aedt.core.generic.numbers_utils.Quantity.sqrt")()  | Square root of the value.  |  
| [`Quantity.tan`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.tan.html#ansys.aedt.core.generic.numbers_utils.Quantity.tan "ansys.aedt.core.generic.numbers_utils.Quantity.tan")()  | Tangent of the value.  |  
| [`Quantity.to`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.to.html#ansys.aedt.core.generic.numbers_utils.Quantity.to "ansys.aedt.core.generic.numbers_utils.Quantity.to")(unit)  | Convert the actual number to new unit.  |  
Attributes  
| [`Quantity.expression`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.expression.html#ansys.aedt.core.generic.numbers_utils.Quantity.expression "ansys.aedt.core.generic.numbers_utils.Quantity.expression")  | Retrieve expression.  |  
| --- | --- |  
| [`Quantity.imag`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.imag.html#ansys.aedt.core.generic.numbers_utils.Quantity.imag "ansys.aedt.core.generic.numbers_utils.Quantity.imag")  | the imaginary part of a complex number  |  
| [`Quantity.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.public_dir.html#ansys.aedt.core.generic.numbers_utils.Quantity.public_dir "ansys.aedt.core.generic.numbers_utils.Quantity.public_dir")  | Shortcut for dir(self).  |  
| [`Quantity.real`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.real.html#ansys.aedt.core.generic.numbers_utils.Quantity.real "ansys.aedt.core.generic.numbers_utils.Quantity.real")  | the real part of a complex number  |  
| [`Quantity.unit`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.unit.html#ansys.aedt.core.generic.numbers_utils.Quantity.unit "ansys.aedt.core.generic.numbers_utils.Quantity.unit")  | Value unit.  |  
| [`Quantity.unit_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.unit_system.html#ansys.aedt.core.generic.numbers_utils.Quantity.unit_system "ansys.aedt.core.generic.numbers_utils.Quantity.unit_system")  | Value unit system.  |  
| [`Quantity.value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.numbers_utils.Quantity.value.html#ansys.aedt.core.generic.numbers_utils.Quantity.value "ansys.aedt.core.generic.numbers_utils.Quantity.value")  | Value number.  |