# spam_detector.py

SPAM_KEYWORDS = [
    "lottery", "win money", "click here", "free", "offer",
    "urgent", "congratulations", "limited time", "act now",
    "guaranteed", "100% free", "investment", "cheap", "deal"
]

def check_spam(message: str) -> str:
    msg = message.lower()
    for word in SPAM_KEYWORDS:
        if word in msg:
            return f"⚠️ Spam detected (keyword: {word})"
    return "✅ Not Spam (Safe message)"

if __name__ == "__main__":
    print("📩 Spam Alert System")
    text = input("Enter a message: ")
    result = check_spam(text)
    print("\nResult:", result)
