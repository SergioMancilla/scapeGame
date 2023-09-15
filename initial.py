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

# Colors
RED = (176, 11, 13)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# -------------------------------------------------------------------

class Game():
    def __init__(self) -> None:
        super().__init__()

    mob_sprite_list = pygame.sprite.Group()
    all_sprite_list = pygame.sprite.Group()

    # Mask for make the flashlight effect
    flash_radio = 70
    flashlight = pygame.Surface((2 * flash_radio, 2 * flash_radio), pygame.SRCALPHA)
    pygame.draw.circle(flashlight, (255, 255, 255, 150), (flash_radio, flash_radio), flash_radio)

    def drawLifeBar(self, current_life: int):
        bar_width = 150
        bar_height = 35
        stroke = 5
        new_bar_width = int(bar_width * (current_life / 100))
        life_bar = pygame.Rect(20, 10, new_bar_width, bar_height)
        bar_border = pygame.Rect(20-stroke, 10, bar_width+2*stroke, bar_height)
        pygame.draw.rect(screen, RED, life_bar)
        pygame.draw.rect(screen, WHITE, bar_border, stroke, 3)

    # Generating enemies
    def generateEnemies(self, num_enemies: int):
        boogies_rate = n_enemies * 0.25
        walkers_rate = n_enemies * 0.35
        # zombies_rate = n_enemies * 0.4
        for i in range(n_enemies):
            if i < boogies_rate:
                enemie = createBoogie()
            elif i < boogies_rate + walkers_rate:
                enemie = createWalker()
            else:
                enemie = createZombie()
            
            enemie.setInitialPosition(random.randrange(screen_width), random.randrange(screen_height))
            self.all_sprite_list.add(enemie)
            self.mob_sprite_list.add(enemie)


    def generatePlayer(self):
        self.player = createPlayer()
        # Set the player in the left bottom corner to start the game
        self.player_height = self.player.rect[3]
        self.player_width = self.player.rect[2]
        self.player.setInitialPosition(0, screen_height - self.player_height)
        self.all_sprite_list.add(self.player)

game = Game()
n_enemies = 30
game.generateEnemies(n_enemies)
game.generatePlayer()

# For the animation purposes: every n clock lap
animation_index = 0
animation_timer = 0
animation_delay = 5

background = pygame.image.load("assets/fondo.jpg")
background = pygame.transform.scale(background, (screen_width, screen_height))


# --------------------------------------------------------------------

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    # screen.blit(background, (0, 0))


    # flashlight effect
    player_pos = game.player.rect
    flashlight_rect = game.flashlight.get_rect(center=(player_pos.x + game.player_width/2, player_pos.y + game.player_height/2))

    screen3 = screen.copy()
    # game.all_sprite_list.draw(screen3)
    screen.blit(screen3, (0, 0))
    screen2 = screen.copy() 
    screen2.blit(game.flashlight, flashlight_rect.topleft)
    screen2.blit(game.player.image, game.player.rect.topleft)
    for mob in game.mob_sprite_list:
        if abs(mob.rect.x - game.player.rect.x) < game.flash_radio -5 and abs(mob.rect.y - game.player.rect.y) < game.flash_radio -5:
            screen2.blit(mob.image, mob.rect.topleft)

    screen.blit(screen2, (0, 0))
    

    # RENDER YOUR GAME HERE
    
    # This allows to give animations to the characters
    if animation_timer >= animation_delay:
        animation_index = (animation_index + 1) % 4
        for mob in game.mob_sprite_list:
            mob.image = mob.images_run[animation_index]
            game.player.image = game.player.images_move[animation_index]
            mob.changePosition()
        animation_timer = 0
    else:
        animation_timer += 1


    mob_collider_list = pygame.sprite.groupcollide(game.mob_sprite_list, [game.player], True, False)

    # Game controls
    keys = pygame.key.get_pressed()
    game.player.playerRunning()
    if keys[pygame.K_a] and (game.player.rect.x - game.player.speed > 0):
        game.player.moveLeft()
    elif keys[pygame.K_d] and (game.player.rect.x + game.player_width < screen_width):
        game.player.moveRight()
    elif keys[pygame.K_w] and (game.player.rect.y + game.player.speed > 0):
        game.player.moveUp()
    elif keys[pygame.K_s] and (game.player.rect.y + game.player_height < screen_height):
        game.player.moveDown()
    else:
        game.player.playerIdle()


    # Drawing the lifebar
    for mob in mob_collider_list:
        game.player.reduceBlood(mob.damage)
    game.drawLifeBar(game.player.blood)
    

    pygame.display.flip()

    clock.tick(60)

pygame.quit()