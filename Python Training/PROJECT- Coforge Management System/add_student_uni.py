from database_connection import get_database_connection
import mysql.connector

from logger_config import (
    application_logger,
    exception_logger
)


def add_student_to_university():

    connection = None
    cursor = None

    try:

        university_id = int(
            input("Enter University ID: ")
        )

        student_id = int(
            input("Enter Student ID: ")
        )

        student_name = input(
            "Enter Student Name: "
        ).strip()

        student_age = int(
            input("Enter Student Age: ")
        )

        student_branch = input(
            "Enter Student Branch: "
        ).strip()

        # Validate University ID
        if university_id <= 0:
            print(
                "University ID must be greater than zero."
            )
            return

        # Validate Student ID
        if student_id <= 0:
            print(
                "Student ID must be greater than zero."
            )
            return

        # Validate Student Name
        if student_name == "":
            print(
                "Student name cannot be empty."
            )
            return

        # Validate Student Age
        if student_age <= 0:
            print(
                "Student age must be greater than zero."
            )
            return

        # Validate Student Branch
        if student_branch == "":
            print(
                "Student branch cannot be empty."
            )
            return

        connection = get_database_connection()

        if connection is None:
            print(
                "Database connection failed."
            )
            return

        cursor = connection.cursor()

        # Check whether university exists
        university_query = """
        SELECT university_id
        FROM universities
        WHERE university_id = %s
        """

        cursor.execute(
            university_query,
            (university_id,)
        )

        university = cursor.fetchone()

        if university is None:

            print(
                f"University ID {university_id} does not exist."
            )

            application_logger.warning(
                "Student could not be added because "
                "university ID %s does not exist.",
                university_id
            )

            return

        # Check whether student already exists
        student_check_query = """
        SELECT student_id
        FROM students
        WHERE university_id = %s
        AND student_id = %s
        """

        cursor.execute(
            student_check_query,
            (
                university_id,
                student_id
            )
        )

        student = cursor.fetchone()

        if student is not None:

            print(
                "Student already exists in this university."
            )

            application_logger.warning(
                "Student ID %s already exists in University ID %s.",
                student_id,
                university_id
            )

            return

        # Insert student
        insert_student_query = """
        INSERT INTO students
        (
            student_id,
            student_name,
            student_age,
            student_branch,
            university_id
        )
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(
            insert_student_query,
            (
                student_id,
                student_name,
                student_age,
                student_branch,
                university_id
            )
        )

        connection.commit()

        print(
            "Student added successfully."
        )

        application_logger.info(
            "Student ID %s added successfully "
            "to University ID %s.",
            student_id,
            university_id
        )

    except ValueError as error:

        print(
            "Invalid input. Please enter valid numeric values."
        )

        exception_logger.exception(
            "Invalid input while adding student: %s",
            error
        )

    except ValueError as error:
        print(
            "University ID, Student ID and Age "
            "must be valid numbers."
        )

        exception_logger.exception(
            "Invalid numeric value entered: %s",
            error
        )

    except mysql.connector.IntegrityError as error:
        if connection is not None:
            connection.rollback()

        print(
            "Student record could not be inserted "
            "because of a database constraint."
        )

        exception_logger.exception(
            "Database integrity error: %s",
            error
        )

    except mysql.connector.Error as error:
        if connection is not None:
            connection.rollback()

        print(
            "Database error while adding student:",
            error
        )

        exception_logger.exception(
            "MySQL error while adding student: %s",
            error
        )

    except Exception as error:
        if connection is not None:
            connection.rollback()

        print(
            "Unexpected error while adding student:",
            error
        )

        exception_logger.exception(
            "Unexpected error while adding student: %s",
            error
        )

    finally:
        if cursor is not None:
            cursor.close()

        if (
            connection is not None
            and connection.is_connected()
        ):
            connection.close()

            application_logger.info(
                "Database connection closed."
            )