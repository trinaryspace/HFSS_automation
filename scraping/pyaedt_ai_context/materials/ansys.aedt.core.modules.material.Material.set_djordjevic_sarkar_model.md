---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_djordjevic_sarkar_model.html"
category: "materials"
domain: "PyAEDT / HFSS"
---

# set_djordjevic_sarkar_model 

Material.set_djordjevic_sarkar_model(_dk : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 4_, _df : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.02_, _frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1000000000.0_, _sigma_dc : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-12_, _freq_hi : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 159154940000.0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set Djordjevic-Sarkar model. 

Parameters: 
     

**dk**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Dielectric constant at input frequency. 

**df**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Loss tangent at input frequency. 

**frequency**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), optional. 
    
Input frequency in Hz. 

**sigma_dc**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Conductivity at DC. The default is `1e-12`. 

**freq_hi**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
High-frequency corner in Hz. The default is `159.15494e9`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modules.material import Material
>>> obj = Material()
>>> obj.set_djordjevic_sarkar_model(dk=1, df=1.0)

```
Copy to clipboard
# set_djordjevic_sarkar_model 

Material.set_djordjevic_sarkar_model(_dk : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 4_, _df : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.02_, _frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1000000000.0_, _sigma_dc : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-12_, _freq_hi : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 159154940000.0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set Djordjevic-Sarkar model. 

Parameters: 
     

**dk**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Dielectric constant at input frequency. 

**df**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Loss tangent at input frequency. 

**frequency**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), optional. 
    
Input frequency in Hz. 

**sigma_dc**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Conductivity at DC. The default is `1e-12`. 

**freq_hi**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
High-frequency corner in Hz. The default is `159.15494e9`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modules.material import Material
>>> obj = Material()
>>> obj.set_djordjevic_sarkar_model(dk=1, df=1.0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.material.Material.set_djordjevic_sarkar_model.rst.txt)

# set_djordjevic_sarkar_model 

Material.set_djordjevic_sarkar_model(_dk : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 4_, _df : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.02_, _frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1000000000.0_, _sigma_dc : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 1e-12_, _freq_hi : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 159154940000.0_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set Djordjevic-Sarkar model. 

Parameters: 
     

**dk**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Dielectric constant at input frequency. 

**df**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Loss tangent at input frequency. 

**frequency**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), optional. 
    
Input frequency in Hz. 

**sigma_dc**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Conductivity at DC. The default is `1e-12`. 

**freq_hi**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
High-frequency corner in Hz. The default is `159.15494e9`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful, `False` otherwise.
Examples

```
>>> from ansys.aedt.core.modules.material import Material
>>> obj = Material()
>>> obj.set_djordjevic_sarkar_model(dk=1, df=1.0)

```
Copy to clipboard