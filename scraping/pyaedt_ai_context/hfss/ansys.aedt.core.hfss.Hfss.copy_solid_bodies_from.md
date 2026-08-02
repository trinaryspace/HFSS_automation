---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.copy_solid_bodies_from.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# copy_solid_bodies_from 

Hfss.copy_solid_bodies_from(_design : [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _no_vacuum : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _no_pec : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _include_sheets : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Copy a list of objects and user defined models from one design to the active design.
If user defined models are selected, the project will be saved automatically. If the destination design is not the same application type, 3DComponents are not copied. 

Parameters: 
     

**design**
    
Starting application object. For example, `hfss1= HFSS3DLayout`. 

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of objects and user defined components to copy. The default is `None`. 

**no_vacuum**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to include vacuum objects for the copied objects. The default is `True`. 

**no_pec**
    
Whether to include pec objects for the copied objects. The default is `True`. 

**include_sheets**
    
Whether to include sheets for the copied objects. The default is `False`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.Copy
>>> oEditor.Paste

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss1 = Hfss(design="Design1")
>>> hfss2 = Hfss(design="Design2")
>>> hfss2.copy_solid_bodies_from(hfss1)

```
Copy to clipboard
# copy_solid_bodies_from 

Hfss.copy_solid_bodies_from(_design : [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _no_vacuum : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _no_pec : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _include_sheets : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Copy a list of objects and user defined models from one design to the active design.
If user defined models are selected, the project will be saved automatically. If the destination design is not the same application type, 3DComponents are not copied. 

Parameters: 
     

**design**
    
Starting application object. For example, `hfss1= HFSS3DLayout`. 

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of objects and user defined components to copy. The default is `None`. 

**no_vacuum**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to include vacuum objects for the copied objects. The default is `True`. 

**no_pec**
    
Whether to include pec objects for the copied objects. The default is `True`. 

**include_sheets**
    
Whether to include sheets for the copied objects. The default is `False`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.Copy
>>> oEditor.Paste

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss1 = Hfss(design="Design1")
>>> hfss2 = Hfss(design="Design2")
>>> hfss2.copy_solid_bodies_from(hfss1)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.copy_solid_bodies_from.rst.txt)

# copy_solid_bodies_from 

Hfss.copy_solid_bodies_from(_design : [object](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.mesh_icepak.Region.object.html#ansys.aedt.core.modules.mesh_icepak.Region.object "ansys.aedt.core.modules.mesh_icepak.Region.object")_, _assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _no_vacuum : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _no_pec : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _include_sheets : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Copy a list of objects and user defined models from one design to the active design.
If user defined models are selected, the project will be saved automatically. If the destination design is not the same application type, 3DComponents are not copied. 

Parameters: 
     

**design**
    
Starting application object. For example, `hfss1= HFSS3DLayout`. 

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of objects and user defined components to copy. The default is `None`. 

**no_vacuum**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to include vacuum objects for the copied objects. The default is `True`. 

**no_pec**
    
Whether to include pec objects for the copied objects. The default is `True`. 

**include_sheets**
    
Whether to include sheets for the copied objects. The default is `False`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oEditor.Copy
>>> oEditor.Paste

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss1 = Hfss(design="Design1")
>>> hfss2 = Hfss(design="Design2")
>>> hfss2.copy_solid_bodies_from(hfss1)

```
Copy to clipboard