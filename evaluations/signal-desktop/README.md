# Signal Desktop — evaluation record

**Subject:** Signal Desktop 8.16.0 (`ffc75db55`, AGPL-3.0) · **Evaluated:** 2026-06-27 ·
**Flow:** evaluate — LLM architectural pass + `egress-lint` deterministic · **Against:** Toolkit-Version 0.2 ·
**Tracking:** [#99](https://github.com/richbodo/personal_network_toolkit/issues/99)

## Headline

Signal Desktop is **not a PNA** and was never built to be one — it is a client/server end-to-end-encrypted
messaging app, a different application *class*, and in fact the canonical conformant **transport** the spec
endorses (AC-18, "Signal-class protocols pass"). Evaluated as a candidate PNA it is **non-conformant** on the
load-bearing ownership/egress commitments — **AC-1** (the private/relationship layer is not sealed by default:
contact notes/nicknames and the relationship graph sync off-device to `storage.signal.org` and the primary
phone), **AC-21** (background sync, not user-initiated), **AC-17** (no per-source provenance) — while genuinely
strong where the spec's values overlap: **AC-18** (E2EE content-blind transport), **AC-19** (full payload
before send), **AC-22** (honest capability assessment), **AC-23** (AGPL source + reproducible Linux builds),
and no telemetry / crash-upload off by default. The mismatch is architectural class, not engineering quality.

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
later commit and diffing the JSON shows any posture drift. The committed copy is the **second run**, regenerated
under the restated AC-1 (the verdict was unchanged — still non-conformant — but the AC-1 *reason* sharpened from
"no two stores" to "the private layer is not sealed by default"). Validate with
`just report-lint evaluations/signal-desktop/evaluate-report.json`.

> **Provenance.** Signal's source is third-party ([`signalapp/Signal-Desktop`](https://github.com/signalapp/Signal-Desktop));
> only the report is archived here, not Signal's source. The validated build was a **stable local build at
> `ffc75db55` (8.16.0)**, held constant across both evaluation runs — so the diff between the two reports
> reflects the AC-1 reframe alone, not any change in Signal.
