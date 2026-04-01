import re
from urllib.parse import urlparse

def check_phishing(url):
    score = 0
    remarks = []

    # Check URL length
    if len(url) > 75:
        score += 1
        remarks.append("URL is very long.")

    # Check for @ symbol
    if "@" in url:
        score += 1
        remarks.append("Contains '@' symbol.")

    # Check for IP address in URL (FIXED REGEX)
    ip_pattern = r'\b\d{1,3}(\.\d{1,3}){3}\b'
    if re.search(ip_pattern, url):
        score += 1
        remarks.append("Uses IP address instead of domain.")

    # Extract domain safely
    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    # Check for hyphen in domain
    if "-" in domain:
        score += 1
        remarks.append("Domain contains hyphen (-).")

    # Check for HTTPS (IMPROVED)
    if parsed_url.scheme != "https":
        score += 1
        remarks.append("Not using HTTPS.")

    # Check for suspicious keywords (WAS MISSING)
    suspicious_keywords = ["login", "verify", "bank", "secure", "account", "update"]
    for word in suspicious_keywords:
        if word in url.lower():
            score += 1
            remarks.append(f"Contains suspicious keyword: {word}")
            break  # avoid multiple counts

    # Result classification (UNCHANGED LOGIC)
    if score <= 1:
        result = "Safe"
    elif score <= 3:
        result = "Suspicious"
    else:
        result = "Phishing Risk"

    return result, remarks


# Main Program
url = input("Enter website URL: ").strip()

# Basic input validation
if not url:
    print("Invalid input! URL cannot be empty.")
else:
    result, remarks = check_phishing(url)

    print("\nResult:", result)

    if remarks:
        print("Warnings:")
        for r in remarks:
            print("-", r)