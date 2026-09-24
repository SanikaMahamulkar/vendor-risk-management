# Vendor Risk Management (TPRM) Tool - Project Report

Author: Sanika Mahamulkar, MSc Cybersecurity, University of Bristol
Repository: https://github.com/SanikaMahamulkar/vendor-risk-management
Date: September 2026

## Executive Summary

This project builds a Third-Party Risk Management tool: a structured, weighted vendor security questionnaire, an automated scoring engine that produces a criticality-adjusted risk rating per vendor, and a generated risk register - the audit-ready artifact a GRC analyst would maintain and present to a vendor management committee. It is the fourth in a series of GRC/security engineering projects, and deliberately covers the business-process side of GRC work rather than the infrastructure-engineering side covered in the earlier three.

Four sample vendors were assessed with a real, deliberately varied spread of risk profiles, producing genuine findings including one HIGH RISK vendor with 14 control gaps. During development, the scoring engine's first output included a mathematically-produced but meaningless result (a risk score of 132.1 on a 0-100 scale), caught by inspecting the actual output rather than only checking that vendor rankings looked directionally correct, root-caused to an unbounded multiplier, and fixed.

## Objectives

1. Build a structured vendor security questionnaire covering standard TPRM domains.
2. Build an objective, weighted scoring engine that produces a defensible risk rating per vendor.
3. Produce an audit-ready risk register, not just raw scores - the artifact an analyst would actually maintain and present.
4. Map every questionnaire domain to a specific compliance control.
5. Test the scoring engine against a realistic spread of vendor profiles, not just a single easy case.

## Methodology

The questionnaire was structured on the SIG-Lite (Standardized Information Gathering, abbreviated) model commonly used in real TPRM programmes, covering five domains: Data Handling & Privacy, Access Control, Incident Response, Business Continuity, and Compliance & Certifications. Each question carries a risk severity, and each domain carries a weight reflecting its relative importance to overall risk.

Four sample vendors were constructed with deliberately different profiles - a strong vendor with no findings, a weak-but-plausible SaaS vendor, a genuinely poor vendor handling sensitive PII with almost no controls, and a low-criticality vendor with gaps that matter less given limited data access - specifically to exercise the scoring engine across a realistic range of scenarios rather than a single easy case.

## A Genuine Bug, Found and Fixed

The scoring formula applies a criticality multiplier (1.5x for High-criticality vendors) to the base risk score to reflect that the same control gap matters more for a vendor handling sensitive data. The first run produced a score of 132.1 for the highest-risk, highest-criticality vendor (LegacyDocs Processing Inc) - a base risk of 88.1 multiplied by 1.5, with no upper bound applied. This is mathematically correct given the formula as originally written, but a real design flaw: a score exceeding the maximum possible value on a 0-100 scale is meaningless and would undermine confidence in every other number the tool produces if it appeared in a report handed to a vendor management committee.

This was caught by inspecting the actual score value, not just checking that the vendor ranking order looked reasonable (LegacyDocs did correctly rank worst, even with the bug present - the ranking alone would not have surfaced the problem). Fixed by capping the adjusted risk score at 100. Re-run and confirmed correct, with no change to the relative ranking of vendors. Full detail is in debugging-notes.md.

## Control Mapping

Full detail in control-mapping.md. In summary: the five questionnaire domains map to ISO 27001:2022 A.5.19 through A.5.22 (information security in supplier relationships, addressing security within supplier agreements, managing supply chain risk, and monitoring/review of supplier services), with the GDPR-specific data processing agreement question mapping to GDPR Article 28. Remediation review dates are risk-tiered from assessment date (30/90/180 days for High/Medium/Low risk), documented as project defaults rather than regulatory requirements, since a real deployment should calibrate these against organisational risk appetite.

## Conclusion

This project delivers a working vendor risk assessment tool tested against a realistic, deliberately varied dataset rather than a single easy case - which is precisely what surfaced a real scoring bug that a simpler test set would have missed. It demonstrates the analyst-facing, business-process side of GRC work: producing a defensible, control-mapped, audit-ready risk register rather than only technical infrastructure assessment, rounding out the project series with the kind of deliverable most directly reflected in day-to-day GRC Analyst job descriptions.

## Skills Demonstrated

- Third-party risk management methodology: SIG-Lite-style questionnaire design, weighted risk scoring
- ISO 27001 supplier-relationship control mapping (A.5.19-A.5.22), GDPR Article 28
- Risk register production: the actual audit-ready artifact, not just raw data
- Deliberate test-case design: constructing a varied dataset specifically to exercise edge cases, which is what surfaced the real bug found in this project
- Root-causing a scoring/business-logic bug to a specific formula flaw, not a vague guess
- Python scripting for structured data processing and report generation
- Risk-tiered remediation SLA design
