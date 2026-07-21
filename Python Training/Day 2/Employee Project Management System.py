# Employee Project Management System (Tuple + List)

employee = (
    101,
    "Gaurav Joshi",
    "AI Developer",
    ["Payroll System", "HR Portal"]
)


def view_employee():
    print("\nEmployee Details")
    print("Employee ID :", employee[0])
    print("Employee Name :", employee[1])
    print("Department :", employee[2])

    print("Assigned Projects :")
    if len(employee[3]) == 0:
        print("No Projects Assigned.")
    else:
        for i in range(len(employee[3])):
            print(i + 1, "-", employee[3][i])


def add_project():
    project = input("Enter Project Name: ")
    employee[3].append(project)
    print("Project added successfully.")


def remove_project():
    project = input("Enter Project Name: ")

    if project in employee[3]:
        employee[3].remove(project)
        print("Project removed successfully.")
    else:
        print("Project not found.")


def search_project():
    project = input("Enter Project Name: ")

    if project in employee[3]:
        print("Project Assigned.")
    else:
        print("Project Not Assigned.")


def total_projects():
    print("Total Projects :", len(employee[3]))


def display_projects():
    if len(employee[3]) == 0:
        print("No Projects Assigned.")
    else:
        print("\nProjects in Alphabetical Order")
        for project in sorted(employee[3]):
            print(project)


while True:
    print("\n========== Employee Project Management System ==========")
    print("1. View Employee Details")
    print("2. Add New Project")
    print("3. Remove Project")
    print("4. Search Project")
    print("5. Display Total Number of Projects")
    print("6. Display Projects Alphabetically")
    print("7. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        view_employee()

    elif choice == 2:
        add_project()

    elif choice == 3:
        remove_project()

    elif choice == 4:
        search_project()

    elif choice == 5:
        total_projects()

    elif choice == 6:
        display_projects()

    elif choice == 7:
        print("Thank you for using Employee Project Management System.")
        break

    else:
        print("Invalid Choice. Please try again.")