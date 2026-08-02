"""Shared smoke design: the matrix's minimal valid Modal structure.

Wave port on the face of a PEC solid, radiation airbox, 3-pass adaptive
setup at 2.4 GHz, 101-point linear sweep 2-3 GHz.
"""

from ansys.aedt.core import Hfss


def build_smoke_design(hfss: Hfss) -> str:
    hfss.modeler.create_box([0, 0, 0], [10, 8, 2], "pedestal", "pec")
    airbox = hfss.modeler.create_box([-15, -15, -15], [40, 38, 33], "airbox", "air")
    hfss.wave_port(hfss.modeler.objects_by_name["pedestal"].faces[0], impedance=50, name="Port1", renormalize=True)
    hfss.assign_radiation_boundary_to_objects(airbox)
    setup = hfss.create_setup("Setup1")
    setup.props["Frequency"] = "2.4GHz"
    setup.props["MaxPasses"] = 3
    setup.props["MaxDeltaS"] = 0.05
    setup.update()
    hfss.create_linear_count_sweep(
        setup=setup.name, unit="GHz", start_frequency=2.0, stop_frequency=3.0, num_of_freq_points=101
    )
    return setup.name
