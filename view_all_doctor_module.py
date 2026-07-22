import mysql.connector

from db_connection import (
    connection,
    cursor
)

from logger_module import (
    application_logger,
    exception_logger
)


def view_all_doctors():

    try:

        query = """
        SELECT
            doctor_id,
            doctor_name,
            department,
            consultation_fee,
            availability_status
        FROM doctors
        """

        cursor.execute(query)

        records = cursor.fetchall()

        if len(records) == 0:

            print("\nNo Doctors Found.")

            application_logger.info(
                "No doctor records found."
            )

        else:

            print("\n" + "=" * 70)
            print("                     ALL DOCTORS")
            print("=" * 70)

            for record in records:

                print(f"Doctor ID           : {record[0]}")
                print(f"Doctor Name         : {record[1]}")
                print(f"Department          : {record[2]}")
                print(f"Consultation Fee    : ₹{record[3]}")
                print(f"Availability Status : {record[4]}")

                print("-" * 70)

            application_logger.info(
                "Viewed all doctors successfully."
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
            "Exited View All Doctors Module."
        )