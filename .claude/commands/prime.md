# Prime — personal_network_toolkit
> Read-only orientation: understand the toolkit and where you are, then summarize. Do NOT
> switch branches, pull, or create a worktree while priming — just orient. (CLAUDE.md
> § Worktrees owns when to branch.)

## Run
git ls-files
git status -sb          # branch + ahead/behind + dirty state
git worktree list       # sibling worktrees another agent may be using
just                    # the command surface; `just ci` is the gate before pushing

## Read
docs/roadmap.md          # sequencing + priority tiers + the inbound-findings registry.
                         # READ THIS FIRST for any significant effort — it says what's next
                         # and which wave of work is owned by whom.
spec/PNA_Spec.md         # the spec proper: Goals, ACs, vocabulary
pna-toolkit/SKILL.md     # the agent flows (build / evaluate / contribute / harden)
docs/users-guide.md      # what a developer actually does, step by step

**Spec work needs more than `PNA_Spec.md`.** `spec/` has seven files, and the one you need
depends on the task: `axes.md` (flavor picks), `exceptions.md` (`EX-*` and their handler
clauses), `constraints.md` (`CST-*`), `use_cases.md`, `user_mediation.md`. Read the ones your
change touches — don't assume the main spec file contains them.

## Know before you touch anything
- **This is a spec/lint/docs repo, not an application.** The reference designs that prove the
  spec are siblings: `../fellows_local_db` and `../prm`.
- **Stdlib-only `python3`.** No third-party runtime deps. The single sanctioned exception is
  the opt-in viewer test suite, which never runs in `just ci`.
- **The AC is the unit of identity**, conformance is *checked, not awarded*, and axis counts
  are always variable language ("the axes", never "the six axes").
- **Every check in `tools/lint-spec-ids.py` needs a fault-injection case in
  `tools/tests/lint_selftest.py`, added in the same change.** A check with no self-test rots
  silently — one did, staying green while enforcing nothing.
- **Every artifact carries a `Toolkit-Version:` stamp** matching `/VERSION`; the lint enforces it.

## Before summarizing
- Note your branch. If a sibling worktree looks like it's on a related wave, flag the overlap.
- Name the roadmap tier your task sits in, and whether it touches spec, lint, skill, or docs.
- If the task is a spec change, say which `spec/` files it will need and whether a
  reference-design attestation moves with it.
