age = int(input("Enter patient age: "))
oxygen = float(input("Enter oxygen level (%): "))
heart_rate = int(input("Enter heart rate (bpm): "))
severity = input("Enter symptom severity (mild/moderate/severe): ").lower()

if oxygen < 90:
    print("Patient Status: Emergency")

elif age >= 60 and severity == "severe":
    print("Patient Status: High Priority")

elif severity == "mild":
    print("Patient Status: General Queue")

else:
    print("Patient Status: Medium Priority")