---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# FieldExpressions 

class ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions(_calculator_) 
    
Builder for AEDT Fields Calculator expressions.
The AEDT Fields Calculator is driven by a stack of string operations (reverse Polish notation), for example `Fundamental_Quantity('E')`, `Operation('Real')`, `Operation('Tangent')`, `Operation('Dot')`. Assembling those strings by hand is error-prone and hides which operations are valid for a given quantity.
This class wraps that operation grammar with four typed expression classes that mirror the calculator’s register kinds:
  * [`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal"), a real scalar quantity.
  * [`ScalarComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex"), a complex scalar quantity.
  * [`VectorReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal"), a real 3-vector quantity.
  * [`VectorComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex"), a complex 3-vector quantity.

The builder wraps the calculator operations:
  * input: fundamental and named quantities; real / complex scalar constants; `vector_constant`; `function` (a design variable / `Scalar_Function`).
  * general: `+ - * /` and negation (numbers are accepted as operands, for example `E * 2`); `real` / `imaginary` / `conjugate` / `magnitude` / `component_magnitude` / `phase` / `at_phase` / `smooth` / `absolute`; `as_complex_real` / `as_complex_imag` and the `cmplx()` helper.
  * scalar: `sqrt` / `power` / `ln` / `log10` / `sin` / `cos` / `tan` / `asin` / `acos` / `atan` / `derivative` / `gradient` and forming a vector with `as_vector_x` / `as_vector_y` / `as_vector_z`.
  * vector: components `scalar_x` / `scalar_y` / `scalar_z`; `dot` / `cross` / `curl` / `divergence`; and the geometry unit vectors `FieldExpressions.tangent` / `FieldExpressions.normal` (push a unit vector to dot a field against, for tangential / flux quantities).
  * output: `integrate` / `maximum` / `minimum` / `mean` / `std` / `value` / `max_position` / `min_position` over a [`Line`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.Line.html#ansys.aedt.core.visualization.post.field_calculator_expressions.Line "ansys.aedt.core.visualization.post.field_calculator_expressions.Line"), [`Surface`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.Surface.html#ansys.aedt.core.visualization.post.field_calculator_expressions.Surface "ansys.aedt.core.visualization.post.field_calculator_expressions.Surface"), or [`Volume`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.Volume.html#ansys.aedt.core.visualization.post.field_calculator_expressions.Volume "ansys.aedt.core.visualization.post.field_calculator_expressions.Volume").

Examples

```
>>> fx = FieldExpressions(calculator=None)
>>> e_vector = fx.vector("E")
>>> energy = (e_vector.magnitude() * e_vector.magnitude()).integrate(Surface("MySheet"))
>>> energy.operations[-3:]
["EnterSurface('MySheet')", "Operation('SurfaceValue')", "Operation('Integrate')"]

```
Copy to clipboard
Methods  
| [`FieldExpressions.complex_constant`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.complex_constant.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.complex_constant "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.complex_constant")(real, imag)  | Create a complex scalar constant.  |  
| --- | --- |  
| [`FieldExpressions.function`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.function.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.function "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.function")(name)  | Create a scalar expression from a design variable or function.  |  
| [`FieldExpressions.named_expression`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.named_expression.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.named_expression "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.named_expression")(name[, ...])  | Start from a previously defined named expression.  |  
| [`FieldExpressions.normal_vector`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.normal_vector.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.normal_vector "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.normal_vector")()  | Push the geometry unit normal vector.  |  
| [`FieldExpressions.scalar`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.scalar.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.scalar "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.scalar")(quantity[, is_complex])  | Start from a fundamental scalar quantity.  |  
| [`FieldExpressions.scalar_constant`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.scalar_constant.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.scalar_constant "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.scalar_constant")(value)  | Create a real scalar constant.  |  
| [`FieldExpressions.tangent_vector`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.tangent_vector.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.tangent_vector "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.tangent_vector")()  | Push the geometry unit tangent vector.  |  
| [`FieldExpressions.vector`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.vector.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.vector "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.vector")([quantity, is_complex])  | Start from a fundamental vector quantity.  |  
| [`FieldExpressions.vector_constant`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.vector_constant.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.vector_constant "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.vector_constant")(x, y, z)  | Create a constant real vector.  |  
Attributes  
| [`FieldExpressions.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.public_dir.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.public_dir "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |  
# FieldExpressions 

class ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions(_calculator_) 
    
Builder for AEDT Fields Calculator expressions.
The AEDT Fields Calculator is driven by a stack of string operations (reverse Polish notation), for example `Fundamental_Quantity('E')`, `Operation('Real')`, `Operation('Tangent')`, `Operation('Dot')`. Assembling those strings by hand is error-prone and hides which operations are valid for a given quantity.
This class wraps that operation grammar with four typed expression classes that mirror the calculator’s register kinds:
  * [`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal"), a real scalar quantity.
  * [`ScalarComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex"), a complex scalar quantity.
  * [`VectorReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal"), a real 3-vector quantity.
  * [`VectorComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex"), a complex 3-vector quantity.

The builder wraps the calculator operations:
  * input: fundamental and named quantities; real / complex scalar constants; `vector_constant`; `function` (a design variable / `Scalar_Function`).
  * general: `+ - * /` and negation (numbers are accepted as operands, for example `E * 2`); `real` / `imaginary` / `conjugate` / `magnitude` / `component_magnitude` / `phase` / `at_phase` / `smooth` / `absolute`; `as_complex_real` / `as_complex_imag` and the `cmplx()` helper.
  * scalar: `sqrt` / `power` / `ln` / `log10` / `sin` / `cos` / `tan` / `asin` / `acos` / `atan` / `derivative` / `gradient` and forming a vector with `as_vector_x` / `as_vector_y` / `as_vector_z`.
  * vector: components `scalar_x` / `scalar_y` / `scalar_z`; `dot` / `cross` / `curl` / `divergence`; and the geometry unit vectors `FieldExpressions.tangent` / `FieldExpressions.normal` (push a unit vector to dot a field against, for tangential / flux quantities).
  * output: `integrate` / `maximum` / `minimum` / `mean` / `std` / `value` / `max_position` / `min_position` over a [`Line`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.Line.html#ansys.aedt.core.visualization.post.field_calculator_expressions.Line "ansys.aedt.core.visualization.post.field_calculator_expressions.Line"), [`Surface`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.Surface.html#ansys.aedt.core.visualization.post.field_calculator_expressions.Surface "ansys.aedt.core.visualization.post.field_calculator_expressions.Surface"), or [`Volume`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.Volume.html#ansys.aedt.core.visualization.post.field_calculator_expressions.Volume "ansys.aedt.core.visualization.post.field_calculator_expressions.Volume").

Examples

```
>>> fx = FieldExpressions(calculator=None)
>>> e_vector = fx.vector("E")
>>> energy = (e_vector.magnitude() * e_vector.magnitude()).integrate(Surface("MySheet"))
>>> energy.operations[-3:]
["EnterSurface('MySheet')", "Operation('SurfaceValue')", "Operation('Integrate')"]

```
Copy to clipboard
Methods  
| [`FieldExpressions.complex_constant`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.complex_constant.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.complex_constant "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.complex_constant")(real, imag)  | Create a complex scalar constant.  |  
| --- | --- |  
| [`FieldExpressions.function`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.function.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.function "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.function")(name)  | Create a scalar expression from a design variable or function.  |  
| [`FieldExpressions.named_expression`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.named_expression.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.named_expression "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.named_expression")(name[, ...])  | Start from a previously defined named expression.  |  
| [`FieldExpressions.normal_vector`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.normal_vector.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.normal_vector "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.normal_vector")()  | Push the geometry unit normal vector.  |  
| [`FieldExpressions.scalar`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.scalar.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.scalar "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.scalar")(quantity[, is_complex])  | Start from a fundamental scalar quantity.  |  
| [`FieldExpressions.scalar_constant`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.scalar_constant.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.scalar_constant "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.scalar_constant")(value)  | Create a real scalar constant.  |  
| [`FieldExpressions.tangent_vector`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.tangent_vector.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.tangent_vector "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.tangent_vector")()  | Push the geometry unit tangent vector.  |  
| [`FieldExpressions.vector`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.vector.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.vector "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.vector")([quantity, is_complex])  | Start from a fundamental vector quantity.  |  
| [`FieldExpressions.vector_constant`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.vector_constant.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.vector_constant "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.vector_constant")(x, y, z)  | Create a constant real vector.  |  
Attributes  
| [`FieldExpressions.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.public_dir.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.public_dir "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.rst.txt)

# FieldExpressions 

class ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions(_calculator_) 
    
Builder for AEDT Fields Calculator expressions.
The AEDT Fields Calculator is driven by a stack of string operations (reverse Polish notation), for example `Fundamental_Quantity('E')`, `Operation('Real')`, `Operation('Tangent')`, `Operation('Dot')`. Assembling those strings by hand is error-prone and hides which operations are valid for a given quantity.
This class wraps that operation grammar with four typed expression classes that mirror the calculator’s register kinds:
  * [`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal"), a real scalar quantity.
  * [`ScalarComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex"), a complex scalar quantity.
  * [`VectorReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorReal"), a real 3-vector quantity.
  * [`VectorComplex`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex.html#ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex "ansys.aedt.core.visualization.post.field_calculator_expressions.VectorComplex"), a complex 3-vector quantity.

The builder wraps the calculator operations:
  * input: fundamental and named quantities; real / complex scalar constants; `vector_constant`; `function` (a design variable / `Scalar_Function`).
  * general: `+ - * /` and negation (numbers are accepted as operands, for example `E * 2`); `real` / `imaginary` / `conjugate` / `magnitude` / `component_magnitude` / `phase` / `at_phase` / `smooth` / `absolute`; `as_complex_real` / `as_complex_imag` and the `cmplx()` helper.
  * scalar: `sqrt` / `power` / `ln` / `log10` / `sin` / `cos` / `tan` / `asin` / `acos` / `atan` / `derivative` / `gradient` and forming a vector with `as_vector_x` / `as_vector_y` / `as_vector_z`.
  * vector: components `scalar_x` / `scalar_y` / `scalar_z`; `dot` / `cross` / `curl` / `divergence`; and the geometry unit vectors `FieldExpressions.tangent` / `FieldExpressions.normal` (push a unit vector to dot a field against, for tangential / flux quantities).
  * output: `integrate` / `maximum` / `minimum` / `mean` / `std` / `value` / `max_position` / `min_position` over a [`Line`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.Line.html#ansys.aedt.core.visualization.post.field_calculator_expressions.Line "ansys.aedt.core.visualization.post.field_calculator_expressions.Line"), [`Surface`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.Surface.html#ansys.aedt.core.visualization.post.field_calculator_expressions.Surface "ansys.aedt.core.visualization.post.field_calculator_expressions.Surface"), or [`Volume`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.Volume.html#ansys.aedt.core.visualization.post.field_calculator_expressions.Volume "ansys.aedt.core.visualization.post.field_calculator_expressions.Volume").

Examples

```
>>> fx = FieldExpressions(calculator=None)
>>> e_vector = fx.vector("E")
>>> energy = (e_vector.magnitude() * e_vector.magnitude()).integrate(Surface("MySheet"))
>>> energy.operations[-3:]
["EnterSurface('MySheet')", "Operation('SurfaceValue')", "Operation('Integrate')"]

```
Copy to clipboard
Methods  
| [`FieldExpressions.complex_constant`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.complex_constant.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.complex_constant "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.complex_constant")(real, imag)  | Create a complex scalar constant.  |  
| --- | --- |  
| [`FieldExpressions.function`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.function.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.function "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.function")(name)  | Create a scalar expression from a design variable or function.  |  
| [`FieldExpressions.named_expression`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.named_expression.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.named_expression "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.named_expression")(name[, ...])  | Start from a previously defined named expression.  |  
| [`FieldExpressions.normal_vector`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.normal_vector.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.normal_vector "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.normal_vector")()  | Push the geometry unit normal vector.  |  
| [`FieldExpressions.scalar`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.scalar.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.scalar "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.scalar")(quantity[, is_complex])  | Start from a fundamental scalar quantity.  |  
| [`FieldExpressions.scalar_constant`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.scalar_constant.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.scalar_constant "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.scalar_constant")(value)  | Create a real scalar constant.  |  
| [`FieldExpressions.tangent_vector`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.tangent_vector.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.tangent_vector "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.tangent_vector")()  | Push the geometry unit tangent vector.  |  
| [`FieldExpressions.vector`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.vector.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.vector "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.vector")([quantity, is_complex])  | Start from a fundamental vector quantity.  |  
| [`FieldExpressions.vector_constant`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.vector_constant.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.vector_constant "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.vector_constant")(x, y, z)  | Create a constant real vector.  |  
Attributes  
| [`FieldExpressions.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.public_dir.html#ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.public_dir "ansys.aedt.core.visualization.post.field_calculator_expressions.FieldExpressions.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |