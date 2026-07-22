import logging

from student_university_module import add_university
from view_all_universities import view_all_universities
from add_student_to_university import add_student_to_university


logging.basicConfig(
    filename="university.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)



while True:

    print("\n================================================================")
    print("1) Add University")
    print("2) View All Universities")
    print("3) Add Student to University")
    print("4) Exit")


    try:
        choice = int(input("Enter Your Choice: "))

    except Exception as e:
        print("Invalid choice.")
        logging.error(str(e))
        continue



    if choice == 1:

        try:

            u_id = int(input("Enter University ID: "))

            student_id = int(input("Enter Student ID: "))

            student_name = input("Enter Student Name: ")

            age = int(input("Enter Student Age: "))

            branch = input("Enter Student Branch: ")


            student_list = {
                student_id: [
                    student_name,
                    age,
                    branch
                ]
            }


            add_university(
                u_id,
                student_list
            )


        except Exception as e:

            print("Please enter valid values.")
            logging.error(str(e))



    elif choice == 2:

        view_all_universities()



    elif choice == 3:


        try:

            u_id = int(input("Enter University ID: "))

            student_id = int(input("Enter Student ID: "))

            student_name = input("Enter Student Name: ")

            age = int(input("Enter Student Age: "))

            branch = input("Enter Student Branch: ")


            add_student_to_university(
                u_id,
                student_id,
                student_name,
                age,
                branch
            )


        except Exception as e:

            print("Please enter valid values.")
            logging.error(str(e))



    elif choice == 4:

        print("Thank You!")
        logging.critical("Program terminated.")
        break



    else:

        print("Invalid Choice.")
        logging.error("Invalid choice selected.")