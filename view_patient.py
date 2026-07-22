import mysql.connector

from db_connection import (
    get_database_connection
)

from logger_module import (
    application_logger,
    exception_logger
)


def view_all_patients():

    connection = None
    cursor = None

    try:

        connection = get_database_connection()

        cursor = connection.cursor(
            dictionary=True
        )

        cursor.execute(
            """
            SELECT *
            FROM patient
            """
        )

        patients = cursor.fetchall()

        if not patients:

            print("No Patient Records Found.")

            application_logger.warning(
                "Attempted to view patients, but no records found."
            )

            return

        print("\n========== Patient Records ==========\n")

        for patient in patients:

            print(f"Patient ID      : {patient['patient_id']}")
            print(f"Patient Name    : {patient['patient_name']}")
            print(f"Age             : {patient['age']}")
            print(f"Gender          : {patient['gender']}")
            print(f"Contact Number  : {patient['contact_number']}")
            print(f"City            : {patient['city']}")
            print(f"Blood Group     : {patient['blood_group']}")
            print(f"Disease         : {patient['disease']}")
            print("-" * 50)

        application_logger.info(
            "Viewed all patient records successfully."
        )

    except mysql.connector.Error as error:

        print(error)

        exception_logger.exception(error)

    except Exception as error:

        print(error)

        exception_logger.exception(error)

    finally:

        if cursor:

            cursor.close()

        if connection:

            connection.close()