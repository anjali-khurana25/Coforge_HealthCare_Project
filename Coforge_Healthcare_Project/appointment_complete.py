import logging

from appointment_validation import validate_appointment_id



def complete_appointment(get_connection):


    connection=None
    cursor=None


    try:

        connection=get_connection()

        cursor=connection.cursor()



        appointment_id=validate_appointment_id(
            input("Appointment ID : ")
        )



        query="""
        UPDATE appointments
        SET status='Completed'
        WHERE appointment_id=%s
        """

        cursor.execute(
            query,
            (appointment_id,)
        )


        connection.commit()



        logging.info(
            "Appointment Completed"
        )


        print(
            "Appointment Completed"
        )



    except Exception as e:

        logging.error(e)

        print(e)



    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()