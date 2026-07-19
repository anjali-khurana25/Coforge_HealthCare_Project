usage = float(input("Enter monthly usage (hours): "))
missed_payments = int(input("Enter number of missed payments: "))
tickets = int(input("Enter support tickets count: "))
satisfaction = float(input("Enter satisfaction score (out of 10): "))

high_usage = 50
low_usage = 10
many_complaints = 5
payment_threshold = 2
high_satisfaction = 8

if usage >= high_usage and satisfaction >= high_satisfaction:
    print("Renewal Status: Likely Renew")

elif usage <= low_usage and tickets >= many_complaints:
    print("Renewal Status: High Churn Risk")

elif missed_payments > payment_threshold:
    print("Renewal Status: Payment Risk")

else:
    print("Renewal Status: Moderate Renewal Probability")