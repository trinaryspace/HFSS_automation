"""The template runners' events, driven against the real fixture corpus.

Run logging, ticket 03. `run_events.py` is the workspace's hook into
`hfss_spec/events.py`; every runner that prints a `PASS:` / `FAIL:` line,
attaches, submits, sees the watchdog's terminal line, banks or tears down
appends that fact as one event. These tests drive the ACTUAL runner code
paths — not the emit calls in isolation — at the same no-AEDT seams
`test_template_runners` uses (AEDT entry points stood in by fakes, ws_common's
STATE / PROJECT redirected to a throwaway tree, `os._exit` turned into
`SystemExit`), and assert the event SEQUENCE a session leaves behind:

    solve session:  desktop.attach -> solve.submitted -> solve.terminal
                    -> solve.banked -> teardown
    build session:  snapshot.captured -> sync.verify

The solve evidence is the captured `pilot-normal` tree (`real_fixtures`),
materialized with directories where AEDT made directories, and the watchdog
is run to its terminal line for real: the real profile slice lands on the
tree mid-run, exactly as the solver writes it, so `solve.terminal`'s detail
is the line the watchdog actually printed. The sync verifier's snapshot is a
real captured model (`knowledge/cases/_snapshots/`). Nothing here is written
from memory — see `docs/agents/fixture-fidelity.md`.

Run:  python src/test_run_events.py
"""

import contextlib
import importlib.util
import io
import json
import os
import shutil
import sys
import tempfile
import unittest
from unittest import mock

SRC = os.path.dirname(os.path.abspath(__file__))
if SRC not in sys.path:
    sys.path.insert(0, SRC)

import real_fixtures  # noqa: E402
import run_events     # noqa: E402
import ws_common      # noqa: E402  (imports pyAEDT classes; never launches)

# The profile the pilot's solve actually completed on (real_fixtures meta).
PILOT_CASE = "pilot-normal"
PILOT_PROFILE = "DV3019_S1911_V2586.profile"


