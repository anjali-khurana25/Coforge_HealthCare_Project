power = float(input("Enter total power consumption (kW): "))
cooling = input("Enter cooling efficiency (good/poor): ").lower()
rack_load = float(input("Enter rack load percentage: "))

safe_power = 1000     
rack_threshold = 80    

if power > safe_power and cooling == "poor":
    print("Data Center Status: Critical")

elif rack_load > rack_threshold:
    print("Data Center Status: Warning")

elif cooling == "good" and rack_load <= rack_threshold and power <= safe_power:
    print("Data Center Status: Normal")

else:
    print("Data Center Status: Moderate Risk")