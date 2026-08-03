---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.Profiles.html"
category: "setup_and_mesh"
domain: "PyAEDT / HFSS"
---

# Profiles 

class ansys.aedt.core.modules.profile.Profiles(_profile_dict_) 
    
Provide an interface to solver profiles.
The Profiles class is iterable. Individual profiles are accessed via the unique key made up of “setup_name - variation”. If there are no variations available, the unique key is the setup name.
Examples
HFSS 3D Layout:

```
>>> app = Hfss3DLayout(project="solved_h3d_project")
>>> profiles = app.setups[0].get_profile()
>>> key_for_profile = list(profiles.keys())[0]
>>> print(key_for_profile)
'HFSS Setup 1'
>>> profiles[key_for_profile].product
'HFSS3DLayout'
>>> print(f"Elapsed time: {profiles[key_for_profile].elapsed_time}")
Elapsed time: 0:01:39
>>> print(f"Number of adaptive passes: {profiles[key_for_profile].num_adaptive_passes}")
Number of adaptive passes: 6
>>> fsweeps = profiles[key_for_profile].frequency_sweeps
>>> sweep_name = list(fsweeps.keys())[0]  # Select the first sweep
>>> print(f"Frequency sweep '{sweep_name}' calculated {len(fsweeps[sweep_name].frequencies)} frequency points.")
Frequency sweep 'Sweep 1' calculated 74 frequency points.

```
Copy to clipboard
Maxwell 2D (Transient):

