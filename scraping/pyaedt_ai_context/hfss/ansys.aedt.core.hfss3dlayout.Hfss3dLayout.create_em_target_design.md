---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.create_em_target_design.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# create_em_target_design 

Hfss3dLayout.create_em_target_design(_design : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _design_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create an EM Target design. 

Parameters: 
     

**design**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the target design. Possible choices are `"Icepak"` or `"Mechanical"`. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the EM setup to link to the target design. The default is `None`, in which case the `LastAdaptive` setup is used. 

**design_setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
For Icepak designs, specify `"Forced"` for forced convention or `"Natural"` for natural convention. The default is `None`, in which case the `"Forced"` option is used. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.CreateEMLossTarget

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Maxwell3d, Mechanical
>>> from ansys.aedt.core.generic.aedt_constants import IcepakFeaConstants
>>> m3d = Maxwell3d(version="2026.1")
>>> # From 2026.1, Mechanical has been renamed to IcepakFEA.
>>> # Pass the target design through the IcepakFeaConstants metaclass.
>>> # This automatically selects the correct AEDT API design name.
>>> m3d.create_em_target_design(design=IcepakFeaConstants.NAME)
>>> mechanical = Mechanical(version="2026.1")
>>> mechanical.release_desktop(False, False)

```
Copy to clipboard
# create_em_target_design 

Hfss3dLayout.create_em_target_design(_design : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _design_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create an EM Target design. 

Parameters: 
     

**design**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the target design. Possible choices are `"Icepak"` or `"Mechanical"`. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the EM setup to link to the target design. The default is `None`, in which case the `LastAdaptive` setup is used. 

**design_setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
For Icepak designs, specify `"Forced"` for forced convention or `"Natural"` for natural convention. The default is `None`, in which case the `"Forced"` option is used. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.CreateEMLossTarget

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Maxwell3d, Mechanical
>>> from ansys.aedt.core.generic.aedt_constants import IcepakFeaConstants
>>> m3d = Maxwell3d(version="2026.1")
>>> # From 2026.1, Mechanical has been renamed to IcepakFEA.
>>> # Pass the target design through the IcepakFeaConstants metaclass.
>>> # This automatically selects the correct AEDT API design name.
>>> m3d.create_em_target_design(design=IcepakFeaConstants.NAME)
>>> mechanical = Mechanical(version="2026.1")
>>> mechanical.release_desktop(False, False)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.create_em_target_design.rst.txt)

# create_em_target_design 

Hfss3dLayout.create_em_target_design(_design : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _design_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create an EM Target design. 

Parameters: 
     

**design**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the target design. Possible choices are `"Icepak"` or `"Mechanical"`. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the EM setup to link to the target design. The default is `None`, in which case the `LastAdaptive` setup is used. 

**design_setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
For Icepak designs, specify `"Forced"` for forced convention or `"Natural"` for natural convention. The default is `None`, in which case the `"Forced"` option is used. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.CreateEMLossTarget

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Maxwell3d, Mechanical
>>> from ansys.aedt.core.generic.aedt_constants import IcepakFeaConstants
>>> m3d = Maxwell3d(version="2026.1")
>>> # From 2026.1, Mechanical has been renamed to IcepakFEA.
>>> # Pass the target design through the IcepakFeaConstants metaclass.
>>> # This automatically selects the correct AEDT API design name.
>>> m3d.create_em_target_design(design=IcepakFeaConstants.NAME)
>>> mechanical = Mechanical(version="2026.1")
>>> mechanical.release_desktop(False, False)

```
Copy to clipboard