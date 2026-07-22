import mysql.connector

from db_connection import (
    connection,
    cursor
)

from logger_module import (
    application_logger,
    exception_logger
)


def view_all_bills():

    try:

        query = """
        SELECT
            b.bill_id,
            b.patient_id,
            p.patient_name,
            b.appointment_id,
            b.gross_amount,
            b.discount,
            b.total_amount,
            b.payment_status
        FROM bills b
        INNER JOIN patients p
        ON b.patient_id = p.patient_id
        ORDER BY b.bill_id;
        """

        cursor.execute(query)

        bills = cursor.fetchall()

        if len(bills) == 0:

            print("\nNo Bills Found.")

            application_logger.warning(
                "No bills available."
            )

            return

        print("\n" + "=" * 80)
        print("                ALL BILLS")
        print("=" * 80)

        for bill in bills:

            print(f"""
Bill ID           : {bill[0]}
Patient ID        : {bill[1]}
Patient Name      : {bill[2]}
Appointment ID    : {bill[3]}
Gross Amount      : {bill[4]}
Discount          : {bill[5]}
Total Amount      : {bill[6]}
Payment Status    : {bill[7]}
            """)

            print("-" * 80)

        application_logger.info(
            "Viewed all bills successfully."
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