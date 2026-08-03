---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.delete.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# delete 

UserDefinedComponent.delete() → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Delete the object.
The project must be saved after the operation to update the list of names for user-defined components.
References

```
>>> oEditor.Delete

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import hfss
>>> hfss = Hfss()
>>> hfss.modeler["UDM"].delete()
>>> hfss.save_project()
>>> hfss._project_dictionary = None
>>> udc = hfss.modeler.user_defined_component_names

```
Copy to clipboard
# delete 

UserDefinedComponent.delete() → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Delete the object.
The project must be saved after the operation to update the list of names for user-defined components.
References

```
>>> oEditor.Delete

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import hfss
>>> hfss = Hfss()
>>> hfss.modeler["UDM"].delete()
>>> hfss.save_project()
>>> hfss._project_dictionary = None
>>> udc = hfss.modeler.user_defined_component_names

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.components_3d.UserDefinedComponent.delete.rst.txt)

# delete 

UserDefinedComponent.delete() → [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Delete the object.
The project must be saved after the operation to update the list of names for user-defined components.
References

```
>>> oEditor.Delete

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import hfss
>>> hfss = Hfss()
>>> hfss.modeler["UDM"].delete()
>>> hfss.save_project()
>>> hfss._project_dictionary = None
>>> udc = hfss.modeler.user_defined_component_names

```
Copy to clipboard