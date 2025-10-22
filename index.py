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

def classify_message(score: int) -> str:
    """
    Classifies the message as HAM or SPAM based on score.
    """
    if score < 30:
        return "✅ Likely Safe (HAM)"
    elif score < 60:
        return "⚠ Possibly Spam"
    else:
        return "🚨 Likely Spam"

def main():
    print("=== Simple Spam Detector (Regex-based) ===")
    print("Enter/Paste a message to analyze (or type 'exit' to quit):\n")

    while True:
        message = input("Message:\n> ").strip()
        if message.lower() == "exit":
            print("Exiting Spam Detector. Goodbye!")
            break

        result = detect_spam(message)
        label = classify_message(result["Spam Score"])

        print("\n--- Analysis Result ---")
        print(f"Spam Score: {result['Spam Score']}/100")
        print(f"Classification: {label}")

        if result["Matches"]:
            print("\nMatched Categories:")
            for category, count in result["Matches"].items():
                print(f" - {category}: {count} match(es)")
        else:
             print(" - No spam indicators found.")

        print("\n" + "=" * 40 + "\n")

if _name_ == "_main_":
    main()


