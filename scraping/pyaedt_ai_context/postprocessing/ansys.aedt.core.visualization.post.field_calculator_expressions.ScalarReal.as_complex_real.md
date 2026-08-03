---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.as_complex_real.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# as_complex_real 

ScalarReal.as_complex_real() → [ScalarComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex") 
    
Use this real scalar as the real part of a complex number (calculator `CmplxR`). 

Returns: 
     

[`ScalarComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex")
    
Complex scalar expression using this value as the real component.
Examples
Promote a real scalar to the real part of a complex value.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).as_complex_real().operations[-1]
"Operation('CmplxR')"

```
Copy to clipboard
# as_complex_real 

ScalarReal.as_complex_real() → [ScalarComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex") 
    
Use this real scalar as the real part of a complex number (calculator `CmplxR`). 

Returns: 
     

[`ScalarComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex")
    
Complex scalar expression using this value as the real component.
Examples
Promote a real scalar to the real part of a complex value.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).as_complex_real().operations[-1]
"Operation('CmplxR')"

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.as_complex_real.rst.txt)

# as_complex_real 

ScalarReal.as_complex_real() → [ScalarComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex") 
    
Use this real scalar as the real part of a complex number (calculator `CmplxR`). 

Returns: 
     

[`ScalarComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex")
    
Complex scalar expression using this value as the real component.
Examples
Promote a real scalar to the real part of a complex value.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("Phi", is_complex=False).as_complex_real().operations[-1]
"Operation('CmplxR')"

```
Copy to clipboard