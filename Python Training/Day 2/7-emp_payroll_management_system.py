def get_employee_details():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Basic Salary: "))
    overtime_hours = int(input("Enter Overtime Hours: "))
    leave_days = int(input("Enter Leave Days: "))

    return emp_id, name, basic_salary, overtime_hours, leave_days

def calculate_hra(basic_salary):
    return basic_salary * 0.20


def calculate_da(basic_salary):
    return basic_salary * 0.10

def calculate_overtime(overtime_hours):
    return overtime_hours * 500


def calculate_leave_deduction(leave_days):
    if leave_days <= 2:
        return 0
    else:
        return (leave_days - 2) * 1000

def calculate_pf(basic_salary):
    return basic_salary * 0.12

def calculate_professional_tax(gross_salary):
    if gross_salary <= 30000:
        return 200
    elif gross_salary <= 60000:
        return 500
    else:
        return 1000


def calculate_payroll(basic_salary, overtime_hours, leave_days):

    hra = calculate_hra(basic_salary)
    da = calculate_da(basic_salary)
    overtime = calculate_overtime(overtime_hours)

    gross_salary = basic_salary + hra + da + overtime

    pf = calculate_pf(basic_salary)
    professional_tax = calculate_professional_tax(gross_salary)
    leave_deduction = calculate_leave_deduction(leave_days)

    total_deduction = pf + professional_tax + leave_deduction

    net_salary = gross_salary - total_deduction

    return hra, da, overtime, gross_salary, pf, professional_tax, leave_deduction, total_deduction, net_salary


def display_salary_slip(emp_id, name, basic_salary,
                        hra, da, overtime, gross_salary,
                        pf, professional_tax,
                        leave_deduction,
                        total_deduction,
                        net_salary):

    print("\n----------------------------------------")
    print("         EMPLOYEE SALARY SLIP")
    print("----------------------------------------")
    print("Employee ID      :", emp_id)
    print("Employee Name    :", name)
    print("Basic Salary     : ₹", basic_salary)
    print("HRA              : ₹", hra)
    print("DA               : ₹", da)
    print("Overtime Payment : ₹", overtime)
    print("Gross Salary     : ₹", gross_salary)
    print("PF Deduction     : ₹", pf)
    print("Professional Tax : ₹", professional_tax)
    print("Leave Deduction  : ₹", leave_deduction)
    print("Total Deduction  : ₹", total_deduction)
    print("Net Salary       : ₹", net_salary)
    print("----------------------------------------")


emp_id = ""
name = ""
basic_salary = 0
overtime_hours = 0
leave_days = 0
payroll_done = False


while True:

    print("\n===== EMPLOYEE PAYROLL MANAGEMENT SYSTEM =====")
    print("1. Enter Employee Details")
    print("2. Calculate Monthly Payroll")
    print("3. Display Salary Slip")
    print("4. Calculate Annual Net Salary")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id, name, basic_salary, overtime_hours, leave_days = get_employee_details()

    elif choice == 2:
        hra, da, overtime, gross_salary, pf, professional_tax, leave_deduction, total_deduction, net_salary = calculate_payroll(
            basic_salary, overtime_hours, leave_days)
        payroll_done = True
        print("Payroll Calculated Successfully.")

    elif choice == 3:
        if payroll_done:
            display_salary_slip(emp_id, name, basic_salary,
                                hra, da, overtime, gross_salary,
                                pf, professional_tax,
                                leave_deduction,
                                total_deduction,
                                net_salary)
        else:
            print("Please calculate payroll first.")

    elif choice == 4:
        if payroll_done:
            annual_salary = net_salary * 12
            print("Annual Net Salary = ₹", annual_salary)
        else:
            print("Please calculate payroll first.")

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")