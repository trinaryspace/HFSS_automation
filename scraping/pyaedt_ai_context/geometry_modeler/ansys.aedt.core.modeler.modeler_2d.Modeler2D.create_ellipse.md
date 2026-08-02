---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.create_ellipse.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_ellipse 

Modeler2D.create_ellipse(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _major_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _ratio : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _is_covered : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _non_model : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _segments : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create an ellipse. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Center Position of the ellipse 

**major_radius**`flost` 
    
Length of the major axis of the ellipse 

**ratio**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Ratio of the major axis to the minor axis of the ellipse 

**is_covered**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Specify whether the ellipse is a sheet (covered) or a line object 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), default=None 
    
Name of the object. The default is `None`. If `None` , a unique name NewObject_xxxxxx will be assigned) 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), default=None 
    
Name of the material. The default is `None`. If `None`, the default material is assigned. 

**non_model**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create the object as a non-model. The default is `False`, in which case the object is created as a model. 

**segments**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments to apply to create the segmented geometry. The default is `0`. 

****kwargs**`optional` 
    
> Additional keyword arguments to pass to set properties when creating the primitive.
For more information, see `ansys.aedt.core.modeler.cad.object_3d.Object3d`. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
Object 3d.
References

```
>>> oEditor.CreateEllipse

```
Copy to clipboard
Examples

```
>>> ellipse1 = aedtapp.modeler.create_ellipse([0, -2, -2], 4.0, 0.2)
>>> ellipse2 = aedtapp.modeler.create_ellipse(origin=[0, -2, -2], major_radius=4.0, ratio=0.2,
...                                           name="MyEllipse", material="Copper")

```
Copy to clipboard
# create_ellipse 

Modeler2D.create_ellipse(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _major_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _ratio : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _is_covered : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _non_model : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _segments : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create an ellipse. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Center Position of the ellipse 

**major_radius**`flost` 
    
Length of the major axis of the ellipse 

**ratio**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Ratio of the major axis to the minor axis of the ellipse 

**is_covered**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Specify whether the ellipse is a sheet (covered) or a line object 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), default=None 
    
Name of the object. The default is `None`. If `None` , a unique name NewObject_xxxxxx will be assigned) 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), default=None 
    
Name of the material. The default is `None`. If `None`, the default material is assigned. 

**non_model**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create the object as a non-model. The default is `False`, in which case the object is created as a model. 

**segments**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments to apply to create the segmented geometry. The default is `0`. 

****kwargs**`optional` 
    
> Additional keyword arguments to pass to set properties when creating the primitive.
For more information, see `ansys.aedt.core.modeler.cad.object_3d.Object3d`. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
Object 3d.
References

```
>>> oEditor.CreateEllipse

```
Copy to clipboard
Examples

```
>>> ellipse1 = aedtapp.modeler.create_ellipse([0, -2, -2], 4.0, 0.2)
>>> ellipse2 = aedtapp.modeler.create_ellipse(origin=[0, -2, -2], major_radius=4.0, ratio=0.2,
...                                           name="MyEllipse", material="Copper")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.create_ellipse.rst.txt)

# create_ellipse 

Modeler2D.create_ellipse(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _major_radius : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _ratio : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)")_, _is_covered : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = True_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _non_model : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _segments : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create an ellipse. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Center Position of the ellipse 

**major_radius**`flost` 
    
Length of the major axis of the ellipse 

**ratio**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Ratio of the major axis to the minor axis of the ellipse 

**is_covered**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)") 
    
Specify whether the ellipse is a sheet (covered) or a line object 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), default=None 
    
Name of the object. The default is `None`. If `None` , a unique name NewObject_xxxxxx will be assigned) 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), default=None 
    
Name of the material. The default is `None`. If `None`, the default material is assigned. 

**non_model**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to create the object as a non-model. The default is `False`, in which case the object is created as a model. 

**segments**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Number of segments to apply to create the segmented geometry. The default is `0`. 

****kwargs**`optional` 
    
> Additional keyword arguments to pass to set properties when creating the primitive.
For more information, see `ansys.aedt.core.modeler.cad.object_3d.Object3d`. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
Object 3d.
References

```
>>> oEditor.CreateEllipse

```
Copy to clipboard
Examples

```
>>> ellipse1 = aedtapp.modeler.create_ellipse([0, -2, -2], 4.0, 0.2)
>>> ellipse2 = aedtapp.modeler.create_ellipse(origin=[0, -2, -2], major_radius=4.0, ratio=0.2,
...                                           name="MyEllipse", material="Copper")

```
Copy to clipboard