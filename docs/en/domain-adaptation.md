<!-- GENERATED PAGE - do not edit here.
     Source of truth: skill/mizan/references/domain-adaptation.md
     Regenerate:      python tools/sync_en_docs.py
     CI (`--check`) fails if this page drifts from its source. -->

# Domain adaptation — modes 3/4/5 beyond software

> **Mirrored from the skill package.** This is the canonical English text that
> Claude actually loads, published here so it can be read next to its Turkish
> mirror instead of only on GitHub. Edit the source above, not this
> page; the Turkish mirror is `docs/tr/alan-uyarlama.md`.

## Mizan Domain Adaptation — Modes 3/4/5 Beyond Software

Modes 3, 4, and 5 are software costumes on three universal patterns:

- **Mode 3 (audit):** the claim-bearing artifact is never the
  behavior-bearing artifact — verify every hop between them.
- **Mode 4 (anomaly registry):** anomaly → mechanism hypothesis →
  rival hypotheses → discriminating test. Never close on the first
  story that fits.
- **Mode 5 (commitment gate):** any forward resource commitment carries
  value/cost/dependency claims — tier them, lock thresholds and a kill
  condition BEFORE committing, force alternatives incl. the null.

### The adaptation recipe (use this for any domain not listed)

Answer six questions; the answers ARE the domain module. Question 0 is
the one that decides how much of the software-verification loop actually
survives the move:

0. **Arbiter:** who returns the verdict on a locked threshold in this
   domain — a deterministic executor, an independent instrument, a third
   party, or the claim's own author? Software's rigor is borrowed from
   the runtime, not from the fact that the artifact is code; most domains
   inherit the protocol and lose the judge. Answer honestly per entry
   (schema field `hypothesis.arbiter`, rule R8): `author` caps the claim
   at a permanent [KKE], `none` means the threshold is decorative and the
   entry stays [S]. A domain where every arbiter is `author` is not
   thereby un-auditable — it just cannot produce [K], and saying so is
   the whole point.

1. **Hop map:** where do claims live vs. where does evidence live?
   (In code: comment vs. implementation. In sales: CRM field vs.
   activity log.)
2. **Instruments:** what produces the numbers, and what are its known
   distortions?
3. **Confound catalog:** what boring explanation produces the same
   result in this domain?
4. **Ground-truth latency:** how fast and how cheaply can a claim be
   refuted? (Seconds in code; quarters in marketing.) Set expectations:
   slow domains make "underpowered" the NORM, not the exception.
5. **Prior art:** which existing discipline in this domain is already a
   loose version of this? (Name it in entries; Mizan formalizes, it
   rarely invents.)

Universal rules that transfer unchanged: append-only history; refuted
entries never deleted; surprising positives wait for a symmetric
control; where a symmetric control is unethical or impossible
(human-subject domains), the claim carries a PERMANENT [KKE] as an
honesty label, not a defect. **DC-001 applies wherever individual hit
rates could be weaponized** (sales forecasts, analyst calls, hiring
decisions): individual scores stay with the individual; management
sees aggregates only.

### Domain catalog

Every entry answers question 0 and question 4 on one line, **Arbiter /
latency**, because those two set the entry's ceiling before any threshold
is written: an `author` arbiter caps at a permanent [KKE] (R8), and a
latency of quarters or years makes "underpowered" the expected outcome.
Where a domain has two arbiters for two kinds of claim, both are named —
the split is usually the most useful thing the line says.

#### 1. Data & Analytics
- Hop map: metric label / dashboard title / report narrative ↔ the
  actual query (SQL/pipeline) ↔ the raw data. "Active users" on the
  chart vs. what the WHERE clause counts.
- Mode 4 = metric-anomaly investigation: rival hypotheses for any
  drop/spike — tracking change, seasonality, mix shift (Simpson's
  paradox), real effect.
- Confounds: instrumentation changes, backfills, timezone/window
  definitions, survivorship in cohorts.
- Prior art: data-quality testing (dbt tests ≈ assertions on claims).
- Arbiter / latency: `runtime` for "does the query count what the label
  says" — re-run it, [K] is reachable; `instrument` for an anomaly's
  cause. Minutes to days.

#### 2. Marketing & Growth
- Hop map: campaign brief / landing-page promise ↔ product's actual
  behavior; audience claims ↔ survey/telemetry evidence.
- Mode 5 = campaign gate: CAC/conversion threshold locked pre-launch;
  spend cap = kill condition; null alternative ("don't run it") priced.
- Confounds: novelty effect, seasonality, cannibalization of sibling
  channels, peeking (early stopping = R1 violation).
- Prior art: proper A/B methodology IS preregistration; [Y] was
  practically invented for marketing copy.
- Arbiter / latency: `instrument` (the experiment platform, analytics)
  for conversion claims; `author` for positioning and brand claims, which
  therefore carry a permanent [KKE]. Weeks to quarters — attribution
  windows make most closures underpowered.

