---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.update.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# update 

Setup.update(_properties : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Update the setup based on either the class argument or a dictionary. 

Parameters: 
     

**properties**`optional` 
    
Dictionary to use to update the setup. The default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.EditSetup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> setup = app.create_setup()
>>> setup.update(properties={"Name": "Value"})

```
Copy to clipboard
# update 

Setup.update(_properties : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Update the setup based on either the class argument or a dictionary. 

Parameters: 
     

**properties**`optional` 
    
Dictionary to use to update the setup. The default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.EditSetup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> setup = app.create_setup()
>>> setup.update(properties={"Name": "Value"})

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.solve_setup.Setup.update.rst.txt)

# update 

Setup.update(_properties : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Update the setup based on either the class argument or a dictionary. 

Parameters: 
     

**properties**`optional` 
    
Dictionary to use to update the setup. The default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oModule.EditSetup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> app = Hfss()
>>> setup = app.create_setup()
>>> setup.update(properties={"Name": "Value"})

```
Copy to clipboard