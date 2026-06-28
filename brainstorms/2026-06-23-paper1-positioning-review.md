# Paper 1 (PNA positioning) — review + rewrite decisions

**Date:** 2026-06-23. **Target:** finish the paper this week.
**Paper:** [`docs/papers/paper1-pna-positioning.md`](../docs/papers/paper1-pna-positioning.md) (still a skeleton: outline + exec summary + section stubs).
**Inputs that expanded last week:** [`docs/PriorArt.md`](../docs/PriorArt.md), [`docs/PriorArtReferences.md`](../docs/PriorArtReferences.md).
**Scope of this checkpoint:** Rich's inline review of the **Audience framing → Executive summary**, plus four framing decisions. Rest-of-paper review (§§1–10) still to come.

---

## Audience & tone (settled)

- **Audience** is **developers building privacy-oriented software that gives users confidence and control over their data and their communications.** The local-first community is *included*, not the core. (Rewrite the current "local-first + SE-research" Audience line.)
- **Tone / venue** unchanged: decentralized-web community white-paper tone; Onward!/arXiv/community-whitepaper.

## Problem statement (Q1 — settled: lead with safety-terminology)

The spine **leads with the safety-terminology problem**, not pure positioning:
> The field lacks **shared, checkable terminology for "is this app safe to use with my data?"** A **behavior-rooted directed graph** is the instrument to *converge on that terminology so apps can be validated*. Positioning the PNA class is the **worked demonstration**, not the thesis.

Keep the liked opener ("specifications in the ballpark of local-first software"); strengthen what follows.

## Executive-summary rewrite plan (mapped to Rich's notes)

