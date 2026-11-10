"""Print every boundary's properties as the live model holds them. Read-only.

Usage (workspace root):  python src/16_boundary_card.py
Prints one Verification line:  PASS: boundary_card boundaries=<n>
"""

import ws_common


def main():
    hfss = ws_common.attach()
    count = 0
    for boundary in hfss.boundaries:
        count += 1
        print("%s [%s]" % (boundary.name, boundary.type), flush=True)
        for key, value in dict(boundary.props).items():
            print("    %s = %s" % (key, value), flush=True)
    print("PASS: boundary_card boundaries=%d" % count, flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - verification-line contract
        print("STAGE_FAILED", type(e).__name__, str(e)[:600], flush=True)
    ws_common.exit_keep_alive()
