import mysql.connector
from datetime import datetime
import logging

# Logger
logging.basicConfig(
    filename="appointment.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="healthcare_management"
    )



def validate_appointment_id(app_id):
    if not str(app_id).isdigit():
        raise ValueError("Appointment ID must be numeric.")
    return int(app_id)


def validate_date(date):
    try:
        appointment_date = datetime.strptime(date, "%Y-%m-%d")

        if appointment_date.date() < datetime.today().date():
            raise ValueError("Past date is not allowed.")

        return date

    except ValueError:
        raise ValueError("Date should be in YYYY-MM-DD format.")


def validate_time(time):
    try:
        datetime.strptime(time, "%H:%M")
        return time
    except ValueError:
        raise ValueError("Time should be in HH:MM format.")



def patient_exists(cursor, patient_id):

    sql = "SELECT patient_id FROM patients WHERE patient_id=%s"

    cursor.execute(sql, (patient_id,))

    return cursor.fetchone() is not None



def doctor_exists(cursor, doctor_id):

    sql = "SELECT doctor_id FROM doctors WHERE doctor_id=%s"

    cursor.execute(sql, (doctor_id,))

    return cursor.fetchone() is not None



def doctor_available(cursor, doctor_id, date, time):

    sql = """
    SELECT *
    FROM appointments
    WHERE doctor_id=%s
    AND appointment_date=%s
    AND appointment_time=%s
    AND status='Booked'
    """

    cursor.execute(sql, (doctor_id, date, time))

    return cursor.fetchone() is None



def book_appointment():

    connection = None
    cursor = None

    try:

        connection = get_connection()
        cursor = connection.cursor()

        print("\n========== BOOK APPOINTMENT ==========")

        appointment_id = validate_appointment_id(
            input("Enter Appointment ID : ")
        )

        patient_id = int(input("Enter Patient ID : "))
        doctor_id = int(input("Enter Doctor ID : "))

        appointment_date = validate_date(
            input("Enter Appointment Date (YYYY-MM-DD) : ")
        )

        appointment_time = validate_time(
            input("Enter Appointment Time (HH:MM) : ")
        )

        if not patient_exists(cursor, patient_id):
            print("Patient does not exist.")
            return

        if not doctor_exists(cursor, doctor_id):
            print("Doctor does not exist.")
            return

        if not doctor_available(cursor,
                                doctor_id,
                                appointment_date,
                                appointment_time):

            logging.warning("Doctor Unavailable")
            logging.warning("Duplicate Appointment")

            print("Doctor is not available at this time.")
            return

        sql = """
        INSERT INTO appointments
        (
        appointment_id,
        patient_id,
        doctor_id,
        appointment_date,
        appointment_time,
        status
        )
        VALUES(%s,%s,%s,%s,%s,%s)
        """

        values = (
            appointment_id,
            patient_id,
            doctor_id,
            appointment_date,
            appointment_time,
            "Booked"
        )

        cursor.execute(sql, values)

        connection.commit()

        logging.info("Appointment Booked")

        print("\nAppointment Booked Successfully.")

    except mysql.connector.Error as err:
        print("Database Error :", err)
        logging.error(err)

    except ValueError as err:
        print(err)
        logging.error(err)

    except Exception as err:
        print(err)
        logging.error(err)

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()
            


def view_all_appointments():

    connection = None
    cursor = None

    try:

        connection = get_connection()
        cursor = connection.cursor()

        sql = "SELECT * FROM appointments"

        cursor.execute(sql)

        records = cursor.fetchall()

        if len(records) == 0:
            print("\nNo Appointments Found.")
            return

        print("\n================ ALL APPOINTMENTS ================\n")

        print("{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}".format(
            "App ID",
            "Patient ID",
            "Doctor ID",
            "Date",
            "Time",
            "Status"
        ))

        print("-"*90)

        for row in records:

            print("{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}".format(
                row[0],
                row[1],
                row[2],
                str(row[3]),
                str(row[4]),
                row[5]
            ))

    except mysql.connector.Error as err:

        print("Database Error :", err)

        logging.error(err)

    except Exception as err:

        print("Error :", err)

        logging.error(err)

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()




def cancel_appointment():

    connection = None
    cursor = None

    try:

        connection = get_connection()
        cursor = connection.cursor()

        print("\n========== CANCEL APPOINTMENT ==========\n")

        appointment_id = validate_appointment_id(
            input("Enter Appointment ID : ")
        )

        # Appointment Exists

        sql = """
        SELECT *
        FROM appointments
        WHERE appointment_id=%s
        """

        cursor.execute(sql, (appointment_id,))

        appointment = cursor.fetchone()

        if appointment is None:

            print("Appointment not found.")

            return

        # Already Cancelled

        if appointment[5] == "Cancelled":

            print("Appointment is already cancelled.")

            return

        # Already Completed

        if appointment[5] == "Completed":

            print("Completed appointment cannot be cancelled.")

            return

        update_sql = """
        UPDATE appointments
        SET status='Cancelled'
        WHERE appointment_id=%s
        """

        cursor.execute(update_sql, (appointment_id,))

        connection.commit()

        logging.info("Appointment Cancelled")

        print("\nAppointment Cancelled Successfully.")

    except mysql.connector.Error as err:

        print("Database Error :", err)

        logging.error(err)

    except ValueError as err:

        print(err)

        logging.error(err)

    except Exception as err:

        print(err)

        logging.error(err)

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()
            
            
            


def complete_appointment():

    connection = None
    cursor = None

    try:

        connection = get_connection()
        cursor = connection.cursor()

        print("\n========== COMPLETE APPOINTMENT ==========\n")

        appointment_id = validate_appointment_id(
            input("Enter Appointment ID : ")
        )

        # Check Appointment Exists

        sql = """
        SELECT *
        FROM appointments
        WHERE appointment_id=%s
        """

        cursor.execute(sql, (appointment_id,))

        appointment = cursor.fetchone()

        if appointment is None:

            print("Appointment not found.")

            return

        # Already Completed

        if appointment[5] == "Completed":

            print("Appointment is already completed.")

            return

        # Cancelled Appointment

        if appointment[5] == "Cancelled":

            print("Cancelled appointment cannot be completed.")

            return

        # Update Status

        update_sql = """
        UPDATE appointments
        SET status='Completed'
        WHERE appointment_id=%s
        """

        cursor.execute(update_sql, (appointment_id,))

        connection.commit()

        logging.info("Appointment Completed")

        print("\nAppointment Completed Successfully.")

    except mysql.connector.Error as err:

        print("Database Error :", err)

        logging.error(err)

    except ValueError as err:

        print(err)

        logging.error(err)

    except Exception as err:

        print(err)

        logging.error(err)

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()




def appointment_menu():

    while True:

        print("\n===================================")
        print("      APPOINTMENT MANAGEMENT")
        print("===================================")
        print("1. Book Appointment")
        print("2. View All Appointments")
        print("3. Cancel Appointment")
        print("4. Complete Appointment")
        print("5. Exit")

        choice = input("Enter your choice : ")

        if choice == "1":

            book_appointment()

        elif choice == "2":

            view_all_appointments()

        elif choice == "3":

            cancel_appointment()

        elif choice == "4":

            complete_appointment()

        elif choice == "5":

            print("\nExiting Appointment Module...")
            break

        else:

            print("Invalid Choice. Try Again.")




if __name__ == "__main__":
    appointment_menu()