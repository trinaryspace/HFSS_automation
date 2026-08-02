---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.field_setups.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# field_setups 

property Hfss.field_setups 
    
List of AEDT radiation fields. 

Returns: 
     

`List` `of` [`ansys.aedt.core.modules.boundary.hfss_boundary.FarFieldSetup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.FarFieldSetup.html#ansys.aedt.core.modules.boundary.hfss_boundary.FarFieldSetup "ansys.aedt.core.modules.boundary.hfss_boundary.FarFieldSetup") `and` 
     

`ansys.aedt.core.modules.hfss_boundary.NearFieldSetup`
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.create_open_region()
>>> setups = hfss.field_setups
Edit start phi for the first field setup.
>>> hfss.field_setups[0].phi_start = 0

```
Copy to clipboard
# field_setups 

property Hfss.field_setups 
    
List of AEDT radiation fields. 

Returns: 
     

`List` `of` [`ansys.aedt.core.modules.boundary.hfss_boundary.FarFieldSetup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.FarFieldSetup.html#ansys.aedt.core.modules.boundary.hfss_boundary.FarFieldSetup "ansys.aedt.core.modules.boundary.hfss_boundary.FarFieldSetup") `and` 
     

`ansys.aedt.core.modules.hfss_boundary.NearFieldSetup`
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.create_open_region()
>>> setups = hfss.field_setups
Edit start phi for the first field setup.
>>> hfss.field_setups[0].phi_start = 0

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.field_setups.rst.txt)

# field_setups 

property Hfss.field_setups 
    
List of AEDT radiation fields. 

Returns: 
     

`List` `of` [`ansys.aedt.core.modules.boundary.hfss_boundary.FarFieldSetup`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.boundary.hfss_boundary.FarFieldSetup.html#ansys.aedt.core.modules.boundary.hfss_boundary.FarFieldSetup "ansys.aedt.core.modules.boundary.hfss_boundary.FarFieldSetup") `and` 
     

`ansys.aedt.core.modules.hfss_boundary.NearFieldSetup`
    
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.create_open_region()
>>> setups = hfss.field_setups
Edit start phi for the first field setup.
>>> hfss.field_setups[0].phi_start = 0

```
Copy to clipboard