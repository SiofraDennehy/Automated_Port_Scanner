# Automated_Port_Scanner
<br/>

## Disclaimer - This tool is intended for educational and authorized security testing only. Do not use it to scan systems you do not own or have explicit permission to test. Unauthorized scanning may be illegal. 
<br/>

This is a Python Script that wraps around **Nmap** to scan ports in a user-specified list of targets. and output the results into another user-specified file.

---
## Features:

-Multi-threaded scanning for efficiency and to keep output clean and readable
-Asks user for targets, ports and output file for full flexibility
-Clean output to terminal for understanding at a glance
-Saves detailed results to report file with time stamps

## Requirements:

- Python 3.x
- [Nmap](https://nmap.org/) installed and available

## How to Use:

1. Clone this repository.
2. Create file with target list. Example: localhost, scanme.nmap.org
3. Run the Script with "python thread_scan.py" in terminal
4. Provide inputs to application when prompted




