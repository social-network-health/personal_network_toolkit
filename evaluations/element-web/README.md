# Element Web — evaluation record

**Subject:** Element Web 1.12.23-dev (`7d2657708`, develop; AGPL-3.0/GPL-3.0/commercial) + matrix-js-sdk 41.9.0 (`be09f070c`, Apache-2.0) · **Evaluated:** 2026-07-09 ·
**Flow:** evaluate — LLM architectural pass + `egress-lint` deterministic (static tier only; dynamic-egress blind spot declared) · **Against:** Toolkit-Version 0.2 ·
**Mode:** goal-impact (Mode 2) — posture `not-a-pna`

## Headline

Element Web is **not a PNA** and never claimed to be — it is the flagship web client of the **Matrix
federation**, a browser SPA that is a client of a user-chosen homeserver (default `matrix.org`), so this is a
**goal-impact read** (posture `not-a-pna`) with the AC findings as the instrument. All four Goals read
**mixed** — including Goal 4, which drops from Signal's `protects`. The diminishing facets: **AC-1** (the
contact graph, the `m.direct` DM map, and even Element's own settings are homeserver-side account data; the
local IndexedDB store is a disposable cache), **AC-18** (E2EE is per-room, conditional, and
homeserver-vetoable — plaintext rooms are decoded by the operator as part of operating), **AC-21** (a
background `/sync` long-poll is the app's only data supply), **AC-5** (a server-side token invalidation can
erase the local store), and **AC-9** (no local backup ring — the homeserver *is* the backup). Where Element is
genuinely strong: **AC-11** (a specific "connected in another tab" conflict screen — the full AC, which Signal
only half-meets), **AC-19** (full payload before an explicit send), **AC-22** (probed capabilities, evented
MemoryStore degradation), **AC-23** (AGPL/Apache source, GPG-signed self-hostable releases), opt-in-gated
PostHog analytics (defaults off; the web sample config ships no key), and — the thing Signal structurally
cannot offer — a **self-hostable, open-source server side**.

## What it proved

The question this evaluation was run to answer: **does the Mode-2 goal-impact read discriminate *within* the
E2EE-messenger class**, or does every well-engineered encrypted messenger collapse into the same
mixed/mixed/mixed verdict Signal got? It discriminates, in both directions and on every Goal:

- **Goal 1** — same `mixed`, opposite anatomy: Signal keeps a real local root bound to a fixed service;
  Element keeps no local root at all (**AC-1**, **AC-5**) but lets the user own the *server*
  (self-hosting is first-class), a form of root ownership Signal cannot offer.
- **Goal 3** — the read splits on **AC-18**: Signal's E2EE is universal and unconditioned; Element's is
  per-room, conditional on device keys, and vetoable by the homeserver via `.well-known` — plus
  receipts/typing default **on** where Signal defaults **off**.
- **Goal 4** — the impacts *diverge* (`protects` → `mixed`): Signal's durability is user-held local backups
  (dies with the device unless moved); Element's is delegated to the account — history survives total device
  loss via server-side rooms + encrypted key backup, and dies with the account (**AC-9**, **AC-5**). The two
  failure modes are duals, and the per-Goal scale caught that where a single privacy score could not.
- The deterministic tier's **dynamic-egress blind spot** recurred on a web app exactly as the Signal run
  predicted for native ones: `egress-lint` found 3 static well-known fetches while every load-bearing egress
  rides matrix-js-sdk's parameterized homeserver `baseUrl` — recorded as a declared false-negative on AC-1.

## The report

[`evaluate-report.json`](evaluate-report.json) is keyed to AC IDs and **diffable** — re-evaluating Element at a
later commit and diffing the JSON shows any posture drift. This is the **first run**, emitted directly as a
first-class Mode-2 (goal-impact) report at report schema 0.2: `candidate.classification` names what Element
*is*, the verdict lives in `summary.goal_impacts` (Goals 1–4 all **mixed**, each note carrying the
within-class contrast against Signal), and the evaluation spans **two pinned repos** (`element-web`
`7d2657708` + `matrix-js-sdk` `be09f070c`), with citation paths prefixed per repo. Validate with
`just report-lint evaluations/element-web/evaluate-report.json`.

> **Provenance.** Element's source is third-party ([`element-hq/element-web`](https://github.com/element-hq/element-web),
> with the data/protocol layer in [`matrix-org/matrix-js-sdk`](https://github.com/matrix-org/matrix-js-sdk));
> only the report is archived here, not Element's source. All code citations were read directly at the pinned
> commits (develop-branch checkout, `element-web` monorepo layout with the former matrix-react-sdk merged into
> `apps/web/src`).
