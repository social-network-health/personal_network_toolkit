# Obsidian — evaluation record

**Subject:** Obsidian 1.4.16 (`/Applications/Obsidian.app`, closed-source proprietary Electron app; no public source, no commit) · **Evaluated:** 2026-07-09 ·
**Flow:** evaluate — LLM bundle-inspection pass only (no deterministic egress-lint tier: a static lint over a 2.8 MB minified asar is not meaningful) · **Against:** Toolkit-Version 0.2 ·
**Mode:** goal-impact (Mode 2) — posture `not-a-pna`, nexus **user-declared**

## Headline

Obsidian is a **closed-source note-taking editor**, not a PNA — and on its face a Mode-3 candidate (an
editor has no apparent personal-network nexus). The nexus is **user-declared**, recorded verbatim in the
report: *"It's just an editor, but I keep all my contacts and my notes about people in it, and I paste
emails to people out of it."* That declaration converts the run to a **goal-impact read** (posture
`not-a-pna`) over the declared contacts vault. The strongest read in the app's favor is the **substrate**:
the root is a local folder of plain markdown the user authored — no account, no proprietary encoding,
readable by any tool — so **Goal 1 and Goal 4 read `protects`** (helped by the File Recovery snapshot
ring, AC-9). The strongest reads against are **epistemic**: the app is an opaque, self-updating minified
artifact with no published source (**AC-23 non-conformant**, the one AC the opacity itself decides), so
the sealed-by-default property Goal 3 wants is checkable only as vendor trust (**AC-1
unable-to-determine**) — the one automatic egress the bundle *does* prove is an hourly update-check
beacon carrying a persistent 16-byte device id to `releases.obsidian.md`, not vault content. **Goals 2
and 3 read `mixed`**: plain-text data is maximally inspectable while the code that touches it is
maximally not. Obsidian Sync is an opt-in, login-gated paid add-on whose end-to-end encryption
(optionally under a user-held key) is provider-asserted, not verifiable here.

## What it proved

This is the **first user-declared-nexus evaluation** — the first real outing of the
Mode-3 → declaration → Mode-2 path end to end ([`pna-toolkit/SKILL.md` § Evaluate flow](../../pna-toolkit/SKILL.md)
step 1; `nexus_source: user-declared` with the verbatim `user_declaration`, schema 0.2). It is also the
first evaluation of a **closed-source candidate**, exercising the honesty rules that entails:
`unable-to-determine` as the default wherever behavior can't be established from the local artifact,
citations as real bundle-relative paths (`Contents/Resources/app.asar!/main.js` — the loader is fully
readable; the 24 MB `obsidian.asar` payload is not), and a `generated_by` that states the verification
ceiling plainly. Fourteen of twenty-three findings are `not-applicable` — an editor triggers almost none of
the spec's behavioral properties — which is itself the Mode-2 point: the goal reads, not the AC walk,
carry the verdict.

## The report

[`evaluate-report.json`](evaluate-report.json) is keyed to AC IDs and **diffable** — re-evaluating a later
Obsidian at the same paths shows any posture drift (e.g. an AI feature arriving would flip AC-20 from
`not-applicable`). Emitted at report schema 0.2: `candidate.classification` records what Obsidian *is*
plus the verbatim declaration that established nexus, and the verdict lives in `summary.goal_impacts`
(Goals 1 and 4 **protects**, Goals 2 and 3 **mixed** — each note naming the AC findings behind it).
Validate with `just report-lint evaluations/obsidian/evaluate-report.json`.

> **Provenance.** The subject is the installed app bundle at `/Applications/Obsidian.app` — the only
> citable artifact (no public source repo exists). Evidence: `Contents/Info.plist`; `main.js` and
> `package.json` extracted read-only from `Contents/Resources/app.asar`; the minified `app.js` and
> `i18n/en.json` extracted from `Contents/Resources/obsidian.asar` (via `@electron/asar`). No dynamic or
> network observation was performed; Obsidian Sync's E2EE claim is recorded as provider-asserted.
