tasks = []


def add_task():
    task = input("Enter Task Name: ")
    tasks.append(task)
    print("Task added successfully.")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nProject Tasks")
        for i in range(len(tasks)):
            print(i + 1, "-", tasks[i])


def search_task():
    task = input("Enter Task Name: ")
    if task in tasks:
        print("Task Found.")
    else:
        print("Task Not Found.")


def update_task():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nProject Tasks")
        for i in range(len(tasks)):
            print(i + 1, "-", tasks[i])

        num = int(input("Enter Task Number: "))

        if num >= 1 and num <= len(tasks):
            new_task = input("Enter New Task: ")
            tasks[num - 1] = new_task
            print("Task updated successfully.")
        else:
            print("Invalid Task Number.")


def delete_task():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nProject Tasks")
        for i in range(len(tasks)):
            print(i + 1, "-", tasks[i])

        num = int(input("Enter Task Number: "))

        if num >= 1 and num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted successfully.")
        else:
            print("Invalid Task Number.")


def count_tasks():
    print("Total Project Tasks :", len(tasks))


while True:
    print("\n========== Project Task Management System ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Count Tasks")
    print("7. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_task()

    elif choice == 2:
        view_tasks()

    elif choice == 3:
        search_task()

    elif choice == 4:
        update_task()

    elif choice == 5:
        delete_task()

    elif choice == 6:
        count_tasks()

    elif choice == 7:
        print("Thank you for using Project Task Management System.")
        break

    else:
        print("Invalid Choice. Please try again.")