---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.insert.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# insert 

Person.insert(_app : [Hfss](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss")_, _motion : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Insert the person in HFSS SBR+. 

Parameters: 
     

**app**`Hfss` 
    
HFSS application instance. 

**motion**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the person is in motion. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> import ansys.aedt.core as pyaedt
>>> from ansys.aedt.core.modeler.advanced_cad.actors import Person
>>> hfss = pyaedt.Hfss()
>>> person = Person(r"C:\temp\actors\person")
>>> person.insert(app=hfss)

```
Copy to clipboard
# insert 

Person.insert(_app : [Hfss](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss")_, _motion : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Insert the person in HFSS SBR+. 

Parameters: 
     

**app**`Hfss` 
    
HFSS application instance. 

**motion**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the person is in motion. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> import ansys.aedt.core as pyaedt
>>> from ansys.aedt.core.modeler.advanced_cad.actors import Person
>>> hfss = pyaedt.Hfss()
>>> person = Person(r"C:\temp\actors\person")
>>> person.insert(app=hfss)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Person.insert.rst.txt)

# insert 

Person.insert(_app : [Hfss](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss")_, _motion : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Insert the person in HFSS SBR+. 

Parameters: 
     

**app**`Hfss` 
    
HFSS application instance. 

**motion**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the person is in motion. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> import ansys.aedt.core as pyaedt
>>> from ansys.aedt.core.modeler.advanced_cad.actors import Person
>>> hfss = pyaedt.Hfss()
>>> person = Person(r"C:\temp\actors\person")
>>> person.insert(app=hfss)

```
Copy to clipboard