severity = input("Enter issue severity (critical/medium/low): ").lower()
department = input("Enter department: ")
impact = input("Enter business impact (high/medium/low): ").lower()
vip_status = input("Is user VIP? (yes/no): ").lower()

if severity == "critical" and vip_status == "yes":
    print("Issue Priority: P1")

elif severity == "critical" and impact == "high":
    print("Issue Priority: P1")

elif severity == "medium":
    print("Issue Priority: P3")

elif severity == "low":
    print("Issue Priority: P4")

else:
    print("Issue Priority: P2")