"""Route-B add-on: make `fr4_cst` dispersive, as CST's "FR-4 (lossy)" is.

Schema v1 materials are constants. CST's model uses a fitted dispersive FR-4
(eps' 4.81 at 0.8 GHz falling to 4.65 at 6 GHz, tan delta 0.023-0.025), and
`data/fr4_cst_fit.csv` holds 60 rows of that fit taken verbatim from CST's
export. This stage loads them as two project datasets and points the
material's permittivity and loss tangent at them with `pwl(..., Freq)`.

Run AFTER `compile_spec` (whose materials stage resets the constants).

Usage (workspace root):  python src/21_fr4_dispersion.py
Prints one Verification line:  PASS: fr4_dispersion ...

API, quoted from the KB:
  Hfss.create_dataset1d_project(name, x, y, x_unit='', y_unit='', sort=True)
      -> DataSet      (name "without a prefix for a project dataset")
"""

import os

import ws_common

MATERIAL = "fr4_cst"
DS_EPS, DS_TAND = "fr4_eps", "fr4_tand"
DATA = os.path.join(ws_common.WORKSPACE, "data", "fr4_cst_fit.csv")


def load():
    freq_hz, eps, tand = [], [], []
    with open(DATA, encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("freq"):
                continue
            f, e, t = (float(v) for v in line.split(","))
            freq_hz.append(f * 1e9)
            eps.append(e)
            tand.append(t)
    if len(freq_hz) < 10:
        raise RuntimeError("fit table too short: %d rows" % len(freq_hz))
    return freq_hz, eps, tand


def main():
    hfss = ws_common.attach()
    # The RO4350B design shares this project and this add-on set. Its
    # substrate is not FR-4, so there is nothing to make dispersive: say so and
    # pass, rather than touching a material the design does not use.
    substrate = hfss.modeler["Substrate"]
    used = (substrate.material_name or "").lower() if substrate else ""
    if used != MATERIAL.lower():
        print("PASS: fr4_dispersion skipped - Substrate is %r, not %r"
              % (used, MATERIAL), flush=True)
        return
    freq_hz, eps, tand = load()

    for name in (DS_EPS, DS_TAND):          # delete-then-create (ADR 0008)
        existing = (hfss.project_datasets or {}).get("$" + name)
        if existing is not None:
            existing.delete()
    # x in Hz with no unit: `Freq` is evaluated in Hz inside pwl().
    if not hfss.create_dataset1d_project(DS_EPS, freq_hz, eps):
        raise RuntimeError("could not create dataset %s" % DS_EPS)
    if not hfss.create_dataset1d_project(DS_TAND, freq_hz, tand):
        raise RuntimeError("could not create dataset %s" % DS_TAND)
    have = set(hfss.project_datasets or {})
    if not {"$" + DS_EPS, "$" + DS_TAND} <= have:
        raise RuntimeError("datasets missing after create: %s" % sorted(have))

    mat = hfss.materials[MATERIAL]
    if mat is None:
        raise RuntimeError("material %r missing - run compile_spec first" % MATERIAL)
    eps_expr = "pwl($%s, Freq)" % DS_EPS
    tand_expr = "pwl($%s, Freq)" % DS_TAND
    mat.permittivity = eps_expr
    mat.dielectric_loss_tangent = tand_expr

    got_eps = str(hfss.materials[MATERIAL].permittivity.value)
    got_tand = str(hfss.materials[MATERIAL].dielectric_loss_tangent.value)
    if "pwl" not in got_eps or "pwl" not in got_tand:
        raise RuntimeError("material read-back is not dispersive: eps=%r tand=%r"
                           % (got_eps, got_tand))

    hfss.save_project()
    ws_common.write_state("stage_fr4_dispersion", "done")
    print("PASS: fr4_dispersion rows=%d f=%.3g..%.3gGHz eps=%.4f..%.4f "
          "tand=%.4f..%.4f material_eps=%r material_tand=%r"
          % (len(freq_hz), freq_hz[0] / 1e9, freq_hz[-1] / 1e9, eps[0], eps[-1],
             tand[0], tand[-1], got_eps, got_tand), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    ws_common.exit_keep_alive()
