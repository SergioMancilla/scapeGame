from abc import ABC, abstractmethod
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.blood = 100

# Enemies
class Enemy(ABC):
    def __init__(self, qualities: int) -> None:
        self.qualities = self.setQualities(qualities)

    qualities = {
        "damage": int,
        "speed": int,
        "life": int
    }

    def setQualities(self, qualities: dict):
        return {
            "damage": qualities["damage"],
            "speed": qualities["speed"],
            "life": qualities["life"]
        }


class Zombie(Enemy, pygame.sprite.Sprite):
    def __init__(self, qualities: dict) -> None:
        super().__init__(qualities)

class Boogie(Enemy, pygame.sprite.Sprite):
    def __init__(self, qualities: dict) -> None:
        super().__init__(qualities)

class Walker(Enemy, pygame.sprite.Sprite):
    def __init__(self, qualities: dict) -> None:
        super().__init__(qualities)
    
        

        