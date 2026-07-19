principle = int(input("Enter the principal amount: "))
rate = int(input("Enter the rate of interest: "))
time = int(input("Enter the time: "))

simple_interest = (principle * rate * time) / 100
print(f"The Simple Interest is: {simple_interest}")

amount = principle * (1 + rate / 100) ** time
compound_interest = amount - principle

print(f"The Compound Interest is: {compound_interest}")