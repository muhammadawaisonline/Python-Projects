import re 
from collections import Counter

# base class to Handle log enteries
class LogEntry:
    def __init__(self, line):
        # Store Log line for this instance
        self.line = line
        # Extract and store properties for this instance
        self.ip_address = self.extract_ip()
        self.date = self.extract_date()
    # Extract the ip address using regular Expression
    def extract_ip(self):
        
        ip_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
        match = re.search(ip_pattern, self.line)
        return match.group(0) if match else None
    
    def extract_date(self):
        # Extract the date from log entry using regex
         date_pattern = r"\b\d{2}/[A-Za-z]+/\d{4}:\d{2}:\d{2}:\d{2}\b"
         match = re.search(date_pattern, self.line)
         return match.group(0) if match else None
    def dispaly_info(self):
        return f"IP: {self.ip_address}, Date: {self.date}"
class ErrorLogEntry(LogEntry):
    def __init__(self, line):
        super().__init__(line)
        self.error_code = self.error_extract_code()


        # Extract HTTP Error Code (e.g. 404, 500)
    def extract_error_code(self):    
        error_pattern = r"\d{3}"
        match = re.search(error_pattern, self.line)
        return match.group(0).strip() if match else None
    def display_error_info(self):
        base_info = self.dispaly_info()
        return f" {base_info}, Error Code: {self.error_code} "



# Sample log data (in a real scenario, this would be read from a log file)
log_data = [
    '192.168.0.1 - - [12/Mar/2022:14:32:10 +0000] "GET /index.html HTTP/1.1" 200 1024',
    '192.168.0.2 - - [12/Mar/2022:14:35:20 +0000] "GET /about.html HTTP/1.1" 404 512',
    '192.168.0.3 - - [12/Mar/2022:14:36:30 +0000] "POST /login HTTP/1.1" 500 256',
    '192.168.0.1 - - [12/Mar/2022:14:37:40 +0000] "GET /contact.html HTTP/1.1" 200 768'
]

# List comprehension to create log entry object
log_entries = [ErrorLogEntry(line) for line in log_data]

# Dispaly all entries
print("All Log Entries: ")
for entry in log_entries:
    print(entry.display_error_info())
    
# Dictionary comprehension to count accourence of each IP address

ip_count = {ip: sum(1 for entry in log_entries if entry.ip_address == ip)
            for ip in {entry.ip_address for entry in log_entries}}
# Display IP Adress count
print("\nIP Adress Count: ")
for ip, count in ip_count.items():
    print(f"{ip}: {count}")

# Dictionary comprehension to count Error occurrence/ occurrence

error_count = {error: sum(1 for entry in log_entries if entry.error_code == error) 
               for error in {entry.error_code for entry in log_entries if entry.error_code}}

print("\nErrpr Count: ")
for error, count in error_count.items():
    print(f" Error {error}: {count}")

