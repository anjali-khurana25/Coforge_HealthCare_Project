import mysql.connector

from db_connection import (
    connection,
    cursor
)

from logger_module import (
    application_logger,
    exception_logger
)


def add_doctor():

    try:

        doctor_id = input(
            "Enter Doctor ID : "
        ).strip().upper()

        doctor_name = input(
            "Enter Doctor Name : "
        ).strip()

        department = input(
            "Enter Department : "
        ).strip()

        consultation_fee = float(
            input(
                "Enter Consultation Fee : "
            )
        )

        availability_status = input(
            "Enter Availability Status (Available/Unavailable/On Leave) : "
        ).title()

      

        if doctor_id == "":

            print(
                "Doctor ID cannot be empty."
            )

            application_logger.warning(
                "Empty Doctor ID entered."
            )

            return

        cursor.execute(
            """
            SELECT *
            FROM doctors
            WHERE doctor_id=%s
            """,
            (doctor_id,)
        )

        if cursor.fetchone():

            print(
                "Doctor ID already exists."
            )

            application_logger.warning(
                f"Duplicate Doctor ID : {doctor_id}"
            )

            return


        if doctor_name == "":

            print(
                "Doctor Name cannot be empty."
            )

            application_logger.warning(
                "Empty Doctor Name entered."
            )

            return

        if not doctor_name.replace(
            " ",
            ""
        ).isalpha():

            print(
                "Doctor Name should contain only alphabets."
            )

            application_logger.warning(
                "Invalid Doctor Name entered."
            )

            return

       

        if department == "":

            print(
                "Department cannot be empty."
            )

            application_logger.warning(
                "Empty Department entered."
            )

            return

      

        if consultation_fee <= 0:

            print(
                "Consultation Fee must be greater than zero."
            )

            application_logger.warning(
                "Invalid Consultation Fee entered."
            )

            return

        

        valid_status = [
            "Available",
            "Unavailable",
            "On Leave"
        ]

        if availability_status not in valid_status:

            print(
                "Invalid Availability Status."
            )

            application_logger.warning(
                f"Invalid Status : {availability_status}"
            )

            return

     
        query = """
        INSERT INTO doctors
        (
            doctor_id,
            doctor_name,
            department,
            consultation_fee,
            availability_status
        )

        VALUES
        (
            %s,%s,%s,%s,%s
        )
        """

        values = (
            doctor_id,
            doctor_name,
            department,
            consultation_fee,
            availability_status
        )

        cursor.execute(
            query,
            values
        )

        connection.commit()

        print(
            "\nDoctor Added Successfully."
        )

        application_logger.info(
            f"Doctor {doctor_id} added successfully."
        )

    except ValueError:

        print(
            "Please enter a valid numeric Consultation Fee."
        )

        exception_logger.exception(
            "ValueError occurred while adding doctor."
        )

    except mysql.connector.Error as error:

        print(
            "Database Error :",
            error
        )

        exception_logger.exception(error)

    except Exception as error:

        print(
            "Unexpected Error :",
            error
        )

        exception_logger.exception(error)

    finally:

        application_logger.info(
            "Exited Add Doctor Module."
        )