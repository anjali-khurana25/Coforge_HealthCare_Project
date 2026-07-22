import mysql.connector

from db_connection import (
    connection,
    cursor
)

from logger_module import (
    application_logger,
    exception_logger
)


def search_doctor():

    try:

        while True:

            print("\n" + "=" * 50)
            print("            SEARCH DOCTOR")
            print("=" * 50)
            print("1. Search by Doctor ID")
            print("2. Search by Doctor Name")
            print("3. Search by Department")
            print("4. Search by Availability Status")
            print("5. Back")
            print("=" * 50)

            choice = input("Enter your choice : ").strip()

            if choice == "1":

                doctor_id = input(
                    "Enter Doctor ID : "
                ).strip().upper()

                query = """
                SELECT
                    doctor_id,
                    doctor_name,
                    department,
                    consultation_fee,
                    availability_status
                FROM doctors
                WHERE doctor_id=%s
                """

                cursor.execute(
                    query,
                    (doctor_id,)
                )

                records = cursor.fetchall()

            elif choice == "2":

                doctor_name = input(
                    "Enter Doctor Name : "
                ).strip()

                query = """
                SELECT
                    doctor_id,
                    doctor_name,
                    department,
                    consultation_fee,
                    availability_status
                FROM doctors
                WHERE doctor_name LIKE %s
                """

                cursor.execute(
                    query,
                    ("%" + doctor_name + "%",)
                )

                records = cursor.fetchall()

            elif choice == "3":

                department = input(
                    "Enter Department : "
                ).strip()

                query = """
                SELECT
                    doctor_id,
                    doctor_name,
                    department,
                    consultation_fee,
                    availability_status
                FROM doctors
                WHERE department LIKE %s
                """

                cursor.execute(
                    query,
                    ("%" + department + "%",)
                )

                records = cursor.fetchall()

            elif choice == "4":

                status = input(
                    "Enter Availability Status (Available/Unavailable/On Leave) : "
                ).title()

                query = """
                SELECT
                    doctor_id,
                    doctor_name,
                    department,
                    consultation_fee,
                    availability_status
                FROM doctors
                WHERE availability_status=%s
                """

                cursor.execute(
                    query,
                    (status,)
                )

                records = cursor.fetchall()

            elif choice == "5":

                break

            else:

                print("\nInvalid Choice.")

                continue

            if len(records) == 0:

                print("\nNo Doctor Found.")

                application_logger.info(
                    "Doctor search returned no records."
                )

            else:

                print("\n" + "=" * 70)
                print("                  SEARCH RESULT")
                print("=" * 70)

                for record in records:

                    print(f"Doctor ID           : {record[0]}")
                    print(f"Doctor Name         : {record[1]}")
                    print(f"Department          : {record[2]}")
                    print(f"Consultation Fee    : ₹{record[3]}")
                    print(f"Availability Status : {record[4]}")
                    print("-" * 70)

                application_logger.info(
                    "Doctor searched successfully."
                )

    except mysql.connector.Error as error:

        exception_logger.exception(error)

        print(
            f"\nDatabase Error : {error}"
        )

    except Exception as error:

        exception_logger.exception(error)

        print(
            f"\nError : {error}"
        )

    finally:

        application_logger.info(
            "Exited Search Doctor Module."
        )