---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_layer.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# add_layer 

Stackup3D.add_layer(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _layer_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'S'_, _material_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_, _thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.035_, _fill_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'FR4_epoxy'_, _frequency =None_) → [Layer3D](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
Add a new layer to the stackup.
The new layer can be a signal (S), ground (G), or dielectric (D). The layer is entirely filled with the specified fill material. Anything will be drawn material. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Layer name. 

**layer_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Layer type. The default is `"S"`. Options are:
>   * `"D"` for “dielectric” layer
>   * `"G"` for “ground” layer
>   * `"S"` for “signal” layer
> 

**material_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material name. The default is `"copper"`. The material is parametrized. 

**thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Thickness value. The default is `0.035`. The thickness will be parametrized. 

**fill_material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Fill material name. The default is `"FR4_epoxy"`. The fill material will be parametrized. This parameter is not valid for dielectrics. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
The layer frequency, it will be common to all geometric shapes on the layer. The default is None, so each shape must have their own frequency. 

Returns: 
     

[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D")
    
Layer object.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss()
>>> my_stackup = Stackup3D(hfss, 2.5e9)
>>> my_layer = my_stackup.add_layer("my_layer")

```
Copy to clipboard
# add_layer 

Stackup3D.add_layer(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _layer_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'S'_, _material_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_, _thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.035_, _fill_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'FR4_epoxy'_, _frequency =None_) → [Layer3D](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
Add a new layer to the stackup.
The new layer can be a signal (S), ground (G), or dielectric (D). The layer is entirely filled with the specified fill material. Anything will be drawn material. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Layer name. 

**layer_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Layer type. The default is `"S"`. Options are:
>   * `"D"` for “dielectric” layer
>   * `"G"` for “ground” layer
>   * `"S"` for “signal” layer
> 

**material_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material name. The default is `"copper"`. The material is parametrized. 

**thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Thickness value. The default is `0.035`. The thickness will be parametrized. 

**fill_material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Fill material name. The default is `"FR4_epoxy"`. The fill material will be parametrized. This parameter is not valid for dielectrics. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
The layer frequency, it will be common to all geometric shapes on the layer. The default is None, so each shape must have their own frequency. 

Returns: 
     

[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D")
    
Layer object.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss()
>>> my_stackup = Stackup3D(hfss, 2.5e9)
>>> my_layer = my_stackup.add_layer("my_layer")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_layer.rst.txt)

# add_layer 

Stackup3D.add_layer(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _layer_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'S'_, _material_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_, _thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.035_, _fill_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'FR4_epoxy'_, _frequency =None_) → [Layer3D](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
Add a new layer to the stackup.
The new layer can be a signal (S), ground (G), or dielectric (D). The layer is entirely filled with the specified fill material. Anything will be drawn material. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Layer name. 

**layer_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Layer type. The default is `"S"`. Options are:
>   * `"D"` for “dielectric” layer
>   * `"G"` for “ground” layer
>   * `"S"` for “signal” layer
> 

**material_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material name. The default is `"copper"`. The material is parametrized. 

**thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Thickness value. The default is `0.035`. The thickness will be parametrized. 

**fill_material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Fill material name. The default is `"FR4_epoxy"`. The fill material will be parametrized. This parameter is not valid for dielectrics. 

**frequency**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
The layer frequency, it will be common to all geometric shapes on the layer. The default is None, so each shape must have their own frequency. 

Returns: 
     

[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D")
    
Layer object.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss()
>>> my_stackup = Stackup3D(hfss, 2.5e9)
>>> my_layer = my_stackup.add_layer("my_layer")

```
Copy to clipboard