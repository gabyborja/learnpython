""" # Ex45 You Make a Game
# Requirements
1. Make a different game from the one I made.
2. Use more than one file, and use import to use them. Make sure you know what that is.
3. Use one class per room and give the classes names that fit their purposes
4. Your runner will need to know about these rooms, so make a class that runs them and knows about them. There are plenty of ways to do this, but consider having each room return what room is next or setting a variable of what room is next. 
"""

class Map(object):
    
    def __init__(self, room):
        self.room_list = {'copper_room':CopperRoom(), 'jade_room':JadeRoom(), 'crystal_room':CrystalRoom(), 'finished':Finished(), 'death':Death()}
        print("Map __init__")
        self.room = room
        print(self.room)
    
    def opening_room(self):
        print(f"{self.room_list.get((self.room))}")
        return self.room_list.get((self.room))

class Engine(object):
    def __init__(self, map):
        self.map = map
        pass

    def play(self):
        print("Engine play")
        print(f"self.map {self.map}")
        room = self.map.opening_room()
        print(f"Engine play opening_room {room}")
        next_room = room.enter() 

class Room(object):
    def __init__(self):
        print("Room __init__")

class CopperRoom(Room):
    def __init__(self):
        print("CopperRoom __init___")
    
    def enter(self):
        print("CopperRoom enter")
        return 'jade_room'

class JadeRoom(Room):
    def __init__(self):
      print("JadeRoom __init___")
    
    def enter(self):
        print("JadeRoom enter")
        return 'crystal_room'

class CrystalRoom(Room):
    def __init__(self):
        print("CrystalRoom __init___")
    
    def enter(self):
        print("CrystalRoom enter")
        return 'finished'

class Death(Room):
    def __init__(self):
        print("Death __init__")
    
    def enter(self):
        print("Death enter")
        exit(1)

class Finished(Room):
    def __init__(self):
        print("Finished __init__")
    
    def enter(self):
        print("Finished enter")
        exit(1)

a_map = Map('copper_room')
a_game = Engine(a_map)
a_game.play()