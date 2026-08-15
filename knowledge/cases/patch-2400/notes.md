# patch-2400 - inset-fed rectangular patch, 2.4 GHz, FR4

The original Proof-1 recipe and the reference case for the whole tool: it
exercises every Spine stage without any geometry subtlety.

## Where the dimensions come from

All four values are recomputed, not copied. Balanis, *Antenna Theory*,
ch. 14 design procedure for a rectangular microstrip patch:

- width from 14-6, `W = c/(2f)*sqrt(2/(er+1))` -> **38.0100 mm**
- effective permittivity from 14-1 -> **4.0857**
- fringing extension from 14-2 -> **0.7388 mm**
- length from 14-7, `L = c/(2f*sqrt(ereff)) - 2*dL` -> **29.4216 mm**

Digits are carried well past what the physics justifies so that ticket 09's
estimators can be checked against them exactly. FR4 permittivity is itself
only good to a few percent, which is why the target tolerance is 5%.

## Known fragile

- Inset depth sets the feed match, not the resonance; it is tuned, and a
  wrong inset shows up as poor S11 depth with resonance in the right place.
- FR4 loss tangent varies by supplier; QA judges resonance position, not
  absolute S11 depth.
