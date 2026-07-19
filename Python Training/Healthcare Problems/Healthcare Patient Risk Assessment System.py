name = input("Enter Patient Name: ")
age = int(input("Enter Patient Age: "))
temperature = float(input("Enter Body Temperature (°C): "))
heart_rate = int(input("Enter Heart Rate (BPM): "))
oxygen = float(input("Enter Oxygen Saturation (SpO₂): "))

print("Patient Name:", name)

if oxygen < 90 or temperature > 40:
    print("Risk Level: Critical")
    print("Recommendation: Immediately transfer the patient to ICU.")

elif (90 <= oxygen <= 94) or (38 <= temperature <= 40):
    print("Risk Level: High")
    print("Recommendation: Doctor consultation and hospital admission required.")

elif heart_rate > 100 or age > 60:
    print("Risk Level: Medium")
    print("Recommendation: Keep the patient under observation.")

else:
    print("Risk Level: Low")
    print("Recommendation: Patient is healthy and can go home after consultation.")

if age >= 75:
    print("Senior Citizen")
    print("Priority Consultation Required")