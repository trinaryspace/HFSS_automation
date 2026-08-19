"""Closed-form physics pre-check — the part that helps with EM. Ticket 09.

The highest-value-per-token component in the plan, because the thing it
answers in microseconds is the thing that otherwise costs a 7-minute solve and
hours of conversation. The motivating failure is exact: the Astuti bow-tie's
equations did not reproduce its own Table I / Figure 1, the discrepancy
survived clarification, geometry, materials, excitations, mesh, setup,
validation and **four solves**, and the user caught it at the results read
roughly twenty hours in.

Three rules, all of them load-bearing:

- **It never blocks and never overrides.** It prints both numbers and the
  signed disagreement; the user arbitrates and the choice is recorded in
  `provenance.canonical_reading`.
- **Tolerances are data, not code.** They live in
  `knowledge/playbook/precheck-tolerances.json`, because what counts as a
  disagreement worth raising is a domain judgement about how good a given
  closed form is.
- **Every estimator cites its relation** and is tested against a worked
  example whose answer is known independently — the `knowledge/cases/*` files
  carry those numbers recomputed rather than copied.

Stdlib only. No AEDT, no license, no pyAEDT.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from .expressions import Value, resolve_all
from .schema import DesignSpec
from .units import FREQUENCY, LENGTH, RESISTANCE

C0 = 299792458.0

REPO = Path(__file__).resolve().parent.parent
TOLERANCE_FILE = REPO / "knowledge" / "playbook" / "precheck-tolerances.json"


# --- estimators -------------------------------------------------------------


def effective_permittivity(er: float, h: float, w: float) -> float:
    """Balanis 14-1: the quasi-static effective permittivity of a microstrip.

        ereff = (er+1)/2 + (er-1)/2 * (1 + 12h/W)^(-1/2)

    Worked example (knowledge/cases/patch-2400): er 4.4, h 1.6 mm,
    W 38.0100 mm -> 4.0857.
    """
    if w <= 0 or h <= 0:
        raise ValueError("width and height must be positive")
    return (er + 1) / 2.0 + (er - 1) / 2.0 * (1.0 + 12.0 * h / w) ** -0.5


def fringing_extension(ereff: float, h: float, w: float) -> float:
    """Balanis 14-2: the length a patch appears to gain to fringing fields.

        dL/h = 0.412 * ((ereff+0.3)(W/h+0.264)) / ((ereff-0.258)(W/h+0.8))

    Worked example (patch-2400): ereff 4.0857, h 1.6 mm, W 38.0100 mm
    -> 0.7388 mm.
    """
    ratio = w / h
    return 0.412 * h * ((ereff + 0.3) * (ratio + 0.264)) / \
                       ((ereff - 0.258) * (ratio + 0.8))


def patch_resonance(patch_l: float, patch_w: float, h: float, er: float) -> float:
    """Resonant frequency of a rectangular microstrip patch, in Hz.

    Balanis 14-7 solved for frequency rather than length:

        f = c / (2 * (L + 2*dL) * sqrt(ereff))

    Worked example (patch-2400): L 29.4216 mm, W 38.0100 mm, h 1.6 mm,
    er 4.4 -> 2.4 GHz, the frequency the case was synthesised for.
    """
    ereff = effective_permittivity(er, h, patch_w)
    dl = fringing_extension(ereff, h, patch_w)
    return C0 / (2.0 * (patch_l + 2.0 * dl) * math.sqrt(ereff))


def microstrip_dispersion(er: float, h: float, w: float,
                          frequency: float) -> float:
    """Frequency-dependent effective permittivity, Kirschning & Jansen (1982).

        ereff(f) = er - (er - ereff(0)) / (1 + P(f))

    with P(f) the published P1..P4 fit. `effective_permittivity` above is the
    **quasi-static** value, i.e. the f -> 0 limit; the true ereff rises towards
    er as frequency climbs, because the field concentrates into the substrate.

    **This is a bias, not noise, and it has one sign.** Synthesising a patch
    from the static ereff always lands the resonance LOW, because the built
    patch is electrically longer than the static model thought. Measured
    2026-08-18 on the 2x2 array: both designs resonated at 5.6 GHz against a
    5.8 GHz target (-3.4%), identically, which is the signature of a systematic
    element-level bias rather than a feed defect. On that stack (RO4350B,
    er 3.48, h 0.762 mm, W 17.27 mm) this correction predicts -1.16% on its
    own; on the thicker, higher-er FR4 stack the same tool has shipped
    (er 4.4, h 1.6 mm) it predicts -2.9%.

    The bias was invisible to every gate because `patch_resonance` and the
    synthesis that produced the length used the *same* static ereff, so the
    pre-check confirmed its own error to four decimal places.

    Ref: M. Kirschning and R. H. Jansen, "Accurate model for effective
    dielectric constant of microstrip with validity up to millimetre-wave
    frequencies," Electronics Letters 18(6), 1982, pp. 272-273.
    """
    if frequency is None or frequency <= 0:
        return effective_permittivity(er, h, w)
    e0 = effective_permittivity(er, h, w)
    u = w / h
    fn = frequency / 1e9 * h * 1e3            # GHz-mm, the paper's normalisation
    p1 = (0.27488 + u * (0.6315 + 0.525 / (1.0 + 0.0157 * fn) ** 20)
          - 0.065683 * math.exp(-8.7513 * u))
    p2 = 0.33622 * (1.0 - math.exp(-0.03442 * er))
    p3 = 0.0363 * math.exp(-4.6 * u) * (1.0 - math.exp(-(fn / 38.7) ** 4.97))
    p4 = 1.0 + 2.751 * (1.0 - math.exp(-(er / 15.916) ** 8))
    pf = p1 * p2 * ((0.1844 + p3 * p4) * fn) ** 1.5763
    return er - (er - e0) / (1.0 + pf)


def patch_resonance_dispersive(patch_l: float, patch_w: float, h: float,
                               er: float) -> float:
    """`patch_resonance` with the dispersion correction, in Hz.

    ereff depends on frequency and frequency depends on ereff, so this is a
    fixed point; it converges in a handful of iterations because the correction
    is a few percent. Falls back to the last iterate if it ever fails to
    settle, so a pathological stack degrades rather than raising.
    """
    f = patch_resonance(patch_l, patch_w, h, er)        # static, as the seed
    for _ in range(40):
        ereff = microstrip_dispersion(er, h, patch_w, f)
        dl = fringing_extension(ereff, h, patch_w)
        nxt = C0 / (2.0 * (patch_l + 2.0 * dl) * math.sqrt(ereff))
        if abs(nxt - f) < 1e-3:
            return nxt
        f = nxt
    return f


def synthesize_rectangular_patch(frequency: float, er: float, h: float,
                                 dispersive: bool = True) -> dict:
    """Balanis 14-6/14-1/14-2/14-7 forward: (f0, er, h) -> the patch.

    Returns `{"width", "length", "ereff", "delta_l", "resonance"}` in SI, where
    `resonance` is the synthesised patch fed back through the *same* physics as
    a closure check.

    This exists as much for wall-clock as for correctness. Every array run so
    far has re-derived these four relations by hand in conversation, at real
    token and real minute cost, and hand-arithmetic is where the shipped
    defects have come from. A function is also the only place a correction like
    dispersion can be applied once and inherited everywhere.

    With `dispersive=True` the length is solved so the patch resonates at `f0`
    under the Kirschning-Jansen ereff - which is what the solver will see.
    """
    if frequency <= 0 or h <= 0 or er <= 1.0:
        raise ValueError("frequency, substrate height and er must be positive")
    width = C0 / (2.0 * frequency) * math.sqrt(2.0 / (er + 1.0))   # 14-6
    ereff = (microstrip_dispersion(er, h, width, frequency) if dispersive
             else effective_permittivity(er, h, width))            # 14-1
    delta_l = fringing_extension(ereff, h, width)                  # 14-2
    length = C0 / (2.0 * frequency * math.sqrt(ereff)) - 2.0 * delta_l   # 14-7
    check = (patch_resonance_dispersive(length, width, h, er) if dispersive
             else patch_resonance(length, width, h, er))
    return {"width": width, "length": length, "ereff": ereff,
            "delta_l": delta_l, "resonance": check}


def _bessel_j0(x: float) -> float:
    """J0(x) to ~1e-8, Abramowitz & Stegun 9.4.1 / 9.4.3. Stdlib only."""
    ax = abs(x)
    if ax < 3.0:
        y = (x / 3.0) ** 2
        return (1.0 - 2.2499997 * y + 1.2656208 * y ** 2 - 0.3163866 * y ** 3
                + 0.0444479 * y ** 4 - 0.0039444 * y ** 5 + 0.00021 * y ** 6)
    y = 3.0 / ax
    f0 = (0.79788456 - 0.00000077 * y - 0.0055274 * y ** 2
          - 0.00009512 * y ** 3 + 0.00137237 * y ** 4
          - 0.00072805 * y ** 5 + 0.00014476 * y ** 6)
    theta = (ax - 0.78539816 - 0.04166397 * y - 0.00003954 * y ** 2
             + 0.00262573 * y ** 3 - 0.00054125 * y ** 4
             - 0.00029333 * y ** 5 + 0.00013558 * y ** 6)
    return f0 * math.cos(theta) / math.sqrt(ax)


def _slot_integral(w: float, wavelength: float,
                   patch_l: Optional[float] = None) -> float:
    """The shared radiation integral behind Balanis 14-12 and 14-18a.

        I = INT_0^pi [sin(kW/2 cos t)/cos t]^2 * K(t) * sin^3 t dt

    with K = 1 for the self term (G1) and K = J0(kL sin t) for the mutual term
    (G12). One integrand, so the two conductances cannot drift apart.

    Simpson over 2000 panels; the integrand is smooth and the removable
    singularity at t = pi/2 is handled by the limit sin(kW/2 cos t)/cos t ->
    kW/2.
    """
    k = 2.0 * math.pi / wavelength
    n = 2000
    step = math.pi / n

    def f(t: float) -> float:
        c = math.cos(t)
        ratio = (k * w / 2.0) if abs(c) < 1e-12 else math.sin(k * w / 2.0 * c) / c
        kernel = 1.0 if patch_l is None else _bessel_j0(k * patch_l * math.sin(t))
        return ratio ** 2 * kernel * math.sin(t) ** 3

    total = f(0.0) + f(math.pi)
    for i in range(1, n):
        total += (4.0 if i % 2 else 2.0) * f(i * step)
    return total * step / 3.0


def slot_conductance(w: float, wavelength: float,
                     exact: bool = True) -> float:
    """Balanis 14-12: the radiating-slot conductance G1, in siemens.

    Exact (the default) is the integral form, G1 = I1 / (120 pi^2). The
    closed-form approximations

        G1 = (1/90)(W/lambda0)^2      W << lambda0
        G1 = (1/120)(W/lambda0)       W >> lambda0

    are available as `exact=False` and are what a hand calculation usually
    reaches for - but they are only asymptotes. On Balanis Example 14.1 the
    approximation gives 1.737e-3 S against the integral's 1.57e-3 S, an 11%
    error that propagates straight into the edge resistance and the inset
    depth. That is a large enough bias to matter for a match, so the accurate
    form is the default and the approximation is opt-in.

    Worked example (Balanis Example 14.1, RT/duroid 5880 at 10 GHz,
    W 1.186 cm, lambda0 3 cm): 1.57e-3 S.
    """
    if w <= 0 or wavelength <= 0:
        raise ValueError("width and wavelength must be positive")
    if not exact:
        ratio = w / wavelength
        return ratio ** 2 / 90.0 if ratio < 1.0 else ratio / 120.0
    return _slot_integral(w, wavelength) / (120.0 * math.pi ** 2)


def mutual_conductance(w: float, patch_l: float, wavelength: float) -> float:
    """Balanis 14-18a: G12 between the two radiating slots, in siemens.

        G12 = 1/(120 pi^2) INT_0^pi [sin(kW/2 cos t)/cos t]^2 J0(kL sin t) sin^3 t dt

    Worked example (Balanis Example 14.1): 6.1683e-4 S.

    This matters because the edge resistance is 1/(2(G1 + G12)) for the odd
    field distribution, and dropping G12 biases the inset depth by ~20%.
    """
    if w <= 0 or patch_l <= 0 or wavelength <= 0:
        raise ValueError("width, length and wavelength must be positive")
    return _slot_integral(w, wavelength, patch_l) / (120.0 * math.pi ** 2)


def patch_edge_resistance(w: float, patch_l: float, wavelength: float,
                          odd_mode: bool = True) -> float:
    """Balanis 14-17: the patch's input resistance at the radiating edge, ohms.

        Rin(y0 = 0) = 1 / (2 * (G1 +/- G12))

    plus for the odd (antisymmetric) resonant voltage distribution of the
    dominant mode, which is the usual case. Worked example (Balanis Example
    14.1): 228.3508 ohm.
    """
    g1 = slot_conductance(w, wavelength)
    g12 = mutual_conductance(w, patch_l, wavelength)
    denom = 2.0 * (g1 + g12 if odd_mode else g1 - g12)
    if denom <= 0:
        raise ValueError("degenerate conductance sum")
    return 1.0 / denom


def inset_depth(target_impedance: float, edge_resistance: float,
                patch_l: float) -> float:
    """Balanis 14-20a inverted: how far in to cut the feed, in metres.

        Rin(y0) = Rin(0) * cos^2(pi * y0 / L)
        =>  y0 = (L/pi) * arccos(sqrt(Rin_target / Rin(0)))

    Worked example (Balanis Example 14.1): 228.3508 ohm edge, 50 ohm target,
    L 0.906 cm -> y0 = 0.3126 cm.

    **The tool had no way to compute this at all.** `inset` appeared only in
    comments, so every run tuned the depth by hand or by solve. That is the
    expensive way to find a number that is one arccos away, and it is why the
    2x2 array's inset was carried as "the match tuner, expected to move +/-2 mm
    in the build".

    Raises when the target exceeds the edge resistance: no inset can raise the
    impedance above its edge value, and silently clamping would hand back a
    depth that does not match.
    """
    if edge_resistance <= 0 or patch_l <= 0:
        raise ValueError("edge resistance and patch length must be positive")
    if target_impedance <= 0:
        raise ValueError("target impedance must be positive")
    if target_impedance > edge_resistance:
        raise ValueError(
            f"target {target_impedance:.1f} ohm exceeds the edge resistance "
            f"{edge_resistance:.1f} ohm; an inset only lowers the impedance "
            f"- feed at the edge, or use a quarter-wave transformer"
        )
    return patch_l / math.pi * math.acos(
        math.sqrt(target_impedance / edge_resistance))


def circular_patch_effective_radius(a: float, h: float, er: float) -> float:
    """Balanis 14-66: the fringing-corrected radius of a circular patch, metres.

        ae = a * sqrt(1 + (2h / (pi * a * er)) * (ln(pi * a / (2h)) + 1.7726))

    The disc looks electrically larger than it is, exactly as the rectangular
    patch looks longer than it is (14-2); this is the circular analogue.
    """
    if a <= 0 or h <= 0 or er <= 0:
        raise ValueError("radius, substrate height and permittivity must be positive")
    return a * math.sqrt(
        1.0 + (2.0 * h / (math.pi * a * er)) * (math.log(math.pi * a / (2.0 * h)) + 1.7726)
    )


def circular_patch_resonance(a: float, h: float, er: float) -> float:
    """Dominant TM110 resonance of a circular microstrip patch, in Hz.

    Balanis 14-65 with the 14-66 effective radius:

        f110 = 1.8412 * c / (2 * pi * ae * sqrt(er))

    1.8412 is the first zero of J1'. Registered because cell S6 (2026-08-17) was
    asked for a circular patch, found no estimator, and — rather than relabel
    the recipe to borrow the rectangular one — proposed exactly this and stopped
    for approval. This is that approval landed.
    """
    ae = circular_patch_effective_radius(a, h, er)
    return 1.8412 * C0 / (2.0 * math.pi * ae * math.sqrt(er))


def bowtie_resonance(side: float, base: float, h: float, er: float) -> float:
    """Dominant-mode resonance of a bow-tie patch, in Hz.

    A bow-tie is treated as a pair of triangular patches, and the dominant
    TM10 mode of an equilateral triangular patch (Balanis, triangular
    microstrip antenna) gives

        f = 2c / (3 * a * sqrt(ereff))

    with `a` the side (leg) length, and ereff from the microstrip relation
    using the base as the effective width.

    Honesty note, and the reason this estimator is trusted at all: against
    the delivered pilot model — leg 26.3269 mm, base 20.2168 mm, h 1.6 mm,
    er 4.3 — it predicts 3.88 GHz against a **measured 3.85 GHz**, about
    +0.8%. It also predicts +10.9% against that model's 3.5 GHz target,
    which is the Astuti disagreement, flagged in microseconds instead of
    twenty hours.
    """
    ereff = effective_permittivity(er, h, base)
    return 2.0 * C0 / (3.0 * side * math.sqrt(ereff))


def microstrip_impedance(w: float, h: float, er: float) -> tuple[float, float]:
    """`(Z0 in ohm, ereff)` for a microstrip line — Hammerstad.

        W/h >= 1:  Z0 = 120*pi / (sqrt(ereff) * (W/h + 1.393
                                   + 0.667*ln(W/h + 1.444)))
        W/h <  1:  Z0 = 60/sqrt(ereff) * ln(8h/W + W/(4h))

    Worked example (knowledge/cases/microstrip-50r): W 3.0829 mm, h 1.6 mm,
    er 4.4 -> ereff 3.3323, Z0 50.0 ohm.
    """
    ereff = effective_permittivity(er, h, w)
    ratio = w / h
    if ratio >= 1.0:
        z0 = (120.0 * math.pi) / (math.sqrt(ereff) *
                                  (ratio + 1.393 + 0.667 * math.log(ratio + 1.444)))
    else:
        z0 = (60.0 / math.sqrt(ereff)) * math.log(8.0 / ratio + ratio / 4.0)
    return z0, ereff


def guide_wavelength(frequency: float, ereff: float) -> float:
    """Guide wavelength in metres: lambda_g = c / (f * sqrt(ereff)).

    Worked example (microstrip-50r): 2.4 GHz at ereff 3.3323 -> 68.4282 mm.
    """
    return C0 / (frequency * math.sqrt(ereff))


def pyramidal_horn_gain(a1: float, b1: float, wavelength: float,
                        aperture_efficiency: float = 0.51) -> float:
    """Gain of a pyramidal horn in dBi, from its aperture.

        G0 = eap * (4*pi / lambda^2) * a1 * b1

    `eap = 0.51` is the standard optimum-horn aperture efficiency (Balanis
    ch.13): the quadratic phase error across an optimum flare costs a little
    over half the physical aperture.
    """
    gain = aperture_efficiency * (4.0 * math.pi / wavelength ** 2) * a1 * b1
    return 10.0 * math.log10(gain)


def optimum_pyramidal_horn(gain_dbi: float, a: float, b: float,
                           wavelength: float) -> dict:
    """Synthesise an optimum-gain pyramidal horn. Balanis ch.13 procedure.

    Optimum here means the flare that maximises gain for a given axial
    length, which fixes the aperture phase error at the classic values:

        b1 = sqrt(2 * lambda * rho1)      (E-plane)
        a1 = sqrt(3 * lambda * rho2)      (H-plane)

    A *physically realisable* pyramidal horn additionally needs its two flares
    to meet the feed waveguide at the same axial station:

        pe = (b1 - b) * sqrt((rho1/b1)^2 - 1/4)
        ph = (a1 - a) * sqrt((rho2/a1)^2 - 1/4)
        pe == ph

    Balanis reduces the pair to one transcendental equation in chi = rho1 /
    lambda, solved here by bisection rather than by his hand iteration.

    Returns every dimension in metres plus the achieved gain, so the caller
    can check the synthesis closed rather than trusting it.
    """
    g0 = 10.0 ** (gain_dbi / 10.0)
    a_l, b_l = a / wavelength, b / wavelength

    def residual(chi: float) -> float:
        # Balanis 13-56: left and right sides of the pyramidal condition.
        left = (math.sqrt(2.0 * chi) - b_l) ** 2 * (2.0 * chi - 1.0)
        right = ((g0 / (2.0 * math.pi)) * math.sqrt(3.0 / (2.0 * math.pi * chi))
                 - a_l) ** 2 * ((g0 ** 2 / (6.0 * math.pi ** 3 * chi)) - 1.0)
        return left - right

    # Balanis's trial value chi1 = G0/(2*pi*sqrt(2*pi)) is a starting point for
    # his hand iteration, NOT a bound: at 15 dBi on WR-90 it lands above the
    # root, so bracketing upward from it never finds a sign change. Scan the
    # whole physical range instead. chi > 1/2 is required — (2*chi - 1) is a
    # factor of the left-hand side, so the equation is meaningless below it.
    low = high = None
    chi_scan = 0.51
    previous = residual(chi_scan)
    for _ in range(4000):
        nxt = chi_scan * 1.01
        current = residual(nxt)
        if previous * current <= 0:
            low, high = chi_scan, nxt
            break
        chi_scan, previous = nxt, current
    if low is None:
        raise ValueError(
            f"no pyramidal-horn solution for {gain_dbi} dBi on this waveguide — "
            f"the requested gain may be below what the feed itself already gives"
        )
    for _ in range(200):
        mid = 0.5 * (low + high)
        if residual(low) * residual(mid) <= 0:
            high = mid
        else:
            low = mid
    chi = 0.5 * (low + high)

    rho1 = chi * wavelength
    rho2 = (g0 ** 2 / (8.0 * math.pi ** 3)) * (1.0 / chi) * wavelength
    b1 = math.sqrt(2.0 * wavelength * rho1)
    a1 = math.sqrt(3.0 * wavelength * rho2)
    pe = (b1 - b) * math.sqrt((rho1 / b1) ** 2 - 0.25)
    ph = (a1 - a) * math.sqrt((rho2 / a1) ** 2 - 0.25)
    return {
        "a1": a1, "b1": b1, "rho1": rho1, "rho2": rho2,
        "pe": pe, "ph": ph, "axial_length": pe,
        "gain_dbi": pyramidal_horn_gain(a1, b1, wavelength),
        "chi": chi,
    }


def rectangular_waveguide_cutoff(a: float) -> float:
    """TE10 cutoff of a rectangular waveguide, in Hz: f_c = c / (2a).

    Worked example (knowledge/cases/horn-10ghz): WR-90's a = 0.9 in
    = 22.86 mm -> 6.5571 GHz.
    """
    return C0 / (2.0 * a)


# --- the check ---------------------------------------------------------------


@dataclass
class Prediction:
    quantity: str
    target: Optional[float]
    predicted: float
    unit: str
    tolerance_pct: float
    detail: list[tuple[str, str]]
    note: str = ""
    # Set only where a percentage disagreement is the wrong test — the horn's
    # check is "does TE10 propagate and stay single-mode", which is a band
    # membership question, not a distance from a number.
    ok: Optional[bool] = None

    @property
    def delta_pct(self) -> Optional[float]:
        if self.target in (None, 0):
            return None
        return 100.0 * (self.predicted - self.target) / self.target

    @property
    def consistent(self) -> bool:
        if self.ok is not None:
            return self.ok
        delta = self.delta_pct
        return delta is None or abs(delta) <= self.tolerance_pct

    def _fmt(self, value: Optional[float]) -> str:
        if value is None:
            return "n/a"
        scale = {"GHz": 1e9, "ohm": 1.0, "mm": 1e-3}.get(self.unit, 1.0)
        return f"{value / scale:.4f} {self.unit}"

    def text(self) -> str:
        lines = []
        for label, value in self.detail:
            lines.append(f"      {label:<22} {value}")
        lines.append("")
        lines.append(f"      {'target':<22} {self._fmt(self.target)}")
        delta = self.delta_pct
        suffix = "" if delta is None else \
            f"      delta: {delta:+.2f}%   tolerance: {self.tolerance_pct:g}%"
        lines.append(f"      {'closed-form':<22} {self._fmt(self.predicted)}{suffix}")
        # A delta of exactly zero is not the best possible result; it is a sign
        # the dimensions were produced by this same relation, so the check is
        # confirming its own arithmetic. Measured 2026-08-17: two authored specs
        # reported -0.00%, and their transcripts showed one importing
        # `hfss_spec.physics` to size the patch and the other re-running
        # `precheck` until it agreed. The horn, synthesised independently, came
        # in at -0.09%. A residual is the healthy outcome.
        if delta is not None and abs(delta) < 0.005:
            lines.append("")
            lines.append("      NOTE: delta is essentially zero, which usually "
                         "means the dimensions came from this same relation.")
            lines.append("            The check then confirms its own "
                         "arithmetic rather than the design; treat it as "
                         "unverified unless the numbers came from elsewhere.")
        if self.note:
            lines.append("")
            lines.append(f"      note: {self.note}")
        return "\n".join(lines)


@dataclass
class Precheck:
    recipe: str
    prediction: Optional[Prediction]
    reason: str = ""

    @property
    def verdict(self) -> str:
        if self.prediction is None:
            return "no-estimator"
        return "consistent" if self.prediction.consistent else "INCONSISTENT"

    def text(self) -> str:
        # A gate that checked nothing must not render as a gate that passed.
        # `PASS: precheck ... verdict=no-estimator` reads as a pass to anyone
        # skimming for the verification line, and cell S4 was exactly that: no
        # registered estimator, printed as PASS, and it also carried a real port
        # defect. UNCHECKED is its own word so the line cannot be misread.
        if self.verdict == "no-estimator":
            head = "UNCHECKED"
            tail = " - no estimator for this recipe; nothing was verified"
        elif self.verdict == "INCONSISTENT":
            head, tail = "FAIL", " — arbitrate before building"
        else:
            head, tail = "PASS", ""
        body = ""
        if self.prediction is not None:
            body = self.prediction.text() + "\n\n"
        elif self.reason:
            body = f"      {self.reason}\n\n"
        return (f"{body}{head}: precheck recipe={self.recipe} "
                f"verdict={self.verdict}{tail}\n")


def load_tolerances() -> dict:
    try:
        return json.loads(TOLERANCE_FILE.read_text(encoding="utf-8"))["recipes"]
    except (OSError, ValueError, KeyError):
        return {}


def check(spec: DesignSpec) -> Precheck:
    """Predict the spec's target quantity and compare. Never raises, never blocks."""
    recipes = load_tolerances()
    entry = recipes.get(spec.recipe, {})
    estimator = entry.get("estimator")
    if estimator is None:
        return Precheck(spec.recipe, None,
                        reason=f"no estimator registered for recipe "
                               f"{spec.recipe!r} in {TOLERANCE_FILE.name}")
    try:
        scope = resolve_all(spec.variable_scope())
    except Exception as exc:                      # noqa: BLE001 - never blocks
        return Precheck(spec.recipe, None, reason=f"variables unresolved: {exc}")

    # The spec's own tolerance wins when it states one; the playbook is the
    # fallback and the record of how far the closed form can be trusted.
    tolerance = (spec.target.tolerance_pct if spec.target is not None
                 else entry.get("tolerance_pct", 5.0))
    target = _target_si(spec, scope)
    try:
        prediction = _ESTIMATORS[estimator](spec, scope, target, tolerance,
                                            entry.get("note", ""))
    except Exception as exc:                      # noqa: BLE001 - never blocks
        return Precheck(spec.recipe, None, reason=f"estimator failed: {exc}")
    return Precheck(spec.recipe, prediction)


