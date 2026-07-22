import mysql.connector

from db_connection import connection, cursor
from logger_module import logger


def generate_patient_reports():

    try:

        while True:

            print("\n" + "=" * 50)
            print("          PATIENT REPORTS")
            print("=" * 50)
            print("1. Total Patients")
            print("2. Patients by Gender")
            print("3. Patients by Blood Group")
            print("4. Patients by City")
            print("5. Patients by Disease")
            print("6. Patients Above 60 Years")
            print("7. Youngest Patient")
            print("8. Oldest Patient")
            print("9. Back")
            print("=" * 50)

            choice = input("Enter your choice : ")

            if choice == "1":

                cursor.execute("""
                    SELECT COUNT(*)
                    FROM patients
                """)

                total = cursor.fetchone()

                print(f"\nTotal Patients : {total[0]}")

            elif choice == "2":

                cursor.execute("""
                    SELECT gender,
                           COUNT(*)
                    FROM patients
                    GROUP BY gender
                """)

                records = cursor.fetchall()

                print("\nPatients by Gender")

                for record in records:
                    print(f"{record[0]} : {record[1]}")

            elif choice == "3":

                cursor.execute("""
                    SELECT blood_group,
                           COUNT(*)
                    FROM patients
                    GROUP BY blood_group
                """)

                records = cursor.fetchall()

                print("\nPatients by Blood Group")

                for record in records:
                    print(f"{record[0]} : {record[1]}")

            elif choice == "4":

                cursor.execute("""
                    SELECT city,
                           COUNT(*)
                    FROM patients
                    GROUP BY city
                """)

                records = cursor.fetchall()

                print("\nPatients by City")

                for record in records:
                    print(f"{record[0]} : {record[1]}")

            elif choice == "5":

                cursor.execute("""
                    SELECT disease,
                           COUNT(*)
                    FROM patients
                    GROUP BY disease
                """)

                records = cursor.fetchall()

                print("\nPatients by Disease")

                for record in records:
                    print(f"{record[0]} : {record[1]}")

            elif choice == "6":

                cursor.execute("""
                    SELECT patient_id,
                           patient_name,
                           age,
                           gender
                    FROM patients
                    WHERE age > 60
                """)

                records = cursor.fetchall()

                if len(records) == 0:

                    print("\nNo patients found.")

                else:

                    print("\nPatients Above 60 Years\n")

                    for record in records:

                        print(
                            f"ID : {record[0]} | "
                            f"Name : {record[1]} | "
                            f"Age : {record[2]} | "
                            f"Gender : {record[3]}"
                        )

            elif choice == "7":

                cursor.execute("""
                    SELECT patient_id,
                           patient_name,
                           age
                    FROM patients
                    ORDER BY age ASC
                    LIMIT 1
                """)

                record = cursor.fetchone()

                if record:

                    print("\nYoungest Patient")
                    print(f"Patient ID : {record[0]}")
                    print(f"Name       : {record[1]}")
                    print(f"Age        : {record[2]}")

                else:

                    print("\nNo patient records found.")

            elif choice == "8":

                cursor.execute("""
                    SELECT patient_id,
                           patient_name,
                           age
                    FROM patients
                    ORDER BY age DESC
                    LIMIT 1
                """)

                record = cursor.fetchone()

                if record:

                    print("\nOldest Patient")
                    print(f"Patient ID : {record[0]}")
                    print(f"Name       : {record[1]}")
                    print(f"Age        : {record[2]}")

                else:

                    print("\nNo patient records found.")

            elif choice == "9":

                break

            else:

                print("\nInvalid Choice.")

        logger.info("Patient reports generated successfully.")

    except mysql.connector.Error as error:

        logger.exception(error)
        print(f"\nDatabase Error : {error}")

    except Exception as error:

        logger.exception(error)
        print(f"\nError : {error}")

    finally:

        logger.info("Exited Patient Report Module.")