| Note | Change |
|---|---|
| The graph never got drawn — real gap | Build **two** figures from one shared model (also Paper 2's asset): (1) **clustering figure** (sources → four families) backing Finding 1; (2) **derivation graph** (why-layer → root families → app-class nodes → leaves, with the cross-family-composite node). **Medium: Mermaid now** (Q3), SVG at submission. |
| Finding 1 must *show the clustering from evidence* | Back it with a **coded source→family dataset** → a **data-backed appendix table** at the bottom of the paper. Families read as a *result*, not an assertion. Evidence-safe (Q2). |
| Finding 2 "picks on local-first" | Trim. Drop the sync-engine-contract-vs-manifesto-language elaboration from the summary; **link** the canonical local-first manifesto; end on Rich's line: *"Any application that wants them must layer them on; it does not get them for free."* |
| Finding 3 shouldn't be about our own tool | Reframe to the **gap**: *"No surveyed node composes roots from all four families."* No "PNA" here. |
| Wager | Keep it; in the body say **"the cross-family composite with the highest leverage,"** not "the PNA"; the **final sentence** is the first appearance of PNA in the argument. |
| Contribution should name the *class novelty*, not the product | Lead with the general characterization — *a new application class = a cross-family composite (substrate × sovereignty × assurance × machine-checkable verification) specialized to the personal-network root* — then attach the name. (Rich's "telescopic-lens phone class," not "the S10 Pro.") |
| Citations | **Global rule:** when we cite a manifesto / paper / RFC, **drop an inline link** wherever one exists. |

## Settled inferences (correct if wrong)

- **PNA-naming discipline** applies to the *argument flow* of the exec summary (findings → wager → contribution); title/abstract may still name the class. First use *in the argument* = the wager's last sentence.
- **Four families stay as named** (I Substrate/data-liveness · II Sovereignty/portability/interop · III Assurance/protection · IV Machine-followable spec & verification) — these are the clustering buckets.

---

## The four framing decisions

- **Q1 — Thesis spine:** **Lead with safety-terminology** (above).
- **Q2 — Finding-1 evidence:** **Collect more data first**, then present a **coded source→family map** (evidence-safe; no statistical over-claim). The corpus becomes the paper's bottom appendix table. Rich: the four-family claim is *easy to state, harder to defend* — so put a reasonable data-collection effort behind it now, before finalizing this week.
- **Q3 — Graph medium:** **Mermaid now** (Rich hasn't used it; wants to see it first; expects to iterate as data lands). Promote *just* the derivation graph to Graphviz/SVG if Mermaid layout gets cramped; final SVG at submission.
- **Q4 — Research scope:** the launched survey (below) executes it. After it returns, **auto-run a second round to close the `gaps_to_research`**, then show a **consolidated corpus** — **and report the gap highlights** to Rich (don't silently fold them in).

## Running survey (background) — backs Q2

- **Workflow:** `pna-behavioral-space-survey` · Task `w40w5lbzo` · Run `wf_b49e96d3-17b`.
- **Script:** `…/workflows/scripts/pna-behavioral-space-survey-wf_b49e96d3-17b.js`.
- **Shape:** 8 parallel finders (one per slice) → dedup+synthesis → adversarial uniqueness challenge.
- **Slices:** substrate/sync-engine *contracts* · decentralized-social/identity · portability law/frameworks · assurance/privacy frameworks · machine-followable/AI-SDD · **domain-peers** (Solid pods, MyData, Monica/Clay/Dex, vCard/CardDAV/SCIM) · behavioral manifestos · **safe-app-conformance 2026**.
- **Returns:** deduped **coded source→family table** (the appendix) · **clustering verdict** · **cross-family composites found** · **closest-to-PNA** · **adversarial uniqueness verdict** (agent trying to *refute* "nobody composes all four for a personal-data root") · **gaps**.

## Survey round 1 — results (114 sources; full output in the task file `w40w5lbzo`)

- **Clusters "mostly" into four.** Center-of-mass counts: I=13 · II=19 · III=22 · IV=17 · **spans-multiple=24**. Report as **"mostly," not "yes"** — honest. Three predictable straddle seams: (a) local-first engines bundling e2e/ownership onto the substrate (Jazz, Evolu, Fireproof, DXOS); (b) **III↔IV** — a code-enforced guard is *both* an assurance mechanism and a machine-followable artifact (ocap, consent-receipts, VCs, MCP, OpenPort, OWASP AISVS); (c) **II↔IV** — contact formats as portability-with-a-typing-sliver (vCard, JSContact, DTP, SCIM).
- **Uniqueness/gap claim HOLDS — no counterexample found** (adversarial sweep). Every four-family artifact (Solid, DWN, Matrix) is domain-distant; every personal-data/contact artifact drops a family (usually IV or I). Strongest near-misses: **Solid** (II+III+IV, real conformance harness, can hold contacts — **misses Family I** + all leaf behaviors) and **Verida** (I+II+III local-first encrypted store — **misses Family IV**).
- **LOAD-BEARING framing steer (use in Finding 3 + Contribution):** the claim's force is the **conjunction** — *span × domain × conformance-model* — **not any single novel property**. Each property individually has strong prior art; the paper should **concede that** and distinguish on the conjunction. (Matches Rich's "don't talk about ourselves until the conjunction earns it.")
- **Cite-and-distinguish set:** **Solid** (engage head-on — the strongest near-miss), **Monica** (closest *domain* twin: models contacts + private relationship-memory, but zero structural guarantees), **DSNP**, **vCard/JSContact** (has RELATED/MEMBER fields → "a relationship field ≠ the behavioral contract"), **MCP** (closest analogue to the LLM-as-transport leaf; consent *not* protocol-enforced).
- **Checked-vs-awarded contrast pair fell out:** awarded = MyData Operators, Clay (SOC2), AIUC-1, EUDI; checked = Solid (harness), **W3C VC (two-impl gate — the rigorous checked-not-awarded exemplar)**, Gaia-X compliance service, OpenPort.

## Survey round 2 — gap-closer (running; Task `wpt7t6hah`, Run `wf_f65ab5db-cf3`)

Closing, in priority order: (1) **Family-IV distinction** — do Solid/Matrix/DWN ship a *build-time app spec* (Family IV in our sense) or only *server/client interop* suites? (the disagreement that decides whether the four-family composites are truly Family IV); (2) **Solid contacts/relationship** — any deployment modeling private relationship-memory distinct from the contact record (nearest threat to the two-store split); (3) **citation verification** — confirm load-bearing preprints resolve (OpenPort 2602.20196, CodeSpecBench 2604.12268) and find-or-drop the URL-less "AgentRFC/AgentConform" + "LoRe"; (4) **leaf-unmatched** — governed-egress + Exception/Harden; (5) **loose ends** — ISO 31700-1, ElectricSQL write-path (Finding 2), DSNP nuance, conformance recodings. Reconciler emits: citations to drop/confirm, corpus additions, per-finding claim updates, remaining-open.

## Survey round 2 — results (gap-closer; full output in task file `wpt7t6hah`)

- **Citations: 0 dropped on resolution — all 11 load-bearing ones verified.** Two strong **new** additions: **AgentRFC** (arXiv 2603.23801; tool = AgentConform) and **LoRe** (arXiv 2304.07133 — **peer-reviewed**, ECOOP'23/TOPLAS'24, the strongest source in the set). Cite-fixes: Astrogator = *system* not title; "Specifications: The missing link…" = full title; **EDDOps = "Evaluation-Driven"**; AgentRFC=paper / AgentConform=tool. **Vendor caveat:** AIUC-1, Verida = cite-as-industry-standard / comparable-system, *not* evidence.
- **Family-IV build-vs-interop distinction → PRESERVED & STRENGTHENED.** Solid CTH / Matrix Complement+SyTest / DWN = **server/node wire-interop**, not build-time app conformance; even Solid **App-Interop** is a 2025 Draft CG Report with no app-conformance suite. So the four-family composites aren't Family IV in our sense → the "no four-family composite for a personal-data root" claim **holds**. AgentRFC (formal *protocol* conformance) + LoRe (build-time verification of *generic* invariants) reinforce, not threaten.
- **Two-store split unmatched in Solid (cited):** vCard ontology puts `note` as a literal on the card; SolidOS `contacts-pane#8` "Allow card notes to be private" is **OPEN/unrealized**.
- **Both leaves (egress, Harden) unmatched — ONLY AS CONJUNCTIONS.** Egress discriminator: closest analogues work by **content inspection/redaction = inverse of transport-blindness**. **MITRE D3FEND has a top tactic literally named "Harden"** — cite proactively. Drop unqualified first-ness for break-glass / countermeasure catalogs.
- **Finding 2 sharpened:** ElectricSQL read-path-only + the deliberate 2024 'electric-next' pivot — *"the inventors of CRDTs tried offline writes and walked them back."*
- **Near-PNA substrate in the wild:** DXOS Contacts on ECHO/Automerge + HALO — distinguish-from, not competitor.
- **DSNP correction (was stale):** v1.3.0 (2024-09-26) DOES have encrypted Private Follows/Connections — but "All DSNP Records MUST be publicly visible" → reframe as **public-ledger substrate, encrypted edges**, still distinct from the PNA local-primary two-store split.
- **Conformance recodings:** DMA 6(9)=checked/enforced; NIST 800-53=assessed-not-awarded; ISO 31700-1=checkable-not-yet-certified; CardDAV/JMAP=aspirational + wire-not-build caveat.

## Consolidated corpus + figures (DONE)

→ [`docs/papers/figures/behavioral-space-corpus.md`](../docs/papers/figures/behavioral-space-corpus.md) — generated from both rounds: **Figure 1** (clustering, 4 families + 3 seams), **Figure 2** (derivation graph: only the PNA composite touches all four + the leaves), **Table A** (round-1 corpus), **Table B** (round-2 additions), and the corrections/coding notes. Regenerate via `/tmp/gen_corpus.py`.

## Figure critique → the behaviour-first correction (Rich's review, 2026-06-23)

**The miss (Rich, correct):** the two Mermaid figures jumped from data to **PNA-shaped family boxes** and **conflated *references* with *behaviours***. Symptoms: mixed abstraction levels (a manifesto, a library, a product, an RFC as peer nodes); arbitrary sub-groupings inside a family (the B1/B2/B4 bins had no semantic basis); aggregate nodes ("decentralized social identity") at the same level as individual references (Clay, Solid); wide auto-layout + faint edges = unreadable. **And the `behaviors_mandated` data round 1 actually captured was dropped in synthesis** — "we lost something in conversion from data gathering to acronym-soup graphs."

**Mermaid question (answered):** the readability problems are partly Mermaid `flowchart` auto-layout (goes wide, faint default edges, shrinks text) and partly design. We can swap node-link work to **Graphviz** for print quality — but the deeper fix is to **lead with a matrix table, graph optional/derived.** (The repo's own `PriorArt.md` already uses a "Proximity matrix" — same idiom.)

**The corrected model — what we cluster and why.** Atomic unit = a claim: *"Reference R engenders behaviour B in the applications built on it."* Read each reference by deep reading, naming behaviours in **reference-neutral language** (Solid's WAC-grant, ocap's capability, our least-authority AC → one behaviour: *access granted explicitly, least-authority*) — **this neutral naming IS the "clear up the muddled terminology" deliverable.** Then **cluster the behaviours** (not the references) into families; Substrate/Sovereignty/Assurance/Verification are **hypotheses** — let clusters fall out of the behaviour set and check they match (defends the § 1 goal-agnostic claim + § 8 construct-risk, and literally executes the § 2 "root admission test"). Place each reference by which behaviours/families it engenders. **PNA is just another reference** — read its behaviours off goals→ACs and slot it into the same matrix; "does anyone else engender the same four-family conjunction for the personal-network root?" becomes a **read-off**, not an assertion.

**Family names (LOCKED, Rich):** one word each — **Substrate** (I) · **Sovereignty** (II) · **Assurance** (III) · **Verification** (IV). Use throughout (keep I–IV as parenthetical formal IDs). § 5 table already updated; paper-wide rename pending in the readability pass.

**Data store:** build a real **references × behaviours database** (JSON + CSV + a generated matrix), not collapsed family labels. Round-1 behaviours are recoverable from the finder transcripts (`subagents/workflows/wf_b49e96d3-17b`), but a fresh **behaviour-extraction pass** over the verified 97-ref corpus is cleaner (reference-neutral + controlled vocabulary). The two Mermaid figures in `behavioral-space-corpus.md` are **superseded** — regenerate after the behaviours DB lands.

## Behaviour DB — RESULT + adoption (v2, task `wvye4lijn`)

**The families did NOT hold as hypothesised — and Rich ADOPTED the data.** Emergent clusters (96 refs): the hypothesised Substrate + Sovereignty held; **Assurance/Verification collapsed together** (machine-followable checkability); a **new Disclosure family emerged** (runtime egress governance — the biggest cluster after Substrate/Sovereignty); threat-modelling is a thin cross-cut. The old **"Assurance/protection (III)" dissolved** — confidentiality/least-authority → **Sovereignty**, consent/preview/receipts/HITL → **Disclosure**, threat-modelling → the **Adversary** cross-cut.

**Adopted taxonomy (LOCKED, Rich):** four peer families **Substrate · Sovereignty · Verification · Disclosure** + **Adversary-modelling** (cross-cut, not a peer). **"Verification"** = the machine-followable/checkability family (emergent Assurance B09–B11 + tamper-evidence B12 merged; Rich: "verification" is the natural word for machine-followable). **Disclosure** is the data-surfaced new family — and it is PNA's home turf (governed egress, LLM-as-transport).

**Counts (strong / partial of 96):** Substrate 42/19 · Sovereignty 33/39 · Verification 32/37 · Disclosure 16/39 · Adversary 10 (cross-cut).

**PNA placed honestly (adopted):** Substrate **◐ partial** (downstream-of-SaaS — local-primary but no CRDT/offline-collab sync) · Sovereignty **●** · Verification **●** · Disclosure **●** · Adversary **●**. **Read-off:** the corpus splits into 3 disjoint clusters — personal-network apps/protocols (Disclosure **off**), code-verified-conformance cluster (domain-general, Substrate/Sovereignty off), and Disclosure+Adversary AI-security/PbD (general). **Disclosure-strong *in the personal-network domain* is occupied by PNA alone**; closest single neighbour DXOS Contacts matches ~half the span. Strongest, most legible gap statement yet.

**Artifacts stored** (`docs/papers/figures/`): `references.json` (raw emergent data + PNA), `references.csv` + `behaviour-matrix.md` (adopted four + Adversary cross-cut, PNA last row), `behaviour-vocabulary.md` (26 canonical behaviours + emergent families + reconciliation). Regenerators: `/tmp/gen_matrix.py`, `/tmp/adopt.py`.

**PENDING coordinated rewrite** (awaiting Rich's confirm on the 4 family definitions): §3 four families → adopted four (+ Adversary cross-cut, redistribute old-III citations); **§5 table realign** (currently still on hypothesised four); Findings 1 (families emerged as a *different* four + Disclosure) & 3 (disjoint-clusters gap); §6 PNA composite (Substrate partial; Disclosure load-bearing); **regenerate the figures from the matrix**; Appendix A/B = matrix + vocabulary.

## Terminology check — LOCKED (Rich took all recommendations)

A web-verified namespace check found **3 of the 4 families re-derive established research terms** — evidence the bottom-up clustering is real, not idiosyncratic. Final labels + conventional anchors for the §3 rewrite:

- **Substrate** — keep. Closest umbrella: *local-first software* (broader — bundles ownership, which we file under Sovereignty); no single exact term → mildly unique slicing.
- **Sovereignty** — keep (strongly conventional). Anchors: **data sovereignty**, **self-sovereign identity (SSI)**, informational self-determination.
- **Verification** — keep (Rich's pick). Define as **machine-checkable conformance** in the **Design-by-Contract (Meyer) / runtime-verification** tradition; state once it is *not* formal verification (proofs). Tamper-evidence rides as relying-party *integrity/authenticity*.
- **Disclosure** — keep the label, **anchored** to **usage control (UCON; Park & Sandhu — authorizations + obligations + conditions)** and **information-flow control / declassification** (controlled release: what/who/where/when). Note bare "disclosure" conventionally names the *threat* (STRIDE-I / LINDDUN-D); we mean its *governance*.
- **Adversary-modelling → RENAME "Threat modeling"** (STRIDE / LINDDUN / attack trees). **Cross-cut, not a peer** — a design-time stance ("security/privacy by design") that scopes the other families' guards. PNA overlap = (1) the toolkit's **construction** (countermeasure library; AC-PRM-H from modeling a same-host adversary; the data-floor from modeling cloud-LLM egress) and (2) the **Harden** advisory flow — *not* conformant-app behaviour. LINDDUN is its privacy cousin.

**Paper headline from this:** the families independently re-derive four established namespaces (data sovereignty · DbC/runtime-verification · usage-control/declassification · threat modeling); the novelty stays the PNA's **conjunction** of them over the personal-network root.

**§3 citations to add:** UCON-ABC (Park & Sandhu), declassification dimensions (Sabelfeld & Sands), Design by Contract (Meyer), SSI systematic review, threat-modeling methods (CMU SEI).

## Pass log

- **Pass 5 (2026-06-24) — DONE: the composite-group pass (full).** Framing blessed (name all four; **personal-data trio {PNA,EUDI,Inrupt} + IDS-RAM organizational contrast**; conformance fix). Edits landed across the paper:
  - **§6 reworked + retitled** "The composite group, and the PNA's position within it" — the composite group, the **flavour-of-Disclosure** clarifier, the **6-axis comparison table**, the trio+contrast framing (with the honest conformance cross-cut stated), and **PNA's constellation** (outbound-egress · downstream-mirror · checked-not-awarded · AI-as-egress+adversary+spec-consumer).
  - **§2 method** rewritten honestly (behaviour matrix → groupings → composite groups; the full *derives-from* graph is future work). **Exec Finding 3 + contribution(d)** corrected (composite group, not lone). **§7** Finding 3 corrected + the **4 falsification conditions** (FC-1 occupancy · FC-2 additivity · FC-3 demand · FC-4 staged-path). **§9** limitations + **evolutionary future-work** (revisit-paper-each-version) + the **reference-unification note** (reconcile-not-merge + drift lint). **§10** conclusion corrected + a newcomer **"why/how additive"** explanation. Outline + companion-asset line + the §1 method bullet aligned to the matrix framing.
  - **Figures + data:** conformance corrected (**EUDI/IDS-RAM = awarded**); Fig 1 shows the composite group of four (+ a conformance column); Fig 2's composite box is now the group.
  - **Flagged for Rich:** (a) the **Audience bullet** (line 13) still shows the OLD text in the file — Rich said he fixed it, so his edit may not have saved; I left it untouched. (b) front-matter **Status/Date** (line 3) still says "skeleton / 2026-06-14" — update on a later pass. (c) **§1** (light), **§4** (light), **Appendix A/B** still on the pre-correction framing — future top-down passes.


- **Pass 4 (2026-06-24) — IN FLIGHT: the composite-group correction.** The data shows **"PNA is the lone composite" is FALSE.** Coding "composite" = engenders all four families, the group is **{PNA, EUDI Wallet, IDS-RAM, Inrupt ESS}** (PNA / EUDI / IDS-RAM share the **◐●●●** profile — partial Substrate, strong Sov/Ver/Disc; Inrupt is **●●●◐**). This *strengthens* the paper (the composite shape is real and built by several serious efforts → corroborates "high-leverage"). The finding shifts to **PNA's position *within* the group.**
  - **Two questions HELD (Rich) until the within-group analysis lands:** (1) name all four vs. just the three ◐●●● twins; (2) correct EUDI/IDS-RAM conformance coding from "checked" → certified/awarded (so PNA's checked-not-awarded distinction is clean).
  - **Positioning workflow RUNNING (`w9m1lmeqr`)** — 4 study agents (goals · data-subject/scope · author positioning · per-family *flavour* · conformance · AI stance) + a synth orchestrator → differentiation axes (beyond domain), comparison table, PNA's unique position, a **group-composition recommendation**, and a **draft "Positioning within the composite group"** section (a new paper section). Key axis: the **flavour of Disclosure** each governs — PNA = governed *outbound egress* of relationship data / LLM-as-transport; EUDI = *selective credential presentation* about oneself; IDS = *provider-imposed usage control* (B2B); Inrupt = *inbound access grants* to a pod.
  - **Positioning RESULT (`w9m1lmeqr`, DONE).** 8 differentiation axes: data-subject · **disclosure flavour** · authority/conformance · AI-agent stance · downstream-vs-system-of-record · actuation/HITL · substrate flavour · verification flavour. **Answers the 2 held questions:** (1) **name all four**, framed as a **personal-data trio {PNA, EUDI, Inrupt}** + an **organizational-data contrast case {IDS-RAM}**; within the trio differentiate by *disclosure flavour*. (2) **EUDI + IDS-RAM are *awarded*** (eIDAS accredited-CAB certification; IDS dual-approval body) → **correct the "checked" coding**; PNA + Inrupt are checked-not-awarded. **PNA's unique position = a constellation:** governed-outbound-egress of a *downstream-mirrored* personal relationship graph, checked-not-awarded, AI modelled as **egress + runtime adversary + spec consumer** — no peer overlaps the whole. **Honest cross-cut to state:** the conformance pole (PNA+Inrupt checked vs EUDI+IDS awarded) cuts *across* the data-subject split → multi-axis, not cherry-picked. Comparison table + a 9.3 KB draft "Positioning within the composite group" section in hand → becomes a **new paper section**.
  - **Reference audit DONE (`a7fc5c92…`):** **70 of 96** corpus refs missing from `PriorArtReferences.md` (73% drift); ~46 PAR-only. Recommendation: **reconcile, not merge** — PAR stays the human source of truth, `references.csv/.json` the machine corpus, joined on URL, **+ a drift lint** (fail when a corpus URL is absent from PAR — repo lint-discipline). 7-section categorization + 20 draft entries available → §9 note + a toolkit-fix follow-up (the lint).
  - **Falsification conditions (drafted, for §7 / §10):** **FC-1 occupancy** (a composite over the *contact/relationship* root, checked-not-awarded, usable — the existing composites are adjacent/other domains + certified, so they don't count); **FC-2 additivity** (a mainstream stack ships ownership + privacy + durable governance as *enforced contracts* → composite cheap); **FC-3 demand** (usable, safe PNAs deployed but adoption thin → not high-leverage); **FC-4 staged-path** (full composite incl. safe sync assembled all-at-once, OR the simple floor can't be made usable + safe).
  - **HELD pending the positioning analysis:** §2 method rewrite, Figures 1/2 (composite group), exec Finding 3, §6, §7 (+ falsification), §9 (future work + reference unification), §10 (conclusion + newcomer "why additive"), **and the new "Positioning within the composite group" section.**


- **Pass 3 (2026-06-24) — DONE: §6 / §7 / §8 rewritten** to the four adopted families + matrix read-off.
  - **§6** (PNA composite): placed *from the coded matrix* — strong Sov/Ver/Disc, **partial Substrate**, personal-network domain, checked-not-awarded; the three-disjoint-clusters story; the **IDS-RAM near-twin** (same family signature, but B2B domain + *awarded* → differentiator narrows to **domain + checked-not-awarded**); the leaf additions; **"the claim is a conjunction, conceded part by part."**
  - **§7** (findings + wager): Disclosure surfaced + old "assurance/protection" dissolved; Finding 2 evidence = ElectricSQL **walked-back** offline writes; Finding 3 gap **survived the adversarial pass**; wager now includes *grown one safe layer at a time* (the evolutionary stance); falsification (b) names IDS-RAM as the closest near-miss.
  - **§8** (threats): "clustering is a judgment, not a statistic"; threat-modeling reported as a cross-cut; **"we coded our own artifact"** honesty (incl. the partial-Substrate mark it could have hidden).
  - **Still stale for later top-down passes:** §1 intro + §2 method wording (old root/graph framing), §4 (conformance sub-axis — still sound, light touch), §9 limitations ("no Family-II federation" → Sovereignty), §10 conclusion (restates old four), **Appendix A** (point at `figures.md` Figs 1–2), **Appendix B** (the coded matrix / `behaviour-matrix.md`).
- **Pass 2 (2026-06-24) — DONE: Executive summary rewritten** + figures refined + dir tidied.
  - **Exec summary** now: safety-terminology spine (opening); **Finding 1** = the four data-derived families (Substrate/Sovereignty/Verification/Disclosure + Threat-modeling cross-cut) *re-deriving established research namespaces*, with **Disclosure surfaced** as the non-obvious first-class family; **Finding 2** trimmed (manifesto linked, ends on "layer them on; does not get them for free"); **Finding 3** = the disjoint-clusters gap (no PNA name); **new "An evolutionary stance" paragraph** — the point of tension Rich raised: opinionated simple first moves (two-store shared/private split + downstream-of-SaaS) chosen for *implementable + usable + safe-enough-for-feedback*; this is *why* PNA is **partial on Substrate by design** (forgoes CRDT live-sync because the rules to keep users safe across sync scenarios aren't known yet); the spec **earns** complexity — SaaS-sync / richer substrate are explicit future work, *only once simpler systems are proven usable + safe*, likely via a separately-controlled tool under the same ACs. Wager: composite expensive + must be grown safely → highest-leverage least-served; **PNA first named at the wager's end**. Contribution reframed on the class novelty (cross-family composite) + Disclosure + evolutionary + checked-not-awarded.
  - **Figures** (`figures.md`): Fig 2 is now **`figure-2.svg`** — four uniform 600px boxes, left-justified `Group: / Behaviors: / Tools: / Domain:` rows (Mermaid can't left-justify); composite box has all four families with strengths in `Behaviors:`, `Domain:` on every box (makes the gap visible). Fig 1 cluster names capitalized + matched to Fig 2. Intermediates `refs.json` + `behavioral-space-corpus.md` removed (6 files remain).
  - **Still pending Rich's review** (continuing top-down): the **Audience bullet** (update to "developers building privacy-oriented software"), §2 method wording, §6 PNA composite (align to Substrate-partial + Disclosure), §7 wager + §8 falsification, Appendix A (embed Figures 1–2) / B (the matrix). The evolutionary stance may also warrant a short note in the spec itself later (not this pass).


- **Pass 1 (2026-06-24) — DONE:** §3 rewritten to the four adopted families (**Substrate · Sovereignty · Verification · Disclosure** + Threat-modeling cross-cut), each with its conventional-namespace anchor and redistributed citations, plus the "old Assurance/protection dissolved" redistribution note. §5 table realigned to the adopted four (Disclosure column + the "personal-network classes lack Disclosure" gap note). Figures regenerated from the data → `docs/papers/figures/figures.md` (Figure 1 condensed matrix; Figure 2 three-clusters-+-composite diagram).
- **Pending Rich's top-down review pass** (he reviews from the top each pass, a bit further each time): exec-summary Findings 1–3 (the *different-four* clustering + Disclosure surfaced + the disjoint-clusters gap), §2 method wording, §4 (light — conformance sub-axis still holds), §6 PNA composite (strong Sov/Ver/Disc, partial Substrate), §7 wager, Appendix A (embed Figures 1–2) / Appendix B (the full `behaviour-matrix.md`). NOTE: exec summary still references the *old* four families — expected; his next pass fixes it top-down.

## Next actions

1. **DONE:** § 5 table readability fix (one-word families, *Contributes to*, round-2 corrections folded in).
2. Behaviour-extraction pipeline (Rich chose **A-emergent · B-matrix-first · C-fresh**). 96-ref list (`docs/papers/figures/refs.json`) → Extract (reference-neutral behaviours) → Normalize (controlled vocab + **emergent families** + reconciliation) → Map (re-tag each ref to canonical behaviours + per-family strength) → Place (slot PNA, leaf behaviours + conjunction read-off). Returns structured data → store as JSON/CSV + generated **matrix**.
   - **v1 (`wvywi0u5o`) FAILED** — `args.total` arrived undefined (object likely stringified in transit) → zero batches → empty Extract; only normalize + place ran. **Lesson: don't pass `args` objects to Workflow / don't depend on subagent file-reads — embed inputs in the script.**
   - **v2 RUNNING (`wvye4lijn`, script `/tmp/pna-extraction-v2.wf.js`)** — 96 refs **embedded** in the script, web optional. Resilient.
   - **Early signal (from v1's place agent, which did run):** reading the spec bottom-up, PNA's own ACs cluster into **five** families — the four hypothesised **plus a distinct "Honest-deviation"** family (Exceptions/Constraints/Harden), which the four-family hypothesis omits. Watch whether the full-corpus Normalize surfaces this fifth cluster for other references too, or whether it's PNA-unique (→ a leaf/contribution, not a shared family).
3. Regenerate the figure(s) from the matrix; build into Appendix A; corpus → Appendix B.
4. Rewrite **Audience + problem statement + Executive summary** (safety-terminology spine; Finding 3 + Contribution on the **conjunction**; Finding 2 ElectricSQL "tried-and-walked-back"; link the manifesto).
5. Continue Rich's inline review of **§§1–10**; paper-wide one-word-family rename in the readability pass.
