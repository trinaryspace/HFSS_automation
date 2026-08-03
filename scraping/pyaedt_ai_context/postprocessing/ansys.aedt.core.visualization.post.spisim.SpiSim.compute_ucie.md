---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.compute_ucie.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# compute_ucie 

SpiSim.compute_ucie(_tx_ports : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")]_, _rx_ports : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")]_, _victim_ports : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")]_, _tx_resistance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 30_, _tx_capacitance : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.2p'_, _rx_resistance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 50_, _rx_capacitance : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.2p'_, _packaging_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'standard'_, _data_rate : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'GTS04'_, _report_directory : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Universal Chiplet Interface Express (UCIe) Compliance support. 

Parameters: 
     

**tx_ports**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Transmitter port indexes. 

**rx_ports**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Receiver port indexes. 

**victim_ports**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Victim port indexes. 

**tx_resistance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Transmitter termination resistance parameter. 

**tx_capacitance**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Transmitter termination capacitance parameter. 

**rx_resistance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Receiver termination resistance parameter. 

**rx_capacitance**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Receiver termination capacitance parameter. 

**packaging_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of packaging. Available options are `standard` and `advanced`. 

**data_rate**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Data rate. Available options are `GTS04`, `GTS08`.,``GTS12``.``GTS16``.``GTS24``. and `GTS32`. 

**report_directory**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Directory to save report files.
Examples

```
>>> from ansys.aedt.core.visualization.post.spisim import SpiSim
>>> obj = SpiSim()
>>> obj.compute_ucie(tx_ports=[1, 2, 3], rx_ports=[1, 2, 3], victim_ports=[1, 2, 3])

```
Copy to clipboard
# compute_ucie 

SpiSim.compute_ucie(_tx_ports : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")]_, _rx_ports : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")]_, _victim_ports : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")]_, _tx_resistance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 30_, _tx_capacitance : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.2p'_, _rx_resistance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 50_, _rx_capacitance : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.2p'_, _packaging_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'standard'_, _data_rate : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'GTS04'_, _report_directory : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Universal Chiplet Interface Express (UCIe) Compliance support. 

Parameters: 
     

**tx_ports**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Transmitter port indexes. 

**rx_ports**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Receiver port indexes. 

**victim_ports**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Victim port indexes. 

**tx_resistance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Transmitter termination resistance parameter. 

**tx_capacitance**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Transmitter termination capacitance parameter. 

**rx_resistance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Receiver termination resistance parameter. 

**rx_capacitance**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Receiver termination capacitance parameter. 

**packaging_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of packaging. Available options are `standard` and `advanced`. 

**data_rate**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Data rate. Available options are `GTS04`, `GTS08`.,``GTS12``.``GTS16``.``GTS24``. and `GTS32`. 

**report_directory**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Directory to save report files.
Examples

```
>>> from ansys.aedt.core.visualization.post.spisim import SpiSim
>>> obj = SpiSim()
>>> obj.compute_ucie(tx_ports=[1, 2, 3], rx_ports=[1, 2, 3], victim_ports=[1, 2, 3])

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.spisim.SpiSim.compute_ucie.rst.txt)

# compute_ucie 

SpiSim.compute_ucie(_tx_ports : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")]_, _rx_ports : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")]_, _victim_ports : [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)")]_, _tx_resistance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 30_, _tx_capacitance : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.2p'_, _rx_resistance : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 50_, _rx_capacitance : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = '0.2p'_, _packaging_type : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'standard'_, _data_rate : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = 'GTS04'_, _report_directory : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Universal Chiplet Interface Express (UCIe) Compliance support. 

Parameters: 
     

**tx_ports**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Transmitter port indexes. 

**rx_ports**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Receiver port indexes. 

**victim_ports**[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") 
    
Victim port indexes. 

**tx_resistance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Transmitter termination resistance parameter. 

**tx_capacitance**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Transmitter termination capacitance parameter. 

**rx_resistance**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Receiver termination resistance parameter. 

**rx_capacitance**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Receiver termination capacitance parameter. 

**packaging_type**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Type of packaging. Available options are `standard` and `advanced`. 

**data_rate**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Data rate. Available options are `GTS04`, `GTS08`.,``GTS12``.``GTS16``.``GTS24``. and `GTS32`. 

**report_directory**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Directory to save report files.
Examples

```
>>> from ansys.aedt.core.visualization.post.spisim import SpiSim
>>> obj = SpiSim()
>>> obj.compute_ucie(tx_ports=[1, 2, 3], rx_ports=[1, 2, 3], victim_ports=[1, 2, 3])

```
Copy to clipboard