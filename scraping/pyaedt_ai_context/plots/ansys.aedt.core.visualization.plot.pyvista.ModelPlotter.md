---
title: ""
url: "https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.html"
category: "plots"
domain: "PyAEDT / HFSS"
---

# ModelPlotter 

class ansys.aedt.core.visualization.plot.pyvista.ModelPlotter 
    
Manages the data to be plotted with `pyvista`.
Examples
This Class can be instantiated within Pyaedt (with plot_model_object or different field plots and standalone). Here an example of standalone project

```
>>> model = ModelPlotter()
>>> model.add_object(r"D:\Simulation\antenna.obj", (200, 20, 255), 0.6, "in")
>>> model.add_object(r"D:\Simulation\helix.obj", (0, 255, 0), 0.5, "in")
>>> model.add_field_from_file(r"D:\Simulation\helic_antenna.csv", True, "meter", 1)
>>> model.background_color = (0, 0, 0)
>>> model.plot()

```
Copy to clipboard
And here an example of animation:

```
>>> model = ModelPlotter()
>>> model.add_object(r"D:\Simulation\antenna.obj", (200, 20, 255), 0.6, "in")
>>> model.add_object(r"D:\Simulation\helix.obj", (0, 255, 0), 0.5, "in")
>>> frames = [
...     r"D:\Simulation\helic_antenna.csv",
...     r"D:\Simulation\helic_antenna_10.fld",
...     r"D:\Simulation\helic_antenna_20.fld",
...     r"D:\Simulation\helic_antenna_30.fld",
...     r"D:\Simulation\helic_antenna_40.fld",
... ]
>>> model.gif_file = r"D:\Simulation\animation.gif"
>>> model.animate()

```
Copy to clipboard
Methods  
| [`ModelPlotter.add_field_from_data`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_field_from_data.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_field_from_data "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_field_from_data")(...[, ...])  | Add field data to the scenario.  |  
| --- | --- |  
| [`ModelPlotter.add_field_from_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_field_from_file.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_field_from_file "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_field_from_file")(field_path)  | Add a field file to the scenario.  |  
| [`ModelPlotter.add_frames_from_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_frames_from_file.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_frames_from_file "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_frames_from_file")(field_files)  | Add a field file to the scenario.  |  
| [`ModelPlotter.add_object`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_object.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_object "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_object")(cad_path[, ...])  | Add a mesh file to the scenario.  |  
| [`ModelPlotter.animate`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.animate.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.animate "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.animate")([show])  | Animate the current field plot.  |  
| [`ModelPlotter.clean_cache_and_files`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.clean_cache_and_files.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.clean_cache_and_files "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.clean_cache_and_files")([...])  | Clean downloaded files, and, on demand, also the cached meshes.  |  
| [`ModelPlotter.close`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.close.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.close "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.close")()  | Close the render window.  |  
| [`ModelPlotter.generate_geometry_mesh`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.generate_geometry_mesh.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.generate_geometry_mesh "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.generate_geometry_mesh")()  | Generate mesh for objects only.  |  
| [`ModelPlotter.plot`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.plot.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.plot "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.plot")([export_image_path, show])  | Plot the current available Data.  |  
| [`ModelPlotter.point_cloud`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.point_cloud.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.point_cloud "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.point_cloud")([points, in_volume])  | Generate point cloud with available objects.  |  
| [`ModelPlotter.populate_pyvista_object`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.populate_pyvista_object.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.populate_pyvista_object "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.populate_pyvista_object")()  | Populate pyvista object with geometry and fields added to the model plotter.  |  
| [`ModelPlotter.set_orientation`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.set_orientation.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.set_orientation "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.set_orientation")([...])  | Change the plot default orientation.  |  
Attributes  
| [`ModelPlotter.azimuth_angle`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.azimuth_angle.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.azimuth_angle "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.azimuth_angle")  | Get/Set the azimuth angle value.  |  
| --- | --- |  
| [`ModelPlotter.background_color`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.background_color.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.background_color "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.background_color")  | Background color.  |  
| [`ModelPlotter.background_image`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.background_image.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.background_image "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.background_image")  | Background image.  |  
| [`ModelPlotter.camera_position`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.camera_position.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.camera_position "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.camera_position")  | Get or set the camera position value.  |  
| [`ModelPlotter.convert_fields_in_db`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.convert_fields_in_db.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.convert_fields_in_db "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.convert_fields_in_db")  | Either if convert the fields before plotting in dB.  |  
| [`ModelPlotter.elevation_angle`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.elevation_angle.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.elevation_angle "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.elevation_angle")  | Get/Set the elevation angle value.  |  
| [`ModelPlotter.fields`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.fields.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.fields "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.fields")  | List of fields object.  |  
| [`ModelPlotter.focal_point`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.focal_point.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.focal_point "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.focal_point")  | Get/Set the camera focal point value.  |  
| [`ModelPlotter.frames`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.frames.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.frames "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.frames")  | Frames list for animation.  |  
| [`ModelPlotter.isometric_view`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.isometric_view.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.isometric_view "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.isometric_view")  | Enable or disable the default iso view.  |  
| [`ModelPlotter.log_multiplier`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.log_multiplier.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.log_multiplier "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.log_multiplier")  | Multiply the log value.  |  
| [`ModelPlotter.objects`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.objects.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.objects "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.objects")  | List of class objects.  |  
| [`ModelPlotter.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.public_dir.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.public_dir "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.public_dir")  | Shortcut for dir(self).  |  
| [`ModelPlotter.roll_angle`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.roll_angle.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.roll_angle "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.roll_angle")  | Get/Set the roll angle value.  |  
| [`ModelPlotter.vector_field_scale`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.vector_field_scale.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.vector_field_scale "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.vector_field_scale")  | Field scale.  |  
| [`ModelPlotter.view_up`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.view_up.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.view_up "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.view_up")  | Get/Set the camera view axis.  |  
| [`ModelPlotter.x_scale`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.x_scale.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.x_scale "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.x_scale")  | Scale plot on X.  |  
| [`ModelPlotter.y_scale`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.y_scale.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.y_scale "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.y_scale")  | Scale plot on Y.  |  
| [`ModelPlotter.z_scale`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.z_scale.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.z_scale "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.z_scale")  | Scale plot on Z.  |  
| [`ModelPlotter.zoom`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.zoom.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.zoom "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.zoom")  | Get/Set the zoom value.  |  
# ModelPlotter 

class ansys.aedt.core.visualization.plot.pyvista.ModelPlotter 
    
Manages the data to be plotted with `pyvista`.
Examples
This Class can be instantiated within Pyaedt (with plot_model_object or different field plots and standalone). Here an example of standalone project

```
>>> model = ModelPlotter()
>>> model.add_object(r"D:\Simulation\antenna.obj", (200, 20, 255), 0.6, "in")
>>> model.add_object(r"D:\Simulation\helix.obj", (0, 255, 0), 0.5, "in")
>>> model.add_field_from_file(r"D:\Simulation\helic_antenna.csv", True, "meter", 1)
>>> model.background_color = (0, 0, 0)
>>> model.plot()

```
Copy to clipboard
And here an example of animation:

```
>>> model = ModelPlotter()
>>> model.add_object(r"D:\Simulation\antenna.obj", (200, 20, 255), 0.6, "in")
>>> model.add_object(r"D:\Simulation\helix.obj", (0, 255, 0), 0.5, "in")
>>> frames = [
...     r"D:\Simulation\helic_antenna.csv",
...     r"D:\Simulation\helic_antenna_10.fld",
...     r"D:\Simulation\helic_antenna_20.fld",
...     r"D:\Simulation\helic_antenna_30.fld",
...     r"D:\Simulation\helic_antenna_40.fld",
... ]
>>> model.gif_file = r"D:\Simulation\animation.gif"
>>> model.animate()

```
Copy to clipboard
Methods  
| [`ModelPlotter.add_field_from_data`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_field_from_data.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_field_from_data "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_field_from_data")(...[, ...])  | Add field data to the scenario.  |  
| --- | --- |  
| [`ModelPlotter.add_field_from_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_field_from_file.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_field_from_file "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_field_from_file")(field_path)  | Add a field file to the scenario.  |  
| [`ModelPlotter.add_frames_from_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_frames_from_file.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_frames_from_file "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_frames_from_file")(field_files)  | Add a field file to the scenario.  |  
| [`ModelPlotter.add_object`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_object.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_object "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_object")(cad_path[, ...])  | Add a mesh file to the scenario.  |  
| [`ModelPlotter.animate`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.animate.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.animate "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.animate")([show])  | Animate the current field plot.  |  
| [`ModelPlotter.clean_cache_and_files`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.clean_cache_and_files.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.clean_cache_and_files "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.clean_cache_and_files")([...])  | Clean downloaded files, and, on demand, also the cached meshes.  |  
| [`ModelPlotter.close`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.close.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.close "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.close")()  | Close the render window.  |  
| [`ModelPlotter.generate_geometry_mesh`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.generate_geometry_mesh.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.generate_geometry_mesh "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.generate_geometry_mesh")()  | Generate mesh for objects only.  |  
| [`ModelPlotter.plot`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.plot.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.plot "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.plot")([export_image_path, show])  | Plot the current available Data.  |  
| [`ModelPlotter.point_cloud`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.point_cloud.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.point_cloud "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.point_cloud")([points, in_volume])  | Generate point cloud with available objects.  |  
| [`ModelPlotter.populate_pyvista_object`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.populate_pyvista_object.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.populate_pyvista_object "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.populate_pyvista_object")()  | Populate pyvista object with geometry and fields added to the model plotter.  |  
| [`ModelPlotter.set_orientation`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.set_orientation.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.set_orientation "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.set_orientation")([...])  | Change the plot default orientation.  |  
Attributes  
| [`ModelPlotter.azimuth_angle`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.azimuth_angle.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.azimuth_angle "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.azimuth_angle")  | Get/Set the azimuth angle value.  |  
| --- | --- |  
| [`ModelPlotter.background_color`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.background_color.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.background_color "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.background_color")  | Background color.  |  
| [`ModelPlotter.background_image`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.background_image.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.background_image "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.background_image")  | Background image.  |  
| [`ModelPlotter.camera_position`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.camera_position.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.camera_position "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.camera_position")  | Get or set the camera position value.  |  
| [`ModelPlotter.convert_fields_in_db`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.convert_fields_in_db.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.convert_fields_in_db "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.convert_fields_in_db")  | Either if convert the fields before plotting in dB.  |  
| [`ModelPlotter.elevation_angle`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.elevation_angle.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.elevation_angle "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.elevation_angle")  | Get/Set the elevation angle value.  |  
| [`ModelPlotter.fields`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.fields.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.fields "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.fields")  | List of fields object.  |  
| [`ModelPlotter.focal_point`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.focal_point.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.focal_point "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.focal_point")  | Get/Set the camera focal point value.  |  
| [`ModelPlotter.frames`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.frames.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.frames "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.frames")  | Frames list for animation.  |  
| [`ModelPlotter.isometric_view`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.isometric_view.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.isometric_view "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.isometric_view")  | Enable or disable the default iso view.  |  
| [`ModelPlotter.log_multiplier`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.log_multiplier.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.log_multiplier "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.log_multiplier")  | Multiply the log value.  |  
| [`ModelPlotter.objects`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.objects.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.objects "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.objects")  | List of class objects.  |  
| [`ModelPlotter.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.public_dir.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.public_dir "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.public_dir")  | Shortcut for dir(self).  |  
| [`ModelPlotter.roll_angle`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.roll_angle.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.roll_angle "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.roll_angle")  | Get/Set the roll angle value.  |  
| [`ModelPlotter.vector_field_scale`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.vector_field_scale.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.vector_field_scale "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.vector_field_scale")  | Field scale.  |  
| [`ModelPlotter.view_up`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.view_up.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.view_up "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.view_up")  | Get/Set the camera view axis.  |  
| [`ModelPlotter.x_scale`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.x_scale.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.x_scale "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.x_scale")  | Scale plot on X.  |  
| [`ModelPlotter.y_scale`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.y_scale.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.y_scale "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.y_scale")  | Scale plot on Y.  |  
| [`ModelPlotter.z_scale`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.z_scale.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.z_scale "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.z_scale")  | Scale plot on Z.  |  
| [`ModelPlotter.zoom`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.zoom.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.zoom "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.zoom")  | Get/Set the zoom value.  |  
On this page 
  * [Show Source](https://aedt.docs.pyansys.com/version/stable/_sources/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.rst.txt)

# ModelPlotter 

class ansys.aedt.core.visualization.plot.pyvista.ModelPlotter 
    
Manages the data to be plotted with `pyvista`.
Examples
This Class can be instantiated within Pyaedt (with plot_model_object or different field plots and standalone). Here an example of standalone project

```
>>> model = ModelPlotter()
>>> model.add_object(r"D:\Simulation\antenna.obj", (200, 20, 255), 0.6, "in")
>>> model.add_object(r"D:\Simulation\helix.obj", (0, 255, 0), 0.5, "in")
>>> model.add_field_from_file(r"D:\Simulation\helic_antenna.csv", True, "meter", 1)
>>> model.background_color = (0, 0, 0)
>>> model.plot()

```
Copy to clipboard
And here an example of animation:

```
>>> model = ModelPlotter()
>>> model.add_object(r"D:\Simulation\antenna.obj", (200, 20, 255), 0.6, "in")
>>> model.add_object(r"D:\Simulation\helix.obj", (0, 255, 0), 0.5, "in")
>>> frames = [
...     r"D:\Simulation\helic_antenna.csv",
...     r"D:\Simulation\helic_antenna_10.fld",
...     r"D:\Simulation\helic_antenna_20.fld",
...     r"D:\Simulation\helic_antenna_30.fld",
...     r"D:\Simulation\helic_antenna_40.fld",
... ]
>>> model.gif_file = r"D:\Simulation\animation.gif"
>>> model.animate()

```
Copy to clipboard
Methods  
| [`ModelPlotter.add_field_from_data`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_field_from_data.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_field_from_data "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_field_from_data")(...[, ...])  | Add field data to the scenario.  |  
| --- | --- |  
| [`ModelPlotter.add_field_from_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_field_from_file.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_field_from_file "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_field_from_file")(field_path)  | Add a field file to the scenario.  |  
| [`ModelPlotter.add_frames_from_file`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_frames_from_file.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_frames_from_file "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_frames_from_file")(field_files)  | Add a field file to the scenario.  |  
| [`ModelPlotter.add_object`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_object.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_object "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.add_object")(cad_path[, ...])  | Add a mesh file to the scenario.  |  
| [`ModelPlotter.animate`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.animate.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.animate "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.animate")([show])  | Animate the current field plot.  |  
| [`ModelPlotter.clean_cache_and_files`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.clean_cache_and_files.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.clean_cache_and_files "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.clean_cache_and_files")([...])  | Clean downloaded files, and, on demand, also the cached meshes.  |  
| [`ModelPlotter.close`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.close.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.close "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.close")()  | Close the render window.  |  
| [`ModelPlotter.generate_geometry_mesh`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.generate_geometry_mesh.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.generate_geometry_mesh "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.generate_geometry_mesh")()  | Generate mesh for objects only.  |  
| [`ModelPlotter.plot`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.plot.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.plot "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.plot")([export_image_path, show])  | Plot the current available Data.  |  
| [`ModelPlotter.point_cloud`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.point_cloud.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.point_cloud "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.point_cloud")([points, in_volume])  | Generate point cloud with available objects.  |  
| [`ModelPlotter.populate_pyvista_object`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.populate_pyvista_object.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.populate_pyvista_object "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.populate_pyvista_object")()  | Populate pyvista object with geometry and fields added to the model plotter.  |  
| [`ModelPlotter.set_orientation`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.set_orientation.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.set_orientation "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.set_orientation")([...])  | Change the plot default orientation.  |  
Attributes  
| [`ModelPlotter.azimuth_angle`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.azimuth_angle.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.azimuth_angle "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.azimuth_angle")  | Get/Set the azimuth angle value.  |  
| --- | --- |  
| [`ModelPlotter.background_color`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.background_color.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.background_color "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.background_color")  | Background color.  |  
| [`ModelPlotter.background_image`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.background_image.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.background_image "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.background_image")  | Background image.  |  
| [`ModelPlotter.camera_position`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.camera_position.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.camera_position "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.camera_position")  | Get or set the camera position value.  |  
| [`ModelPlotter.convert_fields_in_db`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.convert_fields_in_db.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.convert_fields_in_db "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.convert_fields_in_db")  | Either if convert the fields before plotting in dB.  |  
| [`ModelPlotter.elevation_angle`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.elevation_angle.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.elevation_angle "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.elevation_angle")  | Get/Set the elevation angle value.  |  
| [`ModelPlotter.fields`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.fields.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.fields "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.fields")  | List of fields object.  |  
| [`ModelPlotter.focal_point`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.focal_point.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.focal_point "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.focal_point")  | Get/Set the camera focal point value.  |  
| [`ModelPlotter.frames`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.frames.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.frames "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.frames")  | Frames list for animation.  |  
| [`ModelPlotter.isometric_view`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.isometric_view.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.isometric_view "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.isometric_view")  | Enable or disable the default iso view.  |  
| [`ModelPlotter.log_multiplier`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.log_multiplier.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.log_multiplier "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.log_multiplier")  | Multiply the log value.  |  
| [`ModelPlotter.objects`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.objects.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.objects "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.objects")  | List of class objects.  |  
| [`ModelPlotter.public_dir`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.public_dir.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.public_dir "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.public_dir")  | Shortcut for dir(self).  |  
| [`ModelPlotter.roll_angle`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.roll_angle.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.roll_angle "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.roll_angle")  | Get/Set the roll angle value.  |  
| [`ModelPlotter.vector_field_scale`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.vector_field_scale.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.vector_field_scale "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.vector_field_scale")  | Field scale.  |  
| [`ModelPlotter.view_up`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.view_up.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.view_up "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.view_up")  | Get/Set the camera view axis.  |  
| [`ModelPlotter.x_scale`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.x_scale.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.x_scale "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.x_scale")  | Scale plot on X.  |  
| [`ModelPlotter.y_scale`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.y_scale.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.y_scale "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.y_scale")  | Scale plot on Y.  |  
| [`ModelPlotter.z_scale`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.z_scale.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.z_scale "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.z_scale")  | Scale plot on Z.  |  
| [`ModelPlotter.zoom`](https://aedt.docs.pyansys.com/version/stable/API/visualization/_autosummary/ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.zoom.html#ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.zoom "ansys.aedt.core.visualization.plot.pyvista.ModelPlotter.zoom")  | Get/Set the zoom value.  |