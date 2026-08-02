---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.set_sbr_txrx_settings.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# set_sbr_txrx_settings 

Hfss.set_sbr_txrx_settings(_txrx_settings : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Set SBR+ TX RX antennas settings. 

Parameters: 
     

**txrx_settings**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary containing the TX as key and RX as values. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.SetSBRTxRxSettings

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.solution_type = "SBR+"
>>> par_beam = hfss.create_sbr_antenna(
...     hfss.SbrAntennas.ParametricBeam, parameters={"Polarization": "Horizontal"}, name="TX1"
... )
Only transmitter
>>> hfss.set_sbr_txrx_settings({"TX1_1_p1": "TX1_1_p1"})
Only receiver
>>> hfss.set_sbr_txrx_settings({"TX1_1_p1": "RX1_1_p1", "RX1_1_p1": "RX1_1_p1"})
Transmitter and receiver
>>> hfss.set_sbr_txrx_settings({"TX1_1_p1": "RX1_1_p1", "RX1_1_p1": "TX1_1_p1"})

```
Copy to clipboard
# set_sbr_txrx_settings 

Hfss.set_sbr_txrx_settings(_txrx_settings : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Set SBR+ TX RX antennas settings. 

Parameters: 
     

**txrx_settings**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary containing the TX as key and RX as values. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.SetSBRTxRxSettings

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.solution_type = "SBR+"
>>> par_beam = hfss.create_sbr_antenna(
...     hfss.SbrAntennas.ParametricBeam, parameters={"Polarization": "Horizontal"}, name="TX1"
... )
Only transmitter
>>> hfss.set_sbr_txrx_settings({"TX1_1_p1": "TX1_1_p1"})
Only receiver
>>> hfss.set_sbr_txrx_settings({"TX1_1_p1": "RX1_1_p1", "RX1_1_p1": "RX1_1_p1"})
Transmitter and receiver
>>> hfss.set_sbr_txrx_settings({"TX1_1_p1": "RX1_1_p1", "RX1_1_p1": "TX1_1_p1"})

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.set_sbr_txrx_settings.rst.txt)

# set_sbr_txrx_settings 

Hfss.set_sbr_txrx_settings(_txrx_settings : [dict](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)")_) → [BoundaryObject](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject") 
    
Set SBR+ TX RX antennas settings. 

Parameters: 
     

**txrx_settings**[`dict`](https://docs.python.org/3.11/library/stdtypes.html#dict "\(in Python v3.11\)") 
    
Dictionary containing the TX as key and RX as values. 

Returns: 
     

[`ansys.aedt.core.modules.boundary.common.BoundaryObject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.common.BoundaryObject.html#ansys.aedt.core.modules.boundary.common.BoundaryObject "ansys.aedt.core.modules.boundary.common.BoundaryObject")
    
Boundary object.
References

```
>>> oModule.SetSBRTxRxSettings

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.solution_type = "SBR+"
>>> par_beam = hfss.create_sbr_antenna(
...     hfss.SbrAntennas.ParametricBeam, parameters={"Polarization": "Horizontal"}, name="TX1"
... )
Only transmitter
>>> hfss.set_sbr_txrx_settings({"TX1_1_p1": "TX1_1_p1"})
Only receiver
>>> hfss.set_sbr_txrx_settings({"TX1_1_p1": "RX1_1_p1", "RX1_1_p1": "RX1_1_p1"})
Transmitter and receiver
>>> hfss.set_sbr_txrx_settings({"TX1_1_p1": "RX1_1_p1", "RX1_1_p1": "TX1_1_p1"})

```
Copy to clipboard