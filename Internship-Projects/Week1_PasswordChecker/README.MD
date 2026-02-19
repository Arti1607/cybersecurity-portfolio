🛡 Password Strength Checker
📌 Project Overview

The Password Strength Checker is a Python-based command-line tool designed to evaluate password security based on widely accepted cybersecurity standards.

This project demonstrates fundamental concepts of authentication security and input validation.

🎯 Objective

To analyze a user-provided password and classify it as:

Weak

Medium

Strong

based on predefined security rules.

🔍 Security Rules Implemented

The password is evaluated against the following criteria:

Minimum length of 8 characters

At least one uppercase letter

At least one lowercase letter

At least one numeric digit

At least one special character

Each satisfied rule increases the strength score.

⚙️ Technologies Used

Python 3

Regular Expressions (re module)

Command Line Interface

🧠 Strength Classification Logic
Score	Classification
0–2	Weak
3–4	Medium
5	Strong
📸 Sample Output
Weak Password

Short length

Missing character variety

Strong Password

Meets all defined security requirements

(Screenshots available in the screenshots/ folder.)

📚 Learning Outcomes

Understanding password security principles

Applying regular expressions for validation

Implementing rule-based classification systems

Improving cybersecurity awareness

🚀 Future Improvements

Add password entropy calculation

Convert to GUI version

Integrate password blacklist detection

Add logging functionality