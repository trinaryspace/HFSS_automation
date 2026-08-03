---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.as_vector_z.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# as_vector_z 

ScalarComplex.as_vector_z() → [VectorComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex") 
    
Place this scalar in the z component of a vector (calculator `VecZ`). 

Returns: 
     

[`VectorComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex")
    
Complex vector expression with the scalar in the z component.
Examples
Embed a complex scalar into the z component of a vector.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("V").as_vector_z().operations[-1]
"Operation('VecZ')"

```
Copy to clipboard
# as_vector_z 

ScalarComplex.as_vector_z() → [VectorComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex") 
    
Place this scalar in the z component of a vector (calculator `VecZ`). 

Returns: 
     

[`VectorComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex")
    
Complex vector expression with the scalar in the z component.
Examples
Embed a complex scalar into the z component of a vector.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("V").as_vector_z().operations[-1]
"Operation('VecZ')"

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.as_vector_z.rst.txt)

# as_vector_z 

ScalarComplex.as_vector_z() → [VectorComplex](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex") 
    
Place this scalar in the z component of a vector (calculator `VecZ`). 

Returns: 
     

[`VectorComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex")
    
Complex vector expression with the scalar in the z component.
Examples
Embed a complex scalar into the z component of a vector.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("V").as_vector_z().operations[-1]
"Operation('VecZ')"

```
Copy to clipboard