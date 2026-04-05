# CyberTrap-Intelligent-Honeypot-with-Attack-Visualization
CyberTrap is a lightweight cybersecurity project that implements a honeypot system to simulate vulnerable network services and capture malicious activities in real time. The system is designed to attract attackers, record their interactions, and provide insights into unauthorized access attempts.

The honeypot server is built using Python socket programming and listens on a specific port, mimicking a real service such as a login interface. When an attacker connects, the system captures critical details including IP address, port number, timestamp, and input data. These interactions are stored in a structured JSON format for efficient logging and analysis.

To enhance usability, CyberTrap includes a web-based dashboard developed using Flask. The dashboard displays captured attack data in a clear tabular format, enabling real-time monitoring of suspicious activities. This allows users to observe attacker behavior and analyze patterns effectively.

This project demonstrates fundamental cybersecurity concepts such as intrusion detection, threat monitoring, and defensive system design. It is designed to be simple, efficient, and suitable for educational purposes, making it ideal for beginners exploring network security.
