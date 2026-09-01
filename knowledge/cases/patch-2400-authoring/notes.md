# patch-2400-authoring — the exemplar, split from the record

Not a sixth canonical case. It is deliberately absent from `index.json` and
carries no `case.json`, because it contributes no dimension of its own: every
number in it is `patch-2400`'s, and `patch-2400/case.json` remains the
provenance for all of them.

## Why it exists

`SKILL.md` and `reference/design-spec.md` both told the authoring agent to
start from `knowledge/cases/*/design.yaml`, naming `patch-2400` as the one that
"has been built and solved here". That file's `air_pad: 31mm  # ~lambda0/4 at
f0` is lambda0/4 at 2.4 GHz, against a lambda0/3 rule of 41.64 mm — and it says
so in a comment. In the 2026-08-31 parallel campaign four of five patch-family
specs independently chose lambda0/4 or worse. That is not five mistakes and it
is not a missing default; it is one contaminated exemplar, copied. The full
diagnosis is `.scratch/hfss-agent-parallel-tests/clearance-defect-mechanism.md`.

The obvious repair — correct the pad in `patch-2400` — is the one repair not
available. That file describes a model built and solved on this box on
2026-08-15 (session kind-rocket, S11 minimum 2.317 GHz at -20 dB), it is the
fixture behind the compiler's golden call sequences in
`hfss_spec/test_hfss_spec.py`, and `docs/agents/fixture-fidelity.md` exists
because this repo has twice shipped a P0 bug behind a fixture that no longer
matched its artifact. So the roles were split instead: the record keeps its
numbers and gains a warning comment, and authoring gets a file that is correct.

Neither of the two canonical specs that are *not* solved records could take the
job:

- `horn-10ghz` already clears by a full lambda0 and is not a patch. Rewriting
  its pad as `c0 / (3 * f0)` would shrink its airbox threefold — a physics
  change to the one case that was already compliant.
- `microstrip-50r`'s `air_pad` is not a radiation clearance at all. It sets the
  lid height, and both wave-port sheets are `h + air_pad` tall, so enlarging it
  changes the port cross-section of the only case whose target is an impedance.
  Whether the lambda0/3 rule should even apply to a non-radiating TEM line is
  an open question for the rule's owner, recorded in the diagnosis.

## What differs from the record

Two lines, both so the exemplar validates clean — an exemplar that trips the
validator is the defect it exists to cure:

| | `patch-2400` | here |
|---|---|---|
| `air_pad` | `31mm` (lambda0/4) | `"c0 / (3 * f0)"` (lambda0/3, 41.64 mm) |
| sweep | 2.0–3.0 GHz, 201 pts | 1.8–3.0 GHz, 241 pts |

Everything else is identical, on purpose: the diff is meant to be readable in
one screen, and every Balanis dimension traces to the same source.

The expression form is the point, not the value. `c0` is a constant that both
`hfss_spec.units` and AEDT provide, expressions pass through to AEDT verbatim,
and so the pad stays lambda0/3 when `f0` moves — where a literal would silently
stop being lambda0/3 and nothing would say so.

## Status

`validate_spec` reports `errors=0 warnings=0`; `precheck` reports
`verdict=consistent`. Nothing here has been built on a desktop. If it ever is,
it becomes a solved record too, and the next author needs a fresh exemplar
rather than an edit to this one.
