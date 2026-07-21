# emp_id = ""
# emp_name = ""
# designation = ""
# emp_salary = 0

# def add_employee():
#     global emp_id, emp_name, designation, emp_salary

#     emp_id = input("Enter Employee ID: ")
#     emp_name = input("Enter Employee Name: ")
#     designation = input("Enter Designation: ")
#     emp_salary = float(input("Enter Employee Salary: "))

#     print("Employee Added Successfully")

# def view_employee():
#     if emp_id == "":
#         print("No Employee Record Found")
#     else:
#         print("\nEmployee Details")
#         print("Employee ID      :", emp_id)
#         print("Employee Name    :", emp_name)
#         print("Designation      :", designation)
#         print("Employee Salary  :", emp_salary)

# def search_employee():
#     search = input("Enter Employee ID to Search: ")

#     if search == emp_id:
#         print("\nEmployee Found")
#         print("Employee ID      :", emp_id)
#         print("Employee Name    :", emp_name)
#         print("Designation      :", designation)
#         print("Employee Salary  :", emp_salary)
#     else:
#         print("Employee Not Found")

# while True:
#     print("\n===== EMPLOYEE MENU =====")
#     print("1. Add Employee")
#     print("2. View Employee")
#     print("3. Search Employee")
#     print("4. Exit")

#     choice = int(input("Enter Your Choice: "))

#     if choice == 1:
#         add_employee()
#     elif choice == 2:
#         view_employee()
#     elif choice == 3:
#         search_employee()
#     elif choice == 4:
#         print("Thank You!")
#         break
#     else:
#         print("Invalid Choice")

Employee_skills = {
    "EMP101": "Python",
    "EMP102": "Java",
    "EMP103": "C++",
    "EMP104": "SQL",
    "EMP105": "HTML",
    "EMP106": "CSS",
    "EMP107": "JavaScript"
}

while True:
    print("\n----------------------------------------")
    print("Employee Skill Management System")
    print("----------------------------------------")
    print("1. Display Skills")
    print("2. Add Skill")
    print("3. Update Skill")
    print("4. Remove Skill")
    print("5. Search Skill")
    print("6. Count Skills")
    print("7. Sort Employee IDs")
    print("8. Copy Dictionary")
    print("9. Clear Dictionary")
    print("10. Display Using enumerate()")
    print("11. Exit")

    choice = input("Enter your choice (1-11): ")

    if choice == "1":
        if len(Employee_skills) == 0:
            print("No employee skills available.")
        else:
            print("\nEmployee Skills:")
            for emp_id, skill in Employee_skills.items():
                print(f"{emp_id} : {skill}")

    elif choice == "2":
        emp_id = input("Enter Employee ID: ")
        skill = input("Enter Skill: ")

        if emp_id not in Employee_skills:
            Employee_skills[emp_id] = skill
            print("Skill added successfully.")
        else:
            print("Employee ID already exists.")

    elif choice == "3":
        emp_id = input("Enter Employee ID to update: ")

        if emp_id in Employee_skills:
            new_skill = input("Enter New Skill: ")
            Employee_skills[emp_id] = new_skill
            print("Skill updated successfully.")
        else:
            print("Employee ID not found.")

    elif choice == "4":
        emp_id = input("Enter Employee ID to remove: ")

        if emp_id in Employee_skills:
            del Employee_skills[emp_id]
            print("Employee deleted successfully.")
        else:
            print("Employee ID not found.")

    elif choice == "5":
        skill = input("Enter Skill to search: ")

        found = False
        for emp_id, emp_skill in Employee_skills.items():
            if emp_skill.lower() == skill.lower():
                print(f"{skill} found for Employee ID: {emp_id}")
                found = True

        if not found:
            print("Skill not found.")

    elif choice == "6":
        print("Total Employees:", len(Employee_skills))

    elif choice == "7":
        print("\nSorted Employee IDs:")
        for emp_id in sorted(Employee_skills):
            print(f"{emp_id} : {Employee_skills[emp_id]}")

    elif choice == "8":
        copied_dict = Employee_skills.copy()
        print("Dictionary copied successfully.")
        print(copied_dict)

    elif choice == "9":
        Employee_skills.clear()
        print("All employee records cleared.")

    elif choice == "10":
        print("\nEmployee Skills using enumerate():")
        for i, (emp_id, skill) in enumerate(Employee_skills.items(), start=1):
            print(f"{i}. {emp_id} : {skill}")

    elif choice == "11":
        print("Exiting Employee Skill Management System.")
        break

    else:
        print("Invalid choice. Please enter between 1 and 11.")
