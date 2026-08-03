---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expressions.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# expressions 

property FieldsCalculator.expressions 
    
Typed, fluent builder for Fields Calculator expressions.
Returns a [`FieldExpressions`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions") factory that produces strongly typed expression objects. Chaining their `.method()` calls and the `dot` / `cross` helpers builds the calculator operation stack with type safety, instead of assembling the operation strings by hand. 

Returns: 
     

[`FieldExpressions`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions")
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import Volume
>>> hfss = Hfss()
>>> fx = hfss.post.fields_calculator.expressions
>>> e_vec = fx.vector("E")  # VectorComplex
>>> mag_e = e_vec.magnitude()  # ScalarReal
>>> value = mag_e.maximum(Volume("MySolid")).evaluate(setup="Setup1 : LastAdaptive")

```
Copy to clipboard
# expressions 

property FieldsCalculator.expressions 
    
Typed, fluent builder for Fields Calculator expressions.
Returns a [`FieldExpressions`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions") factory that produces strongly typed expression objects. Chaining their `.method()` calls and the `dot` / `cross` helpers builds the calculator operation stack with type safety, instead of assembling the operation strings by hand. 

Returns: 
     

[`FieldExpressions`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions")
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import Volume
>>> hfss = Hfss()
>>> fx = hfss.post.fields_calculator.expressions
>>> e_vec = fx.vector("E")  # VectorComplex
>>> mag_e = e_vec.magnitude()  # ScalarReal
>>> value = mag_e.maximum(Volume("MySolid")).evaluate(setup="Setup1 : LastAdaptive")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.fields_calculator.FieldsCalculator.expressions.rst.txt)

# expressions 

property FieldsCalculator.expressions 
    
Typed, fluent builder for Fields Calculator expressions.
Returns a [`FieldExpressions`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions") factory that produces strongly typed expression objects. Chaining their `.method()` calls and the `dot` / `cross` helpers builds the calculator operation stack with type safety, instead of assembling the operation strings by hand. 

Returns: 
     

[`FieldExpressions`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions")
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import Volume
>>> hfss = Hfss()
>>> fx = hfss.post.fields_calculator.expressions
>>> e_vec = fx.vector("E")  # VectorComplex
>>> mag_e = e_vec.magnitude()  # ScalarReal
>>> value = mag_e.maximum(Volume("MySolid")).evaluate(setup="Setup1 : LastAdaptive")

```
Copy to clipboard