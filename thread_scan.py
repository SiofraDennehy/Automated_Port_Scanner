import subprocess
from datetime import datetime
from threading import Thread, Lock

print_lock = Lock() #Lock to synchronise printing between threads

def run_nmap(target, ports, report_file): #function takes 3 inputs
    try:
        result = subprocess.run(
            ["nmap", "-sS", "-Pn", "-T4", "-p", ports, target],
            capture_output=True, text=True
        ) #captures scan output as result so it can be input to a file later
        output = result.stdout #default output stream

        with print_lock:
            print(f"\nScanning {target} on ports {ports}... \n{'-'*40}")
            print(f"[+] Open Ports on {target}:")
            for line in output.splitlines():
                if "open" in line:
                    print(f"  {line}")

        with open(report_file, "a") as file:
            file.write(f"\n Scan Result for {target} ({datetime.now()}) \n")
            file.write(output + "\n")

    except Exception as e:
        with print_lock:
            print(f"Error scanning {target}: {e}")

def load_targets(filename): #takes in a file as input that includes the targets for the scan
    with open(filename, "r") as file:
        targets = [line.strip() for line in file if line.strip()] #removes any empty spaces before and after each name
    return targets #returns name without spaces
    
if __name__ == "__main__": #starts code when executed but not imported
    filename = input("Enter file with target list (e.g. targets.txt): ") #takes user input for target list
    ports = input("Enter ports to scan (e.g. 22,80 or 1-1000):") #takes user input for which ports to scan
    report_file = input("Enter filename to save results to (e.g. scan_results.txt):") # takes user input for output file

    targets = load_targets(filename) # sets sanitised target list as input for scan function

    print(f"\nStarting scan as {datetime.now()}\n{'='*50}") #Tells user start time

    threads = [] #sets empty array list for threads to inhabit

    for target in targets: #for each target in list
        t = Thread(target=run_nmap, args=(target, ports, report_file)) #create thread
        t.start() #start thread
        threads.append(t) #add thread to array

    for t in threads: #for each thread in thread array
        t.join() #blocks programme until thread has completed

    print(f"\nAll done :) Full results saved to: {report_file}\n")