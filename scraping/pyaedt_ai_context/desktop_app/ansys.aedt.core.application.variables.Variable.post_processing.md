---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.application.variables.Variable.post_processing.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# post_processing 

property Variable.post_processing: [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Whether this variable is a post-processing variable.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.variable_manager.set_variable("post_gain", expression="1", is_post_processing=True)
>>> var = hfss.variable_manager["post_gain"]
>>> var.post_processing

```
Copy to clipboard
# post_processing 

property Variable.post_processing: [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Whether this variable is a post-processing variable.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.variable_manager.set_variable("post_gain", expression="1", is_post_processing=True)
>>> var = hfss.variable_manager["post_gain"]
>>> var.post_processing

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.application.variables.Variable.post_processing.rst.txt)

# post_processing 

property Variable.post_processing: [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Whether this variable is a post-processing variable.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.variable_manager.set_variable("post_gain", expression="1", is_post_processing=True)
>>> var = hfss.variable_manager["post_gain"]
>>> var.post_processing

```
Copy to clipboard