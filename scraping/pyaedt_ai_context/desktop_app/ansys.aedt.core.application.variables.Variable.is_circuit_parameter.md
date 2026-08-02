---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.is_circuit_parameter.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# is_circuit_parameter 

property Variable.is_circuit_parameter: [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Whether this variable is a circuit parameter (for supported design types).
Examples

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> circuit["Rload"] = "50ohm"
>>> var = circuit.variable_manager["Rload"]
>>> var.is_circuit_parameter

```
Copy to clipboard
# is_circuit_parameter 

property Variable.is_circuit_parameter: [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Whether this variable is a circuit parameter (for supported design types).
Examples

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> circuit["Rload"] = "50ohm"
>>> var = circuit.variable_manager["Rload"]
>>> var.is_circuit_parameter

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.application.variables.Variable.is_circuit_parameter.rst.txt)

# is_circuit_parameter 

property Variable.is_circuit_parameter: [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Whether this variable is a circuit parameter (for supported design types).
Examples

```
>>> from ansys.aedt.core import Circuit
>>> circuit = Circuit()
>>> circuit["Rload"] = "50ohm"
>>> var = circuit.variable_manager["Rload"]
>>> var.is_circuit_parameter

```
Copy to clipboard