---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# Polygon 

class ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon(_application_ , _point_list_ , _signal_layer_ , _poly_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'poly'_, _mat_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_, _is_void : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _reference_system =None_) 
    
Polygon Class in Stackup3D. It is preferable to use the add_polygon method in the class Layer3D than directly the class constructor. 

Parameters: 
     

**application**[`ansys.aedt.core.hfss.Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss") 
    
HFSS design or project where the variable is to be created. 

**point_list**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Points list of [x,y] coordinates. 

**signal_layer**[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
The signal layer where the line will be drawn. 

**poly_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Polygon name. The default is `poly`. 

**mat_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The polygon material name. 

**is_void**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the polygon is a void. The default is `False`. On ground layers, it will act opposite of the Boolean value because the ground is negative. 

**reference_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)"), `optional` 
    
Coordinate system of the polygon. By default, None.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss(new_desktop=True)
>>> my_stackup = Stackup3D(hfss, 2.5e9)
>>> gnd = my_stackup.add_ground_layer("gnd", thickness=None)
>>> my_stackup.add_dielectric_layer("diel1", thickness=1.5, material="Duroid (tm)")
>>> top = my_stackup.add_signal_layer("top", thickness=None)
>>> my_polygon = top.add_polygon([[0, 0], [0, 1], [1, 1], [1, 0]])
>>> my_stackup.dielectric_x_position = "2mm"
>>> my_stackup.dielectric_y_position = "2mm"
>>> my_stackup.dielectric_length = "-3mm"
>>> my_stackup.dielectric_width = "-3mm"

```
Copy to clipboard
Attributes  
| [`Polygon.aedt_object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.aedt_object.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.aedt_object "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.aedt_object")  | PyAEDT object 3D.  |  
| --- | --- |  
| [`Polygon.application`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.application.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.application "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.application")  | App object.  |  
| [`Polygon.dielectric_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.dielectric_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.dielectric_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.dielectric_layer")  | Dielectric layer that the object belongs to.  |  
| [`Polygon.layer_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.layer_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.layer_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.layer_name")  | Layer name.  |  
| [`Polygon.layer_number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.layer_number.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.layer_number "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.layer_number")  | Layer ID.  |  
| [`Polygon.material_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.material_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.material_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.material_name")  | Material name.  |  
| [`Polygon.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.name")  | Object name.  |  
| [`Polygon.points_on_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.points_on_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.points_on_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.points_on_layer")  | Object Bounding Box.  |  
| [`Polygon.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.public_dir.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.public_dir "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.public_dir")  | Shortcut for dir(self).  |  
| [`Polygon.reference_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.reference_system.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.reference_system "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.reference_system")  | Coordinate system of the object.  |  
| [`Polygon.signal_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.signal_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.signal_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.signal_layer")  | Signal layer that the object belongs to.  |  
# Polygon 

class ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon(_application_ , _point_list_ , _signal_layer_ , _poly_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'poly'_, _mat_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_, _is_void : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _reference_system =None_) 
    
Polygon Class in Stackup3D. It is preferable to use the add_polygon method in the class Layer3D than directly the class constructor. 

Parameters: 
     

**application**[`ansys.aedt.core.hfss.Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss") 
    
HFSS design or project where the variable is to be created. 

**point_list**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Points list of [x,y] coordinates. 

**signal_layer**[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
The signal layer where the line will be drawn. 

**poly_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Polygon name. The default is `poly`. 

**mat_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The polygon material name. 

**is_void**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the polygon is a void. The default is `False`. On ground layers, it will act opposite of the Boolean value because the ground is negative. 

**reference_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)"), `optional` 
    
Coordinate system of the polygon. By default, None.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss(new_desktop=True)
>>> my_stackup = Stackup3D(hfss, 2.5e9)
>>> gnd = my_stackup.add_ground_layer("gnd", thickness=None)
>>> my_stackup.add_dielectric_layer("diel1", thickness=1.5, material="Duroid (tm)")
>>> top = my_stackup.add_signal_layer("top", thickness=None)
>>> my_polygon = top.add_polygon([[0, 0], [0, 1], [1, 1], [1, 0]])
>>> my_stackup.dielectric_x_position = "2mm"
>>> my_stackup.dielectric_y_position = "2mm"
>>> my_stackup.dielectric_length = "-3mm"
>>> my_stackup.dielectric_width = "-3mm"

```
Copy to clipboard
Attributes  
| [`Polygon.aedt_object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.aedt_object.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.aedt_object "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.aedt_object")  | PyAEDT object 3D.  |  
| --- | --- |  
| [`Polygon.application`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.application.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.application "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.application")  | App object.  |  
| [`Polygon.dielectric_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.dielectric_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.dielectric_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.dielectric_layer")  | Dielectric layer that the object belongs to.  |  
| [`Polygon.layer_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.layer_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.layer_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.layer_name")  | Layer name.  |  
| [`Polygon.layer_number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.layer_number.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.layer_number "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.layer_number")  | Layer ID.  |  
| [`Polygon.material_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.material_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.material_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.material_name")  | Material name.  |  
| [`Polygon.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.name")  | Object name.  |  
| [`Polygon.points_on_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.points_on_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.points_on_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.points_on_layer")  | Object Bounding Box.  |  
| [`Polygon.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.public_dir.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.public_dir "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.public_dir")  | Shortcut for dir(self).  |  
| [`Polygon.reference_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.reference_system.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.reference_system "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.reference_system")  | Coordinate system of the object.  |  
| [`Polygon.signal_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.signal_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.signal_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.signal_layer")  | Signal layer that the object belongs to.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.rst.txt)

# Polygon 

class ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon(_application_ , _point_list_ , _signal_layer_ , _poly_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'poly'_, _mat_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'copper'_, _is_void : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _reference_system =None_) 
    
Polygon Class in Stackup3D. It is preferable to use the add_polygon method in the class Layer3D than directly the class constructor. 

Parameters: 
     

**application**[`ansys.aedt.core.hfss.Hfss`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss") 
    
HFSS design or project where the variable is to be created. 

**point_list**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Points list of [x,y] coordinates. 

**signal_layer**[`ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Layer3D") 
    
The signal layer where the line will be drawn. 

**poly_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Polygon name. The default is `poly`. 

**mat_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
The polygon material name. 

**is_void**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the polygon is a void. The default is `False`. On ground layers, it will act opposite of the Boolean value because the ground is negative. 

**reference_system**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`None`](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)"), `optional` 
    
Coordinate system of the polygon. By default, None.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> from ansys.aedt.core.modeler.advanced_cad.stackup_3d import Stackup3D
>>> hfss = Hfss(new_desktop=True)
>>> my_stackup = Stackup3D(hfss, 2.5e9)
>>> gnd = my_stackup.add_ground_layer("gnd", thickness=None)
>>> my_stackup.add_dielectric_layer("diel1", thickness=1.5, material="Duroid (tm)")
>>> top = my_stackup.add_signal_layer("top", thickness=None)
>>> my_polygon = top.add_polygon([[0, 0], [0, 1], [1, 1], [1, 0]])
>>> my_stackup.dielectric_x_position = "2mm"
>>> my_stackup.dielectric_y_position = "2mm"
>>> my_stackup.dielectric_length = "-3mm"
>>> my_stackup.dielectric_width = "-3mm"

```
Copy to clipboard
Attributes  
| [`Polygon.aedt_object`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.aedt_object.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.aedt_object "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.aedt_object")  | PyAEDT object 3D.  |  
| --- | --- |  
| [`Polygon.application`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.application.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.application "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.application")  | App object.  |  
| [`Polygon.dielectric_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.dielectric_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.dielectric_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.dielectric_layer")  | Dielectric layer that the object belongs to.  |  
| [`Polygon.layer_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.layer_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.layer_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.layer_name")  | Layer name.  |  
| [`Polygon.layer_number`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.layer_number.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.layer_number "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.layer_number")  | Layer ID.  |  
| [`Polygon.material_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.material_name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.material_name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.material_name")  | Material name.  |  
| [`Polygon.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.name.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.name "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.name")  | Object name.  |  
| [`Polygon.points_on_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.points_on_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.points_on_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.points_on_layer")  | Object Bounding Box.  |  
| [`Polygon.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.public_dir.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.public_dir "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.public_dir")  | Shortcut for dir(self).  |  
| [`Polygon.reference_system`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.reference_system.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.reference_system "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.reference_system")  | Coordinate system of the object.  |  
| [`Polygon.signal_layer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.signal_layer.html#ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.signal_layer "ansys.aedt.core.modeler.advanced_cad.stackup_3d.Polygon.signal_layer")  | Signal layer that the object belongs to.  |