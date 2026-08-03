---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.conjugate.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# conjugate 

VectorComplex.conjugate() → [VectorComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex") 
    
Complex conjugate, component-wise (calculator `Conj`). 

Returns: 
     

[`VectorComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex")
    
Complex vector expression with the conjugate of each component.
Examples
Conjugate a complex vector field.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.vector("E").conjugate().operations[-1]
"Operation('Conj')"

```
Copy to clipboard
# conjugate 

VectorComplex.conjugate() → [VectorComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex") 
    
Complex conjugate, component-wise (calculator `Conj`). 

Returns: 
     

[`VectorComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex")
    
Complex vector expression with the conjugate of each component.
Examples
Conjugate a complex vector field.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.vector("E").conjugate().operations[-1]
"Operation('Conj')"

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.conjugate.rst.txt)

# conjugate 

VectorComplex.conjugate() → [VectorComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex") 
    
Complex conjugate, component-wise (calculator `Conj`). 

Returns: 
     

[`VectorComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex")
    
Complex vector expression with the conjugate of each component.
Examples
Conjugate a complex vector field.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.vector("E").conjugate().operations[-1]
"Operation('Conj')"

```
Copy to clipboard