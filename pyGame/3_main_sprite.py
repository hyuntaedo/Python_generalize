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

#Game_title
pygame.display.set_caption("GameName")

#event roof
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background,(0,0)) #좌표설정
    screen.blit(character,(character_x_position,character_y_position))
    pygame.display.update()


pygame.quit()

         
        


