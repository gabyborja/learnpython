""" # Ex45 You Make a Game
# Requirements
1. Make a different game from the one I made.
2. Use more than one file, and use import to use them. Make sure you know what that is.
3. Use one class per room and give the classes names that fit their purposes
4. Your runner will need to know about these rooms, so make a class that runs them and knows about them. There are plenty of ways to do this, but consider having each room return what room is next or setting a variable of what room is next. 
"""

class Engine(object):
    def __init__(self, map):
        self.map = map
        pass

    def play(self):
        print("Engine play")
        print(f"self.map {self.map}")
        room = self.map.opening_room()
        print(f"Engine play opening_room {room}")
        last_room = self.map.next_room('finished')
        print(f"Engine play last_room {last_room}")

        while room != last_room:
            print(f"Engine play enter {room}")
            next_room_str = room.enter()
            print(f"Engine next_room {next_room_str}")
            room = self.map.next_room(next_room_str)

        room.enter()

class Room(object):
    def __init__(self):
        print("Room __init__")

class CopperRoom(Room):
    def __init__(self):
        print("CopperRoom __init___")
    
    def enter(self):
        print("CopperRoom enter")
        print("You start out in the copper room. Where do you want to go next?")
        direction = input("> ")

        if direction == 'north':
            "You went north"
            return 'jade_room'
        elif direction == 'south':
            return 'death'
        elif direction == 'east':
            return 'death'
        elif direction == 'west':
            return 'death'
        else:
            "Invalid input"
            return 'copper_room'

class JadeRoom(Room):
    def __init__(self):
      print("JadeRoom __init___")
    
    def enter(self):
        print("JadeRoom enter")
        print("You reached the jade room")
        direction = input("> ")

        if direction == 'north':
            "You went north"
            return 'crystal_room'
        elif direction == 'south':
            return 'death'
        elif direction == 'east':
            return 'death'
        elif direction == 'west':
            return 'death'
        else:
            "Invalid input"
            return 'jade_room'
        

class CrystalRoom(Room):
    def __init__(self):
        print("CrystalRoom __init___")
    
    def enter(self):
        print("CrystalRoom enter")
        print("You reached the crystal room room")
        direction = input("> ")

        if direction == 'north':
            "You went north"
            return 'finished'
        elif direction == 'south':
            return 'death'
        elif direction == 'east':
            return 'death'
        elif direction == 'west':
            return 'death'
        else:
            "Invalid input"
            return 'crystal_room'

class Death(Room):
    def __init__(self):
        print("Death __init__")
    
    def enter(self):
        print("Death enter")
        print("You died. Game over.")
        exit(1)

class Finished(Room):
    def __init__(self):
        print("Finished __init__")
    
    def enter(self):
        print("Finished enter")
        print("You reached the end. You win.")
        exit(1)

class Map(object):
    room_list = {
        'copper_room':CopperRoom(), 
        'jade_room':JadeRoom(), 
        'crystal_room':CrystalRoom(), 
        'finished':Finished(), 
        'death':Death()
    }

    def __init__(self, start_room):
        print("Map __init__")
        self.start_room = start_room
        print(f"Map __init__ {self.start_room}")
    
    def next_room(self, next_room):
        next_room_object = self.room_list.get(next_room) 
        return next_room_object

    def opening_room(self):
        print(f"Opening_room {self.next_room(self.start_room)}")
        return self.next_room(self.start_room)

a_map = Map('copper_room')
a_game = Engine(a_map)
a_game.play()