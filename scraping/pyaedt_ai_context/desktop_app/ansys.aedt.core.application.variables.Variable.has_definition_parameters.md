---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.has_definition_parameters.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# has_definition_parameters 

property Variable.has_definition_parameters: [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Whether the design type has DefinitionParameters or only LocalVariables.
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> h3d = Hfss3dLayout()
>>> h3d["trace_width"] = "0.2mm"
>>> var = h3d.variable_manager["trace_width"]
>>> var.has_definition_parameters

```
Copy to clipboard
# has_definition_parameters 

property Variable.has_definition_parameters: [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Whether the design type has DefinitionParameters or only LocalVariables.
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> h3d = Hfss3dLayout()
>>> h3d["trace_width"] = "0.2mm"
>>> var = h3d.variable_manager["trace_width"]
>>> var.has_definition_parameters

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.application.variables.Variable.has_definition_parameters.rst.txt)

# has_definition_parameters 

property Variable.has_definition_parameters: [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Whether the design type has DefinitionParameters or only LocalVariables.
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> h3d = Hfss3dLayout()
>>> h3d["trace_width"] = "0.2mm"
>>> var = h3d.variable_manager["trace_width"]
>>> var.has_definition_parameters

```
Copy to clipboard