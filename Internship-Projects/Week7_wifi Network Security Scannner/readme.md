# Week 7 – Wi-Fi Network Security Scanner

## Project Overview

The Wi-Fi Network Security Scanner is a Python-based cybersecurity project developed as part of the Cyber Security Internship Program.

This project scans nearby Wi-Fi networks and analyzes their security configurations to help users understand the risks associated with unsecured wireless connections.

In addition to identifying network names (SSID) and security types, the project applies basic SOC (Security Operations Center) monitoring concepts and CEH (Certified Ethical Hacker) security awareness concepts by classifying network risk levels, displaying potential threats, and providing security recommendations.

---

## Objectives

- Understand wireless network security concepts
- Identify different Wi-Fi security standards
- Detect unsecured wireless networks
- Learn the risks associated with public Wi-Fi
- Apply SOC monitoring and CEH security awareness concepts

---

## Features

- Scan available Wi-Fi networks
- Display Network Name (SSID)
- Display Authentication/Security Type
- Detect Open (Unsecured) Networks
- Risk Level Classification
- Security Threat Awareness
- Security Recommendations
- Security Summary Report
- Windows Command Integration using Python

---

## Security Classification

| Security Type | Risk Level |
|--------------|------------|
| Open | Critical |
| WEP | High |
| WPA | Medium |
| WPA2 | Low |
| WPA3 | Very Low |

---

## Threat Awareness

The scanner provides awareness of common wireless security threats:

### Open Networks
Possible Risks:
- Packet Sniffing
- Evil Twin Attack
- Man-in-the-Middle (MITM) Attack

### WEP Networks
Possible Risks:
- Weak Encryption
- Easy Password Cracking

### WPA Networks
Possible Risks:
- Older Security Standard
- Reduced Security Compared to WPA2/WPA3

---

## Technologies Used

- Python 3
- Windows Command Line (netsh)
- Subprocess Module
- String Processing
- SOC Monitoring Concepts
- CEH Security Awareness Concepts

---

## Project Structure

```text
Week7_WiFi_Scanner/

│
├── wifi_scanner.py
│
├── screenshots/
│   ├── code.png
│   ├── output.png
│   └── flow.png
│
└── README.md
```

---

## How It Works

1. Executes the Windows command:

```cmd
netsh wlan show networks
```

2. Collects nearby Wi-Fi network information.

3. Extracts:
   - SSID (Network Name)
   - Authentication Type

4. Classifies network security level.

5. Displays:
   - Risk Level
   - Possible Threats
   - Security Recommendations

6. Generates a security summary report.

---

## Sample Output

```text
=== Wi-Fi Security Scanner ===

Network Name : Home_WiFi
Security Type: WPA2-Personal
Risk Level   : LOW

Possible Threats:
- Generally Secure

Recommendation:
Safe for everyday usage.

--------------------------------------------------

Network Name : Free_Public_WiFi
Security Type: Open
Risk Level   : CRITICAL

Possible Threats:
- Packet Sniffing
- Evil Twin Attack
- Man-in-the-Middle Attack

Recommendation:
Avoid sensitive logins and banking transactions.

--------------------------------------------------

===== Security Summary =====

Total Networks Found : 5
Open Networks        : 1
Secured Networks     : 4
```

---

## Learning Outcomes

After completing this project, I understood:

- Basics of wireless security
- Difference between Open, WEP, WPA, WPA2, and WPA3
- Risks of public Wi-Fi networks
- Wireless attack awareness
- Security risk classification
- SOC-style monitoring and reporting concepts
- CEH-based threat awareness concepts
- Python system command execution

---

## Future Enhancements

- Real-time Wi-Fi monitoring
- Export scan results to CSV
- Security score calculation
- Detection of duplicate SSIDs
- GUI-based Wi-Fi scanner
- Alert notifications for insecure networks

---

## Author

**Arti Ganesh Mayanikar**

Cyber Security Internship – Week 7 Project

Wi-Fi Network Security Scanner
