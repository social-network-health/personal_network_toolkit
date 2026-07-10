# What four adjacent-app evaluations taught the toolkit's own machinery

> **Toolkit-Version:** 0.2 · 2026-07 · design note (toolkit self-check routing from the
> Monica / Thunderbird / Element Web / Obsidian goal-impact evaluations; observations and
> small conventions — no spec obligation proposed)

The first batch of routine Mode-2 evaluations ([`evaluations/`](../../evaluations/):
`monica`, `thunderbird`, `element-web`, `obsidian`, joining `signal-desktop`) exercised the
classification gate and the goal-impact report end-to-end. The per-AC content lessons went
to field notes ([`AC-19`](../field-notes/AC-19.md) — send-time review does not cover
pre-send persistence). This note routes the **toolkit-machinery** findings.

## 1. Tooling honesty — `egress-lint`'s blind spot now has three named forms

The documented dynamic-egress blind spot
([`2026-06-egress-lint-dynamic-egress-blind-spot.md`](2026-06-egress-lint-dynamic-egress-blind-spot.md))
was reconfirmed in two new forms and pre-empted in a third:

- **Server-side-language blind spot (Monica).** The lint returned clean /
  `suggested_status: conformant` on a candidate whose *every* egress vector is server-side
  PHP (Uploadcare, LocationIQ, Telegram, Sentry). Recorded as an uncredited
  `source: deterministic` evidence entry on the AC-1 finding, not as a pass.
- **Parameterized-endpoint blind spot (Element Web).** Near-clean on a web SPA whose
  entire egress rides matrix-js-sdk's `baseUrl` parameter — the URLs simply aren't
  literals in the tree.
- **Structurally unavailable for closed bundles (Obsidian).** A static lint over a
  minified `app.asar` is not evidence either way; the run was declined and declared.

**Convention adopted in these reports** (candidate for SKILL wording later): when the
deterministic tier is not meaningful for a candidate's class, *say which class and why in
`generated_by`*, and when it runs but is structurally blind, fold the result in as
evidence explicitly marked a false pass / not credited. A clean scan is never a verdict
(already the rule); on these candidate classes it is not even *evidence*.

## 2. Citation convention for closed-source candidates (Obsidian)

`code_location.path` is described as "repo-relative"; a closed-source candidate has no
repo. The Obsidian report cites the **installed artifact**, using archive-member syntax
for readable files inside a bundle: `Contents/Resources/app.asar!/main.js` (with lines).
Adopted as the working convention so closed-bundle reports stay uniform and diffable —
one descriptive line could later land in the schema's `code_location` description
(toolkit fix; not done here to keep this PR evaluation-only).

## 3. AC seams that strain on non-PNA architectures (observations, no restatement proposed)

Mode-2's instrument-vs-verdict framing absorbed all of these, but the next evaluator
should not have to re-derive the judgment calls:

- **AC-15 ↔ AC-23 coupling (Obsidian).** "Build label tied to source revision" has
  nothing to tie to when no source is published — AC-15 becomes *unsatisfiable via* the
  AC-23 failure, which the spec doesn't name. (Sharper: Obsidian's loader silently
  prefers a newer vendor-signed bundle over the installed one, so the audited artifact
  may not even be the running code — the label question collapses into the source
  question.)
- **Server-class candidates (Monica).** AC-6/AC-7 presume the app runs where the user
  is; AC-PRM-H's loopback trigger presumes a local app. On a served web app these restate
  one architectural fact (server-resident) as several non-conformances. Mode 2 reads
  stay honest because the Goal notes carry the single underlying fact; a "server-class
  candidates" field note may be worth writing after a second server-class evaluation
  confirms the pattern.
- **AC-5 wording (Element Web).** "Gates data behind an authenticated refresh" presumes
  a local-cache-serving architecture; on a server-authoritative client the same concern
  surfaces as *logout wipes the local copy*. The AC still discriminated (it produced the
  Signal↔Element Goal-1/Goal-4 duality), so no restatement proposed.
- **AC-18 when the candidate IS the mail client (Thunderbird).** The AC's email
  allowance is worded for a workspace handing off via `mailto:`; when the candidate is
  the thing `mailto:` hands off *to*, "the downstream provider is outside enforcement"
  strains — the finding carries `needs_human_review`. A clarifying spec note (toolkit-fix
  weight, no new obligation) would settle it.

## 4. What worked

The classification gate + goal-impact verdict did what they were built for: five
applications across four architectures (centralized E2EE client, federated E2EE client,
server web app, closed local editor, mail client) produced **discriminating, non-noisy
reads** — Signal `mixed/mixed/mixed/protects`, Element `mixed×4` *for dual reasons*
(delegated vs. local durability), Thunderbird the casebook's first Goal-1 `protects`,
Monica the category-vs-architecture contrast (`diminishes` on Goal 3 with no
relationship-layer export), Obsidian a user-declared nexus read that still found a real
egress (an hourly update beacon with a persistent device ID). None of it required new
marks on the measuring stick — the Goals carried all of it.
