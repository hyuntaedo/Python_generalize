import pygame
from random import *

from pygame.constants import K_LEFT, K_RIGHT
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#Background load
background = pygame.image.load("pyGame/background.png") 

#Game_Charactor load
character = pygame.image.load("pyGame/character.png")
enemy = pygame.image.load("pyGame/enemy.png")
#title
pygame.display.set_caption("Arrow Game")

#character
character_size = character.get_rect().size
character_width = character_size[0] #가로크기
character_height = character_size[1] #세로크기

#enemy
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]

#move_location
to_x = 0

#char_speed
character_speed = 1
enemy_speed = 0.3

#character_position
character_x_position = (screen_width /2) - (character_width/2) #가로위치
character_y_position = screen_height - character_height #세로위치
enemy_x_position = randint(0,screen_width- enemy_width) 
enemy_y_position = 0


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        if event.type == pygame.KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                to_x = 0


    if character_x_position <0:
        character_x_position = 0
    elif character_x_position > screen_width - character_width:
        character_x_position = screen_width - character_width 

    if enemy_y_position > screen_height:
        enemy_y_position = 0
        enemy_x_position = randint(0,screen_width-enemy_width)
    
    enemy_y_position += enemy_speed

    
    #character collision
    character_rect = character.get_rect()
    character_rect.left = character_x_position #char정보 update
    character_rect.top = character_y_position        
    
    #enemy collision
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_position
    enemy_rect.top = enemy_y_position

    #collision check
    if character_rect.colliderect(enemy_rect):
        print("충돌")
        running = False
    
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_position,character_y_position))
    screen.blit(enemy,(enemy_x_position,enemy_y_position))
    pygame.display.update()


pygame.quit()