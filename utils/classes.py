from abc import ABC
import random

import pygame

from .animations import *

class Player(pygame.sprite.Sprite):
    def __init__(self, qualities: dict) -> None:
        super().__init__()

        self.blood = 100
        self.num_keys_collected = 0
        self.speed = qualities["speed"]
        self.isAlive = True

        self.images_idle = main_idle
        self.images_run = main_run
        self.setImage(self.images_idle[0])

    speed: int
    num_keys_collected: int
    isAlive: bool

    def setImage(self, image):
        self.image = image
        self.rect = self.image.get_rect()

    def setInitialPosition(self, x_pos: int, y_pos: int):
        self.rect.x = x_pos;
        self.rect.y = y_pos;

    def moveUp(self):
        self.rect.y -= self.speed

    def moveDown(self):
        self.rect.y += self.speed

    def moveLeft(self):
        self.rect.x -= self.speed

    def moveRight(self):
        self.rect.x += self.speed

    def playerRunning(self):
        self.images_move = self.images_run

    def playerIdle(self):
        self.images_move = self.images_idle

    def reduceBlood(self, damage: int):
        if self.blood - damage >= 0:
            self.blood -= damage
        else:
            self.blood = 0
            self.isAlive = False

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

    damage: int
    speed: int
    life: int

    def setQualities(self, qualities: dict):
        self.damage = qualities["damage"]
        self.speed = qualities["speed"]
        self.life = qualities["life"]

    def setImage(self, image):
        self.image = image
        self.rect = self.image.get_rect()

    def changePosition(self):
        ''' Change the position on a randomly way
            The character can take one of 3 actions in vertical in 3 ways: up, down, doesn't move
            Analogically for the horizontal movement '''
        self.rect.x += random.choice([-self.speed, 0, self.speed])
        self.rect.y += random.choice([-self.speed, 0, self.speed])

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
    
        

        