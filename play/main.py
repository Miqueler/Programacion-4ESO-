
import pygame
from sys import exit

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('33')
clock = pygame.time.Clock()
test_font = pygame.font.Font("play/font/Pixeltype.ttf", 50)

#Create textures#
sky_surface = pygame.image.load('play/graphics/sky.png').convert()
ground_surface = pygame.image.load('play/graphics/ground.png') .convert()
score_surface = test_font.render('My Game', False, (64, 64, 64))
score_rect = score_surface.get_rect(center=(400, 50))
game_over=test_font.render("Game Over!", False, (64,64,64))
game_over_rect=game_over.get_rect(center=(400,50))

snail_surface = pygame.image.load('play/graphics/snail/snail1.png').convert_alpha()

snail_rectangle = snail_surface.get_rect(midbottom=(600, 300))

player_surface = pygame.image.load('play/graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80, 300))

ground_rectangle= ground_surface.get_rect()

#Main variables#
jump_counter = 0
player_current_surface = 0
snail_texture_counter=0
loose=False
#BG MUSIC#
pygame.mixer.music.load('play/audio/music.wav')
pygame.mixer.music.play()
#SOUNDS#
jump_sound = pygame.mixer.Sound('play/audio/jump.mp3')

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
    if loose==False:
        screen.blit(score_surface, (score_rect))
    screen.blit(snail_surface, snail_rectangle)

    
    if snail_rectangle.right < 0:
        snail_rectangle.left = 800
    screen.blit(player_surface, player_rectangle)

    
# JUMP#
    if keys[pygame.K_SPACE] and jump_counter==0 and player_rectangle.bottom==300 and loose==False:
        jump_counter=15
        jump_sound.play()
    if jump_counter!=0 and loose==False:
        jump_counter-=1
        player_rectangle.bottom-=8
        player_current_surface=-1

    if player_rectangle.bottom>300:
        player_rectangle.bottom=300

    elif player_rectangle.bottom!=300 and jump_counter==0 and loose==False:
        player_rectangle.y+=5
#MOVEMENT#
    if keys[pygame.K_d] and player_rectangle.right < 800 and loose==False:
        player_rectangle.x += 5
        if jump_counter==0:
            player_current_surface=1
    
    if keys[pygame.K_a] and player_rectangle.left > 0 and loose==False:
        player_rectangle.x -= 5
        if jump_counter==0:
            player_current_surface=2
    
    if not keys[pygame.K_a] and not keys[pygame.K_d] and jump_counter==0 and loose==False:
        player_current_surface=0
#COLISIONS
    if pygame.Rect.colliderect(player_rectangle, snail_rectangle):
        screen.blit(game_over, (game_over_rect))
        loose=True




#TEXTURES:
#PLAYER#
    if player_current_surface == 0:
        player_surface = pygame.image.load('play/graphics/Player/player_stand.png').convert_alpha()

    if player_current_surface == -1:
        player_surface = pygame.image.load('play/graphics/Player/jump.png').convert_alpha()

    if player_current_surface == 1:
        player_surface = pygame.image.load('play/graphics/Player/player_walk_1.png').convert_alpha()

    if player_current_surface == 2:
        player_surface = pygame.image.load('play/graphics/Player/player_walk_2.png').convert_alpha()
#SNAIL#
        
    if snail_texture_counter==0 and loose==False:
        snail_texture_counter=28
        snail_surface = pygame.image.load("play/graphics/snail/snail1.png").convert_alpha()
    if snail_texture_counter==14 and loose==False:
        snail_surface = pygame.image.load("play/graphics/snail/snail2.png").convert_alpha()
        snail_rectangle.x-=20
    snail_texture_counter-=1


    pygame.display.update()
    clock.tick(60)