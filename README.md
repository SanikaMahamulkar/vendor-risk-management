# Vendor Risk Management (TPRM) Tool

A Third-Party Risk Management tool: a SIG-Lite-style security questionnaire, an automated weighted risk scoring engine, and a generated vendor risk register - the actual artifact a GRC analyst would maintain and present to a vendor management committee.

This project rounds out a series of four GRC/security engineering projects by covering the business-process side of GRC work (vendor risk assessment) rather than the technical infrastructure side covered in aws-cloud-security-baseline, soc-detection-lab, and iam-access-governance.

## Tech stack

- **Language:** Python 3 (no external dependencies)
- **Data:** structured JSON questionnaire and vendor response data
- **Output:** JSON scoring results + audit-ready Markdown risk register

## Repository structure

- `questionnaire/security_questionnaire.json` - 5-domain, weighted vendor security questionnaire (SIG-Lite-style)
- `vendors/vendor_responses.json` - 4 sample vendors with deliberately varied risk profiles
- `scripts/risk_scoring.py` - weighted scoring engine: domain scores, criticality adjustment, overall risk rating
- `scripts/generate_risk_register.py` - turns scores into an audit-ready Markdown risk register with SLA-tiered review dates
- `control-mapping.md` - maps questionnaire domains to ISO 27001 supplier-relationship controls and GDPR Art. 28
- `debugging-notes.md` - a real scoring bug found via output inspection, root-caused, and fixed

## Progress log

- [x] Built a 5-domain, weighted vendor security questionnaire (Data Handling, Access Control, Incident Response, Business Continuity, Compliance)
- [x] Built the risk scoring engine with domain weighting and criticality-based adjustment
- [x] Found and fixed a real scoring bug (unbounded criticality multiplier producing scores above 100)
- [x] Built the risk register generator with SLA-tiered remediation review dates
- [x] Control mapping to ISO 27001 A.5.19-A.5.22 and GDPR Article 28
- [ ] Full project report

## Sample findings

Four sample vendors were assessed, producing a genuine spread of outcomes: one HIGH RISK vendor with 14 findings (a document processor handling sensitive PII with almost no controls in place), one HIGH RISK vendor with more moderate gaps, and two LOW RISK vendors. This spread was deliberate - it's what surfaced the scoring bug documented in debugging-notes.md, which only appeared at the highest-risk, highest-criticality combination.

## Author

Sanika Mahamulkar - MSc Cybersecurity, University of Bristol
