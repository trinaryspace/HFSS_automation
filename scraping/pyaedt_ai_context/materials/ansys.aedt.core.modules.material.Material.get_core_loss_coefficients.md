---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.material.Material.get_core_loss_coefficients.html"
category: "materials"
domain: "PyAEDT / HFSS"
---

# get_core_loss_coefficients 

Material.get_core_loss_coefficients(_points_at_frequency : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _core_loss_model_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Electrical Steel'_, _thickness : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.5mm'_, _conductivity : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _coefficient_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'w_per_cubic_meter'_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get electrical steel or power ferrite core loss coefficients at a given frequency. 

Parameters: 
     

**points_at_frequency**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary where keys are the frequencies (in Hz) and values are lists of points (BP curve). If the core loss model is calculated at one frequency, this parameter must be provided as a dictionary with one key (single frequency in Hz) and values are lists of points at that specific frequency (BP curve). 

**core_loss_model_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Core loss model type. The default value is `"Electrical Steel"`. Options are `"Electrical Steel"` and `"Power Ferrite"`. 

**thickness**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Thickness provided as the value plus the unit. The default is `0.5mm`. 

**conductivity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Material conductivity. The default is `0`. 

**coefficient_setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Core loss unit. The default is `"w_per_cubic_meter"`. Options are `"kw_per_cubic_meter"`, `"w_per_cubic_meter"`, `"w_per_kg"`, and `"w_per_lb"`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of core loss coefficients. Returns Kh, Kc, and Ke coefficients if the core loss model is `"Electrical Steel"`. Returns Cm, X, and Y if the core loss model is `"Power Ferrite"`.
Examples
This example shows how to get core loss coefficients for Electrical Steel core loss model.

```
>>> from ansys.aedt.core import Maxwell3d
>>> m3d = Maxwell3d()
>>> box = m3d.modeler.create_box([-10, -10, 0], [20, 20, 20], "box_to_split")
>>> box.material = "magnesium"
>>> coefficients = m3d.materials["magnesium"].get_core_loss_coefficients(
...     points_at_frequency={60: [[0, 0], [1, 3], [2, 7]]}, thickness="0.5mm", conductivity=0
... )
>>> print(coefficients)
>>> m3d.desktop_class.close_desktop()

```
Copy to clipboard
# get_core_loss_coefficients 

Material.get_core_loss_coefficients(_points_at_frequency : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _core_loss_model_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Electrical Steel'_, _thickness : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.5mm'_, _conductivity : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _coefficient_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'w_per_cubic_meter'_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get electrical steel or power ferrite core loss coefficients at a given frequency. 

Parameters: 
     

**points_at_frequency**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary where keys are the frequencies (in Hz) and values are lists of points (BP curve). If the core loss model is calculated at one frequency, this parameter must be provided as a dictionary with one key (single frequency in Hz) and values are lists of points at that specific frequency (BP curve). 

**core_loss_model_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Core loss model type. The default value is `"Electrical Steel"`. Options are `"Electrical Steel"` and `"Power Ferrite"`. 

**thickness**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Thickness provided as the value plus the unit. The default is `0.5mm`. 

**conductivity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Material conductivity. The default is `0`. 

**coefficient_setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Core loss unit. The default is `"w_per_cubic_meter"`. Options are `"kw_per_cubic_meter"`, `"w_per_cubic_meter"`, `"w_per_kg"`, and `"w_per_lb"`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of core loss coefficients. Returns Kh, Kc, and Ke coefficients if the core loss model is `"Electrical Steel"`. Returns Cm, X, and Y if the core loss model is `"Power Ferrite"`.
Examples
This example shows how to get core loss coefficients for Electrical Steel core loss model.

```
>>> from ansys.aedt.core import Maxwell3d
>>> m3d = Maxwell3d()
>>> box = m3d.modeler.create_box([-10, -10, 0], [20, 20, 20], "box_to_split")
>>> box.material = "magnesium"
>>> coefficients = m3d.materials["magnesium"].get_core_loss_coefficients(
...     points_at_frequency={60: [[0, 0], [1, 3], [2, 7]]}, thickness="0.5mm", conductivity=0
... )
>>> print(coefficients)
>>> m3d.desktop_class.close_desktop()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.material.Material.get_core_loss_coefficients.rst.txt)

# get_core_loss_coefficients 

Material.get_core_loss_coefficients(_points_at_frequency : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _core_loss_model_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'Electrical Steel'_, _thickness : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.5mm'_, _conductivity : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = 0_, _coefficient_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'w_per_cubic_meter'_) → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Get electrical steel or power ferrite core loss coefficients at a given frequency. 

Parameters: 
     

**points_at_frequency**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary where keys are the frequencies (in Hz) and values are lists of points (BP curve). If the core loss model is calculated at one frequency, this parameter must be provided as a dictionary with one key (single frequency in Hz) and values are lists of points at that specific frequency (BP curve). 

**core_loss_model_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Core loss model type. The default value is `"Electrical Steel"`. Options are `"Electrical Steel"` and `"Power Ferrite"`. 

**thickness**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Thickness provided as the value plus the unit. The default is `0.5mm`. 

**conductivity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Material conductivity. The default is `0`. 

**coefficient_setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Core loss unit. The default is `"w_per_cubic_meter"`. Options are `"kw_per_cubic_meter"`, `"w_per_cubic_meter"`, `"w_per_kg"`, and `"w_per_lb"`. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")
    
List of core loss coefficients. Returns Kh, Kc, and Ke coefficients if the core loss model is `"Electrical Steel"`. Returns Cm, X, and Y if the core loss model is `"Power Ferrite"`.
Examples
This example shows how to get core loss coefficients for Electrical Steel core loss model.

```
>>> from ansys.aedt.core import Maxwell3d
>>> m3d = Maxwell3d()
>>> box = m3d.modeler.create_box([-10, -10, 0], [20, 20, 20], "box_to_split")
>>> box.material = "magnesium"
>>> coefficients = m3d.materials["magnesium"].get_core_loss_coefficients(
...     points_at_frequency={60: [[0, 0], [1, 3], [2, 7]]}, thickness="0.5mm", conductivity=0
... )
>>> print(coefficients)
>>> m3d.desktop_class.close_desktop()

```
Copy to clipboard