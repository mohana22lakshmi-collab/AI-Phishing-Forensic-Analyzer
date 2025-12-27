def classify_phishing(features):
    score = 0

    if features["url_count"] > 0:
        score += 1

    if features["suspicious_word_count"] >= 2:
        score += 2

    if features["ip_url"] == 1:
        score += 2

    if features["length"] < 300:
        score += 1

    if score >= 4:
        return "PHISHING"
    else:
        return "LEGITIMATE"
