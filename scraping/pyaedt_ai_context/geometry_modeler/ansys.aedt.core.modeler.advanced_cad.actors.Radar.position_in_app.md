---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.position_in_app.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# position_in_app 

Radar.position_in_app(_app : [Hfss](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss")_) → [CoordinateSystem](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Set up design variables and values to enable motion for the multi-part 3D component. 

Parameters: 
     

**app**`ansys.aedt.core.Hfss` 
    
HFSS application instance. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.modeler.CoordinateSystem`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem")
    
Examples

```
>>> import ansys.aedt.core as pyaedt
>>> from ansys.aedt.core.modeler.advanced_cad.multiparts import MultiPartComponent
>>> hfss = pyaedt.Hfss()
>>> component = MultiPartComponent(r"C:\temp\actors", motion=True)
>>> component.position_in_app(hfss)

```
Copy to clipboard
# position_in_app 

Radar.position_in_app(_app : [Hfss](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss")_) → [CoordinateSystem](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Set up design variables and values to enable motion for the multi-part 3D component. 

Parameters: 
     

**app**`ansys.aedt.core.Hfss` 
    
HFSS application instance. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.modeler.CoordinateSystem`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem")
    
Examples

```
>>> import ansys.aedt.core as pyaedt
>>> from ansys.aedt.core.modeler.advanced_cad.multiparts import MultiPartComponent
>>> hfss = pyaedt.Hfss()
>>> component = MultiPartComponent(r"C:\temp\actors", motion=True)
>>> component.position_in_app(hfss)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.advanced_cad.actors.Radar.position_in_app.rst.txt)

# position_in_app 

Radar.position_in_app(_app : [Hfss](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.html#ansys.aedt.core.hfss.Hfss "ansys.aedt.core.hfss.Hfss")_) → [CoordinateSystem](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") 
    
Set up design variables and values to enable motion for the multi-part 3D component. 

Parameters: 
     

**app**`ansys.aedt.core.Hfss` 
    
HFSS application instance. 

Returns: 
     

[`ansys.aedt.core.modeler.cad.modeler.CoordinateSystem`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.modeler.CoordinateSystem.html#ansys.aedt.core.modeler.cad.modeler.CoordinateSystem "ansys.aedt.core.modeler.cad.modeler.CoordinateSystem")
    
Examples

```
>>> import ansys.aedt.core as pyaedt
>>> from ansys.aedt.core.modeler.advanced_cad.multiparts import MultiPartComponent
>>> hfss = pyaedt.Hfss()
>>> component = MultiPartComponent(r"C:\temp\actors", motion=True)
>>> component.position_in_app(hfss)

```
Copy to clipboard