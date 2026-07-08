# report-fixtures-lint fixtures

Self-test inputs for [`../report-fixtures-lint.py`](../report-fixtures-lint.py).

- **Clean inputs are the real samples** at [`../report-viewer/sample-reports/`](../report-viewer/sample-reports/)
  — the self-test runs the lint against that directory and expects **exit 0**, so the Visual Validator's
  actual render fixtures are continuously validated (no duplicated clean copy to drift). The set includes
  `05-adjacent-app-goal-impact.json`, the clean **Mode-2 (goal-impact)** shape at schema `0.2`.
- **`dirty/`** — deliberately broken reports, one per lint rule. Expected: **exit 1**, each for its
  own named reason (pinned individually by `case_report_mode2` in the self-tests):
  - `conformant-without-citations.json` — a `conformant` finding with no `citations` (the schema's
    status-conditional rule).
  - `v02-without-classification.json` — a `0.2` report missing `candidate.classification` (the Step-0
    categorization is required at `0.2`).
  - `goal-impact-without-impacts.json` — `classification.mode: goal-impact` with no
    `summary.goal_impacts` (the Mode-2 verdict is missing).
  - `not-a-pna-membership-mismatch.json` — posture `not-a-pna` on a `membership` report (the posture is
    exclusive to goal-impact reads).
  - `user-declared-without-declaration.json` — `nexus_source: user-declared` without the verbatim
    `user_declaration`.
  - `mixed-impact-without-note.json` — a `mixed` Goal read with no `note` naming its two facets.

The self-test wiring is in [`../tests/lint_selftest.py`](../tests/lint_selftest.py) via `case_fixture_lint`
(clean dir passes; dirty dir fails), matching the egress / export / attestation lints, plus
`case_report_mode2` (each dirty fixture fails **for its expected reason**, message-pinned).
