# Debugging Notes

## Risk score exceeding 100: root cause and fix

**Symptom:** The first run of `risk_scoring.py` produced a criticality-adjusted risk score of 132.1 for LegacyDocs Processing Inc - a High-criticality vendor with numerous control gaps. A risk score above 100 is meaningless on a 0-100 scale and would have looked like an obvious tooling error to anyone reviewing the register.

**Root cause:** The scoring formula computed `(100 - overall_score_pct) * criticality_multiplier`, where the multiplier (1.5 for High criticality) was applied after subtracting from 100, with no upper bound. For a vendor with a very low overall control score (LegacyDocs: 11.9%), the base risk (100 - 11.9 = 88.1) multiplied by 1.5 produced 132.1 - mathematically correct given the formula, but a genuine design flaw: the multiplier is meant to weight how much a gap matters for a critical vendor, not to produce a score that exceeds the maximum possible risk.

**Fix:** the adjusted risk score is now capped at 100 via `min(..., 100.0)`. Re-run and confirmed: LegacyDocs now correctly shows a risk score of 100.0 (still the worst of the four sample vendors, as it should be), with no change to the relative ranking of vendors - only the uncapped, out-of-range value was corrected.

**Why this matters for a scoring tool specifically:** an obviously-wrong number (132 out of 100) in a report handed to a vendor management committee undermines trust in every other number the tool produces, even correct ones. This was caught by inspecting the actual output rather than only checking that the ranking order looked directionally reasonable - the same validation discipline applied throughout this project series: a plausible-looking result is not the same as a correct one, and both were checked.

## Sample data design note

The four sample vendors were deliberately constructed with a real spread of outcomes - one strong vendor with no findings, one weak-but-plausible SaaS vendor, one genuinely poor vendor handling sensitive data with almost no controls, and one low-criticality vendor with gaps that matter less given its limited data access - specifically so the scoring engine's behaviour could be checked against multiple different scenarios, not just a single "happy path" case. This is what surfaced the scoring bug: it only appeared for the highest-risk, highest-criticality combination, and would not have been caught by testing only moderate cases.
