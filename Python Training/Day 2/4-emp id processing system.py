for emp_id in range(1, 51):

    if emp_id == 37:
        print("Employee ID 37 found. Processing stopped.")
        break

    if emp_id % 5 == 0:
        continue

    if emp_id > 20:
        print(emp_id)