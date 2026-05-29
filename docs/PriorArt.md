# Prior Art Survey: Generative Application Class Blueprints

This document surveys the landscape of related work to the Personal Network Toolkit (PNT) — specifically, prior art for what we are calling a *generative application class blueprint*: a machine-readable specification, designed primarily for AI agents to consume, that defines what makes an instance of a *class* of applications correct, and against which many valid implementations can attest conformance.

The survey was conducted as a conversation with Claude (Anthropic) in May 2026, working through three angles: (1) what the agentic-coding industry is publishing in this space, (2) what protocol/standards bodies are doing for analogous "spec a class of artifact" problems, and (3) what production AI app-builders (Lovable, Replit, Bolt, v0) are doing internally that has become public through documentation or leaked system prompts.

The finding is that **no published artifact occupies the same position as PNT**. The closest analogs are either *evaluative* rather than *generative*, *per-project* rather than *per-application-class*, or *stack-coupled* rather than *architecture-coupled*. This justifies continued investment in PNT as a distinct category of artifact.

> **Scope of this document.** This is the *survey* — prose that positions PNT and argues its novelty, citing only the references that do circumscribing work (the closest analogs and conceptual ancestors). The complete annotated source list, including the background and development reading behind the survey, lives in [`PriorArtReferences.md`](./PriorArtReferences.md).

