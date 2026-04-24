🔐 Secure Login System with Brute Force Protection

📌 Project Overview

The Secure Login System with Brute Force Protection is a Python-based cybersecurity project developed as part of a Cyber Security Internship (Week 5).

This project simulates a secure authentication system that protects user accounts from brute force attacks by limiting failed login attempts, temporarily locking accounts, detecting suspicious IP behavior, and logging security events.

The project was later enhanced using SOC (Security Operations Center) and CEH (Certified Ethical Hacker) concepts to demonstrate advanced defensive security logic.

---

🎯 Objective

- Understand authentication security mechanisms
- Learn how brute force attacks work
- Implement account lockout protection
- Detect suspicious login activity
- Apply SOC and CEH defensive concepts using Python

---

⚙️ Features

🔑 Authentication Features

- Username and password verification
- Secure login validation
- Successful login access message

🛡️ Brute Force Protection

- Maximum 3 failed attempts per username
- Temporary account lock after repeated failures
- Progressive delay after wrong attempts

🌐 IP Security Monitoring

- Detect repeated failed attempts from same IP
- Temporary IP block on suspicious activity
- Detect multiple usernames targeted from one IP (password spraying simulation)

📊 SOC Security Features

- Security log generation
- Timestamp-based event tracking
- Login success/failure records
- Suspicious activity alerts

---

🛠️ Technologies Used

- Python
- "time" module
- "datetime" module
- File handling
- Dictionaries for security tracking

---

🚀 How to Run the Project

1️⃣ Clone Repository

git clone https://github.com/Arti1607/cybersecurity-portfolio.git

2️⃣ Open Project Folder

cd Internship-Projects/Week5_SecureLogin

3️⃣ Run Python File

python secure_login.py

---

💻 Sample Output

✅ Successful Login

=== Secure Login System ===
Enter Username: admin
Enter Password: Admin@123

Login Successful! Access Granted.

---

❌ Failed Attempts

Invalid Username or Password.
Please wait 2 seconds before next attempt.

---

🔒 Account Lock

Too many failed attempts.
Account temporarily locked.

---

🚫 Suspicious IP Block

Suspicious activity detected.
This IP has been temporarily blocked.

---

📂 Project Structure

Week5_SecureLogin/
│
├── secure_login.py
├── security_logs.txt
├── screenshots/
│   ├── code.png
│   ├── success_output.png
│   ├── failed_output.png
│   └── flow.png
└── README.md

---

📊 Security Logic Implemented

Username Protection

- 3 failed attempts → Temporary account lock

IP Protection

- Excessive failures from same IP → Temporary IP block

Attack Detection

- Multiple usernames targeted by one IP → Password spraying alert

Delay Control

- Wrong attempts trigger progressive delay

---

📁 Log File Example

[2026-04-13 14:22:05] USER=admin IP=192.168.1.5 STATUS=FAILED
[2026-04-13 14:23:12] USER=admin IP=192.168.1.5 STATUS=ACCOUNT_LOCK_TRIGGERED

---

🧠 Learning Outcomes

After completing this project, I understood:

- Authentication systems
- Brute force attack concepts
- Account lockout mechanisms
- IP-based attack detection
- Password spraying basics
- SOC event logging concepts
- Python logic building for cybersecurity

---

⚠️ Disclaimer

This project is developed for educational purposes only.
It is a simulation of login security concepts and should not be used as a production authentication system without further security enhancements.

---

🔮 Future Enhancements

- Password hashing using bcrypt
- Database integration
- OTP / Multi-Factor Authentication
- CAPTCHA support
- Email alert system
- Dashboard for security monitoring
- SIEM integration (Splunk / ELK)

---

👩‍💻 Author

Arti Ganesh Mayanikar
Cyber Security Internship – Week 5 Project
