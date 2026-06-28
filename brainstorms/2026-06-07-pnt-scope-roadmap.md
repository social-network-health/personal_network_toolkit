# PNT Scope / Roadmap / Naming — Brainstorm Notes
Date: 2026-06-07 · Goal: Slice the validator's scope, find a value/priority method, and resolve terminology+name. Follows the 2026-06-05 positioning grill.

## Concerns raised by user
1. **Terminology fuzziness** — "personal network" and "relationship data" are used but never defined; language needs cleanup. Upstream of the preamble.
2. **The name** — "Personal Network Toolkit" doesn't explain "personal network"; wants the name aligned on "PNA." (Correction 2026-06-07: the predecessor was **"Personal Relationship Toolkit" (PRT)** — NOT "Personal Network Toolkit." Two docs mislabeled it; both fixed via /btw. So there was never a real name collision — the rename rests on **PNA-alignment**, not disambiguation.)
3. **Scope** — could the **validator become general-purpose** (point it at any app, evaluate against the PNA spec)? End-user framing ("is this safe, here's good/bad, here's how to be safer") differs sharply from the developer AC-keyed report. 80/20 = top OSS apps that handle contact data (Signal + top ~10). Vision: auto-posted report → eventually a daily agent-updated red-light **dashboard** people subscribe to.

## ULTRATHINK — slice scope on 3 INDEPENDENT axes (the "general validator" bundles all three)
- **Axis 1 — Target breadth:** T0 PNAs only (today) · **T1 top OSS contact-data apps (80/20)** · T2 any OSS app.
  - → **T1, reject T2.** The spec only has discriminating power over contact/relationship-data apps; pointed at a video editor it's noise. T2 dilutes signal; T1 is a *bounded, enumerable* test set.
- **Axis 2 — Audience / output register:** A0 developer (AC-keyed conformance) · **A1 end-user (safety posture: good / risk / how-to-be-safer)**.
  - → **A1 is the value unlock.** A0 serves ~him; A1 serves the large privacy-conscious population. A1 reframes the spec from "a build standard" to "a lens for judging the data-safety of an app you already use." Machinery already exists (evaluate flow) — what changes is the *output template* + *target list*. The Signal example is pure A1.
- **Axis 3 — Cadence:** C0 on-demand · **C1 one curated published report** · C2 live daily dashboard.
  - → **C1 now; park C2.** C2 = a product with real ops + liability (continuously publishing judgments, false-reds, maintainer pushback). C1 is cheap, reversible, a great dwebcamp artifact, and produces the learning regardless of readership.

### Synthesis — the thin slice
**One curated, end-user-framed report evaluating the top ~10 OSS contact-data apps against the PNA spec [T1+A1+C1], timed as a dwebcamp artifact.** This is FOCUS-aligned, not scope creep — IF bounded to C1 and refused at C2. It's also the "good test of the system" he wanted + stress-tests the spec + recruits collaborators.

