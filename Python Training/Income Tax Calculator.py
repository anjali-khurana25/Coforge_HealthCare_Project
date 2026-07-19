income = float(input("Enter annual income: "))
age = int(input("Enter age: "))
investment = float(input("Enter investment amount: "))

if age >= 60:
    exemption = 100000
else:
    exemption = 0

taxable_income = income - investment - exemption

if taxable_income < 0:
    taxable_income = 0

if taxable_income < 500000:
    tax = 0

elif taxable_income <= 1000000:
    tax = taxable_income * 0.10

elif taxable_income <= 2000000:
    tax = taxable_income * 0.20

else:
    tax = taxable_income * 0.30


print("Annual Income:", income)
print("Age:", age)
print("Investment Amount:", investment)
print("Senior Citizen Exemption:", exemption)
print("Taxable Income:", taxable_income)
print("Tax Payable: ₹", tax)