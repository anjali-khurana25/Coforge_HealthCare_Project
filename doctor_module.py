from add_doctor import add_doctor
from view_all_doctors import view_all_doctors
from search_doctor import search_doctor


def doctor_menu():

    while True:

        print("\n========== DOCTOR MODULE ==========")
        print("1. Add Doctor")
        print("2. View All Doctors")
        print("3. Search Doctor")
        print("4. Back")

        choice = input("Enter your choice : ")

        if choice == "1":

            add_doctor()

        elif choice == "2":

            view_all_doctors()

        elif choice == "3":

            search_doctor()

        elif choice == "4":

            break

        else:

            print("Invalid Choice")