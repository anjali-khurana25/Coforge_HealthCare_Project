# Cricket Team Management System (Tuple + Dictionary)

players = []


def register_player():
    player_id = int(input("Enter Player ID: "))
    name = input("Enter Player Name: ")
    team = input("Enter Team Name: ")

    matches = int(input("Enter Matches Played: "))
    runs = int(input("Enter Total Runs: "))
    centuries = int(input("Enter Centuries: "))
    half_centuries = int(input("Enter Half Centuries: "))

    stats = {
        "Matches": matches,
        "Runs": runs,
        "Centuries": centuries,
        "HalfCenturies": half_centuries
    }

    player = (player_id, name, team, stats)
    players.append(player)

    print("Player registered successfully.")


def view_players():
    if len(players) == 0:
        print("No player records found.")
    else:
        for player in players:
            print("\nPlayer ID       :", player[0])
            print("Player Name     :", player[1])
            print("Team            :", player[2])
            print("Matches         :", player[3]["Matches"])
            print("Runs            :", player[3]["Runs"])
            print("Centuries       :", player[3]["Centuries"])
            print("Half Centuries  :", player[3]["HalfCenturies"])
            print("----------------------------------------")


def update_statistics():
    player_id = int(input("Enter Player ID: "))
    found = False

    for player in players:
        if player[0] == player_id:
            found = True

            print("\n1. Matches")
            print("2. Runs")
            print("3. Centuries")
            print("4. Half Centuries")

            choice = int(input("Enter Your Choice: "))
            value = int(input("Enter New Value: "))

            if choice == 1:
                player[3]["Matches"] = value
            elif choice == 2:
                player[3]["Runs"] = value
            elif choice == 3:
                player[3]["Centuries"] = value
            elif choice == 4:
                player[3]["HalfCenturies"] = value
            else:
                print("Invalid Choice.")
                return

            print("Player statistics updated successfully.")
            break

    if found == False:
        print("Player not found.")


def search_player():
    player_id = int(input("Enter Player ID: "))
    found = False

    for player in players:
        if player[0] == player_id:
            print("\nPlayer ID       :", player[0])
            print("Player Name     :", player[1])
            print("Team            :", player[2])
            print("Matches         :", player[3]["Matches"])
            print("Runs            :", player[3]["Runs"])
            print("Centuries       :", player[3]["Centuries"])
            print("Half Centuries  :", player[3]["HalfCenturies"])
            found = True
            break

    if found == False:
        print("Player not found.")


def highest_run_scorer():
    if len(players) == 0:
        print("No player records found.")
    else:
        highest = players[0]

        for player in players:
            if player[3]["Runs"] > highest[3]["Runs"]:
                highest = player

        print("\nHighest Run Scorer")
        print("Player Name :", highest[1])
        print("Runs        :", highest[3]["Runs"])


def players_centuries():
    found = False

    for player in players:
        if player[3]["Centuries"] > 10:
            print("\nPlayer Name :", player[1])
            print("Centuries  :", player[3]["Centuries"])
            found = True

    if found == False:
        print("No players found with more than 10 centuries.")


def team_count():
    if len(players) == 0:
        print("No player records found.")
    else:
        teams = []

        for player in players:
            if player[2] not in teams:
                teams.append(player[2])

        for team in teams:
            count = 0
            for player in players:
                if player[2] == team:
                    count += 1
            print(team, ":", count)


while True:
    print("\n========== Cricket Team Management System ==========")
    print("1. Register New Player")
    print("2. View All Players")
    print("3. Update Player Statistics")
    print("4. Search Player")
    print("5. Display Highest Run Scorer")
    print("6. Display Players with More Than 10 Centuries")
    print("7. Team-wise Player Count")
    print("8. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        register_player()

    elif choice == 2:
        view_players()

    elif choice == 3:
        update_statistics()

    elif choice == 4:
        search_player()

    elif choice == 5:
        highest_run_scorer()

    elif choice == 6:
        players_centuries()

    elif choice == 7:
        team_count()

    elif choice == 8:
        print("Thank you for using Cricket Team Management System.")
        break

    else:
        print("Invalid Choice. Please try again.")