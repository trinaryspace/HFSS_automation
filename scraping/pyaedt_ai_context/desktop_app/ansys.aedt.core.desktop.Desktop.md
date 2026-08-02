---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# Desktop 

class ansys.aedt.core.desktop.Desktop(_* args_, _** kwargs_) 
    
Provides the Ansys Electronics Desktop (AEDT) interface. 

Parameters: 
     

**version**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Version of AEDT to use. The default is `None`, in which case the active setup or latest installed version is used. Examples of input values are `261`, `26.1`, `2026.1`, `"2026.1"`. 

**non_graphical**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to launch AEDT in non-graphical mode. The default is `False`, in which case AEDT is launched in graphical mode. This parameter is ignored when a script is launched within AEDT. 

**new_desktop**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to launch an instance of AEDT in a new thread, even if another instance of the `version` is active on the machine. The default is `True`. 

**close_on_exit**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to close AEDT on exit. The default is `None`, which means the behavior is chosen automatically:
  * If `Desktop` is used in a context manager (`with` statement), the context manager take precedence and AEDT will be closed on exit (equivalent to `close_on_exit=True`).
  * If PyAEDT actually starts a new AEDT session, the session will be closed on exit (`close_on_exit=True`).
  * If PyAEDT connects to an existing AEDT session, the session will not be closed on exit (`close_on_exit=False`).

A user-specified boolean (`True` or `False`) always overrides the automatic behavior. 

**When ``Desktop`` is used outside a context manager, the ``release_desktop`` method arguments offer**
    
finer control over releasing and closing behavior. 

**student_version**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to open the AEDT student version. The default is `False`. 

**machine**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Machine name to connect the oDesktop session to. This parameter works only in 2022 R2 and later. The remote server must be up and running with the command `"ansysedt.exe -grpcsrv portnum"`. If the machine is `"localhost"`, the server also starts if not present. 

**port**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Port number on which to start the oDesktop communication on the already existing server. This parameter is ignored when creating a new server. It works only in 2022 R2 and later. The remote server must be up and running with the command `"ansysedt.exe -grpcsrv portnum"`. 

**aedt_process_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Process ID for the instance of AEDT to point PyAEDT at. The default is `None`. This parameter is only used when `new_desktop = False`.
Examples
Launch AEDT 2026 R1 in non-graphical mode and initialize HFSS.

```
>>> import ansys.aedt.core
>>> desktop = ansys.aedt.core.Desktop(version="2026.1", non_graphical=False)
PyAEDT INFO: pyaedt v...
PyAEDT INFO: Python version ...
>>> hfss = ansys.aedt.core.Hfss(design="HFSSDesign1")
PyAEDT INFO: Project...
PyAEDT INFO: Added design 'HFSSDesign1' of type HFSS.

```
Copy to clipboard
Launch AEDT 2025 R1 in graphical mode and initialize HFSS.

