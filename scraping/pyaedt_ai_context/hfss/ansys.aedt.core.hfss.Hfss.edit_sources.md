---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.edit_sources.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# edit_sources 

Hfss.edit_sources(_assignment : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _include_port_post_processing : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _max_available_power : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _use_incident_voltage : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _eigenmode_stored_energy : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _incident_wave : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set up the power loaded for HFSS postprocessing in multiple sources simultaneously. 

Parameters: 
     

**assignment**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary of input sources to modify module and phase. Dictionary values can be: - 1 value to setup 0deg as default - 2 values tuple or list (magnitude and phase) or - 3 values (magnitude, phase, and termination flag) for Terminal solution in case of incident voltage usage. 

**include_port_post_processing**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Include port post-processing effects. The default is `True`. 

**max_available_power**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
System power for gain calculations. The default is `None`, in which case maximum available power is applied. 

**use_incident_voltage**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Use incident voltage definition. The default is `False`. This argument applies only to the Terminal solution type. 

**eigenmode_stored_energy**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Use stored energy definition. The default is `True`. This argument applies only to the Eigenmode solution type. 

**incident_wave**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Incident wave type. The default is None`, in which case the current type is not modified. Options are `IncidentWaveType.Scattered`, `IncidentWaveType.Incident`, and `IncidentWaveType.Total`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> sources = {"Port1:1": ("0W", "0deg"), "Port2:1": ("1W", "90deg")}
>>> hfss.edit_sources(sources, include_port_post_processing=True)

```
Copy to clipboard

```
>>> sources = {"Box2_T1": ("0V", "0deg", True), "Box1_T1": ("1V", "90deg")}
>>> hfss.edit_sources(sources, max_available_power="2W", use_incident_voltage=True)

```
Copy to clipboard

```
>>> aedtapp = add_app(solution_type="Eigenmode")
>>> _ = aedtapp.modeler.create_box([0, 0, 0], [10, 20, 20])
>>> setup = aedtapp.create_setup()
>>> setup.props["NumModes"] = 2
>>> sources = {"1": "1Joules", "2": "0Joules"}
>>> aedtapp.edit_sources(sources, eigenmode_stored_energy=True)
>>> sources = {"1": ("0V/M", "0deg"), "2": ("2V/M", "90deg")}
>>> aedtapp.edit_sources(sources, eigenmode_stored_energy=False)

```
Copy to clipboard
# edit_sources 

Hfss.edit_sources(_assignment : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _include_port_post_processing : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _max_available_power : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _use_incident_voltage : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _eigenmode_stored_energy : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _incident_wave : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set up the power loaded for HFSS postprocessing in multiple sources simultaneously. 

Parameters: 
     

**assignment**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary of input sources to modify module and phase. Dictionary values can be: - 1 value to setup 0deg as default - 2 values tuple or list (magnitude and phase) or - 3 values (magnitude, phase, and termination flag) for Terminal solution in case of incident voltage usage. 

**include_port_post_processing**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Include port post-processing effects. The default is `True`. 

**max_available_power**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
System power for gain calculations. The default is `None`, in which case maximum available power is applied. 

**use_incident_voltage**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Use incident voltage definition. The default is `False`. This argument applies only to the Terminal solution type. 

**eigenmode_stored_energy**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Use stored energy definition. The default is `True`. This argument applies only to the Eigenmode solution type. 

**incident_wave**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Incident wave type. The default is None`, in which case the current type is not modified. Options are `IncidentWaveType.Scattered`, `IncidentWaveType.Incident`, and `IncidentWaveType.Total`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> sources = {"Port1:1": ("0W", "0deg"), "Port2:1": ("1W", "90deg")}
>>> hfss.edit_sources(sources, include_port_post_processing=True)

```
Copy to clipboard

```
>>> sources = {"Box2_T1": ("0V", "0deg", True), "Box1_T1": ("1V", "90deg")}
>>> hfss.edit_sources(sources, max_available_power="2W", use_incident_voltage=True)

```
Copy to clipboard

```
>>> aedtapp = add_app(solution_type="Eigenmode")
>>> _ = aedtapp.modeler.create_box([0, 0, 0], [10, 20, 20])
>>> setup = aedtapp.create_setup()
>>> setup.props["NumModes"] = 2
>>> sources = {"1": "1Joules", "2": "0Joules"}
>>> aedtapp.edit_sources(sources, eigenmode_stored_energy=True)
>>> sources = {"1": ("0V/M", "0deg"), "2": ("2V/M", "90deg")}
>>> aedtapp.edit_sources(sources, eigenmode_stored_energy=False)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.edit_sources.rst.txt)

# edit_sources 

Hfss.edit_sources(_assignment : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_, _include_port_post_processing : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _max_available_power : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _use_incident_voltage : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _eigenmode_stored_energy : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = True_, _incident_wave : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Set up the power loaded for HFSS postprocessing in multiple sources simultaneously. 

Parameters: 
     

**assignment**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary of input sources to modify module and phase. Dictionary values can be: - 1 value to setup 0deg as default - 2 values tuple or list (magnitude and phase) or - 3 values (magnitude, phase, and termination flag) for Terminal solution in case of incident voltage usage. 

**include_port_post_processing**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Include port post-processing effects. The default is `True`. 

**max_available_power**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
System power for gain calculations. The default is `None`, in which case maximum available power is applied. 

**use_incident_voltage**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Use incident voltage definition. The default is `False`. This argument applies only to the Terminal solution type. 

**eigenmode_stored_energy**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Use stored energy definition. The default is `True`. This argument applies only to the Eigenmode solution type. 

**incident_wave**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Incident wave type. The default is None`, in which case the current type is not modified. Options are `IncidentWaveType.Scattered`, `IncidentWaveType.Incident`, and `IncidentWaveType.Total`. 

Returns: 
     

[bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)")
    
Examples

```
>>> sources = {"Port1:1": ("0W", "0deg"), "Port2:1": ("1W", "90deg")}
>>> hfss.edit_sources(sources, include_port_post_processing=True)

```
Copy to clipboard

```
>>> sources = {"Box2_T1": ("0V", "0deg", True), "Box1_T1": ("1V", "90deg")}
>>> hfss.edit_sources(sources, max_available_power="2W", use_incident_voltage=True)

```
Copy to clipboard

```
>>> aedtapp = add_app(solution_type="Eigenmode")
>>> _ = aedtapp.modeler.create_box([0, 0, 0], [10, 20, 20])
>>> setup = aedtapp.create_setup()
>>> setup.props["NumModes"] = 2
>>> sources = {"1": "1Joules", "2": "0Joules"}
>>> aedtapp.edit_sources(sources, eigenmode_stored_energy=True)
>>> sources = {"1": ("0V/M", "0deg"), "2": ("2V/M", "90deg")}
>>> aedtapp.edit_sources(sources, eigenmode_stored_energy=False)

```
Copy to clipboard