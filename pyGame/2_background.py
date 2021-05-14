import pygame

#initialize
pygame.init()

#Game_screen
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#game_Background
background = pygame.image.load("pyGame/background.png") 

#Game_title
pygame.display.set_caption("GameName")

#event roof
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background,(0,0)) #좌표설정
    pygame.display.update()


pygame.quit()

         
        


