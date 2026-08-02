---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# SinusoidalDictionary 

class ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary(_vertical_offset_ , _vertical_scaling_ , _period_ , _period_offset_) 
    
Manages sinusoidal condition assignments, which are children of the `BoundaryDictionary` class. 

This class applies a condition `y` dependent on the time `t`:
    
`y=a+b*sin(2*pi(t-t0)/T)` 

Parameters: 
     

**vertical_offset**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Vertical offset summed to the sinusoidal law, which corresponds to the coefficient `a` in the formula. 

**vertical_scaling**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Coefficient that multiplies the sinusoidal term, which corresponds to the coefficient `b` in the formula. 

**period**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Period of the sinusoid, which corresponds to the coefficient `T` in the formula. 

**period_offset**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Offset of the sinusoid, which corresponds to the coefficient `t0` in the formula.
Examples

```
>>> from ansys.aedt.core.modules.boundary.icepak_boundary import SinusoidalDictionary
>>> obj = SinusoidalDictionary()

```
Copy to clipboard
Attributes  
| [`SinusoidalDictionary.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary.props.html#ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary.props "ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary.props")  | Dictionary that defines all the boundary condition properties.  |  
| --- | --- |  
| [`SinusoidalDictionary.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary.public_dir.html#ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary.public_dir "ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary.public_dir")  | Shortcut for dir(self).  |  
# SinusoidalDictionary 

class ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary(_vertical_offset_ , _vertical_scaling_ , _period_ , _period_offset_) 
    
Manages sinusoidal condition assignments, which are children of the `BoundaryDictionary` class. 

This class applies a condition `y` dependent on the time `t`:
    
`y=a+b*sin(2*pi(t-t0)/T)` 

Parameters: 
     

**vertical_offset**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Vertical offset summed to the sinusoidal law, which corresponds to the coefficient `a` in the formula. 

**vertical_scaling**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Coefficient that multiplies the sinusoidal term, which corresponds to the coefficient `b` in the formula. 

**period**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Period of the sinusoid, which corresponds to the coefficient `T` in the formula. 

**period_offset**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Offset of the sinusoid, which corresponds to the coefficient `t0` in the formula.
Examples

```
>>> from ansys.aedt.core.modules.boundary.icepak_boundary import SinusoidalDictionary
>>> obj = SinusoidalDictionary()

```
Copy to clipboard
Attributes  
| [`SinusoidalDictionary.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary.props.html#ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary.props "ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary.props")  | Dictionary that defines all the boundary condition properties.  |  
| --- | --- |  
| [`SinusoidalDictionary.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary.public_dir.html#ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary.public_dir "ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary.public_dir")  | Shortcut for dir(self).  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary.rst.txt)

# SinusoidalDictionary 

class ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary(_vertical_offset_ , _vertical_scaling_ , _period_ , _period_offset_) 
    
Manages sinusoidal condition assignments, which are children of the `BoundaryDictionary` class. 

This class applies a condition `y` dependent on the time `t`:
    
`y=a+b*sin(2*pi(t-t0)/T)` 

Parameters: 
     

**vertical_offset**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Vertical offset summed to the sinusoidal law, which corresponds to the coefficient `a` in the formula. 

**vertical_scaling**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Coefficient that multiplies the sinusoidal term, which corresponds to the coefficient `b` in the formula. 

**period**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Period of the sinusoid, which corresponds to the coefficient `T` in the formula. 

**period_offset**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Offset of the sinusoid, which corresponds to the coefficient `t0` in the formula.
Examples

```
>>> from ansys.aedt.core.modules.boundary.icepak_boundary import SinusoidalDictionary
>>> obj = SinusoidalDictionary()

```
Copy to clipboard
Attributes  
| [`SinusoidalDictionary.props`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary.props.html#ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary.props "ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary.props")  | Dictionary that defines all the boundary condition properties.  |  
| --- | --- |  
| [`SinusoidalDictionary.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary.public_dir.html#ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary.public_dir "ansys.aedt.core.modules.boundary.icepak_boundary.SinusoidalDictionary.public_dir")  | Shortcut for dir(self).  |