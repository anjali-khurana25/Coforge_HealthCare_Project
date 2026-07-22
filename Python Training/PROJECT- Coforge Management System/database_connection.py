import mysql.connector

from logger_config import (
    application_logger,
    exception_logger
)


def get_database_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sam123",
            database="University_Management"
        )

        if connection.is_connected():
            application_logger.info(
                "MySQL database connection established."
            )

        return connection

    except mysql.connector.Error as error:
        print("Unable to connect to MySQL database.")

        exception_logger.exception(
            "Database connection error: %s",
            error
        )

        return None