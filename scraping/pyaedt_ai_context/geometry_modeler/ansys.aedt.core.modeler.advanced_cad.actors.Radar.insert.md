---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.insert.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# insert 

Radar.insert(_app : [Hfss](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss")_, _motion : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Insert radar in the HFSS application instance. 

Parameters: 
     

**app**`Hfss` 
     

**motion**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the actor is in motion. The default is `False`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of antennae that have been placed.
Examples

```
>>> import ansys.aedt.core as pyaedt
>>> from ansys.aedt.core.modeler.advanced_cad.actors import Radar
>>> hfss = pyaedt.Hfss()
>>> radar = Radar(r"C:\temp\actors\radar")
>>> radar.insert(app=hfss)

```
Copy to clipboard
# insert 

Radar.insert(_app : [Hfss](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss")_, _motion : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Insert radar in the HFSS application instance. 

Parameters: 
     

**app**`Hfss` 
     

**motion**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the actor is in motion. The default is `False`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of antennae that have been placed.
Examples

```
>>> import ansys.aedt.core as pyaedt
>>> from ansys.aedt.core.modeler.advanced_cad.actors import Radar
>>> hfss = pyaedt.Hfss()
>>> radar = Radar(r"C:\temp\actors\radar")
>>> radar.insert(app=hfss)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.insert.rst.txt)

# insert 

Radar.insert(_app : [Hfss](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss")_, _motion : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Insert radar in the HFSS application instance. 

Parameters: 
     

**app**`Hfss` 
     

**motion**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the actor is in motion. The default is `False`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of antennae that have been placed.
Examples

```
>>> import ansys.aedt.core as pyaedt
>>> from ansys.aedt.core.modeler.advanced_cad.actors import Radar
>>> hfss = pyaedt.Hfss()
>>> radar = Radar(r"C:\temp\actors\radar")
>>> radar.insert(app=hfss)

```
Copy to clipboard