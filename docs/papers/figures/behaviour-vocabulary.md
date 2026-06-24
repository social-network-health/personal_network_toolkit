# Behaviour vocabulary & emergent families — Paper 1

> Generated from the behaviour-extraction pipeline (task wvye4lijn): 96 references coded, 26 canonical behaviours, 6 emergent families.

## Emergent families (bottom-up — did NOT match the hypothesised four)

> **Reconciliation:** The emergent families DO NOT cleanly match the hypothesised four (Substrate, Sovereignty, Assurance, Verification). The honest result is: two of the four hold strongly, the third is thin, the fourth nearly collapses, and a large fifth family emerges that the four-way scheme does not name.  What matches: Substrate (B01-B05, B13) and Sovereignty (B06-B08, B14-B17) are robust, well-populated clusters that survive the merge intact and correspond closely to the hypothesis.  Where it strains: 1) ASSURANCE and VERIFICATION blur together and are both thin. The hypothesis treats them as peer families, but the corpus splits the assurance idea by *who is checking*: Assurance-as-self-proof (typed contracts, code-verified conformance, layered spec — B09/B10/B11) is about the builder demonstrating its own behaviour, while Verification-as-independent-confirmation reduces to a SINGLE behaviour, tamper-evident integrity (B12). A family of one is a sign the hypothesised Assurance/Verification split is finer than the evidence supports. A defensible alternative is to MERGE them into one "Assurance/Verification" family (B09-B12): checkable guarantees, whether self-attested or relying-party-confirmed.  2) A genuinely DISTINCT fifth family emerges that the four do not capture: DISCLOSURE / runtime egress governance (B18-B24, B26). This is the largest cluster after Substrate+Sovereignty and is qualitatively different from all four hypothesised families — it is neither about where data rests (Substrate), nor static control posture (Sovereignty), nor proving built behaviour (Assurance/Verification). It governs the *live moment of sharing*: preview, consent, receipts, priority-ordered policy, human-in-the-loop guards, and treating LLM/agent calls as egress. This strongly corresponds to the prompt's flagged candidate "a distinct honest-deviation / exception-handling family" — the runtime mediation/consent surface. It should be ADDED as a first-class family; folding it into Sovereignty would lose the build-time-vs-runtime distinction that the corpus clearly draws.  3) Threat-modelling (B25) is a stance/prerequisite rather than a behaviour peer; it sits adjacent to Disclosure and Sovereignty (it scopes their guards) and is reported as a small Adversary-modelling family rather than forced into one of the four.  Net recommendation: keep Substrate and Sovereignty; collapse Assurance+Verification into one checkability family (the Verification-as-separate hypothesis is not supported — it is a singleton); ADD a Disclosure/runtime-egress-governance family. So the four-family hypothesis is better described as: Substrate, Sovereignty, Assurance/Verification (merged), and Disclosure (added) — four again, but a different four than hypothesised, with threat-modelling as a thin cross-cutting fifth."

| Family | Behaviours | Gloss |
|---|---|---|
| **Substrate** | B01, B02, B03, B04, B05, B13 | Where the data lives and how it moves: local-primary residence, offline use, conflict-free background sync, lock-in-free migration, portable export, and federation over a published wire contract — the local-first storage/replication/interop layer. |
| **Sovereignty** | B06, B07, B08, B14, B15, B16, B17 | Who controls access and identity: owner-controlled access authority, privacy-by-default, confidentiality/encryption, explicit least-authority grants, self-controlled identity, authentication, and public/private visibility — the user's standing as the authority over their data. |
| **Assurance** | B09, B10, B11 | How the system proves its own behaviour as built: typed/declarative contracts, code-verified conformance, and a layered derive-and-extend spec — machine-checkable guarantees about the application itself. |
| **Verification** | B12 | How a relying party independently confirms data has not been altered: tamper-evident integrity via signing/hash-chaining — trust without trusting the holder. |
| **Disclosure** | B18, B19, B20, B21, B22, B23, B24, B26 | Governance of the live act of sharing/egress: user-chosen channel, runtime capability negotiation, pre-send payload preview, informed consent, priority-ordered policy, auditable consent receipts, least-privilege/human-in-the-loop guards, and governed LLM/agent egress — runtime mediation of every outbound disclosure. |
| **Adversary-modelling** | B25 | Reasoning about who the system must defend against: explicit threat-modelling of the design — the prerequisite stance that scopes the guards in the other families. |

## Canonical behaviour vocabulary

| ID | Behaviour | Definition |
|---|---|---|
| B01 | Local-primary data residence | The authoritative copy of the data lives on the user's own device/store, owned and controlled by the user. |
| B02 | Offline operation | The application reads and works without a network connection. |
| B03 | Background sync with conflict-free convergence | Changes replicate in the background and concurrent edits converge without a central authority. |
| B04 | Provider migration without lock-in | The user can move to another provider/host while keeping their identity and data intact. |
| B05 | Portable, machine-readable export | Data can be exported in a portable, machine-readable format and is portable across applications. |
| B06 | Owner-controlled access authority | The data owner is the authority deciding who may access the data. |
| B07 | Privacy as default posture | Privacy is the default; data is not exposed unless deliberately shared. |
| B08 | Confidentiality / encryption at rest and in transit | Data is kept confidential, e.g. encrypted, and the transport cannot read message contents. |
| B09 | Typed / declarative contract for behaviour | Behaviour is expressed as a typed or declarative contract rather than implicit code. |
| B10 | Conformance verified by code, not prose | Conformance is established by executable checks/tests rather than asserted in prose. |
| B11 | Layered, derive-and-extend spec | The specification is layered so others can derive from and extend it. |
| B12 | Tamper-evident integrity | Data carries tamper-evident integrity via signing or hash-chaining. |
| B13 | Federation via published wire contract | Systems interoperate through a published wire contract / federation protocol. |
| B14 | Explicit least-authority grants | Access requires an explicit grant scoped to least authority. |
| B15 | Self-controlled, host-independent identity | The user holds a self-sovereign identity independent of any host. |
| B16 | Authentication required for access | Access requires authenticating the requester. |
| B17 | Public/private visibility distinction | Data distinguishes public from private visibility states. |
| B18 | User-chosen outbound channel | The user chooses the channel used for outbound sharing. |
| B19 | Runtime capability negotiation/discovery | Capabilities are negotiated or discovered at runtime. |
| B20 | Pre-send payload preview | The user previews the exact payload before it is sent. |
| B21 | Informed consent before disclosure | The user is shown what is disclosed and consents before any disclosure. |
| B22 | Priority-ordered policy | Policy rules are evaluated in an explicit priority order. |
| B23 | Auditable record / consent receipt | The system keeps an auditable record or consent receipt of disclosures and actions. |
| B24 | Runtime least-privilege / human-in-the-loop guards | Runtime guards enforce least-privilege and require a human in the loop. |
| B25 | Threat-modelled design | The design is explicitly threat-modelled. |
| B26 | Governed LLM/agent egress | An LLM or agent call over the data is governed like any other egress. |