def _target_si(spec: DesignSpec, scope: dict[str, Value]) -> Optional[float]:
    if spec.target is None:
        return None
    from .expressions import evaluate
    try:
        return evaluate(spec.target.value, scope).si
    except Exception:                             # noqa: BLE001 - never blocks
        return None


def _var(scope: dict[str, Value], *names: str) -> float:
    """The first variable that exists, by SI magnitude."""
    for name in names:
        if name in scope:
            return scope[name].si
    raise KeyError(f"none of {names} is a declared variable")


def _mm(value: float) -> str:
    return f"{value * 1000:.4f} mm"


# Relative permittivity of the AEDT library materials a v1 recipe might use as
# a substrate. Only needed when the spec references a library material rather
# than defining one inline or declaring an `er` variable.
LIBRARY_PERMITTIVITY = {
    "fr4_epoxy": 4.4,
    "rogers rt/duroid 5880 (tm)": 2.2,
    "rogers rt/duroid 6002 (tm)": 2.94,
    "teflon_based": 2.1,
    "polyimide": 3.5,
    "alumina_96pct": 9.4,
    "quartz": 3.78,
    "air": 1.0,
    "vacuum": 1.0,
}

_NON_SUBSTRATE = {"air", "vacuum", "pec", "copper", "gold", "silver",
                  "aluminum", "aluminium"}


