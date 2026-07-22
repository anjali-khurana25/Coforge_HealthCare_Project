import mysql.connector

from database_connection import get_database_connection
from logger_config import application_logger, exception_logger


def view_all_universities():
    connection = None
    cursor = None

    try:
        connection = get_database_connection()
        if connection is None:
            return

        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            """SELECT u.university_id, u.university_name,
                      s.student_id, s.student_name, s.student_age,
                      s.student_branch
               FROM universities AS u
               LEFT JOIN students AS s ON s.university_id = u.university_id
               ORDER BY u.university_id, s.student_id"""
        )
        rows = cursor.fetchall()

        if not rows:
            print("No universities found.")
            return

        current_university = None
        for row in rows:
            university_id = row["university_id"]
            if university_id != current_university:
                current_university = university_id
                print(f"\nUniversity ID: {university_id}")
                print(f"University Name: {row['university_name']}")

            if row["student_id"] is None:
                print("  Students: None")
            else:
                print(
                    f"  Student ID: {row['student_id']}, "
                    f"Name: {row['student_name']}, Age: {row['student_age']}, "
                    f"Branch: {row['student_branch']}"
                )

        application_logger.info("All universities viewed successfully.")
    except mysql.connector.Error as error:
        print("Database Error:", error)
        exception_logger.exception("Database error while viewing universities: %s", error)
    except Exception as error:
        print("Unexpected application error:", error)
        exception_logger.exception("Unexpected view error: %s", error)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
