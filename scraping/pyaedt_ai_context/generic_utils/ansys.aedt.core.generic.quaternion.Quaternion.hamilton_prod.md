---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.hamilton_prod.html"
category: "generic_utils"
domain: "PyAEDT / HFSS"
---

# hamilton_prod 

static Quaternion.hamilton_prod(_q1 : 'Quaternion' | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")_, _q2 : 'Quaternion' | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")_) → [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion") 
     

Evaluate the Hamilton product of two quaternions, `q1` and `q2`, defined as:
    
q1 = p0 + p’ = p0 + ip1 + jp2 + kp3 q2 = q0 + q’ = q0 + iq1 + jq2 + kq3 m = q1*q2 = p0q0 - p’ • q’ + p0q’ + q0p’ + p’ x q’ 

Parameters: 
     

**q1**[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion"), `List`, [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
The value to multiply with this quaternion. It can be another Quaternion or a sequence that can be interpreted as one. 

**q2**[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion"), `List`, [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
The value to multiply with this quaternion. It can be another Quaternion or a sequence that can be interpreted as one. 

**q1 and q2 must be quaternions or compatible values. Multiplicaiton between quaternions and scalar values is**
     

**handled by the method ``mul``**
     

Returns: 
     

[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")
    
The quaternion result of the multiplication between q1 and q2
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q1 = Quaternion(1, 2, 3, 4)
>>> q2 = Quaternion(5, 6, 7, 8)
>>> Quaternion.hamilton_prod(q1, q2)
Quaternion(-60, 12, 30, 24)

```
Copy to clipboard
# hamilton_prod 

static Quaternion.hamilton_prod(_q1 : 'Quaternion' | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")_, _q2 : 'Quaternion' | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")_) → [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion") 
     

Evaluate the Hamilton product of two quaternions, `q1` and `q2`, defined as:
    
q1 = p0 + p’ = p0 + ip1 + jp2 + kp3 q2 = q0 + q’ = q0 + iq1 + jq2 + kq3 m = q1*q2 = p0q0 - p’ • q’ + p0q’ + q0p’ + p’ x q’ 

Parameters: 
     

**q1**[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion"), `List`, [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
The value to multiply with this quaternion. It can be another Quaternion or a sequence that can be interpreted as one. 

**q2**[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion"), `List`, [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
The value to multiply with this quaternion. It can be another Quaternion or a sequence that can be interpreted as one. 

**q1 and q2 must be quaternions or compatible values. Multiplicaiton between quaternions and scalar values is**
     

**handled by the method ``mul``**
     

Returns: 
     

[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")
    
The quaternion result of the multiplication between q1 and q2
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q1 = Quaternion(1, 2, 3, 4)
>>> q2 = Quaternion(5, 6, 7, 8)
>>> Quaternion.hamilton_prod(q1, q2)
Quaternion(-60, 12, 30, 24)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.hamilton_prod.rst.txt)

# hamilton_prod 

static Quaternion.hamilton_prod(_q1 : 'Quaternion' | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")_, _q2 : 'Quaternion' | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")_) → [Quaternion](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion") 
     

Evaluate the Hamilton product of two quaternions, `q1` and `q2`, defined as:
    
q1 = p0 + p’ = p0 + ip1 + jp2 + kp3 q2 = q0 + q’ = q0 + iq1 + jq2 + kq3 m = q1*q2 = p0q0 - p’ • q’ + p0q’ + q0p’ + p’ x q’ 

Parameters: 
     

**q1**[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion"), `List`, [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
The value to multiply with this quaternion. It can be another Quaternion or a sequence that can be interpreted as one. 

**q2**[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion"), `List`, [`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)") 
    
The value to multiply with this quaternion. It can be another Quaternion or a sequence that can be interpreted as one. 

**q1 and q2 must be quaternions or compatible values. Multiplicaiton between quaternions and scalar values is**
     

**handled by the method ``mul``**
     

Returns: 
     

[`Quaternion`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.generic.quaternion.Quaternion.html#ansys.aedt.core.generic.quaternion.Quaternion "ansys.aedt.core.generic.quaternion.Quaternion")
    
The quaternion result of the multiplication between q1 and q2
Examples

```
>>> from ansys.aedt.core.generic.quaternion import Quaternion
>>> q1 = Quaternion(1, 2, 3, 4)
>>> q2 = Quaternion(5, 6, 7, 8)
>>> Quaternion.hamilton_prod(q1, q2)
Quaternion(-60, 12, 30, 24)

```
Copy to clipboard