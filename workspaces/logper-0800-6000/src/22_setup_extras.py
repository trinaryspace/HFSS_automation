"""Route-B add-on: broadband adaptive solve, field sweep, far-field sphere.

Schema v1 writes a single-frequency adaptive setup and one sweep. A 0.8-6 GHz
log-periodic array is active in a different part of the board at every
frequency, so the adaptive mesh must be refined across the band, and the
radiation comparison against CST needs saved fields at 1..6 GHz.

Creates / replaces (delete-then-create, ADR 0008):
  - Setup1 adaptive  -> broadband, f_lo..f_hi, MAX_PASSES, MAX_DELTA_S
  - sweep FieldPts   -> discrete 1..6 GHz in 1 GHz steps, fields saved
  - far-field setup FF_Sphere -> theta 0..180, phi 0..360, 2 degree steps
The spec's interpolating sweep `Sweep1` (0.4-6.5 GHz) is left as compiled.

Run AFTER `compile_spec` (whose setup stage recreates Setup1).

Usage (workspace root):  python src/22_setup_extras.py
Prints one Verification line:  PASS: setup_extras ...

API, quoted from the KB:
  SetupHFSS.enable_adaptive_setup_broadband(low_frequency, high_frequency,
      max_passes=6, max_delta_s=0.02) -> bool
  SetupHFSS.delete_sweep(name) -> bool
  Hfss.create_linear_step_sweep(setup, unit, start_frequency, stop_frequency,
      step_size, name=None, save_fields=True, save_rad_fields=False,
      sweep_type='Discrete') -> SweepHFSS | bool
  Hfss.insert_infinite_sphere(definition='Theta-Phi', phi_start=0,
      phi_stop=180, phi_step=10, theta_start=0, theta_stop=180, theta_step=10,
      units='deg', custom_radiation_faces=None, custom_coordinate_system=None,
      use_slant_polarization=False, polarization_angle=45, name=None)
      -> FarFieldSetup
"""

import os

import ws_common

SETUP = "Setup1"
FIELD_SWEEP = "FieldPts"
SPHERE = "FF_Sphere"
F_LO, F_HI = "0.8GHz", "6GHz"
# LOGPER_MAX_PASSES caps the adaptive passes for a tuning iteration: each
# extra pass grows the mesh ~25 %, and passes 8 -> 9 took the per-point memory
# from ~6 GB to ~11 GB on the Rogers board. The final verification uses 12.
MAX_PASSES = int(os.environ.get("LOGPER_MAX_PASSES") or 12)
MAX_DELTA_S = 0.02


def main():
    hfss = ws_common.attach()
    if SETUP not in (hfss.setup_names or []):
        raise RuntimeError("%s missing - run compile_spec first" % SETUP)
    setup = hfss.get_setup(SETUP)

    # pyAEDT 1.3.0's helper indexes props["MultipleAdaptiveFreqsSetup"], which a
    # freshly created single-frequency setup does not carry (KeyError, measured
    # on this run). Seed it without firing an EditSetup, then let the helper
    # write the whole thing in one update.
    if "MultipleAdaptiveFreqsSetup" not in setup.props:
        setup.auto_update = False
        setup.props["MultipleAdaptiveFreqsSetup"] = {"Low": F_LO, "High": F_HI}
        setup.auto_update = True
    if not setup.enable_adaptive_setup_broadband(
            low_frequency=F_LO, high_frequency=F_HI,
            max_passes=MAX_PASSES, max_delta_s=MAX_DELTA_S):
        raise RuntimeError("enable_adaptive_setup_broadband reported failure")
    props = hfss.get_setup(SETUP).props
    solve_type = str(props.get("SolveType"))
    if solve_type.lower() != "broadband":
        raise RuntimeError("SolveType read back as %r, not broadband" % solve_type)
    band = dict(props.get("MultipleAdaptiveFreqsSetup") or {})
    if str(band.get("Low")) != F_LO or str(band.get("High")) != F_HI:
        raise RuntimeError("broadband range read back as %r" % band)

    existing = [s.split(" : ")[-1] for s in (hfss.existing_analysis_sweeps or [])]
    if FIELD_SWEEP in existing:              # delete-then-create
        setup.delete_sweep(FIELD_SWEEP)
    for field_setup in list(hfss.field_setups or []):
        if field_setup.name == SPHERE:
            field_setup.delete()

    # Tuning mode: S11 only. The field sweep stores six full field solutions
    # and the far-field sphere needs them; a design iteration that is judged
    # on its match does not, and on the thin Rogers board each stored point
    # costs minutes and gigabytes. The final candidate is run without this.
    if os.environ.get("LOGPER_TUNING") == "1":
        if not bool(hfss.validate_simple()):
            raise RuntimeError("validate_simple() returned False after setup extras")
        hfss.save_project()
        ws_common.write_state("stage_setup_extras", "done-tuning")
        sweeps = sorted(s.split(" : ")[-1] for s in hfss.existing_analysis_sweeps
                        if s.startswith(SETUP))
        print("PASS: setup_extras TUNING solve_type=%s band=%s..%s passes=%d "
              "delta_s=%s sweeps=%s far_field=none validate_simple=True"
              % (solve_type, F_LO, F_HI, MAX_PASSES, MAX_DELTA_S, sweeps), flush=True)
        return

    sweep = hfss.create_linear_step_sweep(
        setup=SETUP, unit="GHz", start_frequency=1.0, stop_frequency=6.0,
        step_size=1.0, name=FIELD_SWEEP, save_fields=True,
        save_rad_fields=False, sweep_type="Discrete")
    if not sweep:
        raise RuntimeError("could not create sweep %s" % FIELD_SWEEP)

    sphere = hfss.insert_infinite_sphere(
        definition="Theta-Phi", phi_start=0, phi_stop=360, phi_step=2,
        theta_start=0, theta_stop=180, theta_step=2, units="deg", name=SPHERE)
    if not sphere:
        raise RuntimeError("could not create far-field sphere %s" % SPHERE)

    sweeps = sorted(s.split(" : ")[-1] for s in hfss.existing_analysis_sweeps
                    if s.startswith(SETUP))
    spheres = [f.name for f in hfss.field_setups]
    if FIELD_SWEEP not in sweeps or SPHERE not in spheres:
        raise RuntimeError("read-back missing: sweeps=%s spheres=%s" % (sweeps, spheres))
    if not bool(hfss.validate_simple()):
        raise RuntimeError("validate_simple() returned False after setup extras")

    hfss.save_project()
    ws_common.write_state("stage_setup_extras", "done")
    print("PASS: setup_extras solve_type=%s band=%s..%s passes=%d delta_s=%s "
          "sweeps=%s far_field=%s validate_simple=True"
          % (solve_type, F_LO, F_HI, MAX_PASSES, MAX_DELTA_S, sweeps, spheres),
          flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    ws_common.exit_keep_alive()
