import tkinter as tk
import pygame

clock = pygame.time.Clock()

pygame.init()
root = tk.Tk()

display_width = 618    # root.winfo_screenwidth()
display_height = 359    # root.winfo_screenheight() - 50

gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)
pygame.display.set_caption('Project')

background = pygame.image.load('images/background.png').convert()

walk_right = [
    pygame.image.load('images/priv/walk_right1.png').convert_alpha(),
    pygame.image.load('images/priv/walk_right2.png').convert_alpha(),
    pygame.image.load('images/priv/walk_right3.png').convert_alpha(),
    pygame.image.load('images/priv/walk_right4.png').convert_alpha(),
]

walk_left = [
    pygame.image.load('images/priv/walk_left1.png').convert_alpha(),
    pygame.image.load('images/priv/walk_left2.png').convert_alpha(),
    pygame.image.load('images/priv/walk_left3.png').convert_alpha(),
    pygame.image.load('images/priv/walk_left4.png').convert_alpha(),
]

ghost_list = [

]
player_anim_count = 0
bg_x = 0

player_speed = 10
player_x = 150
player_y = 250

is_jump = False
jump_count = 9

ghost = pygame.image.load('images/ghost.png').convert_alpha()

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 3000)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == ghost_timer:
            ghost_list.append(ghost.get_rect(topleft=(620, 250)))

    background_ch = pygame.transform.scale(background, gameDisplay.get_size())

    gameDisplay.blit(background_ch, (bg_x, 0))
    gameDisplay.blit(background_ch, (bg_x + 618, 0))

    player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))

    if ghost_list:
        for el in ghost_list:
            gameDisplay.blit(ghost, el)
            el.x -= 5

            if player_rect.colliderect(el):
                player_x = 150

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        gameDisplay.blit(walk_left[player_anim_count], (player_x, player_y))
    else:
        gameDisplay.blit(walk_right[player_anim_count], (player_x, player_y))

    if keys[pygame.K_a] and player_x > 50:
        player_x -= player_speed
    elif keys[pygame.K_d] and player_x < 600:
        player_x += player_speed

    if not is_jump:
        if keys[pygame.K_w]:
            is_jump = True
    else:
        if jump_count >= -9:
            if jump_count > 0:
                player_y -= (jump_count ** 2) // 3
            else:
                player_y += (jump_count ** 2) // 3
            jump_count -= 1
        else:
            jump_count = 9
            is_jump = False

    bg_x -= 2
    if bg_x == -618:
        bg_x = 0

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    pygame.display.flip()

    clock.tick(15)