## How to judge value/priority (his explicit question)
Don't judge by **speculative reach** ("will 1% of Signal users read it?") — unknowable, a trap. Judge by a **portfolio of value types**, weighting the near-certain/compounding over the speculative:
1. Learning / spec-feedback (compounding, near-certain)
2. Artifact / recruiting value (his stated #1 need: collaborators)
3. Dogfood value (serves him + ecologically-valid communities — his north star)
4. Speculative reach (discount heavily — an option, not a plan)
+ **Cost** (build + ops + liability) and **Reversibility** (one report = reversible; daily dashboard = sticky).
→ Prioritize high-(1+2+3) / low-cost / high-reversibility. Kills T2, greenlights T1+A1+C1, parks C2.

### Direction vs small trials (his epistemics worry)
Small trials are good for *tuning within* a direction, bad for *choosing* one (cold-start, can't measure compounding/recruiting value, only measure immediate reach). **Set direction from values + near-certain value types; use trials only to tune + find kill-signals.** The C1 report is the rare trial that is *also a real deliverable* — it pays for itself even if reach-signal is null. That's the one trial worth running; "many reach-measuring micro-trials" is the trap.

## FLAGS
- **Liability:** publishing named-app "safety" judgments (Signal etc.) is a reputational/legal surface. Use the defensive frame he already used: "evaluated *against this specific spec's commitments* — note the app isn't trying to be a PNA," not "App X is unsafe." Reproducible, caveated.
- **Drift risk (ties to parked Q3 flag):** the validator-as-service could quietly become the project's identity, pulling it from "toolkit for *building* PNAs" → "privacy-rating service." Great tactic; don't let the tactic eat the mission.
- **His dev pattern is sound & namable:** spec-driven, dogfood-first development of an application-class = how good standards/protocols actually emerge (build what you need → extract invariants → others reuse). The T1 report literally extracts reusable invariants by testing the spec against the field.

## Naming analysis
- The real problem is the **definitional gap**, not the name; a rename is cosmetic to it. Define "personal network" / "relationship data" / "PNA" REGARDLESS.
- Rename to align on "PNA": PRO = aligns spec/toolkit/repo on "PNA," cheapest *now* (pre-dwebcamp), "Personal Network" rhymes with *social network health* (name↔mission). CON = mid-build sweep cost, doesn't fix the definition. (NO disambiguation reason — predecessor was "Personal Relationship Toolkit," not a name collision.)
- Lower-regret default: **keep PNT + add explanatory tagline ("the toolkit for building Personal Network Applications") + fix definitions now; decide rename later** (reversible). But the predecessor-collision is a real point for renaming now.

## DECISIONS MADE (2026-06-07)
- **Scope = THIN SLICE [T1+A1+C1]** — one curated, end-user-framed report evaluating the top ~10 OSS contact-data apps (Signal etc.) against the PNA spec; bounded to ONE report as a dwebcamp artifact; dashboard (C2) parked until demand shown.
  - *Synergy / low marginal cost:* the **validation dashboard he's already building** (parse report → render) is the rendering surface; the 80/20 runs are the content. New work = (a) end-user output template, (b) curate+run ~10 apps, (c) defensive framing/caveats. Mostly reuses planned work → reinforces "focus-aligned, not new scope."
  - Governed by: liability frame ("evaluated against THIS spec; app isn't trying to be a PNA"), and the drift guardrail (tactic must not eat the build mission).
- **Name = "PNA Toolkit"** (chosen 2026-06-07). **Acronym RETIRED** — no "PNT"/"PNAT." Rendering: **"PNA Toolkit" on first mention per doc, "the toolkit" thereafter** (matches existing doc style — "the toolkit"/"toolkit fix"/"Toolkit-Version" already pervasive; lowest cognitive load).
  - **PNAT rejected:** (1) collides with networking **NAT / Port Address Translation (PAT)** — a false friend for the network-literate dweb/crypto audience; (2) awkward half-letter/half-word pronunciation ("P-NAT").
  - Lead-in **"Personal Network" > predecessor's "Personal Relationship":** "network" = the egocentric graph (associogram), not a dyad, and rhymes in sound+sense with *social network health* (name reinforces mission).
- **Sequencing confirmed:** definitions of "personal network" / "relationship data" / "PNA" are the SPINE of the preamble; do them as part of writing it. Name decision is upstream of the preamble.

## NAMING EXPLORATION (candidates)
Note: NO name fixes "explain what a personal network is" — that's solved by the **definition (preamble) + a tagline**, not the name. The name's job: align on "PNA," be clean, disambiguate from the predecessor.
- **PNA Kit** (repo `pna-kit`) — cleanest/shortest; dev-friendly; holds build+validate; disambiguates. ← recommended.
- **PNA Toolkit** (`pna-toolkit`) — minimal change; conservative; slight echo of predecessor "…Toolkit."
- **PNA Bench / PNA Workbench** (`pna-bench`) — evokes build+validate bench; fresh; slightly obscure.
- **PNA Forge** (`pna-forge`) — agentic-building vibe; memorable; build-leaning (under-evokes validate).
Taglines (carry the definition): "Build and check local-first apps that keep your relationships yours." / "Spec, references, and tooling for Personal Network Applications — local-first apps that protect your relationship data."
