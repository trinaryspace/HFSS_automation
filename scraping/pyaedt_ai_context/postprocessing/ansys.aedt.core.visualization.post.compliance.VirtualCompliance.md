---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.html"
category: "postprocessing"
domain: "PyAEDT / HFSS"
---

# VirtualCompliance 

class ansys.aedt.core.visualization.post.compliance.VirtualCompliance(_desktop_ , _template_) 
    
Provides automatic report generation with pass/fail criteria on virtual compliance. 

Parameters: 
     

**desktop** :class:`ansys.aedt.core.desktop.Desktop` 
    
Desktop object. 

**template**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to the template. Supported formats are JSON and TOML.
Examples

```
>>> from ansys.aedt.core.visualization.post.compliance import VirtualCompliance
>>> obj = VirtualCompliance()

```
Copy to clipboard
Methods  
| [`VirtualCompliance.add_aedt_report`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_aedt_report.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_aedt_report "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_aedt_report")(name, ...)  | Add a new custom aedt report to the compliance.  |  
| --- | --- |  
| [`VirtualCompliance.add_specs_to_report`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_specs_to_report.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_specs_to_report "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_specs_to_report")(folder)  | Add specs to the report from a given folder.  |  
| [`VirtualCompliance.compute_report_data`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.compute_report_data.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.compute_report_data "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.compute_report_data")()  | Compute the report data and exports all the images and table without creating the pdf.  |  
| [`VirtualCompliance.create_compliance_report`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.create_compliance_report.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.create_compliance_report "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.create_compliance_report")([...])  | Create the Virtual Compliance report.  |  
| [`VirtualCompliance.create_pdf`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.create_pdf.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.create_pdf "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.create_pdf")(file_name[, ...])  | Create the PDF report after the method `compute_report_data` is called.  |  
| [`VirtualCompliance.load_project`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.load_project.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.load_project "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.load_project")()  | Open the aedt project in Electronics Desktop.  |  
| [`VirtualCompliance.points_in_polygon`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.points_in_polygon.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.points_in_polygon "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.points_in_polygon")(points, ...)  |   |  
Attributes  
| [`VirtualCompliance.add_project_info`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_project_info.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_project_info "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_project_info")  | Add project information.  |  
| --- | --- |  
| [`VirtualCompliance.add_specs_info`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_specs_info.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_specs_info "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_specs_info")  | Add specification information.  |  
| [`VirtualCompliance.dut_image`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.dut_image.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.dut_image "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.dut_image")  | DUT image.  |  
| [`VirtualCompliance.image_height`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.image_height.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.image_height "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.image_height")  | Image height resolution during export.  |  
| [`VirtualCompliance.image_width`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.image_width.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.image_width "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.image_width")  | Image width resolution during export.  |  
| [`VirtualCompliance.parameters`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.parameters.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.parameters "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.parameters")  | Parameters available in the Virtual compliance.  |  
| [`VirtualCompliance.project_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.project_file.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.project_file "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.project_file")  | Project file.  |  
| [`VirtualCompliance.project_name`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.project_name.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.project_name "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.project_name")  | Project name.  |  
| [`VirtualCompliance.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.public_dir.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.public_dir "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.public_dir")  | Shortcut for dir(self).  |  
| [`VirtualCompliance.reports`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.reports.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.reports "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.reports")  | Reports available in the virtual compliance.  |  
| [`VirtualCompliance.specs_folder`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.specs_folder.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.specs_folder "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.specs_folder")  | Add specification folder.  |  
| [`VirtualCompliance.template_name`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.template_name.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.template_name "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.template_name")  | Template name.  |  
| [`VirtualCompliance.use_portrait`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.use_portrait.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.use_portrait "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.use_portrait")  | Use portrait.  |  
# VirtualCompliance 

class ansys.aedt.core.visualization.post.compliance.VirtualCompliance(_desktop_ , _template_) 
    
Provides automatic report generation with pass/fail criteria on virtual compliance. 

Parameters: 
     

**desktop** :class:`ansys.aedt.core.desktop.Desktop` 
    
Desktop object. 

**template**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to the template. Supported formats are JSON and TOML.
Examples

