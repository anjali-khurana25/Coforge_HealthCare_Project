import logging
import student_university_module
from view_all_universities import view_all_universities

logging.basicConfig(
    filename="university.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

def add_student_to_university(u_id, student_id, student_name, age, branch):
    try:
        if u_id in student_university_module.universities:

            if student_id in student_university_module.universities[u_id]:
                print(f"Student with ID {student_id} already exists.")
                logging.warning(f"Student with ID {student_id} already exists.")
            else:
                student_university_module.universities[u_id][student_id] = [
                    student_name,
                    age,
                    branch
                ]
                print("Student added successfully.")
                logging.info("Student added successfully.")

        else:
            print("University not found.")
            logging.warning("University not found.")

    except Exception as e:
        print(f"Error while adding student: {e}")
        logging.error(str(e))

    else:
        logging.info("Add Student function executed successfully.")


while True:

    print("\n==============================")
    print("1. Add University")
    print("2. View All Universities")
    print("3. Add Student")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        u_id = int(input("Enter University ID: "))
        student_id = int(input("Enter Student ID: "))
        student_name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        branch = input("Enter Branch: ")

        student_list = {
            student_id: [student_name, age, branch]
        }

        student_university_module.add_university(u_id, student_list)

    elif choice == 2:

        view_all_universities()

    elif choice == 3:

        u_id = int(input("Enter University ID: "))
        student_id = int(input("Enter Student ID: "))
        student_name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        branch = input("Enter Branch: ")

        add_student_to_university(
            u_id,
            student_id,
            student_name,
            age,
            branch
        )

    elif choice == 4:
        print("Thank You")
        break

    else:
        print("Invalid Choice")