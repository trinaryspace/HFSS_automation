---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram.internal_plot_name.html"
category: "reports"
domain: "PyAEDT / HFSS"
---

# internal_plot_name 

property AMIConturEyeDiagram.internal_plot_name: [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Internal AEDT plot name with escaped backslashes and forward slashes.
Some AEDT APIs (such as `oReportSetup.GetChildObject` and a few report-related operations) require special characters in the plot name to be escaped: backslashes are doubled (`\` -> `\\`) and forward slashes that are not already preceded by a backslash are prefixed with a backslash (`/` -> `\/`). This property returns the plot name in that escaped form, ready to be passed to those APIs, while [`plot_name`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram.plot_name.html#ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram.plot_name "ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram.plot_name") keeps the original user-facing name. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Escaped plot name suitable for AEDT internal API calls.
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.internal_plot_name

```
Copy to clipboard
# internal_plot_name 

property AMIConturEyeDiagram.internal_plot_name: [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Internal AEDT plot name with escaped backslashes and forward slashes.
Some AEDT APIs (such as `oReportSetup.GetChildObject` and a few report-related operations) require special characters in the plot name to be escaped: backslashes are doubled (`\` -> `\\`) and forward slashes that are not already preceded by a backslash are prefixed with a backslash (`/` -> `\/`). This property returns the plot name in that escaped form, ready to be passed to those APIs, while [`plot_name`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram.plot_name.html#ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram.plot_name "ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram.plot_name") keeps the original user-facing name. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Escaped plot name suitable for AEDT internal API calls.
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.internal_plot_name

```
Copy to clipboard
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram.internal_plot_name.rst.txt)

# internal_plot_name 

property AMIConturEyeDiagram.internal_plot_name: [str](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") 
    
Internal AEDT plot name with escaped backslashes and forward slashes.
Some AEDT APIs (such as `oReportSetup.GetChildObject` and a few report-related operations) require special characters in the plot name to be escaped: backslashes are doubled (`\` -> `\\`) and forward slashes that are not already preceded by a backslash are prefixed with a backslash (`/` -> `\/`). This property returns the plot name in that escaped form, ready to be passed to those APIs, while [`plot_name`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram.plot_name.html#ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram.plot_name "ansys.aedt.core.visualization.report.eye.AMIConturEyeDiagram.plot_name") keeps the original user-facing name. 

Returns: 
     

[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)")
    
Escaped plot name suitable for AEDT internal API calls.
Examples

```
>>> from ansys.aedt.core.visualization.report.common import CommonReport
>>> obj = CommonReport()
>>> obj.internal_plot_name

```
Copy to clipboard