def _permittivity(spec: DesignSpec, scope: dict[str, Value]) -> float:
    """The substrate's relative permittivity, from wherever the spec put it.

    Three legal places, and a real spec uses different ones: an `er` variable
    (patch-2400), an inline material definition (the bow-tie's user-defined
    `FR4_43`, which is not a library entry), or a library reference whose
    value the spec never states.
    """
    from .schema import MaterialDef, MaterialRef

    for name in ("er", "epsilon_r", "eps_r", "Er", "ER"):
        if name in scope:
            return scope[name].si

    for key, material in spec.materials.items():
        if key.lower() in _NON_SUBSTRATE:
            continue
        if isinstance(material, MaterialDef):
            return resolve_all({"_er": material.permittivity})["_er"].si
        if isinstance(material, MaterialRef):
            value = LIBRARY_PERMITTIVITY.get(material.library.lower())
            if value is not None and value > 1.0:
                return value

    raise KeyError(
        "no permittivity: declare an `er` variable, define the substrate "
        "material inline, or reference a known library material"
    )


def _patch(spec, scope, target, tolerance, note) -> Prediction:
    """Rectangular patch resonance, predicted **with dispersion**.

    Changed 2026-08-19. It used to predict from the quasi-static ereff, which
    is the same ereff the synthesis used, so the check confirmed its own
    assumption and reported a perfect zero disagreement on a patch that would
    resonate 1-3% low. The 2x2 run measured exactly that: 5.6 GHz against 5.8,
    identically in two independent designs, on a spec whose precheck was clean.
    A pre-check that shares the synthesis's blind spot is worse than none,
    because it converts an open question into a false green.

    Both numbers are reported. The static one is what the length was probably
    synthesised from; the dispersive one is what the solver will find.
    """
    length = _var(scope, "patch_L", "PatchL", "L")
    width = _var(scope, "patch_W", "PatchW", "W")
    h = _var(scope, "h", "SubH", "sub_h")
    er = _permittivity(spec, scope)
    static = patch_resonance(length, width, h, er)
    predicted = patch_resonance_dispersive(length, width, h, er)
    ereff_s = effective_permittivity(er, h, width)
    ereff_f = microstrip_dispersion(er, h, width, predicted)
    dl = fringing_extension(ereff_f, h, width)
    return Prediction(
        "resonant_frequency", target, predicted, "GHz", tolerance,
        [("patch length (14-7)", _mm(length)),
         ("patch width (14-6)", _mm(width)),
         ("ereff static (14-1)", f"{ereff_s:.4f}"),
         ("ereff at f0 (Kirschning-Jansen)", f"{ereff_f:.4f}"),
         ("fringing dL (14-2)", _mm(dl)),
         ("static prediction (no dispersion)", f"{static / 1e9:.4f} GHz")],
        note,
    )


