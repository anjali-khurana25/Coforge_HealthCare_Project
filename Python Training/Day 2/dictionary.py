colleges = [
    {
        "College": "MRU",
        "College_ID": 1,
        "Students": [
            {
                "Name": "Samriddhi",
                "Age": 21,
                "Branch": "CSE",
                "Student_ID": 101
            }
        ]
    },
    {
        "College": "MRU",
        "College_ID": 2,
        "Students": [
            {
                "Name": "Lavnaya",
                "Age": 22,
                "Branch": "IT",
                "Student_ID": 201
            }
        ]
    }
]

while True:
    print("\n-------------------------------------")
    print("      Student Management System")
    print("-------------------------------------")
    print("1. Add Student Details")
    print("2. View Student Details")
    print("3. Update Student Details")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":

        college_id = int(input("Enter College ID (1-MRIIRS, 2-MRU): "))

        found = False

        for college in colleges:
            if college["College_ID"] == college_id:

                name = input("Enter Student Name: ")
                age = int(input("Enter Age: "))
                branch = input("Enter Branch: ")
                student_id = int(input("Enter Student ID: "))

                duplicate = False

                for c in colleges:
                    for student in c["Students"]:
                        if student["Student_ID"] == student_id:
                            duplicate = True
                            break
                    if duplicate:
                        break

                if duplicate:
                    print("Student ID is already assigned.")
                else:
                    student = {
                        "Name": name,
                        "Age": age,
                        "Branch": branch,
                        "Student_ID": student_id
                    }

                    college["Students"].append(student)
                    print("Student added successfully.")

                found = True
                break

        if found == False:
            print("College not found.")

    elif choice == "2":

        for college in colleges:

            print("\n===================================")
            print("College Name :", college["College"])
            print("College ID   :", college["College_ID"])
            print("===================================")

            if len(college["Students"]) == 0:
                print("No Students Available.")
            else:
                for student in college["Students"]:
                    print("Student ID :", student["Student_ID"])
                    print("Name       :", student["Name"])
                    print("Age        :", student["Age"])
                    print("Branch     :", student["Branch"])
                    print("-----------------------------------")

    elif choice == "3":

        student_id = int(input("Enter Student ID to Update: "))

        found = False

        for college in colleges:
            for student in college["Students"]:
                if student["Student_ID"] == student_id:

                    student["Name"] = input("Enter New Name: ")
                    student["Age"] = int(input("Enter New Age: "))
                    student["Branch"] = input("Enter New Branch: ")

                    print("Student details updated successfully.")
                    found = True
                    break

            if found:
                break

        if found == False:
            print("Student not found.")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")