age = int(input("Enter customer age: "))
smoking = input("Do you smoke? (yes/no): ").lower()
bmi = float(input("Enter BMI: "))
disease = input("Do you have a severe pre-existing disease? (yes/no): ").lower()

if disease == "yes" and age > 60:
    print("Insurance Status: Rejected")

elif smoking == "yes" and age > 50:
    print("Insurance Premium: High")

elif bmi >= 25:
    print("Insurance Premium: Medium")

elif smoking == "no" and bmi < 25 and age < 35 and disease == "no":
    print("Insurance Premium: Low")

else:
    print("Insurance Premium: Standard")