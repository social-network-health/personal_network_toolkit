# PNT developer tasks. `just` (no args) runs the CI gate locally.
# Requires only python3 (3.11+); the recipes shell out to the stdlib-only tools.

# Default: the same checks CI runs.
default: test

# Mechanical spec / contract / version lints.
lint:
    python3 tools/lint-spec-ids.py

# Tier A — toolkit self-tests: pins the lints' own behavior so a check can't
# silently rot (see tools/tests/lint_selftest.py and plans/conformance-suite-plan.md).
test: lint
    python3 tools/tests/lint_selftest.py

# Tier B (scaffold, Phase 4) — pull a reference design's SWHID-pinned source,
# verify it, build it, and run its [verify] entrypoint. Inert until a design
# declares a real verify entrypoint + container; see the plan doc § Phase 4.
test-design name:
    @echo "Phase 4 is not active yet: this would fetch reference design '{{name}}',"
    @echo "verify 'git rev-parse HEAD^{{{{tree}}}} == swhid_dir', build it, and run"
    @echo "its [verify] entrypoint. See plans/conformance-suite-plan.md § Phase 4."
    @exit 1
