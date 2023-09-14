from .classes import Zombie, Boogie, Walker

# Define the characters qualities here
def createZombie():
    return Zombie({
        "damage": 5,
        "speed": 100,
        "life": 10
    })

def createBoogie():
    return Boogie({
        "damage": 20,
        "speed": 180,
        "life": 30
    })

def createWalker():
    return Walker({
        "damage": 10,
        "speed": 130,
        "life": 15
    })