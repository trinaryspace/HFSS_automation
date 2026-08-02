---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.update_var.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# update_var 

Variable.update_var() → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Push the current variable state to AEDT via variable manager.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss["p1"] = "10mm"
>>> var = hfss.variable_manager["p1"]
>>> var.update_var()

```
Copy to clipboard
# update_var 

Variable.update_var() → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Push the current variable state to AEDT via variable manager.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss["p1"] = "10mm"
>>> var = hfss.variable_manager["p1"]
>>> var.update_var()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.application.variables.Variable.update_var.rst.txt)

# update_var 

Variable.update_var() → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Push the current variable state to AEDT via variable manager.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss["p1"] = "10mm"
>>> var = hfss.variable_manager["p1"]
>>> var.update_var()

```
Copy to clipboard