import mysql.connector

from db_connection import (
    get_database_connection
)

from logger_module import (
    application_logger,
    exception_logger
)


def register_patient():

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

        if cursor.fetchone():

            print("Patient ID already exists.")

            application_logger.warning(
                f"Duplicate Patient ID : {patient_id}"
            )

            return

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
            INSERT INTO patient
            (
                patient_id,
                patient_name,
                age,
                gender,
                contact_number,
                city,
                blood_group,
                disease
            )

            VALUES
            (
                %s,%s,%s,%s,%s,%s,%s,%s
            )
            """,

            (
                patient_id,
                patient_name,
                age,
                gender,
                contact_number,
                city,
                blood_group,
                disease
            )

        )

        connection.commit()

        print(
            "Patient Registered Successfully."
        )

        application_logger.info(
            f"Patient {patient_id} Registered Successfully."
        )

    except ValueError:

        print(
            "Invalid Input."
        )

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