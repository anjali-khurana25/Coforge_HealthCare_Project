# Employee Project Management System (Tuple + List)

employees = []


def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")

    n = int(input("Enter Number of Projects: "))
    projects = []

    for i in range(n):
        project = input("Enter Project Name: ")
        projects.append(project)

    employee = (emp_id, name, department, projects)
    employees.append(employee)

    print("Employee added successfully.")


def view_employees():
    if len(employees) == 0:
        print("No employee records found.")
    else:
        for emp in employees:
            print("\nEmployee ID :", emp[0])
            print("Name        :", emp[1])
            print("Department  :", emp[2])
            print("Projects    :", ", ".join(emp[3]))
            print("---------------------------------------")


def assign_project():
    emp_id = int(input("Enter Employee ID: "))
    found = False

    for emp in employees:
        if emp[0] == emp_id:
            project = input("Enter New Project Name: ")
            emp[3].append(project)
            print("Project assigned successfully.")
            found = True
            break

    if found == False:
        print("Employee not found.")


def remove_project():
    emp_id = int(input("Enter Employee ID: "))
    found = False

    for emp in employees:
        if emp[0] == emp_id:
            project = input("Enter Project Name: ")

            if project in emp[3]:
                emp[3].remove(project)
                print("Project removed successfully.")
            else:
                print("Project not found.")
            found = True
            break

    if found == False:
        print("Employee not found.")


def search_employee():
    emp_id = int(input("Enter Employee ID: "))
    found = False

    for emp in employees:
        if emp[0] == emp_id:
            print("\nEmployee ID :", emp[0])
            print("Name        :", emp[1])
            print("Department  :", emp[2])
            print("Projects    :", ", ".join(emp[3]))
            found = True
            break

    if found == False:
        print("Employee not found.")


def multiple_projects():
    found = False

    for emp in employees:
        if len(emp[3]) > 2:
            print("\nName :", emp[1])
            print("Projects :", len(emp[3]))
            found = True

    if found == False:
        print("No employee is working on more than two projects.")


def department_count():
    if len(employees) == 0:
        print("No employee records found.")
    else:
        departments = []

        for emp in employees:
            if emp[2] not in departments:
                departments.append(emp[2])

        for dept in departments:
            count = 0
            for emp in employees:
                if emp[2] == dept:
                    count += 1
            print(dept, ":", count)


while True:
    print("\n========== Employee Project Management System ==========")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Assign a New Project")
    print("4. Remove a Project")
    print("5. Search Employee")
    print("6. Display Employees Working on Multiple Projects")
    print("7. Display Department-wise Employee Count")
    print("8. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_employee()

    elif choice == 2:
        view_employees()

    elif choice == 3:
        assign_project()

    elif choice == 4:
        remove_project()

    elif choice == 5:
        search_employee()

    elif choice == 6:
        multiple_projects()

    elif choice == 7:
        department_count()

    elif choice == 8:
        print("Thank you for using Employee Project Management System.")
        break

    else:
        print("Invalid Choice. Please try again.")