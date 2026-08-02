---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_output_variable.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# create_output_variable 

Hfss.create_output_variable(_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _context : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_differential : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create or modify an output variable. 

Parameters: 
     

**variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variable. 

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Value for the variable. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the solution in the format “name : sweep_name”. If None, the first available solution is used. Default is None. 

**context**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Context under which the output variable will produce results. 

**is_differential**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the expression corresponds to a differential pair. This parameter is only valid for HFSS 3D Layout and Circuit design types. The default value is False. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.CreateOutputVariable

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Circuit
>>> aedtapp = Circuit()
>>> aedtapp.create_output_variable(variable="output_diff", expression="S(Comm,Diff)", is_differential=True)
>>> aedtapp.create_output_variable(variable="output_terminal", expression="S(1,1)", is_differential=False)

```
Copy to clipboard
# create_output_variable 

Hfss.create_output_variable(_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _context : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_differential : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create or modify an output variable. 

Parameters: 
     

**variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variable. 

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Value for the variable. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the solution in the format “name : sweep_name”. If None, the first available solution is used. Default is None. 

**context**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Context under which the output variable will produce results. 

**is_differential**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the expression corresponds to a differential pair. This parameter is only valid for HFSS 3D Layout and Circuit design types. The default value is False. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.CreateOutputVariable

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Circuit
>>> aedtapp = Circuit()
>>> aedtapp.create_output_variable(variable="output_diff", expression="S(Comm,Diff)", is_differential=True)
>>> aedtapp.create_output_variable(variable="output_terminal", expression="S(1,1)", is_differential=False)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_output_variable.rst.txt)

# create_output_variable 

Hfss.create_output_variable(_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _solution : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _context : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _is_differential : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Create or modify an output variable. 

Parameters: 
     

**variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the variable. 

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Value for the variable. 

**solution**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the solution in the format “name : sweep_name”. If None, the first available solution is used. Default is None. 

**context**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Context under which the output variable will produce results. 

**is_differential**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the expression corresponds to a differential pair. This parameter is only valid for HFSS 3D Layout and Circuit design types. The default value is False. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.CreateOutputVariable

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Circuit
>>> aedtapp = Circuit()
>>> aedtapp.create_output_variable(variable="output_diff", expression="S(Comm,Diff)", is_differential=True)
>>> aedtapp.create_output_variable(variable="output_terminal", expression="S(1,1)", is_differential=False)

```
Copy to clipboard