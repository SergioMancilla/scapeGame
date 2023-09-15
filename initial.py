import random
import pygame
from utils.characters import *
from utils.animations import *

pygame.init()
screen_width = 1000
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

# -------------------------------------------------------------------
mob_sprite_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

n_enemies = 20

boogies_rate = n_enemies * 0.25
walkers_rate = n_enemies * 0.35
zombies_rate = n_enemies * 0.4

# Generating enemies
for i in range(n_enemies):
    if i < boogies_rate:
        enemie = createBoogie()
    elif i < walkers_rate:
        enemie = createWalker()
    else:
        enemie = createZombie()
    
    enemie.setInitialPosition(random.randrange(screen_width), random.randrange(screen_height))
    all_sprite_list.add(enemie)
    mob_sprite_list.add(enemie)

# For the animation purposes: every n clock lap
animation_index = 0
animation_timer = 0
animation_delay = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    # RENDER YOUR GAME HERE
    
    if animation_timer >= animation_delay:
        animation_index = (animation_index + 1) % 4
        for mob in mob_sprite_list:
            mob.image = mob.images_idle[animation_index]
            mob.changePosition()
        animation_timer = 0
    else:
        animation_timer += 1

    all_sprite_list.draw(screen)
    

    pygame.display.flip()

    clock.tick(60)

pygame.quit()