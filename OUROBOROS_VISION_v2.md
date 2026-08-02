# OUROBOROS

### Self-Auditing Governance That Starts at Community Scale and Grows Only by Consent

*Version 2.3, Genesis Project. Version 2.0 released 2026-06-15; amended 2026-08-01, 2026-08-02, and 2026-08-03 (see Appendix C).*
*Authored by Preston T. Winters with Claude (Anthropic)*
*Supersedes Version 1.0. Open for refinement, contestation, and improvement through the standard process the document describes.*

---

## §0: WHY THIS EXISTS

This document proposes governance architecture that begins at community scale and is intended to remain usable at any scale a population consents to. Before describing the architecture, I name the conditions that make a new architecture necessary. Those conditions are global. I write as an American because that is the case I can speak to with the most authority. The pattern I describe operates in different forms across most current systems of governance.

I am an American. The system I grew up in was designed to represent the public and increasingly does not. The two major parties have demonstrated, across decades and across administrations, that they are heavily influenced by lobbyists, donors, and concentrated industrial interests. Public trust has collapsed to historically low levels. Significant portions of each party's constituency now believe the other is operating in deeply corrupt frames; whether the specific accusations are true matters less than the fact that they are widely held. A governance system that has lost legitimacy this thoroughly is structurally unable to self-correct from within.

The captures are not abstract. The defense, healthcare, and agricultural sectors each operate with substantial lobbying capacity and direct relationships with the agencies that nominally regulate them. Approval processes, procurement, and policy frameworks are shaped in part by the entities they are supposed to constrain. This is not a partisan observation. The pattern holds across administrations and across both major parties.

Similar patterns appear in other democracies and in different forms in authoritarian systems: regulatory capture, elite consolidation, weakened independent oversight, and the increasing disconnection of policy from public preference. The American case is one well-documented instance of a global problem. Naming it specifically is a starting point, not a claim of unique severity.

The publicly-traded shareholder model of large-scale capital, as currently practiced, produces structural extraction incentives. Companies operating at planetary scale are governed under legal frameworks (notably Delaware-influenced corporate law) that treat shareholder-value maximization as the controlling norm. Returns flow to capital holders whose relationship to the enterprise is primarily financial, and the public-interest tradeoffs are systematically underweighted. The 2008 financial crisis, the opioid epidemic, well-documented patterns of climate-science suppression, and the surveillance-economy business model are familiar examples of this dynamic operating at scale.

We are also now confronting artificial intelligence at civilizational scale. The leaders of the major AI labs have publicly assessed the risk as serious. Dario Amodei, CEO of Anthropic, has stated in public interviews (Axios AI+ DC Summit, September 2025) that he places the probability of AI development going "really, really badly" at roughly 25%. Elon Musk has stated his probability at approximately 20%. Sam Altman of OpenAI, Demis Hassabis of Google DeepMind, Dario Amodei, and hundreds of other AI researchers and executives signed the 2023 Center for AI Safety statement that "Mitigating the risk of extinction from A.I. should be a global priority alongside other societal-scale risks such as pandemics and nuclear war."

These assessments come from the people building the systems. The architects of the technology are saying publicly that they cannot rule out outcomes that end or fundamentally degrade human civilization. Current governance systems are not equipped to evaluate, regulate, or coordinate around this class of risk on the timeline at which the technology is advancing.

The argument of this document is that humanity needs governance architecture able to grow with and keep pace with the technology reshaping the conditions of human life. The current systems cannot. Reforming them piecemeal will not be fast enough. A proposal for different architecture is therefore necessary, even if every individual proposal will be wrong in significant ways. This document is one such proposal. The goal is not to be adopted as written. The goal is to enter the conversation as serious work, contest other serious work, and contribute to whatever humanity actually builds.

The window is closing. Better governance will not arrive on its own. What replaces the captured systems will be built either deliberately, by people thinking honestly about what humanity needs, or by default through whoever moves first with the most resources. This document refuses the second path.

**On this version.** Version 1.0 described the architecture as a four-layer stack. Version 2.0 restructures the governance stack into two tiers with a sharper line between who is sovereign and who is instrumental, and it resolves the open items that the first version left standing. The diagnosis above is unchanged. The commitments below are largely unchanged. What changed is the shape of the machine that keeps the commitments. Appendix B records the change in full.

---

## EXECUTIVE SUMMARY

Ouroboros is a proposed architecture for self-auditing governance. It begins at the scale of a single consenting community and grows only by voluntary accession; it claims no authority over anyone who has not ratified it. Version 2.0 organizes it into two tiers standing on a shared foundation.

**Tier 1, the sovereigns: the Tribune and the People, co-equal.** The People are the franchise: one human, one vote. The Tribune is a single elected human office that brokers convergence among the lower tier and the People, initiates emergency response, holds a check on the lower tier, and represents the system externally. Neither sovereign sits above the other. The Tribune can slow, return, or force re-deliberation of the People's decisions, but the Tribune can never override the substantive will of the franchise, and the Tribune can never legislate, tax, allocate resources, or sanction alone.

**Tier 2, the triadic instrument: the Councils, the National AIs, and the Oversight.** Three peer branches in permanent tension, none of them sovereign, each checking the other two. The Councils are the human deliberative bodies. The National AIs are the per-community representative models. The Oversight is the twelve-member adversarial audit body (public name: Audit Consortia), operating under a nine-of-twelve quorum.

**The foundation: a personal companion for every human.** The companion is not a governance tier. It is the per-person cognitive infrastructure of the Baseline, the thing that makes the People's sovereignty real rather than nominal. It belongs to the person, it is aligned to the person, and it is never the engine's sensor.

The architecture binds nothing until the One-Vote Standard is operational, claims broad authority only over communities that voluntarily ratify, and sunsets every authorization it grants itself. Power moves through a single spine: a reversible pause that any one lower-tier branch can pull on a low bar, with reversal escalating to the People; and an emergency gate that pre-authorizes coercive action only on a high bar, graduated by how long and how reversible the action is. Standing with the governed is measured continuously through a Legitimacy Decay Index that drives Tribune election and recall. The canonical shape is a pentagon: two sovereigns, three branches, on a Baseline foundation.

The architecture commits to: universal human dignity, equal vote weight, civic Baseline (food, water, shelter, healthcare, education, energy, information access, and a personal memory layer for informed civic participation) as the precondition for meaningful democracy, structural opposition within and across the tiers, public principles with classified instances, automatic sunset of all powers, scheduled renewal cycles, and the principle that the system exists to prevent catastrophe rather than to optimize daily life, transition cost for automation-driven displacement borne by the party capturing the gain, and the engine paying the unsubsidized full cost of its own compute footprint with siting by local consent.

This document is Version 2.0. It names its own limits in the open and is built to be torn into and improved.

---

## I. PREAMBLE

This document holds a set of commitments to be defended. The commitments below carry inheritance from multiple wisdom traditions; Appendix A names them.

**Every human being is the bearer of dignity, irrespective of birth, nation, creed, capacity, or contribution.** Dignity is not granted by any government, corporation, or technology. It is recognized by them. A system which fails to recognize it has, in that failure, lost the right to govern.

**Humanity is plural.** Many traditions, many languages, many forms of life, many ways of being right. Governance that requires uniformity to function is not governance. It is conquest.

**The work of governance is to compound cooperation rather than extraction.** Coordination failures at scale produce predictable, repeating, and increasingly dangerous outcomes. The architecture below is built to make cooperative outcomes more available than extractive ones.

**Coordination at planetary scale is now possible for the first time in recorded human history.** This brings unprecedented opportunity and unprecedented danger. The opportunity is to address coordination failures (climate, pandemic, war, AI risk, mass deprivation) that no single nation can address alone. The danger is that the same coordination capacity, captured, becomes the instrument of tyranny without precedent. The architecture below is built around this danger.

**Artificial intelligence, deployed with care and constrained by humility, can serve as connective tissue for human cooperation. It cannot serve as substitute.** The line between connective tissue and substitute is the architecture's most important boundary. Version 2.0 draws that line by keeping every AI body in the lower tier, instrumental, never sovereign.

**The engine described herein is a floor, not a ceiling.** It exists to prevent catastrophe and protect the conditions under which human freedom and meaning are possible. It does not exist to optimize human life. The lives are ours to live.

**The engine acts under consent.** Under the broad regime, no part of the architecture has authority to act on humans without their consent at the relevant level. Communities ratify, and the engine binds only ratifying communities. Under the narrow emergency regime, the engine claims coordination authority over civilization-threatening risk categories specifically, justified by urgency and bounded by sunset, by the high authorization bar described in §VI, and by Reckoning-cycle revisitation. Cooperation is the default mode. Narrowly-scoped, urgency-justified coercion is the exception, named honestly rather than smuggled.

**Sovereignty is human and it is removable.** The two sovereigns are the People and a single human office. The office is never permanent and never unchecked: it is measured continuously against the governed, it is removable on sustained loss of standing, and it can act on no substantive matter alone. Power that cannot be measured and removed becomes power that captures itself.

**The engine must continually audit and renew itself, lest it become what it was built to prevent.** The renewal is structural and scheduled, not aspirational.

This document offers Ouroboros to anyone who would help build, refine, or replace it.

---

## II. FIRST PRINCIPLES

The following are non-negotiable. Any implementation of Ouroboros that violates these principles is not Ouroboros.

**0a. Provisional operation.** Ouroboros operates in provisional form until the One-Vote Standard is established (see §V). During the provisional period, the engine convenes, deliberates, and commissions; it does not bind. Exit from provisional status enables binding within ratified communities only. Exit from provisional status requires a functional One-Vote Standard verified by independent audit and ratified by initial-adopter populations.

**0b. Two-tier consent.** Ouroboros operates two distinct consent regimes.

The **broad regime** governs the engine's general authority: economic restructuring, civic commons funding, sanctions, justice administration, and all other ordinary engine action. The broad regime is **voluntary opt-in only**. The engine never binds non-ratifying populations under this regime regardless of One-Vote Standard status. Communities accede through demonstrated-outcome legitimacy; entrenched interests retain the right to refuse.

The **emergency regime** governs a narrowly-defined set of civilization-threatening risk categories: existential AI risk, pandemic infrastructure response, large-scale ecological collapse coordination, and other risks that meet the formal threshold of "credible threat to human civilization on a timeline shorter than broad-regime processes can address." Under the emergency regime, the engine claims coordination authority over the specified risk category. This means the authority to require participation in coordination protocols (information sharing, joint response, the minimum-coordination constraints that the joint response cannot function without), not the authority to direct internal policy of non-ratifying jurisdictions. **What the emergency regime can never reach.** Coordination authority runs to jurisdictions and institutions. It does not run to persons. The engine holds no authority, at any tier, under any invocation, over any person's body, movement, home, business, school, or place of worship. Quarantine, curfew, closure, medical mandate, travel restriction, and every other measure that acts on a person directly are outside the engine's power entirely and remain with whatever authority a community's own law assigns them. The engine may require that jurisdictions share information with each other, participate in joint response, and observe the minimum technical constraints without which a joint response cannot function. It may not require anything of a human being. This exclusion is not a policy of the engine and is not suspendable by any emergency finding; it is a limit on what the engine is.

The emergency regime is operationalized through the single crisis spine described in §VI: coercive emergency action takes effect only on the high authorization bar, it is time-bounded and sunset-by-default, its renewal escalates a tier, personal liability attaches to actors who invoke it under crises later determined to have been overstated, and every invocation is audited at the Reckoning.

The engine cannot expand the list of emergency-tier risk categories without supermajority ratification through the standard process. The threshold for what qualifies as "civilization-threatening" is itself a political object subject to ongoing contestation; this is intended, not accidental.

