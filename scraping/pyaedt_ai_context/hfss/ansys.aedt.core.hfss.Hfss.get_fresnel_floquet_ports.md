---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.get_fresnel_floquet_ports.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# get_fresnel_floquet_ports 

Hfss.get_fresnel_floquet_ports() → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Identify and validate Floquet ports from excitation names.
This method extracts port and mode information from the excitation names, checks that each port has exactly two modes, and identifies the top and bottom ports based on their bounding box Z-coordinate. The function supports only two Floquet ports. If more than two ports are defined or the mode conditions are not met, appropriate errors are logged. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
A list containing the names of the top and bottom Floquet ports, ordered by their Z-coordinate (top port first). If only one port is defined, it returns a list with that single port name.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> ports = hfss.get_fresnel_floquet_ports()

```
Copy to clipboard
# get_fresnel_floquet_ports 

Hfss.get_fresnel_floquet_ports() → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Identify and validate Floquet ports from excitation names.
This method extracts port and mode information from the excitation names, checks that each port has exactly two modes, and identifies the top and bottom ports based on their bounding box Z-coordinate. The function supports only two Floquet ports. If more than two ports are defined or the mode conditions are not met, appropriate errors are logged. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
A list containing the names of the top and bottom Floquet ports, ordered by their Z-coordinate (top port first). If only one port is defined, it returns a list with that single port name.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> ports = hfss.get_fresnel_floquet_ports()

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.get_fresnel_floquet_ports.rst.txt)

# get_fresnel_floquet_ports 

Hfss.get_fresnel_floquet_ports() → [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)")[[str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")] 
    
Identify and validate Floquet ports from excitation names.
This method extracts port and mode information from the excitation names, checks that each port has exactly two modes, and identifies the top and bottom ports based on their bounding box Z-coordinate. The function supports only two Floquet ports. If more than two ports are defined or the mode conditions are not met, appropriate errors are logged. 

Returns: 
     

[`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") `of` [`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
A list containing the names of the top and bottom Floquet ports, ordered by their Z-coordinate (top port first). If only one port is defined, it returns a list with that single port name.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> ports = hfss.get_fresnel_floquet_ports()

```
Copy to clipboard