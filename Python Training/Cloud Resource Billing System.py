compute_hours = float(input("Enter number of compute hours: "))
storage_used = float(input("Enter storage used (GB): "))
support_plan = input("Enter support plan (Basic/Premium/Enterprise): ").lower()

if support_plan == "basic":
    support_fee = 500
    compute_rate = 10      
    storage_rate = 2        

elif support_plan == "premium":
    support_fee = 1000
    compute_rate = 8   
    storage_rate = 2

elif support_plan == "enterprise":
    support_fee = 2000
    compute_rate = 6    
    storage_rate = 1.5  

else:
    print("Invalid support plan!")
    exit()

if compute_hours <= 100:
    compute_charge = compute_hours * compute_rate
elif compute_hours <= 200:
    compute_charge = (100 * compute_rate) + ((compute_hours - 100) * (compute_rate + 2))
else:
    compute_charge = (100 * compute_rate) + (100 * (compute_rate + 2)) + ((compute_hours - 200) * (compute_rate + 4))

storage_charge = storage_used * storage_rate

total_bill = support_fee + compute_charge + storage_charge

print("Support Plan:", support_plan.capitalize())
print("Support Fee: ₹", support_fee)
print("Compute Charge: ₹", compute_charge)
print("Storage Charge: ₹", storage_charge)
print("Total Bill: ₹", total_bill)