def _circular_patch(spec, scope, target, tolerance, note) -> Prediction:
    radius = _var(scope, "patch_a", "patch_R", "a", "radius", "patch_radius")
    h = _var(scope, "h", "SubH", "sub_h")
    er = _permittivity(spec, scope)
    ae = circular_patch_effective_radius(radius, h, er)
    predicted = circular_patch_resonance(radius, h, er)
    return Prediction(
        "resonant_frequency", target, predicted, "GHz", tolerance,
        [("physical radius a", _mm(radius)),
         ("effective radius ae (14-66)", _mm(ae)),
         ("substrate h", _mm(h)),
         ("er", f"{er:.4f}")],
        note,
    )


def _bowtie(spec, scope, target, tolerance, note) -> Prediction:
    side = _var(scope, "PatchLeg", "patch_leg", "leg")
    base = _var(scope, "PatchBase", "patch_base", "base")
    h = _var(scope, "SubH", "h", "sub_h")
    er = _permittivity(spec, scope)
    ereff = effective_permittivity(er, h, base)
    predicted = bowtie_resonance(side, base, h, er)
    return Prediction(
        "resonant_frequency", target, predicted, "GHz", tolerance,
        [("leg / side", _mm(side)),
         ("base", _mm(base)),
         ("ereff (14-1 on base)", f"{ereff:.4f}")],
        note,
    )


