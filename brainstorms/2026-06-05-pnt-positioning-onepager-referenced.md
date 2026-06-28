# Personal Network Toolkit — Positioning, Evidence-Checked (with references)
*Derived from the 2026-06-05 grill session. Empirical claims validated by two independent research agents and spot-checked against primary sources. Product/mission statements are positioning, not factual claims, and are left as-is. Where evidence is contested, the claim is hedged or reframed rather than dropped.*

---

## Mission (headline — positioning, not a factual claim)
**Improve the health of your personal networks — the communities with you at the center.**

## What PNT is (positioning)
The **open recipe** for building local-first apps that turn your contacts into **private relationship memory you own** — a spec + reference designs + MCP servers + lint + an agent skill. An AI agent builds a conformant app, or validates one it didn't build, against typed, checkable contracts.

> **PNT doesn't ship the app. It makes the app prove it protects your data.** *(A home-cooked meal — and we open-source the recipe.)*

---

## The problem — restricted to what the evidence actually supports

### Pillar 1 — Reaching the people you rely on is a *mental-health* issue **[well-supported, with one important nuance]**
Social connection is among the most robustly health-protective factors in population health: a 148-study meta-analysis found ~50% greater survival odds for people with stronger relationships [1]; isolation, loneliness, and living alone independently predict mortality [2]; and the US Surgeon General [3] and a 2025 WHO Commission [4] now treat disconnection as a population-health priority (WHO links it to ~871,000 deaths/year).

**The honest nuance — and it actually helps you.** The newest, most rigorous causal work (genetic / Mendelian-randomization on 476k people) finds loneliness is **mostly a surrogate marker, not a direct cause, for physical disease** — the causal signal that survives is concentrated in **mental-health and behavioral** outcomes (depression, substance use, sleep) [5]. That is exactly where PNT operates. So: claim the **mental-health** pathway with confidence; do **not** claim "social isolation causes heart disease/cancer/death like smoking" as a *causal* statement.

Help-seeking also drops as depression deepens, and the *perceived availability* of someone to reach is itself protective [6] — which is precisely the friction PNT attacks (and matches the crisis story). *(One caveat to respect: "I'd rather handle it myself" is among the most common help-seeking barriers — a frictionless "who do I call" tool helps the reachability problem, not the autonomy-preference one.)*

### Pillar 2 — Platforms bury your strong ties in noise **[well-supported]**
Passive feed/broadcast consumption is linked to *lower* wellbeing, while *targeted contact with close ties* raises it — the platform's broadcast surface is the harmful part; the strong-tie channel is the good part [7][8]. And people accumulate far more nominal contacts than they can actually maintain, in nested layers of closeness [9]. *(Cite the contacts-vs-maintainable **gap**, which is robust — not "Dunbar's number = 150," whose exact value is contested [10].)*

### Pillar 3 — Lock-in and loss are real and documented **[well-supported]**
Facebook's data export hands you friends' **names but not their email/phone — by design**, preserving the social graph as a competitive moat; the one thing you'd need to rebuild your network elsewhere is the one thing withheld [11]. Account bans and platform exits sever relationships that live only on-platform. *Own the tension:* part of why platforms withhold a contact's info is **legitimate third-party privacy** — and a PNA exports that info too. PNT's answer is **sovereignty + consent**, not pretending the tension away.

### Pillar 4 — In local-first, this corner is under-explored **["underserved" supported; "highest-leverage" is a stated bet]**
The founding local-first manifesto and the curated community indexes center **sync, CRDTs, and storage**, with essentially **no personal-contact / relationship-application category** [12]. "Underserved" is well-triangulated. "**Highest-leverage**" is your **wager**, not a measured fact — leverage = (value if solved) × (neglectedness), and the value term rests on the mental-health evidence above. State it as a bet — which "come break the thesis" already invites.

### The timely hook — the AI-OS is arriving **[real trend; not yet mature]**
OS-level agentic AI is shipping, not just demoing (Anthropic Computer Use; OpenAI Operator; a 2025 ACL survey of OS-using agents) [13]. Cite it as a **direction**, not an accomplished outcome — which makes *"where does the AI operate on your relationship data"* a now-question, not a someday-question.

---

## What we deliberately do NOT claim (the credibility shield for a "break the thesis" room)
Pre-empt the four attacks a skeptical dweb audience will reach for first:
1. **Not** broad physical-disease causation — genetic evidence narrows the causal claim to mental health [5].
2. **Not** community-scale "wellbeing contagion" — the spread-through-networks claims are confounded by homophily and weakest for mood states [14]. Keep "*your own* network predicts *your* wellbeing."
3. **Not** "Dunbar's number = 150" as fact — the constant is deconstructed [10]; the *gap* is what's real.
4. **Not** "can only help" — relationship tooling can instrumentalize intimacy, normalize surveillance-of-friends, and induce its own anxiety [15]. (You already walked this back to "*likely* to help" — keep that hedge in public copy.)

