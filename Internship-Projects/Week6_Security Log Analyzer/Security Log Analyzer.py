# =========================================================
# Week 6 Project - Security Log Analyzer
# =========================================================

from collections import defaultdict

# -----------------------------
# Suspicious Patterns
# -----------------------------
SQLI_PATTERNS = [
    "' OR 1=1",
    "UNION SELECT",
    "--",
    "' OR 'a'='a"
]

XSS_PATTERNS = [
    "<script>",
    "</script>",
    "javascript:"
]

# -----------------------------
# Main Function
# -----------------------------
def analyze_logs(filename):

    failed_attempts = defaultdict(int)
    ip_targets = defaultdict(set)

    total_failed = 0
    suspicious_ips = set()

    try:
        with open(filename, "r") as file:

            print("\n========== Security Log Analysis ==========\n")

            for line in file:

                log = line.strip()

                # ---------------------------------
                # Brute Force Detection
                # ---------------------------------
                if "LOGIN FAILED" in log:

                    parts = log.split()

                    user = parts[4]
                    ip = parts[5]

                    failed_attempts[user] += 1
                    ip_targets[ip].add(user)

                    total_failed += 1

                # ---------------------------------
                # SQL Injection Detection
                # ---------------------------------
                for pattern in SQLI_PATTERNS:
                    if pattern.lower() in log.lower():

                        print("[ALERT] Possible SQL Injection Detected")
                        print("Log:", log)
                        print()

                # ---------------------------------
                # XSS Detection
                # ---------------------------------
                for pattern in XSS_PATTERNS:
                    if pattern.lower() in log.lower():

                        print("[ALERT] Possible XSS Attack Detected")
                        print("Log:", log)
                        print()

            # =====================================
            # Failed Login Report
            # =====================================

            print("\n========== Failed Login Report ==========\n")

            for user, count in failed_attempts.items():

                print(f"{user}: {count} failed attempts")

                # Brute Force Alert
                if count >= 3:

                    print(f"[ALERT] Brute Force Attack Detected on user: {user}\n")

            # =====================================
            # Password Spraying Detection
            # =====================================

            print("\n========== IP Activity Analysis ==========\n")

            for ip, users in ip_targets.items():

                if len(users) >= 3:

                    suspicious_ips.add(ip)

                    print(f"[ALERT] Password Spraying Detected from IP: {ip}")
                    print(f"Targeted Users: {', '.join(users)}\n")

            # =====================================
            # Summary Report
            # =====================================

            print("\n========== Security Summary ==========\n")

            print(f"Total Failed Login Attempts : {total_failed}")
            print(f"Suspicious IPs Detected     : {len(suspicious_ips)}")
            print(f"Users Affected              : {len(failed_attempts)}")

    except FileNotFoundError:
        print("Error: Log file not found!")

# =========================================================
# Main Program
# =========================================================

filename = input("Enter full log file path:").strip()

if not filename:
    print("Error: Filename cannot be empty!")

else:
    analyze_logs(filename)