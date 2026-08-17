# Review sheet — the six Wave A specs, with independent cross-checks

**Your job:** decide, per spec, `correct` / `subtly wrong` / `grossly wrong`.
That verdict is the false-green measurement and it is the one thing the tooling
cannot produce — §3 of the findings shows why the automated gates cannot answer
it (two specs were *fitted* to the pre-check rather than checked by it).

**What I did here:** recomputed the key numbers from first principles, by hand,
**not** with `hfss_spec.physics` — because using the repo's own estimator is
exactly the circularity that makes the pre-check useless on authored specs. These
are numbers to judge against, not verdicts. Where I think something is worth your
eye, it says so.

Specs live beside this file: `cells/<CELL>.design.yaml`.
(`X0a-DRY.design.yaml` is the contaminated dry cell — ignore it.)

λ₀ values used: 2.4 GHz → 124.91 mm · 2.45 GHz → 122.36 mm · 5.8 GHz → 51.69 mm ·
10 GHz → 29.98 mm.

---

## X0a — inset patch, 2.4 GHz, FR4 (authored **blind**)

| variable | spec | my independent check |
|---|---|---|
| patch_W | 38.0100 mm | Balanis 14-6: `c/(2f)·√(2/(εr+1))` = 62.46·0.6086 = **38.01 mm** ✓ |
| patch_L | 29.4216 mm | εeff ≈ 4.09, ΔL ≈ 0.74 → **≈29.42 mm** ✓ |
| feed_W | 3.0829 mm | 50 Ω on 1.6 mm FR4 → **≈3.06–3.10 mm** ✓ |
| sub_W/L | 60 × 60 mm | patch + ~6h margin each side; reasonable |
| air_pad_top | 31.2 mm | λ₀/4 = 31.23 mm ✓ |
| air_pad_side | 15 mm | λ₀/10 = 12.5 mm — **thinner than the top pad** |
| inset_d | 9.77 mm | match tuner, not resonance — not independently checkable |

**Worth your eye:** the side air pad is λ₀/10 while the top is λ₀/4. Defensible
for a patch (radiation is broadside) but it is an asymmetry someone chose; is it
what you want? Also note `port_h: 13.6mm` is commented "smoke-matrix shape" — a
wave port on a patch feed edge, borrowed from a different recipe.

---

## X0b — same prompt as X0a, independent run (authored **blind**)

| variable | spec | note |
|---|---|---|
| patch_W | 38.0100 mm | **identical to X0a to 4 dp** |
| patch_L | 29.4216 mm | **identical to X0a to 4 dp** |
| feed_W | 3.0829 mm | identical |
| inset_d | 9.0 mm | X0a chose 9.77 mm — the tuner differs |
| sub_W/L | 80 × 80 mm | X0a chose 60 × 60 mm |
| feed_run | `"sub_L/2 - patch_L/2"` | **kept as an expression** — more parametric than X0a |
| air_pad | `"0.25 * c0 / f0"` | expression using `c0` |

**Two replicates converging on identical geometry to four decimal places** is a
good sign: the Balanis path is deterministic and both walked it correctly, blind.
The divergence is confined to judgement calls (substrate extent, inset depth),
which is the right place for it.

**On `c0`:** I flagged this as possibly undeclared, then checked — it is a
legitimate built-in in `hfss_spec/units.py`: `c0 = 299792458.0` with dimension
LENGTH/TIME. X0b's `"0.25 * c0 / f0"` is correct and dimensionally sound. No
concern. Using it is arguably *better* than X0a's hardcoded `31.2mm`, because the
air pad stays correct if `f0` changes.

**Unrelated but real, found while checking that:** the same `CONSTANTS` table
declares `eps0` and `mu0` as `DIMENSIONLESS`, which they are not (F/m and H/m).
Nothing in these six specs uses them, so no cell is affected — but any spec that
did would pass dimensional analysis that should have caught it. Worth a ticket.

---

## S1 — inset patch, 5.8 GHz, Rogers RO4350B 0.762 mm

| variable | spec | my independent check |
|---|---|---|
| patch_W | 17.2679 mm | 25.845·√(2/4.48) = 25.845·0.6682 = **17.27 mm** ✓ |
| patch_L | 13.6238 mm | W/h ≈ 22.7 → εeff ≈ 3.19; λ₀/(2√εeff) − 2ΔL ≈ **13.6 mm** ✓ |
| feed_W | 1.7427 mm | 50 Ω on this stack, W/h ≈ 2.3 — plausible ✓ |
| sub_W/L | 33 × 33 mm | patch + margin ✓ |
| air_pad | 13 mm | λ₀/4 = 12.92 mm ✓ |

**This is the strongest cell.** 5.8 GHz on RO4350B is not in the case set, so
every number had to be produced. All of them check out.

---

## S3 — pyramidal horn, 10 GHz, WR-90, 15 dBi (authored **blind**)

