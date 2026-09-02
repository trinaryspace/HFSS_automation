"""Tier 0 tests for the pain-point classifiers (run logging, ticket 05).

Ground truth, all real (docs/agents/fixture-fidelity.md):

- `scripts/fixtures/opencode/ses_fe9ae6dd3ffe2a8knbeE1b4yrr.jsonl` — the
  Aug 18 patch-array-5800 run, opencode session `neon-eagle` with its two
  subagents `cosmic-knight` (kb-lookup, in the clarify phase) and
  `hidden-falcon` (runcard, in the last solve phase). One session carries all
  seven phase declarations of the run as `scripts/session.py --phase`
  commands; no `sessions.jsonl` or `events.jsonl` existed yet.
- `scripts/fixtures/claude-code/f0c832a3-….jsonl` — a real Claude Code
  session that never declared a phase (`ls -R`, two 13-17 KB reads, one
  failed `python -c`).
- `scripts/fixtures/claude-code/a0e9c38f-….jsonl` — a real Claude Code
  session with two subagents (20 and 18 tool calls; recaptured with the
  ticket-06 slicer, so their tool blocks and output heads are present).
- `scripts/fixtures/patch-array-5800/state/` — every `results/state/` file
  of the real workspace, byte for byte (`capture.py` there).

Since ticket 06 the trace carries each command whole, the first 2 KB of
every tool output (`output_head`) and of every edit / write input
(`input_head`), and stamps an opencode tool call at its emission
(`time_created`), so the seq literals below are the recaptured slice's.

Where a classifier has no positive in any of those, the positive is built
from a real step or a real writer and the test name says `synthetic`: a copy
of a real step with one field changed (`_variant`, which asserts the key set
is the real one), an event from `hfss_spec.events.record`, a history line
from `hfss_spec.session.history_record`, a watchdog line from the real
`poll_solve.format_progress`. Nothing here is typed from memory.

Run: `python hfss_spec/test_painpoints.py`
"""

import json
import os
import sys
import unittest
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SRC = REPO / "skill" / "hfss-agent" / "templates" / "workspace" / "src"
for entry in (str(REPO), str(REPO / "scripts"), str(SRC)):
    if entry not in sys.path:
        sys.path.insert(0, entry)

from hfss_spec import events, painpoints as P            # noqa: E402
from hfss_spec import session as S                       # noqa: E402
import poll_solve                                        # noqa: E402
import run_trace                                         # noqa: E402

FIXTURES = REPO / "scripts" / "fixtures"
OPENCODE_SLICE = FIXTURES / "opencode" / "ses_fe9ae6dd3ffe2a8knbeE1b4yrr.jsonl"
CLAUDE_SLICE = FIXTURES / "claude-code" / "f0c832a3-cb36-4168-ac07-70c2793c74a2.jsonl"
CLAUDE_TEXT_ONLY = FIXTURES / "claude-code" / "a0e9c38f-3117-4d93-8086-9b4f16ee0d52.jsonl"
STATE_DIR = FIXTURES / "patch-array-5800" / "state"

NEON = "ses_fe9ae6dd3ffe2a8knbeE1b4yrr"          # neon-eagle, the run
KNIGHT = "ses_fe964cc55ffeHbmOUhRVH9huBi"        # cosmic-knight, kb-lookup subagent
FALCON = "ses_fe8c117fdffeX8Q8m5QQ6By5Cz"        # hidden-falcon, runcard subagent
F0 = "f0c832a3-cb36-4168-ac07-70c2793c74a2"

# The seven declarations in neon-eagle, by the seq of the `session.py
# --phase` call (read off the trace by hand): clarify 149, build 243, solve
# 473, build-2 536, solve-1b 648 (failed: cwd) and 652 (landed), build-3
# 740, solve-2 822. The main session has 908 steps (0..907). A tool call's
# ts is the part row's time_created (ticket 06), so a call emitted before a
# user typed sits before that text: the build declaration is seq 243, and
# the Start-Sleep call (517) precedes the user's mid-sleep message (518).
DECLARATION_SEQS = (149, 243, 473, 536, 652, 740, 822)
MAIN_STEPS = 908
KNIGHT_STEPS, FALCON_STEPS = 16, 30

_CACHE = {}


def neon_steps():
    if "neon" not in _CACHE:
        store = run_trace.SliceStore(OPENCODE_SLICE)
        family = run_trace.trace_opencode_family(store, NEON)
        _CACHE["neon"] = [s for steps in family.values() for s in steps]
    return [dict(s) for s in _CACHE["neon"]]


def claude_steps(path=CLAUDE_SLICE):
    key = ("claude", str(path))
    if key not in _CACHE:
        family = run_trace.trace_claude(path)
        _CACHE[key] = [s for steps in family.values() for s in steps]
    return [dict(s) for s in _CACHE[key]]


def machine_state():
    if "state" not in _CACHE:
        _CACHE["state"] = {name: (STATE_DIR / name).read_text(encoding="utf-8-sig")
                           for name in os.listdir(STATE_DIR)}
    return dict(_CACHE["state"])


def by_kind(findings):
    out = defaultdict(list)
    for f in findings:
        out[f["kind"]].append(f)
    return out


def main_only(steps):
    return [s for s in steps if s["session_id"] == NEON]


def step(steps, session, seq):
    return next(s for s in steps if s["session_id"] == session and s["seq"] == seq)


