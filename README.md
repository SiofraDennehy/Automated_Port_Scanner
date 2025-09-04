[scan_results.txt](https://github.com/user-attachments/files/22140828/scan_results.txt)# Automated_Port_Scanner
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

## Example Output:

In terminal: <br/>
<img width="717" height="407" alt="scan" src="https://github.com/user-attachments/assets/fabc78c1-f9f5-4292-8f63-f3b77235c4c2" />


In Output File:<br/>
<img width="870" height="572" alt="scan_results" src="https://github.com/user-attachments/assets/ba6d4197-0f72-4dbf-97a5-5e261a8a93c0" />

