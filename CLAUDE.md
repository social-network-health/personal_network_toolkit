# CLAUDE.md

PNA Toolkit — a machine-readable, goal-anchored spec (plus typed
contracts, lints, an agent skill, and reference designs) that an AI agent uses to
**build** conformant Personal Network Applications (PNAs) and **evaluate** candidate
apps against the PNA Goals. This is a spec/lint/docs repo, **not** an application.

**Read in this order:** [`README.md`](README.md) (overview + status) →
[`spec/PNA_Spec.md`](spec/PNA_Spec.md) (the spec) →
[`pna-toolkit/SKILL.md`](pna-toolkit/SKILL.md) (the agent flows) →
[`docs/users-guide.md`](docs/users-guide.md) (step-by-step how-to). Run `just` for the
command menu and `just ci` before pushing.

## Keep the docs current

The toolkit's users are developers, and [`docs/users-guide.md`](docs/users-guide.md) is the
developer-facing source of truth. **Any PR that changes a behavior a developer would
notice — a `just` recipe, a lint check or its message, a skill flow, a contract / AC /
manifest field, or a contribution step — MUST update `docs/users-guide.md` in the same
PR.** Accepting the PR accepts the doc change with it. (The PR template carries a
matching checkbox.) This rule exists because the docs fell behind the code once already;
don't let it happen again.

## Documentation map — one source of truth per fact

Restating a fact in a second doc creates a drift surface. Each doc *owns* a category and
the others *link* to it rather than re-explaining:

- **`spec/*.md`** — normative content: Goals, ACs, axes, sub-contracts, Exceptions
  (`EX-*`), Constraints (`CST-*`). Owns *what conformance means*.
- **`pna-toolkit/SKILL.md`** — how the agent executes the build / evaluate /
  contribute flows. Owns *agent procedure*.
- **`docs/users-guide.md`** — task-ordered how-to for humans; mostly numbered action
  sequences. Owns *what a developer does, step by step*. Links to the spec / SKILL /
  CONTRIBUTING for definitions and policy; does not restate them.
- **`CONTRIBUTING.md`** — contribution *policy*: what's accepted, versioning (SemVer),
  archival. Owns *policy*.
- **`CHANGELOG.md`** — version history.

When you add a fact, put it in the doc that owns its category and link from the others.

**Definition before first use.** In a term-defining document (the spec especially, but watch for
others), a term is defined before it is first used. When you reorder such a doc — e.g. promoting a
section toward the top — first check that every term the moved section relies on is already defined
*above* it, and move or add those definitions ahead of it. (Concretely: § Goals and its cardinality
table lean on *Goal*, *Axis*, *Flavor*, *Component*, *Sub-contract*, *AC*, *Exception*, *Constraint* — all
glossed in § Vocabulary, which therefore stays above § Goals.)

## Conventions

- **Stdlib-only `python3` (3.10+).** No third-party runtime deps — no `pytest`, no
  `tomllib` (hand-roll a small parser if needed). CI runs bare `python3`.
  - **One scoped exception:** the Visual Validator viewer is browser JS that can't be tested in
    stdlib, so it has an **opt-in** `pytest` + Playwright suite (`just test-viewer`; dev deps in
    `requirements-dev.txt`) that runs in its **own** CI job and is **never** part of `just ci`. This
    is the sole sanctioned third-party / `pytest` dependency, scoped to browser-UI rendering. See
    [`plans/viewer-e2e-testing-plan.md`](plans/viewer-e2e-testing-plan.md).
- **RFC 2119 language in spec files** — `MUST`/`SHOULD`/`MAY` only when capitalized;
  plain English (motivation, examples) otherwise.
- **The toolkit is versioned as a unit** — every artifact carries a `Toolkit-Version:`
  stamp matching `/VERSION`, enforced by `tools/lint-spec-ids.py`.
- **The AC is the unit of identity**; conformance is *checked, not awarded*; use variable
  language about axis counts ("the axes", never "the six axes").
- Run `just ci` after changes; put manual test/QA steps in the **PR description**.

<!-- BEGIN SHARED: org-conventions v6 -->
<!-- Canonical copy: social-network-health/docs/shared/org-conventions.md
     Do not edit this block in place. Edit the canonical copy and propagate. -->