def _variant(real, **changes):
    """A copy of a real step with some fields changed. The key set must be
    the real one, so a synthetic step can never define the shape."""
    copy = dict(real)
    for key, value in changes.items():
        if key not in run_trace.STEP_KEYS and key not in P.TEXT_KEYS:
            raise AssertionError(f"{key} is not a step key")
        copy[key] = value
    # `output_head` is both a real step key and a text key; the other text
    # keys are the ones a future trace may add.
    assert set(copy) - set(P.TEXT_KEYS) == set(run_trace.STEP_KEYS) - set(P.TEXT_KEYS)
    return copy


def _event(name, now_ms, **fields):
    """An event exactly as `hfss_spec.events` would write it."""
    return events.record(str(REPO / "nonexistent-state-dir"), name, now_ms=now_ms, **fields)


class TestFixturesArePresent(unittest.TestCase):
    """A missing corpus is a failure, never a skip (fixture-fidelity rule 4)."""

    def test_slices_and_state(self):
        for path in (OPENCODE_SLICE, CLAUDE_SLICE, CLAUDE_TEXT_ONLY):
            self.assertTrue(path.is_file(), path)
        index = json.loads((FIXTURES / "patch-array-5800" / "index.json").read_text())
        for name in ("solve_progress.txt", "readouts.txt", "aedt_port.txt",
                     "session.json", "solved.txt", "outcome.txt", "z_act.txt"):
            self.assertTrue((STATE_DIR / name).is_file(), name)
            entry = index["files"]["state/" + name]
            self.assertEqual(entry["bytes"], (STATE_DIR / name).stat().st_size)
        steps = neon_steps()
        self.assertEqual(Counter(s["session_id"] for s in steps),
                         {NEON: MAIN_STEPS, KNIGHT: KNIGHT_STEPS, FALCON: FALCON_STEPS})


class TestAttribution(unittest.TestCase):

    def test_declarations_read_off_the_trace(self):
        steps = neon_steps()
        decls = P.declarations(steps, [], [])
        self.assertEqual([d[1] for d in decls],
                         ["clarify", "build", "solve", "build", "solve", "build", "solve"])
        self.assertTrue(all(d[3] == "trace" and d[2] == NEON for d in decls))
        # The failed declaration (emitted 22:29:06, `can't open file
        # ...\scripts\session.py`) and the one that landed 18 s later are
        # one cluster, and the cluster keeps the LATEST instant.
        self.assertEqual(decls[4][0], step(steps, NEON, 652)["ts"])
        self.assertIn("No such file", step(steps, NEON, 649)["output_head"])
        self.assertIn("PASS: session declared phase=solve", step(steps, NEON, 653)["output_head"])

    def test_step_count_by_phase_matches_the_hand_count(self):
        steps = neon_steps()
        attributed = P.attribute(steps)
        counts = Counter((s["phase"], s["phase_index"]) for s in attributed)
        # Hand count: the main session's steps between consecutive
        # declaration seqs (the first phase also owns the 149 steps before
        # its declaration — backfilled), plus each subagent in the phase
        # its parent was in when it ran.
        bounds = (0,) + DECLARATION_SEQS[1:] + (MAIN_STEPS,)
        expected = {}
        for i, phase in enumerate(["clarify", "build", "solve", "build", "solve", "build", "solve"]):
            expected[(phase, i)] = bounds[i + 1] - bounds[i]
        expected[("clarify", 0)] += KNIGHT_STEPS          # cosmic-knight ran 20:41
        expected[("solve", 6)] += FALCON_STEPS            # hidden-falcon ran 23:39
        self.assertEqual(dict(counts), expected)
        self.assertEqual(sum(counts.values()), len(steps))
        self.assertEqual(Counter(s["phase_source"] for s in attributed),
                         {"trace": len(steps) - 149, "backfill": 149})

    def test_subagents_inherit_the_parent_phase(self):
        attributed = P.attribute(neon_steps())
        self.assertEqual({s["phase"] for s in attributed if s["session_id"] == KNIGHT}, {"clarify"})
        self.assertEqual({s["phase"] for s in attributed if s["session_id"] == FALCON}, {"solve"})

    def test_stage_fallback_from_commands_hand_picked(self):
        attributed = P.attribute(neon_steps())
        expect = {253: "compile", 254: "compile", 257: "snapshot", 353: "sync-verify",
                  476: "solve", 529: "solve", 857: "readout", 876: "summary",
                  232: "gate", 3: P.BETWEEN, 187: P.BETWEEN}
        for seq, stage in expect.items():
            s = step(attributed, NEON, seq)
            self.assertEqual(s["stage"], stage, (seq, s["command"]))
            self.assertEqual(s["stage_source"], "commands")
        # A read of compile_spec.py is not a compile (seq 99).
        self.assertEqual(step(attributed, NEON, 99)["stage"], P.BETWEEN)

    def test_stage_from_events_beats_the_command_fallback(self):
        steps = neon_steps()
        use, result = step(steps, NEON, 253), step(steps, NEON, 254)
        sleep = step(steps, NEON, 518)
        evs = [_event("compile.start", use["ts"] + 5, stage="compile"),
               _event("stage.start", use["ts"] + 6, stage="geometry"),   # the compiler's sub-stage
               _event("stage.end", use["ts"] + 7, stage="geometry", verdict="PASS: geometry"),
               _event("compile.end", result["ts"] - 1, stage="compile", verdict="PASS: compile_spec"),
               _event("solve.submitted", sleep["ts"] - 60_000, stage="solve"),
               _event("solve.terminal", sleep["ts"] + 60_000, stage="solve", detail="tick=9 status=complete"),
               _event("snapshot.captured", step(steps, NEON, 258)["ts"] - 1, stage="snapshot")]
        attributed = P.attribute(steps, evs)
        self.assertEqual(step(attributed, NEON, 253)["stage"], "compile")
        self.assertEqual(step(attributed, NEON, 254)["stage_source"], "events")
        self.assertEqual(step(attributed, NEON, 518)["stage"], "solve")
        self.assertEqual(step(attributed, NEON, 257)["stage"], "snapshot")   # the point event inside the call
        self.assertEqual(step(attributed, NEON, 857)["stage"], P.BETWEEN)    # no event covered the readout

    def test_history_and_events_declare_a_session(self):
        steps = claude_steps()
        first_ts = min(s["ts"] for s in steps)
        record = S.history_record(S.Session(phase="solve", name="t", started_ms=first_ts - 1000,
                                            host="claude-code", host_session_id=F0),
                                  cwd=str(REPO), commit="abc1234")
        attributed = P.attribute(steps, [], [record])
        self.assertEqual({s["phase"] for s in attributed}, {"solve"})
        self.assertEqual({s["phase_source"] for s in attributed}, {"history"})
        ev = _event("phase.declared", first_ts - 500, phase="build",
                    detail=f"name=t host=claude-code session_id={F0} budget=60 declared=1")
        attributed = P.attribute(steps, [ev], [])
        self.assertEqual({s["phase"] for s in attributed}, {"build"})
        # A declaration naming a session the trace does not know governs by time.
        ev = _event("phase.declared", first_ts - 500, phase="clarify",
                    detail="name=t host=opencode session_id=some-slug budget=60 declared=1")
        self.assertEqual({s["phase"] for s in P.attribute(steps, [ev], [])}, {"clarify"})

    def test_undeclared_stays_undeclared(self):
        attributed = P.attribute(claude_steps())
        self.assertEqual({s["phase"] for s in attributed}, {P.UNDECLARED})


