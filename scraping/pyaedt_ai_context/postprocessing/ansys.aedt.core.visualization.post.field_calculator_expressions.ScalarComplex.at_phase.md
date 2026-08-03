---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.at_phase.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# at_phase 

ScalarComplex.at_phase(_phase_deg : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Real value at a given phase angle in degrees (calculator `AtPhase`). 

Parameters: 
     

**phase_deg**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Phase angle in degrees. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression evaluated at the requested phase.
Examples
Evaluate a complex scalar at a specific phase.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("V").at_phase(90).operations[-2:]
['Scalar_Constant(90)', "Operation('AtPhase')"]

```
Copy to clipboard
# at_phase 

ScalarComplex.at_phase(_phase_deg : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Real value at a given phase angle in degrees (calculator `AtPhase`). 

Parameters: 
     

**phase_deg**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Phase angle in degrees. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression evaluated at the requested phase.
Examples
Evaluate a complex scalar at a specific phase.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("V").at_phase(90).operations[-2:]
['Scalar_Constant(90)', "Operation('AtPhase')"]

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarComplex.at_phase.rst.txt)

# at_phase 

ScalarComplex.at_phase(_phase_deg : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_) → [ScalarReal](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal") 
    
Real value at a given phase angle in degrees (calculator `AtPhase`). 

Parameters: 
     

**phase_deg**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Phase angle in degrees. 

Returns: 
     

[`ScalarReal`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal.html#ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal "ansys.aedt.core.visualization.post.field_calculator_expressions.ScalarReal")
    
Real scalar expression evaluated at the requested phase.
Examples
Evaluate a complex scalar at a specific phase.

```
>>> from ansys.aedt.core.visualization.post.field_calculator_expressions import FieldExpressions
>>> fx = FieldExpressions(calculator=None)
>>> fx.scalar("V").at_phase(90).operations[-2:]
['Scalar_Constant(90)', "Operation('AtPhase')"]

```
Copy to clipboard