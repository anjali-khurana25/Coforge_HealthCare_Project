import mysql.connector

from db_connection import connection, cursor
from logger_module import logger


def generate_doctor_reports():

    try:

        while True:

            print("\n" + "=" * 50)
            print("           DOCTOR REPORTS")
            print("=" * 50)
            print("1. Total Doctors")
            print("2. Doctors by Department")
            print("3. Available Doctors")
            print("4. Unavailable Doctors")
            print("5. Doctors On Leave")
            print("6. Highest Consultation Fee")
            print("7. Lowest Consultation Fee")
            print("8. Back")
            print("=" * 50)

            choice = input("Enter your choice : ")

            if choice == "1":

                cursor.execute("""
                    SELECT COUNT(*)
                    FROM doctors
                """)

                total = cursor.fetchone()

                print(f"\nTotal Doctors : {total[0]}")

            elif choice == "2":

                cursor.execute("""
                    SELECT department,
                           COUNT(*)
                    FROM doctors
                    GROUP BY department
                """)

                records = cursor.fetchall()

                print("\nDoctors by Department\n")

                for record in records:

                    print(f"{record[0]} : {record[1]}")

            elif choice == "3":

                cursor.execute("""
                    SELECT doctor_id,
                           doctor_name,
                           department,
                           consultation_fee
                    FROM doctors
                    WHERE status='Available'
                """)

                records = cursor.fetchall()

                if len(records) == 0:

                    print("\nNo available doctors found.")

                else:

                    print("\nAvailable Doctors\n")

                    for record in records:

                        print(
                            f"ID : {record[0]} | "
                            f"Name : {record[1]} | "
                            f"Department : {record[2]} | "
                            f"Fee : {record[3]}"
                        )

            elif choice == "4":

                cursor.execute("""
                    SELECT doctor_id,
                           doctor_name,
                           department,
                           consultation_fee
                    FROM doctors
                    WHERE status='Unavailable'
                """)

                records = cursor.fetchall()

                if len(records) == 0:

                    print("\nNo unavailable doctors found.")

                else:

                    print("\nUnavailable Doctors\n")

                    for record in records:

                        print(
                            f"ID : {record[0]} | "
                            f"Name : {record[1]} | "
                            f"Department : {record[2]} | "
                            f"Fee : {record[3]}"
                        )

            elif choice == "5":

                cursor.execute("""
                    SELECT doctor_id,
                           doctor_name,
                           department,
                           consultation_fee
                    FROM doctors
                    WHERE status='On Leave'
                """)

                records = cursor.fetchall()

                if len(records) == 0:

                    print("\nNo doctors are on leave.")

                else:

                    print("\nDoctors On Leave\n")

                    for record in records:

                        print(
                            f"ID : {record[0]} | "
                            f"Name : {record[1]} | "
                            f"Department : {record[2]} | "
                            f"Fee : {record[3]}"
                        )

            elif choice == "6":

                cursor.execute("""
                    SELECT doctor_id,
                           doctor_name,
                           department,
                           consultation_fee
                    FROM doctors
                    ORDER BY consultation_fee DESC
                    LIMIT 1
                """)

                record = cursor.fetchone()

                if record:

                    print("\nDoctor with Highest Consultation Fee\n")

                    print(f"Doctor ID          : {record[0]}")
                    print(f"Doctor Name        : {record[1]}")
                    print(f"Department         : {record[2]}")
                    print(f"Consultation Fee  : {record[3]}")

                else:

                    print("\nNo doctor records found.")

            elif choice == "7":

                cursor.execute("""
                    SELECT doctor_id,
                           doctor_name,
                           department,
                           consultation_fee
                    FROM doctors
                    ORDER BY consultation_fee ASC
                    LIMIT 1
                """)

                record = cursor.fetchone()

                if record:

                    print("\nDoctor with Lowest Consultation Fee\n")

                    print(f"Doctor ID          : {record[0]}")
                    print(f"Doctor Name        : {record[1]}")
                    print(f"Department         : {record[2]}")
                    print(f"Consultation Fee  : {record[3]}")

                else:

                    print("\nNo doctor records found.")

            elif choice == "8":

                break

            else:

                print("\nInvalid Choice.")

        logger.info("Doctor reports generated successfully.")

    except mysql.connector.Error as error:

        logger.exception(error)
        print(f"\nDatabase Error : {error}")

    except Exception as error:

        logger.exception(error)
        print(f"\nError : {error}")

    finally:

        logger.info("Exited Doctor Report Module.")