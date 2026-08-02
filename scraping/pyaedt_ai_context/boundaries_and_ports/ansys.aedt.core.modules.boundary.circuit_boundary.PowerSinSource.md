---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# PowerSinSource 

class ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _source_type =None_) 
    
Power Sinusoidal Class.
Examples

```
>>> import ansys.aedt.core as pyaedt
>>> from ansys.aedt.core.modules.boundary.circuit_boundary import PowerSinSource
>>> app = pyaedt.Circuit()
>>> source = PowerSinSource(app, name="P1")

```
Copy to clipboard
Methods  
| [`PowerSinSource.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.create.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.create "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.create")()  | Create a new source in AEDT.  |  
| --- | --- |  
| [`PowerSinSource.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.delete.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.delete "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.delete")()  | Delete the source in AEDT.  |  
| [`PowerSinSource.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.update.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.update "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.update")([original_name, ...])  | Update the source in AEDT.  |  
Attributes  
| [`PowerSinSource.ac_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.ac_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.ac_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.ac_magnitude")  | AC magnitude value.  |  
| --- | --- |  
| [`PowerSinSource.ac_phase`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.ac_phase.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.ac_phase "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.ac_phase")  | AC phase value.  |  
| [`PowerSinSource.damping_factor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.damping_factor.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.damping_factor "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.damping_factor")  | Damping factor.  |  
| [`PowerSinSource.dc_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.dc_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.dc_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.dc_magnitude")  | DC voltage value.  |  
| [`PowerSinSource.delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.delay "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.delay")  | Delay to start of sine wave.  |  
| [`PowerSinSource.frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.frequency.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.frequency "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.frequency")  | Frequency.  |  
| [`PowerSinSource.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.name.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.name "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.name")  | Source name.  |  
| [`PowerSinSource.phase_delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.phase_delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.phase_delay "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.phase_delay")  | Phase delay.  |  
| [`PowerSinSource.power_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.power_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.power_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.power_magnitude")  | Available power of the source above power offset.  |  
| [`PowerSinSource.power_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.power_offset.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.power_offset "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.power_offset")  | Power offset from zero watts.  |  
| [`PowerSinSource.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.public_dir.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.public_dir "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.public_dir")  | Shortcut for dir(self).  |  
| [`PowerSinSource.tone`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.tone.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.tone "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.tone")  | Frequency to use for harmonic balance.  |  
# PowerSinSource 

class ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _source_type =None_) 
    
Power Sinusoidal Class.
Examples

```
>>> import ansys.aedt.core as pyaedt
>>> from ansys.aedt.core.modules.boundary.circuit_boundary import PowerSinSource
>>> app = pyaedt.Circuit()
>>> source = PowerSinSource(app, name="P1")

```
Copy to clipboard
Methods  
| [`PowerSinSource.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.create.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.create "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.create")()  | Create a new source in AEDT.  |  
| --- | --- |  
| [`PowerSinSource.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.delete.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.delete "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.delete")()  | Delete the source in AEDT.  |  
| [`PowerSinSource.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.update.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.update "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.update")([original_name, ...])  | Update the source in AEDT.  |  
Attributes  
| [`PowerSinSource.ac_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.ac_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.ac_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.ac_magnitude")  | AC magnitude value.  |  
| --- | --- |  
| [`PowerSinSource.ac_phase`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.ac_phase.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.ac_phase "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.ac_phase")  | AC phase value.  |  
| [`PowerSinSource.damping_factor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.damping_factor.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.damping_factor "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.damping_factor")  | Damping factor.  |  
| [`PowerSinSource.dc_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.dc_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.dc_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.dc_magnitude")  | DC voltage value.  |  
| [`PowerSinSource.delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.delay "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.delay")  | Delay to start of sine wave.  |  
| [`PowerSinSource.frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.frequency.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.frequency "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.frequency")  | Frequency.  |  
| [`PowerSinSource.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.name.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.name "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.name")  | Source name.  |  
| [`PowerSinSource.phase_delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.phase_delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.phase_delay "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.phase_delay")  | Phase delay.  |  
| [`PowerSinSource.power_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.power_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.power_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.power_magnitude")  | Available power of the source above power offset.  |  
| [`PowerSinSource.power_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.power_offset.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.power_offset "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.power_offset")  | Power offset from zero watts.  |  
| [`PowerSinSource.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.public_dir.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.public_dir "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.public_dir")  | Shortcut for dir(self).  |  
| [`PowerSinSource.tone`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.tone.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.tone "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.tone")  | Frequency to use for harmonic balance.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.rst.txt)

# PowerSinSource 

class ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _source_type =None_) 
    
Power Sinusoidal Class.
Examples

```
>>> import ansys.aedt.core as pyaedt
>>> from ansys.aedt.core.modules.boundary.circuit_boundary import PowerSinSource
>>> app = pyaedt.Circuit()
>>> source = PowerSinSource(app, name="P1")

```
Copy to clipboard
Methods  
| [`PowerSinSource.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.create.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.create "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.create")()  | Create a new source in AEDT.  |  
| --- | --- |  
| [`PowerSinSource.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.delete.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.delete "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.delete")()  | Delete the source in AEDT.  |  
| [`PowerSinSource.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.update.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.update "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.update")([original_name, ...])  | Update the source in AEDT.  |  
Attributes  
| [`PowerSinSource.ac_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.ac_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.ac_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.ac_magnitude")  | AC magnitude value.  |  
| --- | --- |  
| [`PowerSinSource.ac_phase`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.ac_phase.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.ac_phase "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.ac_phase")  | AC phase value.  |  
| [`PowerSinSource.damping_factor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.damping_factor.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.damping_factor "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.damping_factor")  | Damping factor.  |  
| [`PowerSinSource.dc_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.dc_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.dc_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.dc_magnitude")  | DC voltage value.  |  
| [`PowerSinSource.delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.delay "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.delay")  | Delay to start of sine wave.  |  
| [`PowerSinSource.frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.frequency.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.frequency "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.frequency")  | Frequency.  |  
| [`PowerSinSource.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.name.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.name "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.name")  | Source name.  |  
| [`PowerSinSource.phase_delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.phase_delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.phase_delay "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.phase_delay")  | Phase delay.  |  
| [`PowerSinSource.power_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.power_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.power_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.power_magnitude")  | Available power of the source above power offset.  |  
| [`PowerSinSource.power_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.power_offset.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.power_offset "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.power_offset")  | Power offset from zero watts.  |  
| [`PowerSinSource.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.public_dir.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.public_dir "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.public_dir")  | Shortcut for dir(self).  |  
| [`PowerSinSource.tone`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.tone.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.tone "ansys.aedt.core.modules.boundary.circuit_boundary.PowerSinSource.tone")  | Frequency to use for harmonic balance.  |