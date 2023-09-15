import pygame

# Loading the images and the sprites

floor_image = pygame.image.load("assets/fondo.jpg")

main_idle = [
    pygame.image.load("assets/main/wizzard_f_idle_anim_f0.png"),
    pygame.image.load("assets/main/wizzard_f_idle_anim_f1.png"),
    pygame.image.load("assets/main/wizzard_f_idle_anim_f2.png"),
    pygame.image.load("assets/main/wizzard_f_idle_anim_f3.png"),
]

main_run = [
    pygame.image.load("assets/main/wizzard_f_run_anim_f0.png"),
    pygame.image.load("assets/main/wizzard_f_run_anim_f1.png"),
    pygame.image.load("assets/main/wizzard_f_run_anim_f2.png"),
    pygame.image.load("assets/main/wizzard_f_run_anim_f3.png"),
]

boogie_idle = [
    pygame.image.load("assets/boogie/big_demon_idle_anim_f0.png"),
    pygame.image.load("assets/boogie/big_demon_idle_anim_f1.png"),
    pygame.image.load("assets/boogie/big_demon_idle_anim_f2.png"),
    pygame.image.load("assets/boogie/big_demon_idle_anim_f3.png"),
]

boogie_run = [
    pygame.image.load("assets/boogie/big_demon_run_anim_f0.png"),
    pygame.image.load("assets/boogie/big_demon_run_anim_f1.png"),
    pygame.image.load("assets/boogie/big_demon_run_anim_f2.png"),
    pygame.image.load("assets/boogie/big_demon_run_anim_f3.png"),
]


zombie_idle = [
    pygame.image.load("assets/zombie/big_zombie_idle_anim_f0.png"),
    pygame.image.load("assets/zombie/big_zombie_idle_anim_f1.png"),
    pygame.image.load("assets/zombie/big_zombie_idle_anim_f2.png"),
    pygame.image.load("assets/zombie/big_zombie_idle_anim_f3.png"),
]

zombie_run = [
    pygame.image.load("assets/zombie/swampy_anim_f0.png"),
    pygame.image.load("assets/zombie/swampy_anim_f1.png"),
    pygame.image.load("assets/zombie/swampy_anim_f2.png"),
    pygame.image.load("assets/zombie/swampy_anim_f3.png"),
]

walker_idle = [
    pygame.image.load("assets/walker/pumpkin_dude_idle_f0.png"),
    pygame.image.load("assets/walker/pumpkin_dude_idle_f1.png"),
    pygame.image.load("assets/walker/pumpkin_dude_idle_f2.png"),
    pygame.image.load("assets/walker/pumpkin_dude_idle_f3.png"),
]

walker_run = [
    pygame.image.load("assets/walker/pumpkin_dude_run_f0.png"),
    pygame.image.load("assets/walker/pumpkin_dude_run_f1.png"),
    pygame.image.load("assets/walker/pumpkin_dude_run_f2.png"),
    pygame.image.load("assets/walker/pumpkin_dude_run_f3.png"),
]

key_images = [
    pygame.image.load("assets/keys/button_blue_down.png"),
    pygame.image.load("assets/keys/button_blue_up.png"),
    pygame.image.load("assets/keys/button_red_up.png"),
    pygame.image.load("assets/keys/button_red_down.png"),
]

door_images = [
    pygame.image.load("assets/door/doors_leaf_closed.png"),
    pygame.image.load("assets/door/doors_leaf_open.png")
]