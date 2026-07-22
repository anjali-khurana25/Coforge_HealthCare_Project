from db_connection import connection, cursor
from logger_module import logger
import validation_module


def generate_bill():
    try:

        bill_id = input("Enter Bill ID : ").strip()
        patient_id = input("Enter Patient ID : ").strip()
        appointment_id = input("Enter Appointment ID : ").strip()

        # -------------------------------
        # Duplicate Bill Check
        # -------------------------------

        cursor.execute(
            "SELECT * FROM bills WHERE bill_id=%s",
            (bill_id,)
        )

        if cursor.fetchone():
            print("Bill ID already exists.")
            logger.warning(f"Duplicate Bill ID : {bill_id}")
            return

        # -------------------------------
        # Patient Check
        # -------------------------------

        cursor.execute(
            "SELECT * FROM patients WHERE patient_id=%s",
            (patient_id,)
        )

        if cursor.fetchone() is None:
            print("Patient does not exist.")
            logger.warning(f"Invalid Patient ID : {patient_id}")
            return

        # -------------------------------
        # Appointment Check
        # -------------------------------

        cursor.execute(
            "SELECT status FROM appointments WHERE appointment_id=%s",
            (appointment_id,)
        )

        appointment = cursor.fetchone()

        if appointment is None:
            print("Appointment does not exist.")
            logger.warning(f"Invalid Appointment ID : {appointment_id}")
            return

        if appointment[0] != "Completed":
            print("Bill can only be generated for completed appointments.")
            logger.warning(
                f"Appointment {appointment_id} not completed."
            )
            return

        # -------------------------------
        # One Bill Per Appointment
        # -------------------------------

        cursor.execute(
            "SELECT * FROM bills WHERE appointment_id=%s",
            (appointment_id,)
        )

        if cursor.fetchone():
            print("Bill already generated for this appointment.")
            logger.warning(
                f"Duplicate bill for Appointment {appointment_id}"
            )
            return

        # -------------------------------
        # Charges
        # -------------------------------

        consultation_fee = float(
            input("Consultation Fee : ")
        )

        medicine_charges = float(
            input("Medicine Charges : ")
        )

        laboratory_charges = float(
            input("Laboratory Charges : ")
        )

        room_charges = float(
            input("Room Charges : ")
        )

        discount = float(
            input("Discount : ")
        )

        payment_status = input(
            "Payment Status (Paid/Pending) : "
        ).title()

        # -------------------------------
        # Validation
        # -------------------------------

        amounts = [
            consultation_fee,
            medicine_charges,
            laboratory_charges,
            room_charges,
            discount
        ]

        for amount in amounts:

            if amount < 0:
                print("Charges cannot be negative.")
                logger.error("Negative amount entered.")
                return

        gross_amount = (
            consultation_fee
            + medicine_charges
            + laboratory_charges
            + room_charges
        )

        if discount > gross_amount:
            print("Discount cannot exceed Gross Amount.")
            logger.error("Invalid Discount")
            return

        total_amount = gross_amount - discount

        if payment_status not in ("Paid", "Pending"):
            print("Invalid Payment Status.")
            logger.error("Invalid Payment Status")
            return

        # -------------------------------
        # Insert Bill
        # -------------------------------

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

        cursor.execute(query, values)

        connection.commit()

        print("\nBill Generated Successfully")

        print(f"Gross Amount : {gross_amount}")

        print(f"Total Amount : {total_amount}")

        logger.info(
            f"Bill {bill_id} generated successfully."
        )

    except ValueError:

        print("Please enter valid numeric values.")

        logger.exception("Value Error")

    except Exception as error:

        print("Error :", error)

        logger.exception(error)
def view_all_bills():

    try:

        cursor.execute("""
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

            ORDER BY b.bill_id
        """)

        bills = cursor.fetchall()

        if not bills:
            print("\nNo Bills Found.")
            logger.warning("No bills available.")
            return

        print("\n" + "=" * 80)
        print("ALL BILLS")
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

    except Exception as error:

        print("Error :", error)

        logger.exception(error)


def search_patient_bills():

    try:

        patient_id = input(
            "Enter Patient ID : "
        ).strip()

        cursor.execute("""
            SELECT
                bill_id,
                appointment_id,
                gross_amount,
                discount,
                total_amount,
                payment_status

            FROM bills

            WHERE patient_id=%s
        """, (patient_id,))

        bills = cursor.fetchall()

        if not bills:

            print("No Bills Found.")

            logger.warning(
                f"No bills found for Patient {patient_id}"
            )

            return

        total_billed = 0
        total_paid = 0
        total_pending = 0

        print("\n" + "=" * 70)
        print(f"BILLS OF PATIENT : {patient_id}")
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

    except Exception as error:

        print("Error :", error)

        logger.exception(error)
def update_payment_status():

    try:

        bill_id = input(
            "Enter Bill ID : "
        ).strip()

        cursor.execute("""
            SELECT payment_status
            FROM bills
            WHERE bill_id=%s
        """, (bill_id,))

        bill = cursor.fetchone()

        if bill is None:

            print("Bill ID not found.")

            logger.warning(
                f"Invalid Bill ID : {bill_id}"
            )

            return

        if bill[0] == "Paid":

            print("Payment is already completed.")

            logger.warning(
                f"Bill {bill_id} already paid."
            )

            return

        cursor.execute("""
            UPDATE bills
            SET payment_status='Paid'
            WHERE bill_id=%s
        """, (bill_id,))

        connection.commit()

        print("\nPayment Status Updated Successfully.")

        logger.info(
            f"Payment updated for Bill {bill_id}"
        )

    except Exception as error:

        print("Error :", error)

        logger.exception(error)