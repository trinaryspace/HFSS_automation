---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.div.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# div 

Quaternion.div(_other : 'Quaternion' | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_) → [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion") 
    
Performs quaternion division with another quaternion or compatible value. 

Parameters: 
     

**other**[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion"), `List`, [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `or` [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
The value to divide with this quaternion. It can be another Quaternion or a sequence that can be interpreted as one. It can also be a scalar value (float or int). 

Returns: 
     

[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")
    
A new quaternion representing the division of this quaternion and the given value.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q1 = Quaternion(1, 2, 3, 4)
>>> q2 = Quaternion(1, -1, 1, 2)
>>> q1.div(q2)
Quaternion(10/7, 1/7, 10/7, -3/7)
>>> q1.div(2)
Quaternion(0.5, 1, 1.5, 2)

```
Copy to clipboard
# div 

Quaternion.div(_other : 'Quaternion' | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_) → [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion") 
    
Performs quaternion division with another quaternion or compatible value. 

Parameters: 
     

**other**[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion"), `List`, [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `or` [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
The value to divide with this quaternion. It can be another Quaternion or a sequence that can be interpreted as one. It can also be a scalar value (float or int). 

Returns: 
     

[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")
    
A new quaternion representing the division of this quaternion and the given value.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q1 = Quaternion(1, 2, 3, 4)
>>> q2 = Quaternion(1, -1, 1, 2)
>>> q1.div(q2)
Quaternion(10/7, 1/7, 10/7, -3/7)
>>> q1.div(2)
Quaternion(0.5, 1, 1.5, 2)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.div.rst.txt)

# div 

Quaternion.div(_other : 'Quaternion' | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_) → [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion") 
    
Performs quaternion division with another quaternion or compatible value. 

Parameters: 
     

**other**[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion"), `List`, [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `or` [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
The value to divide with this quaternion. It can be another Quaternion or a sequence that can be interpreted as one. It can also be a scalar value (float or int). 

Returns: 
     

[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")
    
A new quaternion representing the division of this quaternion and the given value.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q1 = Quaternion(1, 2, 3, 4)
>>> q2 = Quaternion(1, -1, 1, 2)
>>> q1.div(q2)
Quaternion(10/7, 1/7, 10/7, -3/7)
>>> q1.div(2)
Quaternion(0.5, 1, 1.5, 2)

```
Copy to clipboard