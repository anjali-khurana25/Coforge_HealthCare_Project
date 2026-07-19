defects = int(input("Enter defect count: "))
temperature = float(input("Enter machine temperature (°C): "))
speed = float(input("Enter production speed (units/hour): "))
experience = int(input("Enter operator experience (years): "))

defect_limit = 10
high_temperature = 80
high_speed = 100
low_experience = 2

if defects > defect_limit:
    print("Batch Status: Rejected")

elif temperature > high_temperature and speed > high_speed:
    print("Batch Status: Risk")

elif experience < low_experience and defects > 0:
    print("Batch Status: Warning")

else:
    print("Batch Status: Accepted")