def _microstrip(spec, scope, target, tolerance, note) -> Prediction:
    width = _var(scope, "trace_W", "feed_W", "W", "w")
    h = _var(scope, "h", "SubH", "sub_h")
    er = _permittivity(spec, scope)
    z0, ereff = microstrip_impedance(width, h, er)
    return Prediction(
        "impedance", target, z0, "ohm", tolerance,
        [("trace width", _mm(width)),
         ("W/h", f"{width / h:.5f}"),
         ("ereff (14-1)", f"{ereff:.4f}")],
        note,
    )


def _horn(spec, scope, target, tolerance, note) -> Prediction:
    """Aperture gain, with the feed's TE10 band as a hard sanity gate.

    The gain is the design's stated target, so it is what gets compared. The
    cutoff check rides along because a horn whose feed does not propagate — or
    that is running multi-mode — has a gain number that means nothing.
    """
    a = _var(scope, "wg_a", "WG_a", "guide_a", "a")
    cutoff = rectangular_waveguide_cutoff(a)
    operating = _var(scope, "f0", "design_freq", "freq")
    wavelength = C0 / operating
    ratio = operating / cutoff
    a1 = _var(scope, "horn_a", "Horn_a", "aperture_a", "a1")
    b1 = _var(scope, "horn_b", "Horn_b", "aperture_b", "b1")
    gain = pyramidal_horn_gain(a1, b1, wavelength)
    single_mode = 1.0 < ratio < 2.0
    detail = [("aperture a1", _mm(a1)),
              ("aperture b1", _mm(b1)),
              ("free-space lambda", _mm(wavelength)),
              ("TE10 cutoff", f"{cutoff / 1e9:.4f} GHz"),
              ("f / f_c", f"{ratio:.4f}  (want 1 < f/f_c < 2)")]
    prediction = Prediction(
        "gain", target, gain, "dBi", tolerance, detail,
        note or "aperture-efficiency estimate (eap 0.51); pattern is not predicted",
    )
    if not single_mode:
        prediction.ok = False
        prediction.note = (f"feed is outside the single-mode TE10 band "
                           f"(f/f_c = {ratio:.3f}) — the gain estimate is not "
                           f"meaningful")
    return prediction


