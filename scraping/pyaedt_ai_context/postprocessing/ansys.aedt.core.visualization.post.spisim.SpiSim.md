---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# SpiSim 

class ansys.aedt.core.visualization.post.spisim.SpiSim(_touchstone_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) 
    
Provides support to SpiSim batch mode.
Examples

```
>>> from ansys.aedt.core.visualization.post.spisim import SpiSim
>>> obj = SpiSim()

```
Copy to clipboard
Methods  
| [`SpiSim.compute_com`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.compute_com.html#ansys.aedt.core.visualization.post.spisim.SpiSim.compute_com "ansys.aedt.core.visualization.post.spisim.SpiSim.compute_com")([standard, config_file, ...])  | Compute Channel Operating Margin.  |  
| --- | --- |  
| [`SpiSim.compute_erl`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.compute_erl.html#ansys.aedt.core.visualization.post.spisim.SpiSim.compute_erl "ansys.aedt.core.visualization.post.spisim.SpiSim.compute_erl")([config_file, ...])  | Compute effective return loss (ERL) using Ansys SPISIM from S-parameter file.  |  
| [`SpiSim.compute_icn`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.compute_icn.html#ansys.aedt.core.visualization.post.spisim.SpiSim.compute_icn "ansys.aedt.core.visualization.post.spisim.SpiSim.compute_icn")([config_file, ...])  | Compute the integrated crosstalk noise (ICN) in volts using Ansys SPISIM from S-parameter file.  |  
| [`SpiSim.compute_ucie`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.compute_ucie.html#ansys.aedt.core.visualization.post.spisim.SpiSim.compute_ucie "ansys.aedt.core.visualization.post.spisim.SpiSim.compute_ucie")(tx_ports, rx_ports, ...)  | Universal Chiplet Interface Express (UCIe) Compliance support.  |  
| [`SpiSim.export_com_configure_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.export_com_configure_file.html#ansys.aedt.core.visualization.post.spisim.SpiSim.export_com_configure_file "ansys.aedt.core.visualization.post.spisim.SpiSim.export_com_configure_file")(file_path)  | Generate a configuration file for SpiSim.  |  
Attributes  
| [`SpiSim.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.public_dir.html#ansys.aedt.core.visualization.post.spisim.SpiSim.public_dir "ansys.aedt.core.visualization.post.spisim.SpiSim.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |  
| [`SpiSim.working_directory`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.working_directory.html#ansys.aedt.core.visualization.post.spisim.SpiSim.working_directory "ansys.aedt.core.visualization.post.spisim.SpiSim.working_directory")  | Working directory.  |  
# SpiSim 

class ansys.aedt.core.visualization.post.spisim.SpiSim(_touchstone_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) 
    
Provides support to SpiSim batch mode.
Examples

```
>>> from ansys.aedt.core.visualization.post.spisim import SpiSim
>>> obj = SpiSim()

```
Copy to clipboard
Methods  
| [`SpiSim.compute_com`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.compute_com.html#ansys.aedt.core.visualization.post.spisim.SpiSim.compute_com "ansys.aedt.core.visualization.post.spisim.SpiSim.compute_com")([standard, config_file, ...])  | Compute Channel Operating Margin.  |  
| --- | --- |  
| [`SpiSim.compute_erl`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.compute_erl.html#ansys.aedt.core.visualization.post.spisim.SpiSim.compute_erl "ansys.aedt.core.visualization.post.spisim.SpiSim.compute_erl")([config_file, ...])  | Compute effective return loss (ERL) using Ansys SPISIM from S-parameter file.  |  
| [`SpiSim.compute_icn`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.compute_icn.html#ansys.aedt.core.visualization.post.spisim.SpiSim.compute_icn "ansys.aedt.core.visualization.post.spisim.SpiSim.compute_icn")([config_file, ...])  | Compute the integrated crosstalk noise (ICN) in volts using Ansys SPISIM from S-parameter file.  |  
| [`SpiSim.compute_ucie`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.compute_ucie.html#ansys.aedt.core.visualization.post.spisim.SpiSim.compute_ucie "ansys.aedt.core.visualization.post.spisim.SpiSim.compute_ucie")(tx_ports, rx_ports, ...)  | Universal Chiplet Interface Express (UCIe) Compliance support.  |  
| [`SpiSim.export_com_configure_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.export_com_configure_file.html#ansys.aedt.core.visualization.post.spisim.SpiSim.export_com_configure_file "ansys.aedt.core.visualization.post.spisim.SpiSim.export_com_configure_file")(file_path)  | Generate a configuration file for SpiSim.  |  
Attributes  
| [`SpiSim.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.public_dir.html#ansys.aedt.core.visualization.post.spisim.SpiSim.public_dir "ansys.aedt.core.visualization.post.spisim.SpiSim.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |  
| [`SpiSim.working_directory`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.working_directory.html#ansys.aedt.core.visualization.post.spisim.SpiSim.working_directory "ansys.aedt.core.visualization.post.spisim.SpiSim.working_directory")  | Working directory.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.rst.txt)

# SpiSim 

class ansys.aedt.core.visualization.post.spisim.SpiSim(_touchstone_file : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = ''_) 
    
Provides support to SpiSim batch mode.
Examples

```
>>> from ansys.aedt.core.visualization.post.spisim import SpiSim
>>> obj = SpiSim()

```
Copy to clipboard
Methods  
| [`SpiSim.compute_com`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.compute_com.html#ansys.aedt.core.visualization.post.spisim.SpiSim.compute_com "ansys.aedt.core.visualization.post.spisim.SpiSim.compute_com")([standard, config_file, ...])  | Compute Channel Operating Margin.  |  
| --- | --- |  
| [`SpiSim.compute_erl`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.compute_erl.html#ansys.aedt.core.visualization.post.spisim.SpiSim.compute_erl "ansys.aedt.core.visualization.post.spisim.SpiSim.compute_erl")([config_file, ...])  | Compute effective return loss (ERL) using Ansys SPISIM from S-parameter file.  |  
| [`SpiSim.compute_icn`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.compute_icn.html#ansys.aedt.core.visualization.post.spisim.SpiSim.compute_icn "ansys.aedt.core.visualization.post.spisim.SpiSim.compute_icn")([config_file, ...])  | Compute the integrated crosstalk noise (ICN) in volts using Ansys SPISIM from S-parameter file.  |  
| [`SpiSim.compute_ucie`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.compute_ucie.html#ansys.aedt.core.visualization.post.spisim.SpiSim.compute_ucie "ansys.aedt.core.visualization.post.spisim.SpiSim.compute_ucie")(tx_ports, rx_ports, ...)  | Universal Chiplet Interface Express (UCIe) Compliance support.  |  
| [`SpiSim.export_com_configure_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.export_com_configure_file.html#ansys.aedt.core.visualization.post.spisim.SpiSim.export_com_configure_file "ansys.aedt.core.visualization.post.spisim.SpiSim.export_com_configure_file")(file_path)  | Generate a configuration file for SpiSim.  |  
Attributes  
| [`SpiSim.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.public_dir.html#ansys.aedt.core.visualization.post.spisim.SpiSim.public_dir "ansys.aedt.core.visualization.post.spisim.SpiSim.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |  
| [`SpiSim.working_directory`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.working_directory.html#ansys.aedt.core.visualization.post.spisim.SpiSim.working_directory "ansys.aedt.core.visualization.post.spisim.SpiSim.working_directory")  | Working directory.  |