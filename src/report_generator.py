from datetime import datetime

def generate_report(features, verdict):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = []
    report.append("PHISHING FORENSIC ANALYSIS REPORT")
    report.append("=" * 35)
    report.append(f"Analysis Time : {timestamp}\n")

    report.append("Extracted Evidence:")
    for k, v in features.items():
        report.append(f"- {k} : {v}")

    report.append("\nFinal Verdict:")
    report.append(f">>> {verdict}")

    return "\n".join(report)