```
>>> from ansys.aedt.core.visualization.post.compliance import VirtualCompliance
>>> obj = VirtualCompliance()

```
Copy to clipboard
Methods  
| [`VirtualCompliance.add_aedt_report`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_aedt_report.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_aedt_report "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_aedt_report")(name, ...)  | Add a new custom aedt report to the compliance.  |  
| --- | --- |  
| [`VirtualCompliance.add_specs_to_report`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_specs_to_report.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_specs_to_report "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_specs_to_report")(folder)  | Add specs to the report from a given folder.  |  
| [`VirtualCompliance.compute_report_data`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.compute_report_data.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.compute_report_data "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.compute_report_data")()  | Compute the report data and exports all the images and table without creating the pdf.  |  
| [`VirtualCompliance.create_compliance_report`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.create_compliance_report.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.create_compliance_report "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.create_compliance_report")([...])  | Create the Virtual Compliance report.  |  
| [`VirtualCompliance.create_pdf`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.create_pdf.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.create_pdf "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.create_pdf")(file_name[, ...])  | Create the PDF report after the method `compute_report_data` is called.  |  
| [`VirtualCompliance.load_project`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.load_project.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.load_project "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.load_project")()  | Open the aedt project in Electronics Desktop.  |  
| [`VirtualCompliance.points_in_polygon`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.points_in_polygon.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.points_in_polygon "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.points_in_polygon")(points, ...)  |   |  
Attributes  
| [`VirtualCompliance.add_project_info`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_project_info.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_project_info "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_project_info")  | Add project information.  |  
| --- | --- |  
| [`VirtualCompliance.add_specs_info`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_specs_info.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_specs_info "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_specs_info")  | Add specification information.  |  
| [`VirtualCompliance.dut_image`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.dut_image.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.dut_image "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.dut_image")  | DUT image.  |  
| [`VirtualCompliance.image_height`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.image_height.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.image_height "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.image_height")  | Image height resolution during export.  |  
| [`VirtualCompliance.image_width`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.image_width.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.image_width "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.image_width")  | Image width resolution during export.  |  
| [`VirtualCompliance.parameters`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.parameters.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.parameters "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.parameters")  | Parameters available in the Virtual compliance.  |  
| [`VirtualCompliance.project_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.project_file.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.project_file "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.project_file")  | Project file.  |  
| [`VirtualCompliance.project_name`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.project_name.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.project_name "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.project_name")  | Project name.  |  
| [`VirtualCompliance.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.public_dir.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.public_dir "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.public_dir")  | Shortcut for dir(self).  |  
| [`VirtualCompliance.reports`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.reports.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.reports "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.reports")  | Reports available in the virtual compliance.  |  
| [`VirtualCompliance.specs_folder`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.specs_folder.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.specs_folder "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.specs_folder")  | Add specification folder.  |  
| [`VirtualCompliance.template_name`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.template_name.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.template_name "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.template_name")  | Template name.  |  
| [`VirtualCompliance.use_portrait`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.use_portrait.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.use_portrait "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.use_portrait")  | Use portrait.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.rst.txt)

# VirtualCompliance 

class ansys.aedt.core.visualization.post.compliance.VirtualCompliance(_desktop_ , _template_) 
    
Provides automatic report generation with pass/fail criteria on virtual compliance. 

Parameters: 
     

**desktop** :class:`ansys.aedt.core.desktop.Desktop` 
    
Desktop object. 

**template**[`str`](https://docs.python.org/3.11/library/stdtypes.html#str "\(in Python v3.11\)") or [`pathlib.Path`](https://docs.python.org/3.11/library/pathlib.html#pathlib.Path "\(in Python v3.11\)") 
    
Full path to the template. Supported formats are JSON and TOML.
Examples

```
>>> from ansys.aedt.core.visualization.post.compliance import VirtualCompliance
>>> obj = VirtualCompliance()

```
Copy to clipboard
Methods  
| [`VirtualCompliance.add_aedt_report`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_aedt_report.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_aedt_report "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_aedt_report")(name, ...)  | Add a new custom aedt report to the compliance.  |  
| --- | --- |  
| [`VirtualCompliance.add_specs_to_report`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_specs_to_report.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_specs_to_report "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_specs_to_report")(folder)  | Add specs to the report from a given folder.  |  
| [`VirtualCompliance.compute_report_data`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.compute_report_data.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.compute_report_data "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.compute_report_data")()  | Compute the report data and exports all the images and table without creating the pdf.  |  
| [`VirtualCompliance.create_compliance_report`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.create_compliance_report.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.create_compliance_report "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.create_compliance_report")([...])  | Create the Virtual Compliance report.  |  
| [`VirtualCompliance.create_pdf`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.create_pdf.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.create_pdf "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.create_pdf")(file_name[, ...])  | Create the PDF report after the method `compute_report_data` is called.  |  
| [`VirtualCompliance.load_project`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.load_project.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.load_project "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.load_project")()  | Open the aedt project in Electronics Desktop.  |  
| [`VirtualCompliance.points_in_polygon`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.points_in_polygon.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.points_in_polygon "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.points_in_polygon")(points, ...)  |   |  
Attributes  
| [`VirtualCompliance.add_project_info`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_project_info.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_project_info "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_project_info")  | Add project information.  |  
| --- | --- |  
| [`VirtualCompliance.add_specs_info`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_specs_info.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_specs_info "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.add_specs_info")  | Add specification information.  |  
| [`VirtualCompliance.dut_image`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.dut_image.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.dut_image "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.dut_image")  | DUT image.  |  
| [`VirtualCompliance.image_height`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.image_height.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.image_height "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.image_height")  | Image height resolution during export.  |  
| [`VirtualCompliance.image_width`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.image_width.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.image_width "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.image_width")  | Image width resolution during export.  |  
| [`VirtualCompliance.parameters`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.parameters.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.parameters "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.parameters")  | Parameters available in the Virtual compliance.  |  
| [`VirtualCompliance.project_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.project_file.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.project_file "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.project_file")  | Project file.  |  
| [`VirtualCompliance.project_name`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.project_name.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.project_name "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.project_name")  | Project name.  |  
| [`VirtualCompliance.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.public_dir.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.public_dir "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.public_dir")  | Shortcut for dir(self).  |  
| [`VirtualCompliance.reports`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.reports.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.reports "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.reports")  | Reports available in the virtual compliance.  |  
| [`VirtualCompliance.specs_folder`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.specs_folder.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.specs_folder "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.specs_folder")  | Add specification folder.  |  
| [`VirtualCompliance.template_name`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.template_name.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.template_name "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.template_name")  | Template name.  |  
| [`VirtualCompliance.use_portrait`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.post.compliance.VirtualCompliance.use_portrait.html#ansys.aedt.core.visualization.post.compliance.VirtualCompliance.use_portrait "ansys.aedt.core.visualization.post.compliance.VirtualCompliance.use_portrait")  | Use portrait.  |