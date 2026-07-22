import csv
from datetime import datetime

import mysql.connector

from database_connection import get_database_connection
from logger_config import application_logger, exception_logger


def export_university_report():
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
            print("No data available to export.")
            return

        filename = f"university-report-{datetime.now():%Y%m%d-%H%M%S}.csv"
        with open(filename, "w", newline="", encoding="utf-8") as report_file:
            writer = csv.DictWriter(
                report_file,
                fieldnames=[
                    "university_id", "university_name", "student_id",
                    "student_name", "student_age", "student_branch"
                ]
            )
            writer.writeheader()
            writer.writerows(rows)

        print(f"University report exported to '{filename}'.")
        application_logger.info("University report exported to %s.", filename)
    except mysql.connector.Error as error:
        print("Database Error:", error)
        exception_logger.exception("Database error while exporting report: %s", error)
    except OSError as error:
        print("Unable to write report file:", error)
        exception_logger.exception("Report file error: %s", error)
    except Exception as error:
        print("Unexpected application error:", error)
        exception_logger.exception("Unexpected export error: %s", error)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
