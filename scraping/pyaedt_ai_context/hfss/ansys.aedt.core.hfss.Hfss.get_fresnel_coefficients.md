---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.get_fresnel_coefficients.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# get_fresnel_coefficients 

Hfss.get_fresnel_coefficients(_setup_sweep : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _theta_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _phi_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") = None_, _is_isotropic : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _rttbl_version : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '2.0'_) → [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Generate a Fresnel reflection or reflection/transmission coefficient table from simulation data.
This method calculates the Fresnel reflection (and optionally transmission) coefficients for TE and TM modes using S-parameters between Floquet ports in a HFSS simulation. The results are written to an `.rttbl` file in a format compatible with SBR+ native tables. 

Parameters: 
     

**setup_sweep**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup and sweep. 

**theta_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variation parameter representing the theta angle. 

**phi_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variation parameter representing the phi angle. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)"), `optional` 
    
Path to save the output `.rttbl` file. If not provided, a file will be generated automatically in the toolkit directory. 

**is_isotropic**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
     

Whether to get isotropic or anisotropic coefficients.
    
If `None`, the method will attempt to determine isotropy based on the parametric sweep. 

**rttbl_version**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Version of the Fresnel table to create. The options are `"1.0"` and `"2.0"`. 

Returns: 
     

[`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")
    
The path to the generated .rttbl file containing Fresnel coefficients.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.get_fresnel_coefficients(setup_sweep="Setup1 : Sweep1", theta_name="theta", phi_name="phi")

```
Copy to clipboard
# get_fresnel_coefficients 

Hfss.get_fresnel_coefficients(_setup_sweep : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _theta_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _phi_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") = None_, _is_isotropic : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _rttbl_version : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '2.0'_) → [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Generate a Fresnel reflection or reflection/transmission coefficient table from simulation data.
This method calculates the Fresnel reflection (and optionally transmission) coefficients for TE and TM modes using S-parameters between Floquet ports in a HFSS simulation. The results are written to an `.rttbl` file in a format compatible with SBR+ native tables. 

Parameters: 
     

**setup_sweep**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup and sweep. 

**theta_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variation parameter representing the theta angle. 

**phi_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variation parameter representing the phi angle. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)"), `optional` 
    
Path to save the output `.rttbl` file. If not provided, a file will be generated automatically in the toolkit directory. 

**is_isotropic**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
     

Whether to get isotropic or anisotropic coefficients.
    
If `None`, the method will attempt to determine isotropy based on the parametric sweep. 

**rttbl_version**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Version of the Fresnel table to create. The options are `"1.0"` and `"2.0"`. 

Returns: 
     

[`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")
    
The path to the generated .rttbl file containing Fresnel coefficients.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.get_fresnel_coefficients(setup_sweep="Setup1 : Sweep1", theta_name="theta", phi_name="phi")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.get_fresnel_coefficients.rst.txt)

# get_fresnel_coefficients 

Hfss.get_fresnel_coefficients(_setup_sweep : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _theta_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _phi_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _output_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") = None_, _is_isotropic : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _rttbl_version : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '2.0'_) → [Path](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Generate a Fresnel reflection or reflection/transmission coefficient table from simulation data.
This method calculates the Fresnel reflection (and optionally transmission) coefficients for TE and TM modes using S-parameters between Floquet ports in a HFSS simulation. The results are written to an `.rttbl` file in a format compatible with SBR+ native tables. 

Parameters: 
     

**setup_sweep**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the setup and sweep. 

**theta_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variation parameter representing the theta angle. 

**phi_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variation parameter representing the phi angle. 

**output_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)"), `optional` 
    
Path to save the output `.rttbl` file. If not provided, a file will be generated automatically in the toolkit directory. 

**is_isotropic**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
     

Whether to get isotropic or anisotropic coefficients.
    
If `None`, the method will attempt to determine isotropy based on the parametric sweep. 

**rttbl_version**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Version of the Fresnel table to create. The options are `"1.0"` and `"2.0"`. 

Returns: 
     

[`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)")
    
The path to the generated .rttbl file containing Fresnel coefficients.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.get_fresnel_coefficients(setup_sweep="Setup1 : Sweep1", theta_name="theta", phi_name="phi")

```
Copy to clipboard