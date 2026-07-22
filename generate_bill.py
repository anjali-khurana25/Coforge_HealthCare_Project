import mysql.connector

from db_connection import (
    connection,
    cursor
)

from logger_module import (
    application_logger,
    exception_logger
)


def generate_bill():

    try:

        bill_id = input(
            "Enter Bill ID : "
        ).strip()

        patient_id = input(
            "Enter Patient ID : "
        ).strip()

        appointment_id = input(
            "Enter Appointment ID : "
        ).strip()

        # Check Duplicate Bill ID
        cursor.execute(
            """
            SELECT *
            FROM bills
            WHERE bill_id=%s
            """,
            (bill_id,)
        )

        if cursor.fetchone():

            print("Bill ID already exists.")

            application_logger.warning(
                f"Duplicate Bill ID : {bill_id}"
            )

            return

        # Check Patient Exists
        cursor.execute(
            """
            SELECT *
            FROM patients
            WHERE patient_id=%s
            """,
            (patient_id,)
        )

        if cursor.fetchone() is None:

            print("Patient does not exist.")

            application_logger.warning(
                f"Invalid Patient ID : {patient_id}"
            )

            return

        # Check Appointment Exists
        cursor.execute(
            """
            SELECT status
            FROM appointments
            WHERE appointment_id=%s
            """,
            (appointment_id,)
        )

        appointment = cursor.fetchone()

        if appointment is None:

            print("Appointment does not exist.")

            application_logger.warning(
                f"Invalid Appointment ID : {appointment_id}"
            )

            return

        if appointment[0] != "Completed":

            print(
                "Bill can only be generated for completed appointments."
            )

            application_logger.warning(
                f"Appointment {appointment_id} is not completed."
            )

            return

        # Check One Bill Per Appointment
        cursor.execute(
            """
            SELECT *
            FROM bills
            WHERE appointment_id=%s
            """,
            (appointment_id,)
        )

        if cursor.fetchone():

            print(
                "Bill already generated for this appointment."
            )

            application_logger.warning(
                f"Duplicate bill for Appointment {appointment_id}"
            )

            return

        # Charges
        consultation_fee = float(
            input("Enter Consultation Fee : ")
        )

        medicine_charges = float(
            input("Enter Medicine Charges : ")
        )

        laboratory_charges = float(
            input("Enter Laboratory Charges : ")
        )

        room_charges = float(
            input("Enter Room Charges : ")
        )

        discount = float(
            input("Enter Discount : ")
        )

        payment_status = input(
            "Enter Payment Status (Paid/Pending) : "
        ).title()

        # Validation
        if consultation_fee < 0:
            print("Consultation Fee cannot be negative.")
            return

        if medicine_charges < 0:
            print("Medicine Charges cannot be negative.")
            return

        if laboratory_charges < 0:
            print("Laboratory Charges cannot be negative.")
            return

        if room_charges < 0:
            print("Room Charges cannot be negative.")
            return

        if discount < 0:
            print("Discount cannot be negative.")
            return

        gross_amount = (
            consultation_fee +
            medicine_charges +
            laboratory_charges +
            room_charges
        )

        if discount > gross_amount:

            print(
                "Discount cannot be greater than Gross Amount."
            )

            application_logger.warning(
                "Invalid Discount Entered."
            )

            return

        total_amount = gross_amount - discount

        if payment_status not in (
            "Paid",
            "Pending"
        ):

            print("Invalid Payment Status.")

            return

        # Insert Bill
        query = """
        INSERT INTO bills
        (
            bill_id,
            patient_id,
            appointment_id,
            consultation_fee,
            medicine_charges,
            laboratory_charges,
            room_charges,
            gross_amount,
            discount,
            total_amount,
            payment_status
        )
        VALUES
        (
            %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
        )
        """

        values = (
            bill_id,
            patient_id,
            appointment_id,
            consultation_fee,
            medicine_charges,
            laboratory_charges,
            room_charges,
            gross_amount,
            discount,
            total_amount,
            payment_status
        )

        cursor.execute(
            query,
            values
        )

        connection.commit()

        print("\nBill Generated Successfully.")

        print(
            f"Gross Amount : {gross_amount}"
        )

        print(
            f"Total Amount : {total_amount}"
        )

        application_logger.info(
            f"Bill {bill_id} generated successfully."
        )

    except ValueError:

        print(
            "Please enter valid numeric values."
        )

        exception_logger.exception(
            "ValueError while generating bill."
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