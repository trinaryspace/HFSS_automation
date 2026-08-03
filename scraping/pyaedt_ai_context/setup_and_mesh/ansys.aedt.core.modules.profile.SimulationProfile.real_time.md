---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.real_time.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# real_time 

SimulationProfile.real_time(_num_passes : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _max_time : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [timedelta](https://docs.python.org/3.11/library/datetime.html#datetime.timedelta "\(in Python v3.11\)") 
    
Total real time for adaptive refinement or transient simulations.
> The total real time is calculated as the sum of execution time from all solution process steps. By default, all adaptive passes (for adaptive refinement) or all time steps are included in the result. In contrast to “CPU time”, the “Real time” represents the actual compute time for processes when they are distributed among multiple cores. 

Parameters: 
     

**num_passes**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Only valid when adaptive refinement is used. Number of passes to include in the time calculation. If nothing is passed, then all passes will be used. 

**max_time**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Maximum time step value in seconds to be considered for the sum of compute time. For example, if the total simulated transient time is 100 ms, then `max_time=0.05` will include only time steps up to 500 ms. If nothing is passed, then all time steps will be used. 

Returns: 
     

[`datetime.timedelta`](https://docs.python.org/3.11/library/datetime.html#datetime.timedelta "\(in Python v3.11\)")
     

`Total` `simulation` [`time`](https://docs.python.org/3.11/library/time.html#module-time "\(in Python v3.11\)") `for` `adaptive` `refinement` or `transient` simulation,
     

`excluding` pre-processing `and` `mesh` generation.
    
Examples

```
>>> from ansys.aedt.core.modules.profile import SimulationProfile
>>> obj = SimulationProfile()
>>> obj.real_time(num_passes=[1, 2, 3], max_time=1.0)

```
Copy to clipboard
# real_time 

SimulationProfile.real_time(_num_passes : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _max_time : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [timedelta](https://docs.python.org/3.11/library/datetime.html#datetime.timedelta "\(in Python v3.11\)") 
    
Total real time for adaptive refinement or transient simulations.
> The total real time is calculated as the sum of execution time from all solution process steps. By default, all adaptive passes (for adaptive refinement) or all time steps are included in the result. In contrast to “CPU time”, the “Real time” represents the actual compute time for processes when they are distributed among multiple cores. 

Parameters: 
     

**num_passes**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Only valid when adaptive refinement is used. Number of passes to include in the time calculation. If nothing is passed, then all passes will be used. 

**max_time**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Maximum time step value in seconds to be considered for the sum of compute time. For example, if the total simulated transient time is 100 ms, then `max_time=0.05` will include only time steps up to 500 ms. If nothing is passed, then all time steps will be used. 

Returns: 
     

[`datetime.timedelta`](https://docs.python.org/3.11/library/datetime.html#datetime.timedelta "\(in Python v3.11\)")
     

`Total` `simulation` [`time`](https://docs.python.org/3.11/library/time.html#module-time "\(in Python v3.11\)") `for` `adaptive` `refinement` or `transient` simulation,
     

`excluding` pre-processing `and` `mesh` generation.
    
Examples

```
>>> from ansys.aedt.core.modules.profile import SimulationProfile
>>> obj = SimulationProfile()
>>> obj.real_time(num_passes=[1, 2, 3], max_time=1.0)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.real_time.rst.txt)

# real_time 

SimulationProfile.real_time(_num_passes : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") = None_, _max_time : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") = None_) → [timedelta](https://docs.python.org/3.11/library/datetime.html#datetime.timedelta "\(in Python v3.11\)") 
    
Total real time for adaptive refinement or transient simulations.
> The total real time is calculated as the sum of execution time from all solution process steps. By default, all adaptive passes (for adaptive refinement) or all time steps are included in the result. In contrast to “CPU time”, the “Real time” represents the actual compute time for processes when they are distributed among multiple cores. 

Parameters: 
     

**num_passes**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Only valid when adaptive refinement is used. Number of passes to include in the time calculation. If nothing is passed, then all passes will be used. 

**max_time**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") 
    
Maximum time step value in seconds to be considered for the sum of compute time. For example, if the total simulated transient time is 100 ms, then `max_time=0.05` will include only time steps up to 500 ms. If nothing is passed, then all time steps will be used. 

Returns: 
     

[`datetime.timedelta`](https://docs.python.org/3.11/library/datetime.html#datetime.timedelta "\(in Python v3.11\)")
     

`Total` `simulation` [`time`](https://docs.python.org/3.11/library/time.html#module-time "\(in Python v3.11\)") `for` `adaptive` `refinement` or `transient` simulation,
     

`excluding` pre-processing `and` `mesh` generation.
    
Examples

```
>>> from ansys.aedt.core.modules.profile import SimulationProfile
>>> obj = SimulationProfile()
>>> obj.real_time(num_passes=[1, 2, 3], max_time=1.0)

```
Copy to clipboard