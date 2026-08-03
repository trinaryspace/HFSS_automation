---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_dielectric_layer.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# add_dielectric_layer 

Stackup3D.add_dielectric_layer(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'FR4_epoxy'_, _thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.035_, _frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [Layer3D](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
Add a new dielectric layer to the stackup. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Layer name. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Material name. The default is `"FR4_epoxy"`. The material will be parametrized. 

**thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Thickness value. The default is `0.035`. The thickness will be parametrized. 

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
>>> my_dielectric_layer = my_stackup.add_dielectric_layer("diel", thickness=1.5, material="Duroid (tm)")

```
Copy to clipboard
# add_dielectric_layer 

Stackup3D.add_dielectric_layer(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'FR4_epoxy'_, _thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.035_, _frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [Layer3D](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
Add a new dielectric layer to the stackup. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Layer name. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Material name. The default is `"FR4_epoxy"`. The material will be parametrized. 

**thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Thickness value. The default is `0.035`. The thickness will be parametrized. 

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
>>> my_dielectric_layer = my_stackup.add_dielectric_layer("diel", thickness=1.5, material="Duroid (tm)")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_dielectric_layer.rst.txt)

# add_dielectric_layer 

Stackup3D.add_dielectric_layer(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'FR4_epoxy'_, _thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.035_, _frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [Layer3D](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
Add a new dielectric layer to the stackup. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Layer name. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Material name. The default is `"FR4_epoxy"`. The material will be parametrized. 

**thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Thickness value. The default is `0.035`. The thickness will be parametrized. 

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
>>> my_dielectric_layer = my_stackup.add_dielectric_layer("diel", thickness=1.5, material="Duroid (tm)")

```
Copy to clipboard