import mysql.connector

from db_connection import (
    get_database_connection
)

from logger_module import (
    application_logger,
    exception_logger
)


def search_patient():

    connection = None
    cursor = None

    try:

        connection = get_database_connection()

        cursor = connection.cursor(
            dictionary=True
        )

        print("\n===== Search Patient =====")
        print("1. Patient ID")
        print("2. Patient Name")
        print("3. Contact Number")
        print("4. City")
        print("5. Disease")
        print("6. Blood Group")

        choice = int(
            input("Enter Choice : ")
        )

        if choice == 1:

            patient_id = int(
                input("Enter Patient ID : ")
            )

            query = """
                    SELECT *
                    FROM patient
                    WHERE patient_id=%s
                    """

            value = (patient_id,)

        elif choice == 2:

            patient_name = input(
                "Enter Patient Name : "
            )

            query = """
                    SELECT *
                    FROM patient
                    WHERE patient_name=%s
                    """

            value = (patient_name,)

        elif choice == 3:

            contact_number = input(
                "Enter Contact Number : "
            )

            query = """
                    SELECT *
                    FROM patient
                    WHERE contact_number=%s
                    """

            value = (contact_number,)

        elif choice == 4:

            city = input(
                "Enter City : "
            )

            query = """
                    SELECT *
                    FROM patient
                    WHERE city=%s
                    """

            value = (city,)

        elif choice == 5:

            disease = input(
                "Enter Disease : "
            )

            query = """
                    SELECT *
                    FROM patient
                    WHERE disease=%s
                    """

            value = (disease,)

        elif choice == 6:

            blood_group = input(
                "Enter Blood Group : "
            )

            query = """
                    SELECT *
                    FROM patient
                    WHERE blood_group=%s
                    """

            value = (blood_group,)

        else:

            print("Invalid Choice.")
            return

        cursor.execute(
            query,
            value
        )

        patients = cursor.fetchall()

        if not patients:

            print("No Patient Found.")

            application_logger.warning(
                "Patient Search Failed."
            )

            return

        print("\n========== Patient Details ==========\n")

        for patient in patients:

            print(f"Patient ID      : {patient['patient_id']}")
            print(f"Patient Name    : {patient['patient_name']}")
            print(f"Age             : {patient['age']}")
            print(f"Gender          : {patient['gender']}")
            print(f"Contact Number  : {patient['contact_number']}")
            print(f"City            : {patient['city']}")
            print(f"Blood Group     : {patient['blood_group']}")
            print(f"Disease         : {patient['disease']}")
            print("-" * 50)

        application_logger.info(
            "Patient Search Successful."
        )

    except ValueError:

        print("Invalid Input.")

        exception_logger.exception(
            "ValueError Occurred."
        )

    except mysql.connector.Error as error:

        print(error)

        exception_logger.exception(error)

    except Exception as error:

        print(error)

        exception_logger.exception(error)

    finally:

        if cursor:

            cursor.close()

        if connection:

            connection.close()