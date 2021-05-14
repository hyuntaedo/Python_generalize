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

#character_position
character_x_position = (screen_width /2) - (character_width/2) #가로위치
character_y_position = screen_height - character_height #세로위치

#move_좌표
to_x = 0
to_y = 0

#Game_title
pygame.display.set_caption("GameName")

#FPS
clock = pygame.time.Clock()

#char_speed
character_speed = 0.6

#enemy_load
enemy = pygame.image.load("pyGame/enemy.png")

#enemy character
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0] #가로크기
enemy_height = enemy_size[1] #세로크기

#enemy_move
enemy_x_position = (screen_width /2) - (enemy_width/2) #가로위치
enemy_y_position = (screen_height/2) - (enemy_height/2) #세로위치

# font definition
game_font = pygame.font.Font(None,40) #객체 생성(폰트,크기)

#총 시간
total_time = 10

#시작 시간
start_ticks = pygame.time.get_ticks() #시작 tick을 받아옴

#event roof
running = True

while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임수 설정
    #초당 프레임수 
    print("fps : " + str(clock.get_fps()))
    #10fps -> 1초동안 10번동작 -> 100이동하기위해서는 10번동작
    #20fps -> 1초동안 20번동작 -> 100이동하기위해서는 5번동작
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP: #방향키를 뗏을때
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x =0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y =0

    #위치 좌표(값을 dt값으로 보정함)
    character_x_position += to_x *dt
    character_y_position += to_y *dt

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



    #캐릭터 충돌처리
    character_rect = character.get_rect()
    character_rect.left = character_x_position #char정보 update
    character_rect.top = character_y_position        
    

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_position
    enemy_rect.top = enemy_y_position

    #충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌")
        running = False
    
    

    #배경 좌표설정
    screen.blit(background,(0,0)) #좌표설정
    screen.blit(enemy,(enemy_x_position,enemy_y_position))
    screen.blit(character,(character_x_position,character_y_position))
    
    #timer
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 
    #경과시간 '초(s)'로 환산
    timer = game_font.render(str(int(total_time-elapsed_time)),True,(255,255,255))
    #render(output_text,True,text_color)
    screen.blit(timer,(10,10))

    if total_time - elapsed_time <0:
        print("타임아웃")
        running = False
    
    pygame.display.update()

pygame.time.delay(2000)

#종료
pygame.quit()

         
        