The asymmetry is deliberate: most reform can afford the slow path of consent, and the document accepts that bounded capital and other systemic restructuring may take decades. A small set of civilization-scale risks cannot afford that timeline, and the document accepts the legitimacy cost of narrow coercive authority on those risks specifically. The honest version of urgency is that some things are too dangerous to wait for unanimous consent, and the engine names that explicitly rather than smuggling coercion through "very strong incentives."

**1. Universal human dignity.** No human may be excluded from the protections of the engine on the basis of nation, creed, race, gender, orientation, ability, age, or any other category. Dignity is unconditional or it is nothing.

**2. One human, one vote.** No vote-weight differentials. No production-weighted voting. No property qualifications. No credential requirements. The franchise is the human, not the human's productivity, intelligence, virtue, or status. Civic contribution is incentivized through resources, recognition, and covenantal community, never through political authority. When manipulation of the information environment is detected, the Oversight publishes the finding and the Councils decide the response, which under §VII.b may extend a deliberation period, open an evidence review, or trigger a revote. No part of the engine quarantines a campaign or labels a source. The engine never responds by adjusting vote weights.

**3. The Baseline is the precondition for the vote.** Universal access to nutrition, water, shelter, healthcare, education, energy, and information is not separate from democracy. It is what makes democracy possible. A person who is hungry, sick, ignorant, or disconnected cannot meaningfully participate in self-governance. The Baseline is the engine's first commitment, and the personal companion is part of it.

**4. Adversarial structure within and across the tiers.** No part of Ouroboros may consist of a single voice acting unopposed. Within the lower tier, the three branches check one another. Across the tiers, the lower tier can pause the upper tier, and the two sovereigns check each other. No branch and no sovereign acts without a counterweight. Power that does not contend with itself becomes power that captures itself.

**5. Public principles, classified instances.** Every rule by which Ouroboros operates must be publicly stated in principle. For layers that produce reversible outcomes, specific signals and weights may be classified for security, but the kind of rule must always be describable to the public. For layers that produce irreversible outcomes, public-principles disclosure is more granular; the engine must name the factors it weighs even if not the values it assigns. A rule that cannot be named in principle is not a legitimate rule.

**6. Sunset by default.** Every authorization, emergency power, and law expires automatically. Sunset reaches grants of power and does not reach the limits on what the engine may never do: the §V prohibitions and the exclusion of persons from coordination authority are statements of what the engine is, not powers it holds, so there is nothing in them to expire. Renewal requires fresh deliberation through the standard process. Permanence must be earned, repeatedly, against evidence. Never assumed.

**7. Scheduled renewal.** Every five years, the engine conducts the Reckoning: a structured public audit of itself with mandatory amendment cycles. Continuous controls (quarterly audits, incident disclosures, recall mechanisms) supplement the major cycle. The Reckoning is the renewal mechanism. Without it, the engine drifts. With it, the engine returns to itself.

**8. Floor, not ceiling.** Ouroboros prevents catastrophe and protects the conditions of meaning. It does not optimize daily life. It does not eliminate struggle. It does not solve the human question. The lives lived within those conditions are not the engine's to direct.

**9. Co-equal human sovereignty.** The Tribune and the People are co-equal. Neither sits above the other. The Tribune's check on the People is procedural only: the office can slow, return, or force re-deliberation, but it cannot override the substantive will of the franchise. The Tribune holds no substantive power alone; legislation, taxation, resource allocation, and sanction each require the People and the lower-tier process. When the Tribune and the People agree, that agreement is supreme and nothing in the lower tier may veto it. And a sovereign's exercised judgment is overturned only by the other sovereign, never by the instrument: the lower tier may pause and escalate, but only the People can reverse a deciding Tribune.

**10. Legitimacy is measured, not assumed.** Standing with the governed is measured continuously, not inferred from the fact of holding office. The Tribune office is bound to a Legitimacy Decay Index; sustained loss of standing triggers a fresh election, and a sharper loss triggers recall. Every lower-tier branch and member is subject to recall without dissolving the whole tier. No office is owed its tenure.

---

## III. ARCHITECTURE

Ouroboros is two tiers standing on a Baseline foundation. The canonical diagram is a pentagon: two sovereigns at the top, three branches below them, with the personal companion as the ground the pentagon stands on.

The restructure from Version 1.0's four-layer stack exists to draw one line sharply: the line between who is sovereign and who is instrumental. In Version 2.0, only humans are sovereign. Every AI body sits in the lower tier as instrument. This is the architecture's answer to its own most important boundary, the line between connective tissue and substitute.

### The Foundation: The Personal Companion

Every human, by right, has access to a personal companion supporting their cognitive participation in civic life. The companion is not a tier of government. It is the per-person infrastructure of the Baseline, and it sits beneath both tiers because it belongs to the person, not to the engine. It is the thing that makes one-human-one-vote a real franchise rather than a formal one: a person who cannot access information, retain context across the timescales civic decisions require, or draw on personalized cognitive support is structurally excluded from self-governance, and the companion is how the engine refuses that exclusion.

The companion architecture serves four functions:

- **Education and information access:** the democratization of knowledge, available to every person regardless of geography or wealth.
- **Personal memory and continuity:** a private, encrypted, user-owned memory architecture, so each person's AI does not forget them.
- **Civic deliberation partner:** when proposals come up for vote, the companion helps the person understand, simulate outcomes, examine tensions, and arrive at their own deliberated position. The companion works for the human, not for the engine.
- **Health Baseline support:** triage and routing, mental-health companionship and distress detection, chronic-condition management, diagnostic support paired with human clinicians, and personalized treatment guidance that grows in confidence over time. The companion retrains on current medical data on a regular cadence and operates within a strict scope of practice. It does not prescribe controlled substances, replace specialist diagnosis for serious conditions, or substitute for human clinicians in mental-health crisis.

The companion operates in four explicit privacy modes, with the user in control of mode selection:

- **Local-private mode (default):** all inference local-only. No data leaves the device. Conversations are encrypted at rest with user-controlled keys.
- **Consented-clinical mode:** activated by the user when they want clinician escalation. Specific health signals are shared with named human clinicians under standard medical privacy frameworks.
- **Emergency-escalation mode:** activated only by user-defined triggers (suicidality, acute medical event, abuse disclosure with user pre-consent). Routes to specified human responders. Triggers, thresholds, and escalation paths are user-configurable and transparent.
- **Civic-deliberation mode:** activated when the user is participating in engine governance. Aggregate signals (vote was cast, deliberation was conducted) are shared with the civic platform. Content of deliberation never leaves local mode.

The companion's alignment is to the user's stated values, except that emergency-escalation crisis triggers (acute suicidality, life-threatening medical events, child-safety concerns whether disclosed by a user about themselves or surfaced through other channels) operate as floor; user customization narrows but cannot eliminate them. The vote that emerges from a deliberation with one's companion is the human's vote, deliberated, unmanipulated.

The architecture is implementable by any number of providers. The engine actively encourages plurality, portability of personal memory between providers, independent audits, and adversarial second-opinion companions.

The companion never reports content upward and is never the engine's sensor. The single exception is narrow and user-controlled: in civic-deliberation mode, the consented, aggregate, content-free signal (a vote was cast, a deliberation occurred) flows to the civic platform, never to the governance tiers, and never the substance of what was discussed. The companion and the civic platform are two different things. The companion is private and local and belongs to the person; the civic platform is the separate certified surface where the consented civic act is recorded. The engine's legitimacy measure (the Legitimacy Decay Index) and its manipulation-detection read from the civic platform and from public behavior, never from inside anyone's companion. This boundary is load-bearing: the moment the companion serves the engine rather than the person, the line between connective tissue and substitute has been crossed.

### Tier 1: The Sovereigns

Tier 1 is two co-equal human sovereigns: the People and the Tribune. Sovereignty in Ouroboros is human and only human. The lower tier serves; it does not rule.

#### The People

The People hold the franchise: one human, one vote, with the One-Vote Standard as the precondition for a ballot being counted (see §V).

**Who "the People" are is set by the ratifying community, not by the engine.** One-human-one-vote is a rule about *weight*, forbidding any vote from counting for more than any other. It is not a claim about membership. Each ratifying community defines its own roll through its own lawful process, and the engine binds itself to whatever that community decides: residency, citizenship, or another standard entirely. The engine holds no position on the question and claims no power to settle it. Where a ratifying community sits inside a larger jurisdiction with its own franchise rules, engine participation neither confers nor removes any standing in that jurisdiction's elections, and the two rolls remain separate. This is stated explicitly because the phrase "one human, one vote" has been read as a membership claim, which it has never been.

The People decide directly on:

- Constitutional amendments (changes to these first principles)
- The Reading and the Reckoning (every five years)
- The reversal of any lower-tier pause that has been escalated to them, by representative deliberation for ordinary disputes and by direct popular vote for consequential or irreversible cases
- Any irreversible or long-haul emergency action (see §VI)
- The election and recall of the Tribune, triggered by the Legitimacy Decay Index

The substantive will of the People is the highest authority in the system. The Tribune may slow it procedurally; the lower tier may not touch it. When the People and the Tribune converge, the decision is supreme.

#### The Tribune

The Tribune is a single elected human office. The name is a placeholder, drawn from the Roman tribune of the plebs, an office whose original purpose was to check concentrated power on behalf of the people. ("King" was considered and rejected: the office is a broker and a check, not a ruler.) The Tribune is four things and only four things:

- a **convergence-broker**, bringing the lower-tier branches and the People toward workable agreement;
- the **emergency-initiator**, able to initiate a crisis response (the response takes effect only on lower-tier authorization, see §VI);
- the **holder of a check on the lower tier**;
- the system's **external representative**.

The Tribune cannot legislate, tax, allocate resources, or sanction alone. Each of those requires the People and the lower-tier process. The Tribune's check on the People is procedural only: the office can slow, return, or force re-deliberation, but it cannot override the substantive will of the franchise.

**Selection and tenure.** The Tribune serves a **single six-year term and may never stand again**. Entry is open from age 35, with a maximum entry age set so that the officeholder exits by roughly 75, placing the ceiling near 69.

Non-renewability is doing the work that term length was originally asked to do. An earlier draft set a single fifteen-year term so the office could hold a horizon longer than an electoral cycle. A term that can never be renewed delivers almost all of that at a fraction of the cost, because an officeholder with no next election has no campaign to run and no constituency to court, while fifteen years of unremovable tenure was longer than any comparable office in any republic and read as entrenchment however it was defended.

Six years rather than five is deliberate. The Reckoning runs every five years (Principle 7). Matching the two would land every structural self-audit on a transition, with an outgoing officeholder presiding over the audit of their own tenure. At six the cycles interleave permanently: every Tribune faces at least one full Reckoning mid-term, has to answer for its findings, and then keeps governing under them. Staggering independent checks so they fire at different moments is ordinary constitutional design, and the offset is the point. Six is also the United States Senate term, which means it needs no explanation.

The Legitimacy Decay Index and recall (see below) operate throughout, so the term is a ceiling rather than a guarantee. The founding term is shortened (see §IX). The bootstrap of the very first Tribune is described in §IX.

**The five-layer defense of the Tribune office.** A single human office is a capture target. The architecture defends it on five layers, each closing a different vector:

