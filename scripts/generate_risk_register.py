#!/usr/bin/env python3
"""
Generates a vendor risk register (Markdown) from the latest scoring output -
the audit-ready artifact tracking each vendor's risk rating, key findings,
and remediation status over time.
"""

import json
import glob
from datetime import datetime, timezone, timedelta


def latest_scores():
    files = sorted(glob.glob("reports/vendor-risk-scores-*.json"))
    if not files:
        raise SystemExit("No vendor risk scores found. Run risk_scoring.py first.")
    return files[-1]


REMEDIATION_SLA_DAYS = {
    "HIGH RISK": 30,
    "MEDIUM RISK": 90,
    "LOW RISK": 180,
}


def main():
    path = latest_scores()
    with open(path) as f:
        data = json.load(f)

    lines = []
    lines.append("# Vendor Risk Register")
    lines.append("")
    lines.append(f"**Generated:** {data['generated_at']}")
    lines.append(f"**Vendors assessed:** {data['vendors_assessed']}")
    lines.append(f"**Source data:** `{path}`")
    lines.append("")
    lines.append("---")
    lines.append("")

    lines.append("## Summary")
    lines.append("")
    lines.append("| Vendor | Type | Criticality | Rating | Risk Score | Findings | Review By |")
    lines.append("|---|---|---|---|---|---|---|")

    for r in data["results"]:
        assess_date = datetime.fromisoformat(r["assessment_date"])
        sla_days = REMEDIATION_SLA_DAYS[r["rating"]]
        review_by = (assess_date + timedelta(days=sla_days)).strftime("%Y-%m-%d")
        lines.append(
            f"| {r['vendor_name']} | {r['vendor_type']} | {r['criticality'].title()} | "
            f"**{r['rating']}** | {r['criticality_adjusted_risk_score']} | {r['findings_count']} | {review_by} |"
        )

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Detailed Findings by Vendor")
    lines.append("")

    for r in data["results"]:
        lines.append(f"### {r['vendor_name']} — {r['rating']}")
        lines.append("")
        lines.append(f"- **Type:** {r['vendor_type']}")
        lines.append(f"- **Data shared:** {r['data_shared']}")
        lines.append(f"- **Criticality:** {r['criticality'].title()}")
        lines.append(f"- **Overall control score:** {r['overall_score_pct']}%")
        lines.append(f"- **Criticality-adjusted risk score:** {r['criticality_adjusted_risk_score']} / 100")
        lines.append("")

        if r["findings"]:
            lines.append("**Findings:**")
            lines.append("")
            for f in r["findings"]:
                severity_label = f["severity"].upper()
                lines.append(f"- **[{severity_label}]** ({f['domain']}) {f['text']} — {f['reason']}")
                if f.get("note"):
                    lines.append(f"  - *Note: {f['note']}*")
        else:
            lines.append("No findings — vendor meets all assessed control expectations at time of review.")

        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("## Register Notes")
    lines.append("")
    lines.append("Remediation SLAs above are risk-tiered defaults (High: 30 days, Medium: 90 days, Low: 180 days) "
                  "from date of assessment, not from register generation. Vendors rated HIGH RISK with High "
                  "criticality and access to sensitive data should be escalated for immediate review regardless "
                  "of SLA timing, and existing engagements should have compensating controls or a remediation "
                  "plan agreed before renewal.")

    output_path = f"reports/vendor-risk-register-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}.md"
    with open(output_path, "w") as f:
        f.write("\n".join(lines))

    print(f"Risk register written to {output_path}")


if __name__ == "__main__":
    main()
