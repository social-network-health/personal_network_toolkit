# Scanner blindness, fourth kind: path-set coverage drift

*2026-08-16. Surfaced by the prt archive harvest, reviewing prt's architecture-rule
enforcement against its actual violation set. A **toolkit finding**, not a normative
change — it imposes no new obligation on any design; it records a way a deterministic
scanner's clean output can stop meaning what its reader thinks it means. Tracked in the
[inbound-findings registry](../roadmap.md#inbound-findings-registry-updated-2026-06-27).*

## The finding

The toolkit already records three ways a scanner lies: **vector-shape blindness**
([dynamic / config-driven egress](2026-06-egress-lint-dynamic-egress-blind-spot.md)),
**language blindness** (`loopback-surface-lint`'s bounded claim: Python-only, and "their
absence from a scan is not a clean bill of health"), and **dead-check rot** (the PR #18
lesson in `AGENTS.md`: a check that stays green while enforcing nothing). The prt
harvest surfaced a fourth, distinct from all three: **the path set a scanner is scoped
to encodes an assumption — "these are all the surfaces of this class" — and nothing
re-checks the assumption.**

## The evidence (prt)

The retired [prt](https://github.com/social-network-health/prt) repo enforced four
architecture rules ("only the API layer touches the DB", core-module isolation, and so
on) with grep-able CI invariants — exactly the genre of `egress-lint`. The scanner
covered `prt_src/tui/` because the TUI was the interface that existed when the rule was
written (see prt `docs/ARCHITECTURAL_COMPLIANCE.md` and
`tests/integration/test_architectural_compliance.py`). A second interface
(`prt_src/cli_modules/`) was added later; the scan list was never widened; that
interface decayed into wholesale violations (`api.db.*` calls throughout
`cli_modules/handlers/relationships.py`) while CI stayed green the entire time.

The check still worked — that is what separates this from dead-check rot. It was aimed
at a subset, and the subset silently stopped being the whole. The invariant ceased to be
about the system and became about one directory of it.

## The lesson

A path-scoped scanner makes two claims, and only one is tested: *the scanned paths are
clean* (tested every run) and *the scanned paths are all the paths of this surface
class* (tested never). When a second instance of the surface class appears, the second
claim fails silently and the first keeps passing.

**Countermeasure shape:** pair every path-scoped scanner with an enumeration check — a
cheap assertion that the scanned set still equals the discovered set. For prt's case:
"every top-level package that imports the storage module is in the scan list; if you
added an interface, add it here or this fails red." The general form: derive the
expected surface set from a property the codebase can't hide (imports, entry points,
route registrations), and diff it against the scanner's configured scope.

## Where the toolkit carries the same latent risk

[`tools/egress-lint.py`](../../tools/egress-lint.py)'s `DEFAULT_EXCLUDES` skips
`vendor/`, `dist/`, `build/`, `node_modules/` — each a defensible default, and each
exactly the kind of scope decision this note warns about (the dynamic-egress note's
Signal evidence already showed vendored libraries hiding vectors). The excludes are
visible in `--json` output implicitly but not asserted anywhere. A minimal application
of this lesson to our own tooling: name the exclusion set in the tool's bounded-claim
docstring, and have evaluation records state which excluded directories existed in the
scanned tree, so a reader of a clean report can see what the claim does not cover.

## Status

Captured as a design note (Tier 2 toolkit-fix). Next moves if taken up: (1) the
bounded-claim/reporting line above for `egress-lint`; (2) an enumeration-check pattern
in the lint-authoring guidance (`AGENTS.md` § Lint discipline), alongside the existing
fault-injection-self-test rule — the self-test catches a check that rots; the
enumeration check catches a check that narrows.
