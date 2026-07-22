import mysql.connector

from db_connection import (
    connection,
    cursor
)

from logger_module import (
    application_logger,
    exception_logger
)


def search_patient_bills():

    try:

        patient_id = input(
            "Enter Patient ID : "
        ).strip()

        # Check whether patient exists
        cursor.execute(
            """
            SELECT *
            FROM patients
            WHERE patient_id = %s
            """,
            (patient_id,)
        )

        patient = cursor.fetchone()

        if patient is None:

            print("Patient ID does not exist.")

            application_logger.warning(
                f"Invalid Patient ID : {patient_id}"
            )

            return

        # Fetch all bills of the patient
        cursor.execute(
            """
            SELECT
                bill_id,
                appointment_id,
                gross_amount,
                discount,
                total_amount,
                payment_status
            FROM bills
            WHERE patient_id = %s
            """,
            (patient_id,)
        )

        bills = cursor.fetchall()

        if len(bills) == 0:

            print("No bills found for this patient.")

            application_logger.warning(
                f"No bills found for Patient ID : {patient_id}"
            )

            return

        total_billed = 0
        total_paid = 0
        total_pending = 0

        print("\n" + "=" * 70)
        print("PATIENT BILL DETAILS")
        print("=" * 70)

        for bill in bills:

            print(f"""
Bill ID          : {bill[0]}
Appointment ID   : {bill[1]}
Gross Amount     : {bill[2]}
Discount         : {bill[3]}
Total Amount     : {bill[4]}
Payment Status   : {bill[5]}
            """)

            print("-" * 70)

            total_billed += float(bill[4])

            if bill[5] == "Paid":

                total_paid += float(bill[4])

            else:

                total_pending += float(bill[4])

        print("\n========== BILL SUMMARY ==========")

        print(f"Total Billed Amount  : {total_billed}")

        print(f"Total Paid Amount    : {total_paid}")

        print(f"Total Pending Amount : {total_pending}")

        application_logger.info(
            f"Bills searched successfully for Patient ID : {patient_id}"
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