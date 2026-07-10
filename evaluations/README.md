# Evaluations — a casebook of validations that proved something

Typed `evaluate-report.json` artifacts from running the toolkit's **evaluate flow**
([`pna-toolkit/SKILL.md` § Evaluate flow](../pna-toolkit/SKILL.md)) against real candidates that are
**not accepted reference designs** — kept because the evaluation *proved something*: it is evidence
behind a spec decision, a worked example of the flow, or a diffable baseline for re-evaluation.

**What this is — and is not.**

- ✅ **Records of validations we ran** — Mode-1 candidate audits *and* Mode-2 goal-impact reads (the
  two non-membership output modes in [`docs/conformance-scope-and-lifecycle.md`](../docs/conformance-scope-and-lifecycle.md)).
- ❌ **Not reference designs.** Those live in [`reference_designs/`](../reference_designs/) and are
  *accepted, conformant, continuously-tested* PNAs that are part of the toolkit. Nothing here is
  endorsed, conformant, or part of the tested set — an entry here may be (and often is) a non-PNA.
- ❌ **Not synthetic samples.** Those live in [`tools/report-viewer/sample-reports/`](../tools/report-viewer/sample-reports/)
  and are illustrative fixtures; these are real evaluations of real software.

**Layout.** One subdirectory per evaluated subject, holding a schema-valid `evaluate-report.json`
(a [`tools/evaluate-report.schema.json`](../tools/evaluate-report.schema.json) instance) plus a short
`README.md` naming the headline finding and what it drove. The reports are **static records**, not
continuously re-run — re-evaluation is deliberate (re-run the flow, diff the JSON for posture drift).

**Run history (`runs/`).** When a subject is re-evaluated, the superseded report is not discarded:
each run also lands as an immutable dated copy at `runs/<date>-run<N>-<tag>.json`, while
`evaluate-report.json` stays the canonical latest (identical to the newest runs/ file). That keeps the
run-to-run diff — *which findings changed, and why* — browsable as files, and lets the Visual Validator
group a subject's history in its picker (pick the app, walk its runs). Only runs that were actually
committed are backfilled; a run that predates its casebook entry stays uncommitted history, noted in
the subject's README.

```
just report-lint  evaluations/<name>/evaluate-report.json   # validate against the render contract
just view-reports                                           # the library: every evaluation here (runs/
                                                            #   history included) + the reference designs
just view-reports evaluations/<name>/runs                   # one subject's history only
```

## Index

- [`signal-desktop/`](signal-desktop/) — **Signal Desktop 8.17.0**. **Not a PNA** — an end-to-end-encrypted
  messaging client, and the canonical AC-18 *transport* the spec endorses; a **Mode-2 goal-impact read**
  (posture `not-a-pna`: Goals 1–3 **mixed**, Goal 4 **protects**). Drove the AC-1 restatement (#106), the
  AC-18 transport field note + the egress-lint blind-spot finding (#107), the Toolkit self-check (#108),
  and the Mode-2 first-class report shape itself (schema 0.2; run 3 is the first instance).
- [`thunderbird/`](thunderbird/) — **Thunderbird 153.0a1** (comm-central trunk). Mozilla's mail client;
  goal-impact read **protects / mixed / mixed / mixed** — the casebook's first Goal-1 **protects** (a
  genuinely local, account-independent contact root; Sync structurally never uploads local cards). The
  diminishing facets: collected-addresses and telemetry (incl. per-scheme contact counts) **on by
  default**, CardDAV auto-PUTs the notes overlay, drafts autosave to the server pre-send. Drove the
  [AC-19 field note](../docs/field-notes/AC-19.md) (send-time review ≠ pre-send persistence).
- [`element-web/`](element-web/) — **Element Web** (develop, + matrix-js-sdk 41.9.0). Federated Matrix
  client; goal-impact read **mixed × 4** — the within-class discriminator against Signal: same verdicts,
  *dual* anatomies (no local root but you can own the server; durability delegated to the account rather
  than held locally; homeserver can veto DM encryption via `.well-known`). Reconfirmed the egress-lint
  blind spot (parameterized-endpoint form).
- [`monica/`](monica/) — **Monica v5 beta** ("Chandler" rewrite). Open-source **PRM** — the toolkit's own
  second reference-design *category* on a client-server architecture; goal-impact read
  **mixed / mixed / diminishes / mixed**. The category-vs-architecture discriminator: relationship data
  plaintext on the server, documents round-trip a vendor CDN even self-hosted, and **no export path for
  the relationship layer**. Surfaced the egress-lint server-side-language false pass.
- [`obsidian/`](obsidian/) — **Obsidian 1.4.16** (closed-source binary; evaluated from the installed
  bundle). The **user-declared-nexus** worked example ("it's just an editor, but I keep all my contacts
  in it"); goal-impact read **protects / mixed / mixed / protects** — a plain-markdown local vault is a
  strong root, but the readable loader proves an hourly update beacon with a persistent device ID, and
  the opaque payload means every guarantee bottoms out in vendor trust (AC-23). First closed-source
  candidate; set the `app.asar!/member` citation convention.

Machinery lessons from this batch:
[`docs/design-notes/2026-07-adjacent-app-evaluation-findings.md`](../docs/design-notes/2026-07-adjacent-app-evaluation-findings.md).
