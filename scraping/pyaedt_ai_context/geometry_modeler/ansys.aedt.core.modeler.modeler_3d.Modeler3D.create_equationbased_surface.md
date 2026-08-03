---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_equationbased_surface.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# create_equationbased_surface 

Modeler3D.create_equationbased_surface(_x_uv : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _y_uv : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _z_uv : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _u_start : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _u_end : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _v_start : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _v_end : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create an equation-based surface. 

Parameters: 
     

**x_uv**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Expression for the X-component of the surface as a function of `"_u,_v"`. For example, `"cos(_u) * sin(_v)"`. 

**y_uv**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Expression for the Y-component of the surface as a function of `"_u,_v"` 

**z_uv**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Expression for the Z-component of the surface as a function of `"_u,_v"` 

**u_start**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Starting value of the parameter `"_u"`. 

**u_end**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Ending value of the parameter `"_u"`. 

**v_start**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Starting value of the parameter `"_v"`. 

**v_end**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Ending value of the parameter `"_v"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the created surface in the 3D modeler. The default is `None`, in which case the default name is assigned. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object.
References

```
>>> oEditor.CreateEquationSurface

```
Copy to clipboard
Examples
The optional parameter `matname` allows you to set the material name. The optional parameter `name` allows you to assign a name to the surface.
This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> surf = aedtapp.modeler.create_equationbased_surface(x_uv='(cos(_v)+2)*cos(_u)',
...                                                     y_uv='(cos(_v)+2)*sin(_u)',
...                                                     z_uv='sin(_v)',
...                                                     u_start=0,
...                                                     u_end='2*pi',
...                                                     v_start=0,
...                                                     v_end='2*pi'
...                                                     )

```
Copy to clipboard
# create_equationbased_surface 

Modeler3D.create_equationbased_surface(_x_uv : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _y_uv : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _z_uv : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _u_start : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _u_end : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _v_start : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _v_end : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create an equation-based surface. 

Parameters: 
     

**x_uv**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Expression for the X-component of the surface as a function of `"_u,_v"`. For example, `"cos(_u) * sin(_v)"`. 

**y_uv**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Expression for the Y-component of the surface as a function of `"_u,_v"` 

**z_uv**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Expression for the Z-component of the surface as a function of `"_u,_v"` 

**u_start**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Starting value of the parameter `"_u"`. 

**u_end**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Ending value of the parameter `"_u"`. 

**v_start**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Starting value of the parameter `"_v"`. 

**v_end**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Ending value of the parameter `"_v"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the created surface in the 3D modeler. The default is `None`, in which case the default name is assigned. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object.
References

```
>>> oEditor.CreateEquationSurface

```
Copy to clipboard
Examples
The optional parameter `matname` allows you to set the material name. The optional parameter `name` allows you to assign a name to the surface.
This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> surf = aedtapp.modeler.create_equationbased_surface(x_uv='(cos(_v)+2)*cos(_u)',
...                                                     y_uv='(cos(_v)+2)*sin(_u)',
...                                                     z_uv='sin(_v)',
...                                                     u_start=0,
...                                                     u_end='2*pi',
...                                                     v_start=0,
...                                                     v_end='2*pi'
...                                                     )

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_equationbased_surface.rst.txt)

# create_equationbased_surface 

Modeler3D.create_equationbased_surface(_x_uv : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _y_uv : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _z_uv : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _u_start : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _u_end : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _v_start : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _v_end : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 1_, _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_, _** kwargs_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") 
    
Create an equation-based surface. 

Parameters: 
     

**x_uv**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Expression for the X-component of the surface as a function of `"_u,_v"`. For example, `"cos(_u) * sin(_v)"`. 

**y_uv**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Expression for the Y-component of the surface as a function of `"_u,_v"` 

**z_uv**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Expression for the Z-component of the surface as a function of `"_u,_v"` 

**u_start**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Starting value of the parameter `"_u"`. 

**u_end**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Ending value of the parameter `"_u"`. 

**v_start**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Starting value of the parameter `"_v"`. 

**v_end**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Ending value of the parameter `"_v"`. 

**name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the created surface in the 3D modeler. The default is `None`, in which case the default name is assigned. 

****kwargs**`optional` 
    
Additional keyword arguments may be passed when creating the primitive to set properties. See `ansys.aedt.core.modeler.cad.object_3d.Object3d` for more details. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
3D object.
References

```
>>> oEditor.CreateEquationSurface

```
Copy to clipboard
Examples
The optional parameter `matname` allows you to set the material name. The optional parameter `name` allows you to assign a name to the surface.
This method applies to all 3D applications: HFSS, Q3D, Icepak, Maxwell 3D, and Mechanical.

```
>>> from ansys.aedt.core import Hfss
>>> aedtapp = Hfss()
>>> surf = aedtapp.modeler.create_equationbased_surface(x_uv='(cos(_v)+2)*cos(_u)',
...                                                     y_uv='(cos(_v)+2)*sin(_u)',
...                                                     z_uv='sin(_v)',
...                                                     u_start=0,
...                                                     u_end='2*pi',
...                                                     v_start=0,
...                                                     v_end='2*pi'
...                                                     )

```
Copy to clipboard