---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/_autosummary/ansys.aedt.core.aedt_logger.AppFilter.filter.html"
category: "desktop_app"
domain: "PyAEDT / HFSS"
---

# filter 

AppFilter.filter(_record : [LogRecord](https://docs.python.org/3.11/library/logging.html#logging.LogRecord "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Filter logs.
Modify the record sent to the logger. 

Parameters: 
     

**record** class:logging.LogRecord 
    
Contains information related to the event being logged.
Examples

```
>>> from ansys.aedt.core.aedt_logger import AppFilter
>>> app_filter = AppFilter(destination="Global")
>>> import logging
>>> record = logging.LogRecord("name", logging.INFO, "", 0, "msg", None, None)
>>> app_filter.filter(record)
True

```
Copy to clipboard
# filter 

AppFilter.filter(_record : [LogRecord](https://docs.python.org/3.11/library/logging.html#logging.LogRecord "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Filter logs.
Modify the record sent to the logger. 

Parameters: 
     

**record** class:logging.LogRecord 
    
Contains information related to the event being logged.
Examples

```
>>> from ansys.aedt.core.aedt_logger import AppFilter
>>> app_filter = AppFilter(destination="Global")
>>> import logging
>>> record = logging.LogRecord("name", logging.INFO, "", 0, "msg", None, None)
>>> app_filter.filter(record)
True

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/_autosummary/ansys.aedt.core.aedt_logger.AppFilter.filter.rst.txt)

# filter 

AppFilter.filter(_record : [LogRecord](https://docs.python.org/3.11/library/logging.html#logging.LogRecord "\(in Python v3.11\)")_) → [bool](https://docs.python.org/3.11/library/functions.html#bool "\(in Python v3.11\)") 
    
Filter logs.
Modify the record sent to the logger. 

Parameters: 
     

**record** class:logging.LogRecord 
    
Contains information related to the event being logged.
Examples

```
>>> from ansys.aedt.core.aedt_logger import AppFilter
>>> app_filter = AppFilter(destination="Global")
>>> import logging
>>> record = logging.LogRecord("name", logging.INFO, "", 0, "msg", None, None)
>>> app_filter.filter(record)
True

```
Copy to clipboard