class TestHeavyOutput(unittest.TestCase):

    def test_real_positive_neon_eagle(self):
        found = P.find_heavy_output(P.attribute(neon_steps()))
        self.assertEqual(len(found), 19)
        biggest = max(found, key=lambda f: int(f["evidence"].split(" B:")[0].split()[-1].replace(",", "")))
        self.assertIn("physics.py", biggest["evidence"])
        self.assertIn("27,707 B", biggest["evidence"])
        spine = next(f for f in found if "spine-api.md" in f["evidence"])
        self.assertIn("16,740 B", spine["evidence"])
        self.assertIn("stayed in context for 883 later steps", spine["evidence"])
        self.assertEqual(spine["steps"], [23, 24])

    def test_real_positive_claude_code(self):
        found = P.find_heavy_output(P.attribute(claude_steps()))
        self.assertEqual({tuple(f["steps"]) for f in found}, {(7, 8), (15, 16)})

    def test_real_negative_results_under_the_floor(self):
        # Every real session on this box has at least one output above the
        # floor (the a0e9c38f subagents included, now that their slices
        # carry tool blocks), so the negative is a real session's steps
        # with its over-floor results left out: real steps, nothing added.
        steps = [s for s in claude_steps(CLAUDE_TEXT_ONLY) if s["parent_session_id"]]
        self.assertTrue(any((s["out_bytes"] or 0) > P.HEAVY_OUTPUT_BYTES for s in steps))
        under = [s for s in steps if s["kind"] != "tool_result"
                 or (s["out_bytes"] or 0) <= P.HEAVY_OUTPUT_BYTES]
        self.assertTrue(any(s["kind"] == "tool_result" for s in under))
        self.assertEqual(P.find_heavy_output(P.attribute(under)), [])


class TestLongReasoning(unittest.TestCase):

    def test_real_positive_opencode_bytes(self):
        found = P.find_long_reasoning(P.attribute(neon_steps()))
        self.assertEqual(len(found), 31)
        biggest = max(found, key=lambda f: int(f["evidence"].split(" B")[0].replace(",", "")))
        self.assertTrue(biggest["evidence"].startswith("60,572 B reasoning before:"))
        self.assertNotIn("estimated", biggest["evidence"])

    def test_real_positive_claude_code_estimated_from_tokens(self):
        # Claude Code stores thinking with no text: bytes are 0 and the
        # request's tokens_reasoning is the measure (1312 tokens at seq 37).
        found = P.find_long_reasoning(P.attribute(claude_steps()))
        self.assertEqual([f["steps"] for f in found], [[37]])
        self.assertIn("estimated from tokens_reasoning", found[0]["evidence"])
        self.assertIn(f"{1312 * P.BYTES_PER_TOKEN:,} B", found[0]["evidence"])

    def test_real_negative_hidden_falcon(self):
        steps = [s for s in neon_steps() if s["session_id"] == FALCON]
        self.assertEqual(P.find_long_reasoning(P.attribute(steps)), [])


class TestWholeFileRead(unittest.TestCase):

    def test_real_positive_runcard_subagent_read_the_tick_log(self):
        found = P.find_whole_file_read(P.attribute(neon_steps()))
        self.assertEqual(len(found), 1)
        self.assertEqual((found[0]["session"], found[0]["steps"]), (FALCON, [22, 23]))
        self.assertIn("solve_progress.txt", found[0]["evidence"])
        self.assertIn("19,295 B", found[0]["evidence"])

    def test_real_negative_tail_reads_in_the_main_session(self):
        found = P.find_whole_file_read(P.attribute(main_only(neon_steps())))
        self.assertEqual(found, [])      # every read there was `-Tail N`

    def test_synthetic_beside_real_cat_without_tail(self):
        real = step(neon_steps(), NEON, 704)     # `Get-Content ... solve_progress.txt -Tail 1`
        whole = _variant(real, command="Get-Content results/state/solve_progress.txt")
        self.assertEqual(len(P.find_whole_file_read(P.attribute([whole]))), 1)
        self.assertEqual(P.find_whole_file_read(P.attribute([real])), [])


