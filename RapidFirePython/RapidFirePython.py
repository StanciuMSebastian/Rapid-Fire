import pygame, sys
from random import *

seed(randint(0,randint(1,100)))

# pygame library initialization
pygame.init()

keys=pygame.key.get_pressed()

# screen initialization
displayWidth = 800
displayHeight = 600
screen = pygame.display.set_mode((displayWidth, displayHeight))

lives = 5
gameState = 'mainMenu'

# makes mouse invisible
pygame.mouse.set_visible( False ) 

# window title and icon
pygame.display.set_caption('Rapid Fire')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# backgound
backgroundImg = pygame.image.load('background.png')

# target
targetImg = pygame.image.load('target.png')
targetX = [randint(0,600),randint(0,600),randint(0,600),randint(0,600),randint(0,600),randint(0,600)]
targetY = [600,600,600,0,0,0]
targetSpeedX = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
targetSpeedY = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

def target(x, y):
    screen.blit(targetImg, (x, y))
    
# cursor
cursorImg = pygame.image.load('cursor.png')

def cursor(x, y):
    screen.blit(cursorImg, (x, y))
    x = (displayWidth * 0.45)
    y = (displayHeight * 0.8)

# game window loop
running = True
while running:
    #screen background
    screen.fill((255, 255, 255))

    screen.blit(backgroundImg, (0, 0))

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    if gameState is 'mainMenu':
        startGameText = myfont.render("Start Game", False, (0, 0, 0))
        screen.blit(startGameText, (340, 200))
        pos = pygame.mouse.get_pos()
        screen.blit(cursorImg, (pos[0],pos[1]))

        pygame.display.update()

    else:
        # efectiv scris pe ecran
        livesText = myfont.render(str(lives) + ' LIVES', False, (0, 0, 0))
        screen.blit(livesText,(0,0))


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                 keys = pygame.key.get_pressed()
            if event.type == pygame.MOUSEBUTTONUP:
                lives -= 1
                if lives == 0:
                    running = False
            if event.type == pygame.mouse.get_pos:
                print(event)

        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            running = False
    
    

        i=0
        while i <= 5:
            target(targetX[i], targetY[i])
            targetY[i] -= targetSpeedY[i]
            targetX[i] += targetSpeedX[i]

            if(randint(0,500) == 90):
                targetSpeedX[i] *= (-1)
            if(randint(0,600)==2):
                targetSpeedY[i] *= (-1)

            if(targetY[i] <= -64):
                targetY[i] = 664
            else:
                if(targetY[i] >= 664):
                     targetY[i] = -64

            if(targetX[i] <= -64):
                targetX[i] = 864
            else:
                if(targetX[i] >= 864):
                    targetX[i] = -64
            i += 1
    
    

    

    

