---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.import_nastran.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# import_nastran 

Modeler3D.import_nastran(_file_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _import_lines : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _lines_thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0_, _import_as_light_weight : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _decimation : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0_, _group_parts : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _enable_planar_merge : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'True'_, _save_only_stl : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _preview : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _merge_angle : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.001_, _remove_multiple_connections : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")['Object3d'], [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")] | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")], [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")] 
    
Import Nastran file into 3D Modeler by converting the faces to stl and reading it.
The solids are translated directly to AEDT format. 

Parameters: 
     

**file_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to .nas file. 

**import_lines**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to import the lines or only triangles. Default is `True`. 

**lines_thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Whether to thicken lines after creation and it’s default value. Every line will be parametrized with a design variable called `xsection_linename`. 

**import_as_light_weight**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Import the stl generatated as light weight. It works only on SBR+ and HFSS Regions. Default is `False`. 

**decimation**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Fraction of the original mesh to remove before creating the stl file. If set to `0.9`, this function tries to reduce the data set to 10% of its original size and removes 90% of the input triangles. 

**group_parts**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to group imported parts by object ID. The default is `True`. 

**enable_planar_merge**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to enable or not planar merge. It can be `"True"`, `"False"` or `"Auto"`. `"Auto"` will disable the planar merge if stl contains more than 50000 triangles. 

**save_only_stl**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to import the model in HFSS or only generate the stl file. 

**preview**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to preview the model in pyvista or skip it. 

**merge_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Angle in radians for which faces will be considered planar. Default is `1e-3`. 

**remove_multiple_connections**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to remove multiple connections in the mesh. Default is `False`. 

Returns: 
     

`List` `of` [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
New object created and nastran dictionary.
Examples

```
>>> from ansys.aedt.core.modeler.modeler_3d import Modeler3D
>>> obj = Modeler3D()
>>> obj.import_nastran(file_path="example.txt")

```
Copy to clipboard
# import_nastran 

Modeler3D.import_nastran(_file_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _import_lines : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _lines_thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0_, _import_as_light_weight : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _decimation : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0_, _group_parts : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _enable_planar_merge : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'True'_, _save_only_stl : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _preview : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _merge_angle : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.001_, _remove_multiple_connections : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")['Object3d'], [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")] | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")], [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")] 
    
Import Nastran file into 3D Modeler by converting the faces to stl and reading it.
The solids are translated directly to AEDT format. 

Parameters: 
     

**file_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to .nas file. 

**import_lines**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to import the lines or only triangles. Default is `True`. 

**lines_thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Whether to thicken lines after creation and it’s default value. Every line will be parametrized with a design variable called `xsection_linename`. 

**import_as_light_weight**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Import the stl generatated as light weight. It works only on SBR+ and HFSS Regions. Default is `False`. 

**decimation**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Fraction of the original mesh to remove before creating the stl file. If set to `0.9`, this function tries to reduce the data set to 10% of its original size and removes 90% of the input triangles. 

**group_parts**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to group imported parts by object ID. The default is `True`. 

**enable_planar_merge**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to enable or not planar merge. It can be `"True"`, `"False"` or `"Auto"`. `"Auto"` will disable the planar merge if stl contains more than 50000 triangles. 

**save_only_stl**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to import the model in HFSS or only generate the stl file. 

**preview**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to preview the model in pyvista or skip it. 

**merge_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Angle in radians for which faces will be considered planar. Default is `1e-3`. 

**remove_multiple_connections**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to remove multiple connections in the mesh. Default is `False`. 

Returns: 
     

`List` `of` [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
New object created and nastran dictionary.
Examples

```
>>> from ansys.aedt.core.modeler.modeler_3d import Modeler3D
>>> obj = Modeler3D()
>>> obj.import_nastran(file_path="example.txt")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.import_nastran.rst.txt)

# import_nastran 

Modeler3D.import_nastran(_file_path : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _import_lines : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _lines_thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0_, _import_as_light_weight : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _decimation : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0_, _group_parts : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _enable_planar_merge : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'True'_, _save_only_stl : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _preview : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _merge_angle : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.001_, _remove_multiple_connections : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")['Object3d'], [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")] | [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")], [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")] 
    
Import Nastran file into 3D Modeler by converting the faces to stl and reading it.
The solids are translated directly to AEDT format. 

Parameters: 
     

**file_path**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Path to .nas file. 

**import_lines**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to import the lines or only triangles. Default is `True`. 

**lines_thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Whether to thicken lines after creation and it’s default value. Every line will be parametrized with a design variable called `xsection_linename`. 

**import_as_light_weight**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Import the stl generatated as light weight. It works only on SBR+ and HFSS Regions. Default is `False`. 

**decimation**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Fraction of the original mesh to remove before creating the stl file. If set to `0.9`, this function tries to reduce the data set to 10% of its original size and removes 90% of the input triangles. 

**group_parts**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to group imported parts by object ID. The default is `True`. 

**enable_planar_merge**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Whether to enable or not planar merge. It can be `"True"`, `"False"` or `"Auto"`. `"Auto"` will disable the planar merge if stl contains more than 50000 triangles. 

**save_only_stl**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to import the model in HFSS or only generate the stl file. 

**preview**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to preview the model in pyvista or skip it. 

**merge_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Angle in radians for which faces will be considered planar. Default is `1e-3`. 

**remove_multiple_connections**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to remove multiple connections in the mesh. Default is `False`. 

Returns: 
     

`List` `of` [`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d"), [`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
New object created and nastran dictionary.
Examples

```
>>> from ansys.aedt.core.modeler.modeler_3d import Modeler3D
>>> obj = Modeler3D()
>>> obj.import_nastran(file_path="example.txt")

```
Copy to clipboard