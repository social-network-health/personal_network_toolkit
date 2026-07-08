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

```
just report-lint  evaluations/<name>/evaluate-report.json   # validate against the render contract
just view-reports evaluations/<name>                        # render in the Visual Validator
```

## Index

- [`signal-desktop/`](signal-desktop/) — **Signal Desktop 8.17.0**. **Not a PNA** — an end-to-end-encrypted
  messaging client, and the canonical AC-18 *transport* the spec endorses; a **Mode-2 goal-impact read**
  (posture `not-a-pna`: Goals 1–3 **mixed**, Goal 4 **protects**). Drove the AC-1 restatement (#106), the
  AC-18 transport field note + the egress-lint blind-spot finding (#107), the Toolkit self-check (#108),
  and the Mode-2 first-class report shape itself (schema 0.2; run 3 is the first instance).
