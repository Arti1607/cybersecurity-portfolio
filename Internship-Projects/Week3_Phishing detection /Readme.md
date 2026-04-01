# 🔐 Phishing URL Detector

## 📌 Project Overview

The **Phishing URL Detector** is a basic cybersecurity tool developed in Python to identify potentially malicious or phishing URLs using pattern-based analysis.

This project is part of a cybersecurity internship (Week 3) and focuses on understanding how attackers design deceptive links to trick users into revealing sensitive information.

---

## 🎯 Objective

The main objective of this project is to:

* Analyze URLs for common phishing indicators
* Classify URLs into risk levels (Safe, Suspicious, Phishing Risk)
* Help users understand basic phishing detection techniques

---

## ⚙️ Features

* 🔍 User input URL analysis
* ⚠️ Detection of common phishing patterns:

  * Use of IP address instead of domain
  * Presence of “@” symbol
  * Long or complex URLs
  * Hyphens in domain
  * Suspicious keywords (e.g., login, verify, bank)
  * Non-HTTPS URLs
* 📊 Risk level classification:

  * Safe
  * Suspicious
  * Phishing Risk
* 💻 Simple command-line interface

---

## 🛠️ Technologies Used

* Python
* Regular Expressions (re module)
* URL Parsing (urllib.parse)

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/phishing-url-detector.git
cd phishing-url-detector
```

### 2. Run the Program

```bash
python phishing_detector.py
```

### 3. Enter URL

Example:

```
Enter website URL: http://fake-bank-login.com@192.168.0.1
```

---

## 📌 Sample Output

### 🔴 Phishing Example

```
Result: Phishing Risk

Warnings:
- Contains '@' symbol
- Uses IP address instead of domain
- Not using HTTPS
```

### 🟢 Safe Example

```
Result: Safe
```

---

## 📂 Project Structure

```
Week3_Phishing_URL_Detector/
│
├── phishing_detector.py
├── test_urls.txt
├── screenshots/
│   ├── code.png
│   ├── safe_output.png
│   ├── phishing_output.png
│   └── flow.png
└── README.md
```

---

## 🧠 Learning Outcomes

* Understanding phishing attack techniques
* URL structure and analysis
* Pattern matching using Python
* Basics of cybersecurity detection methods

---

## ⚠️ Limitations

* Rule-based detection (not AI/ML-based)
* Cannot detect advanced or highly sophisticated phishing attacks
* No real-time threat intelligence integration

---

## 🔮 Future Scope

* Integration with phishing databases (e.g., Google Safe Browsing)
* Machine learning-based detection
* GUI or web-based interface

---

## 👩‍💻 Author

Internship Project – Cybersecurity (Week 3)

---

## ⭐ Acknowledgement

This project was developed as part of a cybersecurity internship to gain practical exposure to phishing detection techniques.
