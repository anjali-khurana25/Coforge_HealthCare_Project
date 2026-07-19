salary = float(input("Enter monthly salary: "))
credit_score = int(input("Enter credit score: "))
existing_loan = float(input("Enter existing loan amount: "))
employment_type = input("Enter employment type: ")

if salary > 80000 and credit_score > 750 and existing_loan < 20000:
    print("Loan Status: Approved Immediately")

elif salary > 50000 and credit_score > 650:
    print("Loan Status: Approved with Caution")

elif credit_score < 600:
    print("Loan Status: Rejected")

else:
    print("Loan Status: Under Manual Review")