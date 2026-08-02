---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# PowerIQSource 

class ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _source_type =None_) 
    
Power IQ Class.
Examples

```
>>> import ansys.aedt.core as pyaedt
>>> from ansys.aedt.core.modules.boundary.circuit_boundary import PowerIQSource
>>> app = pyaedt.Circuit()
>>> source = PowerIQSource(app, name="IQ1")

```
Copy to clipboard
Methods  
| [`PowerIQSource.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.create.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.create "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.create")()  | Create a new source in AEDT.  |  
| --- | --- |  
| [`PowerIQSource.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.delete.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.delete "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.delete")()  | Delete the source in AEDT.  |  
| [`PowerIQSource.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.update.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.update "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.update")([original_name, new_source])  | Update the source in AEDT.  |  
Attributes  
| [`PowerIQSource.carrier_amplitude_power`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_amplitude_power.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_amplitude_power "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_amplitude_power")  | Carrier amplitude value, power-based.  |  
| --- | --- |  
| [`PowerIQSource.carrier_amplitude_voltage`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_amplitude_voltage.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_amplitude_voltage "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_amplitude_voltage")  | Carrier amplitude value, voltage-based.  |  
| [`PowerIQSource.carrier_frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_frequency.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_frequency "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_frequency")  | Carrier frequency value.  |  
| [`PowerIQSource.carrier_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_offset.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_offset "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_offset")  | Carrier offset.  |  
| [`PowerIQSource.damping_factor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.damping_factor.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.damping_factor "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.damping_factor")  | Damping factor.  |  
| [`PowerIQSource.dc_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.dc_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.dc_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.dc_magnitude")  | DC voltage value.  |  
| [`PowerIQSource.delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.delay "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.delay")  | Delay to start of sine wave.  |  
| [`PowerIQSource.file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.file.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.file "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.file")  | File path with I and Q values.  |  
| [`PowerIQSource.i_q_values`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.i_q_values.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.i_q_values "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.i_q_values")  | I and Q value at each timepoint.  |  
| [`PowerIQSource.imaginary_impedance`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.imaginary_impedance.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.imaginary_impedance "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.imaginary_impedance")  | Imaginary carrier impedance.  |  
| [`PowerIQSource.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.name.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.name "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.name")  | Source name.  |  
| [`PowerIQSource.phase_delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.phase_delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.phase_delay "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.phase_delay")  | Phase delay.  |  
| [`PowerIQSource.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.public_dir.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.public_dir "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.public_dir")  | Shortcut for dir(self).  |  
| [`PowerIQSource.real_impedance`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.real_impedance.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.real_impedance "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.real_impedance")  | Real carrier impedance.  |  
| [`PowerIQSource.repeat_from`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.repeat_from.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.repeat_from "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.repeat_from")  | Repeat from time.  |  
| [`PowerIQSource.sampling_time`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.sampling_time.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.sampling_time "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.sampling_time")  | Sampling time value.  |  
| [`PowerIQSource.tone`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.tone.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.tone "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.tone")  | Frequency to use for harmonic balance.  |  
# PowerIQSource 

class ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _source_type =None_) 
    
Power IQ Class.
Examples

```
>>> import ansys.aedt.core as pyaedt
>>> from ansys.aedt.core.modules.boundary.circuit_boundary import PowerIQSource
>>> app = pyaedt.Circuit()
>>> source = PowerIQSource(app, name="IQ1")

```
Copy to clipboard
Methods  
| [`PowerIQSource.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.create.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.create "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.create")()  | Create a new source in AEDT.  |  
| --- | --- |  
| [`PowerIQSource.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.delete.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.delete "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.delete")()  | Delete the source in AEDT.  |  
| [`PowerIQSource.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.update.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.update "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.update")([original_name, new_source])  | Update the source in AEDT.  |  
Attributes  
| [`PowerIQSource.carrier_amplitude_power`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_amplitude_power.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_amplitude_power "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_amplitude_power")  | Carrier amplitude value, power-based.  |  
| --- | --- |  
| [`PowerIQSource.carrier_amplitude_voltage`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_amplitude_voltage.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_amplitude_voltage "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_amplitude_voltage")  | Carrier amplitude value, voltage-based.  |  
| [`PowerIQSource.carrier_frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_frequency.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_frequency "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_frequency")  | Carrier frequency value.  |  
| [`PowerIQSource.carrier_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_offset.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_offset "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_offset")  | Carrier offset.  |  
| [`PowerIQSource.damping_factor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.damping_factor.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.damping_factor "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.damping_factor")  | Damping factor.  |  
| [`PowerIQSource.dc_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.dc_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.dc_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.dc_magnitude")  | DC voltage value.  |  
| [`PowerIQSource.delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.delay "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.delay")  | Delay to start of sine wave.  |  
| [`PowerIQSource.file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.file.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.file "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.file")  | File path with I and Q values.  |  
| [`PowerIQSource.i_q_values`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.i_q_values.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.i_q_values "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.i_q_values")  | I and Q value at each timepoint.  |  
| [`PowerIQSource.imaginary_impedance`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.imaginary_impedance.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.imaginary_impedance "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.imaginary_impedance")  | Imaginary carrier impedance.  |  
| [`PowerIQSource.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.name.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.name "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.name")  | Source name.  |  
| [`PowerIQSource.phase_delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.phase_delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.phase_delay "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.phase_delay")  | Phase delay.  |  
| [`PowerIQSource.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.public_dir.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.public_dir "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.public_dir")  | Shortcut for dir(self).  |  
| [`PowerIQSource.real_impedance`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.real_impedance.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.real_impedance "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.real_impedance")  | Real carrier impedance.  |  
| [`PowerIQSource.repeat_from`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.repeat_from.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.repeat_from "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.repeat_from")  | Repeat from time.  |  
| [`PowerIQSource.sampling_time`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.sampling_time.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.sampling_time "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.sampling_time")  | Sampling time value.  |  
| [`PowerIQSource.tone`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.tone.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.tone "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.tone")  | Frequency to use for harmonic balance.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.rst.txt)

