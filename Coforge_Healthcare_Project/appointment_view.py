import logging


def view_all_appointments(get_connection):


    connection=None
    cursor=None


    try:

        connection=get_connection()

        cursor=connection.cursor()


        cursor.execute(
            "SELECT * FROM appointments"
        )


        data=cursor.fetchall()



        for row in data:

            print(row)



    except Exception as e:

        logging.error(e)

        print(e)



    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()