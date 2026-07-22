import mysql.connector

from db_connection import connection, cursor
from logger_module import logger


def generate_billing_reports():

    try:

        while True:

            print("\n" + "=" * 50)
            print("           BILLING REPORTS")
            print("=" * 50)
            print("1. Total Bills")
            print("2. Total Revenue")
            print("3. Paid Bills")
            print("4. Pending Bills")
            print("5. Highest Bill")
            print("6. Lowest Bill")
            print("7. Average Bill Amount")
            print("8. Patient with Highest Total Bill")
            print("9. Back")
            print("=" * 50)

            choice = input("Enter your choice : ")

            if choice == "1":

                cursor.execute("""
                    SELECT COUNT(*)
                    FROM bills
                """)

                total = cursor.fetchone()

                print(f"\nTotal Bills : {total[0]}")

            elif choice == "2":

                cursor.execute("""
                    SELECT SUM(total_amount)
                    FROM bills
                """)

                revenue = cursor.fetchone()

                print(f"\nTotal Revenue : ₹ {revenue[0] if revenue[0] else 0}")

            elif choice == "3":

                cursor.execute("""
                    SELECT bill_id,
                           patient_id,
                           total_amount,
                           payment_status
                    FROM bills
                    WHERE payment_status='Paid'
                """)

                records = cursor.fetchall()

                if len(records) == 0:

                    print("\nNo paid bills found.")

                else:

                    print("\nPaid Bills\n")

                    for record in records:

                        print(
                            f"Bill ID : {record[0]} | "
                            f"Patient ID : {record[1]} | "
                            f"Amount : ₹{record[2]} | "
                            f"Status : {record[3]}"
                        )

            elif choice == "4":

                cursor.execute("""
                    SELECT bill_id,
                           patient_id,
                           total_amount,
                           payment_status
                    FROM bills
                    WHERE payment_status='Pending'
                """)

                records = cursor.fetchall()

                if len(records) == 0:

                    print("\nNo pending bills found.")

                else:

                    print("\nPending Bills\n")

                    for record in records:

                        print(
                            f"Bill ID : {record[0]} | "
                            f"Patient ID : {record[1]} | "
                            f"Amount : ₹{record[2]} | "
                            f"Status : {record[3]}"
                        )

            elif choice == "5":

                cursor.execute("""
                    SELECT bill_id,
                           patient_id,
                           total_amount
                    FROM bills
                    ORDER BY total_amount DESC
                    LIMIT 1
                """)

                record = cursor.fetchone()

                if record:

                    print("\nHighest Bill\n")

                    print(f"Bill ID      : {record[0]}")
                    print(f"Patient ID   : {record[1]}")
                    print(f"Amount       : ₹{record[2]}")

                else:

                    print("\nNo billing records found.")

            elif choice == "6":

                cursor.execute("""
                    SELECT bill_id,
                           patient_id,
                           total_amount
                    FROM bills
                    ORDER BY total_amount ASC
                    LIMIT 1
                """)

                record = cursor.fetchone()

                if record:

                    print("\nLowest Bill\n")

                    print(f"Bill ID      : {record[0]}")
                    print(f"Patient ID   : {record[1]}")
                    print(f"Amount       : ₹{record[2]}")

                else:

                    print("\nNo billing records found.")

            elif choice == "7":

                cursor.execute("""
                    SELECT AVG(total_amount)
                    FROM bills
                """)

                average = cursor.fetchone()

                print(f"\nAverage Bill Amount : ₹ {round(average[0], 2) if average[0] else 0}")

            elif choice == "8":

                cursor.execute("""
                    SELECT patient_id,
                           SUM(total_amount) AS total_bill
                    FROM bills
                    GROUP BY patient_id
                    ORDER BY total_bill DESC
                    LIMIT 1
                """)

                record = cursor.fetchone()

                if record:

                    print("\nPatient with Highest Total Bill\n")

                    print(f"Patient ID : {record[0]}")
                    print(f"Total Bill : ₹{record[1]}")

                else:

                    print("\nNo billing records found.")

            elif choice == "9":

                break

            else:

                print("\nInvalid Choice.")

        logger.info("Billing reports generated successfully.")

    except mysql.connector.Error as error:

        logger.exception(error)
        print(f"\nDatabase Error : {error}")

    except Exception as error:

        logger.exception(error)
        print(f"\nError : {error}")

    finally:

        logger.info("Exited Billing Report Module.")