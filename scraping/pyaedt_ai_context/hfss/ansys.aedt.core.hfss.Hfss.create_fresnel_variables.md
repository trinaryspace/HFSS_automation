---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_fresnel_variables.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# create_fresnel_variables 

Hfss.create_fresnel_variables(_setup_sweep : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _rttbl_version : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '2.0'_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Create (or overwrite) the output variables in HFSS needed to compute Fresnel reflection/transmission coefficients between Floquet ports. 

Parameters: 
     

**setup_sweep**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup and sweep. 

**rttbl_version**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Version of the Fresnel table to create. The options are `"1.0"` and `"2.0"`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.create_fresnel_variables("Setup2 : Sweep")

```
Copy to clipboard
# create_fresnel_variables 

Hfss.create_fresnel_variables(_setup_sweep : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _rttbl_version : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '2.0'_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Create (or overwrite) the output variables in HFSS needed to compute Fresnel reflection/transmission coefficients between Floquet ports. 

Parameters: 
     

**setup_sweep**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup and sweep. 

**rttbl_version**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Version of the Fresnel table to create. The options are `"1.0"` and `"2.0"`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.create_fresnel_variables("Setup2 : Sweep")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_fresnel_variables.rst.txt)

# create_fresnel_variables 

Hfss.create_fresnel_variables(_setup_sweep : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _rttbl_version : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '2.0'_) → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Create (or overwrite) the output variables in HFSS needed to compute Fresnel reflection/transmission coefficients between Floquet ports. 

Parameters: 
     

**setup_sweep**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup and sweep. 

**rttbl_version**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Version of the Fresnel table to create. The options are `"1.0"` and `"2.0"`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.create_fresnel_variables("Setup2 : Sweep")

```
Copy to clipboard