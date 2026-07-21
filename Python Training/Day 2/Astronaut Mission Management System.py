# Astronaut Mission Management System (Tuple + List)

astronauts = []


def register_astronaut():
    astro_id = int(input("Enter Astronaut ID: "))
    name = input("Enter Astronaut Name: ")
    agency = input("Enter Space Agency: ")

    n = int(input("Enter Number of Missions: "))
    missions = []

    for i in range(n):
        mission = input("Enter Mission Name: ")
        missions.append(mission)

    astronaut = (astro_id, name, agency, missions)
    astronauts.append(astronaut)

    print("Astronaut registered successfully.")


def view_astronauts():
    if len(astronauts) == 0:
        print("No astronaut records found.")
    else:
        for astro in astronauts:
            print("\nAstronaut ID :", astro[0])
            print("Name         :", astro[1])
            print("Agency       :", astro[2])
            print("Missions     :", ", ".join(astro[3]))
            print("--------------------------------------------")


def assign_mission():
    astro_id = int(input("Enter Astronaut ID: "))
    found = False

    for astro in astronauts:
        if astro[0] == astro_id:
            mission = input("Enter New Mission Name: ")
            astro[3].append(mission)
            print("Mission assigned successfully.")
            found = True
            break

    if found == False:
        print("Astronaut not found.")


def complete_mission():
    astro_id = int(input("Enter Astronaut ID: "))
    found = False

    for astro in astronauts:
        if astro[0] == astro_id:
            mission = input("Enter Mission Name: ")

            if mission in astro[3]:
                astro[3].remove(mission)
                print("Mission completed and removed successfully.")
            else:
                print("Mission not found.")

            found = True
            break

    if found == False:
        print("Astronaut not found.")


def search_astronaut():
    astro_id = int(input("Enter Astronaut ID: "))
    found = False

    for astro in astronauts:
        if astro[0] == astro_id:
            print("\nAstronaut ID :", astro[0])
            print("Name         :", astro[1])
            print("Agency       :", astro[2])
            print("Missions     :", ", ".join(astro[3]))
            found = True
            break

    if found == False:
        print("Astronaut not found.")


def experienced_astronauts():
    found = False

    for astro in astronauts:
        if len(astro[3]) >= 3:
            print("\nName :", astro[1])
            print("Agency :", astro[2])
            print("Total Missions :", len(astro[3]))
            found = True

    if found == False:
        print("No experienced astronauts found.")


def agency_count():
    if len(astronauts) == 0:
        print("No astronaut records found.")
    else:
        agencies = []

        for astro in astronauts:
            if astro[2] not in agencies:
                agencies.append(astro[2])

        for agency in agencies:
            count = 0

            for astro in astronauts:
                if astro[2] == agency:
                    count += 1

            print(agency, ":", count)


while True:
    print("\n========== Astronaut Mission Management System ==========")
    print("1. Register New Astronaut")
    print("2. View All Astronauts")
    print("3. Assign New Mission")
    print("4. Complete (Remove) Mission")
    print("5. Search Astronaut")
    print("6. Display Experienced Astronauts")
    print("7. Display Space Agency-wise Astronaut Count")
    print("8. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        register_astronaut()

    elif choice == 2:
        view_astronauts()

    elif choice == 3:
        assign_mission()

    elif choice == 4:
        complete_mission()

    elif choice == 5:
        search_astronaut()

    elif choice == 6:
        experienced_astronauts()

    elif choice == 7:
        agency_count()

    elif choice == 8:
        print("Thank you for using Astronaut Mission Management System.")
        break

    else:
        print("Invalid Choice. Please try again.")