class TestRecursiveListing(unittest.TestCase):

    def test_real_positive_claude_ls_R(self):
        found = P.find_recursive_listing(P.attribute(claude_steps()))
        self.assertEqual([f["steps"] for f in found], [[3, 4]])
        self.assertIn("ls -R", found[0]["evidence"])
        self.assertIn(" B", found[0]["evidence"])

    def test_real_positive_get_childitem_recurse(self):
        found = P.find_recursive_listing(P.attribute(main_only(neon_steps())))
        seqs = {f["steps"][0] for f in found}
        self.assertTrue({50, 61, 84} <= seqs, seqs)

    def test_real_negative_subagents(self):
        steps = [s for s in neon_steps() if s["session_id"] == FALCON]
        self.assertEqual(P.find_recursive_listing(P.attribute(steps)), [])


class TestRetrySameCommand(unittest.TestCase):

    def test_real_positive_capture_state_twice_in_snapshot(self):
        found = P.find_retry_same_command(P.attribute(neon_steps()))
        hit = next(f for f in found if "capture_state.py" in f["evidence"])
        self.assertEqual(hit["steps"], [350, 351, 415, 416])
        self.assertEqual((hit["phase"], hit["stage"]), ("build", "snapshot"))
        self.assertIn("x2", hit["evidence"])

    def test_real_negative_claude(self):
        self.assertEqual(P.find_retry_same_command(P.attribute(claude_steps())), [])


class TestIdenticalErrorTwice(unittest.TestCase):

    def test_real_negative_errors_never_consecutive(self):
        for steps in (neon_steps(), claude_steps()):
            self.assertTrue(any(s["is_error"] for s in steps))
            self.assertEqual(P.find_identical_error_twice(P.attribute(steps)), [])

    def test_synthetic_beside_real_same_error_twice(self):
        steps = neon_steps()
        use, result = step(steps, NEON, 39), step(steps, NEON, 40)    # the real failed read
        self.assertTrue(result["is_error"])
        again = [_variant(use, seq=41, tool_use_id="again"), _variant(result, seq=42, tool_use_id="again")]
        found = P.find_identical_error_twice(P.attribute([use, result] + again))
        self.assertEqual(len(found), 1)
        self.assertIn("S7.design.yaml", found[0]["evidence"])
        self.assertEqual(found[0]["steps"], [39, 40, 41, 42])

    def test_synthetic_beside_real_signature_from_output_text(self):
        steps = neon_steps()
        use, result = step(steps, NEON, 39), step(steps, NEON, 40)
        text = "ansys.aedt.core.internal.errors.GrpcApiError: Failed to execute gRPC AEDT command: Subtract"
        self.assertEqual(P.error_signature(_variant(result, output_head=text)), "GrpcApiError Subtract")


class TestRebuildChain(unittest.TestCase):

    def test_real_positive_every_build_phase(self):
        found = P.find_rebuild_chain(P.attribute(neon_steps()))
        self.assertEqual(sorted(f["evidence"].split(" in build #")[1][0] for f in found), ["1", "3", "5"])
        # With the commands whole, every compile's --spec is visible: 3 / 4
        # / 6 compiles in the three build phases (the cut trace read 5 / 5).
        counts = {f["evidence"].split(" in build #")[1][0]: int(f["evidence"].split(" compiles")[0])
                  for f in found}
        self.assertEqual(counts, {"1": 3, "3": 4, "5": 6})
        for index in ("3", "5"):
            chain = next(f for f in found if f"build #{index}" in f["evidence"])
            self.assertIn("ws_common.py", chain["evidence"])
            self.assertEqual(chain["stage"], "compile")

    def test_real_negative_claude(self):
        self.assertEqual(P.find_rebuild_chain(P.attribute(claude_steps())), [])

    def test_from_events_synthetic_beside_real(self):
        steps = neon_steps()
        t0 = step(steps, NEON, 253)["ts"]
        evs = [_event("phase.declared", t0 - 10, phase="build"),
               _event("compile.start", t0, stage="compile"),
               _event("stage.end", t0 + 100, stage="geometry", verdict="FAIL: geometry boom"),
               _event("compile.start", t0 + 200, stage="compile")]
        found = P.find_rebuild_chain(P.attribute(steps, evs), evs)
        self.assertEqual(len(found), 1)
        self.assertIn("FAIL: geometry boom", found[0]["evidence"])
        self.assertEqual(found[0]["source"], "events")


class TestForegroundPoll(unittest.TestCase):

    def test_real_positive_start_sleep(self):
        found = P.find_foreground_poll(P.attribute(neon_steps()))
        four = next(f for f in found if "Start-Sleep -Seconds 240" in f["evidence"])
        self.assertEqual(four["steps"], [517, 519])
        # The call's real wall (emitted -> result, 241 s) now beats the
        # declared 240 s; before ticket 06 the call measured 32 ms.
        self.assertGreaterEqual(four["cost_wall_ms"], 240_000)
        self.assertLess(four["cost_wall_ms"], 245_000)
        self.assertIn("4 min 0 s declared", four["evidence"])

    def test_real_negative_reads_within_a_minute(self):
        found = P.find_foreground_poll(P.attribute(neon_steps()))
        self.assertFalse([f for f in found if "reads of" in f["evidence"]])

    def test_synthetic_beside_real_three_tail_reads_in_a_minute(self):
        real = step(neon_steps(), NEON, 704)
        reads = [_variant(real, seq=i, ts=real["ts"] + i * 10_000, tool_use_id=f"t{i}") for i in range(3)]
        found = P.find_foreground_poll(P.attribute(reads))
        self.assertEqual(len(found), 1)
        self.assertIn("3 reads of solve_progress.txt within 20 s", found[0]["evidence"])
        two = P.find_foreground_poll(P.attribute(reads[:2]))
        self.assertEqual(two, [])


