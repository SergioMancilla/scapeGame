import random
import pygame
from utils.init_characters import *
from utils.animations import *

pygame.init()
screen_width = 1000
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

# -------------------------------------------------------------------

# Colores
RED = (176, 11, 13)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def drawLifeBar(current_life):
    bar_width = 150
    bar_height = 35
    stroke = 5
    new_bar_width = int(bar_width * (current_life / 100))
    life_bar = pygame.Rect(10, 10, new_bar_width, bar_height)
    bar_border = pygame.Rect(10-stroke, 10, bar_width+2*stroke, bar_height)
    pygame.draw.rect(screen, RED, life_bar)
    pygame.draw.rect(screen, BLACK, bar_border, stroke, 3)

mob_sprite_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

n_enemies = 30

boogies_rate = n_enemies * 0.25
walkers_rate = n_enemies * 0.35
zombies_rate = n_enemies * 0.4

# Generating enemies
for i in range(n_enemies):
    if i < boogies_rate:
        enemie = createBoogie()
    elif i < boogies_rate + walkers_rate:
        enemie = createWalker()
    else:
        enemie = createZombie()
    
    enemie.setInitialPosition(random.randrange(screen_width), random.randrange(screen_height))
    all_sprite_list.add(enemie)
    mob_sprite_list.add(enemie)


player = createPlayer()
# Set the player in the left bottom corner to start the game
player_height = player.rect[3]
player_width = player.rect[2]
player.setInitialPosition(0, screen_height - player_height)
all_sprite_list.add(player)

# For the animation purposes: every n clock lap
animation_index = 0
animation_timer = 0
animation_delay = 5


# --------------------------------------------------------------------

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    # RENDER YOUR GAME HERE
    
    if animation_timer >= animation_delay:
        animation_index = (animation_index + 1) % 4
        for mob in mob_sprite_list:
            mob.image = mob.images_run[animation_index]
            player.image = player.images_move[animation_index]
            mob.changePosition()
        animation_timer = 0
    else:
        animation_timer += 1

    mob_collider_list = pygame.sprite.groupcollide(mob_sprite_list, [player], True, False)

    # Game controls
    keys = pygame.key.get_pressed()
    player.playerRunning()
    if keys[pygame.K_a] and (player.rect.x - player.speed > 0):
        player.moveLeft()
    elif keys[pygame.K_d] and (player.rect.x + player_width < screen_width):
        player.moveRight()
    elif keys[pygame.K_w] and (player.rect.y + player.speed > 0):
        player.moveUp()
    elif keys[pygame.K_s] and (player.rect.y + player_height < screen_height):
        player.moveDown()
    else:
        player.playerIdle()

    all_sprite_list.draw(screen)

    for mob in mob_collider_list:
        player.reduceBlood(mob.damage)
    
    drawLifeBar(player.blood)
    

    pygame.display.flip()

    clock.tick(60)

pygame.quit()