import mysql.connector

from db_connection import (
    get_database_connection
)

from logger_module import (
    application_logger,
    exception_logger
)


def delete_patient():

    connection = None
    cursor = None

    try:

        connection = get_database_connection()

        cursor = connection.cursor()

        patient_id = int(
            input("Enter Patient ID : ")
        )

        cursor.execute(
            """
            SELECT *
            FROM patient
            WHERE patient_id=%s
            """,
            (patient_id,)
        )

        patient = cursor.fetchone()

        if not patient:

            print("Patient Not Found.")

            application_logger.warning(
                f"Patient ID {patient_id} does not exist."
            )

            return

        confirmation = input(
            "Are you sure you want to delete this patient? (Y/N) : "
        )

        if confirmation.upper() != "Y":

            print("Patient Deletion Cancelled.")

            application_logger.info(
                f"Deletion Cancelled for Patient ID {patient_id}"
            )

            return

        cursor.execute(
            """
            DELETE FROM patient
            WHERE patient_id=%s
            """,
            (patient_id,)
        )

        connection.commit()

        print("Patient Deleted Successfully.")

        application_logger.info(
            f"Patient {patient_id} Deleted Successfully."
        )

    except ValueError:

        print("Invalid Input.")

        exception_logger.exception(
            "ValueError Occurred."
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