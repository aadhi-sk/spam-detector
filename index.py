import re


SPAM_PATTERNS = {
    "Suspicious Links": r"(https?://[^\s]+|www\.[^\s]+)",
    "Money Offers": r"(₹|\$|\beuro\b|\bpound\b|\bdollars?\b|\bmillion\b|\bbillion\b)",
    "Urgency Words": r"\b(urgent|act now|limited time|only today|hurry|offer ends)\b",
    "Free Offers": r"\b(free|giveaway|won|prize|reward)\b",
    "Suspicious Email": r"\b(click here|subscribe|claim now|sign up)\b",
    "Excessive Symbols": r"([!?.]{3,}|[%$#@]{3,})",
    "Suspicious Words": r"\b(lottery|guarantee|investment|credit|loan|cash|bitcoin)\b"
}


compiled_patterns = {name: re.compile(pattern, re.IGNORECASE) for name, pattern in SPAM_PATTERNS.items()}

def detect_spam(message: str) -> dict:
  
    results = {}
    score = 0

    for name, pattern in compiled_patterns.items():
        matches = pattern.findall(message)
        if matches:
            results[name] = len(matches)
            score += len(matches)

    spam_score = min(score * 10, 100)  # Cap at 100
    return {"Spam Score": spam_score, "Matches": results}

