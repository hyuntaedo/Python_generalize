from types import MappingProxyType
import pygame

#initialize
pygame.init()

#Game_screen
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#game_Background
background = pygame.image.load("pyGame/background.png") 

#Game_Charactor load
character = pygame.image.load("pyGame/character.png")

#image size load
character_size = character.get_rect().size
character_width = character_size[0] #가로크기
character_height = character_size[1] #세로크기

#character_move
character_x_position = (screen_width /2) - (character_width/2) #가로위치
character_y_position = screen_height - character_height #세로위치

#move_좌표
to_x = 0
to_y = 0

#Game_title
pygame.display.set_caption("GameName")

#event roof
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 1
            elif event.key == pygame.K_RIGHT:
                to_x += 1
            elif event.key == pygame.K_UP:
                to_y -= 1
            elif event.key == pygame.K_DOWN:
                to_y += 1
        if event.type == pygame.KEYUP: #방향키를 뗏을때
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x =0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y =0

    character_x_position += to_x
    character_y_position += to_y

    #캐릭터가 화면 좌표 밖을 벗어난다면
    
    #가로처리
    if character_x_position <0:
        character_x_position = 0
    elif character_x_position > screen_width - character_width:
        character_x_position = screen_width - character_width
    #세로처리
    if character_y_position <0:
        character_y_position =0
    elif character_y_position >screen_height - character_height:
        character_y_position = screen_height - character_height
    
    #배경 좌표설정
    screen.blit(background,(0,0)) #좌표설정
    screen.blit(character,(character_x_position,character_y_position))
    pygame.display.update()


pygame.quit()

         
        