_ESTIMATORS = {
    "patch_resonance": _patch,
    "circular_patch_resonance": _circular_patch,
    "bowtie_resonance": _bowtie,
    "microstrip_impedance": _microstrip,
    "horn_cutoff": _horn,
}


def active_reflection(s_row, excitation=None):
    """Active reflection coefficient of one element in an excited array.

    `s_row` is that element's row of the array S-matrix (complex, port order
    fixed); `excitation` is the incident wave at each port, defaulting to uniform
    broadside (all equal). Returns the complex active reflection coefficient

        gamma_act,i = sum_j S_ij * (a_j / a_i)

    **Why this matters, and why an isolated patch impedance is the wrong target.**
    At half-wavelength spacing the elements are strongly enough coupled that what
    a feed actually sees is not the isolated element impedance. Matching to the
    isolated value leaves a real mismatch that no amount of correct feed
    arithmetic removes, because the arithmetic was solved against the wrong load.

    The proper order is therefore: simulate the elements with individual ports
    and no feed network, extract the S-matrix, compute the active impedance from
    it, and only then synthesise the match.
    """
    values = list(s_row)
    if not values:
        raise ValueError("s_row must contain at least the element's own S_ii")
    if excitation is None:
        excitation = [1.0] * len(values)
    excitation = list(excitation)
    if len(excitation) != len(values):
        raise ValueError("excitation must have one entry per port")
    self_a = excitation[0]
    if self_a == 0:
        raise ValueError("the element's own excitation cannot be zero")
    return sum(s * (a / self_a) for s, a in zip(values, excitation))


def impedance_from_gamma(gamma, z0=50.0):
    """Convert a reflection coefficient to an impedance, `Z = Z0 (1+g)/(1-g)`."""
    denominator = 1.0 - gamma
    if denominator == 0:
        raise ValueError("gamma = 1 is an open circuit; impedance is unbounded")
    return z0 * (1.0 + gamma) / denominator


def active_impedance(s_row, excitation=None, z0=50.0):
    """The impedance one element presents while the whole array is driven."""
    return impedance_from_gamma(active_reflection(s_row, excitation), z0)
