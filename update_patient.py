import mysql.connector

from db_connection import (
    get_database_connection
)

from logger_module import (
    application_logger,
    exception_logger
)


def update_patient():

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

        print("\nEnter New Details\n")

        patient_name = input(
            "Enter Patient Name : "
        )

        age = int(
            input("Enter Age : ")
        )

        gender = input(
            "Enter Gender : "
        )

        contact_number = input(
            "Enter Contact Number : "
        )

        city = input(
            "Enter City : "
        )

        blood_group = input(
            "Enter Blood Group : "
        )

        disease = input(
            "Enter Disease : "
        )

        cursor.execute(
            """
            UPDATE patient

            SET

            patient_name=%s,
            age=%s,
            gender=%s,
            contact_number=%s,
            city=%s,
            blood_group=%s,
            disease=%s

            WHERE patient_id=%s
            """,

            (
                patient_name,
                age,
                gender,
                contact_number,
                city,
                blood_group,
                disease,
                patient_id
            )
        )

        connection.commit()

        print("Patient Updated Successfully.")

        application_logger.info(
            f"Patient {patient_id} Updated Successfully."
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