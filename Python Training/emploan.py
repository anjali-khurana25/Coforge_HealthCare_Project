name = input("Enter applicant name: ")
age = int(input("Enter age: "))
salary = float(input("Enter monthly salary: "))
experience = float(input("Enter work experience in years: "))
credit_score = int(input("Enter credit score: "))
emi = float(input("Enter existing monthly EMI: "))

print("Applicant name: ",name)

if age < 21 or age > 58:
    print("Loan Application Status: Rejected")
    print("Reason: Age should be between 21 and 58 years.")
    
elif experience < 2:
    print("Loan Application Status: Rejected")
    print("Reason: Work experience should be at least 2 years.")
    
elif credit_score < 650:
    print("Loan Application Status: Rejected")
    print("Reason: Credit score is below 650.")
    
elif emi > (0.40 * salary):
    print("Loan Application Status: Rejected")
    print("Reason: Existing EMI is more than 40% of monthly salary.")
    
else:
    if 25000 <= salary <= 39999:
        loan = 200000
    elif 40000 <= salary <= 59999:
        loan = 500000
    elif 60000 <= salary <= 99999:
        loan = 1000000
    elif salary >= 100000:
        loan = 1500000
    else:
        loan = 0

    if loan == 0:
        print("Loan Application Status: Rejected")
        print("Reason: Monthly salary is below ₹25,000.")
    else:
        print("Loan Application Status: Eligible")
        print(f"Maximum Loan Amount: ₹{loan:,}")