> **⚙ Shared, generated section — don't edit it here.** Everything from this line down to
> *"Changing this block"* is identical in every repo in the org. Change it in the canonical
> copy (hub `docs/shared/org-conventions.md`) and run `just sync-conventions`; an edit made
> in place will be reported as `EDITED` and then overwritten. Repo-specific guidance belongs
> in this file's *other* sections, which the tooling never touches.

## The organization

The repos of the **[social-network-health](https://github.com/social-network-health)** GitHub
org. A developer normally has them **all checked out side by side in one parent directory**,
so from any repo root every other repo is at `../<name>`. Write cross-repo paths relative to
the repo root, never absolute — the parent directory differs per host.

The set changes as repos are added and archived, so no document states a count; ask the org
(`gh repo list social-network-health`) or read `RELATED_REPOS.md`.

**[`RELATED_REPOS.md`](https://github.com/social-network-health/social-network-health/blob/main/RELATED_REPOS.md)**
in the hub repo is the single source of truth for what those repos are and what each is for.
Don't restate the list in a repo's own docs — a second copy is a second thing to forget.

The layout is a convention of the working environment; it could change, but it holds for now.
It lives in `CLAUDE.md` rather than agent memory because **memory is keyed to the working
directory** — a worktree at a different path starts with a fresh memory dir. A committed file
is the only channel that reaches every worktree and every concurrent agent.

## Planning has four layers

| # | Question | Lives in |
|---|---|---|
| 1 | "What is the software program?" | hub [`software-plan.md`](https://github.com/social-network-health/social-network-health/blob/main/software-plan.md) — the M1/M2/M3 summary |
| 2 | "What should the org be doing?" | hub [`plans/`](https://github.com/social-network-health/social-network-health/tree/main/plans) + `plans/ORG-TASKS.md` |
| 3 | "Where is this repo headed?" | **this repo's** `docs/roadmap.md` |
| 4 | "What's in flight?" | **this repo's** GitHub issues and active branches |

Record a thought at the layer matching its scope.

**Layer 2 is org-only.** Work actionable inside one existing repo belongs in that repo;
`ORG-TASKS.md` links down to it rather than restating its status. **Layer 1 is narrower than
the organization** — `software-plan.md` summarizes the software and research program, not community
building, the toolkit wiki, or educational materials.

Dated files under `plans/` are append-only thinking artifacts. Never update one; write a new
one. `ORG-TASKS.md` is the sole exception — it is kept current.

## Cross-repo working rules

Each of these was learned the hard way in one repo. They apply in all of them.

- **PR and issue bodies via `--body-file`, never an inline `--body`.** Backticks and `$(…)`
  get shell-interpreted and silently drop content — a commit hash has been lost this way.
- **After a PR merges, verify every intended commit actually landed.** A dropped commit is
  silent; recover it in a follow-up rather than assuming the merge was faithful.
- **Triage every test failure as pre-existing or newly-introduced before shipping.** Stash
  and re-run against the base to tell which. Never absorb a pre-existing red into unrelated
  work, and never claim green while a known red stands.
- **Upstream `main` beats local staging plans.** In a multi-agent setup another agent may
  have already filed, merged, or evolved a cross-repo contribution. Check the upstream repo's
  `main` before developing one further — local `plans/` lag.
- **Fail loudly.** Convert an absent guarantee into a red test or a lint failure, never a
  silent pass. Deferrals carry an honest status marker — a strict-xfail, an `Open`/`partial`
  attestation, a documented "⏳ next" — never a bare `TODO` claiming a property the code
  doesn't deliver.
- **One source of truth per fact.** Restating a fact in a second document creates a drift
  surface. Put it in the doc that owns the category and link from the others.
- **Orient without moving; branch only to work.** Reading and priming never need a branch
  change — in a multi-worktree setup `main` is often checked out elsewhere, so a checkout
  fails or strands uncommitted work. Run `git worktree list` before starting. Repo-specific
  worktree setup and port serialization live in that repo's own sections.
- **A sync rule without a mechanical check is a wish.** Anything that must hold in more than
  one repo ships with a command that verifies it, and the rule names the command. Nobody
  eyeballs every repo by hand, so silent drift is the default outcome otherwise.
- **Add a load-bearing document or module → update `.claude/commands/prime.md` in the same
  PR.** Priming is how every agent gets its systems-level picture of a repo, and a prime that
  misses the file where the invariants live sends every future session searching for it. This
  is the same rule as "a user-visible change updates the users guide in the same PR", applied
  to the agent's entry point. Prime is bespoke per repo, so no checksum catches this one —
  the PR is the only gate.
- **Prime is expensive; not priming is more expensive.** `CLAUDE.md` loads every session, so
  it holds what is always true and stays short. Prime is opt-in and costs tokens, so it holds
  the *reading list* — which files give systems-level understanding, and which to skim rather
  than read. Keep prime curated: name the seams, never glob a directory.

## Changing this block

This block is generated. To change it: edit the canonical copy, bump the version in both
markers, run `just sync-conventions` from the hub repo, then open one PR per repo.
`just check-conventions` verifies every copy matches; `just check-org` runs every org check.
Full procedure: hub `docs/org-upkeep.md`.

<!-- END SHARED: org-conventions v6 -->

## Reference designs (cross-repo work)

Two of the sibling repos are this toolkit's reference designs:

- `../fellows_local_db` — first reference design (Directory Archive).
- `../prm` — second reference design (PRM). Note `prm` ≠ `../prt`, the graveyard
  predecessor project.

Spec/contract changes here can have cross-repo implications for both; when in doubt, read
their `docs/Architecture.md`.

## Worktrees (multiple agents on one host)

**Default posture: orient without moving; branch only to work.** Reading and priming never
need a branch change — don't `git checkout main` / `git pull` just to get oriented (in a
multi-worktree setup `main` is often checked out elsewhere, so the checkout fails or strands
uncommitted work). Create a worktree when you start *actual work*, not before. Before you do,
run `git worktree list` and note any sibling worktree whose branch name suggests it's on a
related feature or bug — surface the possible overlap, since two or three agents often run
here at once on different problems.

Worktrees are **cheap and nearly isolated** here — this is a stdlib-only `python3` spec/lint/docs
repo where `just ci` runs against a tempdir copy, so concurrent `just ci` across worktrees can't
collide. The shared host resources are the opt-in viewer servers — **port 8791** (`just test-viewer`)
and **port 8009** (`just view-reports`) — serialize those across worktrees;
everything else (edits, `just ci`, the lints) stays parallel-safe. When more than one Claude
Code / agent works on this host's checkout at once, give each its own worktree so a `git checkout`
in one can't pull the branch (or uncommitted work) out from under another:

```
git worktree add ../pnt-wt-<branch> -b <branch>     # ready immediately — no setup
git worktree remove ../pnt-wt-<branch>              # when done
```

No `wt` recipe or env-share script is needed for the normal stdlib work (the app reference designs
gate on a shared workspace port; here only the opt-in viewer test does — see above). See
[`docs/roadmap.md`](docs/roadmap.md) for which Claude Code instance owns which wave of work.

## Lint discipline — fail loudly

- **Every check in `tools/lint-spec-ids.py` needs a fault-injection case in
  `tools/tests/lint_selftest.py`, added in the *same* change.** A check with no self-test
  can silently rot — exactly what happened to the dead `Reversible:`/`Reversal:` check
  (PR #18, green while enforcing nothing). `just lint-selftest` runs them; the clean tree
  must pass and each injected fault must fail with its expected message.
- **Deferrals are honest** — an in-artifact status (`archival = "pending"`, an attestation
  `partial`/`Open`, a CHANGELOG "deferred" note), never a bare `TODO`/`INERT` comment that
  *claims* a property the code doesn't deliver.
- **Convert an absent guarantee into a red test (or a lint failure), never a silent pass.**

## Toolkit self-check — run it on validations and spec edits

When you complete a **validation / evaluation** or **edit any spec or contract artifact**, run the
**Toolkit self-check** and emit its one-line verdict — routine hygiene, like running tests and checking
docs. It is a judgment-tier audit (not a lint): (1) **layer integrity** — every AC you touched still
**survives a technology swap** *and* **advances a Goal** (a fail means a mis-filed realization or an
orphan), plus the rare, high-value **up-ripple** where a realization or a validation finding reveals an
L1 AC is mis-stated (how AC-1 was restated); (2) **tooling honesty** — did a lint/tool mislead (a false
pass/fail, a checkability gap)?; (3) **route** any finding (field note · inbound-findings registry ·
design note · issue · spec diff) and **honest-decline** when there is nothing. Procedure:
[`pna-toolkit/SKILL.md` § Toolkit self-check](pna-toolkit/SKILL.md). Most runs find nothing — the point
is the occasional high-leverage catch not waiting on serendipity.
