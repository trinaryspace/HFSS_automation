---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# VoltageSinSource 

class ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _source_type =None_) 
    
Power Sinusoidal Class.
Examples

```
>>> from ansys.aedt.core.modules.boundary.circuit_boundary import VoltageSinSource
>>> import ansys.aedt.core as pyaedt
>>> app = pyaedt.Circuit()
>>> source = VoltageSinSource(app, name="V1")

```
Copy to clipboard
Methods  
| [`VoltageSinSource.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.create.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.create "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.create")()  | Create a new source in AEDT.  |  
| --- | --- |  
| [`VoltageSinSource.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.delete.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.delete "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.delete")()  | Delete the source in AEDT.  |  
| [`VoltageSinSource.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.update.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.update "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.update")([original_name, ...])  | Update the source in AEDT.  |  
Attributes  
| [`VoltageSinSource.ac_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.ac_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.ac_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.ac_magnitude")  | AC magnitude value.  |  
| --- | --- |  
| [`VoltageSinSource.ac_phase`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.ac_phase.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.ac_phase "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.ac_phase")  | AC phase value.  |  
| [`VoltageSinSource.damping_factor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.damping_factor.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.damping_factor "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.damping_factor")  | Damping factor.  |  
| [`VoltageSinSource.dc_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.dc_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.dc_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.dc_magnitude")  | DC voltage value.  |  
| [`VoltageSinSource.delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.delay "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.delay")  | Delay to start of sine wave.  |  
| [`VoltageSinSource.frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.frequency.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.frequency "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.frequency")  | Frequency.  |  
| [`VoltageSinSource.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.name.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.name "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.name")  | Source name.  |  
| [`VoltageSinSource.phase_delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.phase_delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.phase_delay "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.phase_delay")  | Phase delay.  |  
| [`VoltageSinSource.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.public_dir.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.public_dir "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.public_dir")  | Shortcut for dir(self).  |  
| [`VoltageSinSource.tone`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.tone.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.tone "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.tone")  | Frequency to use for harmonic balance.  |  
| [`VoltageSinSource.voltage_amplitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.voltage_amplitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.voltage_amplitude "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.voltage_amplitude")  | Voltage amplitude.  |  
| [`VoltageSinSource.voltage_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.voltage_offset.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.voltage_offset "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.voltage_offset")  | Voltage offset from zero watts.  |  
# VoltageSinSource 

class ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _source_type =None_) 
    
Power Sinusoidal Class.
Examples

```
>>> from ansys.aedt.core.modules.boundary.circuit_boundary import VoltageSinSource
>>> import ansys.aedt.core as pyaedt
>>> app = pyaedt.Circuit()
>>> source = VoltageSinSource(app, name="V1")

```
Copy to clipboard
Methods  
| [`VoltageSinSource.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.create.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.create "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.create")()  | Create a new source in AEDT.  |  
| --- | --- |  
| [`VoltageSinSource.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.delete.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.delete "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.delete")()  | Delete the source in AEDT.  |  
| [`VoltageSinSource.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.update.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.update "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.update")([original_name, ...])  | Update the source in AEDT.  |  
Attributes  
| [`VoltageSinSource.ac_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.ac_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.ac_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.ac_magnitude")  | AC magnitude value.  |  
| --- | --- |  
| [`VoltageSinSource.ac_phase`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.ac_phase.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.ac_phase "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.ac_phase")  | AC phase value.  |  
| [`VoltageSinSource.damping_factor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.damping_factor.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.damping_factor "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.damping_factor")  | Damping factor.  |  
| [`VoltageSinSource.dc_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.dc_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.dc_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.dc_magnitude")  | DC voltage value.  |  
| [`VoltageSinSource.delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.delay "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.delay")  | Delay to start of sine wave.  |  
| [`VoltageSinSource.frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.frequency.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.frequency "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.frequency")  | Frequency.  |  
| [`VoltageSinSource.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.name.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.name "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.name")  | Source name.  |  
| [`VoltageSinSource.phase_delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.phase_delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.phase_delay "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.phase_delay")  | Phase delay.  |  
| [`VoltageSinSource.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.public_dir.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.public_dir "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.public_dir")  | Shortcut for dir(self).  |  
| [`VoltageSinSource.tone`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.tone.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.tone "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.tone")  | Frequency to use for harmonic balance.  |  
| [`VoltageSinSource.voltage_amplitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.voltage_amplitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.voltage_amplitude "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.voltage_amplitude")  | Voltage amplitude.  |  
| [`VoltageSinSource.voltage_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.voltage_offset.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.voltage_offset "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.voltage_offset")  | Voltage offset from zero watts.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.rst.txt)

# VoltageSinSource 

class ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _source_type =None_) 
    
Power Sinusoidal Class.
Examples

```
>>> from ansys.aedt.core.modules.boundary.circuit_boundary import VoltageSinSource
>>> import ansys.aedt.core as pyaedt
>>> app = pyaedt.Circuit()
>>> source = VoltageSinSource(app, name="V1")

```
Copy to clipboard
Methods  
| [`VoltageSinSource.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.create.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.create "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.create")()  | Create a new source in AEDT.  |  
| --- | --- |  
| [`VoltageSinSource.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.delete.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.delete "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.delete")()  | Delete the source in AEDT.  |  
| [`VoltageSinSource.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.update.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.update "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.update")([original_name, ...])  | Update the source in AEDT.  |  
Attributes  
| [`VoltageSinSource.ac_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.ac_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.ac_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.ac_magnitude")  | AC magnitude value.  |  
| --- | --- |  
| [`VoltageSinSource.ac_phase`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.ac_phase.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.ac_phase "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.ac_phase")  | AC phase value.  |  
| [`VoltageSinSource.damping_factor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.damping_factor.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.damping_factor "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.damping_factor")  | Damping factor.  |  
| [`VoltageSinSource.dc_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.dc_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.dc_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.dc_magnitude")  | DC voltage value.  |  
| [`VoltageSinSource.delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.delay "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.delay")  | Delay to start of sine wave.  |  
| [`VoltageSinSource.frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.frequency.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.frequency "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.frequency")  | Frequency.  |  
| [`VoltageSinSource.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.name.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.name "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.name")  | Source name.  |  
| [`VoltageSinSource.phase_delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.phase_delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.phase_delay "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.phase_delay")  | Phase delay.  |  
| [`VoltageSinSource.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.public_dir.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.public_dir "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.public_dir")  | Shortcut for dir(self).  |  
| [`VoltageSinSource.tone`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.tone.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.tone "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.tone")  | Frequency to use for harmonic balance.  |  
| [`VoltageSinSource.voltage_amplitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.voltage_amplitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.voltage_amplitude "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.voltage_amplitude")  | Voltage amplitude.  |  
| [`VoltageSinSource.voltage_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.voltage_offset.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.voltage_offset "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageSinSource.voltage_offset")  | Voltage offset from zero watts.  |