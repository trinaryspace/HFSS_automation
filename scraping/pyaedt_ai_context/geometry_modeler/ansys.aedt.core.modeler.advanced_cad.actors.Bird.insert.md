---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.insert.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# insert 

Bird.insert(_app : [Hfss](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss")_, _motion : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Insert the bird in HFSS SBR+. 

Parameters: 
     

**app**`Hfss` 
     

**motion**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether the bird is in motion. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> import ansys.aedt.core as pyaedt
>>> from ansys.aedt.core.modeler.advanced_cad.actors import Bird
>>> hfss = pyaedt.Hfss()
>>> bird = Bird(r"C:\temp\actors\bird")
>>> bird.insert(app=hfss)

```
Copy to clipboard
# insert 

Bird.insert(_app : [Hfss](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss")_, _motion : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Insert the bird in HFSS SBR+. 

Parameters: 
     

**app**`Hfss` 
     

**motion**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether the bird is in motion. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> import ansys.aedt.core as pyaedt
>>> from ansys.aedt.core.modeler.advanced_cad.actors import Bird
>>> hfss = pyaedt.Hfss()
>>> bird = Bird(r"C:\temp\actors\bird")
>>> bird.insert(app=hfss)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Bird.insert.rst.txt)

# insert 

Bird.insert(_app : [Hfss](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss")_, _motion : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Insert the bird in HFSS SBR+. 

Parameters: 
     

**app**`Hfss` 
     

**motion**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Whether the bird is in motion. The default is `True`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
Examples

```
>>> import ansys.aedt.core as pyaedt
>>> from ansys.aedt.core.modeler.advanced_cad.actors import Bird
>>> hfss = pyaedt.Hfss()
>>> bird = Bird(r"C:\temp\actors\bird")
>>> bird.insert(app=hfss)

```
Copy to clipboard