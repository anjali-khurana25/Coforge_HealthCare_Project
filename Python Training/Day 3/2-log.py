import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s - %(message)s"
)

def get_employee_details():
    logging.info("Enter Employee Details")

    while True:
        emp_id = input("Enter Employee ID: ").strip()
        if emp_id != "":
            break
        logging.warning("Employee ID cannot be empty")

    while True:
        name = input("Enter Employee Name: ").strip()
        if name != "":
            break
        logging.warning("Employee Name cannot be empty")

    while True:
        try:
            basic_salary = float(input("Enter Basic Salary: "))
            if basic_salary > 0:
                break
            logging.warning("Basic Salary must be greater than zero")
        except ValueError:
            logging.error("Invalid Basic Salary")

    while True:
        try:
            overtime_hours = int(input("Enter Overtime Hours: "))
            if overtime_hours >= 0:
                break
            logging.warning("Overtime Hours cannot be negative")
        except ValueError:
            logging.error("Invalid Overtime Hours")

    while True:
        try:
            leave_days = int(input("Enter Leave Days: "))
            if leave_days >= 0:
                break
            logging.warning("Leave Days cannot be negative")
        except ValueError:
            logging.error("Invalid Leave Days")

    logging.info("Employee Details Saved Successfully")

    return {
        "id": emp_id,
        "name": name,
        "basic_salary": basic_salary,
        "overtime_hours": overtime_hours,
        "leave_days": leave_days
    }


def calculate_hra(basic_salary):
    logging.debug("Calculating HRA")
    return basic_salary * 0.20


def calculate_da(basic_salary):
    logging.debug("Calculating DA")
    return basic_salary * 0.10


def calculate_overtime(overtime_hours):
    logging.debug("Calculating Overtime Payment")
    return overtime_hours * 500


def calculate_leave_deduction(leave_days):
    logging.debug("Calculating Leave Deduction")
    if leave_days <= 2:
        return 0
    return (leave_days - 2) * 1000


def calculate_pf(basic_salary):
    logging.debug("Calculating PF")
    return basic_salary * 0.12


def calculate_professional_tax(gross_salary):
    logging.debug("Calculating Professional Tax")
    if gross_salary <= 30000:
        return 200
    elif gross_salary <= 60000:
        return 500
    else:
        return 1000


def calculate_payroll(employee):
    logging.info("Calculating Monthly Payroll")

    hra = calculate_hra(employee["basic_salary"])
    da = calculate_da(employee["basic_salary"])
    overtime = calculate_overtime(employee["overtime_hours"])

    gross_salary = employee["basic_salary"] + hra + da + overtime

    pf = calculate_pf(employee["basic_salary"])
    professional_tax = calculate_professional_tax(gross_salary)
    leave_deduction = calculate_leave_deduction(employee["leave_days"])

    total_deduction = pf + professional_tax + leave_deduction
    net_salary = gross_salary - total_deduction

    logging.info("Payroll Calculated Successfully")

    return {
        "hra": hra,
        "da": da,
        "overtime": overtime,
        "gross_salary": gross_salary,
        "pf": pf,
        "professional_tax": professional_tax,
        "leave_deduction": leave_deduction,
        "total_deduction": total_deduction,
        "net_salary": net_salary
    }


def display_salary_slip(employee, payroll):
    logging.info("----------------------------------------")
    logging.info("EMPLOYEE SALARY SLIP")
    logging.info("----------------------------------------")
    logging.info(f"Employee ID       : {employee['id']}")
    logging.info(f"Employee Name     : {employee['name']}")
    logging.info(f"Basic Salary      : ₹{employee['basic_salary']:.2f}")
    logging.info(f"HRA               : ₹{payroll['hra']:.2f}")
    logging.info(f"DA                : ₹{payroll['da']:.2f}")
    logging.info(f"Overtime Payment  : ₹{payroll['overtime']:.2f}")
    logging.info(f"Gross Salary      : ₹{payroll['gross_salary']:.2f}")
    logging.info(f"PF Deduction      : ₹{payroll['pf']:.2f}")
    logging.info(f"Professional Tax  : ₹{payroll['professional_tax']:.2f}")
    logging.info(f"Leave Deduction   : ₹{payroll['leave_deduction']:.2f}")
    logging.info(f"Total Deduction   : ₹{payroll['total_deduction']:.2f}")
    logging.info(f"Net Salary        : ₹{payroll['net_salary']:.2f}")
    logging.info("----------------------------------------")


employee = None
payroll = None

while True:
    logging.info("")
    logging.info("EMPLOYEE PAYROLL MANAGEMENT SYSTEM")
    logging.info("1. Enter Employee Details")
    logging.info("2. Calculate Monthly Payroll")
    logging.info("3. Display Salary Slip")
    logging.info("4. Calculate Annual Net Salary")
    logging.info("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        logging.error("Invalid Menu Choice")
        continue

    if choice == 1:
        employee = get_employee_details()

    elif choice == 2:
        if employee is None:
            logging.warning("Employee details are not available")
        else:
            payroll = calculate_payroll(employee)

    elif choice == 3:
        if employee is None:
            logging.warning("Enter Employee Details First")
        elif payroll is None:
            logging.warning("Calculate Payroll First")
        else:
            display_salary_slip(employee, payroll)

    elif choice == 4:
        if payroll is None:
            logging.warning("Calculate Payroll First")
        else:
            annual_salary = payroll["net_salary"] * 12
            logging.info(f"Annual Net Salary : ₹{annual_salary:.2f}")

    elif choice == 5:
        logging.critical("Program Closed Successfully")
        break

    else:
        logging.error("Invalid Menu Option Selected")