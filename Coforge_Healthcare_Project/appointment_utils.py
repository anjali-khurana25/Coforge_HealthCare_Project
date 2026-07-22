def patient_exists(cursor, patient_id):

    query = """
    SELECT patient_id
    FROM patients
    WHERE patient_id=%s
    """

    cursor.execute(
        query,
        (patient_id,)
    )

    return cursor.fetchone()



def doctor_exists(cursor, doctor_id):

    query = """
    SELECT doctor_id
    FROM doctors
    WHERE doctor_id=%s
    """

    cursor.execute(
        query,
        (doctor_id,)
    )

    return cursor.fetchone()



def doctor_available(cursor,
                     doctor_id,
                     date,
                     time):


    query = """
    SELECT *
    FROM appointments
    WHERE doctor_id=%s
    AND appointment_date=%s
    AND appointment_time=%s
    AND status='Booked'
    """

    cursor.execute(
        query,
        (
            doctor_id,
            date,
            time
        )
    )

    result = cursor.fetchone()


    return result is None