def add_university(u_id, student_list):
    try:
        if u_id in universities:
            print(f"University with ID {u_id} already exists.")
            logging.warning(f"University with ID {u_id} already exists.")
    except Exception as e:
        print(f"Error in adding the university::{str(e)}")
        logging.error(f"{str(e)}")
        
    else:
        universities[u_id] = student_list
        logging.info(f"University with ID {u_id} added successfully.")
