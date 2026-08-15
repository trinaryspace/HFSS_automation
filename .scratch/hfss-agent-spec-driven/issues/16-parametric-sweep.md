# 16 — Parametric sweep from one spec: the payoff

**What to build:** Generate N designs from one spec plus a parameter range, build
and solve them, and collect the results into one comparison. This is where the
tool stops being a slower way to do what the user could do by hand and starts
doing something they would not: sweeping bowtie flare angle across eight values,
or substrate thickness across five, and reading the resonance trend out of the
set. It is nearly free once the spec exists — a sweep is a list comprehension
over specs, and every downstream layer already works one spec at a time.

Deliberately *not* optimization. No search, no surrogate, no objective function;
the user picks the parameter and the range, and the tool reports. Inverse design
is a later conversation and a different spec.

The real work is scheduling and evidence: solves are serial on one license, each
design needs its own workspace and banked solve marker, the watchdog must track
which design is in flight, and a partially-completed sweep must be resumable from
the ledger rather than restarted. Results collect into one table plus one overlay
plot, with per-design QA signals preserved so an anomalous member is visible
rather than averaged away.

**Blocked by:** 10, 11, 14. Also wants 01 and 13 (banking and readout must be
reliable before anything runs N times).

**Status:** needs-triage

- [ ] One spec plus a parameter range produces N validated specs, each with its own workspace
- [ ] Solves run serially with per-design banking; a killed sweep resumes from the ledger
- [ ] Results collect into one table and one overlay plot, with per-design QA signals retained
- [ ] The physics pre-check (ticket 09) runs across the whole set before any solve, so an out-of-range member is flagged before license time is spent
- [ ] Explicitly documented as reporting, not optimization
