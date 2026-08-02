---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.set_mesh_fusion_settings.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# set_mesh_fusion_settings 

Hfss.set_mesh_fusion_settings(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _volume_padding : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _priority : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set mesh fusion settings in HFSS. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of active 3D Components. The default is `None`, in which case components are disabled. 

**volume_padding**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of mesh envelope padding, the format is `[+x, -x, +y, -y, +z, -z]`. The default is `None`, in which case all zeros are applied. 

**priority**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of components with the priority flag enabled. The default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.SetDoMeshAssembly

```
Copy to clipboard
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Hfss()
>>> app.set_mesh_fusion_settings(assignment=["Comp1", "Comp2"],
>>>                              volume_padding=[[0,0,0,0,0,0], [0,0,5,0,0,0]],priority=["Comp1"])

```
Copy to clipboard
# set_mesh_fusion_settings 

Hfss.set_mesh_fusion_settings(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _volume_padding : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _priority : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set mesh fusion settings in HFSS. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of active 3D Components. The default is `None`, in which case components are disabled. 

**volume_padding**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of mesh envelope padding, the format is `[+x, -x, +y, -y, +z, -z]`. The default is `None`, in which case all zeros are applied. 

**priority**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of components with the priority flag enabled. The default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.SetDoMeshAssembly

```
Copy to clipboard
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Hfss()
>>> app.set_mesh_fusion_settings(assignment=["Comp1", "Comp2"],
>>>                              volume_padding=[[0,0,0,0,0,0], [0,0,5,0,0,0]],priority=["Comp1"])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.set_mesh_fusion_settings.rst.txt)

# set_mesh_fusion_settings 

Hfss.set_mesh_fusion_settings(_assignment : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _volume_padding : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _priority : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set mesh fusion settings in HFSS. 

Parameters: 
     

**assignment**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of active 3D Components. The default is `None`, in which case components are disabled. 

**volume_padding**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of mesh envelope padding, the format is `[+x, -x, +y, -y, +z, -z]`. The default is `None`, in which case all zeros are applied. 

**priority**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
List of components with the priority flag enabled. The default is `None`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDesign.SetDoMeshAssembly

```
Copy to clipboard
Examples

```
>>> import ansys.aedt.core
>>> app = ansys.aedt.core.Hfss()
>>> app.set_mesh_fusion_settings(assignment=["Comp1", "Comp2"],
>>>                              volume_padding=[[0,0,0,0,0,0], [0,0,5,0,0,0]],priority=["Comp1"])

```
Copy to clipboard