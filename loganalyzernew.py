import csv
from datetime import datetime, timedelta
import random
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# Step 1: Generate CSV File
# -------------------------
filename = "securitynew.csv"

columns = ["EventID", "Timestamp", "SourceIP", "DestinationIP", "Protocol", 
           "Action", "Username", "Status", "Severity", "Description"]

protocols = ["TCP", "UDP", "ICMP", "HTTP", "HTTPS", "SSH"]
actions = ["ALLOW", "DENY", "BLOCK", "ALERT"]
statuses = ["Success", "Failed"]
usernames = ["admin", "user1", "guest", "service"]
descriptions = [
    "Login attempt", "File access", "Firewall blocked", 
    "Suspicious activity", "Port scan detected", "Malware alert"
]

def random_ip():
    return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"

def random_timestamp():
    start = datetime.now() - timedelta(days=30)
    random_time = start + timedelta(seconds=random.randint(0, 30*24*3600))
    return random_time.strftime("%Y-%m-%d %H:%M:%S")

with open(filename, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    for i in range(1, 51):  # 50 sample rows
        writer.writerow({
            "EventID": i,
            "Timestamp": random_timestamp(),
            "SourceIP": random_ip(),
            "DestinationIP": random_ip(),
            "Protocol": random.choice(protocols),
            "Action": random.choice(actions),
            "Username": random.choice(usernames),
            "Status": random.choice(statuses),
            "Severity": random.choice(["Low", "Medium", "High", "Critical"]),
            "Description": random.choice(descriptions)
        })

print(f"{filename} generated successfully!")

# -------------------------
# Step 2: Read CSV with Pandas
# -------------------------
df = pd.read_csv(filename)
print("\n--- First 10 Rows ---")
print(df.head(10))

# -------------------------
# Step 3: Visual Outputs
# -------------------------
# Bar chart: Number of events by Action
plt.figure(figsize=(6,4))
df['Action'].value_counts().plot(kind='bar', color='skyblue', title='Events by Action')
plt.xlabel('Action')
plt.ylabel('Number of Events')
plt.show()

# Bar chart: Number of events by Protocol
plt.figure(figsize=(6,4))
df['Protocol'].value_counts().plot(kind='bar', color='orange', title='Events by Protocol')
plt.xlabel('Protocol')
plt.ylabel('Number of Events')
plt.show()
