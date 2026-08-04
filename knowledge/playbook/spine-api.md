# Spine API — the verified call set behind an HFSS build

Distilled reference for the hfss-agent Spine: script authoring reads this file instead of crawling `scraping/pyaedt_ai_context/` (analysis §6); per-file KB reads happen only for off-spine calls. Each entry: signature + one-line semantics + the environment-compat gotchas that apply on this machine (ADR 0004). Generated, do not hand-edit.

## Provenance

- Generated: 2026-08-04 by `scraping/generate_spine_api.py`
- KB files: 4375 (markdown pages under `scraping/pyaedt_ai_context/`, .rst.md stubs and provenance.md excluded)
- KB content hash (sha256): 8376262dae7b379aa37dc1a42461a9d50620d1bcbdf840cf395907d50eacf67c
- Spine call count: 36; regenerate in the KB top-up ceremony

## Lifecycle & desktop

### Hfss
`class ansys.aedt.core.hfss.Hfss(project : str | None = None, design : str | None = None, solution_type : str | None = None, setup : str | None = None, version : str | None = None, non_graphical : bool | None = False, new_desktop : bool | None = False, close_on_exit : bool | None = False, student_version : bool | None = False, machine : str | None = '', port : int | None = 0, aedt_process_id : int | None = None, remove_lock : bool | None = False)`
Provides the HFSS application interface.
KB: `hfss/ansys.aedt.core.hfss.Hfss.md` · EC gotchas: [EC#1 Launch new graphical desktop — WORKS](environment-compat.md#1-launch-new-graphical-desktop-works) · [EC#2 Attach onto running desktop — WORKS (cross-process)](environment-compat.md#2-attach-onto-running-desktop-works-cross-process) · [EC#9 Project files and locks — manage explicitly](environment-compat.md#9-project-files-and-locks-manage-explicitly) · [EC#11 Solution-type default — Terminal, not Modal](environment-compat.md#11-solution-type-default-terminal-not-modal)

### Hfss.analyze
`Hfss.analyze(setup : str = None, cores : int = None, tasks : int = None, gpus : int = None, acf_file : str = None, use_auto_settings : bool = True, solve_in_batch : bool = False, machine : str = 'localhost', run_in_thread : bool = False, revert_to_initial_mesh : bool = False, blocking : bool = True) → bool`
Solve the active design.
KB: `hfss/ansys.aedt.core.hfss.Hfss.analyze.md` · EC gotchas: [EC#4 Blocking solve — WORKS](environment-compat.md#4-blocking-solve-works) · [EC#5 Non-blocking solve — WORKS (submission); background completion INFERRED](environment-compat.md#5-non-blocking-solve-works-submission-background-completion-inferred)

### Hfss.validate_simple
`Hfss.validate_simple(log_file : str | Path = None) → int`
Validate a design.
KB: `hfss/ansys.aedt.core.hfss.Hfss.validate_simple.md` · EC gotchas: [EC#8 Validation gates — MUST use before solve](environment-compat.md#8-validation-gates-must-use-before-solve)

### Hfss.save_project
`Hfss.save_project(file_name : str | Path = None, overwrite : bool = True, refresh_ids : bool = False) → bool`
Save the project and add a message.
KB: `hfss/ansys.aedt.core.hfss.Hfss.save_project.md`

### Hfss.release_desktop
`Hfss.release_desktop(close_projects : bool = True, close_desktop : bool = True) → bool`
Release AEDT.
KB: `hfss/ansys.aedt.core.hfss.Hfss.release_desktop.md` · EC gotchas: [EC#10 Release / process hygiene — kill-until-gone required](environment-compat.md#10-release-process-hygiene-kill-until-gone-required)

### Hfss.cleanup_solution
`Hfss.cleanup_solution(variations : str | list = 'All', entire_solution : bool = True, field : bool = True, mesh : bool = True, linked_data : bool = True) → bool`
Delete a set of Solution Variations or part of them.
KB: `hfss/ansys.aedt.core.hfss.Hfss.cleanup_solution.md`

### Hfss.change_validation_settings
`Hfss.change_validation_settings(entity_check_level : str = 'Strict', ignore_unclassified : bool = False, skip_intersections : bool = False)`
Update the validation design settings.
KB: `hfss/ansys.aedt.core.hfss.Hfss.change_validation_settings.md`

## Geometry modeler

### Modeler3D.create_box
`Modeler3D.create_box(origin : list, sizes : list, name : str = None, material : str = None, ** kwargs) → Object3d`
Create a box.
KB: `geometry_modeler/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_box.md`

### Modeler3D.create_cylinder
`Modeler3D.create_cylinder(orientation : str | int | Plane, origin : list, radius : float | str, height : float | str, num_sides : int = 0, name : str = None, material : str = None, ** kwargs) → Object3d`
Create a cylinder.
KB: `geometry_modeler/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_cylinder.md`

### Modeler3D.create_rectangle
`Modeler3D.create_rectangle(orientation : str | int | Plane, origin : list | object, sizes : list, name : str = None, material : str = None, is_covered : bool = True, ** kwargs) → Object3d`
Create a rectangle.
KB: `geometry_modeler/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_rectangle.md`

### Modeler3D.create_circle
`Modeler3D.create_circle(orientation : str | int | Plane, origin : list, radius : float | int | str, num_sides : int = 0, is_covered : bool = True, name : str = None, material : str = None, non_model : bool = False, ** kwargs) → Object3d`
Create a circle.
KB: `geometry_modeler/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_circle.md`

### Modeler3D.create_polyline
`Modeler3D.create_polyline(points : list, segment_type : PolylineSegment | list = None, cover_surface : bool = False, close_surface : bool = False, name : str | None = None, material : str | None = None, xsection_type : str = None, xsection_orient : str = None, xsection_width : int = 1, xsection_topwidth : int = 1, xsection_height : int = 1, xsection_num_seg : int = 0, xsection_bend_type : str = None, non_model : bool = False) → Polyline`
Draw a polyline object in the 3D modeler.
KB: `geometry_modeler/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_polyline.md`

### Modeler3D.create_region
`Modeler3D.create_region(pad_value : float | str | list[float | str | int] = 300, pad_type : str = 'Percentage Offset', name : str = 'Region', ** kwarg) → Object3d`
Create an air region.
KB: `geometry_modeler/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_region.md`

### Modeler3D.create_airbox
`Modeler3D.create_airbox(offset : int = 0, offset_type : str = 'Absolute', name : str = 'AirBox_Auto') → int`
Create an airbox that is as big as the bounding extension of the project.
KB: `geometry_modeler/ansys.aedt.core.modeler.modeler_3d.Modeler3D.create_airbox.md`

### Modeler3D.thicken_sheet
`Modeler3D.thicken_sheet(assignment : str | int | list | Object3d, thickness : float | str, both_sides : bool = False) → Object3d`
Thicken the sheet of the selection.
KB: `geometry_modeler/ansys.aedt.core.modeler.modeler_3d.Modeler3D.thicken_sheet.md`

### Modeler3D.unite
`Modeler3D.unite(assignment : list, purge : bool = False, keep_originals : bool = False) → str | bool`
Unite objects from a list.
KB: `geometry_modeler/ansys.aedt.core.modeler.modeler_3d.Modeler3D.unite.md`

### Modeler3D.subtract
`Modeler3D.subtract(blank_list : str | int | list | Object3d, tool_list : str | int | list | Object3d, keep_originals : bool = True) → bool`
Subtract objects.
KB: `geometry_modeler/ansys.aedt.core.modeler.modeler_3d.Modeler3D.subtract.md`

### Modeler3D.duplicate_along_line
`Modeler3D.duplicate_along_line(assignment : str | int | list | Object3d, vector : list, clones : int = 2, attach : bool = False, is_3d_comp : bool = False, duplicate_assignment : bool = True) → tuple`
Duplicate a selection along a line.
KB: `geometry_modeler/ansys.aedt.core.modeler.modeler_3d.Modeler3D.duplicate_along_line.md`

### Object3d.move
`Object3d.move(vector : list[float] | object) → Object3d | bool`
Move objects from a list.
KB: `geometry_modeler/ansys.aedt.core.modeler.cad.object_3d.Object3d.move.md`

## Materials

### Material.update
`Material.update() → bool`
Update the material in AEDT.
KB: `materials/ansys.aedt.core.modules.material.Material.update.md`

### Materials.add_material
`Materials.add_material(name : str, properties : dict = None) → Material | bool`
Add a material with default values.
KB: `materials/ansys.aedt.core.modules.material_lib.Materials.add_material.md`

## Boundaries & ports

### Hfss.wave_port
`Hfss.wave_port(assignment : int | Object3d | FacePrimitive, reference : int | str | list | Object3d = None, create_port_sheet : bool | None = False, create_pec_cap : bool | None = False, integration_line : int | Gravity | None = 0, port_on_plane : bool | None = True, modes : int | None = 1, impedance : float | None = 50, name : str | None = None, renormalize : bool | None = True, deembed : float | None = 0, is_microstrip : bool | None = False, vfactor : int | None = 3, hfactor : int | None = 5, terminals_rename : bool | None = True, characteristic_impedance : str | list | None = 'Zpi') → BoundaryObject`
Create a waveport from a sheet (`start_object`) or taking the closest edges of two objects.
KB: `hfss/ansys.aedt.core.hfss.Hfss.wave_port.md` · EC gotchas: [EC#7 Excitation assignments — WORKS with caveats (pattern matters)](environment-compat.md#7-excitation-assignments-works-with-caveats-pattern-matters) · [EC#8 Validation gates — MUST use before solve](environment-compat.md#8-validation-gates-must-use-before-solve)

### Hfss.assign_radiation_boundary_to_objects
`Hfss.assign_radiation_boundary_to_objects(assignment : str | list | Object3d, name : str | None = None) → BoundaryObject`
Assign a radiation boundary to one or more objects (usually airbox objects).
KB: `hfss/ansys.aedt.core.hfss.Hfss.assign_radiation_boundary_to_objects.md`

### Hfss.assign_finite_conductivity
`Hfss.assign_finite_conductivity(assignment : str | list, material : str | None = None, conductivity : int = 58000000, permittivity : int = 1, use_thickness : bool = False, thickness : str = '0.1mm', roughness : str = '0um', is_infinite_ground : bool = False, is_two_side : bool = False, is_internal : bool = True, is_shell_element : bool = False, use_huray : bool = False, radius : str = '0.5um', ratio : str = '2.9', height_deviation : float = 0.0, name : str | None = None) → BoundaryObject`
Assign finite conductivity to one or more objects or faces of a given material.
KB: `hfss/ansys.aedt.core.hfss.Hfss.assign_finite_conductivity.md`

### Hfss.assign_perfecte_to_sheets
`Hfss.assign_perfecte_to_sheets(assignment : str | list, name : str | None = None, is_infinite_ground : bool | None = False) → BoundaryObject`
Create a Perfect E taking one sheet.
KB: `hfss/ansys.aedt.core.hfss.Hfss.assign_perfecte_to_sheets.md`

## Setup & mesh

### Hfss.create_setup
`Hfss.create_setup(name : str = 'MySetupAuto', setup_type : str | None = None, ** kwargs) → SetupHFSS | SetupHFSSAuto`
Create an analysis setup for HFSS.
KB: `hfss/ansys.aedt.core.hfss.Hfss.create_setup.md`

### Hfss.create_linear_count_sweep
`Hfss.create_linear_count_sweep(setup : str, unit : str, start_frequency : float, stop_frequency : float, num_of_freq_points : int | None = None, name : str | None = None, save_fields : bool = True, save_rad_fields : bool = False, sweep_type : str = 'Discrete', interpolation_tol : float = 0.5, interpolation_max_solutions : int = 250) → SweepHFSS | bool`
Create a sweep with a specified number of points.
KB: `hfss/ansys.aedt.core.hfss.Hfss.create_linear_count_sweep.md`

### Setup.update
`Setup.update(properties : dict = None) → bool`
Update the setup based on either the class argument or a dictionary.
KB: `setup_and_mesh/ansys.aedt.core.modules.solve_setup.Setup.update.md`

### SweepHFSS
`class ansys.aedt.core.modules.solve_sweeps.SweepHFSS(setup , name : str, sweep_type : str = 'Interpolating', props =None)`
Initializes, creates, and updates sweeps in HFSS.
KB: `setup_and_mesh/ansys.aedt.core.modules.solve_sweeps.SweepHFSS.md`

### Mesh.assign_length_mesh
`Mesh.assign_length_mesh(assignment : list | str, inside_selection : bool = True, maximum_length : int = 1, maximum_elements : int = 1000, name : str = None) → MeshOperation`
Assign a length for the model resolution.
KB: `setup_and_mesh/ansys.aedt.core.modules.mesh.Mesh.assign_length_mesh.md`

### Mesh.assign_skin_depth
`Mesh.assign_skin_depth(assignment : list | str, skin_depth : str = '0.2mm', maximum_elements : int = None, triangulation_max_length : str = '0.1mm', layers_number : str = '2', name : str | None = None) → MeshOperation`
Assign a skin depth for the mesh refinement.
KB: `setup_and_mesh/ansys.aedt.core.modules.mesh.Mesh.assign_skin_depth.md`

## Postprocessing, reports & readout

### PostProcessor3D.create_report
`PostProcessor3D.create_report(expressions : str | list = None, setup_sweep_name : str = None, domain : str = 'Sweep', variations : dict = None, primary_sweep_variable : str = None, secondary_sweep_variable : str = None, report_category : str = None, plot_type : str = 'Rectangular Plot', context : str | dict = None, subdesign_id : int = None, polyline_points : int = 1001, plot_name : str = None, matplotlib : bool = False, show : bool = True, hide_legend : bool = False, snapshot_path : str = None, width : int = 800, height : int = 450) → Standard | AMIEyeDiagram | AMIConturEyeDiagram | EMIReceiver | EyeDiagram | …`
Create a report in AEDT or in Matplotlib.
KB: `postprocessing/ansys.aedt.core.visualization.post.post_common_3d.PostProcessor3D.create_report.md`

### PostProcessor3D.create_report_from_configuration
`PostProcessor3D.create_report_from_configuration(input_file : str = None, report_settings : dict = None, solution_name : str = None, name : str = None, matplotlib : bool = False, show : bool = True, hide_legend : bool = False, snapshot_path : str = None, width : int = 800, height : int = 450) → Standard | AMIEyeDiagram | AMIConturEyeDiagram | EMIReceiver | EyeDiagram | CircuitNetlistReport | Fields | FarField | NearField | Spectral | ReportPlotter | None | bool`
Create a report based on a JSON file, TOML file, RPT file, or dictionary of properties.
KB: `postprocessing/ansys.aedt.core.visualization.post.post_common_3d.PostProcessor3D.create_report_from_configuration.md`

### PostProcessor3D.get_solution_data
`PostProcessor3D.get_solution_data(expressions : str | list = None, setup_sweep_name : str | None = None, domain : str | None = None, variations : dict | None = None, primary_sweep_variable : str | None = None, report_category : str | None = None, context : str | dict | None = None, subdesign_id : int | None = None, polyline_points : int = 1001, math_formula : str | None = None) → SolutionData | bool`
Get a simulation result from a solved setup and cast it in a `SolutionData` object.
KB: `postprocessing/ansys.aedt.core.visualization.post.post_common_3d.PostProcessor3D.get_solution_data.md` · EC gotchas: [EC#6 Reading results (`post.get_solution_data`) — WORKS, FLAKY (single observation)](environment-compat.md#6-reading-results-post-get-solution-data-works-flaky-single-observation)

### SolutionData
`class ansys.aedt.core.visualization.post.solution_data.SolutionData(aedtdata)`
Contains information from the `GetSolutionDataPerVariation()` method.
KB: `postprocessing/ansys.aedt.core.visualization.post.solution_data.SolutionData.md` · EC gotchas: [EC#6 Reading results (`post.get_solution_data`) — WORKS, FLAKY (single observation)](environment-compat.md#6-reading-results-post-get-solution-data-works-flaky-single-observation)

### AedtLogger.get_messages
`AedtLogger.get_messages(project_name : str | None = None, design_name : str | None = None, level : int | None = 0, aedt_messages : bool | None = False) → MessageList`
Get the message manager content for a specified project and design.
KB: `desktop_app/ansys.aedt.core.aedt_logger.AedtLogger.get_messages.md`
