# Positioning the Personal Network Application class among behavioral specifications

**Status:** Working draft — executive summary and section-by-section development on the adopted four-family taxonomy (Substrate · Sovereignty · Verification · Disclosure, with threat-modeling a cross-cut) and the composite-group analysis, with figures generated from the coded 96-source survey. Remaining: full-prose expansion of the skeleton sections (an author pass).
**Date:** 2026-06-24 (rev.; first drafted 2026-06-14).
**Type:** Working paper / pre-draft. This file is a *skeleton an expert can expand* — each section carries its key claims and citations; full prose is left to the drafting pass.
**Companion:** This is **Paper 1** of a planned pair. Paper 2 ("Generative + evaluative application-class blueprints in the AI era — a PNA case study") covers the *method* (how the toolkit is built); it is seeded by [`docs/PriorArt.md`](../PriorArt.md). The two papers share one asset: the behaviour matrix and the composite-group comparison introduced here.
**Provenance:** Synthesized from the R2 multi-agent prior-art investigation recorded in [`brainstorms/2026-06-14-pnt-direction-grill.md`](../../brainstorms/2026-06-14-pnt-direction-grill.md) (§ "R2 SYNTHESIS — the behavioral directed graph"), against the PNA spec's restructured 4-goal shape (Own the root · Integrity-by-validation · Govern egress · Survive entropy/accidents).

---

## Audience & venue framing

