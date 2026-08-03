---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.set_coreloss_at_frequency.html"
category: "materials"
domain: "PyAEDT / HFSS"
---

# set_coreloss_at_frequency 

Material.set_coreloss_at_frequency(_points_at_frequency : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _kdc : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _cut_depth : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1mm'_, _thickness : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.5mm'_, _conductivity : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _coefficient_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'w_per_cubic_meter'_, _core_loss_model_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Electrical Steel'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set electrical steel or power ferrite core loss model at one single frequency or at multiple frequencies. 

Parameters: 
     

**points_at_frequency**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary where keys are the frequencies (in Hz) and values are lists of points (BP curve). If the core loss model is calculated at one frequency, this parameter must be provided as a dictionary with one key (single frequency in Hz) and values are lists of points at that specific frequency (BP curve). 

**kdc**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Coefficient considering the DC flux bias effects 

**cut_depth**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Equivalent cut depth. You use this parameter to consider the manufacturing effects on core loss computation. The default value is `"1mm"`. 

**thickness**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Thickness specified in terms of the value plus the unit. The default is `"0.5mm"`. 

**conductivity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Conductivity. The unit is S/m. The default is `"0 S/m"`. 

**coefficient_setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Core loss unit. The default is `"w_per_cubic_meter"`. Options are `"kw_per_cubic_meter"`, `"w_per_cubic_meter"`, `"w_per_kg"`, and `"w_per_lb"`. 

**core_loss_model_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Core loss model type. The default value is `"Electrical Steel"`. Options are `"Electrical Steel"` and `"Power Ferrite"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDefinitionManager.EditMaterial

```
Copy to clipboard
Examples
This example shows how to set a core loss model for a material in case material properties are calculated for core losses at one frequency or core losses versus frequencies (core losses multicurve data). The first case shows how to set properties for core losses at one frequency:

```
>>> from ansys.aedt.core import Maxwell3d
>>> m3d = Maxwell3d()
>>> box = m3d.modeler.create_box([-10, -10, 0], [20, 20, 20], "box_to_split")
>>> box.material = "magnesium"
>>> m3d.materials["magnesium"].set_coreloss_at_frequency(
                                            ... points_at_frequency={60 : [[0,0], [1,3.5], [2,7.4]]}
                                            ... )
>>> m3d.desktop_class.close_desktop()

```
Copy to clipboard
The second case shows how to set properties for core losses versus frequencies:

```
>>> from ansys.aedt.core import Maxwell3d
>>> m3d = Maxwell3d()
>>> box = m3d.modeler.create_box([-10, -10, 0], [20, 20, 20], "box_to_split")
>>> box.material = "magnesium"
>>> m3d.materials["magnesium"].set_coreloss_at_frequency(
                                            ... points_at_frequency={60 : [[0,0], [1,3.5], [2,7.4]],
                                            ...                      100 : [[0,0], [1,8], [2,9]],
                                            ...                      150 : [[0,0], [1,10], [2,19]]}
                                            ... )
>>> m3d.desktop_class.close_desktop()

```
Copy to clipboard
# set_coreloss_at_frequency 

Material.set_coreloss_at_frequency(_points_at_frequency : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _kdc : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _cut_depth : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1mm'_, _thickness : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.5mm'_, _conductivity : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _coefficient_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'w_per_cubic_meter'_, _core_loss_model_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Electrical Steel'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set electrical steel or power ferrite core loss model at one single frequency or at multiple frequencies. 

Parameters: 
     

**points_at_frequency**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary where keys are the frequencies (in Hz) and values are lists of points (BP curve). If the core loss model is calculated at one frequency, this parameter must be provided as a dictionary with one key (single frequency in Hz) and values are lists of points at that specific frequency (BP curve). 

**kdc**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Coefficient considering the DC flux bias effects 

**cut_depth**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Equivalent cut depth. You use this parameter to consider the manufacturing effects on core loss computation. The default value is `"1mm"`. 

**thickness**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Thickness specified in terms of the value plus the unit. The default is `"0.5mm"`. 

**conductivity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Conductivity. The unit is S/m. The default is `"0 S/m"`. 

**coefficient_setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Core loss unit. The default is `"w_per_cubic_meter"`. Options are `"kw_per_cubic_meter"`, `"w_per_cubic_meter"`, `"w_per_kg"`, and `"w_per_lb"`. 

**core_loss_model_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Core loss model type. The default value is `"Electrical Steel"`. Options are `"Electrical Steel"` and `"Power Ferrite"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDefinitionManager.EditMaterial

```
Copy to clipboard
Examples
This example shows how to set a core loss model for a material in case material properties are calculated for core losses at one frequency or core losses versus frequencies (core losses multicurve data). The first case shows how to set properties for core losses at one frequency:

```
>>> from ansys.aedt.core import Maxwell3d
>>> m3d = Maxwell3d()
>>> box = m3d.modeler.create_box([-10, -10, 0], [20, 20, 20], "box_to_split")
>>> box.material = "magnesium"
>>> m3d.materials["magnesium"].set_coreloss_at_frequency(
                                            ... points_at_frequency={60 : [[0,0], [1,3.5], [2,7.4]]}
                                            ... )
>>> m3d.desktop_class.close_desktop()

```
Copy to clipboard
The second case shows how to set properties for core losses versus frequencies:

```
>>> from ansys.aedt.core import Maxwell3d
>>> m3d = Maxwell3d()
>>> box = m3d.modeler.create_box([-10, -10, 0], [20, 20, 20], "box_to_split")
>>> box.material = "magnesium"
>>> m3d.materials["magnesium"].set_coreloss_at_frequency(
                                            ... points_at_frequency={60 : [[0,0], [1,3.5], [2,7.4]],
                                            ...                      100 : [[0,0], [1,8], [2,9]],
                                            ...                      150 : [[0,0], [1,10], [2,19]]}
                                            ... )
>>> m3d.desktop_class.close_desktop()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.material.Material.set_coreloss_at_frequency.rst.txt)

# set_coreloss_at_frequency 

Material.set_coreloss_at_frequency(_points_at_frequency : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _kdc : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _cut_depth : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '1mm'_, _thickness : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.5mm'_, _conductivity : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _coefficient_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'w_per_cubic_meter'_, _core_loss_model_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Electrical Steel'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set electrical steel or power ferrite core loss model at one single frequency or at multiple frequencies. 

Parameters: 
     

**points_at_frequency**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary where keys are the frequencies (in Hz) and values are lists of points (BP curve). If the core loss model is calculated at one frequency, this parameter must be provided as a dictionary with one key (single frequency in Hz) and values are lists of points at that specific frequency (BP curve). 

**kdc**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Coefficient considering the DC flux bias effects 

**cut_depth**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Equivalent cut depth. You use this parameter to consider the manufacturing effects on core loss computation. The default value is `"1mm"`. 

**thickness**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Thickness specified in terms of the value plus the unit. The default is `"0.5mm"`. 

**conductivity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Conductivity. The unit is S/m. The default is `"0 S/m"`. 

**coefficient_setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Core loss unit. The default is `"w_per_cubic_meter"`. Options are `"kw_per_cubic_meter"`, `"w_per_cubic_meter"`, `"w_per_kg"`, and `"w_per_lb"`. 

**core_loss_model_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Core loss model type. The default value is `"Electrical Steel"`. Options are `"Electrical Steel"` and `"Power Ferrite"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` when successful, `False` when failed.
References

```
>>> oDefinitionManager.EditMaterial

```
Copy to clipboard
Examples
This example shows how to set a core loss model for a material in case material properties are calculated for core losses at one frequency or core losses versus frequencies (core losses multicurve data). The first case shows how to set properties for core losses at one frequency:

```
>>> from ansys.aedt.core import Maxwell3d
>>> m3d = Maxwell3d()
>>> box = m3d.modeler.create_box([-10, -10, 0], [20, 20, 20], "box_to_split")
>>> box.material = "magnesium"
>>> m3d.materials["magnesium"].set_coreloss_at_frequency(
                                            ... points_at_frequency={60 : [[0,0], [1,3.5], [2,7.4]]}
                                            ... )
>>> m3d.desktop_class.close_desktop()

```
Copy to clipboard
The second case shows how to set properties for core losses versus frequencies:

```
>>> from ansys.aedt.core import Maxwell3d
>>> m3d = Maxwell3d()
>>> box = m3d.modeler.create_box([-10, -10, 0], [20, 20, 20], "box_to_split")
>>> box.material = "magnesium"
>>> m3d.materials["magnesium"].set_coreloss_at_frequency(
                                            ... points_at_frequency={60 : [[0,0], [1,3.5], [2,7.4]],
                                            ...                      100 : [[0,0], [1,8], [2,9]],
                                            ...                      150 : [[0,0], [1,10], [2,19]]}
                                            ... )
>>> m3d.desktop_class.close_desktop()

```
Copy to clipboard