---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.mul.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# mul 

Quaternion.mul(_other : 'Quaternion' | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_) → [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion") 
    
Performs quaternion multiplication with another quaternion or compatible value. 

Parameters: 
     

**other**[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion"), `List`, [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `or` [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
The value to multiply with this quaternion. It can be another Quaternion or a sequence that can be interpreted as one. It can also be a scalar value (float or int). 

Returns: 
     

[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")
    
A new quaternion representing the product of this quaternion and the given value.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q1 = Quaternion(1, 2, 3, 4)
>>> q2 = Quaternion(5, 6, 7, 8)
>>> q1.mul(q2)
Quaternion(-60, 12, 30, 24)
>>> q1.mul(2)
Quaternion(2, 4, 6, 8)

```
Copy to clipboard
# mul 

Quaternion.mul(_other : 'Quaternion' | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_) → [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion") 
    
Performs quaternion multiplication with another quaternion or compatible value. 

Parameters: 
     

**other**[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion"), `List`, [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `or` [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
The value to multiply with this quaternion. It can be another Quaternion or a sequence that can be interpreted as one. It can also be a scalar value (float or int). 

Returns: 
     

[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")
    
A new quaternion representing the product of this quaternion and the given value.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q1 = Quaternion(1, 2, 3, 4)
>>> q2 = Quaternion(5, 6, 7, 8)
>>> q1.mul(q2)
Quaternion(-60, 12, 30, 24)
>>> q1.mul(2)
Quaternion(2, 4, 6, 8)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.mul.rst.txt)

# mul 

Quaternion.mul(_other : 'Quaternion' | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_) → [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion") 
    
Performs quaternion multiplication with another quaternion or compatible value. 

Parameters: 
     

**other**[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion"), `List`, [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `or` [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
The value to multiply with this quaternion. It can be another Quaternion or a sequence that can be interpreted as one. It can also be a scalar value (float or int). 

Returns: 
     

[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")
    
A new quaternion representing the product of this quaternion and the given value.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q1 = Quaternion(1, 2, 3, 4)
>>> q2 = Quaternion(5, 6, 7, 8)
>>> q1.mul(q2)
Quaternion(-60, 12, 30, 24)
>>> q1.mul(2)
Quaternion(2, 4, 6, 8)

```
Copy to clipboard