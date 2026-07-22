import mysql.connector

from database_connection import get_database_connection

from logger_config import (
    application_logger,
    exception_logger
)


def add_university():
    connection = None
    cursor = None

    try:
        university_id = int(input("Enter University ID: "))

        university_name = input("Enter University Name: ").strip()

        if university_id <= 0:
            print("University ID must be greater than zero.")
            return

        if university_name == "":
            print("University name cannot be empty.")
            return

        connection = get_database_connection()

        if connection is None:
            return

        cursor = connection.cursor()

        # Check ID already exists
        check_query = """
        SELECT university_id
        FROM universities
        WHERE university_id = %s
        """

        cursor.execute(check_query, (university_id,))
        existing_university = cursor.fetchone()

        if existing_university is not None:
            print(f"University with ID {university_id} already exists.")

            application_logger.warning(
                "University with ID %s already exists.",
                university_id
            )
            return

        # Check Name already exists
        name_check_query = """
        SELECT university_id
        FROM universities
        WHERE university_name = %s
        """

        cursor.execute(name_check_query, (university_name,))
        existing_name = cursor.fetchone()

        if existing_name is not None:
            print(f"University with name '{university_name}' already exists.")

            application_logger.warning(
                "University with name '%s' already exists.",
                university_name
            )
            return

        # Insert University
        insert_query = """
        INSERT INTO universities
        (university_id, university_name)
        VALUES (%s, %s)
        """

        cursor.execute(
            insert_query,
            (university_id, university_name)
        )

        connection.commit()

        print(
            f"University with ID {university_id} and name '{university_name}' added successfully."
        )

        application_logger.info(
            "University with ID %s and name '%s' added successfully.",
            university_id,
            university_name
        )

    except ValueError as error:
        print("Please enter a valid numeric University ID.")

        exception_logger.exception(
            "Invalid University ID: %s",
            error
        )

    except KeyboardInterrupt:
        print("\nApplication stopped by the user.")

        application_logger.warning(
            "Application stopped using keyboard interrupt."
        )

        return

    except mysql.connector.Error as error:
        print("Database Error:", error)

        exception_logger.exception(
            "Database Error: %s",
            error
        )

    except Exception as error:
        print("Unexpected application error:", error)

        exception_logger.exception(
            "Unexpected application error: %s",
            error
        )

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()