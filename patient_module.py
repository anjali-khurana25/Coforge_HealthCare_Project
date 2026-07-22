from register_patient import register_patient
from view_patient import view_all_patients
from search_patient import search_patient
from update_patient import update_patient
from delete_patient import delete_patient


def patient_menu():

    while True:

        print("\n===== PATIENT MODULE =====")
        print("1. Register Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Back")

        choice = int(input("Enter Choice : "))

        if choice == 1:
            register_patient()

        elif choice == 2:
            view_all_patients()

        elif choice == 3:
            search_patient()

        elif choice == 4:
            update_patient()

        elif choice == 5:
            delete_patient()

        elif choice == 6:
            break

        else:
            print("Invalid Choice")