```
>>> app = Maxwell2d(project="solved_m2d_project")
>>> profiles = app.setups[0].get_profile()
>>> profile_name = list(profiles.keys())[0]
>>> print(f"Profile name: {profile_name}")
Profile name: Setup1 - fractions='4'
>>> print(f"Elapsed time: {profiles[profile_name].elapsed_time}")
Elapsed time: 0:01:24
>>> print(f"Number of time steps: {len(profiles[profile_name].time_steps)}")
Number of time steps: 80

```
Copy to clipboard
Methods  
| [`Profiles.get`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.Profiles.get.html#ansys.aedt.core.modules.profile.Profiles.get "ansys.aedt.core.modules.profile.Profiles.get")(k[,d])  |   |  
| --- | --- |  
| [`Profiles.items`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.Profiles.items.html#ansys.aedt.core.modules.profile.Profiles.items "ansys.aedt.core.modules.profile.Profiles.items")()  |   |  
| [`Profiles.keys`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.Profiles.keys.html#ansys.aedt.core.modules.profile.Profiles.keys "ansys.aedt.core.modules.profile.Profiles.keys")()  | Expose the keys of the underlying mapping.  |  
| [`Profiles.values`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.Profiles.values.html#ansys.aedt.core.modules.profile.Profiles.values "ansys.aedt.core.modules.profile.Profiles.values")()  |   |  
Attributes  
| [`Profiles.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.Profiles.public_dir.html#ansys.aedt.core.modules.profile.Profiles.public_dir "ansys.aedt.core.modules.profile.Profiles.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |  
# Profiles 

class ansys.aedt.core.modules.profile.Profiles(_profile_dict_) 
    
Provide an interface to solver profiles.
The Profiles class is iterable. Individual profiles are accessed via the unique key made up of “setup_name - variation”. If there are no variations available, the unique key is the setup name.
Examples
HFSS 3D Layout:

```
>>> app = Hfss3DLayout(project="solved_h3d_project")
>>> profiles = app.setups[0].get_profile()
>>> key_for_profile = list(profiles.keys())[0]
>>> print(key_for_profile)
'HFSS Setup 1'
>>> profiles[key_for_profile].product
'HFSS3DLayout'
>>> print(f"Elapsed time: {profiles[key_for_profile].elapsed_time}")
Elapsed time: 0:01:39
>>> print(f"Number of adaptive passes: {profiles[key_for_profile].num_adaptive_passes}")
Number of adaptive passes: 6
>>> fsweeps = profiles[key_for_profile].frequency_sweeps
>>> sweep_name = list(fsweeps.keys())[0]  # Select the first sweep
>>> print(f"Frequency sweep '{sweep_name}' calculated {len(fsweeps[sweep_name].frequencies)} frequency points.")
Frequency sweep 'Sweep 1' calculated 74 frequency points.

```
Copy to clipboard
Maxwell 2D (Transient):

```
>>> app = Maxwell2d(project="solved_m2d_project")
>>> profiles = app.setups[0].get_profile()
>>> profile_name = list(profiles.keys())[0]
>>> print(f"Profile name: {profile_name}")
Profile name: Setup1 - fractions='4'
>>> print(f"Elapsed time: {profiles[profile_name].elapsed_time}")
Elapsed time: 0:01:24
>>> print(f"Number of time steps: {len(profiles[profile_name].time_steps)}")
Number of time steps: 80

```
Copy to clipboard
Methods  
| [`Profiles.get`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.Profiles.get.html#ansys.aedt.core.modules.profile.Profiles.get "ansys.aedt.core.modules.profile.Profiles.get")(k[,d])  |   |  
| --- | --- |  
| [`Profiles.items`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.Profiles.items.html#ansys.aedt.core.modules.profile.Profiles.items "ansys.aedt.core.modules.profile.Profiles.items")()  |   |  
| [`Profiles.keys`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.Profiles.keys.html#ansys.aedt.core.modules.profile.Profiles.keys "ansys.aedt.core.modules.profile.Profiles.keys")()  | Expose the keys of the underlying mapping.  |  
| [`Profiles.values`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.Profiles.values.html#ansys.aedt.core.modules.profile.Profiles.values "ansys.aedt.core.modules.profile.Profiles.values")()  |   |  
Attributes  
| [`Profiles.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.Profiles.public_dir.html#ansys.aedt.core.modules.profile.Profiles.public_dir "ansys.aedt.core.modules.profile.Profiles.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.modules.profile.Profiles.rst.txt)

# Profiles 

class ansys.aedt.core.modules.profile.Profiles(_profile_dict_) 
    
Provide an interface to solver profiles.
The Profiles class is iterable. Individual profiles are accessed via the unique key made up of “setup_name - variation”. If there are no variations available, the unique key is the setup name.
Examples
HFSS 3D Layout:

```
>>> app = Hfss3DLayout(project="solved_h3d_project")
>>> profiles = app.setups[0].get_profile()
>>> key_for_profile = list(profiles.keys())[0]
>>> print(key_for_profile)
'HFSS Setup 1'
>>> profiles[key_for_profile].product
'HFSS3DLayout'
>>> print(f"Elapsed time: {profiles[key_for_profile].elapsed_time}")
Elapsed time: 0:01:39
>>> print(f"Number of adaptive passes: {profiles[key_for_profile].num_adaptive_passes}")
Number of adaptive passes: 6
>>> fsweeps = profiles[key_for_profile].frequency_sweeps
>>> sweep_name = list(fsweeps.keys())[0]  # Select the first sweep
>>> print(f"Frequency sweep '{sweep_name}' calculated {len(fsweeps[sweep_name].frequencies)} frequency points.")
Frequency sweep 'Sweep 1' calculated 74 frequency points.

```
Copy to clipboard
Maxwell 2D (Transient):

```
>>> app = Maxwell2d(project="solved_m2d_project")
>>> profiles = app.setups[0].get_profile()
>>> profile_name = list(profiles.keys())[0]
>>> print(f"Profile name: {profile_name}")
Profile name: Setup1 - fractions='4'
>>> print(f"Elapsed time: {profiles[profile_name].elapsed_time}")
Elapsed time: 0:01:24
>>> print(f"Number of time steps: {len(profiles[profile_name].time_steps)}")
Number of time steps: 80

```
Copy to clipboard
Methods  
| [`Profiles.get`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.Profiles.get.html#ansys.aedt.core.modules.profile.Profiles.get "ansys.aedt.core.modules.profile.Profiles.get")(k[,d])  |   |  
| --- | --- |  
| [`Profiles.items`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.Profiles.items.html#ansys.aedt.core.modules.profile.Profiles.items "ansys.aedt.core.modules.profile.Profiles.items")()  |   |  
| [`Profiles.keys`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.Profiles.keys.html#ansys.aedt.core.modules.profile.Profiles.keys "ansys.aedt.core.modules.profile.Profiles.keys")()  | Expose the keys of the underlying mapping.  |  
| [`Profiles.values`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.Profiles.values.html#ansys.aedt.core.modules.profile.Profiles.values "ansys.aedt.core.modules.profile.Profiles.values")()  |   |  
Attributes  
| [`Profiles.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.profile.Profiles.public_dir.html#ansys.aedt.core.modules.profile.Profiles.public_dir "ansys.aedt.core.modules.profile.Profiles.public_dir")  | Shortcut for dir(self).  |  
| --- | --- |