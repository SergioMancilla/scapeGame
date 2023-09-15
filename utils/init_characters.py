from .classes import Zombie, Boogie, Walker, Player, Key, Door

def createPlayer():
    return Player({
        "speed": 2
    })

# Define the characters qualities here
def createZombie():
    return Zombie({
        "damage": 5,
        "speed": 2,
        "life": 10
    })

def createBoogie():
    return Boogie({
        "damage": 20,
        "speed": 8,
        "life": 30
    })

def createWalker():
    return Walker({
        "damage": 10,
        "speed": 4,
        "life": 15
    })

def createKey():
    return Key()

def createDoor():
    return Door()