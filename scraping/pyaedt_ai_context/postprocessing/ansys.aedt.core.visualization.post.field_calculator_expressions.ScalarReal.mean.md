---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.mean.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# mean 

ScalarReal.mean(_over : CalculatorGeometry_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Mean over a geometry (calculator `Mean`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the reduction. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression reduced with `Mean`.
Examples
Compute the mean value on a volume.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Volume
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).mean(Volume("Box1")).operations[-1]
"Operation('Mean')"

```
Copy to clipboard
# mean 

ScalarReal.mean(_over : CalculatorGeometry_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Mean over a geometry (calculator `Mean`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the reduction. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression reduced with `Mean`.
Examples
Compute the mean value on a volume.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Volume
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).mean(Volume("Box1")).operations[-1]
"Operation('Mean')"

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.mean.rst.txt)

# mean 

ScalarReal.mean(_over : CalculatorGeometry_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Mean over a geometry (calculator `Mean`). 

Parameters: 
     

**over**`CalculatorGeometry` 
    
Geometry used for the reduction. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression reduced with `Mean`.
Examples
Compute the mean value on a volume.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions, Volume
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).mean(Volume("Box1")).operations[-1]
"Operation('Mean')"

```
Copy to clipboard