#### 3. Sales & CRM
- Hop map: pipeline-stage field / "champion identified" claim ↔
  activity log, buyer-side artifacts (emails, meetings).
- Mode 5 = deal-qualification gate (MEDDIC/BANT = loose prior art);
  disqualification criteria = kill condition; close-probability =
  preregistered prediction.
- Mode 4 = loss analysis: seller's post-hoc story vs. buyer's stated
  reasons vs. rival mechanisms.
- Confounds: quarter-end pressure, discount effects, single-threaded
  contact masquerading as consensus. DC-001 is culturally hardest here.
- Arbiter / latency: `instrument` (won/lost in the CRM) for a forecast;
  the seller's own loss story is `author`, and only buyer-side evidence
  (`third_party`) lifts it. One sales cycle — weeks to months.

#### 4. Academic / Scientific Research
- Native habitat — Modes 1/2 came from here. The genuinely new
  transfer is Mode 3 on literature: abstract claims ↔ methods/results
  evidence (abstract-inflation is documented tier drift), citation
  claims ↔ what the cited paper actually shows.
- Confounds: publication bias, the garden of forking paths, small-sample
  effects that regress on replication, a review cited in place of the
  primary study it summarises.
- Prior art: preregistration, registered reports, PRISMA.
- Arbiter / latency: for a citation hop the instrument is reading the
  cited paper — anyone can, so [K] is reachable in hours; for a finding,
  `third_party` replication, in years.

#### 5. Finance & Investment Decisions
- Hop map: investment thesis ↔ position; "we believe X because Y" ↔
  the data Y actually shows.
- Mode 5 = position gate: entry thesis with refutation condition
  (thesis-invalidation ≠ price stop-loss — record both), sizing as
  cost claim.
- Confounds: market beta dressed as alpha, regime luck, survivorship
  in backtests, overfitting to history.
- Prior art: investment memos + pre-mortems; trading journals are
  informal Mode 4 registries.
- Note: Mizan structures the reasoning; it is not financial advice
  machinery and does not pick trades.
- Arbiter / latency: `instrument` (reported financials) for the thesis's
  operating milestones. Price is NOT the thesis's arbiter: it moves for
  reasons the thesis does not claim, so a price move alone neither
  confirms nor refutes it. Quarters for milestones; a full regime for a
  strategy claim.

#### 6. Operations / Manufacturing / Logistics
- Mode 4 = root-cause analysis formalized: 5-Whys chains are mechanism
  hypotheses that usually skip rival hypotheses and discriminating
  tests — Mizan adds exactly those. "Fix worked" after a process change
  follows the revert-check rule where feasible.
- Mode 3: SOP/work-instruction claims ↔ what the floor actually does.
- Confounds: Hawthorne effect (observation changes behavior),
  concurrent changes, demand mix.
- Prior art: A3/8D reports, Six Sigma DMAIC.
- Arbiter / latency: `instrument` (defect counts, cycle times); a
  feasible revert-check makes the verdict nearly `runtime`. A shift to a
  few weeks.

#### 7. Security & Incident Response
- Mode 4 is nearly isomorphic to IR: symptom (alert/IOC) → intrusion
  hypothesis → rival hypotheses (misconfig? scanner noise? true
  compromise?) → discriminating evidence. Post-incident reports are
  HARKing magnets — timeline claims need artifact citations.
- Mode 3: security-posture claims (docs, compliance answers) ↔ actual
  configs and controls.
