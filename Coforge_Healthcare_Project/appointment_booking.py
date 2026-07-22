import logging
import mysql.connector

from appointment_validation import *
from appointment_utils import *



def book_appointment(get_connection):

    connection=None
    cursor=None


    try:

        connection=get_connection()

        cursor=connection.cursor()


        appointment_id = validate_appointment_id(
            input("Appointment ID : ")
        )


        patient_id=int(
            input("Patient ID : ")
        )


        doctor_id=int(
            input("Doctor ID : ")
        )


        date=validate_date(
            input("Date YYYY-MM-DD : ")
        )


        time=validate_time(
            input("Time HH:MM : ")
        )



        if not patient_exists(cursor,patient_id):

            print("Patient not found")
            return



        if not doctor_exists(cursor,doctor_id):

            print("Doctor not found")
            return



        if not doctor_available(
            cursor,
            doctor_id,
            date,
            time
        ):

            logging.warning(
                "Duplicate Appointment"
            )

            print(
                "Doctor unavailable"
            )

            return



        query="""
        INSERT INTO appointments
        VALUES(%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(
            query,
            (
                appointment_id,
                patient_id,
                doctor_id,
                date,
                time,
                "Booked"
            )
        )


        connection.commit()


        logging.info(
            "Appointment Booked"
        )


        print(
            "Appointment Booked Successfully"
        )


    except Exception as e:

        logging.error(e)

        print(e)



    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()