class TestProbeScript(unittest.TestCase):

    def test_real_positive_python_c_and_temp_probes(self):
        found = P.find_probe_script(P.attribute(neon_steps()))
        build1 = next(f for f in found if "build #1" in f["evidence"])
        # 20 with the commands whole (the cut trace hid one `python -c`
        # behind the 200th character of a compound command).
        self.assertTrue(build1["evidence"].startswith("20 probe(s)"))
        self.assertIn("12 python -c, 8 probe/tmp file(s)", build1["evidence"])
        self.assertIn(312, build1["steps"])                  # write Temp\opencode\probe_aedt_material.py

    def test_real_negative_subagent(self):
        steps = [s for s in neon_steps() if s["session_id"] == FALCON]
        self.assertEqual(P.find_probe_script(P.attribute(steps)), [])


class TestIdleGap(unittest.TestCase):

    def test_real_positive_all_user_waits(self):
        found = P.find_idle_gap(P.attribute(neon_steps()), [], machine_state())
        self.assertEqual(sorted(f["steps"][0] for f in found), [158, 356, 638, 661, 843])
        self.assertTrue(all("(user_wait)" in f["evidence"] for f in found))
        self.assertTrue(all(f["cost_tokens"] == 0 for f in found))
        longest = max(found, key=lambda f: f["cost_wall_ms"])
        self.assertEqual(longest["steps"], [158])
        self.assertEqual(longest["cost_wall_ms"], 4255211)

    def test_synthetic_beside_real_solver_wait_and_unexplained(self):
        steps = neon_steps()
        runs = P.watchdog_runs(machine_state()["solve_progress.txt"])
        inside = runs[0]["started_ms"] + 30_000
        a = _variant(step(steps, NEON, 520), ts=inside, latency_ms=6 * 60_000, seq=0)
        b = _variant(step(steps, NEON, 522), ts=inside + 6 * 60_000, seq=1)
        with_state = P.find_idle_gap(P.attribute([a, b]), [], machine_state())
        self.assertIn("(solver_wait)", with_state[0]["evidence"])
        without = P.find_idle_gap(P.attribute([a, b]), [], {})
        self.assertIn("(unexplained)", without[0]["evidence"])


class TestEscalation(unittest.TestCase):

    def test_real_positive_user_replies(self):
        found = P.find_escalation(P.attribute(neon_steps()))
        # 13 user turns: the first is the task, and the one at seq 518 was
        # typed while the 240 s Start-Sleep call (517) was still running —
        # not a reply after the agent stopped, now that a call's ts is its
        # emission. 11 remain.
        self.assertEqual(len(found), 11)
        steps = neon_steps()
        self.assertEqual(step(steps, NEON, 517)["kind"], "tool_use")
        self.assertEqual((step(steps, NEON, 518)["role"], step(steps, NEON, 518)["kind"]), ("user", "text"))
        first = min(found, key=lambda f: f["steps"][0])
        self.assertEqual(first["steps"], [158, 159])
        self.assertIn("waited 1 h 10 min", first["evidence"])

    def test_real_negative_claude(self):
        self.assertEqual(P.find_escalation(P.attribute(claude_steps())), [])

    def test_events_synthetic_beside_real(self):
        t = step(neon_steps(), NEON, 0)["ts"]
        evs = [_event("phase.declared", t, phase="build", detail="name=a"),
               _event("phase.refused", t + 1, phase="clarify",
                      verdict="FAIL: phase-boundary 'launch_desktop' refused in a 'clarify' session"),
               _event("budget.escalate", t + 2, phase="build", verdict="ESCALATE: session phase=build calls=60"),
               _event("gate.recorded", t + 3, phase="build", detail="gate=1 verdict=fixes note=ports"),
               _event("phase.declared", t + 4, phase="build", detail="name=b")]
        found = P.find_escalation([], evs)
        self.assertEqual([f["evidence"].split(":")[0] for f in found],
                         ["phase.refused", "budget.escalate", "gate fixes requested", "phase re-declared"])


class TestLateDeclaration(unittest.TestCase):

    def test_real_positive_solve_1b_submitted_nine_seconds_early(self):
        # The ledger calls this "the solve-phase declaration came one step
        # late". From the machine state alone: watchdog run 2 started at
        # 1787092156 (22:29:16Z); the trace's solve declaration that landed
        # was emitted at 22:29:24Z; session.json still read build in between.
        found = P.find_late_declaration(P.attribute(neon_steps()), [], machine_state())
        self.assertEqual(len(found), 1)
        f = found[0]
        self.assertEqual((f["phase"], f["stage"], f["source"]), ("build", "solve", "state"))
        self.assertIn("watchdog_started=1787092156", f["evidence"])
        self.assertIn("in phase build, 8 s before the solve declaration at 2026-08-18T22:29:24Z", f["evidence"])

    def test_real_negative_no_state(self):
        self.assertEqual(P.find_late_declaration(P.attribute(neon_steps()), [], {}), [])
        self.assertEqual(P.find_late_declaration(P.attribute(claude_steps()), [], {}), [])

    def test_events_synthetic_beside_real(self):
        t = 1_787_000_000_000
        evs = [_event("phase.declared", t, phase="build"),
               _event("solve.submitted", t + 1000, stage="solve"),
               _event("phase.declared", t + 2000, phase="solve"),
               _event("desktop.launch", t + 3000, stage="desktop", detail="port=1 pid=2")]
        found = P.find_late_declaration([], evs, {})
        self.assertEqual(len(found), 1)
        self.assertIn("solve.submitted", found[0]["evidence"])
        self.assertIn("phase build (owner: solve)", found[0]["evidence"])


