# Signal Desktop — evaluation record

**Subject:** Signal Desktop 8.17.0 (`44c41468d`, AGPL-3.0; runs 1–2 at 8.16.0 `ffc75db55`) · **Evaluated:** 2026-06-27, re-emitted 2026-07-09 ·
**Flow:** evaluate — LLM architectural pass + `egress-lint` deterministic · **Against:** Toolkit-Version 0.2 ·
**Mode:** goal-impact (Mode 2) — posture `not-a-pna` ·
**Tracking:** [#99](https://github.com/richbodo/personal_network_toolkit/issues/99)

## Headline

Signal Desktop is **not a PNA** and was never built to be one — it is a client/server end-to-end-encrypted
messaging app, a different application *class*, and in fact the canonical conformant **transport** the spec
endorses (AC-18, "Signal-class protocols pass"). So the report is a **goal-impact read** (posture `not-a-pna`),
with the AC findings as the instrument: Goals 1–3 read **mixed** and Goal 4 **protects**. The diminishing
facets are the load-bearing ownership/egress findings — **AC-1** (the private/relationship layer is not sealed
by default: contact notes/nicknames and the relationship graph sync off-device to `storage.signal.org` and the
primary phone), **AC-21** (background sync, not user-initiated), **AC-17** (no per-source provenance) — while
Signal is genuinely strong where the spec's values overlap: **AC-18** (E2EE content-blind transport), **AC-19**
(full payload before send), **AC-22** (honest capability assessment), **AC-23** (AGPL source + reproducible
Linux builds), and no telemetry / crash-upload off by default. The mismatch is architectural class, not
engineering quality.

## What it proved (why it's archived)

This evaluation is what surfaced that **AC-1 was a *mechanism* masquerading as a *commitment*** — the
"two-store ownership split" failed the spec's own swap test (it named a structure, not a goal-entailed
property). That drove the restatement of AC-1 to **"Sovereign, sealed private layer"** ([#106]; rationale:
[`docs/design-notes/2026-06-ac1-privacy-boundary-restatement.md`](../../docs/design-notes/2026-06-ac1-privacy-boundary-restatement.md)).
It also produced the [AC-18 transport field note](../../docs/field-notes/AC-18.md) and the
[egress-lint dynamic-egress blind-spot finding](../../docs/design-notes/2026-06-egress-lint-dynamic-egress-blind-spot.md)
([#107]), and was the first real outing of the [Toolkit self-check](../../pna-toolkit/SKILL.md) ([#108]).
It is the realized **Mode-2 (goal-impact read)** worked example in
[`docs/conformance-scope-and-lifecycle.md`](../../docs/conformance-scope-and-lifecycle.md).

## The report

[`evaluate-report.json`](evaluate-report.json) is keyed to AC IDs and **diffable** — re-evaluating Signal at a
later commit and diffing the JSON shows any posture drift. The committed copy is the **third run**, the first
emitted as a **first-class Mode-2 (goal-impact) report** at report schema 0.2 (the classification gate + Mode-2
machinery this evaluation itself motivated — `docs/conformance-scope-and-lifecycle.md` R5): posture moves from
`non-conformant` to **`not-a-pna`**, a `candidate.classification` block names what Signal *is*, and the verdict
now lives in `summary.goal_impacts` (Goals 1–3 **mixed**, Goal 4 **protects** — each note naming the AC findings
behind it). Run 2 (2026-06-27, at 8.16.0) was the regeneration under the restated AC-1, where the AC-1 *reason*
sharpened from "no two stores" to "the private layer is not sealed by default." Validate with
`just report-lint evaluations/signal-desktop/evaluate-report.json`.

> **Provenance.** Signal's source is third-party ([`signalapp/Signal-Desktop`](https://github.com/signalapp/Signal-Desktop));
> only the report is archived here, not Signal's source. Runs 1–2 were a **stable local build at `ffc75db55`
> (8.16.0)**, held constant so their diff reflects the AC-1 reframe alone. Run 3 moves **two** variables at once,
> deliberately and declaredly: the report shape (schema 0.1 → 0.2, Mode 2 first-class) *and* the subject
> (8.16.0 → **8.17.0**, `44c41468d`, a local build whose test suite passes). To keep that honest, all 34 code
> citations were re-verified and re-anchored at 8.17.0 (line shifts only) and the 8.16→8.17 delta was swept for
> finding-relevant drift — none found (no AI/LLM feature, no local listening surface, crash-upload posture
> unchanged, reproducible builds still Linux-only) — so **every per-AC status is unchanged from run 2**, and the
> JSON diff between runs 2 and 3 is the Mode-2 reframe plus citation re-anchoring.
