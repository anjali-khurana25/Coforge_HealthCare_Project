from patient_report_module import generate_patient_reports
from doctor_report_module import generate_doctor_reports
from appointment_report_module import generate_appointment_reports
from billing_report_module import generate_billing_reports


def healthcare_reports_menu():

    while True:

        print("\n========== HEALTHCARE REPORTS ==========")
        print("1. Patient Reports")
        print("2. Doctor Reports")
        print("3. Appointment Reports")
        print("4. Billing Reports")
        print("5. Back")

        choice = input("Enter your choice : ")

        if choice == "1":
            generate_patient_reports()

        elif choice == "2":
            generate_doctor_reports()

        elif choice == "3":
            generate_appointment_reports()

        elif choice == "4":
            generate_billing_reports()

        elif choice == "5":
            break

        else:
            print("Invalid Choice")