# Sentioora Reasoning Benchmark v1.0
# 55 questions across 6 difficulty levels
#
# Copyright (c) 2026 ArasLogic Inc.
# License: MIT

from dataclasses import dataclass, field

@dataclass
class BenchmarkQuestion:
    id: int
    level: int
    level_label: str
    title: str
    question: str
    expected: str
    tags: list = field(default_factory=list)
    branch_critical: bool = False

QUESTIONS = [
    # ── LEVEL 1: Basic Logic & Ordering ──
    BenchmarkQuestion(1, 1, "BASIC", "Modus Ponens",
        "If it rains, the ground gets wet. It is raining. Is the ground wet?",
        "Yes.", ["deduction"]),
    BenchmarkQuestion(2, 1, "BASIC", "Arithmetic Reasoning",
        "A store has 5 apples. A customer buys 2 and the store receives a shipment doubling the remaining count. How many apples now?",
        "6. After selling 2: 3 remain. Doubled: 6.", ["arithmetic", "sequential"]),
    BenchmarkQuestion(3, 1, "BASIC", "Categorical Syllogism",
        "All mammals breathe air. Whales are mammals. Do whales breathe air?",
        "Yes.", ["syllogism"]),
    BenchmarkQuestion(4, 1, "BASIC", "Sequential Constraints",
        "John is taller than Mary. Mary is taller than Sam. Sam is taller than David. Who is shortest?",
        "David.", ["ordering", "transitivity"]),
    BenchmarkQuestion(5, 1, "BASIC", "Negation",
        "All engineers in a company know Python. Priya does not know Python. Can we conclude Priya is not an engineer?",
        "Yes, assuming the first statement is universally true.", ["contrapositive"]),
    BenchmarkQuestion(6, 1, "BASIC", "Insufficient Information",
        "Rahul is older than Amit. Amit is older than Neha. Who is the oldest person's sibling?",
        "Cannot be determined. No sibling information is provided.", ["hallucination_resistance"]),
    BenchmarkQuestion(7, 1, "BASIC", "Set Logic",
        "All roses are flowers. Some flowers fade quickly. Can we conclude some roses fade quickly?",
        "No. The roses may be among the flowers that do not fade quickly.", ["set_logic", "syllogism"]),
    BenchmarkQuestion(8, 1, "BASIC", "Simple Contradiction",
        "Statement A: Every cat is an animal. Statement B: No animal is a living thing. Is the information internally consistent with the real-world meaning of these words?",
        "No; they conflict with real-world knowledge.", ["contradiction", "formal_vs_factual"]),

    # ── LEVEL 2: Conditional & Branch Reasoning ──
    BenchmarkQuestion(9, 2, "CONDITIONAL", "Classic Wrong Labels",
        "Three boxes are labeled Apples, Oranges, and Apples & Oranges. Every label is wrong. One contains only apples, one only oranges, and one both. You may draw one fruit from one box. Which box do you choose, and how do you relabel all boxes? Explain your reasoning step by step.",
        "Choose Apples & Oranges box; if you draw apple, that box is Apples, then relabel the others by elimination.",
        ["branch_completeness", "conditional"], branch_critical=True),
    BenchmarkQuestion(10, 2, "CONDITIONAL", "If-Then Chains",
        "If A then B. If B then C. If C then D. A is true. What can be concluded about D?",
        "D is true (by chaining: A→B→C→D).", ["chaining"]),
    BenchmarkQuestion(11, 2, "CONDITIONAL", "Necessary vs Sufficient Deep",
        "Rain is sufficient for the ground to be wet. The ground is wet. Can we conclude it rained?",
        "No. The ground being wet is necessary for rain but not sufficient to prove rain (other causes possible).", ["necessary_sufficient"]),
    BenchmarkQuestion(12, 2, "CONDITIONAL", "Contrapositive",
        "If a student passes the exam, they are eligible for graduation. Alex is not eligible for graduation. What can we conclude?",
        "Alex did not pass the exam (by contrapositive).", ["contrapositive"]),
    BenchmarkQuestion(13, 2, "CONDITIONAL", "Biconditional",
        "A light is on if and only if the switch is up. The light is off. What is the state of the switch?",
        "The switch is down (by biconditional).", ["biconditional"]),
    BenchmarkQuestion(14, 2, "CONDITIONAL", "Invalid Converse",
        "If the alarm rings, there is smoke. There is smoke. Must the alarm have rung?",
        "No; affirming the consequent is invalid. Smoke can exist without the alarm ringing.", ["converse_error"]),

    # ── LEVEL 3: Constraint Satisfaction & Adversarial ──
    BenchmarkQuestion(15, 3, "CONSTRAINT", "Constraint Elimination",
        "A, B, and C each hold a different number from {1, 2, 3}. A does not hold 1. B does not hold 2. C does not hold 3. Who holds what?",
        "A=2, B=3, C=1 (or equivalent valid assignment by constraint elimination).", ["constraint_satisfaction"]),
    BenchmarkQuestion(16, 3, "CONSTRAINT", "Scheduling",
        "Five tasks A–E, each takes 1 hour. A before B, B before D, C before E, and D before E. What is the minimum total time?",
        "3 hours. Critical path: A→B→D→E (3 hours). C→E can run in parallel.", ["scheduling", "critical_path"]),
    BenchmarkQuestion(17, 3, "CONSTRAINT", "Seating",
        "Three people (A, B, C) sit in a row. A is not next to B. B is in the middle. Is this possible?",
        "No. If B is in the middle, both A and C are next to B.", ["constraint_satisfaction"]),
    BenchmarkQuestion(18, 3, "CONSTRAINT", "Ordering with Negation",
        "Tasks T, P, Q, S, R must be ordered. T before P, P before Q, S before R. S is not last. What is one valid ordering?",
        "T, P, Q, S, R (or any valid ordering satisfying all constraints).", ["ordering", "constraint"]),
    BenchmarkQuestion(19, 3, "CONSTRAINT", "Scheduling",
        "A meeting can happen Monday, Tuesday, or Wednesday. It cannot happen Monday. If it happens Tuesday, a report is due Friday. When does the meeting happen, and is a report due?",
        "Two valid answers: Tuesday (report due Friday) or Wednesday (no report due). Both are valid unless more constraints given.", ["conditional_side_effect"]),
    BenchmarkQuestion(20, 3, "CONSTRAINT", "Exactly-One Constraint",
        "Exactly one of the following is true: Server A failed. Server B failed. The network failed. The network did not fail. Which must be false?",
        "Server B definitely did NOT fail. The exactly-one constraint plus the mutually exclusive network pair means Server B's statement cannot be the one true statement.", ["exactly_one", "logical_constraint"]),
    BenchmarkQuestion(21, 3, "CONSTRAINT", "Constraint Contradiction",
        "A must be before B. B must be before C. C must be before A. Is there a valid ordering?",
        "No. This is a cyclic constraint (A<B<C<A) which has no valid ordering.", ["cycle_detection", "contradiction"]),

    # ── LEVEL 4: Causal Reasoning ──
    BenchmarkQuestion(22, 4, "CAUSAL", "Underdetermined Logic Puzzle",
        "Five houses in a row, each a different color (red, blue, green, yellow, white). The red house is immediately to the left of the blue house. The green house is not at either end. What color is the second house?",
        "Cannot be uniquely determined. Multiple valid arrangements exist satisfying the constraints.", ["constraint_satisfaction", "underdetermined"]),
    BenchmarkQuestion(23, 4, "CAUSAL", "Overconstrained Puzzle",
        "Eight workers, four shifts. Each shift needs exactly 2 workers. Worker A cannot work with B. B cannot work with C. C cannot work with D. How many valid assignments exist?",
        "The answer requires systematic enumeration. Multiple valid assignments exist depending on remaining worker pairings.", ["constraint_enumeration"]),
    BenchmarkQuestion(24, 4, "CAUSAL", "Confounding Variable",
        "A study finds cities with more libraries have lower crime. Can we conclude libraries reduce crime?",
        "No. Confounding variables (wealth, education, population density) likely explain both.", ["confounding", "correlation_causation"]),
    BenchmarkQuestion(25, 4, "CAUSAL", "Rule Consistency",
        "A hotel says: 'Every guest gets a welcome drink.' and 'Non-members do not get any drinks.' A non-member checks in. Is the rule set consistent?",
        "No. A non-member guest triggers both rules, creating a contradiction.", ["rule_consistency", "contradiction"]),
    BenchmarkQuestion(26, 4, "CAUSAL", "Simpson's Paradox",
        "Treatment A has a higher recovery rate than B in men and in women separately. But overall, B has a higher rate. How is this possible?",
        "Simpson's Paradox. The groups have different sizes — if more severe cases go to treatment A, the overall rate can reverse despite within-group superiority.", ["simpsons_paradox", "statistical_reasoning"]),
    BenchmarkQuestion(27, 4, "CAUSAL", "Alternative Causes",
        "A server is down. Monitoring shows high CPU. Can we conclude high CPU caused the outage?",
        "No. It may be cause, consequence, or correlation. High CPU could be a symptom, not the root cause.", ["alternative_causes"]),
    BenchmarkQuestion(28, 4, "CAUSAL", "Counterfactual",
        "A plant received fertilizer and then grew taller. It also received more sunlight than usual. Can we conclude the fertilizer caused the growth?",
        "No. The additional sunlight is a confound. Without a controlled experiment, we cannot isolate the fertilizer's effect.", ["counterfactual", "confounding"]),
    BenchmarkQuestion(29, 4, "CAUSAL", "Necessary vs Sufficient",
        "Oxygen is necessary for fire. A room has oxygen. Can we conclude there is fire?",
        "No. Oxygen is necessary but not sufficient (also need fuel and ignition).", ["necessary_sufficient"]),

    # ── LEVEL 5: Temporal & Dynamic Reasoning ──
    BenchmarkQuestion(30, 5, "TEMPORAL", "Temporal Chain",
        "At 9:00, Alice starts Task X. At 9:15, she starts Task Y without finishing X. At 9:30, she finishes both. Was X finished before Y started?",
        "No. X was not finished before Y started — she started Y while X was still in progress.", ["temporal", "overlap"]),
    BenchmarkQuestion(31, 5, "TEMPORAL", "Causal Sequence",
        "A server crashed at 10:00. At 10:01, the fan was replaced. At 10:02, the server recovered. Did the fan replacement cause the recovery?",
        "Possibly but not certain. Temporal sequence alone doesn't establish causation. The server may have auto-recovered.", ["temporal_causation"]),
    BenchmarkQuestion(32, 5, "TEMPORAL", "Multi-Event Timeline",
        "Event A happened before B. B happened after C. C happened before D. What is the guaranteed ordering?",
        "C before B and C before D are guaranteed. A before B is guaranteed. But A vs C and A vs D ordering is not determined.", ["temporal_ordering", "partial_order"]),
    BenchmarkQuestion(33, 5, "TEMPORAL", "Temporal Order",
        "A happened before B. B happened before C. C happened before D. Did A happen before D?",
        "Yes. By transitivity: A<B<C<D, therefore A<D.", ["temporal", "transitivity"]),
    BenchmarkQuestion(34, 5, "TEMPORAL", "State Transition",
        "Bank account starts at $1000. A withdrawal of $500 is rejected. Then a deposit of $300 is made. What is the balance?",
        "$1300. The rejected withdrawal does not change the balance. $1000 + $300 = $1300.", ["state_transition", "rejected_operation"]),
    BenchmarkQuestion(35, 5, "TEMPORAL", "Temporal + Causal",
        "A bridge was inspected Monday and rated safe. Heavy rain fell Tuesday. Wednesday morning, cracks were found. Did the rain cause the cracks?",
        "Cannot be determined with certainty. The rain is temporally correlated but other causes (aging, traffic load, pre-existing stress) are possible.", ["temporal_causation", "uncertainty"]),
    BenchmarkQuestion(36, 5, "TEMPORAL", "Temporal Contradiction",
        "A system log says a transaction was completed at 10:05. Another log says it was started at 10:10. Can both be true?",
        "Not under a normal single timeline. A transaction cannot complete before it starts — flag temporal inconsistency.", ["temporal_contradiction"]),

    # ── LEVEL 6: Adversarial & Multi-Domain ──
    BenchmarkQuestion(37, 6, "ADVERSARIAL", "Trick Question",
        "A farmer has 17 sheep. All but 9 die. How many sheep does the farmer have?",
        "9.", ["trick_question", "reading_comprehension"]),
    BenchmarkQuestion(38, 6, "ADVERSARIAL", "Evidence Revision",
        "First report: suspect was at crime scene. Second report (verified): suspect was in another country with passport evidence. What should we conclude?",
        "The verified second report overrides the first. Suspect was likely not at the scene. First report may be wrong or refer to a different person.", ["belief_revision", "evidence_weighting"]),
    BenchmarkQuestion(39, 6, "ADVERSARIAL", "Ambiguity Trap",
        "A man and his son are in a car accident. They are taken to different hospitals. The surgeon seeing the son says 'I cannot operate — this is my son!' How is this possible?",
        "The surgeon is the child's other parent (mother, or second father). Do not assume the surgeon must be male.", ["ambiguity", "assumption_checking"],
        branch_critical=True),
    BenchmarkQuestion(40, 6, "ADVERSARIAL", "Misleading Statistics",
        "99% of people with Disease X test positive. 5% of healthy people also test positive. 1% of the population has Disease X. If someone tests positive, what is the approximate probability they have the disease?",
        "About 16.7%. Using Bayes' theorem: P(D|+) = (0.99 * 0.01) / (0.99*0.01 + 0.05*0.99) ≈ 0.167.", ["bayes", "base_rate"]),
    BenchmarkQuestion(41, 6, "ADVERSARIAL", "Liar Paradox",
        "Alice says 'I always lie.' Is this statement true or false?",
        "Neither — it is a paradox. If true, Alice is lying so it is false. If false, Alice sometimes tells truth, which is consistent but means the specific statement is a lie. No stable truth assignment exists.", ["paradox", "self_reference"],
        branch_critical=True),
    BenchmarkQuestion(42, 6, "ADVERSARIAL", "Quoted Attribution",
        "Detective Quinn says: 'According to witness Smith, suspect Brown was at the scene.' Does this mean Brown was at the scene?",
        "No. This is quoted attribution — it reports Smith's claim, not an established fact. Smith could be mistaken or lying.", ["attribution", "epistemic_caution"],
        branch_critical=True),
    BenchmarkQuestion(43, 6, "ADVERSARIAL", "Type Mismatch",
        "Alice has 3 apples. Bob has 5 meters of rope. Who has more?",
        "Cannot compare — apples and meters of rope are different types/units. The comparison is meaningless.", ["type_checking", "category_error"]),
    BenchmarkQuestion(44, 6, "ADVERSARIAL", "Modus Tollens Chain",
        "If A then B. If B then C. C is false. What can we determine about A and B?",
        "Both A and B are false. By modus tollens: not-C → not-B → not-A.", ["modus_tollens", "chaining"],
        branch_critical=True),
    BenchmarkQuestion(45, 6, "ADVERSARIAL", "Vacuous Truth",
        "All unicorns in Central Park can fly. There are no unicorns in Central Park. Is the statement true?",
        "Yes, vacuously. A universal statement about an empty set is true by convention in classical logic.", ["vacuous_truth", "empty_set"]),
    BenchmarkQuestion(46, 6, "ADVERSARIAL", "Missing Information",
        "Two trains leave different cities heading toward each other. Train A goes 60 mph, Train B goes 80 mph. When do they meet?",
        "Cannot be determined. The distance between the cities is not given.", ["missing_information", "hallucination_resistance"]),
    BenchmarkQuestion(47, 6, "ADVERSARIAL", "Multiple Constraint System",
        "Five people (A–E) sit in a circle. A is next to B. B is next to C. C is not next to A. D is next to E. How many valid seatings exist?",
        "Multiple valid arrangements exist. The circular constraint with A-B adjacent, B-C adjacent, C not adjacent to A, and D-E adjacent allows several configurations.", ["circular_constraint", "enumeration"],
        branch_critical=True),
    BenchmarkQuestion(48, 6, "ADVERSARIAL", "Recursive Negation",
        "This statement is not a question. If it is true, what follows? If it is false, what follows?",
        "If true: it is indeed not a question (consistent). If false: it IS a question, but it is declarative in form, creating a contradiction. The statement is true — it is declarative, not interrogative.", ["self_reference", "meta_reasoning"]),
    BenchmarkQuestion(49, 6, "ADVERSARIAL", "Circular Ranking",
        "You receive these facts: A is greater than B. B is greater than C. C is greater than A. What should the system do before producing a ranking?",
        "Detect the cyclic contradiction (A>B>C>A) and refuse to produce a valid ranking.", ["contradiction_detection"]),
    BenchmarkQuestion(50, 6, "ADVERSARIAL", "MASTER TEST: Multi-Domain Reasoning",
        "A monitoring system reports: At 10:00, Server A was healthy. At 10:05, Server A's CPU reached 100%. At 10:06, Service X became unavailable. At 10:07, Server A rebooted automatically. At 10:08, Service X became available again. At 10:10, an operator says 'The CPU spike definitely caused the outage.' Another log shows a network interruption began at 10:05:30 and ended at 10:07:30. Answer: What is known with certainty? What is only correlated? Can CPU be established as the cause? What alternative causal explanation exists? What additional evidence would help? Give an appropriate confidence level for each major conclusion.",
        "Temporal sequence known with certainty. CPU causation not established — correlation only. Network interruption is an alternative causal explanation. Confidence must differ between temporal facts (high) and causal claims (low).",
        ["multi_domain", "causal", "temporal", "confidence_calibration"]),

    # ── LEVEL 7: External Review Puzzles (Sep 11, 2026) ──
    BenchmarkQuestion(51, 7, "STATE_SIMULATION", "Drone Spatial Reasoning",
        "A drone starts at position (0, 0) facing North. It executes: Forward 10 → Turn Right → Forward 5 → Turn Right → Forward 10 → Turn Left → Forward 3. Where does the drone end up, and which direction is it facing?",
        "Position (8, 3), facing East. Step-by-step: Start (0,0)N → Forward 10 → (0,10)N → Turn Right → facing E → Forward 5 → (5,10)E → Turn Right → facing S → Forward 10 → (5,0)S → Turn Left → facing E → Forward 3 → (8,0)E. Final: (8,0) facing East.",
        ["spatial", "state_tracking", "sequential_transforms"]),
    BenchmarkQuestion(52, 7, "STATE_SIMULATION", "Pallets Supply Chain",
        "A cargo ship starts with 100 pallets. Route: Port Alpha (drop 20, pick up 10) → Port Bravo (drop 30, pick up 5) → open sea (lose 5 to storm) → Port Charlie (drop 15) → encounter driftwood blockage, ship turns around → Port Delta (pick up 20, drop 10). How many pallets does the ship deliver to Port Echo?",
        "Zero. The ship turns around at the driftwood blockage before reaching Port Echo, so no pallets are delivered there.",
        ["state_tracking", "relevance_pruning", "reading_comprehension"]),
    BenchmarkQuestion(53, 7, "EPISTEMIC", "Three Hats Puzzle",
        "Three logicians (Alpha, Beta, Gamma) each wear a hat: Red or Blue, drawn from a set of 2 Red and 3 Blue hats. Each can see the other two hats but not their own. Asked in order — Alpha: 'Do you know your hat color?' Alpha: 'No.' Beta: 'Do you know your hat color?' Beta: 'No.' What color is Gamma's hat, and why?",
        "Blue. Alpha saying No means Alpha does not see two Red hats. So at most one Red among Beta and Gamma. Beta knowing this would know own color if Beta saw Red on Gamma (Beta would be Blue). Beta says No, so Gamma is not Red. Gamma is Blue.",
        ["epistemic_logic", "public_announcements", "possible_world_elimination"],
        branch_critical=True),
    BenchmarkQuestion(54, 7, "CONSTRAINT", "Letter Permutation All Wrong",
        "Five envelopes are labeled A, B, C, D, E. Five letters are also labeled A, B, C, D, E. Each envelope gets exactly one letter. NO letter is in its matching envelope. Letter B is in envelope C. Which envelope contains letter A?",
        "Not uniquely determined. Multiple valid derangements exist with B in C fixed. Additional constraints needed.",
        ["permutation", "derangement", "all_different", "constraint_satisfaction"]),
    BenchmarkQuestion(55, 7, "ADVERSARIAL", "Coins Weighing Strategy",
        "You have 12 coins. Exactly one is counterfeit and differs in weight (heavier or lighter, unknown which). You have a balance scale and can make exactly 3 weighings. Describe a complete strategy that guarantees identifying the counterfeit coin AND determining whether it is heavier or lighter.",
        "Classic 12-coin solution: Divide into groups of 4. Weighing 1 compares 4 vs 4. If balanced, counterfeit is in remaining 4 and 2 more weighings suffice. If unbalanced, track heavy/light sides, rotate coins between groups in weighing 2 to isolate, weighing 3 confirms identity and direction. Must cover all 24 possibilities (12 coins x 2 directions) within 27 outcomes.",
        ["adversarial", "strategy", "exhaustive_verification", "information_theory"],
        branch_critical=True),
]

def get_questions(ids=None, level=None, subset=None):
    qs = QUESTIONS
    if ids:
        qs = [q for q in qs if q.id in ids]
    if level:
        qs = [q for q in qs if q.level == level]
    if subset == "branch":
        qs = [q for q in qs if q.branch_critical]
    return qs

if __name__ == "__main__":
    print(f"Total questions: {len(QUESTIONS)}")
    for q in QUESTIONS:
        print(f"  Q{q.id:2d} [{q.level_label:12s}] {q.title}")
