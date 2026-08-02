---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.html"
category: "boundaries_and_ports"
domain: "PyAEDT / HFSS"
---

# VoltageFrequencyDependentSource 

class ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _source_type =None_) 
    
Voltage Frequency Dependent Class.
Examples

```
>>> from ansys.aedt.core.modules.boundary.circuit_boundary import VoltageFrequencyDependentSource
>>> import ansys.aedt.core as pyaedt
>>> app = pyaedt.Circuit()
>>> source = VoltageFrequencyDependentSource(app, name="VFD1")

```
Copy to clipboard
Methods  
| [`VoltageFrequencyDependentSource.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.create.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.create "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.create")()  | Create a new source in AEDT.  |  
| --- | --- |  
| [`VoltageFrequencyDependentSource.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.delete.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.delete "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.delete")()  | Delete the source in AEDT.  |  
| [`VoltageFrequencyDependentSource.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.update.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.update "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.update")([...])  | Update the source in AEDT.  |  
Attributes  
| [`VoltageFrequencyDependentSource.fds_filename`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.fds_filename.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.fds_filename "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.fds_filename")  | FDS file path.  |  
| --- | --- |  
| [`VoltageFrequencyDependentSource.frequencies`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.frequencies.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.frequencies "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.frequencies")  | List of frequencies in `Hz`.  |  
| [`VoltageFrequencyDependentSource.magnitude_angle`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.magnitude_angle.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.magnitude_angle "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.magnitude_angle")  | Enable magnitude and angle data.  |  
| [`VoltageFrequencyDependentSource.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.name.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.name "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.name")  | Source name.  |  
| [`VoltageFrequencyDependentSource.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.public_dir.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.public_dir "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.public_dir")  | Shortcut for dir(self).  |  
| [`VoltageFrequencyDependentSource.vang`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vang.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vang "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vang")  | List of angles in `rad`.  |  
| [`VoltageFrequencyDependentSource.vimag`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vimag.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vimag "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vimag")  | List of imaginary values in `V`.  |  
| [`VoltageFrequencyDependentSource.vmag`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vmag.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vmag "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vmag")  | List of magnitudes in `V`.  |  
| [`VoltageFrequencyDependentSource.vreal`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vreal.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vreal "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vreal")  | List of real values in `V`.  |  
# VoltageFrequencyDependentSource 

class ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _source_type =None_) 
    
Voltage Frequency Dependent Class.
Examples

```
>>> from ansys.aedt.core.modules.boundary.circuit_boundary import VoltageFrequencyDependentSource
>>> import ansys.aedt.core as pyaedt
>>> app = pyaedt.Circuit()
>>> source = VoltageFrequencyDependentSource(app, name="VFD1")

```
Copy to clipboard
Methods  
| [`VoltageFrequencyDependentSource.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.create.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.create "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.create")()  | Create a new source in AEDT.  |  
| --- | --- |  
| [`VoltageFrequencyDependentSource.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.delete.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.delete "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.delete")()  | Delete the source in AEDT.  |  
| [`VoltageFrequencyDependentSource.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.update.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.update "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.update")([...])  | Update the source in AEDT.  |  
Attributes  
| [`VoltageFrequencyDependentSource.fds_filename`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.fds_filename.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.fds_filename "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.fds_filename")  | FDS file path.  |  
| --- | --- |  
| [`VoltageFrequencyDependentSource.frequencies`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.frequencies.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.frequencies "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.frequencies")  | List of frequencies in `Hz`.  |  
| [`VoltageFrequencyDependentSource.magnitude_angle`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.magnitude_angle.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.magnitude_angle "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.magnitude_angle")  | Enable magnitude and angle data.  |  
| [`VoltageFrequencyDependentSource.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.name.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.name "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.name")  | Source name.  |  
| [`VoltageFrequencyDependentSource.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.public_dir.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.public_dir "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.public_dir")  | Shortcut for dir(self).  |  
| [`VoltageFrequencyDependentSource.vang`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vang.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vang "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vang")  | List of angles in `rad`.  |  
| [`VoltageFrequencyDependentSource.vimag`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vimag.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vimag "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vimag")  | List of imaginary values in `V`.  |  
| [`VoltageFrequencyDependentSource.vmag`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vmag.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vmag "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vmag")  | List of magnitudes in `V`.  |  
| [`VoltageFrequencyDependentSource.vreal`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vreal.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vreal "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vreal")  | List of real values in `V`.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.rst.txt)

# VoltageFrequencyDependentSource 

class ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource(_app_ , _name : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _source_type =None_) 
    
Voltage Frequency Dependent Class.
Examples

```
>>> from ansys.aedt.core.modules.boundary.circuit_boundary import VoltageFrequencyDependentSource
>>> import ansys.aedt.core as pyaedt
>>> app = pyaedt.Circuit()
>>> source = VoltageFrequencyDependentSource(app, name="VFD1")

```
Copy to clipboard
Methods  
| [`VoltageFrequencyDependentSource.create`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.create.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.create "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.create")()  | Create a new source in AEDT.  |  
| --- | --- |  
| [`VoltageFrequencyDependentSource.delete`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.delete.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.delete "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.delete")()  | Delete the source in AEDT.  |  
| [`VoltageFrequencyDependentSource.update`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.update.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.update "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.update")([...])  | Update the source in AEDT.  |  
Attributes  
| [`VoltageFrequencyDependentSource.fds_filename`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.fds_filename.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.fds_filename "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.fds_filename")  | FDS file path.  |  
| --- | --- |  
| [`VoltageFrequencyDependentSource.frequencies`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.frequencies.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.frequencies "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.frequencies")  | List of frequencies in `Hz`.  |  
| [`VoltageFrequencyDependentSource.magnitude_angle`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.magnitude_angle.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.magnitude_angle "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.magnitude_angle")  | Enable magnitude and angle data.  |  
| [`VoltageFrequencyDependentSource.name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.name.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.name "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.name")  | Source name.  |  
| [`VoltageFrequencyDependentSource.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.public_dir.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.public_dir "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.public_dir")  | Shortcut for dir(self).  |  
| [`VoltageFrequencyDependentSource.vang`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vang.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vang "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vang")  | List of angles in `rad`.  |  
| [`VoltageFrequencyDependentSource.vimag`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vimag.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vimag "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vimag")  | List of imaginary values in `V`.  |  
| [`VoltageFrequencyDependentSource.vmag`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vmag.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vmag "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vmag")  | List of magnitudes in `V`.  |  
| [`VoltageFrequencyDependentSource.vreal`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vreal.html#ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vreal "ansys.aedt.core.modules.boundary.circuit_boundary.VoltageFrequencyDependentSource.vreal")  | List of real values in `V`.  |