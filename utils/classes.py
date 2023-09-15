from abc import ABC, abstractmethod
import random

import pygame

from .animations import *

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.blood = 100

# Enemies
class Enemy(ABC):
    def __init__(self, qualities: int, images_idle: list, images_run: list) -> None:
        super().__init__()
        self.qualities = self.setQualities(qualities)
        # We load the images for both movements
        self.images_idle = images_idle
        self.images_run = images_run
        # Initialize the character with any image
        self.setImage(self.images_idle[0])

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

    def setImage(self, image):
        self.image = image
        self.rect = self.image.get_rect()

    def changePosition(self):
        ''' Change the position on a randomly way
            The character can take one of 3 actions in vertical in 3 ways: up, down, doesn't move
            Analogically for the horizontal movement '''
        self.rect.x += random.choice([-2, 0, 2])
        self.rect.y += random.choice([-2, 0, 2])

    def setInitialPosition(self, x_pos: int, y_pos: int):
        self.rect.x = x_pos;
        self.rect.y = y_pos;


class Zombie(Enemy, pygame.sprite.Sprite):
    def __init__(self, qualities: dict) -> None:
        super().__init__(qualities, self.images_idle, self.images_run)

    images_idle = zombie_idle
    images_run = zombie_run

class Boogie(Enemy, pygame.sprite.Sprite):
    def __init__(self, qualities: dict) -> None:
        super().__init__(qualities, self.images_idle, self.images_run)

    images_idle = boogie_idle
    images_run = boogie_run

class Walker(Enemy, pygame.sprite.Sprite):
    def __init__(self, qualities: dict) -> None:
        super().__init__(qualities, self.images_idle, self.images_run)

    images_idle = walker_idle
    images_run = walker_run
    
        

        