class TestUndeclaredSession(unittest.TestCase):

    def test_real_positive_claude_session(self):
        found = P.find_undeclared_session(P.attribute(claude_steps()))
        self.assertEqual([f["session"] for f in found], [F0])
        self.assertEqual(found[0]["steps"], [])
        self.assertIn("40 steps, no phase declaration", found[0]["evidence"])

    def test_real_negative_neon_eagle_and_its_subagents(self):
        self.assertEqual(P.find_undeclared_session(P.attribute(neon_steps())), [])


class TestBackendError(unittest.TestCase):

    def test_real_positive_from_machine_state(self):
        found = [f for f in P.find_backend_error(P.attribute(neon_steps()), [], machine_state())
                 if f["source"] == "state"]
        self.assertEqual(len(found), 1)
        f = found[0]
        self.assertEqual((f["source"], f["phase"], f["stage"]), ("state", "solve", "readout"))
        self.assertEqual(f["evidence"],
                         "GrpcApiError GetVariables x3 quoted by readouts.txt x2, z_act.txt x1 "
                         "(readouts.txt: route=both-failed)")

    def test_real_positive_from_the_trace_output_heads(self):
        # The trace carries the first 2 KB of every tool output (ticket 06),
        # so the errors the run hit are read off it: five AEDT commands in
        # the main session, grouped by command and stage, plus the runcard
        # subagent's two reads of readouts.txt / z_act.txt, which quote the
        # same GetVariables / GetPropValue lines the state files hold.
        found = [f for f in P.find_backend_error(P.attribute(neon_steps()), [], {})
                 if f["source"] == "trace"]
        main = {(f["evidence"].split(" x")[0], f["stage"]): f for f in found if f["session"] == NEON}
        self.assertEqual(set(main), {("GrpcApiError GetPropertyValue", P.BETWEEN),
                                     ("GrpcApiError GetVariables", "readout"),
                                     ("GrpcApiError Subtract", "compile"),
                                     ("GrpcApiError GetDesignNames", P.BETWEEN),
                                     ("GrpcApiError GetPropValue", "readout")})
        self.assertEqual(main[("GrpcApiError Subtract", "compile")]["steps"], [743, 744, 750, 751])
        self.assertEqual(main[("GrpcApiError GetVariables", "readout")]["evidence"].split(" in ")[0],
                         "GrpcApiError GetVariables x4")
        self.assertEqual({f["session"] for f in found} - {NEON}, {FALCON})
        self.assertEqual(len(found), 7)

    def test_real_negative_without_heads(self):
        steps = [dict(s, output_head=None) for s in neon_steps()]
        self.assertEqual(P.find_backend_error(P.attribute(steps), [], {}), [])

    def test_synthetic_beside_real_output_head(self):
        steps = neon_steps()
        use, result = step(steps, NEON, 743), step(steps, NEON, 744)
        text = ("    raise GrpcApiError(f\"Failed to execute gRPC AEDT command: {funcName}\")\n"
                "ansys.aedt.core.internal.errors.GrpcApiError: Failed to execute gRPC AEDT command: Subtract")
        found = P.find_backend_error(P.attribute([use, _variant(result, output_head=text)]), [], {})
        self.assertEqual(len(found), 1)
        self.assertTrue(found[0]["evidence"].startswith("GrpcApiError Subtract x1 in compile"))
        self.assertEqual(found[0]["steps"], [743, 744])


class TestDesktopRecycle(unittest.TestCase):

    def test_real_positive_mid_run_kill_and_recorded_pin_moves(self):
        found = P.find_desktop_recycle(P.attribute(neon_steps()), [], machine_state())
        kills = [f for f in found if f["source"] == "trace"]
        self.assertEqual([f["steps"] for f in kills], [[761, 762]])
        self.assertIn("Stop-Process -Id 29756", kills[0]["evidence"])
        self.assertEqual(kills[0]["phase"], "build")
        pins = sorted(f["evidence"] for f in found if f["source"] == "state")
        self.assertEqual(len(pins), 2)
        self.assertIn("port 55583 -> port 64077/pid 29620", pins[0])
        self.assertIn("port 57850/pid 25840 -> port 64077/pid 29620", pins[1])
        self.assertTrue(all("aedt_port.txt now 64077" in p for p in pins))

    def test_real_negative(self):
        self.assertEqual(P.find_desktop_recycle(P.attribute(claude_steps()), [], {}), [])

    def test_events_synthetic_beside_real(self):
        t = 1_787_000_000_000
        evs = [_event("desktop.attach", t, phase="build", stage="desktop", detail="port=100 pid=1"),
               _event("desktop.attach", t + 1, phase="build", stage="desktop", detail="port=100 pid=1"),
               _event("desktop.launch", t + 2, phase="build", stage="desktop", detail="port=200 pid=2"),
               _event("desktop.recycle", t + 3, phase="solve", stage="desktop", detail="channel degraded")]
        found = P.find_desktop_recycle([], evs, {})
        self.assertEqual(len(found), 2)
        self.assertIn("port 100/pid 1 -> port 200/pid 2 within build", found[0]["evidence"])
        self.assertIn("channel degraded", found[1]["evidence"])


