---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.model_units.html"
category: "geometry_modeler"
domain: "PyAEDT / HFSS"
---

# model_units 

property Modeler2D.model_units: [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Model units as a string. For example, `"mm"`.
This property allows you to get or set the model units. When setting the model units, you can specify whether to rescale the model by adjusting the `rescale_model` attribute.
References

```
>>> oEditor.GetModelUnits
>>> oEditor.SetModelUnits

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import hfss
>>> hfss = Hfss()
>>> hfss.modeler.model_units = "cm"
>>> hfss.modeler.rescale_model = True
>>> hfss.modeler.model_units = "mm"

```
Copy to clipboard
# model_units 

property Modeler2D.model_units: [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Model units as a string. For example, `"mm"`.
This property allows you to get or set the model units. When setting the model units, you can specify whether to rescale the model by adjusting the `rescale_model` attribute.
References

```
>>> oEditor.GetModelUnits
>>> oEditor.SetModelUnits

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import hfss
>>> hfss = Hfss()
>>> hfss.modeler.model_units = "cm"
>>> hfss.modeler.rescale_model = True
>>> hfss.modeler.model_units = "mm"

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modeler.modeler_2d.Modeler2D.model_units.rst.txt)

# model_units 

property Modeler2D.model_units: [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Model units as a string. For example, `"mm"`.
This property allows you to get or set the model units. When setting the model units, you can specify whether to rescale the model by adjusting the `rescale_model` attribute.
References

```
>>> oEditor.GetModelUnits
>>> oEditor.SetModelUnits

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import hfss
>>> hfss = Hfss()
>>> hfss.modeler.model_units = "cm"
>>> hfss.modeler.rescale_model = True
>>> hfss.modeler.model_units = "mm"

```
Copy to clipboard