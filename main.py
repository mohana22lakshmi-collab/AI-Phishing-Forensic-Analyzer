from src.feature_extractor import extract_features
from src.classifier import classify_phishing
from src.report_generator import generate_report

sample_email = """
URGENT: Verify your bank account now!
Click here: http://192.168.1.10/login
"""

features = extract_features(sample_email)
verdict = classify_phishing(features)

report = generate_report(features, verdict)

print(report)

with open("phishing_report.txt", "w") as f:
    f.write(report)

