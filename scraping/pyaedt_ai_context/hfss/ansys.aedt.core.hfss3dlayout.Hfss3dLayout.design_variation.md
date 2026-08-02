---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.design_variation.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# design_variation 

Hfss3dLayout.design_variation(_variation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Generate a string to specify a desired variation.
This method converts an input string defining a desired solution variation into a valid string taking into account all existing design properties and project variables, including dependent (non-sweep) properties.
This is needed because the standard method COM function `GetVariationVariableValue` does not work for obtaining values of dependent (non-sweep) variables. Using the object-oriented scripting model, which is a beta feature, could make this redundant in future releases. 

Parameters: 
     

**variation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Variation string. For example, `"p1=1mm"` or `"p2=3mm"`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
String specifying the desired variation.
References

```
>>> oDesign.GetNominalVariation

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.design_variation("width=10mm")

```
Copy to clipboard
# design_variation 

Hfss3dLayout.design_variation(_variation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Generate a string to specify a desired variation.
This method converts an input string defining a desired solution variation into a valid string taking into account all existing design properties and project variables, including dependent (non-sweep) properties.
This is needed because the standard method COM function `GetVariationVariableValue` does not work for obtaining values of dependent (non-sweep) variables. Using the object-oriented scripting model, which is a beta feature, could make this redundant in future releases. 

Parameters: 
     

**variation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Variation string. For example, `"p1=1mm"` or `"p2=3mm"`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
String specifying the desired variation.
References

```
>>> oDesign.GetNominalVariation

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.design_variation("width=10mm")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.design_variation.rst.txt)

# design_variation 

Hfss3dLayout.design_variation(_variation : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Generate a string to specify a desired variation.
This method converts an input string defining a desired solution variation into a valid string taking into account all existing design properties and project variables, including dependent (non-sweep) properties.
This is needed because the standard method COM function `GetVariationVariableValue` does not work for obtaining values of dependent (non-sweep) variables. Using the object-oriented scripting model, which is a beta feature, could make this redundant in future releases. 

Parameters: 
     

**variation**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Variation string. For example, `"p1=1mm"` or `"p2=3mm"`. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
String specifying the desired variation.
References

```
>>> oDesign.GetNominalVariation

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> app.design_variation("width=10mm")

```
Copy to clipboard