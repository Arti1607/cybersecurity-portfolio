🌐 Network Port Scanner
📌 Project Overview
The Network Port Scanner is a Python-based cybersecurity tool developed to scan a target system (IP address or domain) and identify open ports within a given range.
This project is part of a cybersecurity internship (Week 4) and demonstrates how open ports can expose services and create potential security risks.
🎯 Objective
To understand how port scanning works
To identify open ports on a target system
To learn the basics of network security assessment
⚙️ Features
Scan target using IP address or domain
Detect open ports within a custom range
Fast and simple command-line interface
Displays scan summary (time taken + open ports)
Basic input validation and error handling
🛠️ Technologies Used
Python
Socket Programming (socket module)
Time module (time)
🚀 How to Run the Project
1. Clone the Repository
git clone https://github.com/your-username/network-port-scanner.git
cd network-port-scanner
2. Run the Script
python port_scanner.py
3. Enter Details
Example:
Enter target IP or domain: scanme.nmap.org
Enter starting port: 20
Enter ending port: 100
📌 Sample Output
Scanning target: scanme.nmap.org
Port range: 20 - 100

Port 22 is OPEN
Port 80 is OPEN

--- Scan Summary ---
Time taken: 2.35 seconds
Open Ports: [22, 80]
