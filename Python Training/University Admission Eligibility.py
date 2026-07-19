exam_score = float(input("Enter entrance exam score: "))
percentage = float(input("Enter 12th percentage: "))
category = input("Enter category (General/SC/ST/OBC): ").lower()
extra_score = float(input("Enter extracurricular score (out of 100): "))

if exam_score >= 90 and percentage >= 85:
    print("Admission Status: Direct Admission")

elif category in ["sc", "st", "obc"] and exam_score >= 80 and percentage >= 75:
    print("Admission Status: Direct Admission (Category Relaxation)")

elif exam_score >= 70 and extra_score >= 80:
    print("Admission Status: Waitlist")

else:
    print("Admission Status: Rejected")