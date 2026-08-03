---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_polygon.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# add_polygon 

Layer3D.add_polygon(_points : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'copper'_, _is_void : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _poly_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [Polygon](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon") 
    
Create a polygon. 

Parameters: 
     

**points**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Points list of [x,y] coordinates. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material name. The default is `"copper"`. 

**is_void**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the polygon is a void. The default is `False`. On ground layers, it will act opposite of the Boolean value because the ground is negative. 

**poly_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Polygon name. The default is `None`. 

Returns: 
     

[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon")
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss()
>>> my_stackup = Stackup3D(hfss, 2.5e9)
>>> gnd = my_stackup.add_ground_layer("gnd")
>>> my_stackup.add_dielectric_layer("diel1", thickness=1.5, material="Duroid (tm)")
>>> top = my_stackup.add_signal_layer("top")
>>> my_polygon = top.add_polygon([[0, 0], [0, 1], [1, 1], [1, 0]])
>>> my_stackup.dielectric_x_position = "2mm"
>>> my_stackup.dielectric_y_position = "2mm"
>>> my_stackup.dielectric_length = "-3mm"
>>> my_stackup.dielectric_width = "-3mm"

```
Copy to clipboard
# add_polygon 

Layer3D.add_polygon(_points : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'copper'_, _is_void : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _poly_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [Polygon](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon") 
    
Create a polygon. 

Parameters: 
     

**points**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Points list of [x,y] coordinates. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material name. The default is `"copper"`. 

**is_void**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the polygon is a void. The default is `False`. On ground layers, it will act opposite of the Boolean value because the ground is negative. 

**poly_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Polygon name. The default is `None`. 

Returns: 
     

[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon")
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss()
>>> my_stackup = Stackup3D(hfss, 2.5e9)
>>> gnd = my_stackup.add_ground_layer("gnd")
>>> my_stackup.add_dielectric_layer("diel1", thickness=1.5, material="Duroid (tm)")
>>> top = my_stackup.add_signal_layer("top")
>>> my_polygon = top.add_polygon([[0, 0], [0, 1], [1, 1], [1, 0]])
>>> my_stackup.dielectric_x_position = "2mm"
>>> my_stackup.dielectric_y_position = "2mm"
>>> my_stackup.dielectric_length = "-3mm"
>>> my_stackup.dielectric_width = "-3mm"

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.add_polygon.rst.txt)

# add_polygon 

Layer3D.add_polygon(_points : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'copper'_, _is_void : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _poly_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [Polygon](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon") 
    
Create a polygon. 

Parameters: 
     

**points**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Points list of [x,y] coordinates. 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Material name. The default is `"copper"`. 

**is_void**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the polygon is a void. The default is `False`. On ground layers, it will act opposite of the Boolean value because the ground is negative. 

**poly_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Polygon name. The default is `None`. 

Returns: 
     

[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon")
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss()
>>> my_stackup = Stackup3D(hfss, 2.5e9)
>>> gnd = my_stackup.add_ground_layer("gnd")
>>> my_stackup.add_dielectric_layer("diel1", thickness=1.5, material="Duroid (tm)")
>>> top = my_stackup.add_signal_layer("top")
>>> my_polygon = top.add_polygon([[0, 0], [0, 1], [1, 1], [1, 0]])
>>> my_stackup.dielectric_x_position = "2mm"
>>> my_stackup.dielectric_y_position = "2mm"
>>> my_stackup.dielectric_length = "-3mm"
>>> my_stackup.dielectric_width = "-3mm"

```
Copy to clipboard