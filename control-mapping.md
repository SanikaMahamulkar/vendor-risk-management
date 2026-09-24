# Control Mapping

This document maps each questionnaire domain and scoring decision to the compliance control it supports.

| Questionnaire Domain | Control | Framework Reference |
|---|---|---|
| Data Handling & Privacy | Ensuring third parties protect information consistent with the organisation's own requirements | ISO 27001:2022 A.5.19 (Information security in supplier relationships) |
| Access Control | Third-party access provisioning and review | ISO 27001:2022 A.5.19, A.8.2 |
| Incident Response | Addressing information security in supplier agreements, including breach notification | ISO 27001:2022 A.5.20 (Addressing security within supplier agreements), A.5.24 (Incident management planning) |
| Business Continuity | Managing supply chain risk to service continuity | ISO 27001:2022 A.5.21 (Managing information security in the ICT supply chain) |
| Compliance & Certifications | Monitoring, review and change management of supplier services | ISO 27001:2022 A.5.22 (Monitoring, review and change management of supplier services) |
| GDPR-specific question (CC-03: DPA availability) | Processor obligations under a data processing agreement | GDPR Article 28 |

## Scoring Methodology

Each question carries a risk severity (high/medium/low) reflecting the impact of a control gap, and each questionnaire domain carries a weight reflecting its relative importance to overall vendor risk. A vendor's overall control score is the weighted average across domains. This is then adjusted by a criticality multiplier (based on how sensitive the data shared with the vendor is and how integral the vendor is to operations), since the same control gap matters more for a vendor handling customer PII than one with no data access. The adjusted score is capped at 100 - a design decision made after testing surfaced a case where the multiplier produced a nonsensical score above 100 (see debugging-notes.md).

## Review Cadence

Remediation SLAs are risk-tiered from date of assessment: 30 days for HIGH RISK, 90 days for MEDIUM RISK, 180 days for LOW RISK vendors. These are defaults for this project, not a regulatory requirement - a real deployment would set these based on organisational risk appetite and contractual review cycles.

## Scope and Limitations

- This is a self-assessment questionnaire model: it scores what a vendor reports, not independently verified evidence. A mature TPRM programme would supplement high-criticality vendor self-assessments with evidence review (e.g. requesting the actual SOC 2 report, not just confirmation one exists) or independent audit.
- The questionnaire covers five common domains but is not exhaustive; a real programme would tailor questions to the specific service type (e.g. additional questions for payment processors under PCI DSS scope).
- Scoring and criticality weighting are configurable defaults in this project, not fixed - they should be calibrated against an organisation's actual risk appetite and reviewed periodically.
