# Vendor Risk Register

**Generated:** 2026-09-24T14:06:34.654873+00:00
**Vendors assessed:** 4
**Source data:** `reports/vendor-risk-scores-20260924-140634.json`

---

## Summary

| Vendor | Type | Criticality | Rating | Risk Score | Findings | Review By |
|---|---|---|---|---|---|---|
| LegacyDocs Processing Inc | Document processing outsourcer | High | **HIGH RISK** | 100.0 | 14 | 2026-10-10 |
| QuickMail Marketing Co | Email marketing SaaS | Medium | **HIGH RISK** | 47.5 | 9 | 2026-10-05 |
| TeamSync Collaboration Tools | Internal productivity SaaS | Low | **LOW RISK** | 2.0 | 2 | 2027-03-11 |
| CloudSecure Storage Ltd | Cloud storage provider | High | **LOW RISK** | 0.0 | 0 | 2027-02-28 |

---

## Detailed Findings by Vendor

### LegacyDocs Processing Inc — HIGH RISK

- **Type:** Document processing outsourcer
- **Data shared:** Customer PII, contracts, ID documents
- **Criticality:** High
- **Overall control score:** 11.9%
- **Criticality-adjusted risk score:** 100.0 / 100

**Findings:**

- **[HIGH]** (Data Handling & Privacy) Is customer/personal data encrypted at rest? — Answered No
- **[MEDIUM]** (Data Handling & Privacy) Does the vendor have a documented data retention and deletion policy? — Answered No
- **[MEDIUM]** (Data Handling & Privacy) Is data processed or stored outside the UK/EEA? — Answered Yes
  - *Note: Not automatically disqualifying - requires adequacy/SCC review*
- **[HIGH]** (Access Control) Is multi-factor authentication enforced for administrative access? — Answered No
- **[MEDIUM]** (Access Control) Does the vendor perform periodic access reviews? — Answered No
- **[MEDIUM]** (Access Control) Is access provisioned on a least-privilege basis? — Answered No
- **[HIGH]** (Incident Response) Does the vendor have a documented incident response plan? — Answered No
- **[HIGH]** (Incident Response) Does the vendor commit to a breach notification SLA (e.g. within 72 hours)? — Answered No
- **[MEDIUM]** (Incident Response) Has the vendor experienced a data breach in the last 24 months? — Answered Yes
  - *Note: Requires review of remediation, not automatically disqualifying*
- **[MEDIUM]** (Business Continuity) Does the vendor have a documented business continuity / disaster recovery plan? — Answered No
- **[LOW]** (Business Continuity) Is the vendor's BC/DR plan tested at least annually? — Answered No
- **[MEDIUM]** (Compliance & Certifications) Does the vendor hold ISO 27001 certification (or equivalent)? — Answered No
- **[LOW]** (Compliance & Certifications) Does the vendor hold a current SOC 2 Type II report? — Answered No
- **[HIGH]** (Compliance & Certifications) Is the vendor GDPR compliant (has a DPA available for signature)? — Answered No

### QuickMail Marketing Co — HIGH RISK

- **Type:** Email marketing SaaS
- **Data shared:** Customer email addresses, names
- **Criticality:** Medium
- **Overall control score:** 52.5%
- **Criticality-adjusted risk score:** 47.5 / 100

**Findings:**

- **[MEDIUM]** (Data Handling & Privacy) Does the vendor have a documented data retention and deletion policy? — Answered No
- **[MEDIUM]** (Data Handling & Privacy) Is data processed or stored outside the UK/EEA? — Answered Yes
  - *Note: Not automatically disqualifying - requires adequacy/SCC review*
- **[HIGH]** (Access Control) Is multi-factor authentication enforced for administrative access? — Answered No
- **[MEDIUM]** (Access Control) Does the vendor perform periodic access reviews? — Answered No
- **[HIGH]** (Incident Response) Does the vendor commit to a breach notification SLA (e.g. within 72 hours)? — Answered No
- **[MEDIUM]** (Business Continuity) Does the vendor have a documented business continuity / disaster recovery plan? — Answered No
- **[LOW]** (Business Continuity) Is the vendor's BC/DR plan tested at least annually? — Answered No
- **[MEDIUM]** (Compliance & Certifications) Does the vendor hold ISO 27001 certification (or equivalent)? — Answered No
- **[LOW]** (Compliance & Certifications) Does the vendor hold a current SOC 2 Type II report? — Answered No

### TeamSync Collaboration Tools — LOW RISK

- **Type:** Internal productivity SaaS
- **Data shared:** Internal project data, no customer PII
- **Criticality:** Low
- **Overall control score:** 96.7%
- **Criticality-adjusted risk score:** 2.0 / 100

**Findings:**

- **[LOW]** (Business Continuity) Is the vendor's BC/DR plan tested at least annually? — Answered No
- **[LOW]** (Compliance & Certifications) Does the vendor hold a current SOC 2 Type II report? — Answered No

### CloudSecure Storage Ltd — LOW RISK

- **Type:** Cloud storage provider
- **Data shared:** Customer PII, financial records
- **Criticality:** High
- **Overall control score:** 100.0%
- **Criticality-adjusted risk score:** 0.0 / 100

No findings — vendor meets all assessed control expectations at time of review.

---

## Register Notes

Remediation SLAs above are risk-tiered defaults (High: 30 days, Medium: 90 days, Low: 180 days) from date of assessment, not from register generation. Vendors rated HIGH RISK with High criticality and access to sensitive data should be escalated for immediate review regardless of SLA timing, and existing engagements should have compensating controls or a remediation plan agreed before renewal.