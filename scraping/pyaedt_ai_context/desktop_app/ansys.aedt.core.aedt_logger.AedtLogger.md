---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# AedtLogger 

class ansys.aedt.core.aedt_logger.AedtLogger(_level =10_, _filename : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _to_stdout : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _desktop =None_) 
    
Specifies the logger to use for each AEDT logger.
This class allows you to add a handler to write messages to a file and to indicate whether to write mnessages to the standard output (stdout). 

Parameters: 
     

**level**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Logging level to filter the message severity allowed in the logger. The default is `logging.DEBUG`. 

**filename**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the file to write messages to. The default is `None`. 

**to_stdout**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to write log messages to stdout. The default is `False`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.logger.info("Info message")
>>> hfss.logger.warning("Warning message")

```
Copy to clipboard
Methods  
| [`AedtLogger.add_debug_message`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_debug_message.html#ansys.aedt.core.aedt_logger.AedtLogger.add_debug_message "ansys.aedt.core.aedt_logger.AedtLogger.add_debug_message")(message_text[, ...])  | Parameterized message to the message manager to specify the type and project or design level.  |  
| --- | --- |  
| [`AedtLogger.add_error_message`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_error_message.html#ansys.aedt.core.aedt_logger.AedtLogger.add_error_message "ansys.aedt.core.aedt_logger.AedtLogger.add_error_message")(message_text[, ...])  | Add a type 2 "Error" message to the message manager tree.  |  
| [`AedtLogger.add_file_logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_file_logger.html#ansys.aedt.core.aedt_logger.AedtLogger.add_file_logger "ansys.aedt.core.aedt_logger.AedtLogger.add_file_logger")(filename, ...[, ...])  | Add a new file to the logger handlers list.  |  
| [`AedtLogger.add_info_message`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_info_message.html#ansys.aedt.core.aedt_logger.AedtLogger.add_info_message "ansys.aedt.core.aedt_logger.AedtLogger.add_info_message")(message_text[, ...])  | Add a type 0 "Info" message to the active design level of the message manager tree.  |  
| [`AedtLogger.add_logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_logger.html#ansys.aedt.core.aedt_logger.AedtLogger.add_logger "ansys.aedt.core.aedt_logger.AedtLogger.add_logger")(destination[, level])  | Add a logger for either the active project or active design.  |  
| [`AedtLogger.add_message`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_message.html#ansys.aedt.core.aedt_logger.AedtLogger.add_message "ansys.aedt.core.aedt_logger.AedtLogger.add_message")(message_type, ...[, ...])  | Add a message to the message manager to specify the type and project or design level.  |  
| [`AedtLogger.add_warning_message`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_warning_message.html#ansys.aedt.core.aedt_logger.AedtLogger.add_warning_message "ansys.aedt.core.aedt_logger.AedtLogger.add_warning_message")(message_text)  | Add a type 1 "Warning" message to the message manager tree.  |  
| [`AedtLogger.clear_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.clear_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.clear_messages "ansys.aedt.core.aedt_logger.AedtLogger.clear_messages")([proj_name, ...])  | Clear all messages.  |  
| [`AedtLogger.debug`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.debug.html#ansys.aedt.core.aedt_logger.AedtLogger.debug "ansys.aedt.core.aedt_logger.AedtLogger.debug")(msg, *args, **kwargs)  | Write a debug message to the global logger.  |  
| [`AedtLogger.disable_desktop_log`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.disable_desktop_log.html#ansys.aedt.core.aedt_logger.AedtLogger.disable_desktop_log "ansys.aedt.core.aedt_logger.AedtLogger.disable_desktop_log")()  | Disable the log in AEDT.  |  
| [`AedtLogger.disable_log_on_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.disable_log_on_file.html#ansys.aedt.core.aedt_logger.AedtLogger.disable_log_on_file "ansys.aedt.core.aedt_logger.AedtLogger.disable_log_on_file")()  | Disable writing log messages to an output file.  |  
| [`AedtLogger.disable_stdout_log`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.disable_stdout_log.html#ansys.aedt.core.aedt_logger.AedtLogger.disable_stdout_log "ansys.aedt.core.aedt_logger.AedtLogger.disable_stdout_log")()  | Disable printing log messages to stdout.  |  
| [`AedtLogger.enable_desktop_log`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.enable_desktop_log.html#ansys.aedt.core.aedt_logger.AedtLogger.enable_desktop_log "ansys.aedt.core.aedt_logger.AedtLogger.enable_desktop_log")()  | Enable the log in AEDT.  |  
| [`AedtLogger.enable_log_on_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.enable_log_on_file.html#ansys.aedt.core.aedt_logger.AedtLogger.enable_log_on_file "ansys.aedt.core.aedt_logger.AedtLogger.enable_log_on_file")()  | Enable writing log messages to an output file.  |  
| [`AedtLogger.enable_stdout_log`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.enable_stdout_log.html#ansys.aedt.core.aedt_logger.AedtLogger.enable_stdout_log "ansys.aedt.core.aedt_logger.AedtLogger.enable_stdout_log")()  | Enable printing log messages to stdout.  |  
| [`AedtLogger.error`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.error.html#ansys.aedt.core.aedt_logger.AedtLogger.error "ansys.aedt.core.aedt_logger.AedtLogger.error")(msg, *args, **kwargs)  | Write an error message to the global logger.  |  
| [`AedtLogger.get_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.get_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.get_messages "ansys.aedt.core.aedt_logger.AedtLogger.get_messages")([project_name, ...])  | Get the message manager content for a specified project and design.  |  
| [`AedtLogger.info`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.info.html#ansys.aedt.core.aedt_logger.AedtLogger.info "ansys.aedt.core.aedt_logger.AedtLogger.info")(msg, *args, **kwargs)  | Write an info message to the global logger.  |  
| [`AedtLogger.info_timer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.info_timer.html#ansys.aedt.core.aedt_logger.AedtLogger.info_timer "ansys.aedt.core.aedt_logger.AedtLogger.info_timer")(msg[, start_time])  | Write an info message to the global logger with elapsed time.  |  
| [`AedtLogger.remove_all_project_file_logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.remove_all_project_file_logger.html#ansys.aedt.core.aedt_logger.AedtLogger.remove_all_project_file_logger "ansys.aedt.core.aedt_logger.AedtLogger.remove_all_project_file_logger")()  | Remove all the local files from the logger handlers list.  |  
| [`AedtLogger.remove_file_logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.remove_file_logger.html#ansys.aedt.core.aedt_logger.AedtLogger.remove_file_logger "ansys.aedt.core.aedt_logger.AedtLogger.remove_file_logger")(project_name)  | Remove a file from the logger handlers list.  |  
| [`AedtLogger.reset_timer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.reset_timer.html#ansys.aedt.core.aedt_logger.AedtLogger.reset_timer "ansys.aedt.core.aedt_logger.AedtLogger.reset_timer")([time_val])  | Reset actual timer to actual time or specified time.  |  
| [`AedtLogger.suspend_logging`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.suspend_logging.html#ansys.aedt.core.aedt_logger.AedtLogger.suspend_logging "ansys.aedt.core.aedt_logger.AedtLogger.suspend_logging")()  | Temporarily disable all logs and restore them afterward.  |  
| [`AedtLogger.warning`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.warning.html#ansys.aedt.core.aedt_logger.AedtLogger.warning "ansys.aedt.core.aedt_logger.AedtLogger.warning")(msg, *args, **kwargs)  | Write a warning message to the global logger.  |  
Attributes  
| [`AedtLogger.aedt_error_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.aedt_error_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.aedt_error_messages "ansys.aedt.core.aedt_logger.AedtLogger.aedt_error_messages")  | Message manager content for the active project and design.  |  
| --- | --- |  
| [`AedtLogger.aedt_info_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.aedt_info_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.aedt_info_messages "ansys.aedt.core.aedt_logger.AedtLogger.aedt_info_messages")  | Message manager content for the active project and design.  |  
| [`AedtLogger.aedt_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.aedt_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.aedt_messages "ansys.aedt.core.aedt_logger.AedtLogger.aedt_messages")  | Message manager content for the active project and design.  |  
| [`AedtLogger.aedt_warning_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.aedt_warning_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.aedt_warning_messages "ansys.aedt.core.aedt_logger.AedtLogger.aedt_warning_messages")  | Message manager content for the active project and design.  |  
| [`AedtLogger.design_logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.design_logger.html#ansys.aedt.core.aedt_logger.AedtLogger.design_logger "ansys.aedt.core.aedt_logger.AedtLogger.design_logger")  | Design logger.  |  
| [`AedtLogger.design_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.design_name.html#ansys.aedt.core.aedt_logger.AedtLogger.design_name "ansys.aedt.core.aedt_logger.AedtLogger.design_name")  | Name of current logger design.  |  
| [`AedtLogger.error_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.error_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.error_messages "ansys.aedt.core.aedt_logger.AedtLogger.error_messages")  | Message manager content for the active pyaedt session.  |  
| [`AedtLogger.glb`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.glb.html#ansys.aedt.core.aedt_logger.AedtLogger.glb "ansys.aedt.core.aedt_logger.AedtLogger.glb")  | Global logger.  |  
| [`AedtLogger.info_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.info_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.info_messages "ansys.aedt.core.aedt_logger.AedtLogger.info_messages")  | Message manager content for the active pyaedt session.  |  
| [`AedtLogger.log_on_desktop`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.log_on_desktop.html#ansys.aedt.core.aedt_logger.AedtLogger.log_on_desktop "ansys.aedt.core.aedt_logger.AedtLogger.log_on_desktop")  | Status of the log in AEDT (Message Manager).  |  
| [`AedtLogger.log_on_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.log_on_file.html#ansys.aedt.core.aedt_logger.AedtLogger.log_on_file "ansys.aedt.core.aedt_logger.AedtLogger.log_on_file")  | Status of printing log messages to a file.  |  
| [`AedtLogger.log_on_stdout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.log_on_stdout.html#ansys.aedt.core.aedt_logger.AedtLogger.log_on_stdout "ansys.aedt.core.aedt_logger.AedtLogger.log_on_stdout")  | Status of printing log messages to stdout.  |  
| [`AedtLogger.logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.logger.html#ansys.aedt.core.aedt_logger.AedtLogger.logger "ansys.aedt.core.aedt_logger.AedtLogger.logger")  | AEDT logger object.  |  
| [`AedtLogger.messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.messages.html#ansys.aedt.core.aedt_logger.AedtLogger.messages "ansys.aedt.core.aedt_logger.AedtLogger.messages")  | Message manager content for the active session.  |  
| [`AedtLogger.non_graphical`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.non_graphical.html#ansys.aedt.core.aedt_logger.AedtLogger.non_graphical "ansys.aedt.core.aedt_logger.AedtLogger.non_graphical")  | Check if desktop is graphical or not.  |  
| [`AedtLogger.odesign`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.odesign.html#ansys.aedt.core.aedt_logger.AedtLogger.odesign "ansys.aedt.core.aedt_logger.AedtLogger.odesign")  | Design object.  |  
| [`AedtLogger.oproject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.oproject.html#ansys.aedt.core.aedt_logger.AedtLogger.oproject "ansys.aedt.core.aedt_logger.AedtLogger.oproject")  | Project object.  |  
| [`AedtLogger.project_logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.project_logger.html#ansys.aedt.core.aedt_logger.AedtLogger.project_logger "ansys.aedt.core.aedt_logger.AedtLogger.project_logger")  | Project logger.  |  
| [`AedtLogger.project_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.project_name.html#ansys.aedt.core.aedt_logger.AedtLogger.project_name "ansys.aedt.core.aedt_logger.AedtLogger.project_name")  | Name of current logger project.  |  
| [`AedtLogger.warning_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.warning_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.warning_messages "ansys.aedt.core.aedt_logger.AedtLogger.warning_messages")  | Message manager content for the active pyaedt session.  |  
# AedtLogger 

class ansys.aedt.core.aedt_logger.AedtLogger(_level =10_, _filename : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _to_stdout : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _desktop =None_) 
    
Specifies the logger to use for each AEDT logger.
This class allows you to add a handler to write messages to a file and to indicate whether to write mnessages to the standard output (stdout). 

Parameters: 
     

**level**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Logging level to filter the message severity allowed in the logger. The default is `logging.DEBUG`. 

**filename**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the file to write messages to. The default is `None`. 

**to_stdout**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to write log messages to stdout. The default is `False`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.logger.info("Info message")
>>> hfss.logger.warning("Warning message")

```
Copy to clipboard
Methods  
| [`AedtLogger.add_debug_message`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_debug_message.html#ansys.aedt.core.aedt_logger.AedtLogger.add_debug_message "ansys.aedt.core.aedt_logger.AedtLogger.add_debug_message")(message_text[, ...])  | Parameterized message to the message manager to specify the type and project or design level.  |  
| --- | --- |  
| [`AedtLogger.add_error_message`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_error_message.html#ansys.aedt.core.aedt_logger.AedtLogger.add_error_message "ansys.aedt.core.aedt_logger.AedtLogger.add_error_message")(message_text[, ...])  | Add a type 2 "Error" message to the message manager tree.  |  
| [`AedtLogger.add_file_logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_file_logger.html#ansys.aedt.core.aedt_logger.AedtLogger.add_file_logger "ansys.aedt.core.aedt_logger.AedtLogger.add_file_logger")(filename, ...[, ...])  | Add a new file to the logger handlers list.  |  
| [`AedtLogger.add_info_message`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_info_message.html#ansys.aedt.core.aedt_logger.AedtLogger.add_info_message "ansys.aedt.core.aedt_logger.AedtLogger.add_info_message")(message_text[, ...])  | Add a type 0 "Info" message to the active design level of the message manager tree.  |  
| [`AedtLogger.add_logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_logger.html#ansys.aedt.core.aedt_logger.AedtLogger.add_logger "ansys.aedt.core.aedt_logger.AedtLogger.add_logger")(destination[, level])  | Add a logger for either the active project or active design.  |  
| [`AedtLogger.add_message`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_message.html#ansys.aedt.core.aedt_logger.AedtLogger.add_message "ansys.aedt.core.aedt_logger.AedtLogger.add_message")(message_type, ...[, ...])  | Add a message to the message manager to specify the type and project or design level.  |  
| [`AedtLogger.add_warning_message`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_warning_message.html#ansys.aedt.core.aedt_logger.AedtLogger.add_warning_message "ansys.aedt.core.aedt_logger.AedtLogger.add_warning_message")(message_text)  | Add a type 1 "Warning" message to the message manager tree.  |  
| [`AedtLogger.clear_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.clear_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.clear_messages "ansys.aedt.core.aedt_logger.AedtLogger.clear_messages")([proj_name, ...])  | Clear all messages.  |  
| [`AedtLogger.debug`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.debug.html#ansys.aedt.core.aedt_logger.AedtLogger.debug "ansys.aedt.core.aedt_logger.AedtLogger.debug")(msg, *args, **kwargs)  | Write a debug message to the global logger.  |  
| [`AedtLogger.disable_desktop_log`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.disable_desktop_log.html#ansys.aedt.core.aedt_logger.AedtLogger.disable_desktop_log "ansys.aedt.core.aedt_logger.AedtLogger.disable_desktop_log")()  | Disable the log in AEDT.  |  
| [`AedtLogger.disable_log_on_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.disable_log_on_file.html#ansys.aedt.core.aedt_logger.AedtLogger.disable_log_on_file "ansys.aedt.core.aedt_logger.AedtLogger.disable_log_on_file")()  | Disable writing log messages to an output file.  |  
| [`AedtLogger.disable_stdout_log`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.disable_stdout_log.html#ansys.aedt.core.aedt_logger.AedtLogger.disable_stdout_log "ansys.aedt.core.aedt_logger.AedtLogger.disable_stdout_log")()  | Disable printing log messages to stdout.  |  
| [`AedtLogger.enable_desktop_log`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.enable_desktop_log.html#ansys.aedt.core.aedt_logger.AedtLogger.enable_desktop_log "ansys.aedt.core.aedt_logger.AedtLogger.enable_desktop_log")()  | Enable the log in AEDT.  |  
| [`AedtLogger.enable_log_on_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.enable_log_on_file.html#ansys.aedt.core.aedt_logger.AedtLogger.enable_log_on_file "ansys.aedt.core.aedt_logger.AedtLogger.enable_log_on_file")()  | Enable writing log messages to an output file.  |  
| [`AedtLogger.enable_stdout_log`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.enable_stdout_log.html#ansys.aedt.core.aedt_logger.AedtLogger.enable_stdout_log "ansys.aedt.core.aedt_logger.AedtLogger.enable_stdout_log")()  | Enable printing log messages to stdout.  |  
| [`AedtLogger.error`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.error.html#ansys.aedt.core.aedt_logger.AedtLogger.error "ansys.aedt.core.aedt_logger.AedtLogger.error")(msg, *args, **kwargs)  | Write an error message to the global logger.  |  
| [`AedtLogger.get_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.get_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.get_messages "ansys.aedt.core.aedt_logger.AedtLogger.get_messages")([project_name, ...])  | Get the message manager content for a specified project and design.  |  
| [`AedtLogger.info`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.info.html#ansys.aedt.core.aedt_logger.AedtLogger.info "ansys.aedt.core.aedt_logger.AedtLogger.info")(msg, *args, **kwargs)  | Write an info message to the global logger.  |  
| [`AedtLogger.info_timer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.info_timer.html#ansys.aedt.core.aedt_logger.AedtLogger.info_timer "ansys.aedt.core.aedt_logger.AedtLogger.info_timer")(msg[, start_time])  | Write an info message to the global logger with elapsed time.  |  
| [`AedtLogger.remove_all_project_file_logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.remove_all_project_file_logger.html#ansys.aedt.core.aedt_logger.AedtLogger.remove_all_project_file_logger "ansys.aedt.core.aedt_logger.AedtLogger.remove_all_project_file_logger")()  | Remove all the local files from the logger handlers list.  |  
| [`AedtLogger.remove_file_logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.remove_file_logger.html#ansys.aedt.core.aedt_logger.AedtLogger.remove_file_logger "ansys.aedt.core.aedt_logger.AedtLogger.remove_file_logger")(project_name)  | Remove a file from the logger handlers list.  |  
| [`AedtLogger.reset_timer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.reset_timer.html#ansys.aedt.core.aedt_logger.AedtLogger.reset_timer "ansys.aedt.core.aedt_logger.AedtLogger.reset_timer")([time_val])  | Reset actual timer to actual time or specified time.  |  
| [`AedtLogger.suspend_logging`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.suspend_logging.html#ansys.aedt.core.aedt_logger.AedtLogger.suspend_logging "ansys.aedt.core.aedt_logger.AedtLogger.suspend_logging")()  | Temporarily disable all logs and restore them afterward.  |  
| [`AedtLogger.warning`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.warning.html#ansys.aedt.core.aedt_logger.AedtLogger.warning "ansys.aedt.core.aedt_logger.AedtLogger.warning")(msg, *args, **kwargs)  | Write a warning message to the global logger.  |  
Attributes  
| [`AedtLogger.aedt_error_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.aedt_error_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.aedt_error_messages "ansys.aedt.core.aedt_logger.AedtLogger.aedt_error_messages")  | Message manager content for the active project and design.  |  
| --- | --- |  
| [`AedtLogger.aedt_info_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.aedt_info_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.aedt_info_messages "ansys.aedt.core.aedt_logger.AedtLogger.aedt_info_messages")  | Message manager content for the active project and design.  |  
| [`AedtLogger.aedt_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.aedt_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.aedt_messages "ansys.aedt.core.aedt_logger.AedtLogger.aedt_messages")  | Message manager content for the active project and design.  |  
| [`AedtLogger.aedt_warning_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.aedt_warning_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.aedt_warning_messages "ansys.aedt.core.aedt_logger.AedtLogger.aedt_warning_messages")  | Message manager content for the active project and design.  |  
| [`AedtLogger.design_logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.design_logger.html#ansys.aedt.core.aedt_logger.AedtLogger.design_logger "ansys.aedt.core.aedt_logger.AedtLogger.design_logger")  | Design logger.  |  
| [`AedtLogger.design_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.design_name.html#ansys.aedt.core.aedt_logger.AedtLogger.design_name "ansys.aedt.core.aedt_logger.AedtLogger.design_name")  | Name of current logger design.  |  
| [`AedtLogger.error_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.error_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.error_messages "ansys.aedt.core.aedt_logger.AedtLogger.error_messages")  | Message manager content for the active pyaedt session.  |  
| [`AedtLogger.glb`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.glb.html#ansys.aedt.core.aedt_logger.AedtLogger.glb "ansys.aedt.core.aedt_logger.AedtLogger.glb")  | Global logger.  |  
| [`AedtLogger.info_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.info_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.info_messages "ansys.aedt.core.aedt_logger.AedtLogger.info_messages")  | Message manager content for the active pyaedt session.  |  
| [`AedtLogger.log_on_desktop`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.log_on_desktop.html#ansys.aedt.core.aedt_logger.AedtLogger.log_on_desktop "ansys.aedt.core.aedt_logger.AedtLogger.log_on_desktop")  | Status of the log in AEDT (Message Manager).  |  
| [`AedtLogger.log_on_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.log_on_file.html#ansys.aedt.core.aedt_logger.AedtLogger.log_on_file "ansys.aedt.core.aedt_logger.AedtLogger.log_on_file")  | Status of printing log messages to a file.  |  
| [`AedtLogger.log_on_stdout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.log_on_stdout.html#ansys.aedt.core.aedt_logger.AedtLogger.log_on_stdout "ansys.aedt.core.aedt_logger.AedtLogger.log_on_stdout")  | Status of printing log messages to stdout.  |  
| [`AedtLogger.logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.logger.html#ansys.aedt.core.aedt_logger.AedtLogger.logger "ansys.aedt.core.aedt_logger.AedtLogger.logger")  | AEDT logger object.  |  
| [`AedtLogger.messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.messages.html#ansys.aedt.core.aedt_logger.AedtLogger.messages "ansys.aedt.core.aedt_logger.AedtLogger.messages")  | Message manager content for the active session.  |  
| [`AedtLogger.non_graphical`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.non_graphical.html#ansys.aedt.core.aedt_logger.AedtLogger.non_graphical "ansys.aedt.core.aedt_logger.AedtLogger.non_graphical")  | Check if desktop is graphical or not.  |  
| [`AedtLogger.odesign`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.odesign.html#ansys.aedt.core.aedt_logger.AedtLogger.odesign "ansys.aedt.core.aedt_logger.AedtLogger.odesign")  | Design object.  |  
| [`AedtLogger.oproject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.oproject.html#ansys.aedt.core.aedt_logger.AedtLogger.oproject "ansys.aedt.core.aedt_logger.AedtLogger.oproject")  | Project object.  |  
| [`AedtLogger.project_logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.project_logger.html#ansys.aedt.core.aedt_logger.AedtLogger.project_logger "ansys.aedt.core.aedt_logger.AedtLogger.project_logger")  | Project logger.  |  
| [`AedtLogger.project_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.project_name.html#ansys.aedt.core.aedt_logger.AedtLogger.project_name "ansys.aedt.core.aedt_logger.AedtLogger.project_name")  | Name of current logger project.  |  
| [`AedtLogger.warning_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.warning_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.warning_messages "ansys.aedt.core.aedt_logger.AedtLogger.warning_messages")  | Message manager content for the active pyaedt session.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.rst.txt)

# AedtLogger 

class ansys.aedt.core.aedt_logger.AedtLogger(_level =10_, _filename : [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") | [None](https://docs.python.org/3.11/library/constants.html#None "\(in Python v3.11\)") = None_, _to_stdout : [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") = False_, _desktop =None_) 
    
Specifies the logger to use for each AEDT logger.
This class allows you to add a handler to write messages to a file and to indicate whether to write mnessages to the standard output (stdout). 

Parameters: 
     

**level**[`int`](https://docs.python.org/3.11/library/functions.html#int "\(in Python v3.11\)"), `optional` 
    
Logging level to filter the message severity allowed in the logger. The default is `logging.DEBUG`. 

**filename**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)"), `optional` 
    
Name of the file to write messages to. The default is `None`. 

**to_stdout**[ bool](https://docs.python.org/3.11/library/stdtypes.html#bltin-boolean-values "\(in Python v3.11\)"), `optional` 
    
Whether to write log messages to stdout. The default is `False`.
Examples

```
>>> from ansys.aedt.core import Hfss
>>> hfss = Hfss()
>>> hfss.logger.info("Info message")
>>> hfss.logger.warning("Warning message")

```
Copy to clipboard
Methods  
| [`AedtLogger.add_debug_message`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_debug_message.html#ansys.aedt.core.aedt_logger.AedtLogger.add_debug_message "ansys.aedt.core.aedt_logger.AedtLogger.add_debug_message")(message_text[, ...])  | Parameterized message to the message manager to specify the type and project or design level.  |  
| --- | --- |  
| [`AedtLogger.add_error_message`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_error_message.html#ansys.aedt.core.aedt_logger.AedtLogger.add_error_message "ansys.aedt.core.aedt_logger.AedtLogger.add_error_message")(message_text[, ...])  | Add a type 2 "Error" message to the message manager tree.  |  
| [`AedtLogger.add_file_logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_file_logger.html#ansys.aedt.core.aedt_logger.AedtLogger.add_file_logger "ansys.aedt.core.aedt_logger.AedtLogger.add_file_logger")(filename, ...[, ...])  | Add a new file to the logger handlers list.  |  
| [`AedtLogger.add_info_message`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_info_message.html#ansys.aedt.core.aedt_logger.AedtLogger.add_info_message "ansys.aedt.core.aedt_logger.AedtLogger.add_info_message")(message_text[, ...])  | Add a type 0 "Info" message to the active design level of the message manager tree.  |  
| [`AedtLogger.add_logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_logger.html#ansys.aedt.core.aedt_logger.AedtLogger.add_logger "ansys.aedt.core.aedt_logger.AedtLogger.add_logger")(destination[, level])  | Add a logger for either the active project or active design.  |  
| [`AedtLogger.add_message`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_message.html#ansys.aedt.core.aedt_logger.AedtLogger.add_message "ansys.aedt.core.aedt_logger.AedtLogger.add_message")(message_type, ...[, ...])  | Add a message to the message manager to specify the type and project or design level.  |  
| [`AedtLogger.add_warning_message`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.add_warning_message.html#ansys.aedt.core.aedt_logger.AedtLogger.add_warning_message "ansys.aedt.core.aedt_logger.AedtLogger.add_warning_message")(message_text)  | Add a type 1 "Warning" message to the message manager tree.  |  
| [`AedtLogger.clear_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.clear_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.clear_messages "ansys.aedt.core.aedt_logger.AedtLogger.clear_messages")([proj_name, ...])  | Clear all messages.  |  
| [`AedtLogger.debug`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.debug.html#ansys.aedt.core.aedt_logger.AedtLogger.debug "ansys.aedt.core.aedt_logger.AedtLogger.debug")(msg, *args, **kwargs)  | Write a debug message to the global logger.  |  
| [`AedtLogger.disable_desktop_log`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.disable_desktop_log.html#ansys.aedt.core.aedt_logger.AedtLogger.disable_desktop_log "ansys.aedt.core.aedt_logger.AedtLogger.disable_desktop_log")()  | Disable the log in AEDT.  |  
| [`AedtLogger.disable_log_on_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.disable_log_on_file.html#ansys.aedt.core.aedt_logger.AedtLogger.disable_log_on_file "ansys.aedt.core.aedt_logger.AedtLogger.disable_log_on_file")()  | Disable writing log messages to an output file.  |  
| [`AedtLogger.disable_stdout_log`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.disable_stdout_log.html#ansys.aedt.core.aedt_logger.AedtLogger.disable_stdout_log "ansys.aedt.core.aedt_logger.AedtLogger.disable_stdout_log")()  | Disable printing log messages to stdout.  |  
| [`AedtLogger.enable_desktop_log`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.enable_desktop_log.html#ansys.aedt.core.aedt_logger.AedtLogger.enable_desktop_log "ansys.aedt.core.aedt_logger.AedtLogger.enable_desktop_log")()  | Enable the log in AEDT.  |  
| [`AedtLogger.enable_log_on_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.enable_log_on_file.html#ansys.aedt.core.aedt_logger.AedtLogger.enable_log_on_file "ansys.aedt.core.aedt_logger.AedtLogger.enable_log_on_file")()  | Enable writing log messages to an output file.  |  
| [`AedtLogger.enable_stdout_log`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.enable_stdout_log.html#ansys.aedt.core.aedt_logger.AedtLogger.enable_stdout_log "ansys.aedt.core.aedt_logger.AedtLogger.enable_stdout_log")()  | Enable printing log messages to stdout.  |  
| [`AedtLogger.error`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.error.html#ansys.aedt.core.aedt_logger.AedtLogger.error "ansys.aedt.core.aedt_logger.AedtLogger.error")(msg, *args, **kwargs)  | Write an error message to the global logger.  |  
| [`AedtLogger.get_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.get_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.get_messages "ansys.aedt.core.aedt_logger.AedtLogger.get_messages")([project_name, ...])  | Get the message manager content for a specified project and design.  |  
| [`AedtLogger.info`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.info.html#ansys.aedt.core.aedt_logger.AedtLogger.info "ansys.aedt.core.aedt_logger.AedtLogger.info")(msg, *args, **kwargs)  | Write an info message to the global logger.  |  
| [`AedtLogger.info_timer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.info_timer.html#ansys.aedt.core.aedt_logger.AedtLogger.info_timer "ansys.aedt.core.aedt_logger.AedtLogger.info_timer")(msg[, start_time])  | Write an info message to the global logger with elapsed time.  |  
| [`AedtLogger.remove_all_project_file_logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.remove_all_project_file_logger.html#ansys.aedt.core.aedt_logger.AedtLogger.remove_all_project_file_logger "ansys.aedt.core.aedt_logger.AedtLogger.remove_all_project_file_logger")()  | Remove all the local files from the logger handlers list.  |  
| [`AedtLogger.remove_file_logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.remove_file_logger.html#ansys.aedt.core.aedt_logger.AedtLogger.remove_file_logger "ansys.aedt.core.aedt_logger.AedtLogger.remove_file_logger")(project_name)  | Remove a file from the logger handlers list.  |  
| [`AedtLogger.reset_timer`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.reset_timer.html#ansys.aedt.core.aedt_logger.AedtLogger.reset_timer "ansys.aedt.core.aedt_logger.AedtLogger.reset_timer")([time_val])  | Reset actual timer to actual time or specified time.  |  
| [`AedtLogger.suspend_logging`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.suspend_logging.html#ansys.aedt.core.aedt_logger.AedtLogger.suspend_logging "ansys.aedt.core.aedt_logger.AedtLogger.suspend_logging")()  | Temporarily disable all logs and restore them afterward.  |  
| [`AedtLogger.warning`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.warning.html#ansys.aedt.core.aedt_logger.AedtLogger.warning "ansys.aedt.core.aedt_logger.AedtLogger.warning")(msg, *args, **kwargs)  | Write a warning message to the global logger.  |  
Attributes  
| [`AedtLogger.aedt_error_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.aedt_error_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.aedt_error_messages "ansys.aedt.core.aedt_logger.AedtLogger.aedt_error_messages")  | Message manager content for the active project and design.  |  
| --- | --- |  
| [`AedtLogger.aedt_info_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.aedt_info_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.aedt_info_messages "ansys.aedt.core.aedt_logger.AedtLogger.aedt_info_messages")  | Message manager content for the active project and design.  |  
| [`AedtLogger.aedt_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.aedt_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.aedt_messages "ansys.aedt.core.aedt_logger.AedtLogger.aedt_messages")  | Message manager content for the active project and design.  |  
| [`AedtLogger.aedt_warning_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.aedt_warning_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.aedt_warning_messages "ansys.aedt.core.aedt_logger.AedtLogger.aedt_warning_messages")  | Message manager content for the active project and design.  |  
| [`AedtLogger.design_logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.design_logger.html#ansys.aedt.core.aedt_logger.AedtLogger.design_logger "ansys.aedt.core.aedt_logger.AedtLogger.design_logger")  | Design logger.  |  
| [`AedtLogger.design_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.design_name.html#ansys.aedt.core.aedt_logger.AedtLogger.design_name "ansys.aedt.core.aedt_logger.AedtLogger.design_name")  | Name of current logger design.  |  
| [`AedtLogger.error_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.error_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.error_messages "ansys.aedt.core.aedt_logger.AedtLogger.error_messages")  | Message manager content for the active pyaedt session.  |  
| [`AedtLogger.glb`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.glb.html#ansys.aedt.core.aedt_logger.AedtLogger.glb "ansys.aedt.core.aedt_logger.AedtLogger.glb")  | Global logger.  |  
| [`AedtLogger.info_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.info_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.info_messages "ansys.aedt.core.aedt_logger.AedtLogger.info_messages")  | Message manager content for the active pyaedt session.  |  
| [`AedtLogger.log_on_desktop`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.log_on_desktop.html#ansys.aedt.core.aedt_logger.AedtLogger.log_on_desktop "ansys.aedt.core.aedt_logger.AedtLogger.log_on_desktop")  | Status of the log in AEDT (Message Manager).  |  
| [`AedtLogger.log_on_file`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.log_on_file.html#ansys.aedt.core.aedt_logger.AedtLogger.log_on_file "ansys.aedt.core.aedt_logger.AedtLogger.log_on_file")  | Status of printing log messages to a file.  |  
| [`AedtLogger.log_on_stdout`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.log_on_stdout.html#ansys.aedt.core.aedt_logger.AedtLogger.log_on_stdout "ansys.aedt.core.aedt_logger.AedtLogger.log_on_stdout")  | Status of printing log messages to stdout.  |  
| [`AedtLogger.logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.logger.html#ansys.aedt.core.aedt_logger.AedtLogger.logger "ansys.aedt.core.aedt_logger.AedtLogger.logger")  | AEDT logger object.  |  
| [`AedtLogger.messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.messages.html#ansys.aedt.core.aedt_logger.AedtLogger.messages "ansys.aedt.core.aedt_logger.AedtLogger.messages")  | Message manager content for the active session.  |  
| [`AedtLogger.non_graphical`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.non_graphical.html#ansys.aedt.core.aedt_logger.AedtLogger.non_graphical "ansys.aedt.core.aedt_logger.AedtLogger.non_graphical")  | Check if desktop is graphical or not.  |  
| [`AedtLogger.odesign`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.odesign.html#ansys.aedt.core.aedt_logger.AedtLogger.odesign "ansys.aedt.core.aedt_logger.AedtLogger.odesign")  | Design object.  |  
| [`AedtLogger.oproject`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.oproject.html#ansys.aedt.core.aedt_logger.AedtLogger.oproject "ansys.aedt.core.aedt_logger.AedtLogger.oproject")  | Project object.  |  
| [`AedtLogger.project_logger`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.project_logger.html#ansys.aedt.core.aedt_logger.AedtLogger.project_logger "ansys.aedt.core.aedt_logger.AedtLogger.project_logger")  | Project logger.  |  
| [`AedtLogger.project_name`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.project_name.html#ansys.aedt.core.aedt_logger.AedtLogger.project_name "ansys.aedt.core.aedt_logger.AedtLogger.project_name")  | Name of current logger project.  |  
| [`AedtLogger.warning_messages`](https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AedtLogger.warning_messages.html#ansys.aedt.core.aedt_logger.AedtLogger.warning_messages "ansys.aedt.core.aedt_logger.AedtLogger.warning_messages")  | Message manager content for the active pyaedt session.  |