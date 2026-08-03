---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# SimulationProfile 

class ansys.aedt.core.modules.profile.SimulationProfile(_group_data : [BinaryTreeNode](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode")_) 
    
Container for all profile data from a single simulation.
This class parses a _Solution Process Group_ and exposes convenience accessors for common metrics such as times, memory, passes, sweeps and transient steps. 

Parameters: 
     

**group_data** class:ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode 
     

**Root node of a solution process group.**
    
Examples

```
>>> from ansys.aedt.core.modules.profile import SimulationProfile
>>> obj = SimulationProfile()

```
Copy to clipboard
Methods  
| [`SimulationProfile.cpu_time`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.cpu_time.html#ansys.aedt.core.modules.profile.SimulationProfile.cpu_time "ansys.aedt.core.modules.profile.SimulationProfile.cpu_time")([num_passes, ...])  | Total CPU time for adaptive refinement or transient simulations.  |  
| --- | --- |  
| [`SimulationProfile.max_memory`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.max_memory.html#ansys.aedt.core.modules.profile.SimulationProfile.max_memory "ansys.aedt.core.modules.profile.SimulationProfile.max_memory")([num_passes])  | Maximum memory used in the solve process.  |  
| [`SimulationProfile.real_time`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.real_time.html#ansys.aedt.core.modules.profile.SimulationProfile.real_time "ansys.aedt.core.modules.profile.SimulationProfile.real_time")([num_passes, ...])  | Total real time for adaptive refinement or transient simulations.  |  
| [`SimulationProfile.time_keys`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.time_keys.html#ansys.aedt.core.modules.profile.SimulationProfile.time_keys "ansys.aedt.core.modules.profile.SimulationProfile.time_keys")(max_time)  | Return labels for transient steps not exceeding `max_time`.  |  
Attributes  
| [`SimulationProfile.has_frequency_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.has_frequency_sweep.html#ansys.aedt.core.modules.profile.SimulationProfile.has_frequency_sweep "ansys.aedt.core.modules.profile.SimulationProfile.has_frequency_sweep")  | Frequency sweep available.  |  
| --- | --- |  
| [`SimulationProfile.is_transient`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.is_transient.html#ansys.aedt.core.modules.profile.SimulationProfile.is_transient "ansys.aedt.core.modules.profile.SimulationProfile.is_transient")  | Transient profile is available.  |  
| [`SimulationProfile.max_time`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.max_time.html#ansys.aedt.core.modules.profile.SimulationProfile.max_time "ansys.aedt.core.modules.profile.SimulationProfile.max_time")  | Maximum transient time in seconds.  |  
| [`SimulationProfile.num_adaptive_passes`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.num_adaptive_passes.html#ansys.aedt.core.modules.profile.SimulationProfile.num_adaptive_passes "ansys.aedt.core.modules.profile.SimulationProfile.num_adaptive_passes")  | Number of adaptive passes available.  |  
| [`SimulationProfile.product`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.product.html#ansys.aedt.core.modules.profile.SimulationProfile.product "ansys.aedt.core.modules.profile.SimulationProfile.product")  | Product name parsed from the `Product` field.  |  
| [`SimulationProfile.product_version`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.product_version.html#ansys.aedt.core.modules.profile.SimulationProfile.product_version "ansys.aedt.core.modules.profile.SimulationProfile.product_version")  | Product version string parsed from `Product`.  |  
| [`SimulationProfile.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.public_dir.html#ansys.aedt.core.modules.profile.SimulationProfile.public_dir "ansys.aedt.core.modules.profile.SimulationProfile.public_dir")  | Shortcut for dir(self).  |  
| [`SimulationProfile.time_steps`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.time_steps.html#ansys.aedt.core.modules.profile.SimulationProfile.time_steps "ansys.aedt.core.modules.profile.SimulationProfile.time_steps")  | List of transient time steps.  |  
# SimulationProfile 

class ansys.aedt.core.modules.profile.SimulationProfile(_group_data : [BinaryTreeNode](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode")_) 
    
Container for all profile data from a single simulation.
This class parses a _Solution Process Group_ and exposes convenience accessors for common metrics such as times, memory, passes, sweeps and transient steps. 

Parameters: 
     

**group_data** class:ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode 
     

**Root node of a solution process group.**
    
Examples

```
>>> from ansys.aedt.core.modules.profile import SimulationProfile
>>> obj = SimulationProfile()

```
Copy to clipboard
Methods  
| [`SimulationProfile.cpu_time`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.cpu_time.html#ansys.aedt.core.modules.profile.SimulationProfile.cpu_time "ansys.aedt.core.modules.profile.SimulationProfile.cpu_time")([num_passes, ...])  | Total CPU time for adaptive refinement or transient simulations.  |  
| --- | --- |  
| [`SimulationProfile.max_memory`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.max_memory.html#ansys.aedt.core.modules.profile.SimulationProfile.max_memory "ansys.aedt.core.modules.profile.SimulationProfile.max_memory")([num_passes])  | Maximum memory used in the solve process.  |  
| [`SimulationProfile.real_time`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.real_time.html#ansys.aedt.core.modules.profile.SimulationProfile.real_time "ansys.aedt.core.modules.profile.SimulationProfile.real_time")([num_passes, ...])  | Total real time for adaptive refinement or transient simulations.  |  
| [`SimulationProfile.time_keys`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.time_keys.html#ansys.aedt.core.modules.profile.SimulationProfile.time_keys "ansys.aedt.core.modules.profile.SimulationProfile.time_keys")(max_time)  | Return labels for transient steps not exceeding `max_time`.  |  
Attributes  
| [`SimulationProfile.has_frequency_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.has_frequency_sweep.html#ansys.aedt.core.modules.profile.SimulationProfile.has_frequency_sweep "ansys.aedt.core.modules.profile.SimulationProfile.has_frequency_sweep")  | Frequency sweep available.  |  
| --- | --- |  
| [`SimulationProfile.is_transient`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.is_transient.html#ansys.aedt.core.modules.profile.SimulationProfile.is_transient "ansys.aedt.core.modules.profile.SimulationProfile.is_transient")  | Transient profile is available.  |  
| [`SimulationProfile.max_time`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.max_time.html#ansys.aedt.core.modules.profile.SimulationProfile.max_time "ansys.aedt.core.modules.profile.SimulationProfile.max_time")  | Maximum transient time in seconds.  |  
| [`SimulationProfile.num_adaptive_passes`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.num_adaptive_passes.html#ansys.aedt.core.modules.profile.SimulationProfile.num_adaptive_passes "ansys.aedt.core.modules.profile.SimulationProfile.num_adaptive_passes")  | Number of adaptive passes available.  |  
| [`SimulationProfile.product`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.product.html#ansys.aedt.core.modules.profile.SimulationProfile.product "ansys.aedt.core.modules.profile.SimulationProfile.product")  | Product name parsed from the `Product` field.  |  
| [`SimulationProfile.product_version`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.product_version.html#ansys.aedt.core.modules.profile.SimulationProfile.product_version "ansys.aedt.core.modules.profile.SimulationProfile.product_version")  | Product version string parsed from `Product`.  |  
| [`SimulationProfile.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.public_dir.html#ansys.aedt.core.modules.profile.SimulationProfile.public_dir "ansys.aedt.core.modules.profile.SimulationProfile.public_dir")  | Shortcut for dir(self).  |  
| [`SimulationProfile.time_steps`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.time_steps.html#ansys.aedt.core.modules.profile.SimulationProfile.time_steps "ansys.aedt.core.modules.profile.SimulationProfile.time_steps")  | List of transient time steps.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.rst.txt)

# SimulationProfile 

class ansys.aedt.core.modules.profile.SimulationProfile(_group_data : [BinaryTreeNode](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode.html#ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode "ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode")_) 
    
Container for all profile data from a single simulation.
This class parses a _Solution Process Group_ and exposes convenience accessors for common metrics such as times, memory, passes, sweeps and transient steps. 

Parameters: 
     

**group_data** class:ansys.aedt.core.modeler.cad.elements_3d.BinaryTreeNode 
     

**Root node of a solution process group.**
    
Examples

```
>>> from ansys.aedt.core.modules.profile import SimulationProfile
>>> obj = SimulationProfile()

```
Copy to clipboard
Methods  
| [`SimulationProfile.cpu_time`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.cpu_time.html#ansys.aedt.core.modules.profile.SimulationProfile.cpu_time "ansys.aedt.core.modules.profile.SimulationProfile.cpu_time")([num_passes, ...])  | Total CPU time for adaptive refinement or transient simulations.  |  
| --- | --- |  
| [`SimulationProfile.max_memory`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.max_memory.html#ansys.aedt.core.modules.profile.SimulationProfile.max_memory "ansys.aedt.core.modules.profile.SimulationProfile.max_memory")([num_passes])  | Maximum memory used in the solve process.  |  
| [`SimulationProfile.real_time`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.real_time.html#ansys.aedt.core.modules.profile.SimulationProfile.real_time "ansys.aedt.core.modules.profile.SimulationProfile.real_time")([num_passes, ...])  | Total real time for adaptive refinement or transient simulations.  |  
| [`SimulationProfile.time_keys`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.time_keys.html#ansys.aedt.core.modules.profile.SimulationProfile.time_keys "ansys.aedt.core.modules.profile.SimulationProfile.time_keys")(max_time)  | Return labels for transient steps not exceeding `max_time`.  |  
Attributes  
| [`SimulationProfile.has_frequency_sweep`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.has_frequency_sweep.html#ansys.aedt.core.modules.profile.SimulationProfile.has_frequency_sweep "ansys.aedt.core.modules.profile.SimulationProfile.has_frequency_sweep")  | Frequency sweep available.  |  
| --- | --- |  
| [`SimulationProfile.is_transient`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.is_transient.html#ansys.aedt.core.modules.profile.SimulationProfile.is_transient "ansys.aedt.core.modules.profile.SimulationProfile.is_transient")  | Transient profile is available.  |  
| [`SimulationProfile.max_time`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.max_time.html#ansys.aedt.core.modules.profile.SimulationProfile.max_time "ansys.aedt.core.modules.profile.SimulationProfile.max_time")  | Maximum transient time in seconds.  |  
| [`SimulationProfile.num_adaptive_passes`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.num_adaptive_passes.html#ansys.aedt.core.modules.profile.SimulationProfile.num_adaptive_passes "ansys.aedt.core.modules.profile.SimulationProfile.num_adaptive_passes")  | Number of adaptive passes available.  |  
| [`SimulationProfile.product`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.product.html#ansys.aedt.core.modules.profile.SimulationProfile.product "ansys.aedt.core.modules.profile.SimulationProfile.product")  | Product name parsed from the `Product` field.  |  
| [`SimulationProfile.product_version`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.product_version.html#ansys.aedt.core.modules.profile.SimulationProfile.product_version "ansys.aedt.core.modules.profile.SimulationProfile.product_version")  | Product version string parsed from `Product`.  |  
| [`SimulationProfile.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.public_dir.html#ansys.aedt.core.modules.profile.SimulationProfile.public_dir "ansys.aedt.core.modules.profile.SimulationProfile.public_dir")  | Shortcut for dir(self).  |  
| [`SimulationProfile.time_steps`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.SimulationProfile.time_steps.html#ansys.aedt.core.modules.profile.SimulationProfile.time_steps "ansys.aedt.core.modules.profile.SimulationProfile.time_steps")  | List of transient time steps.  |