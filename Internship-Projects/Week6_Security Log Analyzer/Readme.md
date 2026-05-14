# Week 6 – Security Log Analyzer

## Project Overview

The Security Log Analyzer is a Python-based cybersecurity project developed as part of the Cyber Security Internship Program.

This project focuses on analyzing security logs to identify suspicious activities such as:

- Multiple failed login attempts
- Brute force attack patterns
- Password spraying attacks
- SQL Injection attempts
- Cross-Site Scripting (XSS) patterns

The project applies basic SOC (Security Operations Center) monitoring concepts and CEH (Certified Ethical Hacker) attack detection techniques using log analysis and pattern matching.

---

# Features

- Read and analyze log files
- Detect failed login attempts
- Identify brute force attacks
- Detect password spraying attacks
- Detect suspicious SQL Injection patterns
- Detect XSS attack patterns
- Generate security alerts
- Display summary report

---

# Technologies Used

- Python 3
- File Handling
- Dictionaries & Data Structures
- Pattern Matching
- SOC Monitoring Concepts
- CEH Attack Detection Concepts

---

# Project Structure

Week6_Log_Analyzer/
│
├── log_analyzer.py
├── log.txt
├── screenshots/
│ ├── code.png
│ ├── log_file.png
│ ├── output.png
│ └── flow.png
└── README.md

---

# Sample Log Format

```text
2026-02-01 10:12:10 LOGIN FAILED user2 192.168.1.5

2026-02-01 10:15:30 REQUEST /login username=admin password=' OR 1=1 -- 192.168.1.8

2026-02-01 10:16:10 REQUEST /search?q=<script>alert('XSS')</script> 192.168.1.9

Detected Threats
1. Brute Force Attack
Detects repeated failed login attempts on the same user account.
2. Password Spraying
Detects one IP targeting multiple usernames.
3. SQL Injection Detection
Detects suspicious SQL keywords and payloads inside logs.
4. XSS Detection
Detects script injection patterns inside request logs.
How to Run
Step 1
Open terminal in project folder.
Step 2
Run the Python file:
Bash
python log_analyzer.py
Step 3
Enter the log file path when prompted.
Example:
Plain text
C:\Users\Admin\Desktop\Week6_Log_Analyzer\Log.txt
Sample Output
Plain text
[ALERT] Brute Force Attack Detected on user: user2

[ALERT] Possible SQL Injection Detected

[ALERT] Possible XSS Attack Detected

[ALERT] Password Spraying Detected from IP: 192.168.1.5

Learning Outcomes
After completing this project, I understood:
Importance of security log monitoring
SOC monitoring workflow
Incident detection concepts
Brute force attack detection
Password spraying detection
SQL Injection pattern analysis
XSS attack pattern detection
Python file handling and data processing

Future Improvements
Real-time log monitoring
Email alert system
GUI dashboard
Integration with SIEM tools
Export security reports

Author
Arti Ganesh Mayanikar
Cyber Security Internship – Week 6 Project
