---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_signal_layer.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# add_signal_layer 

Stackup3D.add_signal_layer(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_, _thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.035_, _fill_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'FR4_epoxy'_, _frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [Layer3D](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
Add a new ground layer to the stackup.
A signal layer is positive. The layer is entirely filled with the fill material. Anything will be drawn material. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Layer name. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Material name. Material will be parametrized. 

**thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Thickness value. Thickness will be parametrized. 

**fill_material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Fill Material name. Material will be parametrized.= 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material name. Material will be parametrized. Default value is “copper”. 

**thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Thickness value. Thickness will be parametrized. Default value is 0.035. 

**fill_material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Fill material name. Material will be parametrized. Default value is “FR4_epoxy”. 

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
>>> my_signal_layer = my_stackup.add_signal_layer("signal_layer")

```
Copy to clipboard
# add_signal_layer 

Stackup3D.add_signal_layer(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_, _thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.035_, _fill_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'FR4_epoxy'_, _frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [Layer3D](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
Add a new ground layer to the stackup.
A signal layer is positive. The layer is entirely filled with the fill material. Anything will be drawn material. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Layer name. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Material name. Material will be parametrized. 

**thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Thickness value. Thickness will be parametrized. 

**fill_material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Fill Material name. Material will be parametrized.= 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material name. Material will be parametrized. Default value is “copper”. 

**thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Thickness value. Thickness will be parametrized. Default value is 0.035. 

**fill_material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Fill material name. Material will be parametrized. Default value is “FR4_epoxy”. 

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
>>> my_signal_layer = my_stackup.add_signal_layer("signal_layer")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Stackup3D.add_signal_layer.rst.txt)

# add_signal_layer 

Stackup3D.add_signal_layer(_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_, _thickness : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = 0.035_, _fill_material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'FR4_epoxy'_, _frequency : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [Layer3D](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
Add a new ground layer to the stackup.
A signal layer is positive. The layer is entirely filled with the fill material. Anything will be drawn material. 

Parameters: 
     

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Layer name. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Material name. Material will be parametrized. 

**thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Thickness value. Thickness will be parametrized. 

**fill_material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Fill Material name. Material will be parametrized.= 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material name. Material will be parametrized. Default value is “copper”. 

**thickness**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Thickness value. Thickness will be parametrized. Default value is 0.035. 

**fill_material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Fill material name. Material will be parametrized. Default value is “FR4_epoxy”. 

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
>>> my_signal_layer = my_stackup.add_signal_layer("signal_layer")

```
Copy to clipboard