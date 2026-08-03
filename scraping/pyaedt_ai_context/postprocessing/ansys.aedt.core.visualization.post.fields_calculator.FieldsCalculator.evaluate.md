---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.evaluate.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# evaluate 

FieldsCalculator.evaluate(_expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _intrinsics : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Evaluate an expression and return the value. 

Parameters: 
     

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Expression name. The expression must exist already in the named expressions list in AEDT Fields Calculator. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Solution name. If not provided the nominal adaptive solution is taken. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Intrinsics variables provided as a dictionary. Key is the variable name and value is the variable value. These are typically: frequency, time and phase. If it is a dictionary, keys depend on the solution type and can be expressed as: - `"Freq"`. - `"Time"`. - `"Phase"`. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Value computed.
Examples

```
>>> from ansys.aedt.core.visualization.post.fields_calculator import FieldsCalculator
>>> obj = FieldsCalculator()
>>> obj.evaluate(expression="dB(S(1,1))")

```
Copy to clipboard
# evaluate 

FieldsCalculator.evaluate(_expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _intrinsics : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Evaluate an expression and return the value. 

Parameters: 
     

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Expression name. The expression must exist already in the named expressions list in AEDT Fields Calculator. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Solution name. If not provided the nominal adaptive solution is taken. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Intrinsics variables provided as a dictionary. Key is the variable name and value is the variable value. These are typically: frequency, time and phase. If it is a dictionary, keys depend on the solution type and can be expressed as: - `"Freq"`. - `"Time"`. - `"Phase"`. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Value computed.
Examples

```
>>> from ansys.aedt.core.visualization.post.fields_calculator import FieldsCalculator
>>> obj = FieldsCalculator()
>>> obj.evaluate(expression="dB(S(1,1))")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.evaluate.rst.txt)

# evaluate 

FieldsCalculator.evaluate(_expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _intrinsics : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Evaluate an expression and return the value. 

Parameters: 
     

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Expression name. The expression must exist already in the named expressions list in AEDT Fields Calculator. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Solution name. If not provided the nominal adaptive solution is taken. 

**intrinsics**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Intrinsics variables provided as a dictionary. Key is the variable name and value is the variable value. These are typically: frequency, time and phase. If it is a dictionary, keys depend on the solution type and can be expressed as: - `"Freq"`. - `"Time"`. - `"Phase"`. The default is `None` in which case the intrinsics value is automatically computed based on the setup. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")
    
Value computed.
Examples

```
>>> from ansys.aedt.core.visualization.post.fields_calculator import FieldsCalculator
>>> obj = FieldsCalculator()
>>> obj.evaluate(expression="dB(S(1,1))")

```
Copy to clipboard