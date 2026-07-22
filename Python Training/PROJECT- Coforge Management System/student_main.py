from add_university import add_university

from add_student import (
    add_student_to_university
)

from student_view_all_universities import (
    view_all_universities
)

from export_report import (
    export_university_report
)

from logger_config import (
    application_logger,
    exception_logger
)


def display_menu():
    print("\n" + "=" * 60)
    print("UNIVERSITY MANAGEMENT SYSTEM")
    print("=" * 60)

    print("1) Add University")
    print("2) View All Universities")
    print("3) Add Student to University")
    print("4) Export University Report")
    print("5) Exit")


def main():
    application_logger.info(
        "University Management System started."
    )

    while True:
        try:
            display_menu()

            choice = int(
                input("Enter Your Choice: ")
            )

            if choice == 1:
                add_university()

            elif choice == 2:
                view_all_universities()

            elif choice == 3:
                add_student_to_university()

            elif choice == 4:
                export_university_report()

            elif choice == 5:
                print(
                    "Application closed successfully."
                )

                application_logger.info(
                    "University Management System closed."
                )

                break

            else:
                print(
                    "Please enter a choice between 1 and 5."
                )

                application_logger.warning(
                    "Invalid menu choice entered: %s",
                    choice
                )

        except ValueError as error:
            print(
                "Please enter only a numeric menu choice."
            )

            exception_logger.exception(
                "Invalid menu input: %s",
                error
            )

        except KeyboardInterrupt:
            print(
                "\nApplication stopped by the user."
            )

            application_logger.warning(
                "Application stopped using keyboard interrupt."
            )

            break

        except Exception as error:
            print(
                "Unexpected application error:",
                error
            )

            exception_logger.exception(
                "Unexpected main application error: %s",
                error
            )


if __name__ == "__main__":
    main()