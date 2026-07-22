import mysql.connector

from db_connection import (
    connection,
    cursor
)

from logger_module import (
    application_logger,
    exception_logger
)


def update_payment_status():

    try:

        bill_id = input(
            "Enter Bill ID : "
        ).strip()

        # Check Bill ID
        cursor.execute(
            """
            SELECT payment_status
            FROM bills
            WHERE bill_id=%s
            """,
            (bill_id,)
        )

        bill = cursor.fetchone()

        if bill is None:

            print(
                "Bill ID does not exist."
            )

            application_logger.warning(
                f"Invalid Bill ID : {bill_id}"
            )

            return

        # Check Payment Status
        if bill[0] == "Paid":

            print(
                "Payment has already been completed."
            )

            application_logger.warning(
                f"Bill {bill_id} is already paid."
            )

            return

        # Update Payment Status
        cursor.execute(
            """
            UPDATE bills
            SET payment_status = 'Paid'
            WHERE bill_id = %s
            """,
            (bill_id,)
        )

        connection.commit()

        print(
            "\nPayment Status Updated Successfully."
        )

        application_logger.info(
            f"Payment status updated for Bill ID : {bill_id}"
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