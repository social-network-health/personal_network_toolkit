# Adjacent-app evaluation: the classification gate, and Mode 2 as a first-class output

> **Toolkit-Version:** 0.2 · 2026-07 · design note (toolkit-fix rationale, no new design obligation)

## The finding

The Signal Desktop evaluation ([`evaluations/signal-desktop/`](../../evaluations/signal-desktop/)) was
the toolkit's most productive single validation — it drove the AC-1 restatement (#106), an AC-18 field
note, and the egress-lint blind-spot finding (#107) — and Signal is **not a PNA and never claimed to
be one**. That is not a coincidence: reading an *adjacent* app against the Goals stress-tests the
spec's vocabulary exactly where a conforming reference design cannot (a design built to the spec
rarely reveals that an AC is a mechanism masquerading as a commitment; a well-engineered app from a
different class does). Evaluating adjacent applications should therefore be a **routine** use of the
evaluate flow — and the toolkit had already reserved the seat: the three-mode utility line and roadmap
item R5 in [`docs/conformance-scope-and-lifecycle.md`](../conformance-scope-and-lifecycle.md).

Two gaps kept it from being routine:

1. **No gate.** The skill's evaluate flow walked straight into the AC audit; nothing established
   *what the candidate is* — does it store contact data? private relationship data? does it claim
   membership? — so a non-claimant like Signal got a Mode-1-shaped report with a membership verdict
   (`non-conformant`) the scope doc itself calls noise.
2. **Doctrine and artifact disagreed.** The scope doc's Mode-2 wording said a non-claimant's failed
   ACs read `not-applicable`; the realized Signal report keyed real AC statuses — and that precision
   is what made it productive. Neither the schema nor the skill could express what the report was
   actually doing.

## The decision

- **Classify first (SKILL.md § Evaluate flow, step 1).** Application class · stores contact data? ·
  stores private relationship data? · claims/shaped like a PNA? → **membership** (Mode 1) /
  **goal-impact** (Mode 2) / **out-of-scope** (Mode 3). The classification is recorded in every report
  (`candidate.classification`, schema 0.2) as a matter of course.
- **Mode 3 asks before declining.** A user declaration ("it's an editor, but I keep all my contacts in
  it") establishes the nexus, is recorded **verbatim** (`nexus_source: user-declared`), and the
  evaluation proceeds as a Mode-2 read of *that use*. The gate is honesty about the category, not a
  refusal to look.
- **Instrument vs. verdict.** In Mode 2 the AC walk still runs with real statuses — the instrument
  that makes the read precise, citable, and diffable — but a `non-conformant` entry is a
  *class-contrast observation* feeding a Goal read, not the failure of a claim. The **verdict** is
  `summary.goal_impacts` (per-Goal `protects` / `neutral` / `diminishes` / `mixed` / `out-of-scope`)
  and the posture is **`not-a-pna`**. The scope doc's Mode-2 section was updated to match the realized
  practice (the doc, not the practice, was wrong).
- **`mixed` added to the Goal-impact scale.** Signal's Goal 3 forced it: an exemplary content-blind
  transport (the very transport AC-18 endorses) whose private overlay nonetheless syncs off-device.
  One Goal, materially both directions; a single value + a required note naming both facets beats
  averaging them into `neutral` (which would erase the finding).
- **`not-a-pna` vs `not-pna-active`.** Deliberately distinct: `not-pna-active` is a *claimant*
  temporarily out of PNA mode under an active, handled Exception; `not-a-pna` is an app that was never
  a claimant. Reusing `not-pna-active` for Signal would imply an exception machinery it never engaged.
- **Strictly additive schema (0.2).** Every valid 0.1 instance stays valid — which is what keeps this
  a **toolkit fix**: no design, and no design's deterministic `[verify].entrypoint` emitter, has to do
  anything new to stay conformant. The couplings (0.2 ⇒ classification; goal-impact ⇔ `not-a-pna`;
  complete Goals 1–4; notes on `diminishes`/`mixed`; verbatim user declaration) are enforced by
  `tools/report-fixtures-lint.py`, each rule pinned by a message-level fault-injection self-test.

## Declined

- **A general "privacy score."** The scale stays bounded to the four Goals — the utility line's whole
  argument. Mode 2 reads the Goals, never new criteria.
- **Emitting a report for Mode 3.** An out-of-scope decline is one honest line of prose; a typed
  artifact would dignify "nothing to say" with a shape that invites dashboards of nothing.
- **Requiring Mode 2 for adjacent apps.** A runner may force Mode 1 ("evaluate it as a candidate PNA
  anyway"); the classification still records the nexus honestly, so the report can't silently launder
  a non-claimant into a failed claimant.

## Ripples

- `tools/evaluate-report.schema.json` 0.2 · `tools/report-fixtures-lint.py` + fixtures + self-tests ·
  `pna-toolkit/SKILL.md` evaluate flow · `docs/users-guide.md` §§ Audit / Audit an adjacent app ·
  `docs/conformance-scope-and-lifecycle.md` §§ Mode 2 / R5 (realized) · sample report 05 ·
  `evaluations/signal-desktop/` re-emitted as a first-class Mode-2 report (run 3, v8.17.0).
- Visual Validator rendering of the classification banner + per-Goal impact strip: follow-up PR.
- The casebook (`evaluations/`) is expected to grow adjacent-app reads (Monica, Thunderbird, Element,
  an editor-with-contacts worked example) — each a Mode-2 record, none an endorsement.
