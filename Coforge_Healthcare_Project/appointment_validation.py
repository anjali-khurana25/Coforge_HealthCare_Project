from datetime import datetime


def validate_appointment_id(app_id):

    if not str(app_id).isdigit():
        raise ValueError("Appointment ID must be numeric.")

    return int(app_id)



def validate_date(date):

    try:

        appointment_date = datetime.strptime(
            date,
            "%Y-%m-%d"
        )

        if appointment_date.date() < datetime.today().date():
            raise ValueError(
                "Past date is not allowed."
            )

        return date


    except ValueError:

        raise ValueError(
            "Date should be YYYY-MM-DD format."
        )



def validate_time(time):

    try:

        datetime.strptime(
            time,
            "%H:%M"
        )

        return time


    except ValueError:

        raise ValueError(
            "Time should be HH:MM format."
        )