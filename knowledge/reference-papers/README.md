# Reference papers

Drop user-provided PDFs (academic papers, book chapters) here so they can
inform a conversation. They are NOT playbook entries — nothing here amends
the playbook automatically.

How the agent treats them (see `skill/hfss-agent/SKILL.md`, Read first #5):

1. Run the globally installed `analyze-papers` skill on every PDF in this
   folder; it invokes the literature-analyzer CLI and writes agent notes to
   `<analyzer repo>/agent_out`.
2. Read the resulting agent notes before the Clarification step and use
   them as context for the Recipe choice and design decisions.
3. Only a user-approved Learning-loop proposal succeeds in turning a paper's
   technique into a playbook amendment (`knowledge/playbook/`).

Outputs are gitignored; only the user's source PDFs are tracked here.
