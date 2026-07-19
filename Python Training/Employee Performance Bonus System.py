rating = int(input("Enter employee rating (1-5): "))
experience = int(input("Enter years of experience: "))
delivery_status = input("Enter project delivery status (on time/delayed): ").lower()

if rating == 5 and experience > 10 and delivery_status == "on time":
    print("Bonus: 30%")

elif rating == 4 and experience > 7:
    print("Bonus: 20%")

elif rating == 3 and delivery_status == "delayed":
    print("Bonus: 5%")

else:
    print("No Bonus")