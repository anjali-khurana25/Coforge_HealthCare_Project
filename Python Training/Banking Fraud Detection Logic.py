transaction_amount = float(input("Enter transaction amount: ₹"))
location_mismatch = input("Is there a location mismatch? (yes/no): ").lower()
unusual_login = input("Is the login time unusual? (yes/no): ").lower()
account_age = int(input("Enter account age (in months): "))
repeated_activity = input("Is there repeated unusual activity? (yes/no): ").lower()

if transaction_amount > 100000 and location_mismatch == "yes":
    print("Transaction Status: Fraud Alert")

elif account_age < 6 and unusual_login == "yes":
    print("Transaction Status: Risk Alert")

elif 50000 <= transaction_amount <= 100000 and repeated_activity == "yes":
    print("Transaction Status: Review Required")

else:
    print("Transaction Status: Approved")