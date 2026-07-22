import logging

universities = {}

logging.basicConfig(
    filename="university.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

def add_university():
    try:
        u_id = int(input("Enter University ID: "))
        student_id = int(input("Enter Student ID: "))
        student_name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))
        branch = input("Enter Student Branch: ")

        student_list = {
            student_id: [student_name, age, branch]
        }

        if u_id in universities:
            print("University already exists.")
            logging.warning("University already exists.")
        else:
            universities[u_id] = student_list
            print("University added successfully.")
            logging.info("University added successfully.")

    except Exception as e:
        print(e)
        logging.error(str(e))


if __name__ == "__main__":
    add_university()
    print(universities)