# PowerIQSource 

class ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _source_type =None_) 
    
Power IQ Class.
Examples

```
>>> import ansys.aedt.core as pyaedt
>>> from ansys.aedt.core.modules.boundary.circuit_boundary import PowerIQSource
>>> app = pyaedt.Circuit()
>>> source = PowerIQSource(app, name="IQ1")

```
Copy to clipboard
Methods  
| [`PowerIQSource.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.create.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.create "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.create")()  | Create a new source in AEDT.  |  
| --- | --- |  
| [`PowerIQSource.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.delete.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.delete "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.delete")()  | Delete the source in AEDT.  |  
| [`PowerIQSource.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.update.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.update "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.update")([original_name, new_source])  | Update the source in AEDT.  |  
Attributes  
| [`PowerIQSource.carrier_amplitude_power`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_amplitude_power.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_amplitude_power "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_amplitude_power")  | Carrier amplitude value, power-based.  |  
| --- | --- |  
| [`PowerIQSource.carrier_amplitude_voltage`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_amplitude_voltage.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_amplitude_voltage "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_amplitude_voltage")  | Carrier amplitude value, voltage-based.  |  
| [`PowerIQSource.carrier_frequency`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_frequency.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_frequency "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_frequency")  | Carrier frequency value.  |  
| [`PowerIQSource.carrier_offset`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_offset.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_offset "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.carrier_offset")  | Carrier offset.  |  
| [`PowerIQSource.damping_factor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.damping_factor.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.damping_factor "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.damping_factor")  | Damping factor.  |  
| [`PowerIQSource.dc_magnitude`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.dc_magnitude.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.dc_magnitude "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.dc_magnitude")  | DC voltage value.  |  
| [`PowerIQSource.delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.delay "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.delay")  | Delay to start of sine wave.  |  
| [`PowerIQSource.file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.file.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.file "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.file")  | File path with I and Q values.  |  
| [`PowerIQSource.i_q_values`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.i_q_values.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.i_q_values "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.i_q_values")  | I and Q value at each timepoint.  |  
| [`PowerIQSource.imaginary_impedance`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.imaginary_impedance.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.imaginary_impedance "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.imaginary_impedance")  | Imaginary carrier impedance.  |  
| [`PowerIQSource.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.name.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.name "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.name")  | Source name.  |  
| [`PowerIQSource.phase_delay`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.phase_delay.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.phase_delay "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.phase_delay")  | Phase delay.  |  
| [`PowerIQSource.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.public_dir.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.public_dir "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.public_dir")  | Shortcut for dir(self).  |  
| [`PowerIQSource.real_impedance`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.real_impedance.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.real_impedance "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.real_impedance")  | Real carrier impedance.  |  
| [`PowerIQSource.repeat_from`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.repeat_from.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.repeat_from "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.repeat_from")  | Repeat from time.  |  
| [`PowerIQSource.sampling_time`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.sampling_time.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.sampling_time "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.sampling_time")  | Sampling time value.  |  
| [`PowerIQSource.tone`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.tone.html#ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.tone "ansys.aedt.core.modules.boundary.circuit_boundary.PowerIQSource.tone")  | Frequency to use for harmonic balance.  |