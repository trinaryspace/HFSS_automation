---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.evaluate_expression.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# evaluate_expression 

Hfss3dLayout.evaluate_expression(_expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Evaluate a valid string expression and return the numerical value in SI units.
This method evaluates mathematical expressions containing design variables, project variables, units, and mathematical operations. It handles various expression types including: - Simple numeric values, for example `"42"`. - Values with units, for example `"10mm"`. - Mathematical expressions, for example `"34mm*sqrt(2)"` or `"pi/2"`. - Variable references, for example `"$var1"`. - PWL (Piecewise Linear) dataset references. - Combined expressions, for example `"$G1*p2/34"`. 

Parameters: 
     

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
A valid string expression for a design property or project variable. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Evaluated value for the string expression in SI units. - Returns `float` for successfully evaluated numeric expressions - Returns `str` for PWL dataset references or invalid expressions - Returns `None` if evaluation fails completely
Notes
The method attempts multiple strategies to evaluate the expression:
  * Direct variable lookup if the expression is a variable name.
  * Check for PWL dataset references.
  * Try direct numeric conversion.
  * Create a temporary internal variable to leverage AEDT’s expression evaluator.

For expressions containing project variables (prefixed with `$`), AEDT restrictions apply. Project variables cannot reference design variables.
The method uses an internal variable named `"pyaedt_evaluator"` for complex evaluations. All results are returned in SI units regardless of the input unit system.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss["width"] = "10mm"
>>> hfss["height"] = "20mm"
>>> # Evaluate simple numeric value
>>> result = hfss.evaluate_expression("42")  # Returns 42.0
>>> # Evaluate value with units
>>> result = hfss.evaluate_expression("10mm")  # Returns 0.01 (in meters)
>>> # Evaluate expression with variables
>>> result = hfss.evaluate_expression("width*height")  # Returns 0.0002 (in m^2)
>>> # Evaluate mathematical expression
>>> result = hfss.evaluate_expression("sqrt(width^2 + height^2)")

```
Copy to clipboard
# evaluate_expression 

Hfss3dLayout.evaluate_expression(_expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Evaluate a valid string expression and return the numerical value in SI units.
This method evaluates mathematical expressions containing design variables, project variables, units, and mathematical operations. It handles various expression types including: - Simple numeric values, for example `"42"`. - Values with units, for example `"10mm"`. - Mathematical expressions, for example `"34mm*sqrt(2)"` or `"pi/2"`. - Variable references, for example `"$var1"`. - PWL (Piecewise Linear) dataset references. - Combined expressions, for example `"$G1*p2/34"`. 

Parameters: 
     

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
A valid string expression for a design property or project variable. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Evaluated value for the string expression in SI units. - Returns `float` for successfully evaluated numeric expressions - Returns `str` for PWL dataset references or invalid expressions - Returns `None` if evaluation fails completely
Notes
The method attempts multiple strategies to evaluate the expression:
  * Direct variable lookup if the expression is a variable name.
  * Check for PWL dataset references.
  * Try direct numeric conversion.
  * Create a temporary internal variable to leverage AEDT’s expression evaluator.

For expressions containing project variables (prefixed with `$`), AEDT restrictions apply. Project variables cannot reference design variables.
The method uses an internal variable named `"pyaedt_evaluator"` for complex evaluations. All results are returned in SI units regardless of the input unit system.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss["width"] = "10mm"
>>> hfss["height"] = "20mm"
>>> # Evaluate simple numeric value
>>> result = hfss.evaluate_expression("42")  # Returns 42.0
>>> # Evaluate value with units
>>> result = hfss.evaluate_expression("10mm")  # Returns 0.01 (in meters)
>>> # Evaluate expression with variables
>>> result = hfss.evaluate_expression("width*height")  # Returns 0.0002 (in m^2)
>>> # Evaluate mathematical expression
>>> result = hfss.evaluate_expression("sqrt(width^2 + height^2)")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.evaluate_expression.rst.txt)

# evaluate_expression 

Hfss3dLayout.evaluate_expression(_expression : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_) → [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Evaluate a valid string expression and return the numerical value in SI units.
This method evaluates mathematical expressions containing design variables, project variables, units, and mathematical operations. It handles various expression types including: - Simple numeric values, for example `"42"`. - Values with units, for example `"10mm"`. - Mathematical expressions, for example `"34mm*sqrt(2)"` or `"pi/2"`. - Variable references, for example `"$var1"`. - PWL (Piecewise Linear) dataset references. - Combined expressions, for example `"$G1*p2/34"`. 

Parameters: 
     

**expression**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
A valid string expression for a design property or project variable. 

Returns: 
     

[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") or [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Evaluated value for the string expression in SI units. - Returns `float` for successfully evaluated numeric expressions - Returns `str` for PWL dataset references or invalid expressions - Returns `None` if evaluation fails completely
Notes
The method attempts multiple strategies to evaluate the expression:
  * Direct variable lookup if the expression is a variable name.
  * Check for PWL dataset references.
  * Try direct numeric conversion.
  * Create a temporary internal variable to leverage AEDT’s expression evaluator.

For expressions containing project variables (prefixed with `$`), AEDT restrictions apply. Project variables cannot reference design variables.
The method uses an internal variable named `"pyaedt_evaluator"` for complex evaluations. All results are returned in SI units regardless of the input unit system.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss["width"] = "10mm"
>>> hfss["height"] = "20mm"
>>> # Evaluate simple numeric value
>>> result = hfss.evaluate_expression("42")  # Returns 42.0
>>> # Evaluate value with units
>>> result = hfss.evaluate_expression("10mm")  # Returns 0.01 (in meters)
>>> # Evaluate expression with variables
>>> result = hfss.evaluate_expression("width*height")  # Returns 0.0002 (in m^2)
>>> # Evaluate mathematical expression
>>> result = hfss.evaluate_expression("sqrt(width^2 + height^2)")

```
Copy to clipboard