# Loopback-surface auth: the app's own transport is an intrinsic countermeasure (candidate `AC-PRM-H`)

*Design note / spec stub · 2026-06 · status: **LANDED in Toolkit-Version 0.1** ([PR #78](https://github.com/richbodo/personal_network_toolkit/pull/78)); demonstrated-by PRM `main` @ `1551896` ([PR #59](https://github.com/richbodo/prm/pull/59), merged). Complements the [countermeasure library](../../spec/exceptions.md#countermeasure-library) (which already covers the *environmental*, same-UID rows) and the [data-floor](2026-06-data-floor-disclosure-tiers.md) (which bounds the *cloud* surface). Indexed from [`../PriorArt.md` § Design notes](../PriorArt.md).*

> **Landed (was a stub).** `AC-PRM-H` is now in the live AC table ([`../../spec/axes.md` § Workspace shell](../../spec/axes.md#ac-prm-h)), beside the "no ungoverned data tap" principle stated under [`AC-2`](../../spec/axes.md#ac-2) — having landed **with its demonstrator** per [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md) § Contribution types: **PRM #59 merged** (daemon session-auth + the loopback-surface lint, green + attested; durable at `main` @ `1551896`). The deterministic toolkit lint is [`../../tools/loopback-surface-lint.py`](../../tools/loopback-surface-lint.py) (#80); the acceptance-process clarification is in CONTRIBUTING (#79). The original RFC text is preserved below as the design record.

## The gap this closes

The toolkit already governs two of the three ways a PNA's private data is reachable on the host:

- **The cloud MCP surface** — bounded by consent (`AC-MCP-A`) and, proposed, the [data-floor](2026-06-data-floor-disclosure-tiers.md) (`AC-MCP-C`: a cloud-facing surface cannot return a `private-sealed` field, even with consent).
- **A same-UID process reading the store off disk** — routed to the advisory **Harden** flow's [countermeasure library](../../spec/exceptions.md#countermeasure-library) (sandbox the agent, a separate OS user), because *"confining a same-UID agent is an access-control problem, not an encryption one"* and the PNA's own code has no reach there.

It does **not** yet govern the surface in between: **an HTTP/loopback API the PNA itself opens over its own data.** A `workspace-shell:vanilla-js-spa` over `storage:native-sqlite-via-filesystem` PNA stands up a local daemon to serve its workspace (PRM does exactly this). If that daemon is unauthenticated, **any other process on the host can read the whole Private DB by dialing `127.0.0.1`** — a reach the OS file-permission baseline did *not* grant (a sandboxed, lower-privilege, or network-only process that cannot read the store file or `ptrace` the app can still `curl` an open localhost API). The app **widened** its own attack surface — and, unlike the same-UID file read, **the app can close it.** That makes it **PNA-intrinsic**, not environmental: an obligation the toolkit can require and a design can demonstrate — exactly the test the countermeasure library uses to sort intrinsic from environmental.

`AC-2` ("the server, when present, MUST be a delivery channel, not a service") is the right principle at the wrong scope: it is flavor-derived for `web-bundle-*` distribution and forbids *per-user RW endpoints* — so it neither fires for nor fits `never-distributed-single-user` + a *local* RW daemon, which legitimately needs RW endpoints for its single user. `AC-2`'s **intent** generalizes; its current wording does not.

## The three-surface map

| Surface | What it is | Home |
|---|---|---|
| **1. The app's own loopback transport** | the daemon the workspace talks to, over the Private DB | **intrinsic — *this note* (`AC-PRM-H`):** loopback-bind + authenticate to the user's own session |
| **2. An unconstrainable private-row consumer** | the cloud / agent MCP surface | consent (`AC-MCP-A`) + the data-floor (`AC-MCP-C`, proposed) |
| **3. Out-of-band reads** | a same-UID agent reads the store / `ptrace`s the app | advisory **Harden** flow + `CST` ceiling (already covered) |

The not-a-PNA signal stays reserved for **Surface 2's** trigger (a surface that can return private rows to a consumer the PNA cannot constrain). **Surface 1, once authenticated, relaxes no guarantee** — the data stays on the device; the app talks only to itself — so it does **not** flip `pna-active`. Flipping it for an authenticated transport would be the over-classification the [existential review](2026-06-exceptions-existential-review.md) warns against: it would dilute the one bit a relying party keys on.

## The proposal

### `AC-PRM-H` (candidate flavor-derived AC) — generalize `AC-2` to the app-opened local surface

*A same-host-reachable surface a PNA opens over its own Private/Shared data (a loopback HTTP daemon, a local socket) MUST be **loopback-bound** and **authenticated to the user's own session**, so it discloses nothing to an unauthorized same-host reader. A non-loopback bind MUST require an explicit, documented opt-out.* The web-bundle delivery server (`AC-2`) and the native loopback daemon are two realizations of one rule — *a server a PNA stands up must not become an ungoverned data tap*. Trigger: a server-backed local workspace shell (`workspace-shell:*-spa` / `tui` served over a local daemon) crossed with a non-`web-bundle` distribution — most naturally a flavor-derived AC on the **Workspace shell** axis. (Exact placement — extend `AC-2`, or mint a new flavor-derived AC — is the maintainer's call at integration.)

### A loopback-surface lint (static "checked, not asserted")

A sibling of [`tools/egress-lint.py`](../../tools/egress-lint.py) / the proposed disclosure-tier lint: AST-scan a design's source for **(L1)** a server bound to a non-loopback host literal (or a host param defaulting to one), and **(L2)** an HTTP request-handler module that shows *no* auth guard (a constant-time token check / a Host allowlist / a session). Reference implementation: PRM's `scripts/loopback_surface_lint.py` (clean/dirty unit tests; PRM passes, and it flags the *pre-auth* daemon at L2). Bounded claim, like `egress-lint`: it flags the **absence** of a guard, not proof of enforcement.

### Clarification — the data-floor bounds the *cloud* surface only

State explicitly (in the data-floor note / `AC-MCP-C`): a `private-sealed` tier keeps a field off the **cloud-facing MCP** surface; it does **not** protect Surface 1 (the local workspace must render everything to its own user) or Surface 3 (out-of-band file reads). "Sealed" is a cloud-disclosure guarantee, never a local-reader one — so `AC-MCP-C` is not mis-read as a same-host defense.

## Why it's demonstrable (not speculative)

PRM **[#59](https://github.com/richbodo/prm/pull/59)** ships the whole thing, green and attested:

- a **per-process session token** (the workspace bootstraps a `SameSite=Strict` cookie from the launch URL; `/api/*` require it → other local processes get `401`), a **Host allowlist** (DNS-rebinding), an **Origin check** on writes, and a **loopback-pin** (a non-loopback `--host` is refused without an explicit flag) — `daemon/server.py`, `tests/unit/test_daemon_security.py`;
- the **lint** (`scripts/loopback_surface_lint.py` + tests), wired into the design's conformance gate and demonstrated to flag the pre-auth daemon;
- **attested** in PRM's `Architecture.md` as the loopback-daemon realization of `AC-2`'s intent.

This is the read-side transport analog of the cloud-surface work: the same *"minimize + authenticate the surface the app itself opens"* move the countermeasure library already names as **intrinsic**, applied to the one app-opened surface the library has no row for.

## How it composes with the existing Harden / at-rest work

It does **not** revive at-rest encryption (declined — see [PriorArt § Ink & Switch / at-rest](../PriorArt.md)) and does **not** duplicate the same-UID environmental rows. It draws the missing line: **Surface 1 is the app's code (close it — authenticate); Surface 3 is the OS (advise — Harden).** The CHANGELOG's same-UID research hardened Surface 3; this hardens Surface 1, completing the intrinsic/environmental split for the local host. And the *can't-identify-the-consumer* limit the existential review established at the MCP boundary applies identically to the daemon transport — you cannot tell which local process is calling — so the boundary is held the same way: by **authentication + honest signaling, never by identifying the caller** (PRM's `mcp-cannot-identify-the-consuming-llm` note, extended from the cloud consumer to the local one).

## Honest caveats

- **Authentication does not stop a same-UID agent** that can read the session token from the page/process or drive the real workspace UI — that residue is Surface 3 (Harden), unchanged. Surface 1's fix raises the bar against *other* local processes (sandboxed, lower-privilege, network-only, DNS-rebinding), not against an agent with full same-user reach. The honest disclosure of that residue is a user-facing Harden concern, not an app conformance gate.
- **No new obligation on existing designs until accepted.** `fellows_local_db` is a browser PWA with no loopback daemon over private data, so `AC-PRM-H` is vacuous for it. It bites only `native-daemon`-shaped designs — i.e. PRM, the demonstrator — which is why it lands *with* PRM, not as prose alone.

## Sequencing

Land `AC-PRM-H` + the loopback-surface lint **with PRM** (the PR that ships the demonstrating commit), per CONTRIBUTING's reference-driven model — exactly as the data-floor lands with PRM v0.2. This note is the design on the stick; PRM [#59](https://github.com/richbodo/prm/pull/59) is the demonstrator.
