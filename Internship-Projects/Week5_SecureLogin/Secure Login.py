
import time
from datetime import datetime

# =====================================================
# Secure Login System with Brute Force Protection
# =====================================================

# Demo Credentials
CORRECT_USERNAME = "Admin"
CORRECT_PASSWORD = "Admin#123"

# ---------------- Security Settings ----------------
MAX_USERNAME_ATTEMPTS = 3          # Lock account after 3 failures
ACCOUNT_LOCK_TIME = 60            # 1 minute temporary lock

MAX_IP_ATTEMPTS = 8               # Many attempts from one IP
IP_BLOCK_TIME = 300              # 5 minute IP block

MULTI_USER_THRESHOLD = 3         # Same IP attacks 3 usernames
PROGRESSIVE_DELAYS = [0, 2, 5, 10]

LOG_FILE = "security_logs.txt"

# ---------------- Tracking Storage ----------------
username_attempts = {}
account_locked_until = {}

ip_attempts = {}
ip_blocked_until = {}

ip_user_targets = {}

# ---------------- Logging Function ----------------
def log_event(status, username, ip, details=""):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] USER={username} IP={ip} STATUS={status} {details}\n"

    with open(LOG_FILE, "a") as file:
        file.write(entry)

# ---------------- Utility ----------------
def now():
    return time.time()

def is_account_locked(username):
    return username in account_locked_until and now() < account_locked_until[username]

def is_ip_blocked(ip):
    return ip in ip_blocked_until and now() < ip_blocked_until[ip]

# =====================================================
# MAIN PROGRAM
# =====================================================

print("=== Secure Login System ===")

# Demo IP input (simulating request source)
ip = input("Enter Source IP Address: ").strip()

while True:

    username = input("\nEnter Username: ").strip()
    password = input("Enter Password: ").strip()

    # ---------------- Check IP Block ----------------
    if is_ip_blocked(ip):
        remaining = int(ip_blocked_until[ip] - now())
        print(f"\nThis IP is blocked. Try again after {remaining} seconds.")
        log_event("IP_BLOCKED", username, ip)
        continue

    # ---------------- Check Account Lock ----------------
    if is_account_locked(username):
        remaining = int(account_locked_until[username] - now())
        print(f"\nAccount temporarily locked. Try again after {remaining} seconds.")
        log_event("ACCOUNT_LOCKED", username, ip)
        continue

    # ---------------- Correct Login ----------------
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        print("\nLogin Successful! Access Granted.")

        username_attempts[username] = 0
        ip_attempts[ip] = 0
        ip_user_targets[ip] = set()

        log_event("SUCCESS", username, ip)
        break

    # ---------------- Wrong Login ----------------
    else:
        print("\nInvalid Username or Password.")

        # Count username failures
        username_attempts[username] = username_attempts.get(username, 0) + 1

        # Count IP failures
        ip_attempts[ip] = ip_attempts.get(ip, 0) + 1

        # Track usernames targeted by this IP
        if ip not in ip_user_targets:
            ip_user_targets[ip] = set()

        ip_user_targets[ip].add(username)

        log_event("FAILED", username, ip)

        # ---------------- Progressive Delay ----------------
        fail_count = username_attempts[username]

        if fail_count < len(PROGRESSIVE_DELAYS):
            delay = PROGRESSIVE_DELAYS[fail_count]
        else:
            delay = PROGRESSIVE_DELAYS[-1]

        if delay > 0:
            print(f"Please wait {delay} seconds before next attempt.")
            time.sleep(delay)

        # ---------------- Account Lock ----------------
        if username_attempts[username] >= MAX_USERNAME_ATTEMPTS:
            account_locked_until[username] = now() + ACCOUNT_LOCK_TIME

            print("\nToo many failed attempts.")
            print("Account temporarily locked.")

            log_event("ACCOUNT_LOCK_TRIGGERED", username, ip)

        # ---------------- IP Block ----------------
        if ip_attempts[ip] >= MAX_IP_ATTEMPTS:
            ip_blocked_until[ip] = now() + IP_BLOCK_TIME

            print("\nSuspicious activity detected.")
            print("This IP has been temporarily blocked.")

            log_event("IP_BLOCK_TRIGGERED", username, ip)

        # ---------------- Multi Username Attack ----------------
        if len(ip_user_targets[ip]) >= MULTI_USER_THRESHOLD:
            print("\nAlert: Possible password spraying attack detected.")
            log_event("MULTI_USER_ATTACK", username, ip)