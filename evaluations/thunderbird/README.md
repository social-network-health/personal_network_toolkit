# Thunderbird — evaluation record

**Subject:** Thunderbird 153.0a1 Daily (comm-central trunk, `72b8ba076`, MPL-2.0; the released ESR shares this architecture) · **Evaluated:** 2026-07-09 ·
**Flow:** evaluate — LLM architectural pass (deterministic `egress-lint` deliberately skipped: a static egress scan over a ~40k-file Gecko mail client would be noise, not evidence) · **Against:** Toolkit-Version 0.2 ·
**Mode:** goal-impact (Mode 2) — posture `not-a-pna`

## Headline

Thunderbird is **not a PNA** and never claimed to be one — it is Mozilla's desktop email/calendar/chat
client, a different application *class*, so the report is a **goal-impact read** (posture `not-a-pna`)
with the AC findings as the instrument. It carries **the strongest local-data root in the casebook**:
a local, account-independent SQLite address book (`abook.sqlite` per book, in the user's profile),
never carried off-device by the app's own sync (the Sync engine syncs only remote-book *configuration*,
never local cards), in decades-stable formats with built-in vCard/CSV/LDIF export — **Goal 1 reads
`protects`**, a first for an adjacent app. Goals 2–4 read **mixed**. The diminishing facets: **AC-1**
(no enforced private class — per-contact Notes live *inside* the vCard and auto-PUT to the server the
moment the card sits in a CardDAV book; unsent drafts autosave to the IMAP server every 5 minutes;
opt-out telemetry uploads address-book/contact counts to Mozilla by default), **AC-17** (Collected
Addresses: every outgoing recipient becomes a contact card by default, unapproved, no provenance),
**AC-21** (background polling/sync is the app's core mode — 10-minute mail checks, IMAP IDLE + autosync,
30-minute CardDAV interval once configured), plus **AC-9** (no auto-backup ring) and **AC-4** (no
future-version guard on the address-book DB). Where the spec's values overlap, Thunderbird is strong:
**AC-18** (email passes the spec's own transport rule, with built-in opt-in OpenPGP/S-MIME E2EE),
**AC-19** (full payload in the compose window before an explicit Send), **AC-20** (no AI/LLM feature at
all), **AC-22** (honest capability probing), **AC-23** (MPL-2.0 public source). The mismatch is
architectural class, not engineering quality.

## What it proved

This evaluation grounds the casebook's first **`protects` read on Goal 1** by an adjacent app — a
genuinely local, account-independent contact root — and sharpens two class-contrast patterns the
restated AC-1 predicts: **privacy attached to the *container*, not the data class** (the same Notes
field is sealed in a local book and server-synced in a CardDAV book, with nothing at the data layer
distinguishing them), and **pre-send egress** (draft autosave to a server folder as private-data egress
*before* the user's send decision — orthogonal to AC-19's send-time review, which Thunderbird passes).
It also documents the collected-addresses default as the cleanest real-world AC-17 specimen yet: contact
records introduced by the user's own outgoing action, unapproved and provenance-free, yet quarantined in
a separate book with a first-class off-switch. Where a mechanism lives in mozilla-central (profile lock,
crash-reporter submission, safe-mode CLI), the findings say so and decline to guess.

## The report

[`evaluate-report.json`](evaluate-report.json) is keyed to AC IDs and **diffable** — re-evaluating
Thunderbird at a later commit and diffing the JSON shows any posture drift. This is the **first run**,
emitted directly as a first-class Mode-2 (goal-impact) report at report schema 0.2: a
`candidate.classification` block names what Thunderbird *is*, the verdict lives in
`summary.goal_impacts` (Goal 1 **protects**; Goals 2–4 **mixed** — each note naming the AC findings
behind it), and every per-AC status carries repo-relative citations anchored at `72b8ba076`. Validate
with `just report-lint evaluations/thunderbird/evaluate-report.json`.

> **Provenance.** Thunderbird's source is third-party
> ([`mozilla/releases-comm-central`](https://github.com/mozilla/releases-comm-central)); only the report
> is archived here, not Thunderbird's source. The subject is a shallow clone of **comm-central trunk**
> (153.0a1 Daily) at `72b8ba076` — the application layer only. It builds against **mozilla-central**
> (the Gecko platform), which was not part of the checkout: findings whose mechanism lives in the
> platform are marked `unable-to-determine` (AC-11) or carry an explicit platform caveat (AC-6, AC-7,
> AC-15, AC-23) rather than being inferred from memory.
