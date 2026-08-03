---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.import_materials_from_workbench.html"
category: "materials"
domain: "PyAEDT / HFSS"
---

# import_materials_from_workbench 

Materials.import_materials_from_workbench(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _name_suffix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[Material](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material")] | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Import and create materials from Workbench Engineering Data XML file. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path and name for the XML file. 

**name_suffix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)"), `optional` 
    
String containing the suffix to be applied to the imported material names. The default is `None`, in which case “_wb” is used. Set it to `""` to maintain in AEDT the same name as in Workbench. 

Returns: 
     

`List` `of` [`ansys.aedt.core.modules.material.Material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material") 
    
Examples

```
>>> from ansys.aedt.core.modules.material_lib import Materials
>>> obj = Materials()
>>> obj.import_materials_from_workbench(input_file="example.txt")

```
Copy to clipboard
# import_materials_from_workbench 

Materials.import_materials_from_workbench(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _name_suffix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[Material](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material")] | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Import and create materials from Workbench Engineering Data XML file. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path and name for the XML file. 

**name_suffix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)"), `optional` 
    
String containing the suffix to be applied to the imported material names. The default is `None`, in which case “_wb” is used. Set it to `""` to maintain in AEDT the same name as in Workbench. 

Returns: 
     

`List` `of` [`ansys.aedt.core.modules.material.Material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material") 
    
Examples

```
>>> from ansys.aedt.core.modules.material_lib import Materials
>>> obj = Materials()
>>> obj.import_materials_from_workbench(input_file="example.txt")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.material_lib.Materials.import_materials_from_workbench.rst.txt)

# import_materials_from_workbench 

Materials.import_materials_from_workbench(_input_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _name_suffix : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[Material](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material")] | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Import and create materials from Workbench Engineering Data XML file. 

Parameters: 
     

**input_file**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Full path and name for the XML file. 

**name_suffix**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)"), `optional` 
    
String containing the suffix to be applied to the imported material names. The default is `None`, in which case “_wb” is used. Set it to `""` to maintain in AEDT the same name as in Workbench. 

Returns: 
     

`List` `of` [`ansys.aedt.core.modules.material.Material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.html#ansys.aedt.core.modules.material.Material "ansys.aedt.core.modules.material.Material") 
    
Examples

```
>>> from ansys.aedt.core.modules.material_lib import Materials
>>> obj = Materials()
>>> obj.import_materials_from_workbench(input_file="example.txt")

```
Copy to clipboard