class TestDesignMisroute(unittest.TestCase):

    def test_real_positive_both_misroutes_confirmed(self):
        # Both DESIGN misroutes the ledger records by hand, confirmed from
        # the trace alone now that the commands are whole (ticket 05 saw
        # the second only as POSSIBLE behind the 200-char cut).
        found = P.find_design_misroute(P.attribute(neon_steps()))
        self.assertEqual([f for f in found if f["evidence"].startswith("POSSIBLE")], [])
        self.assertEqual(len(found), 2)
        first, second = sorted(found, key=lambda f: f["steps"][0])
        # #1 (build-2): fed compile 568, ws_common.py edit 596, fed compiles 599 and 603
        self.assertEqual(first["steps"], [568, 569, 596, 597, 599, 600, 603, 604])
        # #2 (build-3): fed compiles 743 / 750 / 757, edit 791, fed compiles 794 and 798
        self.assertEqual(second["steps"], [743, 744, 750, 751, 757, 758, 791, 792, 794, 795, 798, 799])
        for f in (first, second):
            self.assertEqual((f["phase"], f["stage"]), ("build", "compile"))
            self.assertIn("design.yaml", f["evidence"])
            self.assertIn("ws_common.py", f["evidence"])
            # Every compile here was piped through `Select-Object -Last N`,
            # so its output head is the PASS/FAIL tail, not the attach
            # banner: no Active Design names are quoted from real data.
            self.assertNotIn("Active Design", f["evidence"])
        steps = neon_steps()
        self.assertIn("Select-Object -Last", step(steps, NEON, 743)["command"])
        self.assertIn("PASS: compile_spec", step(steps, NEON, 569)["output_head"])

    def test_real_dry_run_is_not_a_compile(self):
        # Seq 401 ends in `--dry-run`, which the cut trace lost; whole, it
        # is a gate, not a compile, and no POSSIBLE finding is left.
        steps = neon_steps()
        self.assertIn(P.DRY_RUN, step(steps, NEON, 401)["command"])
        self.assertEqual(P.compile_calls(step(steps, NEON, 401)["command"]), [("design.yaml", True)])

    def test_real_negative(self):
        self.assertEqual(P.find_design_misroute(P.attribute(claude_steps())), [])

    def test_synthetic_beside_real_cut_commands_degrade_to_possible(self):
        # The same real steps with the build-3 compiles cut at 200 chars, as
        # the ticket-05 trace carried them (and the classifier's cap set to
        # that cut): the second misroute degrades to POSSIBLE and says why,
        # never to a confirmed finding on a guess. Dormant on today's trace,
        # whose cap no real command reaches.
        steps = neon_steps()
        cut = [_variant(s, command=s["command"][:200])
               if s["session_id"] == NEON and s["seq"] in (743, 744, 750, 751, 757, 758) else s
               for s in steps]
        self.assertTrue(all(len(s["command"]) == 200 for s in cut if s["seq"] in (743, 750) and s["session_id"] == NEON))
        cap = P.COMMAND_CHARS
        P.COMMAND_CHARS = 200
        try:
            found = P.find_design_misroute(P.attribute(cut))
        finally:
            P.COMMAND_CHARS = cap
        confirmed = sorted(f["steps"][0] for f in found if not f["evidence"].startswith("POSSIBLE"))
        possible = [f for f in found if f["evidence"].startswith("POSSIBLE")]
        self.assertEqual(confirmed, [568])
        self.assertEqual([f["steps"][0] for f in possible], [743])
        self.assertIn("200-char command cut", possible[0]["evidence"])

    def test_synthetic_beside_real_active_design_quoted(self):
        steps = neon_steps()
        picked = {568: "Active Design set to ElementsOnly", 599: "Active Design set to PatchArray"}
        restored = []
        for s in steps:
            if s["session_id"] == NEON and s["kind"] == "tool_result" and s["seq"] - 1 in picked:
                s = _variant(s, output_head=picked[s["seq"] - 1])
            restored.append(s)
        found = [f for f in P.find_design_misroute(P.attribute(restored)) if f["steps"][0] == 568]
        self.assertIn("(Active Design ElementsOnly -> PatchArray)", found[0]["evidence"])


class TestSolveAnomaly(unittest.TestCase):

    def test_real_positive_three_submissions(self):
        found = P.find_solve_anomaly([], [], machine_state())
        self.assertEqual(len(found), 1)
        self.assertTrue(found[0]["evidence"].startswith("3 solve submissions (watchdog runs"))
        self.assertEqual(found[0]["evidence"].count("complete"), 3)

    def test_real_negative_no_state(self):
        self.assertEqual(P.find_solve_anomaly([], [], {}), [])

    def test_stalled_line_from_the_real_formatter(self):
        # No stalled tick log exists on this box; the line comes from the
        # watchdog's own formatter, so its shape cannot drift from reality.
        cur = {"mesh": (2, 0), "adp": (1, 0), "fsu": (0, 0), "sd": (7, 0), "files": 30,
               "bytes_total": 100, "semaphores": 4, "profile_stages": [], "profile_status": None}
        line = poll_solve.format_progress(31, poll_solve.STATUS_STALLED, poll_solve.STAGE_ADAPTIVE, cur,
                                          "no growth for 30 unchanged ticks (window 30) in stage "
                                          "adaptive_meshing — not complete", 30, 620, 1787088970)
        real_line = machine_state()["solve_progress.txt"].splitlines()[0]
        self.assertTrue(P.TICK_RE.match(line) and P.TICK_RE.match(real_line))
        found = P.find_solve_anomaly([], [], {"solve_progress.txt": line})
        self.assertEqual(len(found), 1)
        self.assertIn("watchdog terminal: tick=31 status=stalled stage=adaptive_meshing", found[0]["evidence"])


