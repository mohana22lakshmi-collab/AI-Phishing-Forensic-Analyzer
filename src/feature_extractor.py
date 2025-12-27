import re

SUSPICIOUS_KEYWORDS = [
    "urgent", "verify", "account", "click",
    "login", "password", "confirm", "bank"
]

def extract_features(email_text):
    features = {}

    text = email_text.lower()

    features["length"] = len(text)
    features["url_count"] = len(re.findall(r'https?://', text))
    features["suspicious_word_count"] = sum(
        1 for word in SUSPICIOUS_KEYWORDS if word in text
    )
    features["ip_url"] = 1 if re.search(r'\b\d{1,3}(\.\d{1,3}){3}\b', text) else 0

    return features
