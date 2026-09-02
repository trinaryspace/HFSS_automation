# Reference papers

Drop user-provided PDFs (academic papers, book chapters) here so they can
inform a conversation. They are NOT playbook entries — nothing here amends
the playbook automatically.

## Layout — one global folder, one folder per project

- `Global/` — general guidance that applies to every run: HFSS
  fundamentals, port and excitation practice, geometry tips and tricks,
  meshing and solve-setup guidelines. The agent reads these **every time**,
  whatever the structure being built.
- `<Project>/` — one folder per structure family (`Bowtie Patch/`,
  `U-slot/`, …) holding the papers that describe that design: its
  geometry, dimensions, feed, substrate, and measured results. The agent
  reads **only the folder that matches** the requested structure; the
  other project folders stay unread, so one design's numbers never leak
  into another's Recipe.

Choosing the project folder: match the folder name to the structure named
in the request (a U-slot patch reads `U-slot/`); a Re-entry matches the
family of the existing design. If more than one folder could apply, or
none does, say so in the Clarification block — never pick one silently,
and never read all of them "to be safe". No matching folder means the run
proceeds on `Global/` plus the playbook alone.

Adding a paper: general guidance goes in `Global/`; a design paper goes in
its `<Project>/` folder, created if it does not exist yet. Loose PDFs at
this level are not read — file them.

How the agent treats them (see `skill/hfss-agent/SKILL.md`, Read first #6):

1. Run the global `analyze-papers` skill once on `Global/` and once on the
   matching project folder — it takes one folder per invocation, and its
   cache makes the repeated `Global/` run instant and free. It invokes the
   literature-analyzer CLI and writes agent notes to
   `<analyzer repo>/agent_out`. The skill lives in `~/.agents/skills/`
   (opencode's root); `python scripts/install_skill.py` links it into
   `~/.claude/skills/` so Claude Code sees it too. A host that cannot see
   it reports that and asks for the installer — it does not improvise.
2. Read the resulting agent notes before the Clarification step and use
   them as context: the `Global/` notes for the general guidelines
   (geometry, ports, setups), the project notes for the Recipe choice,
   the dimensions, and the Result QA signals of this design.
3. Only a user-approved Learning-loop proposal succeeds in turning a paper's
   technique into a playbook amendment (`knowledge/playbook/`).

Outputs are gitignored; only the user's source PDFs are tracked here.
