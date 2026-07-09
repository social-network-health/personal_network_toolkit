# Monica — evaluation record

**Subject:** Monica, `main` branch — the v5 "Chandler" beta rewrite (`e08e91734`, Laravel 12 / PHP 8.3 / Inertia + Vue 3, AGPL-3.0-or-later; *not* the stable 4.x branch) · **Evaluated:** 2026-07-09 ·
**Flow:** evaluate — LLM architectural pass + `egress-lint` deterministic (result recorded as a false pass; see below) · **Against:** Toolkit-Version 0.2 ·
**Mode:** goal-impact (Mode 2) — posture `not-a-pna`

## Headline

Monica is **not a PNA** and never claimed to be one — but unlike every other subject in the casebook it is
the **right use case**: an open-source **personal relationship manager**, the toolkit's own second
reference-design category, holding exactly the data the spec exists to protect (contacts plus notes,
journals, reminders, relationships — storing that *is* the product). The mismatch is purely
**architectural**: a client-server Laravel web app whose entire root, private layer included, lives
plaintext in a server database behind an account, readable by whoever operates the server. So the report is
a **goal-impact read** (posture `not-a-pna`): Goals 1, 2, and 4 read **mixed**, Goal 3 **diminishes**. The
load-bearing findings: **AC-1** (no sealed private layer; documents ship to the Uploadcare CDN, addresses
geocode to LocationIQ on save, reminders route through Telegram's bot API once configured), **AC-2** (the
app *is* the SaaS surface the spec forbids — per-user RW endpoints, server-persisted private data, admin
console, CardDAV cross-device sync), **AC-5** (a dead session or account leaves *no* local fallback),
**AC-21**/**AC-10** (hourly background CardDAV polling mutates the root unattended, no preview), and
**AC-9** (no in-app backup, and no export at all for the relationship layer — notes and journals cannot
leave). Where Monica is strong it lands on the spec's own values: **AC-23** (AGPL source) + **AC-15** (a
runtime version+commit label hyperlinked to the exact GitHub commit), **AC-17** (contact data enters only
from user-configured sources), **AC-22** (honest capability probing), standards-based CardDAV/CalDAV
portability of the contact layer, and conservative shipped defaults (every cloud integration off in
`.env.example`). Self-hosting moves custody to whoever runs the server — real, but **operator-grade, not
user-grade**.

## What it proved

This evaluation is the casebook's **category-vs-architecture discriminator**. Signal Desktop was the
inverse case — wrong category (a messenger), with an architecture that locally *resembles* a PNA (local
SQLCipher store, exportable backups). Monica is a **PRM that is not a PNA**: it demonstrates that the
toolkit's conformance line tracks the *architecture* (a sovereign, sealed, local private layer), **not the
use case**, and that "PRM" — the toolkit's own second reference-design category — names a product shape,
not a conformance posture. The AC walk makes the contrast mechanical: the very features that make Monica a
good server product (hourly CardDAV sync, a REST API, vault sharing, cloud document storage) are
one-for-one the behaviors AC-1/AC-2/AC-21/AC-PRM-H name as the departures. The run also produced a tooling
finding: `tools/egress-lint.py` returned **clean / suggested `conformant`** on a candidate whose every
egress vector is server-side PHP (`Http::get` to LocationIQ, the Sentry SDK, Telegram, DAV push jobs) — a
**false pass** extending the known dynamic-egress blind spot to a server-side-language blind spot; it is
recorded honestly as uncredited deterministic evidence on the AC-1 finding.

## The report

[`evaluate-report.json`](evaluate-report.json) is keyed to AC IDs and **diffable** — re-evaluating Monica at
a later commit and diffing the JSON shows any posture drift. This is the first run: all 18 universal ACs
walked, plus all five conditional ACs, each of which is *triggered* here (Monica operates a server, gates
data behind auth, runs its own auth server, mirrors multiple sources, and exposes programmatic surfaces) —
itself a measure of how far the architecture sits from the spec's default posture. The verdict lives in
`summary.goal_impacts` (Goals 1/2/4 **mixed**, Goal 3 **diminishes** — each note naming the AC findings
behind it); `non-conformant` statuses are class-contrast observations feeding those reads, not failed
claims. Validate with `just report-lint evaluations/monica/evaluate-report.json`.

> **Provenance.** Monica's source is third-party ([`monicahq/monica`](https://github.com/monicahq/monica));
> only the report is archived here, not Monica's source. The subject is a shallow clone of the `main`
> branch at `e08e91734` (2025-08-30) — the in-development v5 beta, which the repo's own README flags as
> distinct from the stable 4.x line; findings that hinge on absent features (no account export, minimal
> REST API) are statements about *this branch*, and a 4.x evaluation would differ on those ACs.