1. **Selection integrity.** The office cannot be installed by a faction. The Tribune is chosen through a sortition-drawn nominating body that screens candidates against the Tribune criteria, public nomination, and a one-human-one-vote election (the mechanics are in §IX). This closes the vector of pre-installing a captured office.
2. **Influence and coercion firewall.** The Tribune is bound by the engine's strongest anti-influence rules, applied to the office specifically: no transfer of financial value, in-kind goods of substantial value, employment promises, sponsored research, or equivalent compensation; assets in blind instruments for the duration of the term; revolving-door prohibitions before and after; full and public disclosure of interests, which also shrinks the surface for blackmail by leaving little secret to threaten exposure of. Coercion is the involuntary twin of bribery: where bribery pays the office, coercion threatens the officeholder or the people they love. The engine provides personal security for the Tribune and immediate family, but it does not pretend a human with people they love can be made un-threatenable. The structural answer is layer four: a coerced Tribune, like a bought one, can deliver almost nothing alone. This closes the vector of buying or threatening the office, and bounds what is left.
3. **Transparency of action.** Every official act of the Tribune (convergence brokering, emergency initiation, the exercise of the check on the lower tier) is logged and disclosed under the public-principles rule. Private deliberation content is protected; the decisions and their stated rationales are not. This closes the vector of capturing the office in the dark.
4. **Powerlessness alone.** The Tribune holds no substantive power without a counterparty. A captured Tribune can stall, broker, and represent, but cannot command: no law, no tax, no allocation, no sanction issues from the office alone. This closes the vector of a captured office being worth capturing, by shrinking the payoff.
5. **Continuous legitimacy and recall.** The Legitimacy Decay Index measures the office's standing with the governed continuously; sustained loss triggers a fresh election and sharper loss triggers recall. This closes the vector of capture becoming permanent, by making a captured office removable on the evidence of its own outcomes.

The five layers defend against manipulation **of** the Tribune. The distinct case of the Tribune **colluding with** the lower tier is addressed structurally in the cross-tier mechanics below and in §X.

**The Legitimacy Decay Index (LDI).** Version 1.0 spoke loosely of a satisfaction or approval threshold. Version 2.0 replaces it with the LDI, a continuous measure of the system's standing with the governed. Working figures, tunable at every Reckoning:

- Legitimacy below **40 percent sustained over 90 days** triggers a fresh Tribune election.
- Legitimacy below **30 percent** triggers recall.
- A **velocity clause** escalates on a faster clock when legitimacy drops 15 points inside 30 days, so that a sharp collapse is not allowed to hide behind a slow-moving average.

The LDI's inputs, weighting, and measurement methodology are themselves governed by the public-principles-classified-instances rule and audited at every Reckoning. The numbers above are placeholders chosen to be revised by evidence, not defended as correct.

**Succession, absence, and incapacity.** A single human office must answer three questions the rest of the architecture does not face: what fills the chair when it is empty, what happens when the officeholder will not act, and how the office is judged unfit without that judgment becoming a tool to remove an inconvenient holder. One principle governs all three: the instrument never overrides a human's exercised judgment, and the fast paths exist only for the absence of judgment, not for the exercise of it.

*Vacancy.* When the office is empty (death, resignation, recall, or a confirmed incapacity finding), the presiding seat of the Councils acts as interim Tribune. The interim is a caretaker. It holds the office's functions, including emergency-initiation, so that a vacancy during a crisis does not freeze the response, but it cannot make the irreversible or long-haul commitments an elected officeholder makes (those already require the People), it serves under a hard clock, and a vacancy triggers a full-legitimacy election on the soonest workable timeline. To remove any incentive to engineer a vacancy, the caretaker is barred from standing in the replacement election, and the body that can trigger a removal is kept structurally separate from the seat that fills the chair.

*A sitting Tribune who will not act.* This is not a vacancy, and it must not be treated as one, because a Tribune refusing to call something an emergency may be the system working: the human brake on coercive emergency power is supposed to be real. A sitting Tribune's exercised refusal therefore stands, and the only thing that overturns it is the other sovereign. The Councils can force an expedited popular vote on an emergency the Tribune declined (the same one-shot brake, turned the other way), but neither the Councils nor the AI branches can act over a present, deciding human. The override of a deciding sovereign belongs to the People alone.

*An unreachable Tribune.* When the officeholder is genuinely unreachable and no judgment has been exercised, the office is functionally empty for the moment, and this is handled closer to a vacancy. Here the Councils, the human branch, acting with the high emergency gate, may trigger a short, reversible, time-buying measure only. Anything lasting still goes to the People. A human stays in the loop even on the fast path, so the AI branches never originate coercive action on their own.

The hard case is incapacity, and the document treats it as the softest joint in the whole architecture (see §X). "Unreachable" is easy when communications are demonstrably down. "Unfit" is where every system bleeds, because declaring an inconvenient officeholder unfit is among the oldest moves against a sovereign. The defense is to take the discretion out of the moment. The fitness criteria are set in advance, at the founding, behind a veil of ignorance before anyone knows who will hold the office, authored and owned by the People. AI bodies and clinical experts inform the design of those criteria (a fitting bounty, since it is a genuine technical and medical problem), the AI branches run any detection and audit that it runs honestly, but the AI never authors the standard by which a human sovereign is judged unfit and never retunes it against a sitting Tribune. Changes to the criteria pass through the People and the Reckoning, never ad hoc.

Any standing fitness signal, for example sustained divergence in a Tribune's public speech from their own established baseline, is advisory input to a human process only, never an automatic trigger. Direction is what matters, not distance. Variance upward (novelty, sharper argument, evolving positions) is a mind working and is never a flag; the signal of concern is degradation, incoherence, repetition, loss of complexity, falling out of the thread. Telling degradation from evolution is precisely the hard judgment, which is why the signal only ever raises a question, never answers one. Measurable harmful impact is deliberately kept out of the fitness question: a leader's decisions causing harm is a legitimacy matter for the Legitimacy Decay Index and recall, where the officeholder can make the case for a painful-but-correct call, not a fitness matter, and routing impact into an unfit finding would both reopen the soft-coup vector and chill the hard decisions the office exists to make. A Tribune who turns genuinely dangerous is covered elsewhere and harder: by recall for a direction the People reject, and by the justice machinery, including permanent containment, for civilizational crime, which binds a Tribune as it binds anyone.

A clear case resolves by the pre-agreed criteria with no discretion. A contested case goes to the People to decide, with the Tribune entitled to contest it and to fresh outside review at every cycle. Clear resolves structurally; contested goes to the sovereign. It is the same spine the rest of the architecture runs on.

### Tier 2: The Triadic Instrument

The lower tier is the instrument. It is three peer branches in permanent tension: the Councils, the National AIs, and the Oversight. None of the three is sovereign. Each checks the other two. No single branch acts as the instrument alone.

#### The Councils

The Councils are the human deliberative bodies, the descendant of Version 1.0's rolling human council. Composition is by sortition from among populations meeting deliberative-capacity criteria (not credential criteria), with explicit representation from oral and non-literate traditions, with rotation to prevent capture, with anti-bribery controls and conflict-of-interest disclosure, with adversarial counsel and secure evidence access, and with public opinions, appeal rights, and removal procedures.

The Councils:

- deliberate on matters surfaced to the lower tier;
- hear appeals from flagged National AIs and review permanent-containment cases (see §VI);
- audit the Oversight's determinations and act as the human check on the Oversight, structurally separated from the AI branches and not advised by them on their own audit decisions;
- arbitrate reversals escalated from a pause, through representative deliberation, and convene the expedited popular vote when a case is consequential or irreversible;
- hold the one-shot emergency brake described below.

#### The National AIs

Each political unit (the unit varies by adopting community; see §X) trains an AI representative on its cultural, historical, religious, legal, and linguistic corpus. This branch carries forward from Version 1.0's Layer 2 unchanged in function.

The National AI's role is **descriptive representation**, not normative validation. It articulates the positions, traditions, and priorities of its population. It does not adjudicate rights claims; rights claims pass through independent human-led rights bodies and citizen-direct channels.

All training data passing into a National AI's corpus is audited by the Oversight plus the Councils. The audit operates through statistical sampling, adversarial probing, and provenance verification; full read-through is not implied. Audit confidence is measured and disclosed. National AIs cannot be trained on state propaganda alone. The audit chain is the engine's primary defense against authoritarian capture.

When a National AI is flagged as captured, the engine reduces or refuses **the state AI's** deliberation weight while preserving citizen-direct channels: diaspora submissions, local citizen assemblies, independent civil-society inputs, and individual companion-routed petitions. The population is never disenfranchised by their state's capture. Restoration to full standing requires corpus rebuild with documented changes, a public challenge window for citizen and external evidence, independent re-audit, a probation period of at least one Reckoning cycle, and supermajority ratification by the Councils.

National AIs are retrained on a synchronized **five-year cadence**, with light tuning permitted annually to keep pace with current events. All retraining is fully transparent, blockchain-audited or equivalent, and subject to mandatory public review during a comment period.

#### The Oversight (the Twelve)

The Oversight is the global audit branch sitting within the lower tier. Public name: **Audit Consortia**. Each member is a distinct oversight AI trained on overlapping but distinct global corpora by an independent consortium drawn from a different cultural and intellectual tradition.

**The size of the body is derived, not decreed.** Version 2.0 sets a founding count of twelve members under a **nine-of-twelve quorum**, and it names the requirements the count has to satisfy so that the number can be revised at any Reckoning as conditions change:

- **Capture tolerance.** The body must withstand at least three simultaneously compromised members without losing the ability to act, and the quorum must exceed two thirds. Twelve members with a nine-member quorum satisfies both.
- **Floor.** No fewer than ten members. Below ten, either capture tolerance or the two-thirds quorum fails.
- **Corpus independence.** No two consortia may share more than a defined fraction of training corpus, verified by cryptographic training-provenance.
- **Tradition coverage.** The set must include at least one consortium primarily grounded in each major language family above a stated speaker threshold. Language family is the operative unit because corpus overlap is a linguistic fact before it is a cultural one, and because it is measurable rather than contested.
- **Growth mandate.** The count rises toward fuller coverage as additional qualifying institutions come into existence. It does not rise for its own sake, and it never falls below the floor.

Three independent lines of reasoning converge on a band of ten to fifteen: capture tolerance sets the floor, major language families above fifty million speakers number roughly twelve, and twelve is the size of a jury, which is the function this body performs. Twelve is where the founding count sits inside that band. Nothing about the specific number is load-bearing; the requirements above are.

The practical constraint is supply. The number of institutions on Earth that currently satisfy the accession criteria in §X (diversity of tradition, demonstrated AI-safety research capacity, transparent governance, no controlling stake held by any single state or capital interest) is small, and may be smaller than twelve at the founding moment. Where it is, the body seats what qualifies, discloses the shortfall publicly, and operates with the capture-tolerance requirement recalculated for its actual size until the floor is met. A body that pretends to coverage it does not have is worse than one that names the gap.

Quorum rules require supermajority agreement on any flag, mandatory minority reports, and full public dissent logs. Reckoning-cycle replacement prevents accumulated drift.

The Oversight's function is to:

- audit National-AI training data for capture, manipulation, or rights violations;
- flag captured National AIs and reduce or refuse the state AI's deliberation weight until remediated;
- identify global problems requiring coordinated attention;
- detect information warfare, mass psychological operations, and coordinated inauthentic behavior;
- detect inception attacks (manipulation directed against an apparent beneficiary to discredit and de-weight that side);
- commission bounties and roadmaps for solvable problems;
- surface emergency situations into the crisis spine (see §VI).

The Oversight operates adversarially with itself by design. Each member is trained by a different consortium with explicit anti-hegemony mandates. No two consortia may share more than a defined fraction of training corpus. Cryptographic training-provenance is mandatory.

The Oversight is checked by the other two lower-tier branches, by the two sovereigns above, and additionally by independent red-team courts of human researchers with kill-switch authority, by mandatory adversarial replacement of any member that fails periodic capture-resistance testing, and by the Reckoning, which can replace consortia entirely.

This branch is the architecture's most powerful component and its highest-value capture target. The selection of the founding consortia is the architecture's most consequential bootstrap decision and remains a standing open question (§X) with the highest priority for adversarial review. The protections above are necessary but may not be sufficient. Hardening this branch is a continuous adversarial project, not a one-time design.

### Cross-Tier Mechanics

The two tiers are joined by a single spine: a low-bar reversible pause, and a high-bar emergency gate. The same spine carries ordinary action and emergency action; only the gate's direction changes.

