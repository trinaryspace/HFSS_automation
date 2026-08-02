---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_sbr_chirp_i_doppler_setup.html"
category: "hfss"
domain: "PyAEDT / HFSS"
---

# create_sbr_chirp_i_doppler_setup 

Hfss.create_sbr_chirp_i_doppler_setup(_time_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _sweep_time_duration : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0.0_, _center_freq : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 76.5_, _resolution : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 1_, _period : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 200_, _velocity_resolution : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0.4_, _min_velocity : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = -20_, _max_velocity : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 20_, _ray_density_per_wavelength : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0.2_, _max_bounces : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 5_, _include_coupling_effects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _doppler_ad_sampling_rate : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 20_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[SetupHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.html#ansys.aedt.core.modules.solve_setup.SetupHFSS "ansys.aedt.core.modules.solve_setup.SetupHFSS") | [SetupHFSSAuto](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto"), [SetupParam](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.html#ansys.aedt.core.modules.design_xploration.SetupParam "ansys.aedt.core.modules.design_xploration.SetupParam") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)")] 
    
Create an SBR+ Chirp I setup. 

Parameters: 
     

**time_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the time variable. The default is `None`, in which case a search for the first time variable is performed. 

**sweep_time_duration**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Duration for the sweep time. The default is `0.` If a value greater than `0` is specified, a parametric sweep is created. 

**center_freq**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Center frequency in gigahertz (GHz). The default is `76.5`. 

**resolution**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Doppler resolution in meters (m). The default is `1`. 

**period**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Period of analysis in meters (m). The default is `200`. 

**velocity_resolution**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Doppler velocity resolution in meters per second (m/s). The default is `0.4`. 

**min_velocity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Minimum Doppler velocity in meters per second (m/s). The default is `-20`. 

**max_velocity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Maximum Doppler velocity in meters per second (m/s). The default is `20`. 

**ray_density_per_wavelength**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Doppler ray density per wavelength. The default is `0.2`. 

**max_bounces**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of bounces. The default is `5`. 

**include_coupling_effects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to include coupling effects. The default is `False`. 

**doppler_ad_sampling_rate**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Doppler AD sampling rate to use if `include_coupling_effects` is `True`. The default is `20`. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the active setup is used. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
The tuple contains: ([`ansys.aedt.core.modules.solve_setup.SetupHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.html#ansys.aedt.core.modules.solve_setup.SetupHFSS "ansys.aedt.core.modules.solve_setup.SetupHFSS") or [`ansys.aedt.core.modules.solve_setup.SetupHFSSAuto`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto"), [`ansys.aedt.core.modules.design_xploration.SetupParam`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.html#ansys.aedt.core.modules.design_xploration.SetupParam "ansys.aedt.core.modules.design_xploration.SetupParam")) or bool.
References

```
>>> oModule.InsertSetup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(solution_type="SBR+")
>>> setup, sweep = hfss.create_sbr_chirp_i_doppler_setup(sweep_time_duration=20)

```
Copy to clipboard
# create_sbr_chirp_i_doppler_setup 

Hfss.create_sbr_chirp_i_doppler_setup(_time_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _sweep_time_duration : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0.0_, _center_freq : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 76.5_, _resolution : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 1_, _period : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 200_, _velocity_resolution : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0.4_, _min_velocity : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = -20_, _max_velocity : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 20_, _ray_density_per_wavelength : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0.2_, _max_bounces : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 5_, _include_coupling_effects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _doppler_ad_sampling_rate : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 20_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[SetupHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.html#ansys.aedt.core.modules.solve_setup.SetupHFSS "ansys.aedt.core.modules.solve_setup.SetupHFSS") | [SetupHFSSAuto](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto"), [SetupParam](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.html#ansys.aedt.core.modules.design_xploration.SetupParam "ansys.aedt.core.modules.design_xploration.SetupParam") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)")] 
    
Create an SBR+ Chirp I setup. 

Parameters: 
     

**time_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the time variable. The default is `None`, in which case a search for the first time variable is performed. 

**sweep_time_duration**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Duration for the sweep time. The default is `0.` If a value greater than `0` is specified, a parametric sweep is created. 

**center_freq**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Center frequency in gigahertz (GHz). The default is `76.5`. 

**resolution**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Doppler resolution in meters (m). The default is `1`. 

**period**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Period of analysis in meters (m). The default is `200`. 

**velocity_resolution**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Doppler velocity resolution in meters per second (m/s). The default is `0.4`. 

**min_velocity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Minimum Doppler velocity in meters per second (m/s). The default is `-20`. 

**max_velocity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Maximum Doppler velocity in meters per second (m/s). The default is `20`. 

**ray_density_per_wavelength**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Doppler ray density per wavelength. The default is `0.2`. 

**max_bounces**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of bounces. The default is `5`. 

**include_coupling_effects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to include coupling effects. The default is `False`. 

**doppler_ad_sampling_rate**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Doppler AD sampling rate to use if `include_coupling_effects` is `True`. The default is `20`. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the active setup is used. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
The tuple contains: ([`ansys.aedt.core.modules.solve_setup.SetupHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.html#ansys.aedt.core.modules.solve_setup.SetupHFSS "ansys.aedt.core.modules.solve_setup.SetupHFSS") or [`ansys.aedt.core.modules.solve_setup.SetupHFSSAuto`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto"), [`ansys.aedt.core.modules.design_xploration.SetupParam`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.html#ansys.aedt.core.modules.design_xploration.SetupParam "ansys.aedt.core.modules.design_xploration.SetupParam")) or bool.
References

```
>>> oModule.InsertSetup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(solution_type="SBR+")
>>> setup, sweep = hfss.create_sbr_chirp_i_doppler_setup(sweep_time_duration=20)

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.hfss.Hfss.create_sbr_chirp_i_doppler_setup.rst.txt)

# create_sbr_chirp_i_doppler_setup 

Hfss.create_sbr_chirp_i_doppler_setup(_time_variable : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _sweep_time_duration : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0.0_, _center_freq : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 76.5_, _resolution : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 1_, _period : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 200_, _velocity_resolution : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0.4_, _min_velocity : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = -20_, _max_velocity : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 20_, _ray_density_per_wavelength : [float](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 0.2_, _max_bounces : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 5_, _include_coupling_effects : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = False_, _doppler_ad_sampling_rate : [int](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = 20_, _setup : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_) → [tuple](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")[[SetupHFSS](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.html#ansys.aedt.core.modules.solve_setup.SetupHFSS "ansys.aedt.core.modules.solve_setup.SetupHFSS") | [SetupHFSSAuto](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto"), [SetupParam](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.html#ansys.aedt.core.modules.design_xploration.SetupParam "ansys.aedt.core.modules.design_xploration.SetupParam") | [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)")] 
    
Create an SBR+ Chirp I setup. 

Parameters: 
     

**time_variable**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the time variable. The default is `None`, in which case a search for the first time variable is performed. 

**sweep_time_duration**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Duration for the sweep time. The default is `0.` If a value greater than `0` is specified, a parametric sweep is created. 

**center_freq**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Center frequency in gigahertz (GHz). The default is `76.5`. 

**resolution**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Doppler resolution in meters (m). The default is `1`. 

**period**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Period of analysis in meters (m). The default is `200`. 

**velocity_resolution**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Doppler velocity resolution in meters per second (m/s). The default is `0.4`. 

**min_velocity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Minimum Doppler velocity in meters per second (m/s). The default is `-20`. 

**max_velocity**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Maximum Doppler velocity in meters per second (m/s). The default is `20`. 

**ray_density_per_wavelength**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Doppler ray density per wavelength. The default is `0.2`. 

**max_bounces**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Maximum number of bounces. The default is `5`. 

**include_coupling_effects**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to include coupling effects. The default is `False`. 

**doppler_ad_sampling_rate**[`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Doppler AD sampling rate to use if `include_coupling_effects` is `True`. The default is `20`. 

**setup**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the setup. The default is `None`, in which case the active setup is used. 

Returns: 
     

[`tuple`](https://docs.python.org/3.11/library/stdtypes.html#tuple "\(in Python v3.11\)")
    
The tuple contains: ([`ansys.aedt.core.modules.solve_setup.SetupHFSS`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSS.html#ansys.aedt.core.modules.solve_setup.SetupHFSS "ansys.aedt.core.modules.solve_setup.SetupHFSS") or [`ansys.aedt.core.modules.solve_setup.SetupHFSSAuto`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.solve_setup.SetupHFSSAuto.html#ansys.aedt.core.modules.solve_setup.SetupHFSSAuto "ansys.aedt.core.modules.solve_setup.SetupHFSSAuto"), [`ansys.aedt.core.modules.design_xploration.SetupParam`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.modules.design_xploration.SetupParam.html#ansys.aedt.core.modules.design_xploration.SetupParam "ansys.aedt.core.modules.design_xploration.SetupParam")) or bool.
References

```
>>> oModule.InsertSetup

```
Copy to clipboard
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss(solution_type="SBR+")
>>> setup, sweep = hfss.create_sbr_chirp_i_doppler_setup(sweep_time_duration=20)

```
Copy to clipboard