- Prior art: blameless postmortems (= DC-001's ancestor), ATT&CK
  hypothesis hunting.
- Arbiter / latency: `runtime` for a configuration claim — read the
  config, run the control. For "no compromise" there is no arbiter that
  can return a pass: silence caps at [KKE] (R26). For an asset-centred
  pass rather than an incident, use Mode 7 (`security-probe.md`). Minutes
  for config; intrusion dwell time is measured in months.

#### 8. Hiring & People Decisions
- Hop map: job-description and scorecard claims ("strong systems
  thinker") ↔ the evidence that produced them (work sample, the
  interview answer itself, references).
- Mode 5 = hire gate: role's problem claim, success metric at 90 days
  locked before the offer, kill condition for the ROLE (not the
  person) if premises fail.
- Interview signals = hypotheses; preregistered predictions per
  interviewer make calibration measurable over many hires.
- Confounds: halo effect, market conditions, onboarding quality
  confounded with selection quality.
- HARD constraint: DC-001 fully applies; per-interviewer hit rates
  never become performance weapons. Human-subject symmetric controls
  are mostly impossible → permanent [KKE] labels are normal here.
- Prior art: structured interviewing, work-sample tests.
- Arbiter / latency: almost always `author` or a manager as
  `third_party`; a 90-day metric is rarely an instrument → [K] is close
  to unreachable, say so. 90 days to a year, with small n.

#### 9. Procurement & Vendor Selection
- Mode 3: vendor claims (SLA, benchmark decks, "enterprise-ready") ↔
  contract terms ↔ measured behavior in POC. Vendor benchmarks are
  [Y] until reproduced.
- Mode 5 = RFP gate: requirements as tiered claims; dependency claims
  ("integrates with our stack") verified BEFORE signing; exit/switch
  cost recorded as kill-condition economics.
- Confounds: demo-environment vs. production, reference-customer
  selection bias.
- Prior art: POC bake-offs, weighted scoring matrices.
- Arbiter / latency: `instrument` (POC measurement) only if the POC was
  designed before signing; a vendor's own benchmark is the vendor as
  `author`. Weeks for a POC; months for real SLA behaviour.

#### 10. Legal / Contracts / Compliance
- Mode 3: policy/compliance claims ("we are GDPR-compliant") ↔ actual
  clauses, actual data flows; marketing promises ↔ contractual
  obligations (a promise not in the contract is [H] at best).
- Mode 4: dispute analysis — each side's narrative as rival hypotheses
  against the documentary record.
- Confounds: selective document production, hindsight shaping each
  side's narrative, a clause read without the definitions it depends on.
- Prior art: legal due diligence; control testing in compliance audits
  (SOC 2, ISO 27001).
- Arbiter / latency: reading the clauses against the actual data flows
  is instrument-like for Mode 3; the real `third_party` (court,
  regulator, auditor) usually arrives only with a dispute. Days for the
  document check; years for a dispute.
- Note: structures the evidence; not legal advice.

#### 11. Product / UX Research
- Mode 3: "users want X" claims ↔ interview transcripts (what was
  actually said vs. the summary — summarization drift is tier drift),
  usability-report claims ↔ session recordings.
- Confounds: leading questions, sample skew toward vocal users,
  say-do gap (stated preference vs. behavior).
- Prior art: continuous-discovery practices, evidence-based design.
- Arbiter / latency: `instrument` (task success, behavioural telemetry)
  or moderated sessions as `third_party`; the researcher's synthesis is
  `author`. Days for sessions; weeks for telemetry. For auditing an
  application's UX rather than research claims, the sibling skill
  ux-mizan carries the full procedure.

#### 12. Content / Journalism / Technical Writing
- Mode 3: headline ↔ body ↔ source (headline inflation = tier drift);
  every factual claim's hop to a primary source.
- Mode 5 = story/content gate: audience-value claim, distribution
  dependency claims, evergreen-vs-decay expectation as preregistered
  prediction.
- Confounds: two outlets citing the same wire story counted as two
  sources, survivorship in "what performed", a platform algorithm change
  read as audience preference.
- Prior art: fact-checking desks; [Y] and [KKE] map directly onto
  editorial standards.
- Arbiter / latency: the primary source as `third_party` for a factual
  claim — [K] reachable within hours; `instrument` (analytics) for a
  content-value prediction, over weeks.

#### 13. Policy / Program Evaluation (public sector, NGO)
- Hop map: program reports (activities delivered — outputs) ↔ the
  outcome data those activities were meant to move. Outputs are not
  outcomes; a report that counts the first is silent on the second.
- Mode 5 = program gate: theory-of-change as a chain of tiered claims;
  sunset clause = kill condition (rare in practice, transformative
  when preregistered).
- Confounds: selection into programs, secular trends, regression to
  the mean in targeted populations.
- Arbiter / latency: an independent evaluator as `third_party`,
  `instrument` where administrative data exists; the implementing body
  judging itself is `author`. Years — underpowered is the norm; say so
  in every entry.
- Prior art: RCT evaluation culture, logic models.

#### 14. Personal Experimentation (health, fitness, productivity)
- Hop map: the felt improvement or diary entry ↔ the measured value
  (wearable, lab result, logged output) — the gap between them is the
  expectancy confound made visible.
- Mode 4 on n=1: symptom → mechanism hypothesis → the cheapest
  discriminating change, ONE variable at a time; washout periods as
  the personal symmetric control.
- Confounds: placebo/expectancy, regression to the mean (you start
  interventions at your worst), season/sleep/stress co-movement.
- Permanent honesty labels: n=1 means most closures cap at [H]; that
  is the honest ceiling, not failure.
- Prior art: quantified-self practice, n-of-1 trials in clinical
  research.
- Arbiter / latency: the subject is also the `author`, so closures sit
  at [H] or [KKE]; an `instrument` (wearable, lab test) raises what it
  measures, not the felt claim. Days to weeks per cycle, washout
  included.
- Note: structures self-observation; medical decisions belong with
  clinicians.

### Anti-pattern for this file

Do not force all five gate fields onto domains where they parody
themselves. If a domain entry's kill condition or metric feels
theatrical, record the honest version: "no credible instrument exists
→ claim stays [S]" is a legitimate, useful outcome.
