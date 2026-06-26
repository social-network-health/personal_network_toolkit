# `egress-lint` blind spot: static scanning misses dynamic / config-driven egress

*2026-06-27. Surfaced by the Signal Desktop evaluation (Signal Desktop 8.16.0 @
`ffc75db55`). A **toolkit finding**, not a normative change — it imposes no new
obligation on any design; it records a limitation of a deterministic tool and the
honest reading of its output. Tracked in the
[inbound-findings registry](../roadmap.md#inbound-findings-registry-updated-2026-06-27).*

## The finding

[`tools/egress-lint.py`](../../tools/egress-lint.py) is a regex scan over source for
*static egress vectors* — `fetch("https://…")`, `new WebSocket("…")`, `<img src>`,
`<form action>`, and the like — where the remote origin appears as a **string literal**
at the call/markup site. That design is a good fit for the toolkit's first reference
designs (browser PNAs whose off-device calls are literal `fetch`/`<img src>` to a known
bundle/auth origin). It has a **blind spot**: an app whose egress is **dynamic or
config-driven** — the URL assembled at runtime, read from a config file, or buried
inside a vendored networking/protocol library — presents no literal for the regex to
catch, so the scan can come back **clean while the app egresses heavily**. This is a
**false negative**, the more dangerous direction: a false positive is triaged away by
the allow-list; a false negative reads as "no egress found" when there is plenty.

## The evidence (Signal Desktop)

Run against Signal's real source, `egress-lint` reported all-but-clean:

- `ts/` → **4** flagged vectors, *all* `<link href>` literals in **a test file**
  (`test-electron/linkPreviews/linkPreviewFetch_test.preload.ts`) pointing at
  `https://signal.org/...` icons.
- `app/` → **clean** (zero vectors).

Yet Signal Desktop is a network client that talks to **seven** hosted services
(`chat.signal.org`, `storage.signal.org`, `cdsi.signal.org`, three CDNs,
`sfu.voip.signal.org`) plus the update origin, holds a **persistent websocket**, and
**syncs even the private overlay** (notes/nicknames) to `storage.signal.org`. None of
that surfaced, because the endpoints live in `config/production.json` and the calls go
through `ts/textsecure/WebAPI*` + libsignal — assembled at runtime from config, never a
literal at the call site. The lint was *correct on its own terms* (no unsanctioned
literal egress vector) and *badly misleading* as an answer to "does this app egress?"

## Why it happens (and why that's acceptable for the tool)

The lint is deliberately narrow and deliberately *syntactic* — that is what makes it a
**deterministic** check that runs in CI with no false-confidence about understanding the
program. Statically resolving a runtime-assembled URL is the general
program-analysis problem the toolkit explicitly does **not** take on (per
[`pna-toolkit/SKILL.md`](../../pna-toolkit/SKILL.md) § Principles, the LLM tier owns the
architectural reading; the lints own the mechanical layer). The bug is not in the lint;
it is in **reading a clean lint as a conformance verdict.** The skill already says a
clean deterministic run is *necessary, not sufficient* — this finding is the concrete,
load-bearing case that proves why.

## What this changes

Nothing normative, and no behavior change to the lint. Three honesty fixes, all
docs-level:

1. **The tool says so.** `tools/egress-lint.py`'s docstring now names the
   false-negative blind spot (dynamic / config-driven / vendored-library egress) next to
   the false-positive caveat it already carried, and points here.
2. **The evaluate flow already guards it** — the load-bearing read of Signal's AC-1 came
   from the LLM tier (seven servers, the websocket, the private-overlay sync), with the
   near-clean `egress-lint` folded in as `source: deterministic` evidence *alongside*, not
   as the verdict. That is the intended layering; this note records that it held under a
   real adversarial case.
3. **Registry entry** so the gap is tracked rather than re-discovered.

## Recommended directions (none adopted here — for a later toolkit-fix)

- **Detect the app class and warn.** When the tree has the markers of a
  dynamic/native-egress app (an Electron `app/` + `main` entry, a vendored networking or
  protocol library, an endpoint-bearing `config/*.json`), have `egress-lint` emit a
  one-line *"static scan under-reports for this app class — rely on the LLM/human tier"*
  banner so the near-clean result can't be misread. Cheap, honest, no analysis required.
- **A config-origin sweep.** Optionally grep config/JSON for `https?://` origins and list
  them as *informational* (not violations) so the human sees the declared endpoint set
  even when no literal call-site exists.
- **Leave deep resolution alone.** Statically following a runtime-built URL is out of
  scope by the same rule that keeps the toolkit at ~80/20 description-over-runner; the
  fix is *honest signposting*, not a dataflow engine.

The first item is the highest-value, lowest-cost move and is the natural next toolkit-fix
if this gap is prioritized; it would land with a fault-injection self-test per the lint
discipline in [`CLAUDE.md`](../../CLAUDE.md).