- **Audience.** Developers building privacy-oriented software that gives users confidence and control over their data and their communications. The local-first software community and the software-engineering research community (how systems specifications encode behaviour and conformance) are *included*, not the core readership.
- **Venue.** Onward!/SPLASH (the venue where the Ink&Switch local-first essay was published¹), an arXiv preprint, or a local-first community whitepaper. The framing deliberately echoes the local-first essay's "ideals → scorecard" rhetorical move, then departs from it: we replace *ideals* with a *behavior-rooted directed graph* and *aspirations* with *checked conformance*.
- **Tone (evidence-safe).** Claims are stated as **findings** of a structured prior-art survey, not as proofs. The headline positioning claim — that the personal-network root is the *highest-leverage, most underserved* corner of local-first software — is carried as a **stated wager**, explicitly falsifiable, never as settled fact. (This mirrors the spec's own "The wager" framing in [`spec/PNA_Spec.md` § Preamble](../../spec/PNA_Spec.md).)

¹ Kleppmann, Wiggins, van Hardenberg, McGranaghan, "Local-first software: you own your data, in spite of the cloud," *Onward! 2019* — https://www.inkandswitch.com/essay/local-first/ ; ACM DOI https://dl.acm.org/doi/10.1145/3359591.3359737

---

## Executive summary

Specifications "in the ballpark of local-first software" are usually compared by chronology or by feature list — neither of which tells you *which* guarantees an application actually keeps. Yet that is the question a person asks before trusting software with their contacts, their messages, and the private memory of who they know: *is this safe to use?* The field has no shared, checkable vocabulary to answer it. This paper proposes an instrument for building one: a **behaviour-rooted directed graph** that converges on terminology you can use to *validate* an application rather than take it on trust. The leaves are concrete specifications, protocols, and tools; the roots are the *behaviours each one engenders in the applications built on it*; the edges are *derives-from*. We built the graph the hard way — coding a 96-source survey bottom-up, by behaviour — and reading the field this way produces three findings.

**Finding 1 — the field's behaviours cluster into four families that re-derive established research namespaces.** Coded objectively, independent of any one project's framing, the behaviours fall into **Substrate** (where data lives and how it moves — the local-first / replication layer), **Sovereignty** (who controls access and identity — *data sovereignty* and *self-sovereign identity*), **Verification** (checkable guarantees about behaviour — *Design by Contract* and runtime verification, not formal proof), and **Disclosure** (runtime governance of the live act of sharing — *usage control* and *declassification*), with **threat modeling** as a cross-cut. That four bottom-up clusters land on four established namespaces is evidence the taxonomy is real, not idiosyncratic. The non-obvious result: **Disclosure** — show the payload before it is sent, let the user pick the channel, treat an AI/LLM call as just another egress — emerges as a *first-class family* that the usual local-first and security framings fold away.

**Finding 2 — privacy, sovereignty, and durability are *additive*, not inherited from local-first.** The canonical local-first manifesto¹ lists ownership, longevity, and privacy among its ideals, but the mainstream engines people build on enforce none of them; those properties live in the Sovereignty and Disclosure families, not in Substrate. Any application that wants them must **layer them on**; it does not get them for free.

**Finding 3 — a small *composite group* occupies the all-four-families cell, and the PNA sits at a unique corner of it.** The all-four cell is not empty: a composite group engenders all four families — the PNA, the **EUDI** identity wallet, **IDS-RAM** (B2B data spaces), and **Inrupt's Solid** server — which *corroborates* that the shape is real and worth building. Three of them govern an *individual's own* data (a **personal-data trio**); IDS-RAM governs *organizations'* data (the contrast case). The PNA's position within the group is a constellation no peer shares: **governed outbound egress** of a **downstream-mirrored personal relationship graph**, **checked-not-awarded**, with the **AI agent modelled as egress, runtime adversary, and the spec's own consumer** (§ 6).

**An evolutionary stance — why the composite is deliberately incomplete.** A specification for an *application class* earns its recommendations only by building and validating real applications, and that forces a practical question ahead of any elegant one: *what is simple enough to implement, yet usable and safe enough to put in front of users for real feedback?* The class proposed here answers with **opinionated** first moves — splitting storage into a lightly-constrained **shared** store (mirrored, replaceable contact data) and a tightly-constrained **private** store (the user's relationship memory), and operating **downstream of existing SaaS systems of record** rather than synchronising with them. This is exactly why it is, by design, only *partial* on Substrate: it forgoes CRDT-style live multi-device sync not because sync is unwanted but because the rules that would keep users *safe* across every sync scenario are not yet known — and a class specification must not mandate what it cannot yet make safe. Harder capabilities — synchronisation with SaaS, and eventually a richer substrate — are explicit future work, to be taken on *only once the simpler systems are proven usable and safe*, most likely through a separately-controlled tool bound by the same architectural commitments. The specification **earns** complexity; it does not assume it.

**The wager (stated, not proven).** If these properties are additive (Finding 2), the cross-family composite a personal-network root requires (Finding 3) is expensive to assemble and therefore rarely assembled — and if it must additionally be grown one safe, usable layer at a time, rarer still. That is why we bet the **personal-network root is the highest-leverage, least-served corner of this design space**, presented as a falsifiable wager with explicit conditions (§ 7), not a verdict. The specification it motivates — the first worked instance of the method — is the **Personal Network Application (PNA)** specification.

**Contribution.** (a) A reusable, goal-agnostic, behaviour-rooted method that *re-derives* established research namespaces from a coded survey instead of asserting a taxonomy; (b) the four-family taxonomy and the surfacing of **Disclosure** as a first-class family; (c) the *additive-not-inherited* finding, with evidence; (d) the placement of a **new application class** — a cross-family composite (Substrate × Sovereignty × Verification × Disclosure) specialised to the personal-network root (its two-store contact-vs-relationship split, governed egress, and honest-deviation "Harden" model), made machine-checkable and *deliberately evolutionary* — within a small composite group (EUDI, IDS-RAM, Inrupt), at a corner no other member occupies; (e) the *checked-not-awarded* conformance sub-axis that distinguishes its stance.

---

## Paper outline (at a glance)

1. Introduction — the positioning problem; why chronology and feature-lists mislead
2. Method — the behaviour matrix, the groupings, and the composite groups
3. The behaviour families (Substrate · Sovereignty · Verification · Disclosure; Threat-modeling cross-cut)
4. The conformance-model sub-axis — checked/validated vs certified/awarded
5. Application-class nodes and the families they compose (the surveyed leaves)
6. The composite group, and the PNA's position within it
7. Findings & the wager — additive-not-inherited; highest-leverage-underserved (stated bet)
8. Threats to validity & falsification conditions
9. Related work, limitations, future work
10. Conclusion
- Appendix A — the directed graph (future work; today, the behaviour matrix + the composite-group table)
- Appendix B — the reference × behaviour-family matrix

---

## Section-by-section skeleton

### 1. Introduction — the positioning problem

**Purpose.** Motivate reading the field by *behaviour* — not chronology or feature lists — as the instrument for two coupled jobs: converging on a **shared, checkable vocabulary for "is this application safe to use with my data?"**, and, as the worked demonstration of that vocabulary, situating the Personal Network Application class precisely among its neighbours.

**Key claims.**
- The question a person asks before trusting software with their contacts, their messages, and the private memory of who they know is *is this safe to use?* — and the field has **no shared, checkable terminology** to answer it. Converging on that terminology is this paper's primary contribution; positioning the PNA class is the demonstration, not the thesis.
- The local-first essay¹ reframed a field around *ideals* and scored implementations against them (Fast, Multi-device, Offline, Collaboration, Longevity, Privacy, User-control). That move is the model we build on — and the thing we critique: ideals are aspirational, not conformance-bearing. We replace *ideals* with *behaviours* and *aspiration* with *checked conformance*.
- Two common positioning lenses fail for this question. **Chronology** (who published when) hides shared structure; **feature checklists** flatten *derivation* (which behaviour is foundational vs. which is an app-class addition).
- We instead read each artifact by the *behaviours it engenders in the applications built on it* and code them into a **matrix** (§ 2), letting the families (groupings of behaviour) and the *composite groups* (artifacts that engender several families) emerge — so an artifact's placement is a *result* of the coding, not an assumption. The full *derives-from* directed graph that would make every inheritance edge explicit is future work (§ 9); the matrix is what the placement claims rest on.
- The method is **goal-agnostic**: families are identified from what specs actually mandate, independent of the PNA's goals, so the PNA's eventual placement — including the surfacing of **Disclosure** as a first-class family (§ 3) and the PNA's corner of the composite group (§ 6) — is a *read-off*, not an assumption. (Method discipline drawn from the R2 investigation.)

**Citations.** Ink&Switch local-first essay (https://www.inkandswitch.com/essay/local-first/, ACM https://dl.acm.org/doi/10.1145/3359591.3359737); Wikipedia "Local-first software" for the canonical 7-ideals list (https://en.wikipedia.org/wiki/Local-first_software); Tonsky, "Local, First, Forever" as a contrasting community articulation (https://tonsky.me/blog/crdt-filesync/).

---

### 2. Method — the behavior-rooted directed graph

**Purpose.** Define what we actually did precisely, so the result is reproducible and the placement claims are checkable.

**The method, as run.**
- **A behaviour matrix.** For each of the 96 surveyed references we read its primary sources and recorded the *behaviours it engenders in the applications built on it*, in reference-neutral language (so the same behaviour from two sources gets the same name). Each reference is then scored — none / partial / strong — against the behaviour families. The full matrix is Appendix B.
- **Groupings, bottom-up.** The behaviours are clustered into families by what they are *about*; the families (§ 3) are a *result* of the clustering, not an assumption — they are checked against, and re-derive, established research namespaces. References that predominantly engender one family form the source clusters of § 5.
- **Composite groups.** A *composite* is a reference that engenders **all four** families; the composites are themselves a grouping that *composes* the source clusters' behaviours. § 6 identifies the composite group and positions the PNA within it. Coding our own artifact by the identical procedure (§ 8) is what keeps the placement a result rather than an assumption.
- **What this is *not* yet.** We did not build the full *derives-from* directed graph (roots → families → app-class nodes → leaves) that would make every inheritance edge explicit — that richer artifact is appealing future work (§ 9). What we built, and what the placement claims rest on, is the matrix, the groupings, and the composite-group analysis the matrix supports.

**Citations.** GDPR Art. 20 right to data portability (https://gdprhub.eu/Article_20_GDPR); Data Transfer Initiative on DMA Art. 6(9) ↔ GDPR Art. 20 (https://dtinit.org/blog/2025/12/02/dma-gdpr-joint-guidelines); the per-source coding in Appendix B.

---

### 3. The behaviour families

**Purpose.** Present the taxonomy — the paper's backbone. The families below are **not assumed**; they are the result of coding the surveyed corpus (96 references) by the behaviours each one *engenders in the applications built on it*, then letting the clusters emerge (the § 2 method, run for real). Reassuringly, the resulting families re-derive **established research namespaces** — evidence the taxonomy is real, not idiosyncratic — while the one genuinely novel result is *which* combination the personal-network domain leaves unserved (§ 6). Each family states the behaviours it groups, the conventional namespace it corresponds to, and the surveyed references that anchor it. (The full reference × behaviour-family coding is Appendix B.)

#### Substrate — where the data lives and how it moves
- **Behaviours:** local-primary residence · offline operation · conflict-free background sync / convergence · migration without lock-in · portable, machine-readable export · federation over a published wire contract.
- **Conventional namespace:** the *local-first software* substrate — optimistic replication / eventual consistency (CRDTs) plus data portability. No single term covers it exactly; "local-first" is the umbrella, but it bundles *ownership*, which the data files under Sovereignty.
- **Branch point (not a behaviour):** conflict-resolution (CRDT-convergent vs. server-authoritative / LWW); offline-*write* is contested — mainstream engines increasingly decline it (ElectricSQL's 2024 read-path-only pivot is the sharpest case).
- **Anchors:** CRDTs (https://crdt.tech/), Automerge (https://automerge.org/), Yjs (https://yjs.dev/); the local-first essay (Kleppmann et al.); Tonsky, "Local, First, Forever" (https://tonsky.me/blog/crdt-filesync/); LoRe — verifiably-safe local-first (https://arxiv.org/abs/2304.07133) — sits where Substrate meets Verification.

#### Sovereignty — who controls access and identity
- **Behaviours:** owner-decides-access · privacy-by-default · confidentiality / encryption · explicit least-authority grants · self-controlled identity · authentication · public/private visibility.
- **Conventional namespace:** **data sovereignty** and **self-sovereign identity (SSI)** — *informational self-determination*: the user's standing as the authority over their own data and identity. The family absorbs confidentiality and least-authority, which a hand-drawn "security" family would have kept separate.
- **Anchors:** Solid (https://solidproject.org/TR/protocol); AT Protocol (https://atproto.com/); Nostr (https://github.com/nostr-protocol/nips); Matrix (https://spec.matrix.org/); ActivityPub (https://www.w3.org/TR/activitypub/); W3C DIDs (https://www.w3.org/TR/did-1.1/) and Verifiable Credentials (https://www.w3.org/TR/vc-data-model-2.0/); the object-capability model (least-authority); SSI's ten principles (Allen) and the SSI systematic review (https://pmc.ncbi.nlm.nih.gov/articles/PMC9371034/); GDPR Art. 20, DMA Art. 6(9), and the Data Transfer Initiative (https://dtinit.org/) — portability as an instrument of sovereignty.

#### Verification — checkable guarantees about behaviour
- **Behaviours:** typed / declarative contracts · conformance verified by code (not prose) · layered, derive-and-extend specifications · tamper-evident integrity.
- **Conventional namespace:** **Design by Contract** (Meyer) and **runtime verification** — *machine-checkable conformance*. This is **not** *formal verification* (correctness proofs / model-checking): it is the contract-and-conformance tradition, with tamper-evident integrity riding along as its relying-party form (a third party can confirm the data was not altered).
- **Anchors:** GitHub Spec Kit + `constitution.md` (https://github.com/github/spec-kit); Kiro, BMAD, OpenSpec, Tessl; BDD / Gherkin / Cucumber (https://cucumber.io/docs/bdd/); the Model Context Protocol's typed wire contract; AgentRFC / AgentConform (https://arxiv.org/abs/2603.23801) and CodeSpecBench; W3C Verifiable Credentials (the two-independent-implementations conformance gate — the rigorous *checked-not-awarded* exemplar); Design by Contract — Meyer (https://se.inf.ethz.ch/~meyer/publications/old/dbc_chapter.pdf).

#### Disclosure — runtime governance of the live act of egress
- **Behaviours:** user-chosen channel · capability negotiation · pre-send payload preview · informed consent · priority-ordered policy · auditable consent receipts · least-privilege / human-in-the-loop guards · LLM / agent calls governed as egress.
- **Conventional namespace:** **usage control** (UCON — authorizations + *obligations* + *conditions*; Park & Sandhu) and **information-flow control / declassification** — the controlled *release* of protected data, classified along *what / who / where / when*. One caution, stated once: in security, bare "disclosure" names the *threat* (it is STRIDE's *Information Disclosure* and LINDDUN's *D*); here it names the *governance* of that act.
- **Anchors:** the Model Context Protocol's consent model (recommended, not protocol-enforced); OpenID for Verifiable Presentations (wallet selective disclosure); IDS-RAM usage control; ISO/IEC TS 27560 consent receipts; OWASP AISVS and AIUC-1 (AI-egress governance); ISO 31700-1 (privacy-by-design); UCON-ABC — Park & Sandhu (https://profsandhu.com/journals/tissec/ucon-abc.pdf); declassification dimensions — Sabelfeld & Sands (https://link.springer.com/chapter/10.1007/978-3-642-11957-6_5). **This is the largest cluster after Substrate and Sovereignty — and the one the personal-network domain conspicuously lacks (§ 6).**

#### Threat modeling — a cross-cut, not a peer family
- The corpus surfaced one further behaviour — explicit threat-modelling of the design — but it does not behave like a peer family: it is a *design-time stance* that scopes the guards in the others ("security / privacy by design"), not a behaviour an application engenders at runtime. We therefore report it as a cross-cut. Its conventional namespace is **threat modeling** — STRIDE, LINDDUN (privacy), attack trees, MITRE ATT&CK / CAPEC.
- **Anchors:** STRIDE; LINDDUN (https://linddun.org/); threat-modeling methods — CMU SEI (https://www.sei.cmu.edu/blog/threat-modeling-12-available-methods/).

#### What the redistribution tells us
The clustering did not merely rename the hypothesised families — it *re-cut* them, and that re-cut is the terminology-clearing result this paper set out to produce. A hand-drawn "Assurance / protection" family **dissolved**: its confidentiality and least-authority behaviours migrated into **Sovereignty**; its consent / preview / receipt / human-in-the-loop behaviours formed the new **Disclosure** family; its threat-modelling became the cross-cut. The field's protection vocabulary thus splits cleanly into *who holds the data* (Sovereignty), *how the live act of sharing is governed* (Disclosure), and *the modelling stance behind both* (threat modeling). The behaviours that recur across more than one family — owner-decides-access, confidentiality, least-authority, consent / human-in-the-loop, conformance-checked-by-code — are the spine an ambitious application-class specification must touch; their spread foreshadows why a *cross-family composite* is rare (§ 6).

---

### 4. The conformance-model sub-axis — checked vs awarded

**Purpose.** Introduce the orthogonal axis on which the toolkit-as-blueprint takes a position, separate from *which behaviors* a spec mandates.

**Key claims.**
- Conformance models split into two poles: **checked / validated** — published, machine-runnable criteria anyone can apply, no gatekeeper, "checked not awarded" — vs. **certified / awarded** — an accredited human/body confers a credential.
- **Checked cluster:** W3C QA Framework (Specification/Operational/Test Guidelines — conformance is something a spec *defines so anyone can test*); OWASP ASVS/MASVS (a verification standard you run); ISO/IEC TS 27560-style consent **receipts** (machine-readable evidence, not a stamp).
- **Awarded pole (explicitly rejected by the PNA toolkit):** Common Criteria Protection Profiles / ISO 15408 (an evaluation lab issues a certificate); FedRAMP-style authorization (an authority grants ATO). NIST CSF/Privacy Framework corroborate the anti-certification stance (frameworks, not certifications).
- **Adjacent-but-distinct:** OpenSSF-style *badges* — keep the published-criteria-and-linkable-evidence half, drop the badge/award.
- **Placement claim:** The toolkit sits firmly in the **checked** cluster. It borrowed Common Criteria's *structure* (a Protection-Profile-like class document) while dropping its *authority* (no certifying body). (This is the bridge to Paper 2.)
- **The sub-axis cross-cuts the composite group of § 6.** The PNA and Inrupt/Solid sit at the *checked* pole; EUDI and IDS-RAM sit at the *awarded* pole (eIDAS-accredited certification; an IDS dual-approval body). Because that split runs *across* the data-subject split (an individual's data vs. an organization's), *checked-not-awarded* is one of the **independent** axes that distinguish the PNA — not a restatement of its domain.

**Citations.** W3C QA Framework: Specification Guidelines (https://www.w3.org/TR/qaframe-spec/), Operational Guidelines (https://www.w3.org/TR/qaframe-ops/), Test Guidelines (https://www.w3.org/TR/2003/WD-qaframe-test-20030516/); OWASP ASVS (https://owasp.org/www-project-application-security-verification-standard/); Common Criteria Protection Profile / ISO 15408 (https://en.wikipedia.org/wiki/Protection_Profile ; https://www.commoncriteriaportal.org/); ISO/IEC TS 27560 (https://w3c.github.io/dpv/guides/consent-27560); NIST CSF (https://www.nist.gov/cyberframework).

---

### 5. Application-class nodes and the roots they compose

**Purpose.** Lay down the leaves (the surveyed specs) and which family each predominantly draws from — the comparison set against which the PNA is positioned.

**Key claim (one table; most classes anchor in one or two families).**

> *Family shorthand — the four families of § 3, one word each:* **Substrate** · **Sovereignty** · **Verification** · **Disclosure**, with **Threat modeling** as a cross-cut. The **bold** family in each row is the predominant one; *Contributes to* reads "which behaviour families this class engenders in the applications built on it."

| Application class | Contributes to | Conformance model |
|---|---|---|
| Local-first apps (manifesto) | **Substrate**; aspires to Sovereignty but does not enforce it | aspirational scorecard¹ |
| CRDT / sync engines (Automerge, Yjs, Zero, ElectricSQL) | **Substrate**; conflict-resolution is a branch point | engine test suites (checked) |
| Decentralized social / identity (Solid, AT Proto, Nostr, Matrix, ActivityPub, DIDs, VCs) | **Sovereignty** + Verification (signed / typed identity) | mixed; W3C TR conformance for the W3C ones |
| Portability frameworks (DTP, GDPR Art. 20, DMA Art. 6(9)) | **Sovereignty** (export / migrate) | DMA 6(9) Commission-monitored and enforced; GDPR 20 aspirational in practice |
| Machine-checkable / spec-driven dev (MCP, BDD / Gherkin, Spec Kit, Kiro, AgentRFC, LoRe) | **Verification** | checked (executable) |
| AI-egress & privacy governance (MCP consent, OWASP AISVS, AIUC-1, IDS usage control, ISO 27560, ISO 31700-1) | **Disclosure** (+ Threat modeling) | mixed — *checked* (AISVS) to *awarded* (AIUC-1) |
| Security / privacy assurance (CC-PP, NIST CSF / PF, LINDDUN, object-capabilities) | **Verification** + Threat modeling | spans both poles — *checked* and *awarded* |

- **Key claim:** reading down the *Contributes to* column, every class anchors in **one** family (with at most one secondary), and — decisively — the **Disclosure** column is empty for every *personal-network* class (the social / identity / contact apps), while the classes that *do* engender Disclosure are domain-general AI-egress / privacy-governance frameworks. No surveyed class is strong across all four. That split is the empirical setup for § 6 (the PNA composite) and for the **reference × families matrix** (Appendix B) that slots the PNA's own behaviours in alongside these rows.

**Citations:** as enumerated per family in § 3 and § 4.

---

### 6. The composite group, and the PNA's position within it

**Purpose.** State the central positioning result — *read off the coded matrix (Appendix B), not asserted* — at two resolutions: first the **composite group** the PNA belongs to, then the **fine-grained position** of the PNA inside it.

**The composite group.** Coded by the same procedure as every other reference (§ 8), the all-four-families cell is **not the PNA's alone**: a small *composite group* engenders Substrate + Sovereignty + Verification + Disclosure — the **PNA toolkit**, the **EUDI Wallet** (the EU's digital-identity reference architecture), **IDS-RAM** (International Data Spaces, for B2B data exchange), and **Inrupt's Enterprise Solid Server**. That the composite shape is assembled by several serious, independent efforts is *corroborating* evidence — the shape is real and worth building — and it relocates the finding from "the PNA is the lone composite" (false) to *where the PNA sits within the group*. The composites converge from the three source clusters of § 5 (Figure 2); they share the families and diverge sharply on the axes *within* them.

**One clarifying move — the flavour of "Disclosure."** The word hides four distinct acts, and the group splits cleanly along them: *governed outbound egress* (arbitrary user data leaving a store), *selective presentation* (showing chosen claims from one's own credentials), *provider-imposed usage control* (constraining a recipient *after* data has left), and *inbound access grant* (authorising a requester to reach *into* a store). Naming the flavour is the single most legible differentiator in the comparison.

**Positioning within the group** (the axes, beyond domain):

| Axis | **PNA toolkit** | EUDI Wallet | IDS-RAM | Inrupt / Solid |
|---|---|---|---|---|
| **Data subject** | the user's contacts + private relationship memory | the user's own identity credentials | organizations' business data (B2B) | the user's own general Pod data |
| **Disclosure flavour** | governed **outbound egress** (a leak and an outreach are the *same* governed act; an LLM call is a transport) | **selective presentation** of one's own credentials | **provider-imposed usage control** *after* egress | **inbound access grants** to a store |
| **Authority / conformance** | **checked-not-awarded** (no certifying body) | *awarded* — accredited-CAB certification | *awarded* — certification body + PKI | *checked* at the Solid standard layer |
| **AI-agent stance** | first-class: agent as **egress + runtime adversary + spec consumer** | essentially absent | minimal (pre-LLM framing) | governed delegate at the product layer |
| **Downstream vs system-of-record** | **downstream** of SaaS (mirror, don't modify) | holder store; credentials issued upstream | each participant is the system of record | the Pod is the system of record |
| **Actuation / human-in-loop** | un-relaxable floor: **payload preview** + edit/cancel; propose-not-dispose | approval per presentation; *attribute* preview | mostly machine-to-machine | approval at grant time over *metadata* |

**The personal-data trio + an organizational contrast case.** The sharpest single fault line is the **data subject**: three members govern an *individual's own* data (the PNA's contacts, EUDI's credentials, Inrupt's pod) — the **personal-data trio** — while **IDS-RAM** governs *organizations'* data and so anchors the table as the deliberate contrast case (it alone holds the usage-control / system-of-record / machine-to-machine corners, which is what makes the other axes legible). Within the trio, the **flavour of Disclosure** separates all three cleanly: outbound egress (PNA), credential presentation (EUDI), inbound access (Inrupt). Stated honestly, the conformance axis *cross-cuts* this split — the PNA shares the *checked-not-awarded* pole with Inrupt while EUDI sits with IDS-RAM at the *awarded* pole — which is precisely why the members are differentiated on *several independent* axes, not one.

**The PNA's position, as a constellation.** No member overlaps the PNA on the whole intersection: *governed outbound egress* of a *downstream-mirrored personal relationship graph*, *checked-not-awarded*, with the AI agent modelled simultaneously as **egress, runtime adversary, and the spec's own consumer**. Each peer shares one or two of these; none shares the constellation. Per house style this is a **wager** — an invitation to find a counterexample — not a proof of uniqueness.

**The PNA's own leaf additions** (beyond the shared families): the two-store **contact-vs-relationship privilege split**; **governed egress of relationship data** (channel choice, payload preview, never forced onto a content-reading transport, LLM/MCP-as-transport); the **Exception + "Harden"** honest-deviation model; and the **personal-network root** domain itself. **Map onto the spec's goals:** own & build the root (Substrate + Sovereignty) · integrity-by-validation (Verification) · govern egress (Disclosure) · survive entropy & accidents (durability). Threat modeling — the cross-cut — is the design stance behind the spec's Exceptions / Constraints / Harden machinery rather than a runtime behaviour.

**Citations:** the PNA spec ([`spec/PNA_Spec.md`](../../spec/PNA_Spec.md)); the coded matrix (Appendix B); EUDI Wallet ARF (https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/); IDS-RAM (https://docs.internationaldataspaces.org/ids-knowledgebase/ids-ram-4); Inrupt ESS / Solid (https://docs.inrupt.com/ , https://solidproject.org/); the per-member positioning study underlying the table.

---

### 7. Findings & the wager

**Purpose.** State the three findings crisply, then the wager with falsification conditions.

**Key claims.**
- **Finding 1 (taxonomy).** Coding 96 sources bottom-up by behaviour yields four families — **Substrate, Sovereignty, Verification, Disclosure** — that re-derive established research namespaces (§ 3), with **threat modeling** a cross-cut. Two results are non-obvious: **Disclosure** (runtime egress governance) separates out as its own first-class family, and the hand-drawn "assurance / protection" grouping *dissolves* — its behaviours redistribute into Sovereignty, Disclosure, and the cross-cut.
- **Finding 2 (additive-not-inherited) — the empirical centerpiece.** Ownership, longevity/durability, and privacy are present in local-first manifesto *language* but **absent from mainstream sync-engine contracts**; they are behaviours of **Sovereignty and Disclosure**, not **Substrate**. Therefore a local-first app does **not** inherit them — it must add them. The sharpest evidence: ElectricSQL's 2024 *read-path-only* pivot — the inventors of CRDTs tried offline collaborative writes and **walked them back** — so even the substrate specialists decline the behaviour, by contract, not oversight.
- **Finding 3 (the composite group, and the PNA's corner of it).** The all-four-families cell is occupied by a small **composite group** — the PNA, the EUDI Wallet, IDS-RAM, and Inrupt's Solid server — not by the PNA alone (an honest correction the adversarial pass forced). Three govern an individual's own data (a personal-data trio); IDS-RAM is the organizational contrast case. Within the group the PNA holds a corner no peer shares (§ 6): governed *outbound egress* of a *downstream-mirrored personal relationship graph*, *checked-not-awarded*, with the AI agent modelled as egress, runtime adversary, and spec consumer.
- **The wager (stated, falsifiable — not a proven claim).** *Because* these properties are additive (Finding 2), assembling the cross-family composite is costly and therefore rare — and *because* it must be grown one safe, usable layer at a time (the evolutionary stance), rarer still. This is *why* we bet the **personal-network root is the highest-leverage, least-served corner of this design space.** The wager is falsified if any of:
  - **FC-1 · occupancy** — an artifact composes all four families **over a contact / relationship root**, under **checked-not-awarded** conformance, and is usable in practice. The existing composites do *not* count: they govern adjacent or organizational data (EUDI's credentials, Inrupt's pod, IDS-RAM's B2B data), and EUDI / IDS-RAM are *certified* (awarded) — so they corroborate the shape without occupying the PNA's corner. One genuine personal-network + checked composite falsifies it.
  - **FC-2 · additivity** — a mainstream substrate / local-first stack ships ownership + privacy + durable governance as **enforced contracts** (not aspirations) for a personal-data root, making the composite cheap to assemble, so "rare" no longer implies "underserved."
  - **FC-3 · demand** — usable, *safe* PNAs are deployed and adoption / retention is **thin**: people don't keep a sovereign contact-and-relationship store even where it works. (Only the toolkit's own deployment can test this; it is the most decision-relevant.)
  - **FC-4 · the staged path** — the full composite, *including safe multi-device sync*, is assembled all at once (no need to earn complexity layer by layer), *or* the simple floor proves it cannot be made both usable and safe.

  We invite the community to attack each.

**Citations:** Ink&Switch essay (7 ideals); the ElectricSQL writes guide + the 2024 read-path-only pivot (§ 3 Substrate); the coded reference × families matrix (Appendix B).

---

### 8. Threats to validity & falsification conditions

**Purpose.** Pre-empt the obvious objections; keep the tone evidence-safe.

**Key claims.**
- **Survey / selection bias.** The 96-source corpus was assembled by a structured multi-agent survey and then adversarially stress-tested, but it is broad, not exhaustive; under-sampled adjacent fields (decentralized storage à la IPFS / Hypercore, secure-messaging-protocol assurance, data-spaces beyond IDS / Gaia-X) could shift family boundaries or surface a closer near-miss.
- **Clustering is a judgment, not a statistic.** The four families *emerged* from coding behaviours bottom-up and were then reconciled against established namespaces; the coding (reference-neutral behaviour naming, then a strong / partial / none grade per family) is reproducible but not mechanical. The Disclosure↔Sovereignty and Verification↔Substrate seams are the most contestable; we report the center of mass and ship the full coding (Appendix B) so disagreements are about *evidence*, not taste.
- **"Predominant family" is a simplification.** Several references straddle; the matrix records partial cells, and **threat modeling** is reported as a cross-cut rather than forced into a peer family.
- **The wager is a wager.** Finding 3 (the empty intersection) is structural and checkable against the matrix; the *leverage / underserved* claim is the bet, with the conditions in § 7.
- **Construct risk.** "Engenders a behaviour" and the strength grades do heavy lifting; we anchor them to what each source *mandates* (not what it aspires to) and to checkable conformance, to avoid circularity — the same discipline that produces Finding 2.
- **We coded our own artifact.** The PNA was placed by the identical procedure used for every other source, from its goals → ACs — *including* the honest **partial-Substrate** mark it could have hidden. It remains our artifact, and an independent coding is the right external check, which the falsification conditions (§ 7) invite.

---

### 9. Related work, limitations, future work

**Key claims.**
- **Related work.** The local-first essay¹ (the ideals lens we extend); W3C QA's conformance methodology (the "define so anyone can test" stance); and — most directly — the **composite group of § 6** (EUDI, IDS-RAM, Inrupt / Solid) as the nearest neighbours the PNA is positioned against. SPL / feature-modeling and Common Criteria PP authoring belong to **Paper 2** (the method); cited here only to disambiguate scope.
- **Limitations.** v0.1 PNAs are downstream-of-SaaS (no Sovereignty-family federation yet, and only *partial* on Substrate by design — § 6); the analysis captures *specified* behaviour, not *deployed* behaviour; the matrix's strength grades are reproducible judgments, not measurements (§ 8).
- **A note on references.** The survey corpus (the 96-source matrix behind the figures) currently lives apart from the toolkit's curated source list ([`docs/PriorArtReferences.md`](../PriorArtReferences.md)) — ~70 of the 96 have drifted out of that source of truth. The intended fix is to **reconcile, not merge**: keep `PriorArtReferences.md` as the human-readable source of truth and the matrix as the machine corpus, joined on canonical URL, with a small lint that fails when a corpus URL is missing from the list (a follow-up toolkit task).
- **Future work.** (1) The **evolutionary programme** itself: the PNA toolkit continues to develop, and *this paper is revisited each time a new toolkit / spec version expands or contracts the space the class operates in* — most consequentially when synchronisation with SaaS, and a richer Substrate, are taken on (only once the simpler systems are proven usable and safe). (2) Promote the matrix to the full *derives-from* directed graph (§ 2). (3) Add the under-sampled fields (§ 8). (4) Test the wager against a real PNA's adoption (FC-3, § 7).

**Citations.** Paper 2 seed ([`docs/PriorArt.md`](../PriorArt.md), [`docs/PriorArtReferences.md`](../PriorArtReferences.md)); W3C QA (§ 4); the § 6 composite-group sources.

---

### 10. Conclusion

**Key claims (restate, tightly).**
- Reading the field by the *behaviours each artifact engenders* — a coded matrix, not chronology or a feature list — let us position a new application class as a member of a small **composite group**, and locate it precisely within that group.
- The field's behaviours fall into **four families** that re-derive established research namespaces — Substrate, Sovereignty, Verification, Disclosure — with threat modeling a cross-cut.
- **Privacy, sovereignty, and durability are *additive*, not inherited from local-first** — the survey's strongest finding. *Why* (for the reader meeting this cold): a local-first engine guarantees your data lives on your device and converges across copies (Substrate), but it says nothing about *who may access it* (Sovereignty) or *how it is allowed to leave* (Disclosure) — those are different families of behaviour, present in the manifestos' language but absent from the engines' contracts. *How we found it:* coding each engine by what it actually mandates (not what its marketing aspires to) placed ownership / privacy / durability in families other than Substrate, and left the substrate engines — even the CRDT pioneers, who tried and walked back offline writes — not enforcing them. So any app that wants these properties must add them.
- **The PNA is not the lone composite** — the all-four-families cell holds a composite group (PNA, EUDI, IDS-RAM, Inrupt). It is differentiated within the group strongly and on several independent axes: it is the member concerned with a **high-leverage, highly-constrained application class — personal contact and relationship data** — governing **outbound egress**, *downstream of* SaaS, *checked-not-awarded*, with the AI agent treated as egress, adversary, and spec consumer.
- The leverage / underserved claim stands as a **wager** with explicit falsification conditions (§ 7) — an invitation to the community, not a verdict.

---

## Appendix A — the directed graph (future work) and today's figures

The full *derives-from* directed graph — above-the-roots "why" → root families → app-class nodes → leaves, every inheritance edge explicit — is **future work** (§ 9). What backs the placement claims *today* is the coded behaviour matrix and two figures generated from it; see [`figures/figures.md`](figures/figures.md):

- **Figure 1 — the behaviour-family matrix:** the three source clusters and the composite group, scored ● strong / ◐ partial / · none across the four families, with the conformance column and domain.
- **Figure 2 — positioning** ([`figures/figure-2.svg`](figures/figure-2.svg)): the three source clusters converging on the composite group; within it, the PNA's outbound-egress / downstream-mirror / checked-not-awarded / AI-native corner.

*Skeleton of the eventual graph (families re-cut to the adopted four + the Adversary cross-cut; behaviour IDs per [`figures/behaviour-vocabulary.md`](figures/behaviour-vocabulary.md)):*

- **Above-the-roots ("why") layer:** GDPR Art. 20 · DMA Art. 6(9) · Ink&Switch 7 ideals (aspirational).
- **Root families (nodes):** **Substrate** {local-primary residence, offline operation, background-sync/convergence, migrate-without-lock-in, portable export, federation-via-wire-contract} · **Sovereignty** {owner-decides-access, privacy-as-default, confidentiality/encryption, least-authority grants, self-controlled identity, authenticate-before-access, public/private visibility} · **Verification** {typed/declarative contract, conformance-checked-by-code, layered derive-and-extend, tamper-evident integrity} · **Disclosure** {user-chosen channel, runtime capability negotiation, pre-send payload preview, informed consent, priority-ordered policy, auditable consent receipt, human-in-the-loop guards, governed LLM/agent egress}.
- **Cross-cut (not a peer family):** **Adversary-modelling / threat-modelled design** — the design-time stance that scopes the guards in the other families.
- **Branch points (not behaviours):** conflict-resolution (CRDT-convergent vs server-authoritative / LWW) · offline-*write* (mainstream engines increasingly decline it).
- **Conformance sub-axis (orthogonal, § 4):** checked/validated {W3C QA, OWASP ASVS/MASVS, ISO-27560} —|— certified/awarded {CC-PP/ISO-15408, FedRAMP, eIDAS-accredited EUDI, IDS certification}.
- **App-class nodes → edges to families:** read off Figure 1 / Appendix B.
- **PNA node → edges:** **Substrate** ◐ partial {local-primary, downstream-mirror — no CRDT live-sync} · **Sovereignty** {ownership, privacy-default, least-authority, confidentiality} · **Verification** {typed contracts, checked-by-code, *checked-not-awarded*, layered derive-and-extend} · **Disclosure** {channel choice, payload preview, human-in-the-loop, LLM/MCP-as-transport} · **Adversary** cross-cut {Exception + Harden}; **leaves:** contact-vs-relationship two-store split · governed egress of relationship data · Exception + "Harden" honest-deviation model · the personal-network root.

---

## Appendix B — the reference × behaviour-family matrix, and the annotated citation map

**The coded corpus (what the placement claims rest on).** The 96-reference survey — coded behaviour-by-behaviour and scored ● strong / ◐ partial / · none across the adopted families — lives alongside this paper as machine-readable companions:

- [`figures/behaviour-matrix.md`](figures/behaviour-matrix.md) — the full **reference × behaviour-family matrix** (96 references × Substrate · Sovereignty · Verification · Disclosure, plus the Adversary cross-cut; PNA is the last row).
- [`figures/behaviour-vocabulary.md`](figures/behaviour-vocabulary.md) — the **26 canonical behaviours** (B01–B26), the emergent families, and the bottom-up reconciliation: how the hypothesised four became the adopted four (Assurance + Verification merged into **Verification**; **Disclosure** added; threat-modelling a cross-cut).
- [`figures/references.json`](figures/references.json) / [`figures/references.csv`](figures/references.csv) — the raw coded corpus.
- [`figures/figures.md`](figures/figures.md) — Figures 1–2 (the condensed matrix and the composite-group convergence).

**Annotated citation map** *(URLs web-verified across the survey's two rounds, 2026-06-14 and 2026-06-23; grouped by the adopted families of § 3 — the old "Assurance / protection" group is dissolved, its entries redistributed below).*

**Substrate**
- Kleppmann, Wiggins, van Hardenberg, McGranaghan, "Local-first software," Onward! 2019 — https://www.inkandswitch.com/essay/local-first/ · ACM https://dl.acm.org/doi/10.1145/3359591.3359737 · PDF https://www.inkandswitch.com/essay/local-first/local-first.pdf
- "Local-first software" (canonical 7-ideals summary) — https://en.wikipedia.org/wiki/Local-first_software
- Tonsky, "Local, First, Forever" — https://tonsky.me/blog/crdt-filesync/
- CRDT.tech — https://crdt.tech/ · implementations https://crdt.tech/implementations
- Automerge — https://automerge.org/ · Yjs — https://yjs.dev/ (https://github.com/yjs/yjs)

**Sovereignty**
- Solid — https://solidproject.org/TR/protocol · https://github.com/solid/specification
- AT Protocol — https://atproto.com/ · Kleppmann et al., "Bluesky and the AT Protocol," arXiv 2402.03239 — https://arxiv.org/abs/2402.03239
- Nostr (NIPs) — https://github.com/nostr-protocol/nips
- Matrix spec — https://spec.matrix.org/ · https://github.com/matrix-org/matrix-spec
- ActivityPub (W3C Rec) — https://www.w3.org/TR/activitypub/
- W3C DIDs v1.1 — https://www.w3.org/TR/did-1.1/ (self-controlled identity)
- Object-capability model (least-authority) — https://en.wikipedia.org/wiki/Object-capability_model (Miller, "Robust Composition," 2006)
- Data Transfer Initiative (Data Transfer Project) — https://dtinit.org/ (portability as an instrument of sovereignty)
- GDPR Art. 20 — https://gdprhub.eu/Article_20_GDPR · DMA↔GDPR — https://dtinit.org/blog/2025/12/02/dma-gdpr-joint-guidelines

**Verification**
- W3C Verifiable Credentials Data Model v2.0 — https://www.w3.org/TR/vc-data-model-2.0/ (the two-independent-implementations conformance gate — the rigorous *checked-not-awarded* exemplar)
- Model Context Protocol — https://modelcontextprotocol.io/ · spec https://github.com/modelcontextprotocol/modelcontextprotocol · announcement https://www.anthropic.com/news/model-context-protocol (typed wire contract; its consent model also anchors Disclosure)
- BDD / Cucumber / Gherkin — https://cucumber.io/docs/bdd/ · https://cucumber.io/docs/gherkin/
- GitHub Spec Kit — https://github.com/github/spec-kit · https://github.com/github/spec-kit/blob/main/spec-driven.md
- arXiv 2602.00180, "Spec-Driven Development: From Code to Contract…" — https://arxiv.org/abs/2602.00180
- OWASP ASVS — https://owasp.org/www-project-application-security-verification-standard/ · OWASP MASVS — https://mas.owasp.org/MASVS/
- Design by Contract — Meyer — https://se.inf.ethz.ch/~meyer/publications/old/dbc_chapter.pdf

**Disclosure**
- UCON-ABC usage control — Park & Sandhu — https://profsandhu.com/journals/tissec/ucon-abc.pdf
- Declassification dimensions — Sabelfeld & Sands — https://link.springer.com/chapter/10.1007/978-3-642-11957-6_5
- ISO/IEC TS 27560:2023 consent records/receipts — https://w3c.github.io/dpv/guides/consent-27560 · arXiv 2405.04528 https://arxiv.org/abs/2405.04528
- AI-egress governance: OWASP AISVS, AIUC-1, OpenID for Verifiable Presentations, IDS-RAM usage control — cited in §§ 3, 5 (the matrix codes each).

**Threat modeling (the cross-cut)**
- LINDDUN — https://linddun.org/
- Threat-modeling methods (STRIDE, attack trees, …) — CMU SEI — https://www.sei.cmu.edu/blog/threat-modeling-12-available-methods/
- NIST Cybersecurity Framework 2.0 — https://www.nist.gov/cyberframework · NIST Privacy Framework — https://www.nist.gov/privacy-framework

**Conformance model (the checked-vs-awarded sub-axis, § 4)**
- W3C QA Framework — Specification Guidelines https://www.w3.org/TR/qaframe-spec/ · Operational Guidelines https://www.w3.org/TR/qaframe-ops/ · Test Guidelines https://www.w3.org/TR/2003/WD-qaframe-test-20030516/
- Common Criteria Protection Profile / ISO 15408 — https://en.wikipedia.org/wiki/Protection_Profile · https://www.commoncriteriaportal.org/

**The composite group (§ 6)**
- EUDI Wallet Architecture and Reference Framework — https://eu-digital-identity-wallet.github.io/eudi-doc-architecture-and-reference-framework/
- International Data Spaces RAM 4.0 (IDS-RAM) — https://docs.internationaldataspaces.org/ids-knowledgebase/ids-ram-4
- Inrupt Enterprise Solid Server / Solid — https://docs.inrupt.com/ · https://solidproject.org/

**PNA spec & internal companions**
- PNA spec — [`spec/PNA_Spec.md`](../../spec/PNA_Spec.md) · axes — [`spec/axes.md`](../../spec/axes.md)
- Prior-art survey (Paper 2 seed) — [`docs/PriorArt.md`](../PriorArt.md) · [`docs/PriorArtReferences.md`](../PriorArtReferences.md)
- Coded survey corpus — [`figures/behaviour-matrix.md`](figures/behaviour-matrix.md) · [`figures/behaviour-vocabulary.md`](figures/behaviour-vocabulary.md) · [`figures/references.json`](figures/references.json)
- Source synthesis — [`brainstorms/2026-06-14-pnt-direction-grill.md`](../../brainstorms/2026-06-14-pnt-direction-grill.md)

---

*Skeleton ends. Expansion notes for the drafter: (1) Figures 1–2 are generated ([`figures/figures.md`](figures/figures.md), rendering [`figures/figure-2.svg`](figures/figure-2.svg)); the full derives-from directed graph (Appendix A) is still future work; (2) for Finding 2, add a side-by-side table of "ideal vs. enforced-by-engine?" with per-engine citations; (3) confirm each W3C/ISO URL resolves to the version you cite at submission time; (4) keep every leverage/underserved sentence flagged as a wager.*
