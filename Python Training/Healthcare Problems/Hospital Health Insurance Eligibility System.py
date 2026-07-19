name = input("Enter Patient Name: ")
age = int(input("Enter Patient Age: "))
insurance_status = input("Enter Insurance Status (Yes/No): ").lower()
policy_status = input("Enter Policy Status (Active/Expired): ").lower()
treatment_cost = float(input("Enter Estimated Treatment Cost (₹): "))

print("Patient Name:", name)

if insurance_status == "yes" and policy_status == "active" and treatment_cost <= 500000:
    print("Insurance Status: Approved")
    print("Approval Status: Cashless Treatment Approved")
    print("Final Decision: Patient is eligible for Cashless Treatment.")

    if age >= 65:
        print("Senior Citizen Benefit Applied")
        print("5% Discount on Hospital Service Charges")

elif insurance_status == "yes" and policy_status == "active" and treatment_cost <= 1000000:
    print("Insurance Status: Pending Approval")
    print("Approval Status: Additional Approval Required")
    print("Final Decision: Additional approval from the insurance company is required.")

elif insurance_status == "yes" and policy_status == "expired":
    print("Insurance Status: Rejected")
    print("Approval Status: Cashless Treatment Not Available")
    print("Final Decision: Insurance policy has expired. Cashless treatment is not available.")

elif insurance_status == "no":
    print("Insurance Status: Not Available")
    print("Approval Status: Self Payment")
    print("Final Decision: Patient must pay the treatment cost.")

else:
    print("Invalid patient information entered.")