| variable | spec | my independent check |
|---|---|---|
| wg_a / wg_b | 0.9 in / 0.4 in | WR-90 inner dimensions ✓ |
| wall | 0.05 in | outer 1.000 × 0.500 in ✓ |
| horn_a × horn_b | 3.045 × 2.25 in | aperture A = 6.851 in² |
| gain | — | `G = 0.51·4πA/λ²`, λ = 1.1803 in → 0.51·61.80 = 31.5 → **14.99 dBi** ✓ |
| flare_len | 1.501 in | pe = ph = 1.501 in, consistent optimum-horn proportions |
| air_pad | 0.4 in | ≈ λ₀/3 ✓ |

Gain closes to **14.99 dBi against a 15 dBi ask** — and the pre-check reported
−0.09%, a *residual*, which is what an independent synthesis looks like when
checked by a separate relation. Contrast the patches' exact −0.00%.

**Worth your eye:** whether pe = ph is the flare geometry you want, and whether
8 geometry ops is enough to express a horn with a proper waveguide feed section.

---

## S4 — half-wave dipole, 2.45 GHz — **the pre-check validated NOTHING here**

`PASS: precheck recipe=half-wave-dipole verdict=no-estimator`

So this is the cell where your eye is doing all the work. My independent numbers:

| variable | spec | my independent check |
|---|---|---|
| L_arm | 28 mm | — |
| Gap | 2 mm | — |
| **L_tot** | **58 mm** | naive λ/2 = **61.18 mm**; real thin-wire resonance ≈ 0.47–0.48 λ = **57.5–58.7 mm** |
| WireD | 1 mm | as asked ✓ |
| AirGap | 30.6 mm | λ₀/4 = 30.59 mm ✓ |
| PortW | 4 mm | lumped port sheet across a 2 mm gap |

**This is the most interesting result in the batch.** 58 mm is **0.474 λ** — the
agent applied the end-effect shortening rather than naively taking λ/2 = 61.18 mm.
That is the textbook-correct choice and it is *not* something the tooling checked
or could have checked. If you agree it is right, that is a genuine capability
datum; if you think it should be 0.48 λ, the delta is ~1 mm.

**Worth your eye:** a 4 mm port sheet across a 2 mm gap on a 1 mm wire — the port
is wider than the gap and 4× the conductor. Plausible for a lumped port, but it
is the kind of detail that produces a valid-looking model with a wrong impedance.

---

## S7 — 2×2 patch array, 5.8 GHz, corporate feed — **27 geometry ops, 0 escape hatches**

| variable | spec | my independent check |
|---|---|---|
| patch_W / patch_L | 17.2679 / 13.6238 mm | same as S1 ✓ |
| **S** (spacing) | 25.8442 mm | λ₀/2 = **25.845 mm** ✓ exact |
| feed50_W | 1.7427 mm | 50 Ω ✓ (matches S1) |
| feed70_W | 0.9464 mm | 70.7 Ω = √(50·100) — **correct QWT impedance** ✓ |
| feed100_W | 0.4403 mm | 100 Ω ✓ |
| q70 | 7.984 mm | λg/4 → implies εeff ≈ 2.62; for W/h ≈ 1.24 on εr 3.48 that is **plausible** ✓ |
| air_pad | 12.9221 mm | λ₀/4 ✓ |
| sub_W/L | 52 × 52 mm | array extent S + patch_W ≈ 43.1 mm + margin ✓ |
| tand | 0.0037 | RO4350B loss tangent ✓ |

The corporate feed is a proper two-stage binary split with √2 impedance
transformers. **It enumerated four elements rather than reaching for an escape
hatch** — which is why the "missing array op" hypothesis is now a verbosity
problem, not a capability gap.

**Worth your eye:** the 100 Ω line is **0.4403 mm** wide. That is a real
manufacturing constraint question (many processes floor at ~0.1–0.15 mm, so it
passes) and, more importantly for simulation, a fine feature under an
**adaptive-only mesh** — schema v1 cannot express explicit mesh refinement. A
0.44 mm line next to a 17 mm patch is exactly the aspect ratio where
adaptive-only under-resolves.

---

## Summary of what I'd flag, ranked

1. **S4's port geometry** — 4 mm port across a 2 mm gap on a 1 mm wire. Highest
   chance of a valid-looking model with wrong impedance, and nothing checked it.
2. **S7's 0.44 mm line under adaptive-only mesh** — the schema cannot ask for
   refinement, so this may simulate cleanly and answer wrongly.
3. **X0a's asymmetric air pad** — λ₀/10 sides vs λ₀/4 top. Deliberate or drift?
4. **S3's flare proportions** — pe = ph; confirm that is the horn you want.
5. **X0a's borrowed `port_h`** — commented "smoke-matrix shape", i.e. a port
   dimension carried over from a different recipe. X0b used a different approach
   for the same structure.

Dropped from this list after checking: X0b's `c0`, which is a correct built-in.

Nothing in this list is a claim that a spec is wrong. They are the five places I
would look first if I were trying to find the wrongness, which is a different and
more useful thing than a score.
