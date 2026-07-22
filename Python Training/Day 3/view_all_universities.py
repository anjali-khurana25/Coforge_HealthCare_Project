import logging
import student_university_module


logging.basicConfig(
    filename="university.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


def view_all_universities():

    try:
        if not student_university_module.universities:

            print("No universities found.")
            logging.warning("No universities found.")

        else:

            for u_id, students in student_university_module.universities.items():

                print("University ID:", u_id)
                print("Students:", students)

                logging.info(
                    f"University ID: {u_id}, Students: {students}"
                )

    except Exception as e:

        print(f"Error while viewing universities: {e}")
        logging.error(str(e))

    else:
        logging.info("View function executed successfully.")


if __name__ == "__main__":
    view_all_universities()