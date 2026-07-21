skills = ["Python", "SQL", "Excel"]

def display_skills():
    print("Skills:", skills)

def insert_skill():
    new_skill = input("Type new skill: ")
    skills.append(new_skill)
    print("Added!")

def update_skill():
    old = input("Skill to change: ")
    new = input("New name: ")
    index = skills.index(old)
    skills[index] = new
    print("Updated!")

def remove_skill():
    old = input("Skill to delete: ")
    skills.remove(old)
    print("Removed!")

while True:
    print("\n--- EMPLOYEE SKILL MANAGEMENT ---")
    print("1. Display")
    print("2. Insert")
    print("3. Update")
    print("4. Remove")
    print("5. Display skill by enumerate")
    print("6. Exit")
    
    choice = input("Enter Choice: ")
    
    if choice == "1":
        display_skills()
    elif choice == "2":
        insert_skill()
    elif choice == "3":
        update_skill()
    elif choice == "4":
        remove_skill()
    elif choice == "5":
        for index, skill in enumerate(skills):
            print(f"{index}: {skill}")
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please select 1 to 5.")
        continue

    cont = input("\nDo you want to continue? (y/n): ").strip().lower()
    if cont != 'y':
        print("Exiting program.")
        break