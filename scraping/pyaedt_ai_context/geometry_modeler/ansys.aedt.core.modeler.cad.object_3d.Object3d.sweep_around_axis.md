---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.sweep_around_axis.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# sweep_around_axis 

Object3d.sweep_around_axis(_axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _sweep_angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 360_, _draft_angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Sweep around an axis. 

Parameters: 
     

**axis**[`ansys.aedt.core.generic.constants.Axis`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis") 
    
Coordinate system of the axis. 

**sweep_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Sweep angle in degrees. The default is `360`. 

**draft_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Angle of the draft. The default is `0`. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
Swept object.
References

```
>>> oEditor.SweepAroundAxis

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.sweep_around_axis(axis="Z")

```
Copy to clipboard
# sweep_around_axis 

Object3d.sweep_around_axis(_axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _sweep_angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 360_, _draft_angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Sweep around an axis. 

Parameters: 
     

**axis**[`ansys.aedt.core.generic.constants.Axis`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis") 
    
Coordinate system of the axis. 

**sweep_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Sweep angle in degrees. The default is `360`. 

**draft_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Angle of the draft. The default is `0`. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
Swept object.
References

```
>>> oEditor.SweepAroundAxis

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.sweep_around_axis(axis="Z")

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.sweep_around_axis.rst.txt)

# sweep_around_axis 

Object3d.sweep_around_axis(_axis : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")_, _sweep_angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 360_, _draft_angle : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_) → [Object3d](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Sweep around an axis. 

Parameters: 
     

**axis**[`ansys.aedt.core.generic.constants.Axis`](https://aedt.docs.pyansys.com/version/stable/API/Constants.html#ansys.aedt.core.generic.constants.Axis "ansys.aedt.core.generic.constants.Axis") 
    
Coordinate system of the axis. 

**sweep_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Sweep angle in degrees. The default is `360`. 

**draft_angle**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Angle of the draft. The default is `0`. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.object_3d.Object3d`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.object_3d.Object3d.html#ansys.aedt.core.modeler.cad.object_3d.Object3d "ansys.aedt.core.modeler.cad.object_3d.Object3d")
    
Swept object.
References

```
>>> oEditor.SweepAroundAxis

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core.modeler.cad.object_3d import Object3d
>>> obj = Object3d()
>>> obj.sweep_around_axis(axis="Z")

```
Copy to clipboard