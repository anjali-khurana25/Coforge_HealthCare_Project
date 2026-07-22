from database_connection import get_connection

from appointment_booking import book_appointment
from appointment_view import view_all_appointments
from appointment_cancel import cancel_appointment
from appointment_complete import complete_appointment



def appointment_menu():

    while True:


        print("""
        1. Book Appointment
        2. View Appointment
        3. Cancel Appointment
        4. Complete Appointment
        5. Exit
        """)


        choice=input("Choice : ")



        if choice=="1":
            book_appointment(get_connection)


        elif choice=="2":
            view_all_appointments(get_connection)


        elif choice=="3":
            cancel_appointment(get_connection)


        elif choice=="4":
            complete_appointment(get_connection)


        elif choice=="5":
            break



if __name__=="__main__":
    appointment_menu()