visitors = []


def add_visitor():
    name = input("Enter Visitor Name: ")
    address = input("Enter Visitor Address: ")
    phone = input("Enter Visitor Phone No: ")
    email = input("Enter Visitor Email: ")
    city = input("Enter Visitor City: ")

    visitors.append(name)
    print("Visitor added successfully.")


def view_visitors():
    if len(visitors) == 0:
        print("No visitor records found.")
    else:
        print("\nToday's Visitors")
        for i in range(len(visitors)):
            print(i + 1, "-", visitors[i])


def search_visitor():
    name = input("Enter Visitor Name: ")

    if name in visitors:
        print("Visitor Found.")
    else:
        print("Visitor Not Found.")


def update_visitor():
    if len(visitors) == 0:
        print("No visitor records found.")
    else:
        print("\nToday's Visitors")
        for i in range(len(visitors)):
            print(i + 1, "-", visitors[i])

        num = int(input("Enter Visitor Number: "))

        if num >= 1 and num <= len(visitors):
            new_name = input("Enter New Visitor Name: ")
            visitors[num - 1] = new_name
            print("Visitor details updated successfully.")
        else:
            print("Invalid Visitor Number.")


def remove_visitor():
    if len(visitors) == 0:
        print("No visitor records found.")
    else:
        print("\nToday's Visitors")
        for i in range(len(visitors)):
            print(i + 1, "-", visitors[i])

        num = int(input("Enter Visitor Number: "))

        if num >= 1 and num <= len(visitors):
            visitors.pop(num - 1)
            print("Visitor removed successfully.")
        else:
            print("Invalid Visitor Number.")


def total_visitors():
    print("Total Visitors Today :", len(visitors))


while True:
    print("\n========== Office Visitor Management System ==========")
    print("1. Add Visitor")
    print("2. View Visitors")
    print("3. Search Visitor")
    print("4. Update Visitor")
    print("5. Remove Visitor")
    print("6. Total Visitors")
    print("7. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_visitor()

    elif choice == 2:
        view_visitors()

    elif choice == 3:
        search_visitor()

    elif choice == 4:
        update_visitor()

    elif choice == 5:
        remove_visitor()

    elif choice == 6:
        total_visitors()

    elif choice == 7:
        print("Thank you for using Office Visitor Management System.")
        break

    else:
        print("Invalid Choice. Please try again.")