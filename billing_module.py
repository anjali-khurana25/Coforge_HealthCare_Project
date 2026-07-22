from generate_bill import generate_bill
from view_all_bills import view_all_bills
from search_patient_bills import search_patient_bills
from update_payment_status import update_payment_status

from logger_module import (
    application_logger,
    exception_logger
)


def billing_menu():

    while True:

        print("\n" + "=" * 50)
        print("         BILLING MODULE")
        print("=" * 50)

        print("1. Generate Bill")
        print("2. View All Bills")
        print("3. Search Patient Bills")
        print("4. Update Payment Status")
        print("5. Back / Exit")

        choice = input("\nEnter your choice: ").strip()

        try:

            if choice == "1":
                generate_bill()

            elif choice == "2":
                view_all_bills()

            elif choice == "3":
                search_patient_bills()

            elif choice == "4":
                update_payment_status()

            elif choice == "5":
                print("Returning...")
                break

            else:
                print("Invalid choice. Please try again.")

        except Exception as error:

            print("Error:", error)
            exception_logger.exception(error)


if __name__ == "__main__":
    billing_menu()