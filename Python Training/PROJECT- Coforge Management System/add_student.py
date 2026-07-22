import mysql.connector

from database_connection import get_database_connection
from logger_config import application_logger, exception_logger


def add_student_to_university():
    connection = None
    cursor = None

    try:
        student_id = int(input("Enter Student ID: "))
        university_id = int(input("Enter University ID: "))
        student_name = input("Enter Student Name: ").strip()
        age = int(input("Enter Student Age: "))
        branch = input("Enter Student Branch: ").strip()

        if student_id <= 0 or university_id <= 0 or age <= 0:
            print("Student ID, University ID, and age must be greater than zero.")
            return
        if not student_name or not branch:
            print("Student name and branch cannot be empty.")
            return

        connection = get_database_connection()
        if connection is None:
            return

        cursor = connection.cursor()
        cursor.execute(
            "SELECT university_id FROM universities WHERE university_id = %s",
            (university_id,)
        )
        if cursor.fetchone() is None:
            print(f"University with ID {university_id} was not found.")
            return

        cursor.execute(
            "SELECT student_id FROM students WHERE student_id = %s",
            (student_id,)
        )
        if cursor.fetchone() is not None:
            print(f"Student with ID {student_id} already exists.")
            return

        cursor.execute(
            """INSERT INTO students
               (student_id, university_id, student_name, student_age,
                student_branch)
               VALUES (%s, %s, %s, %s, %s)""",
            (student_id, university_id, student_name, age, branch)
        )
        connection.commit()
        print(f"Student with ID {student_id} added successfully.")
        application_logger.info(
            "Student with ID %s added to university ID %s.",
            student_id,
            university_id
        )

    except ValueError as error:
        print("Please enter valid numeric values for ID and age.")
        exception_logger.exception("Invalid student input: %s", error)
    except mysql.connector.Error as error:
        print("Database Error:", error)
        exception_logger.exception("Database error while adding student: %s", error)
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
    except Exception as error:
        print("Unexpected application error:", error)
        exception_logger.exception("Unexpected add-student error: %s", error)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
