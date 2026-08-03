---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# Layer3D 

class ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D(_stackup_ , _app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _layer_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'S'_, _material_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_, _thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.035_, _fill_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'FR4_epoxy'_, _index : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _frequency =None_) 
    
Provides a class for a management of a parametric layer in 3D Modeler.
The Layer3D class is not intended to be used with its constructor, but by using the method “add_layer” available in the Stackup3D class. 

Parameters: 
     

**stackup**[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D") 
    
The stackup where the layers will be added. 

**app**[`ansys.aedt.core.hfss.Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss") 
    
HFSS design or project where the variable is to be created. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the layer. 

**layer_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
“S” for signal layers, “D” for dielectric layers, “G” for ground layers. 

**material_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
The material name of the layer. 

**thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The thickness of the layer. 

**fill_material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
In ground and signal layers, the dielectric material name which will fill the non-conductive areas of the layer. 

**index**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
The number of the layer, starting from bottom to top. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The layer frequency, it will be common to all geometric shapes on the layer.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss()
>>> my_stackup = Stackup3D(hfss, 2.5e9)
>>> my_layer = my_stackup.add_layer("my_layer")
>>> gnd = my_stackup.add_ground_layer("gnd")
>>> diel = my_stackup.add_dielectric_layer("diel1", thickness=1.5, material="Duroid (tm)")
>>> top = my_stackup.add_signal_layer("top")

```
Copy to clipboard
Methods  
| [`Layer3D.add_patch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_patch.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_patch "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_patch")(frequency, patch_width[, ...])  | Create a parametric patch.  |  
| --- | --- |  
| [`Layer3D.add_polygon`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_polygon.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_polygon "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_polygon")(points[, material, ...])  | Create a polygon.  |  
| [`Layer3D.add_trace`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_trace.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_trace "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_trace")(line_width, line_length[, ...])  | Create a trace.  |  
| [`Layer3D.duplicate_parametrize_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.duplicate_parametrize_material.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.duplicate_parametrize_material "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.duplicate_parametrize_material")(...)  | Duplicate a material and parametrize all properties.  |  
Attributes  
| [`Layer3D.duplicated_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.duplicated_material.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.duplicated_material "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.duplicated_material")  | Duplicated material.  |  
| --- | --- |  
| [`Layer3D.elevation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.elevation.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.elevation "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.elevation")  | Layer elevation.  |  
| [`Layer3D.elevation_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.elevation_value.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.elevation_value "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.elevation_value")  | Layer elevation value.  |  
| [`Layer3D.filling_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.filling_material.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.filling_material "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.filling_material")  | Fill material.  |  
| [`Layer3D.filling_material_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.filling_material_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.filling_material_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.filling_material_name")  | Fill material name.  |  
| [`Layer3D.frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.frequency.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.frequency "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.frequency")  | Frequency variable.  |  
| [`Layer3D.material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.material.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.material "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.material")  | Material.  |  
| [`Layer3D.material_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.material_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.material_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.material_name")  | Material name.  |  
| [`Layer3D.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.name")  | Layer name.  |  
| [`Layer3D.number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.number.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.number "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.number")  | Layer ID.  |  
| [`Layer3D.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.public_dir.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.public_dir "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.public_dir")  | Shortcut for dir(self).  |  
| [`Layer3D.stackup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.stackup.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.stackup "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.stackup")  | Stackup.  |  
| [`Layer3D.thickness`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.thickness.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.thickness "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.thickness")  | Thickness variable.  |  
| [`Layer3D.thickness_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.thickness_value.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.thickness_value "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.thickness_value")  | Thickness value.  |  
| [`Layer3D.type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.type.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.type "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.type")  | Layer type.  |  
# Layer3D 

class ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D(_stackup_ , _app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _layer_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'S'_, _material_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_, _thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.035_, _fill_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'FR4_epoxy'_, _index : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _frequency =None_) 
    
Provides a class for a management of a parametric layer in 3D Modeler.
The Layer3D class is not intended to be used with its constructor, but by using the method “add_layer” available in the Stackup3D class. 

Parameters: 
     

**stackup**[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D") 
    
The stackup where the layers will be added. 

**app**[`ansys.aedt.core.hfss.Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss") 
    
HFSS design or project where the variable is to be created. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the layer. 

**layer_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
“S” for signal layers, “D” for dielectric layers, “G” for ground layers. 

**material_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
The material name of the layer. 

**thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The thickness of the layer. 

**fill_material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
In ground and signal layers, the dielectric material name which will fill the non-conductive areas of the layer. 

**index**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
The number of the layer, starting from bottom to top. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The layer frequency, it will be common to all geometric shapes on the layer.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss()
>>> my_stackup = Stackup3D(hfss, 2.5e9)
>>> my_layer = my_stackup.add_layer("my_layer")
>>> gnd = my_stackup.add_ground_layer("gnd")
>>> diel = my_stackup.add_dielectric_layer("diel1", thickness=1.5, material="Duroid (tm)")
>>> top = my_stackup.add_signal_layer("top")

```
Copy to clipboard
Methods  
| [`Layer3D.add_patch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_patch.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_patch "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_patch")(frequency, patch_width[, ...])  | Create a parametric patch.  |  
| --- | --- |  
| [`Layer3D.add_polygon`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_polygon.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_polygon "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_polygon")(points[, material, ...])  | Create a polygon.  |  
| [`Layer3D.add_trace`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_trace.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_trace "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_trace")(line_width, line_length[, ...])  | Create a trace.  |  
| [`Layer3D.duplicate_parametrize_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.duplicate_parametrize_material.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.duplicate_parametrize_material "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.duplicate_parametrize_material")(...)  | Duplicate a material and parametrize all properties.  |  
Attributes  
| [`Layer3D.duplicated_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.duplicated_material.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.duplicated_material "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.duplicated_material")  | Duplicated material.  |  
| --- | --- |  
| [`Layer3D.elevation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.elevation.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.elevation "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.elevation")  | Layer elevation.  |  
| [`Layer3D.elevation_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.elevation_value.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.elevation_value "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.elevation_value")  | Layer elevation value.  |  
| [`Layer3D.filling_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.filling_material.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.filling_material "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.filling_material")  | Fill material.  |  
| [`Layer3D.filling_material_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.filling_material_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.filling_material_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.filling_material_name")  | Fill material name.  |  
| [`Layer3D.frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.frequency.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.frequency "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.frequency")  | Frequency variable.  |  
| [`Layer3D.material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.material.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.material "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.material")  | Material.  |  
| [`Layer3D.material_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.material_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.material_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.material_name")  | Material name.  |  
| [`Layer3D.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.name")  | Layer name.  |  
| [`Layer3D.number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.number.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.number "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.number")  | Layer ID.  |  
| [`Layer3D.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.public_dir.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.public_dir "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.public_dir")  | Shortcut for dir(self).  |  
| [`Layer3D.stackup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.stackup.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.stackup "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.stackup")  | Stackup.  |  
| [`Layer3D.thickness`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.thickness.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.thickness "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.thickness")  | Thickness variable.  |  
| [`Layer3D.thickness_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.thickness_value.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.thickness_value "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.thickness_value")  | Thickness value.  |  
| [`Layer3D.type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.type.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.type "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.type")  | Layer type.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.rst.txt)

# Layer3D 

class ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D(_stackup_ , _app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _layer_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'S'_, _material_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_, _thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.035_, _fill_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'FR4_epoxy'_, _index : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _frequency =None_) 
    
Provides a class for a management of a parametric layer in 3D Modeler.
The Layer3D class is not intended to be used with its constructor, but by using the method “add_layer” available in the Stackup3D class. 

Parameters: 
     

**stackup**[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D") 
    
The stackup where the layers will be added. 

**app**[`ansys.aedt.core.hfss.Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss") 
    
HFSS design or project where the variable is to be created. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the layer. 

**layer_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
“S” for signal layers, “D” for dielectric layers, “G” for ground layers. 

**material_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
The material name of the layer. 

**thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The thickness of the layer. 

**fill_material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
In ground and signal layers, the dielectric material name which will fill the non-conductive areas of the layer. 

**index**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
The number of the layer, starting from bottom to top. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
The layer frequency, it will be common to all geometric shapes on the layer.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss()
>>> my_stackup = Stackup3D(hfss, 2.5e9)
>>> my_layer = my_stackup.add_layer("my_layer")
>>> gnd = my_stackup.add_ground_layer("gnd")
>>> diel = my_stackup.add_dielectric_layer("diel1", thickness=1.5, material="Duroid (tm)")
>>> top = my_stackup.add_signal_layer("top")

```
Copy to clipboard
Methods  
| [`Layer3D.add_patch`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_patch.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_patch "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_patch")(frequency, patch_width[, ...])  | Create a parametric patch.  |  
| --- | --- |  
| [`Layer3D.add_polygon`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_polygon.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_polygon "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_polygon")(points[, material, ...])  | Create a polygon.  |  
| [`Layer3D.add_trace`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_trace.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_trace "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_trace")(line_width, line_length[, ...])  | Create a trace.  |  
| [`Layer3D.duplicate_parametrize_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.duplicate_parametrize_material.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.duplicate_parametrize_material "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.duplicate_parametrize_material")(...)  | Duplicate a material and parametrize all properties.  |  
Attributes  
| [`Layer3D.duplicated_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.duplicated_material.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.duplicated_material "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.duplicated_material")  | Duplicated material.  |  
| --- | --- |  
| [`Layer3D.elevation`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.elevation.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.elevation "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.elevation")  | Layer elevation.  |  
| [`Layer3D.elevation_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.elevation_value.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.elevation_value "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.elevation_value")  | Layer elevation value.  |  
| [`Layer3D.filling_material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.filling_material.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.filling_material "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.filling_material")  | Fill material.  |  
| [`Layer3D.filling_material_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.filling_material_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.filling_material_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.filling_material_name")  | Fill material name.  |  
| [`Layer3D.frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.frequency.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.frequency "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.frequency")  | Frequency variable.  |  
| [`Layer3D.material`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.material.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.material "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.material")  | Material.  |  
| [`Layer3D.material_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.material_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.material_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.material_name")  | Material name.  |  
| [`Layer3D.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.name")  | Layer name.  |  
| [`Layer3D.number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.number.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.number "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.number")  | Layer ID.  |  
| [`Layer3D.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.public_dir.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.public_dir "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.public_dir")  | Shortcut for dir(self).  |  
| [`Layer3D.stackup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.stackup.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.stackup "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.stackup")  | Stackup.  |  
| [`Layer3D.thickness`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.thickness.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.thickness "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.thickness")  | Thickness variable.  |  
| [`Layer3D.thickness_value`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.thickness_value.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.thickness_value "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.thickness_value")  | Thickness value.  |  
| [`Layer3D.type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.type.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.type "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.type")  | Layer type.  |