## Status
First version - May 23 2026 - [Rich and Claude learn from prior art](https://claude.ai/share/df001d9f-e700-4b8e-be4e-b28470f7f5cf) - define the class of work.

## Working definition

A **generative application class blueprint** has four properties:

1. **Generative** — primarily designed to be read by builders (AI agents) producing new applications, not by auditors evaluating finished ones.
2. **Application-class-scoped** — defines requirements for a *category* of applications (e.g. "personal network applications"), not for a single specific application or a single organization's house style.
3. **Multi-flavor** — admits multiple valid configurations (axis picks, slot choices, profiles) such that many legitimately different implementations can attest conformance.
4. **Machine-checkable** — load-bearing requirements are expressed as typed contracts (JSON Schema, OpenAPI, SQL DDL, TypeScript interfaces) so an agent can verify satisfaction at build time, not just at runtime.

PNT meets all four. Most prior art meets one or two.

## Findings by category

Five neighborhoods of related work, each surveyed for how close it comes to PNT's quadrant. Each inline citation names the *boundary-setting* analog for that neighborhood; the full source roster is in [`PriorArtReferences.md`](./PriorArtReferences.md).

### 1. Spec-Driven Development tooling — *closest in mechanism*

The consolidated 2026 methodology where a human (with AI help) authors a spec and agents implement against it. The mechanism is PNT's too — specs as contracts agents read — but every instance is *per-project*. The sharpest analog is **[GitHub Spec Kit](https://github.com/github/spec-kit)**, whose `constitution.md` holds "immutable principles that govern how specifications become code": structurally that is PNT's universal architectural commitments, except each project writes its own constitution and there is no library of pre-built constitutions for application *classes*. The rest of the field — Kiro, OpenSpec, BMAD-METHOD, Tessl, Google Antigravity, and the academic framing in Piskala's 2026 SDD paper — shares the same per-project scoping (rostered in the references file).

**Proximity:** Adjacent in mechanism, different in scope. PNT lifts the same spec-as-contract idea up one level, from project to application class.

### 2. AI app-builders — *closest in deployment mechanism, but stack-coupled*

Commercial app-builders (Lovable, Replit, Bolt, v0) already encode build rules into agents — but at the *stack* layer, not the application-class layer. The leaked **[Lovable system prompt](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/blob/main/Lovable/Agent%20Prompt.txt)** is the clearest empirical record: a fixed React + Vite + Tailwind + shadcn/ui + Supabase stack plus a list of architectural MUSTs, with no domain-specific layer. The closest *mechanism* PNT could slot into is **[Replit Enterprise's `custom_instruction`](https://docs.replit.com/teams/custom-templates)** — a per-organization instructions file injected into the agent's system prompt; it would accept a PNT-shaped artifact with little reshaping, though its scope is the org's house style rather than a class of apps. (The broader leaked-prompt collections and the official prompting handbooks are in the references file.)

**Proximity:** Informative on rule *shape*; adjacent as a deployment surface. Stack-coupled, not class-coupled.

### 3. Conformance test suites & contract testing — *the evaluative mirror*

Mature, per-class specifications do exist — but they *validate finished artifacts* rather than guide construction, the exact inverse of PNT's build-time workflow. The strongest domain match is the **[Solid Conformance Test Harness](https://github.com/solid-contrib/conformance-test-harness)** (decentralized personal data, ecosystem interop) — but it pokes finished servers from the outside. The closest mature *attestation* model is **[HL7 FHIR's CapabilityStatement](https://www.hl7.org/fhir/capabilitystatement.html)**, where each implementation publishes which profiles and operations it supports — structurally PNT's axis-pick attestation. And the closest *practice* to PNT's evaluate flow is **[Pact](https://pact.io)**'s consumer-driven contract testing: verify that an implementation honors its contract, which PNT re-creates at the AC level. Contact-data standards (CardDAV / vCard) are domain-relevant; the supporting vocabulary and harnesses (EARL, ITB, xAPI, NIST) are in the references file.

**Proximity:** Same end-goal (interop across many implementations of one spec), opposite workflow. PNT borrows the attestation and spec-annotation patterns, not the live-server testing model.

### 4. Architecture standards & Protection Profiles — *the conceptual ancestor*

The pre-AI pattern of "a spec for a *class* of products" lives in standards bodies. The closest mature precedent is the **[Common Criteria](https://www.commoncriteriaportal.org/) Protection Profile / Security Target model** (ISO/IEC 15408): a Protection Profile states the requirements for a category of products, and each product publishes a Security Target declaring how it conforms. That is precisely PNT's shape — the PNA Spec plays the Protection Profile, each design's Architecture document plays the Security Target. **[OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)** contributes the level-based attestation idea ("this app is Level 2 conformant"). Other architecture frameworks (IEEE 1471 / ISO 42010, TOGAF, NIST SP 800-160, GAMP 5, SLSA) are prose-oriented or solve adjacent problems, and sit in the references file.

**Proximity:** Conceptual ancestor. PNT keeps its own vocabulary, but the Protection-Profile-plus-Security-Target structure is the mature precedent for class-spec-plus-implementation-attestation.

### 5. Adjacent but out of frame — *agent benchmarks, MCP conformance, local-first*

Three neighborhoods worth ruling in or out explicitly:

- **Coding-agent benchmarks** (SWE-bench, Terminal-Bench, and the like) measure *whether an agent can code*, not whether the resulting app conforms to a class blueprint — distant. Tellingly, when Anthropic needed a conformance target for its multi-agent C-compiler build, it reached for the *existing* C conformance suite rather than authoring one — the same instinct PNT formalizes for an application class.
- **MCP conformance** is in progress (an [open request](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1990) and a [roadmap item](https://modelcontextprotocol.io/development/roadmap)); it's adjacent because PNT's canonical MCP servers implement the protocol, but it is *protocol* conformance, not application-class conformance.
- **Local-first software** is the domain PNT lives in: the **[Ink & Switch "local-first" essay](https://www.inkandswitch.com/local-first/)** defines the seven ideals PNT's ACs operationalize for contact data. The CRDT/sync substrates (Automerge, ElectricSQL, and friends) are build-time options, not blueprints (references file).

**Proximity:** Background and adjacency, not overlap.

## Proximity matrix

| Artifact | Generative? | Class-scoped? | Multi-flavor? | Machine-checkable? | Overall proximity |
|---|---|---|---|---|---|
| **Personal Network Toolkit (PNT)** | ✓ | ✓ | ✓ | ✓ | — |
| GitHub Spec Kit constitution | ✓ | ✗ (per-project) | ✗ | partial | Adjacent |
| Replit Enterprise custom_instruction | ✓ | ✗ (per-org) | ✗ | ✗ | Adjacent (mechanism only) |
| Lovable system prompt | ✓ | ✗ (stack-coupled) | ✗ | ✗ | Informative |
| Solid Conformance Test Harness | ✗ (evaluative) | ✓ | partial | ✓ | Informative (mirror) |
| HL7 FHIR + CapabilityStatement | ✗ (evaluative) | ✓ | ✓ | ✓ | Closest mature analog |
| Pact (consumer-driven contracts) | ✗ (evaluative) | ✗ (per-contract) | partial | ✓ | Adjacent (mechanism) |
| xAPI LRS Conformance Suite | ✗ (evaluative) | ✓ | partial | ✓ | Informative |
| Common Criteria Protection Profile | ✗ (evaluative) | ✓ | ✓ | partial | Conceptual ancestor |
| OWASP ASVS | ✗ (evaluative) | ✓ | ✓ (levels) | partial | Conceptual ancestor |
| CardDAV / vCard RFCs | ✗ (protocol) | ✓ | partial | ✓ | Domain-relevant |
| SWE-bench / Terminal-Bench | ✗ (evaluates agent) | ✗ | ✗ | ✓ | Distant |
| Anthropic evals methodology | ✗ (evaluates agent) | ✗ | ✗ | ✓ | Distant |

## Where PNT fits

PNT is positioned at the intersection of three trends that, as of this survey, have not yet been combined in any published artifact:

1. The **Spec-Driven Development** movement (Spec Kit, Kiro, BMAD, OpenSpec, Tessl, the 2026 SDD arXiv paper) has established that machine-readable specs targeted at AI agents are a productive layer. But all of its artifacts are per-project: the spec is written for one application by one team. PNT lifts the spec one level — to a *class* of applications — so the same spec can guide many implementations.

2. The **conformance test suite** tradition (Solid CTH, xAPI, FHIR, W3C, CC Protection Profiles) has long handled per-class specifications, but exclusively in *evaluative* mode: validate finished artifacts against the spec. PNT inverts the workflow: the spec is consumed at *build time* by agents producing the artifact, and the conformance check is satisfaction of typed contracts rather than runtime test pass/fail.

3. The **AI app-builder** ecosystem (Lovable, Replit, Bolt, v0) has built sophisticated agent-prompting machinery for guiding application construction, but exclusively at the *stack* layer: the system prompt encodes "build with React + Tailwind + Supabase," not "build something that behaves like a personal network application." The application-class layer remains in the model weights, not in any spec document.

PNT occupies the otherwise-empty quadrant: *generative + class-scoped + multi-flavor + machine-checkable*. This is the working definition of a generative application class blueprint.

## Conclusion

The survey confirms that no published artifact does exactly what PNT does. The closest mechanism (Replit Enterprise's `custom_instruction`, GitHub Spec Kit's `constitution.md`) is per-project or per-organization. The closest scoping (Solid CTH, FHIR, CC Protection Profiles) is evaluative rather than generative. The closest content (Lovable's system prompt) is stack-coupled rather than class-coupled.

PNT therefore continues as a distinct line of work. The specific architectural constraints of local-first applications operating on contact and relationship data — local execution, firewalled private data layer, SaaS-bridge ingestion, MCP composability, no remote authority — are not adequately captured by any generic per-project SDD tool or per-org template mechanism. A class-scoped blueprint with typed contracts is the right shape for this problem.

The artifacts surveyed remain useful as references:

- **GitHub Spec Kit's constitution model** — for the universal architectural commitments pattern.
- **Replit Enterprise's custom_instruction docs** — as a target deployment mechanism for PNT-shaped artifacts.
- **Lovable's leaked system prompt** — as empirical evidence of what kinds of rules are load-bearing for agents.
- **HL7 FHIR's CapabilityStatement** — as the most mature precedent for axis-pick attestation in a per-class spec.
- **Pact** — as the consumer-driven precedent for the contract-satisfaction check PNT's evaluate flow performs.
- **Solid's Conformance Test Harness** — as the source of the test-subject description and spec-annotation patterns.
- **Common Criteria Protection Profiles** — as the conceptual ancestor of class-scoped specs with implementation attestations.

These references inform PNT's design without constraining it to any of their workflows. For the complete catalog — including the background and development reading behind this survey — see [`PriorArtReferences.md`](./PriorArtReferences.md).
