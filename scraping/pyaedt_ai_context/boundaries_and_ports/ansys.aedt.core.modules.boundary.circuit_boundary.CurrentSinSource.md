---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# CurrentSinSource 

class ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _source_type =None_) 
    
Current Sinusoidal Class.
Examples

```
>>> from ansys.aedt.core.modules.boundary.circuit_boundary import CurrentSinSource
>>> import ansys.aedt.core as pyaedt
>>> app = pyaedt.Circuit()
>>> source = CurrentSinSource(app, name="I1")

```
Copy to clipboard
Methods  
| [`CurrentSinSource.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.create.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.create "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.create")()  | Create a new source in AEDT.  |  
| --- | --- |  
| [`CurrentSinSource.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.delete.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.delete "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.delete")()  | Delete the source in AEDT.  |  
| [`CurrentSinSource.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.update.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.update "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.update")([original_name, ...])  | Update the source in AEDT.  |  
Attributes  
| [`CurrentSinSource.ac_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.ac_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.ac_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.ac_magnitude")  | AC magnitude value.  |  
| --- | --- |  
| [`CurrentSinSource.ac_phase`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.ac_phase.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.ac_phase "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.ac_phase")  | AC phase value.  |  
| [`CurrentSinSource.current_amplitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.current_amplitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.current_amplitude "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.current_amplitude")  | Current amplitude.  |  
| [`CurrentSinSource.current_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.current_offset.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.current_offset "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.current_offset")  | Current offset.  |  
| [`CurrentSinSource.damping_factor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.damping_factor.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.damping_factor "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.damping_factor")  | Damping factor.  |  
| [`CurrentSinSource.dc_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.dc_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.dc_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.dc_magnitude")  | DC current value.  |  
| [`CurrentSinSource.delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.delay "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.delay")  | Delay to start of sine wave.  |  
| [`CurrentSinSource.frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.frequency.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.frequency "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.frequency")  | Frequency.  |  
| [`CurrentSinSource.multiplier`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.multiplier.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.multiplier "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.multiplier")  | Multiplier for simulating multiple parallel current sources.  |  
| [`CurrentSinSource.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.name.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.name "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.name")  | Source name.  |  
| [`CurrentSinSource.phase_delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.phase_delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.phase_delay "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.phase_delay")  | Phase delay.  |  
| [`CurrentSinSource.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.public_dir.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.public_dir "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.public_dir")  | Shortcut for dir(self).  |  
| [`CurrentSinSource.tone`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.tone.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.tone "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.tone")  | Frequency to use for harmonic balance.  |  
# CurrentSinSource 

class ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _source_type =None_) 
    
Current Sinusoidal Class.
Examples

```
>>> from ansys.aedt.core.modules.boundary.circuit_boundary import CurrentSinSource
>>> import ansys.aedt.core as pyaedt
>>> app = pyaedt.Circuit()
>>> source = CurrentSinSource(app, name="I1")

```
Copy to clipboard
Methods  
| [`CurrentSinSource.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.create.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.create "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.create")()  | Create a new source in AEDT.  |  
| --- | --- |  
| [`CurrentSinSource.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.delete.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.delete "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.delete")()  | Delete the source in AEDT.  |  
| [`CurrentSinSource.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.update.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.update "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.update")([original_name, ...])  | Update the source in AEDT.  |  
Attributes  
| [`CurrentSinSource.ac_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.ac_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.ac_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.ac_magnitude")  | AC magnitude value.  |  
| --- | --- |  
| [`CurrentSinSource.ac_phase`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.ac_phase.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.ac_phase "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.ac_phase")  | AC phase value.  |  
| [`CurrentSinSource.current_amplitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.current_amplitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.current_amplitude "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.current_amplitude")  | Current amplitude.  |  
| [`CurrentSinSource.current_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.current_offset.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.current_offset "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.current_offset")  | Current offset.  |  
| [`CurrentSinSource.damping_factor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.damping_factor.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.damping_factor "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.damping_factor")  | Damping factor.  |  
| [`CurrentSinSource.dc_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.dc_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.dc_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.dc_magnitude")  | DC current value.  |  
| [`CurrentSinSource.delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.delay "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.delay")  | Delay to start of sine wave.  |  
| [`CurrentSinSource.frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.frequency.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.frequency "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.frequency")  | Frequency.  |  
| [`CurrentSinSource.multiplier`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.multiplier.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.multiplier "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.multiplier")  | Multiplier for simulating multiple parallel current sources.  |  
| [`CurrentSinSource.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.name.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.name "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.name")  | Source name.  |  
| [`CurrentSinSource.phase_delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.phase_delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.phase_delay "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.phase_delay")  | Phase delay.  |  
| [`CurrentSinSource.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.public_dir.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.public_dir "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.public_dir")  | Shortcut for dir(self).  |  
| [`CurrentSinSource.tone`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.tone.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.tone "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.tone")  | Frequency to use for harmonic balance.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.rst.txt)

# CurrentSinSource 

class ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _source_type =None_) 
    
Current Sinusoidal Class.
Examples

```
>>> from ansys.aedt.core.modules.boundary.circuit_boundary import CurrentSinSource
>>> import ansys.aedt.core as pyaedt
>>> app = pyaedt.Circuit()
>>> source = CurrentSinSource(app, name="I1")

```
Copy to clipboard
Methods  
| [`CurrentSinSource.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.create.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.create "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.create")()  | Create a new source in AEDT.  |  
| --- | --- |  
| [`CurrentSinSource.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.delete.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.delete "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.delete")()  | Delete the source in AEDT.  |  
| [`CurrentSinSource.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.update.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.update "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.update")([original_name, ...])  | Update the source in AEDT.  |  
Attributes  
| [`CurrentSinSource.ac_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.ac_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.ac_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.ac_magnitude")  | AC magnitude value.  |  
| --- | --- |  
| [`CurrentSinSource.ac_phase`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.ac_phase.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.ac_phase "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.ac_phase")  | AC phase value.  |  
| [`CurrentSinSource.current_amplitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.current_amplitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.current_amplitude "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.current_amplitude")  | Current amplitude.  |  
| [`CurrentSinSource.current_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.current_offset.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.current_offset "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.current_offset")  | Current offset.  |  
| [`CurrentSinSource.damping_factor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.damping_factor.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.damping_factor "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.damping_factor")  | Damping factor.  |  
| [`CurrentSinSource.dc_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.dc_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.dc_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.dc_magnitude")  | DC current value.  |  
| [`CurrentSinSource.delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.delay "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.delay")  | Delay to start of sine wave.  |  
| [`CurrentSinSource.frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.frequency.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.frequency "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.frequency")  | Frequency.  |  
| [`CurrentSinSource.multiplier`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.multiplier.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.multiplier "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.multiplier")  | Multiplier for simulating multiple parallel current sources.  |  
| [`CurrentSinSource.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.name.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.name "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.name")  | Source name.  |  
| [`CurrentSinSource.phase_delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.phase_delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.phase_delay "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.phase_delay")  | Phase delay.  |  
| [`CurrentSinSource.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.public_dir.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.public_dir "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.public_dir")  | Shortcut for dir(self).  |  
| [`CurrentSinSource.tone`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.tone.html#ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.tone "ansys.aedt.core.modules.boundary.circuit_boundary.CurrentSinSource.tone")  | Frequency to use for harmonic balance.  |