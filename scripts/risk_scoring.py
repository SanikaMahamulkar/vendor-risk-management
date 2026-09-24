#!/usr/bin/env python3
"""
Vendor Risk Scoring Engine
Scores vendor questionnaire responses against the weighted questionnaire
schema, producing a domain-level and overall risk score per vendor.
"""

import json
from datetime import datetime, timezone

RISK_SEVERITY_POINTS = {
    "high": 10,
    "medium": 5,
    "low": 2,
}

CRITICALITY_MULTIPLIER = {
    "high": 1.5,
    "medium": 1.0,
    "low": 0.6,
}


def load_questionnaire():
    with open("questionnaire/security_questionnaire.json") as f:
        return json.load(f)


def load_vendors():
    with open("vendors/vendor_responses.json") as f:
        return json.load(f)


def score_vendor(vendor, questionnaire):
    responses = vendor["responses"]
    domain_results = []
    total_risk_points = 0
    total_possible_points = 0
    findings = []

    for domain in questionnaire["domains"]:
        domain_risk_points = 0
        domain_possible_points = 0
        domain_findings = []

        for q in domain["questions"]:
            qid = q["id"]
            answer = responses.get(qid)

            if "risk_if_no" in q:
                severity = q["risk_if_no"]
                points = RISK_SEVERITY_POINTS[severity]
                domain_possible_points += points
                if answer is False:
                    domain_risk_points += points
                    domain_findings.append({
                        "id": qid, "text": q["text"], "severity": severity,
                        "reason": "Answered No"
                    })
            elif "risk_if_yes" in q:
                severity = q["risk_if_yes"]
                points = RISK_SEVERITY_POINTS[severity]
                domain_possible_points += points
                if answer is True:
                    domain_risk_points += points
                    domain_findings.append({
                        "id": qid, "text": q["text"], "severity": severity,
                        "reason": "Answered Yes", "note": q.get("note", "")
                    })

        domain_score_pct = 100 - (domain_risk_points / domain_possible_points * 100 if domain_possible_points else 0)
        domain_results.append({
            "domain": domain["domain"],
            "weight": domain["weight"],
            "score_pct": round(domain_score_pct, 1),
            "findings": domain_findings,
        })
        total_risk_points += domain_risk_points * (domain["weight"] / 100)
        total_possible_points += domain_possible_points * (domain["weight"] / 100)
        findings.extend([{**f, "domain": domain["domain"]} for f in domain_findings])

    overall_score_pct = 100 - (total_risk_points / total_possible_points * 100 if total_possible_points else 0)
    multiplier = CRITICALITY_MULTIPLIER.get(vendor.get("criticality", "medium"), 1.0)
    # Cap at 100: the criticality multiplier is meant to weight how much a given
    # gap matters, not to produce a score exceeding the maximum possible risk.
    # Uncapped, a high-criticality vendor with a low base score (e.g. 88.1 base
    # risk * 1.5 multiplier = 132.1) produced a nonsensical score above 100 -
    # found during testing (LegacyDocs Processing Inc) and fixed here.
    adjusted_risk_score = min(round((100 - overall_score_pct) * multiplier, 1), 100.0)

    if adjusted_risk_score >= 40:
        rating = "HIGH RISK"
    elif adjusted_risk_score >= 20:
        rating = "MEDIUM RISK"
    else:
        rating = "LOW RISK"

    return {
        "vendor_name": vendor["vendor_name"],
        "vendor_type": vendor["vendor_type"],
        "criticality": vendor["criticality"],
        "data_shared": vendor["data_shared"],
        "assessment_date": vendor["assessment_date"],
        "overall_score_pct": round(overall_score_pct, 1),
        "criticality_adjusted_risk_score": adjusted_risk_score,
        "rating": rating,
        "domain_results": domain_results,
        "findings_count": len(findings),
        "findings": findings,
    }


def main():
    questionnaire = load_questionnaire()
    vendors = load_vendors()

    results = [score_vendor(v, questionnaire) for v in vendors]
    results.sort(key=lambda r: r["criticality_adjusted_risk_score"], reverse=True)

    output = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "vendors_assessed": len(results),
        "results": results,
    }

    output_path = f"reports/vendor-risk-scores-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}.json"
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"Scored {len(results)} vendors. Report written to {output_path}")
    for r in results:
        print(f"  {r['vendor_name']}: {r['rating']} (score: {r['criticality_adjusted_risk_score']}, {r['findings_count']} findings)")


if __name__ == "__main__":
    main()