```
>>> desktop = Desktop(261)
PyAEDT INFO: pyaedt v...
PyAEDT INFO: Python version ...
>>> hfss = ansys.aedt.core.Hfss(design="HFSSDesign1")
PyAEDT INFO: No project is defined. Project...

```
Copy to clipboard
Methods  
| [`Desktop.active_design`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.active_design.html#ansys.aedt.core.desktop.Desktop.active_design "ansys.aedt.core.desktop.Desktop.active_design")([project_object, ...])  | Get the active design.  |  
| --- | --- |  
| [`Desktop.active_project`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.active_project.html#ansys.aedt.core.desktop.Desktop.active_project "ansys.aedt.core.desktop.Desktop.active_project")([name])  | Get the active project.  |  
| [`Desktop.analyze_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.analyze_all.html#ansys.aedt.core.desktop.Desktop.analyze_all "ansys.aedt.core.desktop.Desktop.analyze_all")([project, design])  | Analyze all setups in a project.  |  
| [`Desktop.change_active_dso_config_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.change_active_dso_config_name.html#ansys.aedt.core.desktop.Desktop.change_active_dso_config_name "ansys.aedt.core.desktop.Desktop.change_active_dso_config_name")([...])  | Change a specific registry key to a new value.  |  
| [`Desktop.change_license_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.change_license_type.html#ansys.aedt.core.desktop.Desktop.change_license_type "ansys.aedt.core.desktop.Desktop.change_license_type")([license_type])  | Change the license type.  |  
| [`Desktop.change_registry_from_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.change_registry_from_file.html#ansys.aedt.core.desktop.Desktop.change_registry_from_file "ansys.aedt.core.desktop.Desktop.change_registry_from_file")(registry_file)  | Apply desktop registry settings from an ACF file.  |  
| [`Desktop.change_registry_key`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.change_registry_key.html#ansys.aedt.core.desktop.Desktop.change_registry_key "ansys.aedt.core.desktop.Desktop.change_registry_key")(key_full_name, ...)  | Change an AEDT registry key to a new value.  |  
| [`Desktop.check_starting_mode`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.check_starting_mode.html#ansys.aedt.core.desktop.Desktop.check_starting_mode "ansys.aedt.core.desktop.Desktop.check_starting_mode")()  | Check the starting mode.  |  
| [`Desktop.clear_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.clear_messages.html#ansys.aedt.core.desktop.Desktop.clear_messages "ansys.aedt.core.desktop.Desktop.clear_messages")()  | Clear all AEDT messages.  |  
| [`Desktop.close_desktop`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.close_desktop.html#ansys.aedt.core.desktop.Desktop.close_desktop "ansys.aedt.core.desktop.Desktop.close_desktop")()  | Close all projects and shut down AEDT.  |  
| [`Desktop.close_windows`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.close_windows.html#ansys.aedt.core.desktop.Desktop.close_windows "ansys.aedt.core.desktop.Desktop.close_windows")()  | Close all windows.  |  
| [`Desktop.design_list`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.design_list.html#ansys.aedt.core.desktop.Desktop.design_list "ansys.aedt.core.desktop.Desktop.design_list")([project])  | Get a list of the designs.  |  
| [`Desktop.design_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.design_type.html#ansys.aedt.core.desktop.Desktop.design_type "ansys.aedt.core.desktop.Desktop.design_type")([project_name, design_name])  | Get the type of design.  |  
| [`Desktop.disable_autosave`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.disable_autosave.html#ansys.aedt.core.desktop.Desktop.disable_autosave "ansys.aedt.core.desktop.Desktop.disable_autosave")()  | Disable the autosave option.  |  
| [`Desktop.disable_optimetrics`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.disable_optimetrics.html#ansys.aedt.core.desktop.Desktop.disable_optimetrics "ansys.aedt.core.desktop.Desktop.disable_optimetrics")()  | Disable optimetrics.  |  
| [`Desktop.enable_autosave`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.enable_autosave.html#ansys.aedt.core.desktop.Desktop.enable_autosave "ansys.aedt.core.desktop.Desktop.enable_autosave")()  | Enable the autosave option.  |  
| [`Desktop.enable_optimetrics`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.enable_optimetrics.html#ansys.aedt.core.desktop.Desktop.enable_optimetrics "ansys.aedt.core.desktop.Desktop.enable_optimetrics")()  | Enable optimetrics.  |  
| [`Desktop.get_available_toolkits`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.get_available_toolkits.html#ansys.aedt.core.desktop.Desktop.get_available_toolkits "ansys.aedt.core.desktop.Desktop.get_available_toolkits")()  | Get toolkit ready for installation.  |  
| [`Desktop.get_example`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.get_example.html#ansys.aedt.core.desktop.Desktop.get_example "ansys.aedt.core.desktop.Desktop.get_example")(example_name[, folder_name])  | Retrieve the path to a built-in example project.  |  
| [`Desktop.get_monitor_data`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.get_monitor_data.html#ansys.aedt.core.desktop.Desktop.get_monitor_data "ansys.aedt.core.desktop.Desktop.get_monitor_data")()  | Check and get monitor data of an existing analysis.  |  
| [`Desktop.job_status`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.job_status.html#ansys.aedt.core.desktop.Desktop.job_status "ansys.aedt.core.desktop.Desktop.job_status")()  | Get job status from job monitor.  |  
| [`Desktop.launch_job_monitor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.launch_job_monitor.html#ansys.aedt.core.desktop.Desktop.launch_job_monitor "ansys.aedt.core.desktop.Desktop.launch_job_monitor")(input_file)  | Launch job monitor.  |  
| [`Desktop.load_project`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.load_project.html#ansys.aedt.core.desktop.Desktop.load_project "ansys.aedt.core.desktop.Desktop.load_project")(project_file[, design_name])  | Open an AEDT project based on a project and optional design.  |  
| [`Desktop.project_path`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.project_path.html#ansys.aedt.core.desktop.Desktop.project_path "ansys.aedt.core.desktop.Desktop.project_path")([project_name])  | Get the path to the project.  |  
| [`Desktop.release_desktop`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.release_desktop.html#ansys.aedt.core.desktop.Desktop.release_desktop "ansys.aedt.core.desktop.Desktop.release_desktop")([close_projects, ...])  | Release AEDT.  |  
| [`Desktop.save_project`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.save_project.html#ansys.aedt.core.desktop.Desktop.save_project "ansys.aedt.core.desktop.Desktop.save_project")([project_name, ...])  | Save the project.  |  
| [`Desktop.select_scheduler`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.select_scheduler.html#ansys.aedt.core.desktop.Desktop.select_scheduler "ansys.aedt.core.desktop.Desktop.select_scheduler")(scheduler_type[, ...])  | Select a scheduler to submit the job.  |  
| [`Desktop.stop_simulations`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.stop_simulations.html#ansys.aedt.core.desktop.Desktop.stop_simulations "ansys.aedt.core.desktop.Desktop.stop_simulations")([clean_stop])  | Check if there are simulation running and stops them.  |  
| [`Desktop.submit_job`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.submit_job.html#ansys.aedt.core.desktop.Desktop.submit_job "ansys.aedt.core.desktop.Desktop.submit_job")(project_file[, ...])  | Submit a job to be solved on a cluster.  |  
Attributes  
| [`Desktop.active_design_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.active_design_name.html#ansys.aedt.core.desktop.Desktop.active_design_name "ansys.aedt.core.desktop.Desktop.active_design_name")  | Get the display name of the active design.  |  
| --- | --- |  
| [`Desktop.active_project_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.active_project_name.html#ansys.aedt.core.desktop.Desktop.active_project_name "ansys.aedt.core.desktop.Desktop.active_project_name")  | Get the name of the active project.  |  
| [`Desktop.aedt_install_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.aedt_install_dir.html#ansys.aedt.core.desktop.Desktop.aedt_install_dir "ansys.aedt.core.desktop.Desktop.aedt_install_dir")  | AEDT installation path.  |  
| [`Desktop.aedt_process_id`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.aedt_process_id.html#ansys.aedt.core.desktop.Desktop.aedt_process_id "ansys.aedt.core.desktop.Desktop.aedt_process_id")  | Retrieve AEDT process id.  |  
| [`Desktop.aedt_version`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.aedt_version.html#ansys.aedt.core.desktop.Desktop.aedt_version "ansys.aedt.core.desktop.Desktop.aedt_version")  | Retrieve AEDT version from AEDT.  |  
| [`Desktop.aedt_version_id`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.aedt_version_id.html#ansys.aedt.core.desktop.Desktop.aedt_version_id "ansys.aedt.core.desktop.Desktop.aedt_version_id")  | Retrieve AEDT version id.  |  
| [`Desktop.aedt_version_string`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.aedt_version_string.html#ansys.aedt.core.desktop.Desktop.aedt_version_string "ansys.aedt.core.desktop.Desktop.aedt_version_string")  | AEDT version string.  |  
| [`Desktop.are_there_simulations_running`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.are_there_simulations_running.html#ansys.aedt.core.desktop.Desktop.are_there_simulations_running "ansys.aedt.core.desktop.Desktop.are_there_simulations_running")  | Check if there are simulation running.  |  
| [`Desktop.close_on_exit`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.close_on_exit.html#ansys.aedt.core.desktop.Desktop.close_on_exit "ansys.aedt.core.desktop.Desktop.close_on_exit")  | Whether AEDT will close on exit.  |  
| [`Desktop.current_student_version`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.current_student_version.html#ansys.aedt.core.desktop.Desktop.current_student_version "ansys.aedt.core.desktop.Desktop.current_student_version")  | Current AEDT student version.  |  
| [`Desktop.current_version`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.current_version.html#ansys.aedt.core.desktop.Desktop.current_version "ansys.aedt.core.desktop.Desktop.current_version")  | Current AEDT version.  |  
| [`Desktop.global_project_directory`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.global_project_directory.html#ansys.aedt.core.desktop.Desktop.global_project_directory "ansys.aedt.core.desktop.Desktop.global_project_directory")  | AEDT project directory.  |  
| [`Desktop.grpc_mode`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.grpc_mode.html#ansys.aedt.core.desktop.Desktop.grpc_mode "ansys.aedt.core.desktop.Desktop.grpc_mode")  | Retrieve gRPC mode.  |  
| [`Desktop.install_path`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.install_path.html#ansys.aedt.core.desktop.Desktop.install_path "ansys.aedt.core.desktop.Desktop.install_path")  | Installation path for AEDT.  |  
| [`Desktop.installed_versions`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.installed_versions.html#ansys.aedt.core.desktop.Desktop.installed_versions "ansys.aedt.core.desktop.Desktop.installed_versions")  | Dictionary of AEDT versions installed on the system and their installation paths.  |  
| [`Desktop.is_grpc_api`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.is_grpc_api.html#ansys.aedt.core.desktop.Desktop.is_grpc_api "ansys.aedt.core.desktop.Desktop.is_grpc_api")  | Whether the connection is through gRPC API.  |  
| [`Desktop.launched_by_pyaedt`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.launched_by_pyaedt.html#ansys.aedt.core.desktop.Desktop.launched_by_pyaedt "ansys.aedt.core.desktop.Desktop.launched_by_pyaedt")  | Flag to check if AEDT was launched by PyAEDT.  |  
| [`Desktop.logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.logger.html#ansys.aedt.core.desktop.Desktop.logger "ansys.aedt.core.desktop.Desktop.logger")  | AEDT logger.  |  
| [`Desktop.machine`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.machine.html#ansys.aedt.core.desktop.Desktop.machine "ansys.aedt.core.desktop.Desktop.machine")  | Machine name.  |  
| [`Desktop.messenger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.messenger.html#ansys.aedt.core.desktop.Desktop.messenger "ansys.aedt.core.desktop.Desktop.messenger")  | Messenger manager for the AEDT logger.  |  
| [`Desktop.new_desktop`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.new_desktop.html#ansys.aedt.core.desktop.Desktop.new_desktop "ansys.aedt.core.desktop.Desktop.new_desktop")  | Whether a new session will be started or not.  |  
| [`Desktop.non_graphical`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.non_graphical.html#ansys.aedt.core.desktop.Desktop.non_graphical "ansys.aedt.core.desktop.Desktop.non_graphical")  | Whether AEDT is running in non-graphical mode.  |  
| [`Desktop.odesktop`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.odesktop.html#ansys.aedt.core.desktop.Desktop.odesktop "ansys.aedt.core.desktop.Desktop.odesktop")  | AEDT instance containing all projects and designs.  |  
| [`Desktop.personallib`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.personallib.html#ansys.aedt.core.desktop.Desktop.personallib "ansys.aedt.core.desktop.Desktop.personallib")  | PersonalLib directory.  |  
| [`Desktop.port`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.port.html#ansys.aedt.core.desktop.Desktop.port "ansys.aedt.core.desktop.Desktop.port")  | Port number.  |  
| [`Desktop.project_list`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.project_list.html#ansys.aedt.core.desktop.Desktop.project_list "ansys.aedt.core.desktop.Desktop.project_list")  | Get a list of projects.  |  
| [`Desktop.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.public_dir.html#ansys.aedt.core.desktop.Desktop.public_dir "ansys.aedt.core.desktop.Desktop.public_dir")  | Shortcut for dir(self).  |  
| [`Desktop.pyaedt_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.pyaedt_dir.html#ansys.aedt.core.desktop.Desktop.pyaedt_dir "ansys.aedt.core.desktop.Desktop.pyaedt_dir")  | PyAEDT directory.  |  
| [`Desktop.src_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.src_dir.html#ansys.aedt.core.desktop.Desktop.src_dir "ansys.aedt.core.desktop.Desktop.src_dir")  | Python source directory.  |  
| [`Desktop.student_version`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.student_version.html#ansys.aedt.core.desktop.Desktop.student_version "ansys.aedt.core.desktop.Desktop.student_version")  | Whether AEDT is the student version.  |  
| [`Desktop.syslib`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.syslib.html#ansys.aedt.core.desktop.Desktop.syslib "ansys.aedt.core.desktop.Desktop.syslib")  | SysLib directory.  |  
| [`Desktop.temp_directory`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.temp_directory.html#ansys.aedt.core.desktop.Desktop.temp_directory "ansys.aedt.core.desktop.Desktop.temp_directory")  | AEDT temp directory.  |  
| [`Desktop.userlib`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.userlib.html#ansys.aedt.core.desktop.Desktop.userlib "ansys.aedt.core.desktop.Desktop.userlib")  | UserLib directory.  |  
# Desktop 

class ansys.aedt.core.desktop.Desktop(_* args_, _** kwargs_) 
    
Provides the Ansys Electronics Desktop (AEDT) interface. 

Parameters: 
     

**version**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Version of AEDT to use. The default is `None`, in which case the active setup or latest installed version is used. Examples of input values are `261`, `26.1`, `2026.1`, `"2026.1"`. 

**non_graphical**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to launch AEDT in non-graphical mode. The default is `False`, in which case AEDT is launched in graphical mode. This parameter is ignored when a script is launched within AEDT. 

**new_desktop**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to launch an instance of AEDT in a new thread, even if another instance of the `version` is active on the machine. The default is `True`. 

**close_on_exit**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to close AEDT on exit. The default is `None`, which means the behavior is chosen automatically:
  * If `Desktop` is used in a context manager (`with` statement), the context manager take precedence and AEDT will be closed on exit (equivalent to `close_on_exit=True`).
  * If PyAEDT actually starts a new AEDT session, the session will be closed on exit (`close_on_exit=True`).
  * If PyAEDT connects to an existing AEDT session, the session will not be closed on exit (`close_on_exit=False`).

A user-specified boolean (`True` or `False`) always overrides the automatic behavior. 

**When ``Desktop`` is used outside a context manager, the ``release_desktop`` method arguments offer**
    
finer control over releasing and closing behavior. 

**student_version**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to open the AEDT student version. The default is `False`. 

**machine**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Machine name to connect the oDesktop session to. This parameter works only in 2022 R2 and later. The remote server must be up and running with the command `"ansysedt.exe -grpcsrv portnum"`. If the machine is `"localhost"`, the server also starts if not present. 

**port**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Port number on which to start the oDesktop communication on the already existing server. This parameter is ignored when creating a new server. It works only in 2022 R2 and later. The remote server must be up and running with the command `"ansysedt.exe -grpcsrv portnum"`. 

**aedt_process_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Process ID for the instance of AEDT to point PyAEDT at. The default is `None`. This parameter is only used when `new_desktop = False`.
Examples
Launch AEDT 2026 R1 in non-graphical mode and initialize HFSS.

```
>>> import ansys.aedt.core
>>> desktop = ansys.aedt.core.Desktop(version="2026.1", non_graphical=False)
PyAEDT INFO: pyaedt v...
PyAEDT INFO: Python version ...
>>> hfss = ansys.aedt.core.Hfss(design="HFSSDesign1")
PyAEDT INFO: Project...
PyAEDT INFO: Added design 'HFSSDesign1' of type HFSS.

```
Copy to clipboard
Launch AEDT 2025 R1 in graphical mode and initialize HFSS.

```
>>> desktop = Desktop(261)
PyAEDT INFO: pyaedt v...
PyAEDT INFO: Python version ...
>>> hfss = ansys.aedt.core.Hfss(design="HFSSDesign1")
PyAEDT INFO: No project is defined. Project...

```
Copy to clipboard
Methods  
| [`Desktop.active_design`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.active_design.html#ansys.aedt.core.desktop.Desktop.active_design "ansys.aedt.core.desktop.Desktop.active_design")([project_object, ...])  | Get the active design.  |  
| --- | --- |  
| [`Desktop.active_project`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.active_project.html#ansys.aedt.core.desktop.Desktop.active_project "ansys.aedt.core.desktop.Desktop.active_project")([name])  | Get the active project.  |  
| [`Desktop.analyze_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.analyze_all.html#ansys.aedt.core.desktop.Desktop.analyze_all "ansys.aedt.core.desktop.Desktop.analyze_all")([project, design])  | Analyze all setups in a project.  |  
| [`Desktop.change_active_dso_config_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.change_active_dso_config_name.html#ansys.aedt.core.desktop.Desktop.change_active_dso_config_name "ansys.aedt.core.desktop.Desktop.change_active_dso_config_name")([...])  | Change a specific registry key to a new value.  |  
| [`Desktop.change_license_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.change_license_type.html#ansys.aedt.core.desktop.Desktop.change_license_type "ansys.aedt.core.desktop.Desktop.change_license_type")([license_type])  | Change the license type.  |  
| [`Desktop.change_registry_from_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.change_registry_from_file.html#ansys.aedt.core.desktop.Desktop.change_registry_from_file "ansys.aedt.core.desktop.Desktop.change_registry_from_file")(registry_file)  | Apply desktop registry settings from an ACF file.  |  
| [`Desktop.change_registry_key`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.change_registry_key.html#ansys.aedt.core.desktop.Desktop.change_registry_key "ansys.aedt.core.desktop.Desktop.change_registry_key")(key_full_name, ...)  | Change an AEDT registry key to a new value.  |  
| [`Desktop.check_starting_mode`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.check_starting_mode.html#ansys.aedt.core.desktop.Desktop.check_starting_mode "ansys.aedt.core.desktop.Desktop.check_starting_mode")()  | Check the starting mode.  |  
| [`Desktop.clear_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.clear_messages.html#ansys.aedt.core.desktop.Desktop.clear_messages "ansys.aedt.core.desktop.Desktop.clear_messages")()  | Clear all AEDT messages.  |  
| [`Desktop.close_desktop`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.close_desktop.html#ansys.aedt.core.desktop.Desktop.close_desktop "ansys.aedt.core.desktop.Desktop.close_desktop")()  | Close all projects and shut down AEDT.  |  
| [`Desktop.close_windows`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.close_windows.html#ansys.aedt.core.desktop.Desktop.close_windows "ansys.aedt.core.desktop.Desktop.close_windows")()  | Close all windows.  |  
| [`Desktop.design_list`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.design_list.html#ansys.aedt.core.desktop.Desktop.design_list "ansys.aedt.core.desktop.Desktop.design_list")([project])  | Get a list of the designs.  |  
| [`Desktop.design_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.design_type.html#ansys.aedt.core.desktop.Desktop.design_type "ansys.aedt.core.desktop.Desktop.design_type")([project_name, design_name])  | Get the type of design.  |  
| [`Desktop.disable_autosave`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.disable_autosave.html#ansys.aedt.core.desktop.Desktop.disable_autosave "ansys.aedt.core.desktop.Desktop.disable_autosave")()  | Disable the autosave option.  |  
| [`Desktop.disable_optimetrics`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.disable_optimetrics.html#ansys.aedt.core.desktop.Desktop.disable_optimetrics "ansys.aedt.core.desktop.Desktop.disable_optimetrics")()  | Disable optimetrics.  |  
| [`Desktop.enable_autosave`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.enable_autosave.html#ansys.aedt.core.desktop.Desktop.enable_autosave "ansys.aedt.core.desktop.Desktop.enable_autosave")()  | Enable the autosave option.  |  
| [`Desktop.enable_optimetrics`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.enable_optimetrics.html#ansys.aedt.core.desktop.Desktop.enable_optimetrics "ansys.aedt.core.desktop.Desktop.enable_optimetrics")()  | Enable optimetrics.  |  
| [`Desktop.get_available_toolkits`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.get_available_toolkits.html#ansys.aedt.core.desktop.Desktop.get_available_toolkits "ansys.aedt.core.desktop.Desktop.get_available_toolkits")()  | Get toolkit ready for installation.  |  
| [`Desktop.get_example`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.get_example.html#ansys.aedt.core.desktop.Desktop.get_example "ansys.aedt.core.desktop.Desktop.get_example")(example_name[, folder_name])  | Retrieve the path to a built-in example project.  |  
| [`Desktop.get_monitor_data`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.get_monitor_data.html#ansys.aedt.core.desktop.Desktop.get_monitor_data "ansys.aedt.core.desktop.Desktop.get_monitor_data")()  | Check and get monitor data of an existing analysis.  |  
| [`Desktop.job_status`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.job_status.html#ansys.aedt.core.desktop.Desktop.job_status "ansys.aedt.core.desktop.Desktop.job_status")()  | Get job status from job monitor.  |  
| [`Desktop.launch_job_monitor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.launch_job_monitor.html#ansys.aedt.core.desktop.Desktop.launch_job_monitor "ansys.aedt.core.desktop.Desktop.launch_job_monitor")(input_file)  | Launch job monitor.  |  
| [`Desktop.load_project`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.load_project.html#ansys.aedt.core.desktop.Desktop.load_project "ansys.aedt.core.desktop.Desktop.load_project")(project_file[, design_name])  | Open an AEDT project based on a project and optional design.  |  
| [`Desktop.project_path`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.project_path.html#ansys.aedt.core.desktop.Desktop.project_path "ansys.aedt.core.desktop.Desktop.project_path")([project_name])  | Get the path to the project.  |  
| [`Desktop.release_desktop`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.release_desktop.html#ansys.aedt.core.desktop.Desktop.release_desktop "ansys.aedt.core.desktop.Desktop.release_desktop")([close_projects, ...])  | Release AEDT.  |  
| [`Desktop.save_project`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.save_project.html#ansys.aedt.core.desktop.Desktop.save_project "ansys.aedt.core.desktop.Desktop.save_project")([project_name, ...])  | Save the project.  |  
| [`Desktop.select_scheduler`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.select_scheduler.html#ansys.aedt.core.desktop.Desktop.select_scheduler "ansys.aedt.core.desktop.Desktop.select_scheduler")(scheduler_type[, ...])  | Select a scheduler to submit the job.  |  
| [`Desktop.stop_simulations`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.stop_simulations.html#ansys.aedt.core.desktop.Desktop.stop_simulations "ansys.aedt.core.desktop.Desktop.stop_simulations")([clean_stop])  | Check if there are simulation running and stops them.  |  
| [`Desktop.submit_job`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.submit_job.html#ansys.aedt.core.desktop.Desktop.submit_job "ansys.aedt.core.desktop.Desktop.submit_job")(project_file[, ...])  | Submit a job to be solved on a cluster.  |  
Attributes  
| [`Desktop.active_design_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.active_design_name.html#ansys.aedt.core.desktop.Desktop.active_design_name "ansys.aedt.core.desktop.Desktop.active_design_name")  | Get the display name of the active design.  |  
| --- | --- |  
| [`Desktop.active_project_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.active_project_name.html#ansys.aedt.core.desktop.Desktop.active_project_name "ansys.aedt.core.desktop.Desktop.active_project_name")  | Get the name of the active project.  |  
| [`Desktop.aedt_install_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.aedt_install_dir.html#ansys.aedt.core.desktop.Desktop.aedt_install_dir "ansys.aedt.core.desktop.Desktop.aedt_install_dir")  | AEDT installation path.  |  
| [`Desktop.aedt_process_id`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.aedt_process_id.html#ansys.aedt.core.desktop.Desktop.aedt_process_id "ansys.aedt.core.desktop.Desktop.aedt_process_id")  | Retrieve AEDT process id.  |  
| [`Desktop.aedt_version`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.aedt_version.html#ansys.aedt.core.desktop.Desktop.aedt_version "ansys.aedt.core.desktop.Desktop.aedt_version")  | Retrieve AEDT version from AEDT.  |  
| [`Desktop.aedt_version_id`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.aedt_version_id.html#ansys.aedt.core.desktop.Desktop.aedt_version_id "ansys.aedt.core.desktop.Desktop.aedt_version_id")  | Retrieve AEDT version id.  |  
| [`Desktop.aedt_version_string`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.aedt_version_string.html#ansys.aedt.core.desktop.Desktop.aedt_version_string "ansys.aedt.core.desktop.Desktop.aedt_version_string")  | AEDT version string.  |  
| [`Desktop.are_there_simulations_running`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.are_there_simulations_running.html#ansys.aedt.core.desktop.Desktop.are_there_simulations_running "ansys.aedt.core.desktop.Desktop.are_there_simulations_running")  | Check if there are simulation running.  |  
| [`Desktop.close_on_exit`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.close_on_exit.html#ansys.aedt.core.desktop.Desktop.close_on_exit "ansys.aedt.core.desktop.Desktop.close_on_exit")  | Whether AEDT will close on exit.  |  
| [`Desktop.current_student_version`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.current_student_version.html#ansys.aedt.core.desktop.Desktop.current_student_version "ansys.aedt.core.desktop.Desktop.current_student_version")  | Current AEDT student version.  |  
| [`Desktop.current_version`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.current_version.html#ansys.aedt.core.desktop.Desktop.current_version "ansys.aedt.core.desktop.Desktop.current_version")  | Current AEDT version.  |  
| [`Desktop.global_project_directory`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.global_project_directory.html#ansys.aedt.core.desktop.Desktop.global_project_directory "ansys.aedt.core.desktop.Desktop.global_project_directory")  | AEDT project directory.  |  
| [`Desktop.grpc_mode`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.grpc_mode.html#ansys.aedt.core.desktop.Desktop.grpc_mode "ansys.aedt.core.desktop.Desktop.grpc_mode")  | Retrieve gRPC mode.  |  
| [`Desktop.install_path`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.install_path.html#ansys.aedt.core.desktop.Desktop.install_path "ansys.aedt.core.desktop.Desktop.install_path")  | Installation path for AEDT.  |  
| [`Desktop.installed_versions`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.installed_versions.html#ansys.aedt.core.desktop.Desktop.installed_versions "ansys.aedt.core.desktop.Desktop.installed_versions")  | Dictionary of AEDT versions installed on the system and their installation paths.  |  
| [`Desktop.is_grpc_api`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.is_grpc_api.html#ansys.aedt.core.desktop.Desktop.is_grpc_api "ansys.aedt.core.desktop.Desktop.is_grpc_api")  | Whether the connection is through gRPC API.  |  
| [`Desktop.launched_by_pyaedt`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.launched_by_pyaedt.html#ansys.aedt.core.desktop.Desktop.launched_by_pyaedt "ansys.aedt.core.desktop.Desktop.launched_by_pyaedt")  | Flag to check if AEDT was launched by PyAEDT.  |  
| [`Desktop.logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.logger.html#ansys.aedt.core.desktop.Desktop.logger "ansys.aedt.core.desktop.Desktop.logger")  | AEDT logger.  |  
| [`Desktop.machine`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.machine.html#ansys.aedt.core.desktop.Desktop.machine "ansys.aedt.core.desktop.Desktop.machine")  | Machine name.  |  
| [`Desktop.messenger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.messenger.html#ansys.aedt.core.desktop.Desktop.messenger "ansys.aedt.core.desktop.Desktop.messenger")  | Messenger manager for the AEDT logger.  |  
| [`Desktop.new_desktop`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.new_desktop.html#ansys.aedt.core.desktop.Desktop.new_desktop "ansys.aedt.core.desktop.Desktop.new_desktop")  | Whether a new session will be started or not.  |  
| [`Desktop.non_graphical`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.non_graphical.html#ansys.aedt.core.desktop.Desktop.non_graphical "ansys.aedt.core.desktop.Desktop.non_graphical")  | Whether AEDT is running in non-graphical mode.  |  
| [`Desktop.odesktop`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.odesktop.html#ansys.aedt.core.desktop.Desktop.odesktop "ansys.aedt.core.desktop.Desktop.odesktop")  | AEDT instance containing all projects and designs.  |  
| [`Desktop.personallib`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.personallib.html#ansys.aedt.core.desktop.Desktop.personallib "ansys.aedt.core.desktop.Desktop.personallib")  | PersonalLib directory.  |  
| [`Desktop.port`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.port.html#ansys.aedt.core.desktop.Desktop.port "ansys.aedt.core.desktop.Desktop.port")  | Port number.  |  
| [`Desktop.project_list`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.project_list.html#ansys.aedt.core.desktop.Desktop.project_list "ansys.aedt.core.desktop.Desktop.project_list")  | Get a list of projects.  |  
| [`Desktop.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.public_dir.html#ansys.aedt.core.desktop.Desktop.public_dir "ansys.aedt.core.desktop.Desktop.public_dir")  | Shortcut for dir(self).  |  
| [`Desktop.pyaedt_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.pyaedt_dir.html#ansys.aedt.core.desktop.Desktop.pyaedt_dir "ansys.aedt.core.desktop.Desktop.pyaedt_dir")  | PyAEDT directory.  |  
| [`Desktop.src_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.src_dir.html#ansys.aedt.core.desktop.Desktop.src_dir "ansys.aedt.core.desktop.Desktop.src_dir")  | Python source directory.  |  
| [`Desktop.student_version`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.student_version.html#ansys.aedt.core.desktop.Desktop.student_version "ansys.aedt.core.desktop.Desktop.student_version")  | Whether AEDT is the student version.  |  
| [`Desktop.syslib`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.syslib.html#ansys.aedt.core.desktop.Desktop.syslib "ansys.aedt.core.desktop.Desktop.syslib")  | SysLib directory.  |  
| [`Desktop.temp_directory`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.temp_directory.html#ansys.aedt.core.desktop.Desktop.temp_directory "ansys.aedt.core.desktop.Desktop.temp_directory")  | AEDT temp directory.  |  
| [`Desktop.userlib`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.userlib.html#ansys.aedt.core.desktop.Desktop.userlib "ansys.aedt.core.desktop.Desktop.userlib")  | UserLib directory.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.desktop.Desktop.rst.txt)

# Desktop 

class ansys.aedt.core.desktop.Desktop(_* args_, _** kwargs_) 
    
Provides the Ansys Electronics Desktop (AEDT) interface. 

Parameters: 
     

**version**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), [`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), [`float`](https://docs.python.org/3.11/library/functions.html#float "\(in Python v3.11\)"), `optional` 
    
Version of AEDT to use. The default is `None`, in which case the active setup or latest installed version is used. Examples of input values are `261`, `26.1`, `2026.1`, `"2026.1"`. 

**non_graphical**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to launch AEDT in non-graphical mode. The default is `False`, in which case AEDT is launched in graphical mode. This parameter is ignored when a script is launched within AEDT. 

**new_desktop**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to launch an instance of AEDT in a new thread, even if another instance of the `version` is active on the machine. The default is `True`. 

**close_on_exit**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to close AEDT on exit. The default is `None`, which means the behavior is chosen automatically:
  * If `Desktop` is used in a context manager (`with` statement), the context manager take precedence and AEDT will be closed on exit (equivalent to `close_on_exit=True`).
  * If PyAEDT actually starts a new AEDT session, the session will be closed on exit (`close_on_exit=True`).
  * If PyAEDT connects to an existing AEDT session, the session will not be closed on exit (`close_on_exit=False`).

A user-specified boolean (`True` or `False`) always overrides the automatic behavior. 

**When ``Desktop`` is used outside a context manager, the ``release_desktop`` method arguments offer**
    
finer control over releasing and closing behavior. 

**student_version**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to open the AEDT student version. The default is `False`. 

**machine**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Machine name to connect the oDesktop session to. This parameter works only in 2022 R2 and later. The remote server must be up and running with the command `"ansysedt.exe -grpcsrv portnum"`. If the machine is `"localhost"`, the server also starts if not present. 

**port**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Port number on which to start the oDesktop communication on the already existing server. This parameter is ignored when creating a new server. It works only in 2022 R2 and later. The remote server must be up and running with the command `"ansysedt.exe -grpcsrv portnum"`. 

**aedt_process_id**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Process ID for the instance of AEDT to point PyAEDT at. The default is `None`. This parameter is only used when `new_desktop = False`.
Examples
Launch AEDT 2026 R1 in non-graphical mode and initialize HFSS.

```
>>> import ansys.aedt.core
>>> desktop = ansys.aedt.core.Desktop(version="2026.1", non_graphical=False)
PyAEDT INFO: pyaedt v...
PyAEDT INFO: Python version ...
>>> hfss = ansys.aedt.core.Hfss(design="HFSSDesign1")
PyAEDT INFO: Project...
PyAEDT INFO: Added design 'HFSSDesign1' of type HFSS.

```
Copy to clipboard
Launch AEDT 2025 R1 in graphical mode and initialize HFSS.

```
>>> desktop = Desktop(261)
PyAEDT INFO: pyaedt v...
PyAEDT INFO: Python version ...
>>> hfss = ansys.aedt.core.Hfss(design="HFSSDesign1")
PyAEDT INFO: No project is defined. Project...

```
Copy to clipboard
Methods  
| [`Desktop.active_design`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.active_design.html#ansys.aedt.core.desktop.Desktop.active_design "ansys.aedt.core.desktop.Desktop.active_design")([project_object, ...])  | Get the active design.  |  
| --- | --- |  
| [`Desktop.active_project`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.active_project.html#ansys.aedt.core.desktop.Desktop.active_project "ansys.aedt.core.desktop.Desktop.active_project")([name])  | Get the active project.  |  
| [`Desktop.analyze_all`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.analyze_all.html#ansys.aedt.core.desktop.Desktop.analyze_all "ansys.aedt.core.desktop.Desktop.analyze_all")([project, design])  | Analyze all setups in a project.  |  
| [`Desktop.change_active_dso_config_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.change_active_dso_config_name.html#ansys.aedt.core.desktop.Desktop.change_active_dso_config_name "ansys.aedt.core.desktop.Desktop.change_active_dso_config_name")([...])  | Change a specific registry key to a new value.  |  
| [`Desktop.change_license_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.change_license_type.html#ansys.aedt.core.desktop.Desktop.change_license_type "ansys.aedt.core.desktop.Desktop.change_license_type")([license_type])  | Change the license type.  |  
| [`Desktop.change_registry_from_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.change_registry_from_file.html#ansys.aedt.core.desktop.Desktop.change_registry_from_file "ansys.aedt.core.desktop.Desktop.change_registry_from_file")(registry_file)  | Apply desktop registry settings from an ACF file.  |  
| [`Desktop.change_registry_key`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.change_registry_key.html#ansys.aedt.core.desktop.Desktop.change_registry_key "ansys.aedt.core.desktop.Desktop.change_registry_key")(key_full_name, ...)  | Change an AEDT registry key to a new value.  |  
| [`Desktop.check_starting_mode`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.check_starting_mode.html#ansys.aedt.core.desktop.Desktop.check_starting_mode "ansys.aedt.core.desktop.Desktop.check_starting_mode")()  | Check the starting mode.  |  
| [`Desktop.clear_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.clear_messages.html#ansys.aedt.core.desktop.Desktop.clear_messages "ansys.aedt.core.desktop.Desktop.clear_messages")()  | Clear all AEDT messages.  |  
| [`Desktop.close_desktop`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.close_desktop.html#ansys.aedt.core.desktop.Desktop.close_desktop "ansys.aedt.core.desktop.Desktop.close_desktop")()  | Close all projects and shut down AEDT.  |  
| [`Desktop.close_windows`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.close_windows.html#ansys.aedt.core.desktop.Desktop.close_windows "ansys.aedt.core.desktop.Desktop.close_windows")()  | Close all windows.  |  
| [`Desktop.design_list`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.design_list.html#ansys.aedt.core.desktop.Desktop.design_list "ansys.aedt.core.desktop.Desktop.design_list")([project])  | Get a list of the designs.  |  
| [`Desktop.design_type`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.design_type.html#ansys.aedt.core.desktop.Desktop.design_type "ansys.aedt.core.desktop.Desktop.design_type")([project_name, design_name])  | Get the type of design.  |  
| [`Desktop.disable_autosave`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.disable_autosave.html#ansys.aedt.core.desktop.Desktop.disable_autosave "ansys.aedt.core.desktop.Desktop.disable_autosave")()  | Disable the autosave option.  |  
| [`Desktop.disable_optimetrics`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.disable_optimetrics.html#ansys.aedt.core.desktop.Desktop.disable_optimetrics "ansys.aedt.core.desktop.Desktop.disable_optimetrics")()  | Disable optimetrics.  |  
| [`Desktop.enable_autosave`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.enable_autosave.html#ansys.aedt.core.desktop.Desktop.enable_autosave "ansys.aedt.core.desktop.Desktop.enable_autosave")()  | Enable the autosave option.  |  
| [`Desktop.enable_optimetrics`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.enable_optimetrics.html#ansys.aedt.core.desktop.Desktop.enable_optimetrics "ansys.aedt.core.desktop.Desktop.enable_optimetrics")()  | Enable optimetrics.  |  
| [`Desktop.get_available_toolkits`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.get_available_toolkits.html#ansys.aedt.core.desktop.Desktop.get_available_toolkits "ansys.aedt.core.desktop.Desktop.get_available_toolkits")()  | Get toolkit ready for installation.  |  
| [`Desktop.get_example`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.get_example.html#ansys.aedt.core.desktop.Desktop.get_example "ansys.aedt.core.desktop.Desktop.get_example")(example_name[, folder_name])  | Retrieve the path to a built-in example project.  |  
| [`Desktop.get_monitor_data`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.get_monitor_data.html#ansys.aedt.core.desktop.Desktop.get_monitor_data "ansys.aedt.core.desktop.Desktop.get_monitor_data")()  | Check and get monitor data of an existing analysis.  |  
| [`Desktop.job_status`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.job_status.html#ansys.aedt.core.desktop.Desktop.job_status "ansys.aedt.core.desktop.Desktop.job_status")()  | Get job status from job monitor.  |  
| [`Desktop.launch_job_monitor`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.launch_job_monitor.html#ansys.aedt.core.desktop.Desktop.launch_job_monitor "ansys.aedt.core.desktop.Desktop.launch_job_monitor")(input_file)  | Launch job monitor.  |  
| [`Desktop.load_project`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.load_project.html#ansys.aedt.core.desktop.Desktop.load_project "ansys.aedt.core.desktop.Desktop.load_project")(project_file[, design_name])  | Open an AEDT project based on a project and optional design.  |  
| [`Desktop.project_path`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.project_path.html#ansys.aedt.core.desktop.Desktop.project_path "ansys.aedt.core.desktop.Desktop.project_path")([project_name])  | Get the path to the project.  |  
| [`Desktop.release_desktop`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.release_desktop.html#ansys.aedt.core.desktop.Desktop.release_desktop "ansys.aedt.core.desktop.Desktop.release_desktop")([close_projects, ...])  | Release AEDT.  |  
| [`Desktop.save_project`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.save_project.html#ansys.aedt.core.desktop.Desktop.save_project "ansys.aedt.core.desktop.Desktop.save_project")([project_name, ...])  | Save the project.  |  
| [`Desktop.select_scheduler`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.select_scheduler.html#ansys.aedt.core.desktop.Desktop.select_scheduler "ansys.aedt.core.desktop.Desktop.select_scheduler")(scheduler_type[, ...])  | Select a scheduler to submit the job.  |  
| [`Desktop.stop_simulations`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.stop_simulations.html#ansys.aedt.core.desktop.Desktop.stop_simulations "ansys.aedt.core.desktop.Desktop.stop_simulations")([clean_stop])  | Check if there are simulation running and stops them.  |  
| [`Desktop.submit_job`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.submit_job.html#ansys.aedt.core.desktop.Desktop.submit_job "ansys.aedt.core.desktop.Desktop.submit_job")(project_file[, ...])  | Submit a job to be solved on a cluster.  |  
Attributes  
| [`Desktop.active_design_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.active_design_name.html#ansys.aedt.core.desktop.Desktop.active_design_name "ansys.aedt.core.desktop.Desktop.active_design_name")  | Get the display name of the active design.  |  
| --- | --- |  
| [`Desktop.active_project_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.active_project_name.html#ansys.aedt.core.desktop.Desktop.active_project_name "ansys.aedt.core.desktop.Desktop.active_project_name")  | Get the name of the active project.  |  
| [`Desktop.aedt_install_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.aedt_install_dir.html#ansys.aedt.core.desktop.Desktop.aedt_install_dir "ansys.aedt.core.desktop.Desktop.aedt_install_dir")  | AEDT installation path.  |  
| [`Desktop.aedt_process_id`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.aedt_process_id.html#ansys.aedt.core.desktop.Desktop.aedt_process_id "ansys.aedt.core.desktop.Desktop.aedt_process_id")  | Retrieve AEDT process id.  |  
| [`Desktop.aedt_version`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.aedt_version.html#ansys.aedt.core.desktop.Desktop.aedt_version "ansys.aedt.core.desktop.Desktop.aedt_version")  | Retrieve AEDT version from AEDT.  |  
| [`Desktop.aedt_version_id`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.aedt_version_id.html#ansys.aedt.core.desktop.Desktop.aedt_version_id "ansys.aedt.core.desktop.Desktop.aedt_version_id")  | Retrieve AEDT version id.  |  
| [`Desktop.aedt_version_string`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.aedt_version_string.html#ansys.aedt.core.desktop.Desktop.aedt_version_string "ansys.aedt.core.desktop.Desktop.aedt_version_string")  | AEDT version string.  |  
| [`Desktop.are_there_simulations_running`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.are_there_simulations_running.html#ansys.aedt.core.desktop.Desktop.are_there_simulations_running "ansys.aedt.core.desktop.Desktop.are_there_simulations_running")  | Check if there are simulation running.  |  
| [`Desktop.close_on_exit`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.close_on_exit.html#ansys.aedt.core.desktop.Desktop.close_on_exit "ansys.aedt.core.desktop.Desktop.close_on_exit")  | Whether AEDT will close on exit.  |  
| [`Desktop.current_student_version`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.current_student_version.html#ansys.aedt.core.desktop.Desktop.current_student_version "ansys.aedt.core.desktop.Desktop.current_student_version")  | Current AEDT student version.  |  
| [`Desktop.current_version`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.current_version.html#ansys.aedt.core.desktop.Desktop.current_version "ansys.aedt.core.desktop.Desktop.current_version")  | Current AEDT version.  |  
| [`Desktop.global_project_directory`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.global_project_directory.html#ansys.aedt.core.desktop.Desktop.global_project_directory "ansys.aedt.core.desktop.Desktop.global_project_directory")  | AEDT project directory.  |  
| [`Desktop.grpc_mode`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.grpc_mode.html#ansys.aedt.core.desktop.Desktop.grpc_mode "ansys.aedt.core.desktop.Desktop.grpc_mode")  | Retrieve gRPC mode.  |  
| [`Desktop.install_path`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.install_path.html#ansys.aedt.core.desktop.Desktop.install_path "ansys.aedt.core.desktop.Desktop.install_path")  | Installation path for AEDT.  |  
| [`Desktop.installed_versions`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.installed_versions.html#ansys.aedt.core.desktop.Desktop.installed_versions "ansys.aedt.core.desktop.Desktop.installed_versions")  | Dictionary of AEDT versions installed on the system and their installation paths.  |  
| [`Desktop.is_grpc_api`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.is_grpc_api.html#ansys.aedt.core.desktop.Desktop.is_grpc_api "ansys.aedt.core.desktop.Desktop.is_grpc_api")  | Whether the connection is through gRPC API.  |  
| [`Desktop.launched_by_pyaedt`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.launched_by_pyaedt.html#ansys.aedt.core.desktop.Desktop.launched_by_pyaedt "ansys.aedt.core.desktop.Desktop.launched_by_pyaedt")  | Flag to check if AEDT was launched by PyAEDT.  |  
| [`Desktop.logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.logger.html#ansys.aedt.core.desktop.Desktop.logger "ansys.aedt.core.desktop.Desktop.logger")  | AEDT logger.  |  
| [`Desktop.machine`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.machine.html#ansys.aedt.core.desktop.Desktop.machine "ansys.aedt.core.desktop.Desktop.machine")  | Machine name.  |  
| [`Desktop.messenger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.messenger.html#ansys.aedt.core.desktop.Desktop.messenger "ansys.aedt.core.desktop.Desktop.messenger")  | Messenger manager for the AEDT logger.  |  
| [`Desktop.new_desktop`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.new_desktop.html#ansys.aedt.core.desktop.Desktop.new_desktop "ansys.aedt.core.desktop.Desktop.new_desktop")  | Whether a new session will be started or not.  |  
| [`Desktop.non_graphical`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.non_graphical.html#ansys.aedt.core.desktop.Desktop.non_graphical "ansys.aedt.core.desktop.Desktop.non_graphical")  | Whether AEDT is running in non-graphical mode.  |  
| [`Desktop.odesktop`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.odesktop.html#ansys.aedt.core.desktop.Desktop.odesktop "ansys.aedt.core.desktop.Desktop.odesktop")  | AEDT instance containing all projects and designs.  |  
| [`Desktop.personallib`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.personallib.html#ansys.aedt.core.desktop.Desktop.personallib "ansys.aedt.core.desktop.Desktop.personallib")  | PersonalLib directory.  |  
| [`Desktop.port`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.port.html#ansys.aedt.core.desktop.Desktop.port "ansys.aedt.core.desktop.Desktop.port")  | Port number.  |  
| [`Desktop.project_list`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.project_list.html#ansys.aedt.core.desktop.Desktop.project_list "ansys.aedt.core.desktop.Desktop.project_list")  | Get a list of projects.  |  
| [`Desktop.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.public_dir.html#ansys.aedt.core.desktop.Desktop.public_dir "ansys.aedt.core.desktop.Desktop.public_dir")  | Shortcut for dir(self).  |  
| [`Desktop.pyaedt_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.pyaedt_dir.html#ansys.aedt.core.desktop.Desktop.pyaedt_dir "ansys.aedt.core.desktop.Desktop.pyaedt_dir")  | PyAEDT directory.  |  
| [`Desktop.src_dir`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.src_dir.html#ansys.aedt.core.desktop.Desktop.src_dir "ansys.aedt.core.desktop.Desktop.src_dir")  | Python source directory.  |  
| [`Desktop.student_version`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.student_version.html#ansys.aedt.core.desktop.Desktop.student_version "ansys.aedt.core.desktop.Desktop.student_version")  | Whether AEDT is the student version.  |  
| [`Desktop.syslib`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.syslib.html#ansys.aedt.core.desktop.Desktop.syslib "ansys.aedt.core.desktop.Desktop.syslib")  | SysLib directory.  |  
| [`Desktop.temp_directory`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.temp_directory.html#ansys.aedt.core.desktop.Desktop.temp_directory "ansys.aedt.core.desktop.Desktop.temp_directory")  | AEDT temp directory.  |  
| [`Desktop.userlib`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.desktop.Desktop.userlib.html#ansys.aedt.core.desktop.Desktop.userlib "ansys.aedt.core.desktop.Desktop.userlib")  | UserLib directory.  |