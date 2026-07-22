# Mizan Domain Adaptation — Modes 3/4/5 Beyond Software

Modes 3, 4, and 5 are software costumes on three universal patterns:

- **Mode 3 (audit):** the claim-bearing artifact is never the
  behavior-bearing artifact — verify every hop between them.
- **Mode 4 (anomaly registry):** anomaly → mechanism hypothesis →
  rival hypotheses → discriminating test. Never close on the first
  story that fits.
- **Mode 5 (commitment gate):** any forward resource commitment carries
  value/cost/dependency claims — tier them, lock thresholds and a kill
  condition BEFORE committing, force alternatives incl. the null.

## The adaptation recipe (use this for any domain not listed)

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

## Domain catalog

### 1. Data & Analytics
- Hop map: metric label / dashboard title / report narrative ↔ the
  actual query (SQL/pipeline) ↔ the raw data. "Active users" on the
  chart vs. what the WHERE clause counts.
- Mode 4 = metric-anomaly investigation: rival hypotheses for any
  drop/spike — tracking change, seasonality, mix shift (Simpson's
  paradox), real effect.
- Confounds: instrumentation changes, backfills, timezone/window
  definitions, survivorship in cohorts.
- Prior art: data-quality testing (dbt tests ≈ assertions on claims).

### 2. Marketing & Growth
- Hop map: campaign brief / landing-page promise ↔ product's actual
  behavior; audience claims ↔ survey/telemetry evidence.
- Mode 5 = campaign gate: CAC/conversion threshold locked pre-launch;
  spend cap = kill condition; null alternative ("don't run it") priced.
- Confounds: novelty effect, seasonality, cannibalization of sibling
  channels, peeking (early stopping = R1 violation).
- Prior art: proper A/B methodology IS preregistration; [Y] was
  practically invented for marketing copy.

### 3. Sales & CRM
- Hop map: pipeline-stage field / "champion identified" claim ↔
  activity log, buyer-side artifacts (emails, meetings).
- Mode 5 = deal-qualification gate (MEDDIC/BANT = loose prior art);
  disqualification criteria = kill condition; close-probability =
  preregistered prediction.
- Mode 4 = loss analysis: seller's post-hoc story vs. buyer's stated
  reasons vs. rival mechanisms.
- Confounds: quarter-end pressure, discount effects, single-threaded
  contact masquerading as consensus. DC-001 is culturally hardest here.

### 4. Academic / Scientific Research
- Native habitat — Modes 1/2 came from here. The genuinely new
  transfer is Mode 3 on literature: abstract claims ↔ methods/results
  evidence (abstract-inflation is documented tier drift), citation
  claims ↔ what the cited paper actually shows.
- Prior art: preregistration, registered reports, PRISMA.

### 5. Finance & Investment Decisions
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

### 6. Operations / Manufacturing / Logistics
- Mode 4 = root-cause analysis formalized: 5-Whys chains are mechanism
  hypotheses that usually skip rival hypotheses and discriminating
  tests — Mizan adds exactly those. "Fix worked" after a process change
  follows the revert-check rule where feasible.
- Mode 3: SOP/work-instruction claims ↔ what the floor actually does.
- Confounds: Hawthorne effect (observation changes behavior),
  concurrent changes, demand mix.
- Prior art: A3/8D reports, Six Sigma DMAIC.

### 7. Security & Incident Response
- Mode 4 is nearly isomorphic to IR: symptom (alert/IOC) → intrusion
  hypothesis → rival hypotheses (misconfig? scanner noise? true
  compromise?) → discriminating evidence. Post-incident reports are
  HARKing magnets — timeline claims need artifact citations.
- Mode 3: security-posture claims (docs, compliance answers) ↔ actual
  configs and controls.
- Prior art: blameless postmortems (= DC-001's ancestor), ATT&CK
  hypothesis hunting.

### 8. Hiring & People Decisions
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

### 9. Procurement & Vendor Selection
- Mode 3: vendor claims (SLA, benchmark decks, "enterprise-ready") ↔
  contract terms ↔ measured behavior in POC. Vendor benchmarks are
  [Y] until reproduced.
- Mode 5 = RFP gate: requirements as tiered claims; dependency claims
  ("integrates with our stack") verified BEFORE signing; exit/switch
  cost recorded as kill-condition economics.
- Confounds: demo-environment vs. production, reference-customer
  selection bias.

### 10. Legal / Contracts / Compliance
- Mode 3: policy/compliance claims ("we are GDPR-compliant") ↔ actual
  clauses, actual data flows; marketing promises ↔ contractual
  obligations (a promise not in the contract is [H] at best).
- Mode 4: dispute analysis — each side's narrative as rival hypotheses
  against the documentary record.
- Note: structures the evidence; not legal advice.

### 11. Product / UX Research
- Mode 3: "users want X" claims ↔ interview transcripts (what was
  actually said vs. the summary — summarization drift is tier drift),
  usability-report claims ↔ session recordings.
- Confounds: leading questions, sample skew toward vocal users,
  say-do gap (stated preference vs. behavior).
- Prior art: continuous-discovery practices, evidence-based design.

### 12. Content / Journalism / Technical Writing
- Mode 3: headline ↔ body ↔ source (headline inflation = tier drift);
  every factual claim's hop to a primary source.
- Mode 5 = story/content gate: audience-value claim, distribution
  dependency claims, evergreen-vs-decay expectation as preregistered
  prediction.
- Prior art: fact-checking desks; [Y] and [KKE] map directly onto
  editorial standards.

### 13. Policy / Program Evaluation (public sector, NGO)
- Mode 5 = program gate: theory-of-change as a chain of tiered claims;
  sunset clause = kill condition (rare in practice, transformative
  when preregistered).
- Confounds: selection into programs, secular trends, regression to
  the mean in targeted populations.
- Ground-truth latency: years — underpowered is the norm; say so in
  every entry.
- Prior art: RCT evaluation culture, logic models.

### 14. Personal Experimentation (health, fitness, productivity)
- Mode 4 on n=1: symptom → mechanism hypothesis → the cheapest
  discriminating change, ONE variable at a time; washout periods as
  the personal symmetric control.
- Confounds: placebo/expectancy, regression to the mean (you start
  interventions at your worst), season/sleep/stress co-movement.
- Permanent honesty labels: n=1 means most closures cap at [H]; that
  is the honest ceiling, not failure.
- Note: structures self-observation; medical decisions belong with
  clinicians.

## Anti-pattern for this file

Do not force all five gate fields onto domains where they parody
themselves. If a domain entry's kill condition or metric feels
theatrical, record the honest version: "no credible instrument exists
→ claim stays [S]" is a legitimate, useful outcome.