---

## Door A — revised thesis (evidence-safe, still a fight-pick)
> Reaching the people you actually rely on is a **mental-health** problem, not just a privacy one — and it's the most under-explored corner of local-first. The evidence is strongest exactly where it counts: isolation and stalled help-seeking harm mental health, and *feeling someone is reachable* is itself protective. Yet the platforms that hold your relationships **bury your closest ties in noise**, **withhold the contact info** you'd need to reach them elsewhere, and can **lock you out overnight**.
>
> If you believe people should be able to **keep and use** the relationships they rely on — for life, out of reach of anyone who'd sell or lock them — let's build the tools that make it safe. I'm claiming this is the **highest-leverage place to work in local-first. That's a bet, not a proof — so come break the thesis.**

**Supporting slide — the quartet (unchanged; your strongest line):** *Solid asks where personal data can live. AT Protocol asks how social records interoperate. JSContact asks how contact cards should be represented. **PNAs ask what guarantees an app must make when it turns contact data into private relationship memory.***

## Door B — builder (README, cold read; unchanged)
> Personal Network Toolkit is a spec + reference designs + MCP servers + lint + an agent skill for building local-first apps that turn contact data into private relationship memory the user owns. An agent builds a conformant app — or validates one it didn't build — against typed, checkable contracts. It doesn't ship the app; it makes the app prove it protects your data.

---

## References
1. Holt-Lunstad, Smith & Layton (2010). *Social Relationships and Mortality Risk: A Meta-Analytic Review.* PLoS Medicine. https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1000316
2. Holt-Lunstad et al. (2015). *Loneliness and Social Isolation as Risk Factors for Mortality.* Perspectives on Psychological Science. https://journals.sagepub.com/doi/full/10.1177/1745691614568352
3. U.S. Surgeon General (2023). *Our Epidemic of Loneliness and Isolation.* HHS. https://www.hhs.gov/sites/default/files/surgeon-general-social-connection-advisory.pdf
4. WHO Commission on Social Connection (2025). *From loneliness to social connection.* https://www.who.int/news/item/30-06-2025-social-connection-linked-to-improved-heath-and-reduced-risk-of-early-death
5. Liang et al. (2024). *Observational and genetic evidence disagree on the association between loneliness and risk of multiple diseases.* Nature Human Behaviour. https://www.nature.com/articles/s41562-024-01970-0
6. Wang et al. (2018). *Social support and mental health: structural/functional factors, perceived support and help-seeking* (review). https://pmc.ncbi.nlm.nih.gov/articles/PMC8367349/
7. Verduyn et al. (2015). *Passive Facebook Usage Undermines Affective Well-Being.* Journal of Experimental Psychology: General. (DOI 10.1037/xge0000057)
8. Burke & Kraut (2016). *The Relationship Between Facebook Use and Well-Being Depends on Communication Type and Tie Strength.* Journal of Computer-Mediated Communication. https://academic.oup.com/jcmc/article/21/4/265/4161784
9. Mac Carron, Kaski & Dunbar (2016). *Calling Dunbar's Numbers.* Social Networks. https://arxiv.org/abs/1604.02400
10. Lindenfors, Wartel & Lind (2021). *'Dunbar's number' deconstructed.* Biology Letters. https://royalsocietypublishing.org/doi/10.1098/rsbl.2021.0158
11. EFF — Doctorow & Gebhart (2018). *Facing Facebook: Data Portability and Interoperability Are Anti-Monopoly Medicine.* https://www.eff.org/deeplinks/2018/07/facing-facebook-data-portability-and-interoperability-are-anti-monopoly-medicine
12. Kleppmann, Wiggins, van Hardenberg & McGranaghan (2019). *Local-first software: you own your data, in spite of the cloud.* Ink & Switch. https://www.inkandswitch.com/essay/local-first/
13. Hu et al. (2025). *OS Agents: A Survey on MLLM-based Agents for General Computing Devices Use.* ACL 2025. https://arxiv.org/abs/2508.04482  ·  Anthropic (2024), *Computer use.* https://www.anthropic.com/news/3-5-models-and-computer-use
14. Shalizi & Thomas (2011). *Homophily and Contagion Are Generically Confounded in Observational Social Network Studies.* Sociological Methods & Research. https://arxiv.org/abs/1004.4704
15. Danaher, Nyholm & Earp (2018). *The Quantified Relationship.* American Journal of Bioethics. https://pubmed.ncbi.nlm.nih.gov/29393796/