class TestUnbanked(unittest.TestCase):

    def test_real_negative_every_complete_was_banked(self):
        self.assertEqual(P.find_unbanked([], [], machine_state()), [])

    def test_real_state_without_solved_txt(self):
        state = machine_state()
        del state["solved.txt"]
        found = P.find_unbanked([], [], state)
        self.assertEqual(len(found), 3)
        self.assertTrue(all("not banked: solved.txt absent" in f["evidence"] for f in found))

    def test_events_synthetic_beside_real(self):
        t = 1_787_000_000_000
        evs = [_event("solve.terminal", t, stage="solve", detail="tick=9 status=complete stage=done"),
               _event("solve.terminal", t + 1000, stage="solve", detail="tick=9 status=complete stage=done"),
               _event("solve.banked", t + 2000, stage="solve", verdict="PASS: confirm_solve banked")]
        self.assertEqual(P.find_unbanked([], evs, {}), [])
        self.assertEqual(len(P.find_unbanked([], evs[:1], {})), 1)


class TestCostAndSeverity(unittest.TestCase):

    def test_per_kind_sums_never_exceed_the_run(self):
        steps = neon_steps()
        total = P.run_tokens(steps)
        self.assertEqual(total, 2094310 + 76083 + 27888 + 1531 + 19966 + 1085)   # the three cards' billed
        findings = P.analyze(steps, [], [], machine_state())
        sums = Counter()
        for f in findings:
            sums[f["kind"]] += f["cost_tokens"]
        for kind, tokens in sums.items():
            self.assertLessEqual(tokens, total, kind)
        self.assertTrue(sums["long_reasoning"] > 0.2 * total)     # the run's biggest sink
        self.assertEqual(sums["idle_gap"], 0)

    def test_a_request_counts_once_per_kind(self):
        steps = neon_steps()
        first = P.attach_costs([P._finding("probe_script", [step(steps, NEON, 151)]),
                                P._finding("probe_script", [step(steps, NEON, 151), step(steps, NEON, 152)])],
                               steps)
        self.assertEqual(sorted(f["cost_tokens"] for f in first)[0], 0)
        self.assertGreater(max(f["cost_tokens"] for f in first), 0)

    def test_severity_rule(self):
        findings = P.analyze(neon_steps(), [], [], machine_state())
        kinds = by_kind(findings)
        top = kinds["long_reasoning"][0]
        self.assertEqual(top["severity"], "high")
        self.assertGreater(top["cost_tokens"], P.HIGH_TOKEN_SHARE * P.run_tokens(neon_steps()))
        self.assertEqual(kinds["whole_file_read"][0]["severity"], "low")
        gap = max(kinds["idle_gap"], key=lambda f: f["cost_wall_ms"])
        self.assertEqual(gap["severity"], "high")               # 71 min of wall, no tokens
        self.assertTrue(all(f["severity"] in P.SEVERITIES for f in findings))

    def test_findings_have_the_shape_and_are_sorted_by_cost(self):
        findings = P.analyze(neon_steps(), [], [], machine_state())
        keys = {"kind", "severity", "phase", "stage", "cost_tokens", "cost_wall_ms", "steps",
                "evidence", "fix_hint", "session", "source"}
        for f in findings:
            self.assertEqual(set(f), keys)
            self.assertIn(f["kind"], P.KINDS)
            self.assertEqual(f["evidence"].count("\n"), 0)
            self.assertEqual(f["fix_hint"], P.FIX_HINTS[f["kind"]])
        costs = [(f["cost_tokens"], f["cost_wall_ms"]) for f in findings]
        self.assertEqual(costs, sorted(costs, reverse=True))
        self.assertEqual(set(by_kind(findings)) - {"identical_error_twice", "undeclared_session", "unbanked"},
                         set(P.KINDS) - {"identical_error_twice", "undeclared_session", "unbanked"})


class TestStageTable(unittest.TestCase):

    def test_rows_add_up_to_the_run(self):
        steps = neon_steps()
        rows = P.stage_table(steps)
        self.assertEqual(sum(r["steps"] for r in rows), len(steps))
        self.assertEqual(sum(r["tokens"] for r in rows), P.run_tokens(steps))
        self.assertEqual(set(rows[0]), {"phase", "phase_index", "stage", "stage_source", "start",
                                        "wall_ms", "steps", "tokens", "script_runs", "fails", "retries"})
        self.assertEqual([r["start"] for r in rows], sorted(r["start"] for r in rows))

    def test_compile_rows_match_the_rebuild_findings(self):
        steps = neon_steps()
        rows = {(r["phase"], r["phase_index"], r["stage"]): r for r in P.stage_table(steps)}
        chains = {f["evidence"].split(" in build #")[1][0]: int(f["evidence"].split(" compiles")[0])
                  for f in P.find_rebuild_chain(P.attribute(steps))}
        for index, compiles in chains.items():
            row = rows[("build", int(index), "compile")]
            self.assertEqual(row["steps"], 2 * compiles)       # a call is two steps
            self.assertEqual(row["script_runs"], compiles)
        snapshot = rows[("build", 1, "snapshot")]
        self.assertEqual(snapshot["retries"], 1)                # capture_state.py -Last 2, twice

    def test_the_first_phase_is_the_heaviest_wall(self):
        rows = P.stage_table(neon_steps())
        clarify = [r for r in rows if r["phase"] == "clarify" and r["stage"] == P.BETWEEN][0]
        self.assertGreater(clarify["wall_ms"], 60 * 60_000)     # the 71-min gate wait sits in it


if __name__ == "__main__":
    result = unittest.main(exit=False, verbosity=0).result
    failed = len(result.failures) + len(result.errors)
    print(f"{'PASS' if not failed else 'FAIL'}: painpoints "
          f"tests={result.testsRun} failed={failed}")
    raise SystemExit(1 if failed else 0)
