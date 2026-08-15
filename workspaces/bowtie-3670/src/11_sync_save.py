"""Sync housekeeping: save the live (user-corrected) project to disk.

Read-only otherwise — the delivered model is the UI state; this persists it.
"""

import sys

sys.path.insert(0, "src")
from ws_common import attach, exit_keep_alive

hfss = attach(launch=False)
hfss.save_project()
print("live project saved to disk", flush=True)
exit_keep_alive()
