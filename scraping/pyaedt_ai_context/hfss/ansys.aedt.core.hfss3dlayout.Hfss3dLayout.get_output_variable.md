---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.get_output_variable.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# get_output_variable 

Hfss3dLayout.get_output_variable(_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) 
    
Retrieve the value of the output variable. 

Parameters: 
     

**variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variable. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the solution in the format “name : sweep_name”. If None, the first available solution is used. Default is None. 

Returns: 
     

[`type`](https://docs.python.org/3.11/library/functions.html#type "\(in Python v3.11\)")
    
Value of the output variable.
References

```
>>> oDesign.GetNominalVariation
>>> oModule.GetOutputVariableValue

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.get_output_variable("my_var")

```
Copy to clipboard
# get_output_variable 

Hfss3dLayout.get_output_variable(_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) 
    
Retrieve the value of the output variable. 

Parameters: 
     

**variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variable. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the solution in the format “name : sweep_name”. If None, the first available solution is used. Default is None. 

Returns: 
     

[`type`](https://docs.python.org/3.11/library/functions.html#type "\(in Python v3.11\)")
    
Value of the output variable.
References

```
>>> oDesign.GetNominalVariation
>>> oModule.GetOutputVariableValue

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.get_output_variable("my_var")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.get_output_variable.rst.txt)

# get_output_variable 

Hfss3dLayout.get_output_variable(_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) 
    
Retrieve the value of the output variable. 

Parameters: 
     

**variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variable. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the solution in the format “name : sweep_name”. If None, the first available solution is used. Default is None. 

Returns: 
     

[`type`](https://docs.python.org/3.11/library/functions.html#type "\(in Python v3.11\)")
    
Value of the output variable.
References

```
>>> oDesign.GetNominalVariation
>>> oModule.GetOutputVariableValue

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.get_output_variable("my_var")

```
Copy to clipboard