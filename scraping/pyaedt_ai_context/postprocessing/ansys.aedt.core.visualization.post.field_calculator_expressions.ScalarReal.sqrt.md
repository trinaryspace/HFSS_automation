---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.sqrt.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# sqrt 

ScalarReal.sqrt() → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Square root (calculator `Sqrt`). 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression with `Operation('Sqrt')` appended.
Examples
Take the square root of a real scalar field.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).sqrt().operations[-1]
"Operation('Sqrt')"

```
Copy to clipboard
# sqrt 

ScalarReal.sqrt() → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Square root (calculator `Sqrt`). 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression with `Operation('Sqrt')` appended.
Examples
Take the square root of a real scalar field.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).sqrt().operations[-1]
"Operation('Sqrt')"

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.sqrt.rst.txt)

# sqrt 

ScalarReal.sqrt() → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Square root (calculator `Sqrt`). 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression with `Operation('Sqrt')` appended.
Examples
Take the square root of a real scalar field.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).sqrt().operations[-1]
"Operation('Sqrt')"

```
Copy to clipboard