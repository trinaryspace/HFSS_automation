---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.add.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# add 

Quaternion.add(_other : 'Quaternion' | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_) → [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion") 
    
Adds another quaternion or compatible value to this quaternion. 

Parameters: 
     

**other**[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion"), `List`, [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `or` [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
The value to be added. It can be another Quaternion or a sequence that can be interpreted as one. It can also be a scalar value (float or int). 

Returns: 
     

[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")
    
A new quaternion representing the sum of this quaternion and the provided value.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q1 = Quaternion(1, 2, 3, 4)
>>> q2 = Quaternion(5, 6, 7, 8)
>>> q1.add(q2)
Quaternion(6, 8, 10, 12)
>>> q1 + 7
Quaternion(8, 2, 3, 4)

```
Copy to clipboard
# add 

Quaternion.add(_other : 'Quaternion' | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_) → [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion") 
    
Adds another quaternion or compatible value to this quaternion. 

Parameters: 
     

**other**[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion"), `List`, [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `or` [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
The value to be added. It can be another Quaternion or a sequence that can be interpreted as one. It can also be a scalar value (float or int). 

Returns: 
     

[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")
    
A new quaternion representing the sum of this quaternion and the provided value.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q1 = Quaternion(1, 2, 3, 4)
>>> q2 = Quaternion(5, 6, 7, 8)
>>> q1.add(q2)
Quaternion(6, 8, 10, 12)
>>> q1 + 7
Quaternion(8, 2, 3, 4)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.add.rst.txt)

# add 

Quaternion.add(_other : 'Quaternion' | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_) → [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion") 
    
Adds another quaternion or compatible value to this quaternion. 

Parameters: 
     

**other**[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion"), `List`, [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `or` [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
The value to be added. It can be another Quaternion or a sequence that can be interpreted as one. It can also be a scalar value (float or int). 

Returns: 
     

[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")
    
A new quaternion representing the sum of this quaternion and the provided value.
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q1 = Quaternion(1, 2, 3, 4)
>>> q2 = Quaternion(5, 6, 7, 8)
>>> q1.add(q2)
Quaternion(6, 8, 10, 12)
>>> q1 + 7
Quaternion(8, 2, 3, 4)

```
Copy to clipboard