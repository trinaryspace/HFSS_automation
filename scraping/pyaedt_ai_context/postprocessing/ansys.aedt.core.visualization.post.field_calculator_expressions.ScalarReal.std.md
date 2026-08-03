---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.std.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# std 

ScalarReal.std(_over : CalculatorGeometry_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Standard deviation over a geometry (calculator `Std`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the reduction. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression reduced with `Std`.
Examples
Compute the standard deviation on a volume.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Volume
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).std(Volume("Box1")).operations[-1]
"Operation('Std')"

```
Copy to clipboard
# std 

ScalarReal.std(_over : CalculatorGeometry_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Standard deviation over a geometry (calculator `Std`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the reduction. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression reduced with `Std`.
Examples
Compute the standard deviation on a volume.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Volume
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).std(Volume("Box1")).operations[-1]
"Operation('Std')"

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.std.rst.txt)

# std 

ScalarReal.std(_over : CalculatorGeometry_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Standard deviation over a geometry (calculator `Std`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the reduction. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression reduced with `Std`.
Examples
Compute the standard deviation on a volume.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Volume
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).std(Volume("Box1")).operations[-1]
"Operation('Std')"

```
Copy to clipboard