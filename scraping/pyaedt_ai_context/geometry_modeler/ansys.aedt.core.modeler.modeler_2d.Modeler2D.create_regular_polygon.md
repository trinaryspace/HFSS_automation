---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.create_regular_polygon.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_regular_polygon 

Modeler2D.create_regular_polygon(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _start_point : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _num_sides : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 6_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _non_model : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a rectangle. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Position of the center of the polygon in `[x, y, z]`. 

**start_point**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Start point for the outer path of the polygon in `[x, y, z]`. 

**num_sides**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Number of sides of the polygon. Must be an integer >= 3. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), default=None 
    
Name of the object. The default is `None`. If `None` , a unique name NewObject_xxxxxx will be assigned) 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), default=None 
    
Name of the material. The default is `None`. If `None`, the default material is assigned. 

**non_model**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
> Either if create the new object as model or non-model. The default is `False`. 

[**](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.create_regular_polygon.html#id1)kwargsoptional 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
References

```
>>> oEditor.CreateRegularPolygon

```
Copy to clipboard
Examples

```
>>> pg1 = aedtapp.modeler.create_regular_polygon([0, 0, 0], [0, 2, 0])
>>> pg2 = aedtapp.modeler.create_regular_polygon(origin=[0, 0, 0], start_point=[0, 2, 0],
...                                              name="MyPolygon", material="Copper")

```
Copy to clipboard
# create_regular_polygon 

Modeler2D.create_regular_polygon(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _start_point : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _num_sides : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 6_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _non_model : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a rectangle. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Position of the center of the polygon in `[x, y, z]`. 

**start_point**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Start point for the outer path of the polygon in `[x, y, z]`. 

**num_sides**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Number of sides of the polygon. Must be an integer >= 3. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), default=None 
    
Name of the object. The default is `None`. If `None` , a unique name NewObject_xxxxxx will be assigned) 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), default=None 
    
Name of the material. The default is `None`. If `None`, the default material is assigned. 

**non_model**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
> Either if create the new object as model or non-model. The default is `False`. 

[**](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.create_regular_polygon.html#id1)kwargsoptional 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
References

```
>>> oEditor.CreateRegularPolygon

```
Copy to clipboard
Examples

```
>>> pg1 = aedtapp.modeler.create_regular_polygon([0, 0, 0], [0, 2, 0])
>>> pg2 = aedtapp.modeler.create_regular_polygon(origin=[0, 0, 0], start_point=[0, 2, 0],
...                                              name="MyPolygon", material="Copper")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.create_regular_polygon.rst.txt)

# create_regular_polygon 

Modeler2D.create_regular_polygon(_origin : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _start_point : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")_, _num_sides : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 6_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _material : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _non_model : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create a rectangle. 

Parameters: 
     

**origin**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Position of the center of the polygon in `[x, y, z]`. 

**start_point**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Start point for the outer path of the polygon in `[x, y, z]`. 

**num_sides**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") 
    
Number of sides of the polygon. Must be an integer >= 3. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), default=None 
    
Name of the object. The default is `None`. If `None` , a unique name NewObject_xxxxxx will be assigned) 

**material**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), default=None 
    
Name of the material. The default is `None`. If `None`, the default material is assigned. 

**non_model**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
> Either if create the new object as model or non-model. The default is `False`. 

[**](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.create_regular_polygon.html#id1)kwargsoptional 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
References

```
>>> oEditor.CreateRegularPolygon

```
Copy to clipboard
Examples

```
>>> pg1 = aedtapp.modeler.create_regular_polygon([0, 0, 0], [0, 2, 0])
>>> pg2 = aedtapp.modeler.create_regular_polygon(origin=[0, 0, 0], start_point=[0, 2, 0],
...                                              name="MyPolygon", material="Copper")

```
Copy to clipboard