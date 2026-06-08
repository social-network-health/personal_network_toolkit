# Visual Validator — report viewer

A static, zero-dependency, engine-agnostic vanilla-JS viewer for the toolkit's
**evaluate** flow output. It renders one instance of
[`../evaluate-report.schema.json`](../evaluate-report.schema.json) — see
[`plans/visual-validator-plan.md`](../../plans/visual-validator-plan.md).

- **`index.html`** — the viewer. No build, no framework, no network, no Chromium-only APIs.
  DOM is built with `textContent`, so report strings can't inject HTML.
  - **Two registers from one JSON:** a **developer (A0)** view (per-finding status, goals,
    requirement, rationale, citations, evidence tagged `deterministic`/`llm`/`human`,
    `needs_human_review`) and a plain-language **end-user (A1)** view (good / at-risk /
    how-to-be-safer, by Goal, with a liability-safe caveat). The end-user view invents nothing
    the report doesn't assert.
  - **View modes** — a segmented control (`end-user` · `side-by-side` · `developer`), persisted in
    `localStorage` and deep-linkable via `?mode=`. **Side-by-side** pairs each finding's plain-language
    and technical cells in one aligned grid row — the educational payoff.
  - **Tested** in a real browser (Playwright): `just test-viewer` — see
    [`plans/viewer-e2e-testing-plan.md`](../../plans/viewer-e2e-testing-plan.md).
- **`sample-reports/`** — the render fixtures + render contract (see its README), guarded by
  [`../report-fixtures-lint.py`](../report-fixtures-lint.py).

## Open it

- **Drag a report onto the page**, or use **open file…** — both work when you open `index.html`
  directly (`file://`), no server needed.
- **`?report=<path>` and the sample buttons** use `fetch()`, which browsers block on `file://`.
  Serve the folder first:

  ```
  python3 -m http.server --directory tools/report-viewer 8009
  # then open http://localhost:8009/index.html
  #   or    http://localhost:8009/index.html?report=sample-reports/03-mixed-exceptions-and-constraints.json&mode=side-by-side
  ```

(A `just view-reports` recipe + the ←/→ directory flip-through land in Phase 5.)
