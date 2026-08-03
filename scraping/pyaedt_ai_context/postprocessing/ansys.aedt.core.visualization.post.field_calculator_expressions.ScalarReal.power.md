---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.power.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# power 

ScalarReal.power(_exponent : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Constant power (calculator `Pow`). 

Parameters: 
     

**exponent**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Exponent pushed as a scalar constant before `Pow`. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression raised to the requested exponent.
Examples
Square a scalar quantity.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).power(2).operations[-2:]
['Scalar_Constant(2)', "Operation('Pow')"]

```
Copy to clipboard
# power 

ScalarReal.power(_exponent : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Constant power (calculator `Pow`). 

Parameters: 
     

**exponent**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Exponent pushed as a scalar constant before `Pow`. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression raised to the requested exponent.
Examples
Square a scalar quantity.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).power(2).operations[-2:]
['Scalar_Constant(2)', "Operation('Pow')"]

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.power.rst.txt)

# power 

ScalarReal.power(_exponent : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Constant power (calculator `Pow`). 

Parameters: 
     

**exponent**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Exponent pushed as a scalar constant before `Pow`. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression raised to the requested exponent.
Examples
Square a scalar quantity.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).power(2).operations[-2:]
['Scalar_Constant(2)', "Operation('Pow')"]

```
Copy to clipboard