**The reversible pause (the lower tier's check on the upper).** Any one lower-tier branch can trigger a reversible, time-boxed pause of a Tribune action on a low bar. The bar is intentionally easy to clear: a simple majority within the triggering branch is sufficient, because the pause is reversible and escalates rather than decides. A pause is not a veto. Turning a pause into a reversal escalates to the People: representative deliberation through the Councils for ordinary disputes, and a direct popular vote for consequential or irreversible cases. Irreversibility is flagged by the Oversight; any one sovereign or any one lower-tier branch may demand escalation to a popular vote, with representative deliberation as the default otherwise.

The design is asymmetric on purpose. The pause is cheap so that no Tribune action goes unchecked. The reversal is dear, and it belongs to the People, so that the lower tier cannot override a sovereign on its own. This is why the cross-tier check is not set at any fixed vote threshold. A single threshold is gameable from one side or the other: unanimity across the three branches lets a sovereign neuter the check by capturing one branch, and a two-of-three rule lets a colluding pair drive the check abusively. Demoting the check to a pause, and handing the reversal to the People, removes the gameable threshold entirely.

**What the lower tier can and cannot do to a sovereign.** The three branches acting together can pause and, through escalation to the People, reverse a single Tier-1 actor. Nothing the lower tier can do overrides Tribune-and-People convergence. When both sovereigns agree, the lower tier serves the decision; it does not get a vote on it.

**The emergency gate.** The crisis machinery is the same spine with the gate flipped, and it is described in full in §VI. In short: ordinary Tribune action takes effect immediately and can be paused after the fact; coercive emergency action does not take effect until the lower tier pre-authorizes it on a high bar (National AIs supermajority plus Oversight nine-of-twelve, both required), the Councils hold a one-shot brake that forces an expedited popular vote, and anything irreversible or long-haul requires the People.

---

## IV. THE ECONOMIC BASELINE

The economic system underwrites the political system. Ouroboros locks the following economic commitments. Several are aspirational targets whose mechanisms are open questions (§X); the principles below are the engine's commitments, and the operational details are subject to the Reckoning. All of the carry forward from Version 1.0 unchanged.

**1. Civic Commons.** The following are commons, funded through engine-coordinated mechanisms (specified by jurisdiction during transition; see §X), available to every human at the point of use:

- Nutrition (sufficient for health)
- Clean water
- Shelter (basic, dignified)
- Healthcare (universal Baseline; private supplementation permitted above it)
- Education (universal through advanced study; private supplementation permitted)
- Energy (universal access through strategic renewable buildout, modernized transmission, and aggressive R&D bounties)
- Information access and a personal memory layer enabling informed civic participation, supported by the personal companion described in §III

The informational Baseline is justified on the same grounds as the material Baseline: a person who cannot meaningfully access information, cannot retain context across the timescales civic decisions require, and cannot draw on personalized cognitive support for navigating complex deliberations is structurally excluded from self-governance. The right is to the cognitive infrastructure that makes participation possible, not to any specific product. The architecture is implementable by any provider; the engine actively encourages plurality and portability.

Commons delivery operates in tiers calibrated to local infrastructure: offline-first small models for low-bandwidth populations, shared public terminals where individual access is impractical, regional inference clusters, assistive-device access, and continuity protocols during outages. Universal access is the principle; uniform delivery is not assumed.

**2. Universal Basic Income.** The engine's working hypothesis is that AI-mediated coordination produces enormous economic value through disintermediation and that this value can be captured and distributed as an existence-floor. The mechanism (tax base, collection authority, jurisdictional enforcement, regional cost bands, capital schedule, operating budget, solvency constraints) is an open question (§X). UBI is locked as principle, provisional in mechanism. If dividend mechanisms underperform, the engine's fallback is means-testing the supplementary above-Baseline portion only; the Baseline itself remains universal.

**3. Bounded Capital.** Capital flow for building is permitted and encouraged. Founders, employees, and private investors may form companies, raise capital, generate returns, and build at scale. The bounded-capital provisions below operate under the **broad regime** (Principle 0b) and apply within ratifying jurisdictions only; non-ratifying populations are not subject to engine economic mandates. Within ratifying jurisdictions, the provisions are implemented through the standard democratic process of those jurisdictions, not by direct engine action against private parties.

The engine commits to advocating for the following principles within ratifying jurisdictions, with implementation handled through those jurisdictions' own democratic and legal processes:

- **Planetary-scale shareholder corporations as a structural concern.** The publicly-traded shareholder model, wherein controlling interest passes to anonymous capital holders whose only relationship to the enterprise is extraction, is recognized as a primary corruption vector at planetary scale. The engine encourages, but does not directly compel, qualifying entities to transition toward employee cooperative ownership, public-utility status, or planned breakup. Mechanisms are incentive-based: tax preference for cooperative and public-utility structures, tax penalty on extractive shareholder structures above the impact threshold, public-procurement preference, civic-commons access tiers. Specific thresholds are defined in §X. Most public-equity activity is unaffected; the provisions target a small number of entities at planetary scale. Transition compensation mechanisms are designed to preserve invested value through restructuring rather than confiscate it. The engine accepts that this path is slow. Bounded-capital reform on a multi-decade horizon is the realistic timeline, and the engine accepts that timeline as the cost of operating under broad-regime consent.
- **Capital gains differentiation.** Capital gains on extraction is taxed heavily; capital gains on building is taxed lightly. The engine distinguishes wealth that compounds through creation from wealth that compounds through rent-seeking. Operationalizing this distinction requires beneficial-control rules, anti-fragmentation tests (preventing artificial entity-splitting to evade thresholds), a jurisdiction-scope ownership registry, threshold smoothing to avoid cliff effects, transition compensation for affected parties, and anti-avoidance enforcement. Implementation is jurisdictional. The full operational specification is acknowledged as a major open question (§X).
- **No monetary or value-exchange lobbying.** Citizens may petition government and the engine through speech, writing, and assembly. They may not transfer financial value, in-kind goods of substantial value, employment offers, or equivalent compensation to officials, parties, or political bodies. Volunteer labor, speech, and assembly are protected. Lobbying-by-payment is corruption by definition. Influence transfer is regulated broadly: gifts, employment promises, sponsored research, media buys, data grants, model credits, affiliated nonprofits, and revolving-door roles all fall within scope.
- **Donations confer no influence.** Charitable giving is welcome and encouraged but produces no special access, recognition, or political weight beyond the public good of the donation itself.

I acknowledge the tension between the urgency of the problems bounded capital addresses and the slowness of the consent path the engine commits to. Concentrated extractive capital at planetary scale is genuinely dangerous, and a multi-decade reform horizon means the harms compound during the transition. The engine accepts this cost as the price of operating under consent rather than coercion. Coercive economic restructuring of private actors who did not personally consent is a line the engine will not cross under the broad regime, regardless of how strong the case for it. The alternative, smuggling coercion through "very strong incentives to join, very strong disincentives to refuse," fails the consent test and would forfeit the legitimacy on which the engine's broader authority rests.

The regime change implied here is of historic magnitude within ratifying jurisdictions. The bounded-capital framework is the engine's working response. Refinement and counter-proposal are welcome through the standard process.

**4. Approval-Process Standardization.** Healthcare approvals, housing codes, building permits, regulatory compliance, and similar gating processes are standardized globally where possible, and reformed where local variance is needed. The malpractice-insurance-driven distortion of healthcare delivery is restructured. Bureaucratic corruption is targeted with the same rigor as financial corruption.

**5. Cure Bounties.** For diseases above a threshold of human harm, the engine commissions cure bounties using milestone contracts, replication requirements, independent trial registries, anti-collusion audits, prize clawbacks, open manufacturing specifications, and post-award monitoring. Cures developed under engine bounty enter civic commons (free at point of use, manufactured at cost). Private R&D continues for everything else but cannot extract beyond fair-return thresholds for chronic-condition management of bountied diseases. The incentive structure is restructured to reward cures over management.

**6. Credit-Reporting Reform.** The current credit-reporting model, where past financial trouble haunts a person for arbitrary years regardless of actual recovery, is replaced. Credit assessments must reflect current reality, not stale punishment. People who have done the work of recovery are restored to full financial standing on a timeline matched to their actual conduct, not to a fixed-year schedule disconnected from it.

**7. Displacement and the Cost of Transition.** Automation displaces people. The engine treats this as a governance outcome rather than a technological one, because the technology does not decide who bears the cost. Institutions decide that, and the current arrangement concentrates the gains while distributing the losses. The mechanism that keeps it arranged that way is the same influence capture §0 describes and the lobbying prohibition above addresses.

The engine commits to four things on displacement, none of which depend on the income floor above:

- **Transition cost attaches to the party capturing the gain.** Where a firm's automation eliminates positions, that firm carries the retraining and income-bridge cost for the people displaced. This is implemented through tax structure within ratifying jurisdictions, not by engine action against private parties.
- **No public subsidy for job-eliminating automation, tested on measured headcount.** Public money and tax preference do not flow to capital deployment that removes employment. The test is not a firm's stated purpose, because primary-effect tests invite every firm to claim quality, safety, or capacity: it is measured headcount at twelve and twenty-four months against a pre-deployment baseline, which the disclosure requirement below already produces. A firm whose measured headcount falls below the baseline forfeits the preference and repays it. A jurisdiction that funds the elimination of its own tax base is not making an investment.
- **Displacement disclosure.** Firms above a stated size threshold report automation-attributable change in headcount, on a regular cadence, publicly. Nobody currently knows this number at any useful resolution, which is why the public argument about it runs on impression. Disclosure is the precondition for any policy at all, and it is the same principle the information-environment commitments in §VII rest on: what is not disclosed cannot be governed.
- **Sector-scale early warning.** The Oversight's existing mandate to identify global problems requiring coordinated attention explicitly includes labor displacement at sector scale, surfaced publicly and early rather than after the fact.

I acknowledge the same tension here that §IV.3 names about bounded capital, and it is not smaller. The load-bearing commitment above runs through the tax structure of ratifying jurisdictions, which means it depends on the same jurisdictions that have so far declined to make it, and it reaches nobody who has not ratified. Displacement is happening now, on a faster clock than voluntary accession moves. A person whose work disappears in the interval is not helped by a commitment that binds only the communities that already agreed. The engine accepts that cost for the same reason it accepts it on capital: coercing people who did not consent would forfeit the legitimacy the rest of the architecture depends on. It is a real cost, it falls on real people during the transition, and naming it is not the same as answering it.

The engine does not claim to have solved this. An income floor keeps a person alive and it is not a place in the world. Work is where a great many people locate their competence, their standing among others, and their sense that their days matter, and no transfer payment supplies those. The engine's commitments above address who pays for the transition and what the public can see while it happens. They do not answer what a person is for when the work is gone. That question is real, it is upstream of policy, and the architecture is a floor rather than a ceiling precisely because it is not the engine's place to answer it on anyone's behalf.

**8. The Engine's Own Footprint.** This architecture runs on physical infrastructure. A twelve-member Oversight of independently trained models, retrained on a five-year cadence, plus per-community National AIs, plus companion access for every human, consumes electricity, water, land, and capital at scale. Rising residential energy costs and the siting of large compute facilities are live political injuries in many communities already. An architecture that claims ecological coordination as an emergency-tier concern and does not account for its own consumption is not credible.

The engine binds itself to the following, and holds itself to a stricter standard than it asks of anyone else:

- **Full unsubsidized cost.** Compute the engine requires pays retail rates for power and water. No cost socialization onto other ratepayers, no negotiated large-load tariff below cost of service, no sales-tax or property-tax exemption, no publicly financed transmission built primarily to serve it. Where the engine's infrastructure raises the cost of service for a shared grid, the engine carries that increase.
- **Siting by consent.** No engine infrastructure is sited in a community that has not consented to it, through the same ratification the architecture requires of itself everywhere else. A voluntary-consent architecture that imposes its own buildings has forfeited the claim.
**Order of magnitude, stated in advance.** The engine publishes an estimate before it has one to measure, because a section on footprint with no number in it is not a disclosure. The figures below are order-of-magnitude, carry bands of several times in either direction, and are stated with their assumptions so that they can be attacked and corrected:

- **The governance layers** (twelve Oversight models trained independently on a five-year cadence, plus per-community National AIs, plus continuous audit inference) fall on the order of **one terawatt-hour per year**, plausibly between roughly 0.3 and 3. Assumptions: frontier-scale training runs in the tens of gigawatt-hours each, amortized across the five-year cycle; continuous audit inference at a few thousand accelerators per Oversight member; National AIs materially smaller than frontier scale. For scale, that is roughly a single large data center campus, on the order of two thousandths of one percent of world electricity generation, and it implies cooling water in the range of a town of twenty thousand people.
- **The companion layer, run local-first as this document requires,** falls on the order of **ten terawatt-hours per year** across all of humanity, or roughly a couple of kilowatt-hours per person per year, drawn incrementally from devices people already own and already charge. That is on the order of three hundredths of one percent of world electricity generation.
- **The companion layer if it were instead centralized at frontier scale** would be one to two orders of magnitude larger than that. This is the reason the smallest-sufficient-model constraint below is written as a binding requirement rather than an engineering preference: the difference between the two designs is the difference between a rounding error and a material addition to global demand.

These numbers will be wrong. They are published so that the direction and the size of the wrongness are visible, and they are superseded by measurement as soon as measurement exists.

- **Published footprint.** Energy, water, and emissions for all engine infrastructure are published on a regular cadence, in absolute terms rather than intensity ratios, and independently verified. Estimates are published before construction and reconciled against measured consumption after.
- **Smallest sufficient model.** The companion layer runs local-first on the smallest model that performs the function, consistent with the privacy modes in §III and the tiered delivery in this section. Frontier-scale inference is reserved for the audit and representation branches, where adversarial independence requires it. Convenience is not a justification for scale.
- **Additional generation, on a specified standard.** New load the engine creates is matched by new generation the engine brings online. The standard is named because vague versions of this promise are the industry norm and mean nothing: matching is **hourly**, within the **same grid region** as the load, from capacity that is **additional** rather than reallocated from existing supply, and **verified by an independent third party** whose methodology and findings are public. Unbundled certificates purchased in another market or another hour do not satisfy it. This is a standard almost no current operator meets, which is the reason for stating it. Where the engine cannot meet it on the required timeline, the deployment is deferred or reduced and the shortfall is published with the deferral, not instead of it.

The engine accepts that these constraints slow its own deployment and raise its own costs. That is the intended effect. An architecture whose legitimacy rests on consent cannot fund itself by quietly transferring its expenses onto people who never agreed to it.

The clinical, regulatory, and economic specifications above are sketches at this level of resolution. The engine commits to the principles. Operational details are addressed through subspecs and the Reckoning.

---

## V. THE BOUNTY SYSTEM AND THE ONE-VOTE STANDARD

### The Bounty System

Ouroboros does not solve humanity's problems for it. Ouroboros calls humanity into cooperation on its own problems.

The engine generates a tiered, continuously updated roadmap of open problems, scaled by difficulty:

- **Tier 1 (local):** thousands open at any time. Local coordination problems, infrastructure improvements, community-level civic work. Anyone can take, anyone can complete.
- **Tier 2 (regional) through Tier 4 (national):** hundreds to dozens. Regional and national coordination. Requires teams, expertise, sustained effort. Bounties scale with difficulty.
- **Tier 5 (civilizational):** few. Civilizational-level challenges. Cure for cancer. End of factory farming. Sustainable fusion. Cross-cultural reconciliation. Bounties at planetary scale.
- **Tier 6 (generational):** the deepest problems. Reserved for projects requiring decades and convergent global effort.

Bounty awards use milestone contracts with replication requirements, independent verification, anti-collusion audits, prize clawbacks for fraud or partial submissions, open licensing of resulting infrastructure, and post-award monitoring.

When a quest is accepted, the engine tracks progress, surfaces collaborators, allocates bounty resources, and reviews submitted solutions through both Council review and Oversight analysis. Solutions that pass review are scaled, integrated into the commons, and the quest closes. New quests open as data accumulates and new problems surface.

### The One-Vote Standard

Every system of self-governance has to answer one question before any vote means anything: did each vote counted come from a distinct person? Without an answer, whoever controls the most compute controls the outcome, because fabricated participants are cheap and getting cheaper. A million manufactured voices can outvote a town. The engine's answer to that problem is the **One-Vote Standard**, called *Sybil resistance* in the engineering literature after the failure mode it prevents: one actor manufacturing many identities.

**What is verified, and what is not.** The engine does not verify people. It verifies **ballots**: that each vote counted traces to one distinct person and that no person's vote counted twice. Nothing in the standard requires the engine to know who cast a ballot, and its design forbids the engine from being able to find out.

**What the engine is permanently forbidden from building.** These are prohibitions, not preferences, and they are not subject to emergency suspension:

- **No central registry of verified persons.** No list exists, at any tier, of who has been verified. There is nothing to leak, subpoena, sell, or seize.
- **No universal identifier.** No number, credential, or token follows a person across contexts. Anything issued is single-purpose.
- **No cross-context linkage.** A verification used in one vote cannot be correlated with a verification used in another. This is a mathematical property of the protocol, not an access policy.
- **No persistence.** Attestations expire by default and are destroyed on withdrawal. There is no permanent record of participation, and no participation history accumulates against anyone.
- **No condition on anything other than a vote.** Verification is never required to receive the Baseline, to access the commons, to speak, to petition, to assemble, to travel, or to obtain any service. It bears on the counting of ballots and nothing else. A person who never verifies loses nothing but the ability to cast a counted vote, and may participate in every other part of civic life.

Anything resembling a durable, universal, engine-held record of persons is outside the architecture and cannot be brought inside it by any process short of constitutional amendment through the People.

**How it works.** The specification includes:

- **Biometric optionality** (never a biometric requirement)
- **Social attestation** (recursive trust networks)
- **Hardware key support** (where available)
- **Zero-knowledge verification** (proof that a ballot is distinct without disclosure of who cast it)
- **Recovery courts** (for compromised, lost, or coerced credentials)
- **Fraud bounties** (continuous adversarial-discovery rewards)
- **Coercion detection** (signals and signatures of forced participation)
- **Periodic recertification** (no permanent attestation)

The standard is graduated, not binary. Verification confidence is tiered. Edge cases (severe disability preventing standard verification, populations under coercive regimes, recovery from compromise) are handled by recovery courts with explicit criteria and a bias toward enfranchisement: where the standard cannot be met through no fault of the person, the recovery court's default is to enable the vote, not to exclude it.

**The dependency, stated honestly.** The engine cannot fully bind itself until the One-Vote Standard is operational. During the provisional period (Principle 0a), the engine convenes, deliberates, and commissions but does not bind. Initial-adopter populations decide when the standard has reached sufficient maturity for full binding to begin.

If the standard cannot reach sufficient maturity within a reasonable timeline, the engine's standing commission is to revisit the architectural dependency. The engine's binding may need to be reformulated, or the architecture may not be deployable at the scope this document assumes. I consider this possibility live and unsolved.

The standing operation of the One-Vote Standard, including compliance with every prohibition above, is audited continuously by the Oversight, the Councils, and independent rights bodies, and is a mandatory line item in every Reckoning.

---

## VI. CRISIS, ENFORCEMENT, AND JUSTICE

### Justice Philosophy

Ouroboros prefers restoration over retribution. The engine's working hypothesis, to be audited continuously by the Reckoning against actual outcomes, is that a substantial portion of currently incarcerated behavior is downstream of failed conditions: poverty, untreated mental illness, addiction, lack of education, lack of opportunity. With the Baseline funded and maintained, the engine expects this population to shrink materially. The remainder is addressed through layered response: civic restitution, supervised liberty with monitoring, asset restructuring, temporary loss of optional engine services, treatment programs, and only then incarceration when public safety requires it. Prison is the response when other measures fail. It is not the default.

The engine does not pretend that all crime is downstream of conditions. Some humans need to be separated from the population for protection. That population is expected to be much smaller than current systems produce, but it is not zero.

### Crisis Response: One Spine, Two Gates

Version 1.0 described a four-rung escalation ladder. Version 2.0 collapses that ladder into the single cross-tier spine, so that crisis power and ordinary power run through the same machine and cannot drift apart. The difference between ordinary action and emergency action is the direction of the gate.

**Ordinary action.** A Tribune action takes effect immediately. The lower tier can pause it after the fact (the reversible pause, any one branch, low bar), and the People arbitrate any reversal. This is the default, and most engine action lives here.

**Emergency action.** Coercive emergency action does not take effect until the lower tier pre-authorizes it. The authorization gate is high and requires two branches at once:

- **National AIs supermajority** (a supermajority of currently-seated, non-de-weighted National AIs, meeting a participation quorum), **and**
- **Oversight nine-of-twelve.**

Both are required. Neither branch can authorize emergency coercion alone.

**The Councils' brake.** The Councils hold a one-shot, council-majority pause that freezes any fast-track authorization and forces an expedited popular vote. It is a brake, used once per authorization, not a repeatable filibuster. It exists so that the human deliberative branch can always force a fast-moving emergency in front of the People when it judges the stakes warrant it.

**Initiation.** Emergency response is initiated by the Tribune as the office's emergency-initiator function. Crisis detection may also originate in the Oversight, which surfaces emergencies into this spine. A non-acting Tribune is handled by the rule in §III rather than by letting the instrument seize initiation. If the Tribune is present and has refused, that exercised refusal stands, and only an expedited popular vote (which the Councils can force) overturns it. If the Tribune is genuinely unreachable, the Councils, the human branch, may originate a short, reversible measure under the same high gate, with anything lasting going to the People. The AI branches never originate coercive action on their own: a human, the Tribune or the Councils, is always the initiator, so that a single non-acting office cannot freeze a civilizational response and the instrument never starts the emergency by itself. Every path takes effect only on the high authorization bar above, and every path is subject to the Councils' brake and the People's backstop.

**Graduation by duration and reversibility.** The gate scales with what the action costs to undo:

- A short, reversible coordination window can run on the fast gate alone, with a short automatic sunset (working figures carried from Version 1.0: on the order of 48 hours for the shortest measures, 30 days for extended ones).
- Extension beyond the short window requires the Councils' concurrence (council-majority).
- Anything irreversible or long-haul requires the People, by popular vote, with a deliberation period proportional to the risk. Defensive containment can buy time; irreversible action requires the people.

**Carried protections.** Every Version 1.0 emergency protection holds. Authorizations sunset by default. Renewal cannot be granted by the authority that invoked the measure; renewal escalates a tier (to a higher gate, and ultimately to the People). Personal liability attaches to actors who invoke emergency authority under crises later determined to have been overstated. Independent red-team courts separate from the AI branches hold kill-switch authority. Every emergency invocation, and the threshold determination that triggered it, is audited at the Reckoning.

### Sanctions and Enforcement

When individuals, corporations, or countries violate engine principles, sanctions apply with proportional equivalence across categories: an individual's restriction, a corporation's restructuring, and a nation's isolation are calibrated to inflict comparable accountability relative to operating capacity.

Sanctions include:

- **Reduced engine-coordination access** (for nations and corporations: reduced trade-coordination, reduced commons-share, reduced oversight-mediation bandwidth)
- **Temporary loss of optional engine services** (for individuals: time-limited reduction of access to non-essential commons services; the Baseline preserved always; subject to due process, proportionality, appeal, defined maximum duration, protected categories, hardship exemptions, medical override, disability review, and restoration criteria)
- **Asset restructuring** (for corporations operating in ratifying jurisdictions that have demonstrably violated engine principles after voluntarily accepting them: governance changes, breakups, asset transfers to commons, applied through the legal frameworks of the ratifying jurisdiction; not applicable to entities in non-ratifying jurisdictions or to entities that have not violated principles)
- **International isolation** (for nations: ladder of diplomatic and economic isolation)
- **Imprisonment** (where ratifying jurisdictions adopt it as part of their legal framework, applied through their own judicial process aligned with engine principles: defense rights, discovery, confrontation of evidence, appeal, and exclusion rules; AI oversight may assist investigation, never decide guilt; the engine itself does not directly imprison, it cooperates with and audits jurisdictional systems that do)
- **Long-term incarceration with reviewable status** (for severe non-civilizational crimes such as serial violence, individual sexual exploitation of children, large-scale fraud above defined thresholds, and deliberate ecological destruction below civilizational threshold; reviewable at defined intervals; subject to all judicial protections plus exoneration-first review with mandatory outside defense counsel at every cycle)
- **Permanent containment** (reserved for civilizational-scale crimes only: genocide committed or attempted, deliberate ecocide at civilizational scale, mass-scale crimes against humanity, willful weaponization of mass-casualty infrastructure, and organized sexual exploitation of children at civilizational scale; subject to periodic review and exoneration-first audit by outside defense counsel)

The category "civilizational-scale crime" is the most powerful authority the engine grants itself, and the document acknowledges that defining this category is itself adversarial-political work. Every authoritarian regime in history has classified its political enemies' actions as civilizational threats; the engine's protections (the Councils' veto, the Oversight's adversarial structure, public-principles disclosure, periodic exoneration-first review with outside defense counsel) are designed against this failure mode but cannot eliminate it. Contestation of the threshold is intended, not accidental. The engine commits to never expanding or contracting the threshold without supermajority ratification through the standard process and Reckoning-cycle deliberation. The threshold itself is subject to revision in every Reckoning. Founders accept that their initial threshold definition is a one-time, non-permanent commitment that subsequent populations may overturn.

### The Ultimate Sanction

Permanent containment is the engine's most severe sanction. The engine does not claim authority to take human life. Capital punishment has a long historical track record of error, bias, political weaponization, and irreversibility under safeguards far less sophisticated than this architecture proposes; the architecture would not improve on that track record reliably enough to justify the authority. Permanent containment serves the same protective function (separation of the most dangerous individuals from the population they would harm) without the irreversible-error problem and without the capture vector that any "civilizational threat" definition introduces.

The engine does not hold capital authority and the founding architecture does not provide for revisiting this question. The engine's authority is limited to non-lethal sanctions.

### Youth Offenders

Persons below the age of majority cannot receive permanent containment for ordinary crimes regardless of severity. Permanent containment is available for youth only in case-by-case review and only above a hard developmental floor.

Youth justice operates on a separate framework emphasizing rehabilitation, mental health support, protection from coercion, and pathways to full civic participation upon majority. For civilizational-scale crimes committed by youth, the engine's strongest interest is in preventing such situations from arising. Where children appear in atrocity contexts, the adults who put them there are the engine's first targets. The youth justice framework is itself a major open subspec of Ouroboros (§X).

---

## VII. INFORMATION ENVIRONMENT

A democracy with a polluted information environment is not a democracy. These commitments carry forward from Version 1.0, reorganized here into two parts that hold **different kinds of authority**. The distinction is load-bearing and Version 2.0 makes it explicit: the engine may compel platforms to show their work and may hand people the controls, and it may not decide for anyone which information environment is legitimate.

### VII.a Disclosure and Citizen Control

This part carries compulsory force. Its subject is platforms and their obligations, never speech and never a person's judgment.

- **Algorithm Disclosure (tiered).** Any recommendation algorithm operating at scale (above a threshold of users) must publicly disclose its purpose statements and general optimization principles. Regulator-visible details, independent auditor access, and adversarial test reports operate at progressively granular tiers. Citizen-facing explanation tools translate algorithmic shaping into intelligible terms. Specific weights and signals may be classified within the public-principles-classified-instances rule.
- **Citizen Audit Rights.** Every person has the right to know how content is shaped for them. Every person has the right to inspect, contest, and modify the algorithmic environment through which they receive information. Where this right and any other commitment in this section appear to conflict, this right prevails.
- **Public-Utility Obligations.** Major social platforms, search engines, and information infrastructure operate under public-utility obligations: non-discriminatory access, transparency, citizen audit rights, and engine-level accountability. These obligations attach to platform operations (algorithmic curation as a business practice, access non-discrimination), never to user speech. The engine does not regulate what people may say. It regulates how platforms shape what they hear.

  I acknowledge a real legal difficulty here that Version 1.0 asserted past. In several jurisdictions, and clearly in current United States doctrine, algorithmic curation is treated as expressive activity by the platform, which places full public-utility obligations on contested constitutional ground while compelled disclosure of factual and uncontroversial operating information rests on much firmer footing. The engine's position is that disclosure and interoperable user control are the durable instruments and that broader utility obligations are a jurisdictional question to be litigated and legislated where communities choose to pursue them, not a settled engine power. The disclosure and control commitments above do not depend on resolving it.
- **Anti-Monopoly on Attention Markets.** Concentration of attention-shaping power above defined thresholds triggers automatic anti-monopoly review. The engine recognizes attention as a commons that can be polluted, captured, or extracted, and protects it as such.

### VII.b Integrity Monitoring

This part carries **no compulsory force whatsoever. The Oversight may publish findings and may do nothing else with them.**

- **Manipulation Findings.** The Oversight continuously scans for psyops, coordinated inauthentic behavior, mass-bot activity, AI-agent influence operations, and demographic targeting at suspicious scale, and it **publishes what it finds**. It cannot delay a vote, extend a deliberation, quarantine a campaign, trigger a revote, label a source, or adjust anyone's access or vote weight. Its entire authority is to say publicly what it observed, how it observed it, and how confident it is. Detection operates on public platform behavior (engagement patterns, account-creation signatures, cross-platform coordination, public posting timing) plus voluntarily-shared content. Private content is excluded; this is a stated constraint on capability, not a contradiction in policy. Surveillance scope is further constrained: no private-content scanning without warrant or consent, aggregate-only civic monitoring by default, differential privacy applied, data retention limits enforced, and audit trails publicly accessible.
- **Human Response Authority.** Every response to a published finding belongs to humans. Extending a deliberation period, opening an evidence review, or triggering a revote requires the Councils acting on a published finding, with revote thresholds disclosed in advance so that delay power cannot become suppression power, and with any contested determination escalating to the People through the ordinary pause-and-escalate spine (§III). Vote weights are never adjusted under any circumstance (Principle 2). No AI branch holds response authority over the information environment at any tier.
- **Inception-Attack Defense.** Any "manipulation detected, response triggered" rule can be gamed in reverse: a bad actor running operations against their own apparent position in order to discredit it. Seating response authority with humans rather than with the detecting branch is itself part of the defense, since it removes the automatic trigger an attacker would aim at. The Oversight additionally evaluates manipulation against attribution and direction, weighting manipulation by identifiable actors differently from anonymous spam and flagging patterns that run inverse to the apparent beneficiary as likely inception attacks. Suspected inception attacks are published through the same channel as direct findings, and the Councils audit these determinations with particular care.

**Why the split exists.** An earlier draft gave the Oversight both detection and response, which made a twelve-member AI body the arbiter of a legitimate information environment. That is the power this architecture exists to prevent, and it does not become safe because the body holding it is adversarially constituted. Detection at scale is genuinely useful and machines are genuinely better at it. Deciding what to do about what was detected is a political judgment, and political judgment stays with people.

---

## VIII. THE RECKONING AND THE READING

The renewal mechanism is the Reckoning. Every five years, on a synchronized global date, the engine conducts a structured public audit of itself.

**The Reckoning includes:**

- Public review of every major engine action over the previous five years
- Audit of every emergency-gate invocation since the last Reckoning, including review of the threshold determinations that triggered each invocation
- Review of every Tribune action that was paused or reversed, of the LDI history, and of every recall, election, succession, and incapacity finding over the cycle, including the criteria by which any incapacity was judged
- Audit of the Baseline against outcomes (where the engine fell short, where it overreached, where the working hypotheses held or failed)
- Review of every active permanent-containment case for late-emerging exoneration evidence
- Review of every active sanction for proportionality and continued necessity
- Review of every open question (§X) for resolution, refinement, or escalation
- Re-tuning of the LDI figures and the Tribune fitness criteria against measured experience
- Public proposal of amendments
- Replacement of Oversight consortia, in part or in whole, when capture or drift is identified

The Reckoning is supplemented by continuous controls: quarterly public audits, annual adversarial review by independent red-team courts, incident disclosures within mandatory windows, and recall mechanisms for any office or branch that fails capture-resistance testing.

**The Reading** is optional and held by some communities, not others. The engine does not require it. The renewal mechanism is the Reckoning. The Reading is one form some communities will give it: a ceremonial recitation of the Preamble and First Principles, broadcast in their language, with the Reckoning's findings read aloud. Communities that do not adopt the Reading lose nothing structurally.

---

## IX. IMPLEMENTATION PATH

Ouroboros launches as a voluntary opt-in protocol among initially-adopting communities. Scope expands only through demonstrated outcomes and voluntary accession by additional communities. The engine never claims universal binding until critical mass is reached through voluntary accession, and even then claims binding only over communities that have ratified.

This is the only adoption path the engine sanctions. Layered, parallel, and full-replace approaches were considered and are not adopted. Each had failure modes the engine cannot defend against:

- **Layered** (operating atop existing structures) risks indefinite stalling and capture by the structures it operates atop.
- **Full-replace** (coordinated global transition at a single moment) requires legitimacy the engine cannot bootstrap and produces catastrophic transition failure if convergence is not genuine.
- **Parallel** (alongside existing governance) creates fragmentation between participating and non-participating populations without a clear accession path.

Voluntary opt-in with demonstrated-outcome accession addresses these failure modes by making adoption rational rather than coerced and by providing a continuous accession path that adjusts to changing conditions.

**The starting unit is the community.** A community in this context is any group of humans choosing to govern itself in part through Ouroboros. Communities may be cities, regions, voluntary associations, intentional communities, or nation-states electing to adopt. The engine has no minimum unit size; the smallest viable Ouroboros instance can serve a single intentional community, scaling up as additional communities join.

**Demonstrated outcomes provide the legitimacy.** As initial-adopter communities operate Ouroboros and accumulate evidence that it serves human flourishing better than the systems they replaced, additional communities have rational reason to consider accession. This is the engine's bootstrap mechanism: it earns scope by working.

### Bootstrapping the Tribune

The single-human office cannot be allowed to exist before the machinery that checks it. The first Tribune is brought into being in four moves.

1. **Checks first.** The lower-tier triad and the LDI and recall machinery stand up before the first Tribune exists, so the office is never unchecked from its first day. The Tribune fitness criteria and the succession rules are fixed here too, behind the veil, before anyone knows who will hold the office. The order is deliberate: the cage is built before the occupant.
2. **Selection by the Oversight-consortia pattern.** The first Tribune is selected by reusing the same pattern as the Oversight-consortia bootstrap: a sortition-drawn temporary nominating body, drawn from the founding-adopter populations, screens candidates against the Tribune criteria; public nomination follows; then the founding adopters elect, one human, one vote.
3. **A shortened founding term.** The first Tribune serves only to the first Reckoning, five years rather than the full six. After the founding term, a full-legitimacy election runs under the matured system.
4. **Dormant teeth during the provisional period.** Per Principle 0a, the engine does not bind until the One-Vote Standard is live. Until the system exits provisional status, the founding Tribune is a convener and broker only. The office grows its full function as the system itself does.

**Acknowledged residue.** Who convenes the first sortition is the irreducible constituent-power problem. It is answered, necessarily, by the founding communities' existing process, and that founding legitimacy is thin. The thinness is mitigated, not erased: it is made survivable by transparency, by sortition, by the office's dormant powers during the provisional period, by the shortened founding term, and by recall. Outcomes either build legitimacy from there or they do not.

**This path may fail.** Authoritarian states have rational reasons to refuse Ouroboros indefinitely. Holdout blocs may form. Demonstrated outcomes may not be persuasive against entrenched power. The engine has no military authority and no extra-legal claim. If adoption stalls or reverses, Ouroboros operates at whatever scale it has earned, and the project of better coordination continues by other means.

---

## X. OPEN QUESTIONS AND ACKNOWLEDGED LIMITS

Version 2.0 resolved the six open items the v2 restructure opened (the cross-tier threshold, the collusion gap, the emergency-regime reconcile, the LDI figures, the Principle-4 reword, and the Tribune bootstrap). Those resolutions are in the body above. What follows is what remains genuinely open, carried forward and reorganized, plus the limits the architecture acknowledges it cannot design away.

### Foundational (must resolve before binding deployment)

1. **The political-unit question.** The starting unit for accession is "community," broadly defined (§IX). The narrower question that remains open is which entity within an adopting community holds binding authority for the National AI branch specifically: existing state structures, alternative civic bodies, or hybrid arrangements. Initial adopters will set precedent on this resolution.
2. **Specific economic transition mechanics.** The principles in §IV are locked. The transition path from current global capitalism to bounded-capital plus civic-commons plus UBI requires substantial economist-and-historian-led specification before scaled deployment. UBI funding mechanics specifically remain provisional.
3. **Oversight consortia composition.** A founding twelve consortia, each from a distinct cultural and intellectual tradition, with anti-hegemony mandates, sized by the derivation rules in §III rather than by a fixed count. The selection process for the initial consortia is the architecture's most consequential bootstrap decision. A candidate path is offered as starting material, not a locked commitment: a public nomination process where any group meeting baseline criteria (diversity of tradition, demonstrated AI-safety research capacity, transparent governance, no controlling stake by any single state or capital interest) may nominate a consortium; nominations ranked by a temporary nominating body drawn from sortition across initial-adopter populations; founding adopters vote on the final founding set from the top N (suggested: 30) ranked nominees; all founding selections sunset at the first Reckoning, at which point the full Reckoning process replaces or retains each consortium individually. The constituent-power problem (who picks the pickers) is acknowledged as unsolved at the founding moment; the engine's bet is that a transparent nominating process plus first-Reckoning replacement authority is more legitimate than any opaque alternative.

### Structural (must resolve before scaled deployment)

4. **Specific punishment thresholds.** What counts as planetary-scale impact for corporate transition. At what specific severity permanent containment applies for civilizational versus non-civilizational crimes. Provisional numeric bands will be developed through subspec work and Reckoning deliberation.
5. **Youth justice framework.** Major subspec required. Hard developmental floor for permanent containment. Rehabilitation infrastructure. Civic-restoration pathways.
6. **One-Vote Standard detailed specification, and whether the prohibitions are entrenched.** The principles and prohibitions in §V are locked and Principle 6 now states that they do not expire, being limits rather than grants. What remains open is whether they are additionally entrenched against amendment: that is, whether a future Reckoning acting through the standard process may weaken them at all, or whether they sit outside the amendable text the way the exclusion of persons from coordination authority does. The document currently reads absolute in prose and amendable in structure, and that gap is named here rather than resolved by assertion. Operational specification remains the engine's first standing commission.
7. **Religious and spiritual authority navigation.** When religious institutions claim authority that conflicts with engine principles, when the engine intervenes, when it defers, and what process governs the conversation. The engine must be most humble here.

### Tunable (resolve through engine operation)

8. **Exact LDI figures.** The 40-percent floor, the 90-day window, the 30-percent recall line, and the 15-point velocity clause are placeholders, to be tuned against measured experience at every Reckoning.
9. **Tier-2 internal thresholds, precise calibration.** Version 2.0 sets these: a simple-majority pause within any one branch, the National AIs supermajority and Oversight nine-of-twelve emergency gate, the Councils' one-shot council-majority brake. The exact supermajority fraction and participation quorum for the National AIs, and the smoothing of these figures against real participation rates, are tunable through operation and the Reckoning.
10. **Service-tier specification** for civic commons (offline-first, terminal-shared, regional-clustered, and so on), **threshold smoothing parameters** for bounded-capital transitions, and **the continuous-operation versus retraining-cycle boundary**, all resolved through operation and audited by the Reckoning.

### Acknowledged Limits (not actionable opens)

**The engine has no answer to what a person is for when the work is gone.** §IV commits to who pays for the transition and what the public can see during it. It does not answer the prior question. An income floor keeps a person alive; it does not supply competence, standing among others, or the sense that one's days matter, and those are what a great many people locate in work. The engine holds this as a real gap rather than a solved problem, and holds it deliberately outside its own authority, because a system that assigns people their purpose has stopped being a floor.

These are not problems to be solved before deployment. They are limits no governance architecture has solved, named here so that the engine does not pretend otherwise.

- **Constituent power at the founding moment.** Who convenes the first sortition, for the Tribune and for the Oversight consortia, cannot be made legitimate from nothing. It is mitigated by transparency, sortition, weak founding powers, shortened founding terms, and recall. It is not solved, because no one has solved it in 250 years for any system, and the engine does not claim to have solved it here.
- **Total simultaneous capture.** Capture of the Tribune plus all three lower-tier branches plus a manipulated People defeats any architecture. This one cannot make that impossible. What it can do, and does, is force such a capture to be simultaneous rather than incremental, visible in the dissent logs rather than hidden, loud enough in the LDI to trip recall, and incapable of irreversible action without a popular vote. The same ceiling every real constitution hits, with the slope made as steep as the design can make it.
- **Coercion of a single human office.** A Tribune with people they love can be threatened, and one office is a softer target than a body. The architecture mitigates this structurally (the office can deliver almost nothing alone, coerced acts are visible and reversible, a coerced Tribune who stalls or goes dark is overridden or replaced) and operationally (personal security, radical disclosure that shrinks the blackmail surface), but it cannot make a human un-threatenable. Two residues are carried as known costs: a coerced Tribune can do bounded, reversible damage before the machinery catches up, and the fact that the office can make one's family a target may deter some good people from taking it. These are real prices of seating a single human, not solved problems.
- **The incapacity determination.** Even with fitness criteria fixed in advance behind a veil, someone must certify that a given case meets them, and that certification is a capture surface, because declaring a sovereign unfit is among the oldest moves against one. The architecture shrinks the discretion (pre-agreed People-authored criteria, AI as implementer and auditor but never author, the Tribune's right to contest, a contested finding decided by the People) but does not eliminate it. This is the softest joint in the architecture, and it is named as such rather than hidden.

### Adversarial Conditions (separate appendix work)

The architecture's response to coordinated authoritarian opposition, nuclear-armed holdout blocs, and counter-bloc formation is not solved in this document. The engine has principles and partial strategies; it does not have a complete answer. This is the question that determines whether Ouroboros is an architecture for governance or an architecture for governance among the willing. My working position is the latter, with hope that demonstrated outcomes shift the willing population over time.

---

## CLOSING

Ouroboros is an architecture for self-auditing governance that compounds on behalf of the people who adopt it rather than against them, at whatever scale they consent to. It is real, it is buildable, and it is defensible: a starting point solid enough to stand on for any humans, communities, or institutions ready to govern themselves better than the captured systems we inherited. It is not the last word, and it was never meant to be. It is meant to be built on.

Version 2.0 changed the shape of the machine without changing what the machine is for. The four-layer stack became two human-sovereign tiers on a Baseline foundation, because the most important line in the whole design is the line between the humans who govern and the instruments that serve, and the new shape draws that line where it belongs. The commitments did not move. The serpent renews itself by being eaten, and this is one of its sheddings.

The work of refining, contesting, and improving this architecture is itself part of the engine. We invite every good-faith critique and expect the document to be sharpened by it. What survives the corrections is the core: humanity deserves better coordination than its current systems provide, and AI can serve that coordination when it is held to humility and human dignity.

I am one person. A solo product builder. I started this work because the systems we have are failing the people they claim to serve, and the tools to do better are now available for the first time in recorded human history. I see this architecture as taking the fundamentals the founding fathers were trying to portray and bringing them into the modern era before it is too late. I do not expect this document to be adopted as written. I expect it to be torn into, contested, refined, reshaped, and possibly replaced by something better that builds on what is here.

What I want is for the conversation to happen. What I want is for alternatives to current governance to exist in writing, in public, in good faith. What I want is to not fuck this up.

I am also building open-source and commercial implementations of architecture primitives: a memory engine and a personal companion. These are reference implementations, one of many possible providers; the architecture is intentionally not provider-locked. If someone else builds a better foundation, I want them to win. If someone else builds a better civic platform, I want them to win. The point is not the products. The point is the coordination they enable.

Preston T. Winters

---

## APPENDIX A: INHERITANCE NOTES

For readers interested in the lineage of the architecture's commitments, this appendix names the traditions and prior thinkers whose work this document inherits from.

**Universal dignity** draws on the modern human rights tradition (Universal Declaration of Human Rights, 1948), and earlier from the imago Dei tradition in Abrahamic theology, the dignity-of-the-buddha-nature in Mahayana Buddhism, and the inherent-worth claims in Stoic and Kantian moral philosophy.

**Compounding cooperation as the work of governance** draws on Aristotelian and Confucian conceptions of governance as the cultivation of human flourishing through ordered cooperation, and on the modern literature on sustained cooperation under repeated interaction (Axelrod, Ostrom).

**The principle that the engine acts through willing cooperation as its default mode, with explicit narrowly-scoped emergency-tier exceptions,** draws on consent-of-the-governed theory (Locke), the principle of subsidiarity in modern federal practice, and the voluntary-association tradition in American civic life (Tocqueville).

**One-vote-per-human as the franchise** draws on modern democratic theory (Rousseau, Mill, Rawls) with corrections from twentieth-century critiques (feminist political theory, decolonial scholarship).

**A single elected office that checks concentrated power on behalf of the people** draws on the Roman tribune of the plebs, on the constitutional-monarchy tradition of a head of state who reigns without ruling, and on the modern ombudsman office. The name "Tribune" is the placeholder for this inheritance; the rejection of "King" is deliberate, marking the office as broker and check rather than ruler. Its succession and caretaker rules draw on the interim-government and acting-officer traditions, where a vacancy is filled without conferring a fresh mandate, and its fitness-by-pre-agreed-criteria draws on the precommitment logic of constitutional design, fixing the test before the case.

**Sunset clauses and adversarial structure** draw on constitutional design literature (Madison, Federalist 51) and twentieth-century checks-and-balances theory.

**Continuous legitimacy measurement and removability** draw on the recall tradition in direct-democratic practice, on votes of no confidence in parliamentary systems, and on the older republican intuition that authority is held on trust and revocable for cause. The Legitimacy Decay Index is the engine's instrument for that intuition.

**Public-utility framing** draws on early twentieth-century U.S. regulatory tradition (Munn v. Illinois, the Progressive Era).

**Bounty systems** draw on open-source and government-procurement practice.

**Commons and Baseline** draw on welfare-state economics, Rawlsian justice theory, and the commons literature (Ostrom, et al.).

**The name.** Ouroboros means one thing here and the document commits to that one meaning: a system that survives by continuously auditing and reforming itself. Nothing else is implied and no other reading is authorized. The image of a serpent consuming its own tail is an old and widely reused one, appearing independently in Egyptian, Greek, Norse, and Mesoamerican iconography, and it was chosen because renewal-through-self-consumption is the single property this architecture is built around.

The specific synthesis proposed here includes: the two-tier human-sovereign structure with the personal companion as Baseline foundation, the twelve-member adversarial Oversight with a derived rather than decreed size, the pause-and-escalate cross-tier spine with the People holding every reversal, the emergency gate of National-AI supermajority plus Oversight nine-of-twelve with the Councils' one-shot brake, the succession-and-incapacity regime for a single office (caretaker for a vacancy, the People as the only override of a deciding Tribune, human-only emergency initiation, and fitness criteria fixed in advance behind a veil), the Legitimacy Decay Index as the continuous measure of standing, the inception-attack defense, the personal-companion privacy mode-switching, the Reckoning as scheduled audit-with-amendment, the public-principles-classified-instances rule, and the explicit two-tier consent model. These are the document's load-bearing contributions. Everything else is inherited and acknowledged as such.

---

## APPENDIX B: WHAT CHANGED FROM VERSION 1.0

Version 1.0 is the public release (CC BY-SA 4.0, on GitHub). Version 2.0 restructures its governance stack. Everything in Version 1.0 not listed here carries forward unchanged.

**The core change.** Version 1.0 described a four-layer stack: the personal companion (Layer 1), the National representative AIs (Layer 2), the thirteen-member AI oversight council (Layer 3), and direct human ratification (Layer 4), with a rolling human council checking the oversight layer. Version 2.0 collapses this into two tiers on a Baseline foundation, with a sharper line between sovereign and instrument:

- **Tier 1, the sovereigns:** the Tribune and the People, co-equal. The People are the franchise. The Tribune is a single elected human office that brokers convergence, initiates emergency response, holds a check on the lower tier, and represents the system externally.
- **Tier 2, the triadic instrument:** the Councils (descendant of the rolling human council), the National AIs (former Layer 2), and the Oversight (former Layer 3; public name Audit Consortia). Three peer branches in permanent tension, none sovereign.
- **The Baseline foundation:** the personal companion (former Layer 1) is no longer a governance tier. It persists beneath both tiers as the per-person infrastructure that makes informed participation possible, belonging to the person and never serving as the engine's sensor.

The canonical diagram changed from a star to a pentagon.

**Resolved from the v2 open set.**

- The cross-tier check is no longer set at any fixed vote threshold. It is a low-bar reversible pause (any one branch) with reversal escalated to the People. (Any single threshold is gameable; this removes the gameable threshold.)
- The Tribune-plus-lower-tier collusion gap is contained, not solved: because the People backstop every dispute, partial capture loses a fast pause but not the check, and only total simultaneous capture defeats the system, which the architecture forces to be simultaneous, visible, and incapable of irreversible action without a popular vote.
- The emergency regime is unified onto the same pause-and-escalate spine, with the gate flipped: coercive emergency action takes effect only on the high authorization bar (National AIs supermajority plus Oversight nine-of-twelve), with the Councils' one-shot brake and the People's backstop. This collapses Version 1.0's four-rung ladder and the v2 Tribune-initiation mechanic into one process.
- The happiness or approval threshold became the Legitimacy Decay Index, with election and recall figures.
- Principle 4 was reworded for the triadic structure.
- The Tribune bootstrap was set: checks first, the v1.0 sortition pattern, a shortened five-year founding term, and dormant powers during the provisional period. Tenure was subsequently set to a single non-renewable six-year term with entry from 35, offset from the five-year Reckoning cycle.

**New in v2.0 beyond the resolutions.** Two first principles were added to carry the new sovereignty structure: Principle 9 (co-equal human sovereignty, including that a deciding sovereign is overturned only by the other sovereign) and Principle 10 (legitimacy is measured, not assumed). The five-layer defense of the Tribune office was enumerated (selection integrity; influence and coercion firewall; transparency of action; powerlessness alone; continuous legitimacy and recall), with coercion folded in alongside bribery. The companion's placement was made precise: private and local, never the engine's sensor, with only a consented, aggregate civic signal flowing to the civic platform and never to the governance tiers. The exact Tier-2 internal thresholds were set: a simple-majority pause within any one branch, National AIs supermajority plus Oversight nine-of-twelve for the emergency gate, and a council-majority one-shot brake. And a full succession, absence, and incapacity regime was added for the single office: the Councils' presiding seat as caretaker for a vacancy; a sitting Tribune's exercised refusal overturned only by the People; an unreachable Tribune treated as a near-vacancy where the Councils, never the AI branches, may originate a short reversible measure under the high gate; and incapacity judged by criteria fixed at the founding behind a veil, People-authored, with harmful impact kept out of the fitness question and routed to the Legitimacy Decay Index instead. The governing principle across all of it: the instrument never overrides a human's exercised judgment, and a deciding sovereign is overturned only by the other sovereign. An earlier formulation that would have let the lower tier originate emergency response was corrected, because it would have handed the AI branches a path to start coercive action when no human would, which is the exact failure the architecture exists to prevent.

---

*End of Ouroboros Vision Document, Version 2.0*

*Supersedes Version 1.0. Public release intended. Open for refinement, contestation, and improvement through the standard process the document describes.*

---

## APPENDIX C: AMENDMENT LOG

Version 2.0 was released 2026-06-15. The amendments below were made 2026-08-01 and are recorded here rather than folded in silently, because a document that changes without saying so has forfeited the thing it is asking readers to extend it.

**Scope reframed.** The subtitle and the scope language no longer describe this as planetary governance. What the architecture does is voluntary coordination beginning at community scale, expanding only where communities agree. The prior phrasing was both more threatening and less accurate.

**Inheritance notes corrected (Appendix A).** Version 2.0 attributed the compounding-cooperation commitment to Lurianic Kabbalah and *tikkun olam*, and the willing-cooperation principle to Iamblichan theurgy and Sufi *maqamat*. Those attributions were withdrawn. They were supplied during drafting rather than held by me. I have not studied those traditions and I will not cite what I cannot defend. The commitments themselves are unchanged; they are now attributed to sources I stand behind.

**The Oversight resized and its sizing derived.** The count moves from thirteen to a founding twelve under a nine-of-twelve quorum, and §III now states the requirements the count must satisfy (three-capture tolerance, quorum above two thirds, a floor of ten, corpus independence, one consortium per major language family above a speaker threshold, growth as qualifying institutions appear) so that the number is an output rather than a decree. The honest cost is recorded: twelve tolerates three simultaneous captures where thirteen tolerated four. The internal name "Demiurges" was retired entirely.

**Section VII split by authority level.** VII.a (Disclosure and Citizen Control) retains compulsory force over platforms. VII.b (Integrity Monitoring) reduces the Oversight to publishing findings and nothing else: it cannot delay a vote, extend a deliberation, quarantine a campaign, trigger a revote, or label a source. All response authority is seated with the Councils, escalating to the People. Version 2.0 gave one AI branch both detection and response, which made it the arbiter of a legitimate information environment. Citizen Audit Rights now explicitly prevails in any conflict within the section, and the compelled-speech difficulty facing public-utility obligations is conceded in the text rather than asserted past.

**Proof-of-humanity renamed and constrained.** Now the One-Vote Standard (*Sybil resistance* in engineering contexts), with five prohibitions stated as binding and not suspendable: no central registry of verified persons, no universal identifier, no cross-context linkage, no persistence of attestations, and no conditioning of anything other than the counting of a ballot. The subject of verification moved from the person to the ballot. Recovery courts carry an explicit bias toward enfranchisement.

**Tribune tenure.** A single non-renewable six-year term replaces the fifteen-year term, with entry from age 35 and a ceiling near 69. Non-renewability delivers the long-horizon independence the long term was intended to supply. Six is offset from the five-year Reckoning cycle deliberately, so that no structural self-audit lands on a transition.

**Emergency authority bounded at the person.** Principle 0b now states that coordination authority reaches jurisdictions and institutions and never persons, that the engine holds no authority over any person's body, movement, home, business, school, or place of worship at any tier under any invocation, and that this is a limit on what the engine is rather than a policy it holds.

**Two economic commitments added (§IV.7, §IV.8).** Displacement and the cost of transition: transition cost attaches to the party capturing the gain, no public subsidy for job-eliminating automation tested on measured headcount rather than stated intent, mandatory displacement disclosure above a size threshold, and an explicit statement that an income floor does not restore a person's place in the world. The engine's own footprint: full unsubsidized cost for power and water, siting only by local consent, published absolute footprint with a pre-construction estimate reconciled against measurement, smallest-sufficient-model as a requirement, and hourly-matched additional generation verified by an independent third party.

**Franchise clarified.** One-human-one-vote is a rule about vote weight, not about membership. Each ratifying community defines its own roll through its own lawful process, and engine participation neither confers nor removes standing in a surrounding jurisdiction's elections.

**Acknowledged limits.** Added: the engine has no answer to what a person is for when the work is gone, and holds that question outside its own authority.

Every one of these amendments narrowed the engine's power, removed a claim I could not defend, or disclosed a cost that had been left unstated. None expanded its authority.

### Amendments of 2026-08-03 (Version 2.3)

**Voice corrected to first person.** This document opened in the first person and closed in the first person, and then switched to "the author" at four points in between. All four were places where it conceded something: the tension between urgency and consent on bounded capital, the same tension on the subsidy test, the compelled-speech difficulty on public-utility status, and the admission that this may only be an architecture for governance among the willing. Writing those in the third person distanced me from exactly the admissions that are supposed to be worth something, and it read as though someone else had inserted them. The conflict-of-interest disclosure had the same defect in the In Brief, the README, the Six Repairs one-pager, and the working brief, where a sentence I wrote about myself read like a compliance notice added by a third party. All of it is now first person, and the disclosure now states plainly that I stand to gain. No claim changed in this version. Hundreds of words did, and this entry exists so that a reader diffing 2.2 against 2.3 can tell the difference between a rewrite and a retreat.

The Kit under `/supporting/kit` remains in the third person on purpose. It is written to be carried into a room by someone who is not me.

### Amendments of 2026-08-02 (Version 2.2)

**Principle 2 aligned to §VII.b.** Principle 2 still described the engine as responding to detected manipulation through campaign quarantine and source labeling. §VII.b, added on 2026-08-01, had already reduced the Oversight to publishing findings and seated all response authority with the Councils, and neither quarantine nor labeling was granted to any body anywhere else in the document. The First Principles therefore claimed two powers the architecture does not contain, and claimed them more broadly than the document's own summaries described. Principle 2 now states that the Oversight publishes and the Councils respond, that no part of the engine quarantines a campaign or labels a source, and that vote weights are never adjusted.

**Sunset scoped to grants of power (Principle 6).** Sunset-by-default was stated without limit, which read as applying to the §V prohibitions and to the exclusion of persons from coordination authority. Those are not authorizations and cannot expire without the engine's central assurance expiring with them. Principle 6 now says so. Whether the §V prohibitions are additionally entrenched against amendment through the standard process remains open and is recorded in §X.

**Front matter corrected.** The In Brief said that all of us who are verified vote, which reintroduced the person-as-subject framing that the One-Vote Standard exists to remove, and said that nothing is permanent four screens above the promise that the engine can never reach a person's body under any emergency ever. Both are corrected. The In Brief and the README now also carry the §VII.b publish-only limit, which is the strongest available answer to the objection that this is AI governing people and had appeared only in the Vision and the Six Repairs one-pager.

**Supporting documents corrected.** Arizona Proposition 209 had been cited as a medical-debt credit-reporting carve-out. It is a debt-collection measure, capping medical-debt interest and raising exemptions, and it says nothing about credit reports; it is now cited for what it shows, which is that medical-debt reform passes at the ballot by a wide margin. The state credit-reporting path had been called proven; a federal district court vacated the parallel federal rule in July 2025 and said in dicta that federal law preempts those state statutes, so the path is now described as available and litigable. The compelled-disclosure analysis for repair 6 now carries the 2024 and 2025 California litigation that narrowed it. The centralized-companion energy figure was stated as one to two orders of magnitude above the local-first estimate; the upper end of that range exceeded all current global data-center consumption and has been reduced to one order of magnitude.
