import mysql.connector

from db_connection import connection, cursor
from logger_module import logger


def generate_appointment_reports():

    try:

        while True:

            print("\n" + "=" * 50)
            print("        APPOINTMENT REPORTS")
            print("=" * 50)
            print("1. Total Appointments")
            print("2. Scheduled Appointments")
            print("3. Completed Appointments")
            print("4. Cancelled Appointments")
            print("5. Doctor-wise Appointments")
            print("6. Department-wise Appointments")
            print("7. Doctor with Highest Appointments")
            print("8. Patient with Highest Appointments")
            print("9. Back")
            print("=" * 50)

            choice = input("Enter your choice : ")

            if choice == "1":

                cursor.execute("""
                    SELECT COUNT(*)
                    FROM appointments
                """)

                total = cursor.fetchone()

                print(f"\nTotal Appointments : {total[0]}")

            elif choice == "2":

                cursor.execute("""
                    SELECT appointment_id,
                           patient_id,
                           doctor_id,
                           appointment_date,
                           status
                    FROM appointments
                    WHERE status='Scheduled'
                """)

                records = cursor.fetchall()

                if len(records) == 0:

                    print("\nNo scheduled appointments found.")

                else:

                    print("\nScheduled Appointments\n")

                    for record in records:

                        print(
                            f"Appointment ID : {record[0]} | "
                            f"Patient ID : {record[1]} | "
                            f"Doctor ID : {record[2]} | "
                            f"Date : {record[3]} | "
                            f"Status : {record[4]}"
                        )

            elif choice == "3":

                cursor.execute("""
                    SELECT appointment_id,
                           patient_id,
                           doctor_id,
                           appointment_date,
                           status
                    FROM appointments
                    WHERE status='Completed'
                """)

                records = cursor.fetchall()

                if len(records) == 0:

                    print("\nNo completed appointments found.")

                else:

                    print("\nCompleted Appointments\n")

                    for record in records:

                        print(
                            f"Appointment ID : {record[0]} | "
                            f"Patient ID : {record[1]} | "
                            f"Doctor ID : {record[2]} | "
                            f"Date : {record[3]} | "
                            f"Status : {record[4]}"
                        )

            elif choice == "4":

                cursor.execute("""
                    SELECT appointment_id,
                           patient_id,
                           doctor_id,
                           appointment_date,
                           status
                    FROM appointments
                    WHERE status='Cancelled'
                """)

                records = cursor.fetchall()

                if len(records) == 0:

                    print("\nNo cancelled appointments found.")

                else:

                    print("\nCancelled Appointments\n")

                    for record in records:

                        print(
                            f"Appointment ID : {record[0]} | "
                            f"Patient ID : {record[1]} | "
                            f"Doctor ID : {record[2]} | "
                            f"Date : {record[3]} | "
                            f"Status : {record[4]}"
                        )

            elif choice == "5":

                cursor.execute("""
                    SELECT doctor_id,
                           COUNT(*)
                    FROM appointments
                    GROUP BY doctor_id
                    ORDER BY COUNT(*) DESC
                """)

                records = cursor.fetchall()

                print("\nDoctor-wise Appointments\n")

                for record in records:

                    print(f"Doctor ID : {record[0]}  -->  {record[1]} Appointments")

            elif choice == "6":

                cursor.execute("""
                    SELECT d.department,
                           COUNT(*)
                    FROM appointments a
                    INNER JOIN doctors d
                    ON a.doctor_id = d.doctor_id
                    GROUP BY d.department
                    ORDER BY COUNT(*) DESC
                """)

                records = cursor.fetchall()

                print("\nDepartment-wise Appointments\n")

                for record in records:

                    print(f"{record[0]} : {record[1]}")

            elif choice == "7":

                cursor.execute("""
                    SELECT doctor_id,
                           COUNT(*)
                    FROM appointments
                    GROUP BY doctor_id
                    ORDER BY COUNT(*) DESC
                    LIMIT 1
                """)

                record = cursor.fetchone()

                if record:

                    print("\nDoctor with Highest Appointments\n")

                    print(f"Doctor ID : {record[0]}")
                    print(f"Appointments : {record[1]}")

                else:

                    print("\nNo appointment records found.")

            elif choice == "8":

                cursor.execute("""
                    SELECT patient_id,
                           COUNT(*)
                    FROM appointments
                    GROUP BY patient_id
                    ORDER BY COUNT(*) DESC
                    LIMIT 1
                """)

                record = cursor.fetchone()

                if record:

                    print("\nPatient with Highest Appointments\n")

                    print(f"Patient ID : {record[0]}")
                    print(f"Appointments : {record[1]}")

                else:

                    print("\nNo appointment records found.")

            elif choice == "9":

                break

            else:

                print("\nInvalid Choice.")

        logger.info("Appointment reports generated successfully.")

    except mysql.connector.Error as error:

        logger.exception(error)
        print(f"\nDatabase Error : {error}")

    except Exception as error:

        logger.exception(error)
        print(f"\nError : {error}")

    finally:

        logger.info("Exited Appointment Report Module.")