def load(name):
    spec = importlib.util.spec_from_file_location("te_" + name, os.path.join(SRC, name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def repo_path(*parts):
    root = run_events.repo_root()
    assert root, "the repo root must be findable above the template src"
    return os.path.join(root, *parts)


def real_snapshot():
    """A real captured model snapshot, byte-for-byte from the corpus."""
    with open(repo_path("knowledge", "cases", "_snapshots", "horn-10ghz.json"),
              encoding="utf-8") as handle:
        return json.load(handle)


@contextlib.contextmanager
def quiet():
    with contextlib.redirect_stdout(io.StringIO()) as out:
        yield out


# --- the shim -------------------------------------------------------------------


class TestShim(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.state = os.path.join(self.tmp, "results", "state")
        os.makedirs(self.state)
        self.addCleanup(run_events.reset)

    def test_finds_the_checkout_above_the_workspace(self):
        root = run_events.repo_root()
        self.assertTrue(os.path.isfile(os.path.join(root, "hfss_spec", "events.py")))
        self.assertIsNotNone(run_events.events_module())

    def test_finds_it_from_a_sync_verify_copy_too(self):
        # results/state/verify/<stamp>/copy/src is where 12_verify_sync puts a copy
        nested = repo_path("workspaces", "x", "results", "state", "verify", "s", "copy", "src")
        self.assertEqual(run_events.repo_root(nested), run_events.repo_root())

    def test_default_state_dir_is_this_workspaces_results_state(self):
        self.assertEqual(run_events.STATE,
                         os.path.join(run_events.WORKSPACE, "results", "state"))

    def test_emit_lands_and_reads_back(self):
        self.assertTrue(run_events.emit("x.y", stage="s", verdict="PASS: s", state_dir=self.state))
        self.assertEqual(run_events.names(self.state), ["x.y"])
        self.assertEqual(run_events.read(self.state)[0]["verdict"], "PASS: s")

    def test_no_state_dir_is_a_no_op(self):
        missing = os.path.join(self.tmp, "nope")
        self.assertFalse(run_events.emit("x", state_dir=missing))
        self.assertFalse(os.path.exists(missing))

    def test_no_checkout_above_is_a_silent_no_op(self):
        run_events.reset()
        with mock.patch.object(run_events, "repo_root", return_value=None):
            self.assertFalse(run_events.emit("x", state_dir=self.state))
            self.assertEqual(run_events.read(self.state), [])
        run_events.reset()

    def test_a_broken_logger_never_raises(self):
        with mock.patch.object(run_events, "events_module", side_effect=RuntimeError("no")):
            self.assertFalse(run_events.emit("x", state_dir=self.state))
            self.assertEqual(run_events.names(self.state), [])


# --- a solve session, end to end --------------------------------------------------


class FakeDesktopClass:
    port = 0
    aedt_process_id = 0


class _NoAedt:
    """Stands in for `ansys.aedt.core` in sys.modules: any construction is a test failure."""

    def __getattr__(self, name):
        def refuse(*args, **kwargs):
            raise AssertionError("tier 0 must never reach ansys.aedt.core.%s" % name)
        return refuse


class SolveSession(unittest.TestCase):
    """Shared fakes: the AEDT entry points, ws_common redirected, real tree."""

    @classmethod
    def setUpClass(cls):
        cls.solve = load("08_solve")
        cls.poll = load("poll_solve")
        cls.confirm = load("confirm_solve")

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.ws = os.path.join(self.tmp, "ws")
        self.state = os.path.join(self.ws, "results", "state")
        os.makedirs(self.state)
        self.project = os.path.join(self.ws, "fixture.aedt")
        self._orig = (ws_common.STATE, ws_common.PROJECT, ws_common.Hfss, ws_common.Desktop)
        ws_common.STATE = self.state
        ws_common.PROJECT = self.project
        self.addCleanup(self._restore)
        self.released = []
        suite = self

        class AttachedHfss:
            def __init__(self):
                self.desktop_class = FakeDesktopClass()

            def analyze(self, **kw):
                return True

            def cleanup_solution(self, **kw):
                raise AssertionError("cleanup must be skipped with no stale results")

        class LaunchedHfss(AttachedHfss):
            def __init__(self):
                fd = FakeDesktopClass()
                fd.port = 61234
                fd.aedt_process_id = 4242
                self.desktop_class = fd

        def fake_hfss(**kw):
            return LaunchedHfss() if kw.get("new_desktop") else AttachedHfss()

        def fake_desktop(**kw):
            d = FakeDesktopClass()
            d.release_desktop = lambda **rk: suite.released.append(rk)
            return d

        ws_common.Hfss = fake_hfss
        ws_common.Desktop = fake_desktop
        # No AEDT, ever: any code path that re-imports the entry points
        # instead of using ws_common's (patched) module-level names fails
        # loudly here instead of launching a licensed desktop for 13 s —
        # which is exactly what teardown's local re-import once did.
        forbidden = mock.patch.dict(sys.modules, {"ansys.aedt.core": _NoAedt()})
        forbidden.start()
        self.addCleanup(forbidden.stop)

    def _restore(self):
        ws_common.STATE, ws_common.PROJECT, ws_common.Hfss, ws_common.Desktop = self._orig

    def pin(self, port=60123, pid=9999):
        ws_common.write_state("aedt_port", str(port))
        ws_common.write_state("aedt_process_id", str(pid))

    def events(self):
        return run_events.read(self.state)

    def names(self):
        return run_events.names(self.state)

    # -- the steps, each the real runner ----------------------------------

    def attach(self):
        with quiet():
            return ws_common.attach(probe=lambda port: True)

    def submit(self, argv=(), probe=None, now=1755543600.25):
        class FakeProc:
            pid = 4242

        # The REAL attach, with the bounded connect answered "alive" for the
        # pinned port (a socket probe against a fake pin would read stale).
        def attach(**kw):
            return ws_common.attach(probe=lambda port: True, **kw)

        with quiet() as out:
            code = self.solve.main(list(argv), attach=attach,
                                   probe=probe or (lambda: (None, 0)),
                                   popen=lambda *a, **k: FakeProc(), now=now)
        return code, out.getvalue()

    def materialize(self, with_profiles=False):
        root = self.project + "results"
        real_fixtures.materialize(PILOT_CASE, root, include_profiles=with_profiles)
        return root

    def profile_target(self, root):
        for dirpath, _dirs, files in os.walk(root):
            if PILOT_PROFILE in files:
                return os.path.join(dirpath, PILOT_PROFILE)
        raise AssertionError("the pilot profile is not in the materialized tree")

    def land_real_profile(self, root):
        """The solver's completion write: the real profile slice, newer than the tree."""
        target = self.profile_target(root)
        with open(real_fixtures.profile_path(PILOT_CASE, PILOT_PROFILE), encoding="utf-8") as h:
            body = h.read()
        with open(target, "w", encoding="utf-8", newline="\n") as h:
            h.write(body)
        newest = max(os.path.getmtime(os.path.join(d, f))
                     for d, _s, fs in os.walk(root) for f in fs)
        os.utime(target, (newest + 5, newest + 5))
        return target

    def watch(self, root, cfg, land_profile_after_tick=None):
        """Run the watchdog loop to its terminal line; returns (rc, progress lines)."""
        ticks = {"n": 0}

        def sleep(_seconds):
            ticks["n"] += 1
            if land_profile_after_tick is not None and ticks["n"] == land_profile_after_tick:
                self.land_real_profile(root)

        with quiet():
            rc = self.poll.run(self.project, self.state, cfg=cfg, sleep=sleep,
                               process_alive=lambda pid: True)
        with open(os.path.join(self.state, "solve_progress.txt")) as handle:
            return rc, handle.read().splitlines()

    def bank(self):
        rc, lines = self.confirm.confirm(self.project, state_dir=self.state, now=1234567890)
        return rc, lines

    def teardown(self):
        with mock.patch.object(ws_common, "_reap_pinned_process", lambda pid, timeout=None: True), \
                mock.patch.object(ws_common.os, "_exit",
                                  side_effect=lambda code: (_ for _ in ()).throw(SystemExit(code))), \
                quiet():
            try:
                ws_common.teardown()
            except SystemExit as exc:
                return exc.code
        raise AssertionError("teardown must end in os._exit")


class TestSolveSessionSequence(SolveSession):
    def test_the_whole_session_in_order(self):
        """attach -> submit -> terminal -> bank -> teardown, from the real runners.

        The attach is 08_solve's own (it attaches to the pinned desktop before
        submitting), so the session's first event is the launcher's attach.
        """
        self.pin(60123, 9999)
        code, out = self.submit()
        self.assertEqual(code, 0, out)
        root = self.materialize()
        rc, progress = self.watch(root, {"settle_ticks": 2, "start_ticks": 50,
                                         "stall_ticks": 50}, land_profile_after_tick=1)
        self.assertEqual(rc, 0, progress[-1])
        rc, lines = self.bank()
        self.assertEqual(rc, 0, lines)
        self.assertEqual(self.teardown(), 0)

        records = self.events()
        self.assertEqual([r["event"] for r in records],
                         ["desktop.attach", "solve.submitted", "solve.terminal",
                          "solve.banked", "teardown"])
        attach, submitted, terminal, banked, teardown = records

        self.assertEqual(attach["stage"], "desktop")
        self.assertEqual(attach["detail"], "port=60123 pid=9999")

        self.assertEqual(submitted["stage"], "solve")
        self.assertTrue(submitted["verdict"].startswith(
            "PASS: solve submitted blocking=False setup=Setup1 submitted_at=1755543600.25"))
        self.assertIn(submitted["verdict"], out)             # the printed line, verbatim
        self.assertIn("watchdog_pid=4242", submitted["detail"])

        # the watchdog's terminal line, verbatim, and nothing from the ticks before it
        self.assertEqual(terminal["detail"], progress[-1])
        self.assertIn("status=complete", terminal["detail"])
        self.assertIn("profile_status=normal_completion", terminal["detail"])
        self.assertIn("evidence=profile status: Normal Completion", terminal["detail"])
        self.assertGreater(len(progress), 1)
        self.assertIsNone(terminal["verdict"])
        self.assertIsInstance(terminal["duration_ms"], int)

        self.assertEqual(banked["verdict"], lines[0])
        self.assertTrue(banked["verdict"].startswith(
            "PASS: confirm_solve banked status=Normal Completion sweep_points="))
        self.assertIn("profile=" + PILOT_PROFILE, banked["detail"])

        self.assertEqual(teardown["stage"], "teardown")
        self.assertIn("verdict=banked", teardown["detail"])
        self.assertIn("close_projects=False", teardown["detail"])
        self.assertIn("port=60123 pid=9999", teardown["detail"])
        self.assertEqual(self.released, [{"close_projects": False, "close_on_exit": True}])

        for record in records:                             # no run.json: null, never a guess
            self.assertIsNone(record["run_id"])
            self.assertIsNone(record["phase"])

    def test_a_declared_solve_session_stamps_run_id_and_phase(self):
        sys.path.insert(0, run_events.repo_root())
        from hfss_spec import session as S
        with quiet():
            S.start("solve", state_dir=self.state, host="opencode", host_session_id="neon-eagle")
        run_id = S.run_info(self.state)["run_id"]
        self.pin()
        self.submit()
        records = self.events()
        self.assertEqual([r["event"] for r in records],
                         ["phase.declared", "desktop.attach", "solve.submitted"])
        for record in records:
            self.assertEqual(record["run_id"], run_id)
            self.assertEqual(record["phase"], "solve")

    def test_a_refused_submission_is_its_own_event_with_the_fail_line(self):
        code, out = self.submit(probe=lambda: (42, 1))
        self.assertEqual(code, 2)
        records = self.events()
        self.assertEqual([r["event"] for r in records], ["solve.refused"])
        self.assertTrue(records[0]["verdict"].startswith("FAIL: solve not submitted"))
        self.assertIn(records[0]["verdict"], out)
        self.assertIn("live_solvers=1", records[0]["detail"])

    def test_a_stalled_watchdog_and_an_unbanked_confirm(self):
        root = self.materialize()                          # no completion ever lands
        rc, progress = self.watch(root, {"stall_ticks": 2, "start_ticks": 50, "settle_ticks": 9})
        self.assertEqual(rc, 2)
        rc, lines = self.bank()
        self.assertEqual(rc, 2)
        records = self.events()
        self.assertEqual([r["event"] for r in records], ["solve.terminal", "solve.unbanked"])
        self.assertEqual(records[0]["detail"], progress[-1])
        self.assertIn("status=stalled", records[0]["detail"])
        self.assertTrue(records[1]["detail"].startswith("confirm_solve aborted:"))
        self.assertEqual(records[1]["detail"], lines[-1])

    def test_a_launch_and_a_recycle_carry_the_new_port_and_pid(self):
        self.pin(60123, 9999)
        with quiet():
            ws_common.attach(launch=True)
        with mock.patch.object(ws_common, "_reap_pinned_process", lambda pid, timeout=None: True), \
                quiet():
            ws_common.recycle_desktop()
        records = self.events()
        self.assertEqual([r["event"] for r in records],
                         ["desktop.launch", "desktop.launch", "desktop.recycle"])
        self.assertEqual(records[0]["detail"], "port=61234 pid=4242")
        self.assertTrue(records[2]["detail"].startswith("recycled desktop:"))
        self.assertIn("pid 4242", records[2]["detail"])

    def test_a_stale_pin_is_a_launch_that_says_so(self):
        self.pin(60123, 9999)
        with quiet():
            ws_common.attach(probe=lambda port: False)
        records = self.events()
        self.assertEqual(records[0]["event"], "desktop.launch")
        self.assertEqual(records[0]["detail"], "port=61234 pid=4242 (stale pin re-pinned)")

    def test_teardown_without_a_pin_and_teardown_refused(self):
        self.assertEqual(self.teardown(), 0)               # no pin: aborted, touched nothing
        self.pin(60123, 9999)
        root = self.materialize(with_profiles=True)        # terminal evidence, unbanked
        self.land_real_profile(root)
        self.assertEqual(self.teardown(), 2)
        records = self.events()
        self.assertEqual([r["event"] for r in records], ["teardown", "teardown"])
        self.assertTrue(records[0]["detail"].startswith("aborted: no pinned aedt_port"))
        self.assertTrue(records[1]["detail"].startswith("refused: solve evidence on disk"))
        self.assertEqual(self.released, [])


# --- a build session: snapshot and sync -----------------------------------------


class TestBuildSessionSequence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.capture = load("capture_state")
        cls.verify = load("12_verify_sync")
        # verify_spec_replay resolves its verifier from ws_common.WORKSPACE at
        # load time, so it is loaded before any redirect.
        cls.replay = load("verify_spec_replay")
        cls.reader = load("read_results")

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.ws = os.path.join(self.tmp, "ws")
        self.state = os.path.join(self.ws, "results", "state")
        os.makedirs(self.state)
        os.makedirs(os.path.join(self.ws, "src"))
        self._orig = (ws_common.STATE, ws_common.WORKSPACE, ws_common.attach)
        ws_common.STATE = self.state
        ws_common.WORKSPACE = self.ws
        self.addCleanup(self._restore)

    def _restore(self):
        ws_common.STATE, ws_common.WORKSPACE, ws_common.attach = self._orig

    def events(self):
        return run_events.read(self.state)

    def fake_model(self):
        class Modeler:
            object_names = ["Sub", "Patch"]
            model_units = "mm"

            def get_object_bounding_box(self, name):
                return [0.0, 0.0, 0.0, 80.0, 90.0, 1.6]

            def __getitem__(self, name):
                return type("O", (), {"material_name": "pec"})()

        return type("M", (), {"modeler": Modeler(), "boundaries": [], "excitations": [],
                              "setups": [], "existing_analysis_sweeps": [],
                              "variables": {"w": "2mm"}})()

    def test_capture_state_records_its_snapshot_line(self):
        model = self.fake_model()
        ws_common.attach = lambda launch=False: model
        with quiet() as out:
            self.capture.main()
        records = self.events()
        self.assertEqual([r["event"] for r in records], ["snapshot.captured"])
        self.assertEqual(records[0]["stage"], "snapshot")
        self.assertTrue(records[0]["verdict"].startswith("PASS: capture_state "))
        self.assertIn("objects=2", records[0]["verdict"])
        self.assertIn(records[0]["verdict"], out.getvalue())
        self.assertTrue(os.path.isfile(os.path.join(self.state, "model_snapshot.json")))

    def test_verify_sync_pass_against_a_real_snapshot(self):
        """The replay reproduces the live model: the runner's PASS line is the event."""
        snapshot = real_snapshot()
        with open(os.path.join(self.state, "model_snapshot.json"), "w") as handle:
            json.dump(snapshot, handle)
        with open(os.path.join(self.ws, "src", "01_a.py"), "w") as handle:
            handle.write("print('PASS: a')\n")

        def fake_run(python, args, cwd):
            script = args[0]
            if os.path.basename(script) == "capture_state.py":
                copy_state = os.path.join(os.path.dirname(os.path.dirname(script)),
                                          "results", "state")
                os.makedirs(copy_state, exist_ok=True)
                with open(os.path.join(copy_state, "model_snapshot.json"), "w") as handle:
                    json.dump(snapshot, handle)
                return 0, "PASS: capture_state", ""
            return 0, "PASS: a", ""

        with mock.patch.object(self.verify, "_run_py", fake_run), \
                mock.patch.object(self.verify, "_teardown_copy", lambda python, copy: None), \
                quiet():
            rc = self.verify.main(["12_verify_sync.py", self.ws])
        self.assertEqual(rc, 0)
        records = self.events()
        self.assertEqual([r["event"] for r in records], ["sync.verify"])
        self.assertEqual(records[0]["verdict"], "PASS: sync replay matches snapshot")
        self.assertEqual(records[0]["stage"], "sync")

    def test_verify_sync_fail_lines_are_events_too(self):
        with quiet():
            rc = self.verify.main(["12_verify_sync.py", self.ws])   # no live snapshot
        self.assertEqual(rc, 1)
        records = self.events()
        self.assertEqual([r["event"] for r in records], ["sync.verify"])
        self.assertTrue(records[0]["verdict"].startswith(
            "FAIL: sync mismatch — no live model_snapshot.json"))

    def test_spec_replay_verdicts_are_events(self):
        with quiet():
            rc = self.replay.main([])                            # no live snapshot
        self.assertEqual(rc, 1)
        with open(os.path.join(self.state, "model_snapshot.json"), "w") as handle:
            json.dump(real_snapshot(), handle)
        with quiet():
            rc = self.replay.main([])                            # snapshot, no design*.yaml
        self.assertEqual(rc, 1)
        records = self.events()
        self.assertEqual([r["event"] for r in records], ["sync.verify", "sync.verify"])
        self.assertTrue(records[0]["verdict"].startswith("FAIL: sync mismatch — no live"))
        self.assertTrue(records[1]["verdict"].startswith("FAIL: no design*.yaml to replay"))

    # -- readout --------------------------------------------------------------

    def test_readout_attempt_carries_route_and_error_class(self):
        class GrpcApiError(Exception):
            pass

        class Post:
            def get_solution_data(self, **kw):
                raise GrpcApiError("channel degraded")

        failing = type("H", (), {"existing_analysis_sweeps": ["Setup1 : Sweep1"],
                                 "post": Post()})()
        session = self.reader.ReadoutSession(failing, state_dir=self.state)
        readout = session.read("dB(S(1,1))")
        self.assertEqual(readout.route, self.reader.ROUTE_UNTESTED)
        records = self.events()
        self.assertEqual([r["event"] for r in records], ["readout.attempt"])
        self.assertEqual(records[0]["stage"], "readout")
        self.assertIn("expression=dB(S(1,1))", records[0]["detail"])
        self.assertIn("route=untested", records[0]["detail"])
        self.assertIn("error_class=GrpcApiError", records[0]["detail"])
        self.assertIn("points=0", records[0]["detail"])

    def test_readout_success_names_the_route_and_no_error(self):
        class Solution:
            primary_sweep_values = [1.0, 2.0]

            def get_expression_data(self, expression, formula=None):
                return [-3.0, -7.0]

        class Post:
            def get_solution_data(self, **kw):
                return Solution()

        good = type("H", (), {"existing_analysis_sweeps": ["Setup1 : Sweep1"], "post": Post()})()
        readout = self.reader.ReadoutSession(good, state_dir=self.state).read("dB(S(1,1))")
        self.assertEqual(readout.route, self.reader.ROUTE_LIVE)
        detail = self.events()[0]["detail"]
        self.assertIn("route=live-channel", detail)
        self.assertIn("error_class=-", detail)
        self.assertIn("points=2", detail)


if __name__ == "__main__":
    result = unittest.main(exit=False, verbosity=0).result
    failed = len(result.failures) + len(result.errors)
    print(f"{'PASS' if not failed else 'FAIL'}: run_events tests={result.testsRun} failed={failed}")
    raise SystemExit(1 if failed else 0)
