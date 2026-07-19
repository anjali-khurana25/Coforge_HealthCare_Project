cpu = float(input("Enter CPU usage (%): "))
memory = float(input("Enter Memory usage (%): "))
disk = float(input("Enter Disk usage (%): "))
latency = float(input("Enter Network latency (ms): "))

threshold = 100

if cpu > 90 and memory > 85:
    print("Server Status: Critical Alert")

elif disk > 95:
    print("Server Status: Storage Critical")

elif latency > threshold:
    print("Server Status: Network Issue")

elif cpu > 70 or memory > 70 or disk > 80:
    print("Server Status: Warning")

else:
    print("Server Status: Healthy")