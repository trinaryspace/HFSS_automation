# Fabrication package: log-periodic bow-tie array on RO4350B 20 mil

Candidate of 2026-11-12, generated from `design_ro4350b_final.yaml` (the values
of the solved HFSS design `LogPer_RO4350B_v3`) by `tools/export_fab.py`.
Regenerate with `python tools/export_fab.py`, then re-run the `kicad-cli`
exports listed at the bottom.

| File | Use |
|---|---|
| `logper_ro4350b.kicad_pcb` | KiCad board (opens in KiCad 8 or later). F.Cu = coax side, B.Cu = far side, Edge.Cuts = outline. |
| `logper_ro4350b.kicad_pro` | KiCad project file; open this from the KiCad project manager. There is no schematic. |
| `gerbers/` | F.Cu (`.gtl`), B.Cu (`.gbl`), outline (`.gm1`) for LPKF CircuitPro. |
| `drill/` | Excellon drill file for the four mounting holes (`-NPTH.drl`) and its map. The `-PTH` files are empty. |
| `dxf/` | The same three layers as DXF, in mm, for CAD. |
| `logper_ro4350b_board.step` | Bare board solid (outline x thickness) for the mechanical model. |
| `drawing_mechanical.pdf` / `.png` | A3 sheet: dimensions, element table, tip detail, assembly and support notes. |
| `copper_front.pdf`, `copper_both.svg` | Quick-look plots of the copper. |
| `geometry_check.txt` | Extents of the exported copper; they match the HFSS model's bounding boxes. |
| `drc.rpt` | KiCad DRC. The two findings are the feed strips reaching the base and tip edges, which is intended. |

## Board

- Rogers RO4350B, 0.508 mm core, 1 oz copper both sides, no solder mask.
- Outline: trapezoid 264.07 mm long, 202.72 mm wide at the base, 20.00 mm at the tip,
  plus four copper-free mounting tabs on the slanted edges.
- Mounting: four Ø3.2 mm (M3 clearance) non-plated holes on tabs 10 mm wide, at
  x = 95.53 mm, y = ±73.31 mm and x = 168.53 mm, y = ±48.05 mm (x from the base
  edge, y from the centreline). The pairs sit 36.50 mm behind and ahead of the
  turntable axis at x = 132.03 mm on the centreline. Nearest copper is 8.3 mm
  from a hole edge. The tabs stay inside the 202.72 mm base width.
- Narrowest copper 0.59 mm (root of element 15); smallest gap between copper
  features on one layer is over 1 mm. Both are far above the LPKF limits
  (50 µm feature, 15 µm spacing).
- The far-side copper is the mirror image of the coax side about the
  centreline. Front and back must be registered to each other: the feed strips
  have to sit on top of one another.

## Things that differ from, or are not in, the simulation

- **Tip half-hole.** The outline has a Ø0.5 mm half-hole at the centre of the
  tip edge to seat the 0.31 mm centre conductor. The HFSS model notches the
  edge by the wire radius only (Ø0.31 mm). A contour router cannot cut this
  radius; drill a 0.5 mm hole centred on the tip edge line before routing the
  outline, or skip it and file a small notch by hand. It is not in the drill file.
- **Mounting tabs and holes** (added 2026-11-12 at the user's request) are not
  in the HFSS model. The tabs are thin low-loss substrate well clear of the
  copper and are expected to have a negligible effect; that is an estimate, not
  a simulated result.
- **No fixture, stiffener, enclosure or SMA body** was simulated. A PLA fixture,
  steel screws, and above all metal under the board centre can change the match
  and pattern. Use nylon screws and re-simulate with the real fixture.
- **Solder** along the coax braid is not modelled.

## Assembly

Taoglas CAB.01061 (SMA(F) bulkhead to MHF, 300 mm of 1.37 mm micro-coax). Cut
off the MHF end, strip the jacket over the board length, and solder the braid
to the front feed strip from the base edge to 1.00 mm short of the tip. The
centre conductor wraps the tip edge and is soldered to the back strip.

## Re-running the KiCad exports

    kicad-cli pcb export gerbers --layers "F.Cu,B.Cu,Edge.Cuts" --output gerbers logper_ro4350b.kicad_pcb
    kicad-cli pcb export drill --format excellon --excellon-units mm --excellon-separate-th --generate-map --map-format pdf --output drill logper_ro4350b.kicad_pcb
    kicad-cli pcb export dxf --layers "F.Cu,B.Cu,Edge.Cuts" --output-units mm --mode-multi --output dxf logper_ro4350b.kicad_pcb
    kicad-cli pcb export step --force --output logper_ro4350b_board.step logper_ro4350b.kicad_pcb
    kicad-cli pcb export pdf --layers "F.Cu,Edge.Cuts" --mode-single --output copper_front.pdf logper_ro4350b.kicad_pcb
    kicad-cli pcb export svg --layers "F.Cu,B.Cu,Edge.Cuts" --mode-single --page-size-mode 2 --exclude-drawing-sheet --output copper_both.svg logper_ro4350b.kicad_pcb
    kicad-cli pcb drc --output drc.rpt logper_ro4350b.kicad_pcb
