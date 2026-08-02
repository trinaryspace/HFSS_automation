---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.edit_cosim_options.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# edit_cosim_options 

Hfss3dLayout.edit_cosim_options(_simulate_missing_solution : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _align_ports : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _renormalize_ports : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _renorm_impedance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 50_, _setup_override_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _sweep_override_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _use_interpolating_sweep : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _use_y_matrix : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _interpolation_algorithm : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'auto'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Edit cosimulation options. 

Parameters: 
     

**simulate_missing_solution**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the solver is to simulate a missing solution. The default is `True`. If `False`, the solver interpolates a missing solution. 

**align_ports**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the solver is to align microwave parts. The default is `True`. 

**renormalize_ports**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to renormalize port impendance. The default is `True`. 

**renorm_impedance**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Renormalization impedance in ohms. The default is `50`. 

**setup_override_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Setup name if there is a setup override. The default is `None`. 

**sweep_override_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Sweep name if there is a sweep override. The default is `None`. 

**use_interpolating_sweep**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the solver is to use an interpolating sweep. The default is `True`. If `False`, the solver is to use a discrete sweep. 

**use_y_matrix**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the interpolation algorithm is to use the Y matrix. The default is `True`. 

**interpolation_algorithm**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Interpolation algorithm to use. Options are `"auto"`, `"lin"`, `"shadH"`, and `"shadNH"`. The default is `"auto"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful and `False` if failed.
References

```
>>> oDesign.EditCoSimulationOptions

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> h3d = Hfss3dLayout()
>>> h3d.edit_cosim_options(
...     simulate_missing_solution=True,
...     align_ports=True,
...     renormalize_ports=True,
...     renorm_impedance=50,
...     setup_override_name=None,
...     sweep_override_name=None,
...     use_interpolating_sweep=False,
...     use_y_matrix=True,
...     interpolation_algorithm="auto",
... )

```
Copy to clipboard
# edit_cosim_options 

Hfss3dLayout.edit_cosim_options(_simulate_missing_solution : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _align_ports : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _renormalize_ports : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _renorm_impedance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 50_, _setup_override_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _sweep_override_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _use_interpolating_sweep : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _use_y_matrix : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _interpolation_algorithm : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'auto'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Edit cosimulation options. 

Parameters: 
     

**simulate_missing_solution**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the solver is to simulate a missing solution. The default is `True`. If `False`, the solver interpolates a missing solution. 

**align_ports**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the solver is to align microwave parts. The default is `True`. 

**renormalize_ports**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to renormalize port impendance. The default is `True`. 

**renorm_impedance**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Renormalization impedance in ohms. The default is `50`. 

**setup_override_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Setup name if there is a setup override. The default is `None`. 

**sweep_override_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Sweep name if there is a sweep override. The default is `None`. 

**use_interpolating_sweep**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the solver is to use an interpolating sweep. The default is `True`. If `False`, the solver is to use a discrete sweep. 

**use_y_matrix**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the interpolation algorithm is to use the Y matrix. The default is `True`. 

**interpolation_algorithm**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Interpolation algorithm to use. Options are `"auto"`, `"lin"`, `"shadH"`, and `"shadNH"`. The default is `"auto"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful and `False` if failed.
References

```
>>> oDesign.EditCoSimulationOptions

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> h3d = Hfss3dLayout()
>>> h3d.edit_cosim_options(
...     simulate_missing_solution=True,
...     align_ports=True,
...     renormalize_ports=True,
...     renorm_impedance=50,
...     setup_override_name=None,
...     sweep_override_name=None,
...     use_interpolating_sweep=False,
...     use_y_matrix=True,
...     interpolation_algorithm="auto",
... )

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss3dlayout.Hfss3dLayout.edit_cosim_options.rst.txt)

# edit_cosim_options 

Hfss3dLayout.edit_cosim_options(_simulate_missing_solution : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _align_ports : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _renormalize_ports : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _renorm_impedance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 50_, _setup_override_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _sweep_override_name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _use_interpolating_sweep : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _use_y_matrix : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _interpolation_algorithm : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 'auto'_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Edit cosimulation options. 

Parameters: 
     

**simulate_missing_solution**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the solver is to simulate a missing solution. The default is `True`. If `False`, the solver interpolates a missing solution. 

**align_ports**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the solver is to align microwave parts. The default is `True`. 

**renormalize_ports**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to renormalize port impendance. The default is `True`. 

**renorm_impedance**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Renormalization impedance in ohms. The default is `50`. 

**setup_override_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Setup name if there is a setup override. The default is `None`. 

**sweep_override_name**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Sweep name if there is a sweep override. The default is `None`. 

**use_interpolating_sweep**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the solver is to use an interpolating sweep. The default is `True`. If `False`, the solver is to use a discrete sweep. 

**use_y_matrix**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether the interpolation algorithm is to use the Y matrix. The default is `True`. 

**interpolation_algorithm**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Interpolation algorithm to use. Options are `"auto"`, `"lin"`, `"shadH"`, and `"shadNH"`. The default is `"auto"`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
`True` if successful and `False` if failed.
References

```
>>> oDesign.EditCoSimulationOptions

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss3dLayout
>>> h3d = Hfss3dLayout()
>>> h3d.edit_cosim_options(
...     simulate_missing_solution=True,
...     align_ports=True,
...     renormalize_ports=True,
...     renorm_impedance=50,
...     setup_override_name=None,
...     sweep_override_name=None,
...     use_interpolating_sweep=False,
...     use_y_matrix=True,
...     interpolation_algorithm="auto",
... )

```
Copy to clipboard