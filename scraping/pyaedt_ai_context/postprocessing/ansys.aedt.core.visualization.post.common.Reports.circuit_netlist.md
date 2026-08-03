---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.circuit_netlist.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# circuit_netlist 

Reports.circuit_netlist(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _domain : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → CircuitNetlistReport 
    
Create a Circuit Netlist Report object. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the analysis type. Specify the name of the analysis as listed in `ansys.aedt.core.generic.aedt_constants.CircuitNetlistConstants`. 

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more expressions to add into the report. 

**domain**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Domain of the report. The default is `None`, in which case the domain is set to `"Sweep"` or `"Time"` for transient analysis. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.netlist.CircuitNetlistReport`
    
Examples
Initialize Circuit Netlist. >>> from ansys.aedt.core import CircuitNetlist >>> cir = CircuitNetlist(version=”2026.1”) Create a report object (not in AEDT) for a transient analysis. >>> new_report = cir.post.reports_by_category.circuit_netlist( … expressions=”V(net_20,0)”, setup=”NexximTransient”, domain=”Time”, primary_sweep_variable=”Time” … ) Set time range for the report. >>> new_report.time_start = “0us” >>> new_report.time_stop = “10us” Create the report in AEDT. >>> assert new_report.create() >>> cir.release_desktop(False, False)
# circuit_netlist 

Reports.circuit_netlist(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _domain : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → CircuitNetlistReport 
    
Create a Circuit Netlist Report object. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the analysis type. Specify the name of the analysis as listed in `ansys.aedt.core.generic.aedt_constants.CircuitNetlistConstants`. 

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more expressions to add into the report. 

**domain**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Domain of the report. The default is `None`, in which case the domain is set to `"Sweep"` or `"Time"` for transient analysis. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.netlist.CircuitNetlistReport`
    
Examples
Initialize Circuit Netlist. >>> from ansys.aedt.core import CircuitNetlist >>> cir = CircuitNetlist(version=”2026.1”) Create a report object (not in AEDT) for a transient analysis. >>> new_report = cir.post.reports_by_category.circuit_netlist( … expressions=”V(net_20,0)”, setup=”NexximTransient”, domain=”Time”, primary_sweep_variable=”Time” … ) Set time range for the report. >>> new_report.time_start = “0us” >>> new_report.time_stop = “10us” Create the report in AEDT. >>> assert new_report.create() >>> cir.release_desktop(False, False)
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.common.Reports.circuit_netlist.rst.txt)

# circuit_netlist 

Reports.circuit_netlist(_setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")_, _expressions : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [list](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)") = None_, _domain : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") = None_) → CircuitNetlistReport 
    
Create a Circuit Netlist Report object. 

Parameters: 
     

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Name of the analysis type. Specify the name of the analysis as listed in `ansys.aedt.core.generic.aedt_constants.CircuitNetlistConstants`. 

**expressions**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`list`](https://docs.python.org/3.11/library/stdtypes.html#list "\(in Python v3.11\)"), `optional` 
    
One or more expressions to add into the report. 

**domain**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Domain of the report. The default is `None`, in which case the domain is set to `"Sweep"` or `"Time"` for transient analysis. 

Returns: 
     

`ansys.aedt.core.modules.report_templates.netlist.CircuitNetlistReport`
    
Examples
Initialize Circuit Netlist. >>> from ansys.aedt.core import CircuitNetlist >>> cir = CircuitNetlist(version=”2026.1”) Create a report object (not in AEDT) for a transient analysis. >>> new_report = cir.post.reports_by_category.circuit_netlist( … expressions=”V(net_20,0)”, setup=”NexximTransient”, domain=”Time”, primary_sweep_variable=”Time” … ) Set time range for the report. >>> new_report.time_start = “0us” >>> new_report.time_stop = “10us” Create the report in AEDT. >>> assert new_report.create() >>> cir.release_desktop(False, False)