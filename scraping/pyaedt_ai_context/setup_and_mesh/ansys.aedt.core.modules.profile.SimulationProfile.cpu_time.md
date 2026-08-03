---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.cpu_time.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# cpu_time 

SimulationProfile.cpu_time(_num_passes : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _max_time : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [timedelta](https://docs.python.org/3.11/library/datetime.html#datetime.timedelta "\(in Python v3.11\)") 
    
Total CPU time for adaptive refinement or transient simulations.
> The total CPU time is the sum of execution time for all solution process steps and cores. By default, all adaptive passes (for adaptive refinement) or all time steps (for transient simulation) are included in the return value. “CPU time” represents the time required for a process if it were run on a single core. The benefit of multicore processing can be estimated by the ratio between the `real_time` and the `cpu_time`. 

Parameters: 
     

**num_passes**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Only valid when adaptive refinement is used. Number of passes to include in the time calculation. If nothing is passed, then all passes will be used. 

**max_time**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Maximum time step value in seconds to be considered for the calculation of the compute time. For example, if the total simulated transient time is 100 ms, then passing `max_time=0.05` will include only time steps up to 500 ms. If nothing is passed, then all time steps will be considered. 

Returns: 
     

[`datetime.timedelta`](https://docs.python.org/3.11/library/datetime.html#datetime.timedelta "\(in Python v3.11\)")
    
Total simulation time for adaptive refinement or transient simulation.
Examples

```
>>> from ansys.aedt.core.modules.profile import SimulationProfile
>>> obj = SimulationProfile()
>>> obj.cpu_time(num_passes=[1, 2, 3], max_time=1.0)

```
Copy to clipboard
# cpu_time 

SimulationProfile.cpu_time(_num_passes : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _max_time : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [timedelta](https://docs.python.org/3.11/library/datetime.html#datetime.timedelta "\(in Python v3.11\)") 
    
Total CPU time for adaptive refinement or transient simulations.
> The total CPU time is the sum of execution time for all solution process steps and cores. By default, all adaptive passes (for adaptive refinement) or all time steps (for transient simulation) are included in the return value. “CPU time” represents the time required for a process if it were run on a single core. The benefit of multicore processing can be estimated by the ratio between the `real_time` and the `cpu_time`. 

Parameters: 
     

**num_passes**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Only valid when adaptive refinement is used. Number of passes to include in the time calculation. If nothing is passed, then all passes will be used. 

**max_time**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Maximum time step value in seconds to be considered for the calculation of the compute time. For example, if the total simulated transient time is 100 ms, then passing `max_time=0.05` will include only time steps up to 500 ms. If nothing is passed, then all time steps will be considered. 

Returns: 
     

[`datetime.timedelta`](https://docs.python.org/3.11/library/datetime.html#datetime.timedelta "\(in Python v3.11\)")
    
Total simulation time for adaptive refinement or transient simulation.
Examples

```
>>> from ansys.aedt.core.modules.profile import SimulationProfile
>>> obj = SimulationProfile()
>>> obj.cpu_time(num_passes=[1, 2, 3], max_time=1.0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.cpu_time.rst.txt)

# cpu_time 

SimulationProfile.cpu_time(_num_passes : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _max_time : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [timedelta](https://docs.python.org/3.11/library/datetime.html#datetime.timedelta "\(in Python v3.11\)") 
    
Total CPU time for adaptive refinement or transient simulations.
> The total CPU time is the sum of execution time for all solution process steps and cores. By default, all adaptive passes (for adaptive refinement) or all time steps (for transient simulation) are included in the return value. “CPU time” represents the time required for a process if it were run on a single core. The benefit of multicore processing can be estimated by the ratio between the `real_time` and the `cpu_time`. 

Parameters: 
     

**num_passes**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Only valid when adaptive refinement is used. Number of passes to include in the time calculation. If nothing is passed, then all passes will be used. 

**max_time**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Maximum time step value in seconds to be considered for the calculation of the compute time. For example, if the total simulated transient time is 100 ms, then passing `max_time=0.05` will include only time steps up to 500 ms. If nothing is passed, then all time steps will be considered. 

Returns: 
     

[`datetime.timedelta`](https://docs.python.org/3.11/library/datetime.html#datetime.timedelta "\(in Python v3.11\)")
    
Total simulation time for adaptive refinement or transient simulation.
Examples

```
>>> from ansys.aedt.core.modules.profile import SimulationProfile
>>> obj = SimulationProfile()
>>> obj.cpu_time(num_passes=[1, 2, 3], max_time=1.0)

```
Copy to clipboard