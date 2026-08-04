"""Print the opencode run card for a session, from the session database.

Part of the hfss-agent-perf-refactor measurement harness (ticket 01): every
optimization is judged against the numbers this card emits, so the card is
derived from the reference SQL in
docs/hfss-agent-performance-analysis.md section 10.

The database is opened read-only (WAL-safe while opencode is running) with a
generous busy timeout. Stdlib only, Python 3.10 compatible.

Usage:
    python scripts/run_card.py --slug <slug> [--db PATH]
    python scripts/run_card.py --latest [--db PATH]
    python scripts/run_card.py --slug <slug> --summary <path>/summary.md

The database path resolves in order: --db flag, OPENCODE_DB env var, default
~/.local/share/opencode/opencode.db.
"""

import argparse
import os
import re
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_DB = Path.home() / ".local" / "share" / "opencode" / "opencode.db"
ENV_DB = "OPENCODE_DB"
PROJECT_MARKER = "HFSS_automation"

REFERENCE_SQL = """
SELECT s.slug, s.time_created, s.time_updated,
       s.tokens_input, s.tokens_output, s.tokens_reasoning,
       s.tokens_cache_read, s.tokens_cache_write,
       s.tokens_input + s.tokens_output AS billed,
       (SELECT count(*) FROM part p WHERE p.session_id = s.id) AS parts,
       (SELECT sum(length(data)) FROM part p2 WHERE p2.session_id = s.id) AS storesize
FROM session s
"""


def connect(db_path):
    """Open the opencode DB read-only; tolerant of a live-WAL-open DB."""
    uri = "file:" + str(Path(db_path).resolve()).replace("\\", "/") + "?mode=ro"
    con = sqlite3.connect(uri, uri=True, timeout=30.0)
    con.row_factory = sqlite3.Row
    return con


def load_card(con, slug=None, latest=False):
    """Return the card dict for one session, or None if not found.

    Sessions are constrained to the HFSS project (worktree contains
    PROJECT_MARKER), mirroring the reference SQL of analysis section 10;
    slug ties (duplicate slugs across projects) are broken by recency.
    """
    where = ["s.project_id = (SELECT id FROM project WHERE worktree LIKE '%' || ? || '%')"]
    args = [PROJECT_MARKER]
    if slug is not None:
        where.append("s.slug = ?")
        args.append(slug)
        sql_tail = " ORDER BY s.time_created DESC LIMIT 1"
    else:
        sql_tail = " ORDER BY s.time_created DESC LIMIT 1"
    sql = REFERENCE_SQL + " WHERE " + " AND ".join(where) + sql_tail
    row = con.execute(sql, args).fetchone()
    if row is None:
        return None
    card = dict(row)
    card["duration_ms"] = card["time_updated"] - card["time_created"]
    return card


def _iso(epoch_ms):
    if epoch_ms is None:
        return "n/a"
    return datetime.fromtimestamp(epoch_ms / 1000.0, timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )


def _duration(duration_ms):
    if duration_ms is None or duration_ms < 0:
        return "n/a"
    total_s = int(duration_ms / 1000)
    h, rem = divmod(total_s, 3600)
    m, s = divmod(rem, 60)
    return f"{h} h {m} min {s} s"


def _metric_pairs(card):
    """The card's metrics as (label, value) pairs; one per card line."""
    return [
        ("slug", card["slug"]),
        ("created", _iso(card["time_created"])),
        ("updated", _iso(card["time_updated"])),
        ("duration", _duration(card["duration_ms"])),
        ("tokens_input", card["tokens_input"]),
        ("tokens_output", card["tokens_output"]),
        ("tokens_reasoning", card["tokens_reasoning"]),
        ("tokens_cache_read", card["tokens_cache_read"]),
        ("tokens_cache_write", card["tokens_cache_write"]),
        ("billed", card["billed"]),
        ("parts", card["parts"]),
        ("store_bytes", card["storesize"]),
    ]


def summary_section(card):
    """The `## Run card` markdown block, one `- key: value` line per metric."""
    body = "\n".join(f"- {k}: {v}" for k, v in _metric_pairs(card))
    return "## Run card\n\n" + body + "\n"


def upsert_summary(path, card):
    """Insert the Run card section into summary.md; replace any old one.

    The section is the block under a `## Run card` heading (a whole line)
    up to the next `## ` heading (or end of file). Idempotent: writing
    twice yields the same file.
    """
    text = path.read_text(encoding="utf-8")
    match = re.search(r"(?m)^## Run card\s*$", text)
    start = match.start() if match else None
    if start is not None:
        end = len(text)
        nxt = text.find("\n## ", start + len("## Run card"))
        if nxt != -1:
            end = nxt
        head = text[:start].rstrip()
        head = head + "\n\n" if head else ""
        tail = text[end:]
    else:
        head = text.rstrip()
        head = head + "\n\n" if head else ""
        tail = ""
    path.write_text(head + summary_section(card) + tail, encoding="utf-8")


def render_card(card):
    """Format the card as `key: value` lines, one per metric."""
    return "\n".join(f"{k}: {v}" for k, v in _metric_pairs(card))


def main(argv=None):
    parser = argparse.ArgumentParser(description="Print the opencode run card.")
    parser.add_argument("--db", help="path to opencode.db (default: %r)" % DEFAULT_DB)
    parser.add_argument("--slug", help="session slug to card")
    parser.add_argument("--latest", action="store_true",
                        help="card the latest HFSS-project session")
    parser.add_argument("--summary", help="append/replace the Run card section in this summary.md")
    args = parser.parse_args(argv)

    if args.latest == (args.slug is not None):
        parser.error("give exactly one of --slug <slug> or --latest")
    db_path = args.db or os.environ.get(ENV_DB) or DEFAULT_DB
    if not Path(db_path).is_file():
        print(f"error: database not found: {db_path}", file=sys.stderr)
        return 1
    try:
        con = connect(db_path)
    except sqlite3.Error as exc:
        print(f"error: cannot open database {db_path}: {exc}", file=sys.stderr)
        return 1
    try:
        card = load_card(con, slug=args.slug or None, latest=args.latest)
    except sqlite3.Error as exc:
        print(f"error: query failed: {exc}", file=sys.stderr)
        return 1
    finally:
        con.close()
    if card is None:
        subject = f"whose slug is '{args.slug}' " if args.slug else ""
        print(f"error: no session {subject}in the HFSS_automation project",
              file=sys.stderr)
        return 1
    print(render_card(card))
    if args.summary:
        summary_path = Path(args.summary)
        try:
            upsert_summary(summary_path, card)
        except (OSError, ValueError, UnicodeError) as exc:
            print(f"error: cannot write '{args.summary}': {exc}", file=sys.stderr)
            return 1
        print(f"run card written to {args.summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
