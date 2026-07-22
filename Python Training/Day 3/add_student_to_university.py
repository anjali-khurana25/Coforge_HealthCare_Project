import logging
import student_university_module


logging.basicConfig(
    filename="university.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


def add_student_to_university(u_id, student_id, student_name, age, branch):

    try:

        if u_id in student_university_module.universities:

            if student_id in student_university_module.universities[u_id]:

                print("Student already exists.")
                logging.warning(
                    f"Student with ID {student_id} already exists."
                )

            else:

                student_university_module.universities[u_id][student_id] = [
                    student_name,
                    age,
                    branch
                ]

                print("Student added successfully.")
                logging.info(
                    f"Student added to University ID {u_id}"
                )

        else:

            print("University not found.")
            logging.warning(
                f"No university found with ID {u_id}"
            )


    except Exception as e:

        print(f"Error while adding student: {str(e)}")
        logging.error(str(e))


    else:

        logging.info(
            "Add Student function executed successfully."
        )
