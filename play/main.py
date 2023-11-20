from curses.panel import bottom_panel
import pygame
from sys import exit
import movement



from sqlalchemy import false


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Not Hypixel Skyblock')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

#Create textures#
sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png') .convert()
score_surface = test_font.render('My Game', False, (64, 64, 64))
score_rect = score_surface.get_rect(center=(400, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()

snail_rectangle = snail_surface.get_rect(midbottom=(600, 300))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80, 300))

#Main variables#
jump_cooldown = 0
jump_counter = 0
player_current_surface = 0
change_cooldown = 0
#BG MUSIC#
pygame.mixer.music.load('audio/music.wav')
pygame.mixer.music.play(-1)
#SOUNDS#
jump_sound = pygame.mixer.Sound('audio/jump.mp3')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    

    keys = pygame.key.get_pressed()


    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))

    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10 )

    screen.blit(score_surface, (score_rect))
    screen.blit(snail_surface, snail_rectangle)
    snail_rectangle.x -= 2
    
    if snail_rectangle.right < 0:
        snail_rectangle.left = 800
    screen.blit(player_surface, player_rectangle)


# JUMP#
    
    
        
#MOVEMENT#
    if keys[pygame.K_d] and player_rectangle.right < 800:
        player_rectangle.x += 5
        if player_current_surface == 0 and change_cooldown == 0:
            player_current_surface = 1
            change_cooldown = 2
        if player_current_surface == 1 and change_cooldown == 0:
            player_current_surface = 2
            change_cooldown = 2
        if change_cooldown > 0:
            change_cooldown -= 1


    if keys[pygame.K_a] and player_rectangle.left > 0:
        player_rectangle.x -= 5
    
    if snail_rectangle.collidedict:
        player_rectangle.x = 400

#TEXTURE RENDERER#
#PLAYER#
    if player_current_surface == 0:
        player_surface = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()

    if player_current_surface == -1:
        player_surface = pygame.image.load('graphics/Player/jump.png').convert_alpha()

    if player_current_surface == 1:
        player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()

    if player_current_surface == 2:
        player_surface = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
#SNAIL#        
    

    pygame.display.update()
    clock.tick(60)
       
