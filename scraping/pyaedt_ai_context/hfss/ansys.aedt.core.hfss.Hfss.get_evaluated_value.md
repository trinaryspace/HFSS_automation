---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.get_evaluated_value.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# get_evaluated_value 

Hfss.get_evaluated_value(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Retrieve the evaluated value of a design property or project variable in SI units if no unit is provided. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the design property or project variable. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the unit to use for rescaling. The default is `None`, in which case SI units are applied by default. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Evaluated value of the design property or project variable in SI units.
References

```
>>> oDesign.GetNominalVariation
>>> oDesign.GetVariationVariableValue

```
Copy to clipboard
Examples

```
>>> M3D = Maxwell3d()
>>> M3D["p1"] = "10mm"
>>> M3D["p2"] = "20mm"
>>> M3D["p3"] = "P1 * p2"
>>> eval_p3 = M3D.get_evaluated_value("p3")

```
Copy to clipboard
# get_evaluated_value 

Hfss.get_evaluated_value(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Retrieve the evaluated value of a design property or project variable in SI units if no unit is provided. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the design property or project variable. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the unit to use for rescaling. The default is `None`, in which case SI units are applied by default. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Evaluated value of the design property or project variable in SI units.
References

```
>>> oDesign.GetNominalVariation
>>> oDesign.GetVariationVariableValue

```
Copy to clipboard
Examples

```
>>> M3D = Maxwell3d()
>>> M3D["p1"] = "10mm"
>>> M3D["p2"] = "20mm"
>>> M3D["p3"] = "P1 * p2"
>>> eval_p3 = M3D.get_evaluated_value("p3")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.get_evaluated_value.rst.txt)

# get_evaluated_value 

Hfss.get_evaluated_value(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _units : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Retrieve the evaluated value of a design property or project variable in SI units if no unit is provided. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the design property or project variable. 

**units**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the unit to use for rescaling. The default is `None`, in which case SI units are applied by default. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Evaluated value of the design property or project variable in SI units.
References

```
>>> oDesign.GetNominalVariation
>>> oDesign.GetVariationVariableValue

```
Copy to clipboard
Examples

```
>>> M3D = Maxwell3d()
>>> M3D["p1"] = "10mm"
>>> M3D["p2"] = "20mm"
>>> M3D["p3"] = "P1 * p2"
>>> eval_p3 = M3D.get_evaluated_value("p3")

```
Copy to clipboard