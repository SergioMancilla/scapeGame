from .classes import Zombie, Boogie, Walker, Player

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
        "speed": 10,
        "life": 30
    })

def createWalker():
    return Walker({
        "damage": 10,
        "speed": 6,
        "life": 15
    })