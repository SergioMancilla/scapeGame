import random
import pygame
from utils.init_characters import *
from utils.load_animations import *

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
GRAY = (168, 179, 176)

# -------------------------------------------------------------------

class Game():
    def __init__(self) -> None:
        super().__init__()
        self.mob_sprite_list = pygame.sprite.Group()
        self.key_sprite_list = pygame.sprite.Group()
        self.all_sprite_list = pygame.sprite.Group()

    # Mask for make the flashlight effect
    flash_radio = 70
    font = pygame.font.SysFont("serif", 26)
    font_small = pygame.font.SysFont("serif", 16)

    def makeCircleFlash(self):
        self.flashlight = pygame.Surface((2 * self.flash_radio, 2 * self.flash_radio), pygame.SRCALPHA)
        pygame.draw.circle(self.flashlight, (148, 95, 38, 150), (self.flash_radio, self.flash_radio), self.flash_radio)

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

    def generateKeys(self, num_keys: int):
        for i in range(num_keys):
            key = createKey()
            key.setInitialPosition(random.randrange(screen_width), random.randrange(screen_height))
            self.all_sprite_list.add(key)
            self.key_sprite_list.add(key)

    def generateDoor(self):
        self.door = createDoor()
        self.door.setInitialPosition(random.randrange(screen_width), random.randrange(screen_height))
        self.all_sprite_list.add(self.door)

def gameOver():
    screen.fill("black")
    game_over_text = game.font.render("GAME OVER", True, WHITE)
    game_over_info = game.font_small.render("Da click en cualquier lugar para volver al menú principal", True, GRAY)
    game_over_text_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
    game_over_info_rect = game_over_info.get_rect(center=(screen_width // 2, screen_height // 2 + 30))
    screen.blit(game_over_text, game_over_text_rect.topleft)
    screen.blit(game_over_info, game_over_info_rect.topleft)

def goMainMenu():
    global n_keys, n_enemies
    n_keys = 0
    n_enemies = 0
    global is_main_menu
    is_main_menu = True
    screen.fill("white")
    game_over_text = game.font.render("SCAPE GAME", True, BLACK)
    game_over_info = game.font_small.render("Da click en cualquier lugar para comenzar", True, GRAY)
    game_over_text_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))
    game_over_info_rect = game_over_info.get_rect(center=(screen_width // 2, screen_height // 2 + 30))
    screen.blit(game_over_text, game_over_text_rect.topleft)
    screen.blit(game_over_info, game_over_info_rect.topleft)

def nextLevel():
    game.__init__()
    global n_enemies, n_keys, n_keys_remaining
    n_enemies += 5
    n_keys += 2
    generateCharacters(n_enemies, n_keys)
    n_keys_remaining = n_keys

def newGame():
    game.__init__()
    global n_enemies, n_keys, n_keys_remaining, is_game_over, is_main_menu
    n_enemies = 10
    n_keys = 2
    generateCharacters(n_enemies, n_keys)
    n_keys_remaining = n_keys
    is_game_over = False
    is_main_menu = False

def generateCharacters(n_enemies, n_keys):
    global game
    game.generateEnemies(n_enemies)
    game.generatePlayer()
    game.makeCircleFlash()
    game.generateKeys(n_keys)
    game.generateDoor()

game = Game()
n_enemies: int
n_keys: int
is_game_over = False
is_main_menu = True
# newGame()
goMainMenu()

# n_keys_remaining = n_keys

# For the animation purposes: every n clock lap
animation_index = 0
animation_timer = 0
animation_delay = 5



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if is_main_menu and event.type == pygame.MOUSEBUTTONDOWN:
            newGame()
            is_main_menu = False
        if is_game_over and event.type == pygame.MOUSEBUTTONDOWN:
            is_game_over = False
            goMainMenu()
            

    if not is_main_menu:
        screen.fill("black")

    if not is_game_over and not is_main_menu:
        # flashlight effect
        player_pos = game.player.rect
        flashlight_rect = game.flashlight.get_rect(center=(player_pos.x + game.player_width/2, player_pos.y + game.player_height/2))
        screen3 = screen.copy()
        screen.blit(screen3, (0, 0))
        screen2 = screen.copy() 
        screen2.blit(game.flashlight, flashlight_rect.topleft)

        # Render the player
        screen2.blit(game.player.image, game.player.rect.topleft)

        # Render the enemies and other objects if they are near to the main character
        for mob in game.mob_sprite_list:
            if abs(mob.rect.x - game.player.rect.x) < game.flash_radio -20 and abs(mob.rect.y - game.player.rect.y) < game.flash_radio -20:
                screen2.blit(mob.image, mob.rect.topleft)
        for key in game.key_sprite_list:
            if abs(key.rect.x - game.player.rect.x) < game.flash_radio -20 and abs(key.rect.y - game.player.rect.y) < game.flash_radio -20:
                screen2.blit(key.image, key.rect.topleft)
        if abs(game.door.rect.x - game.player.rect.x) < game.flash_radio -20 and abs(game.door.rect.y - game.player.rect.y) < game.flash_radio -20:
            screen2.blit(game.door.image, game.door.rect.topleft)

        screen.blit(screen2, (0, 0))
        
        # This allows to give animations to the characters
        if animation_timer >= animation_delay:
            animation_index = (animation_index + 1) % 4
            for mob in game.mob_sprite_list:
                mob.image = mob.images_run[animation_index]
                game.player.image = game.player.images_move[animation_index]
                mob.changePosition()
            for key in game.key_sprite_list:
                key.image = key.images[animation_index]
            animation_timer = 0
        else:
            animation_timer += 1
        if n_keys_remaining <= 0:
            game.door.image = game.door.door_open


        mob_collider_list = pygame.sprite.groupcollide(game.mob_sprite_list, [game.player], True, False)
        key_collider_list = pygame.sprite.groupcollide(game.key_sprite_list, [game.player], True, False)
        door_collider_list = pygame.sprite.groupcollide([game.door], [game.player], False, False)

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


        # In case of collition
        for mob in mob_collider_list:
            game.player.reduceBlood(mob.damage)
            screen.fill("red")
            if (game.player.blood <= 0):
                screen.fill("black")
                is_game_over = True
        for key in key_collider_list:
            n_keys_remaining -= 1
        for door in door_collider_list:
            if n_keys_remaining <= 0:
                nextLevel()
        
        game.drawLifeBar(game.player.blood)

        # Rendering the score
        score_text = "Llaves restantes: " + str(n_keys_remaining)
        score_render = game.font.render(score_text, True, WHITE)
        screen.blit(score_render, [200, 13])
    elif is_game_over:
        gameOver()
    else:
        goMainMenu()
    

    pygame.display.flip()

    clock.tick(60)

pygame.quit()