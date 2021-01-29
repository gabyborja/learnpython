def start():
    print("This is the start")
    print("What direction do you want to go?")
    direction = input("> ")

    if direction.lower() == "north":
        print(f"You went {direction}")
        cold_room()
    elif direction.lower() == "south":
        print(f"You went {direction}")
        hot_room()
    elif direction.lower() == "east":
        print(f"You went {direction}")
        windy_room()
    elif direction.lower() == "west":
        print(f"You went {direction}")
        diamond_room()
    else:
        print("You died")
        exit(0)

def cold_room():
    print("It's very cold")
    print("You froze and can't move")
    exit(0)

def hot_room():
    print("It's very hot")
    print("You melted")
    exit(0)

def windy_room():
    print("It's very windy")
    print("You were blown away")
    exit(0)

def diamond_room():
    print("DIAMOND HANDS BABY! TO THE MOON")
    exit(0)

start()
