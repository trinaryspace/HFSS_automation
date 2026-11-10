"""Probe: can the pinned desktop save the project? Read-mostly diagnostic.

Used after `analyze` failed on its implicit save. Reports the design list,
whether `save_project()` succeeds, and the exception text if it does not.

Usage (workspace root):  python src/17_save_probe.py
Prints one Verification line:  PASS: save_probe saved=True ... | FAIL: ...
"""

import ws_common


def main():
    hfss = ws_common.attach()
    print("design:", hfss.design_name, "| designs:", hfss.design_list, flush=True)
    try:
        ok = hfss.save_project()
    except Exception as exc:                 # noqa: BLE001 - this IS the probe
        print("FAIL: save_probe saved=False %s: %s"
              % (type(exc).__name__, str(exc)[:300]), flush=True)
        return
    print("%s: save_probe saved=%s" % ("PASS" if ok else "FAIL", bool(ok)), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    ws_common.exit_keep_alive()
