import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",          # Empty password
        database="healthcare_db"
    )

    cursor = connection.cursor()

    if connection.is_connected():
        print("Database Connected Successfully")

except mysql.connector.Error as err:
    print("Database Connection Error:", err)