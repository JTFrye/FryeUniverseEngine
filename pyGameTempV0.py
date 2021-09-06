import pygame
import time
from pygame.locals import *

#Sets up Game
class initializePyGame():
    def __init__(self):
        pygame.init()
        self.crashed = False

#Generic colors we can call
    def basicColorInit(self):

        self.black = (0,0,0)
        self.white = (255,255,255)
        self.red = (255,0,0)
        self.green = (0,255,0)
        self.blue = (0,0,255)

#display settings
    def displaySet(self):
        
        self.display_width = 800
        self.display_height = 600
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        self.clock = pygame.time.Clock()
        self.clock.tick(60)

#how to create some basic shapes and variables
    def initializePrimitive(self):
        #drawLine
        pygame.draw.line(self.gameDisplay, self.blue, (100, 200), (300, 450), 5)
        #draw rectangle
        pygame.draw.rect(self.gameDisplay, self.red, (400, 400, 50, 25))
        #draw circle
        pygame.draw.circle(self.gameDisplay, self.white, (150, 150), 75)
        #polygon
        pygame.draw.polygon(self.gameDisplay, self.green, ((25,75),(76,125),(250,375)))
        self.drawY1Val = 300
        self.drawY2Val = 325

#animates a line
    def animatePrimitive(self, xIn, yIn):
        xIn = xIn
        yIn = yIn
        x1 = 500
        self.drawY1Val += yIn
        self.drawY2Val += -yIn
        for xed in range(10):
            pygame.draw.line(self.gameDisplay, self.blue, (x1, self.drawY1Val), (x1, self.drawY2Val), 10)

#Draw individual pixels. May 'lock screen' preventing drawText from being used
    def pixArrDraw(self):
        #Changes single pixel
        pixAr = pygame.PixelArray(gameDisplay)
        pixAr[10][20] = green

#Throws text boxes on screen
    def drawText(self, x, y, zed):
        mahFont = pygame.font.Font('freesansbold.ttf', 32)
        displayVal = mahFont.render('This is mah texter thing', True, self.blue)
        self.gameDisplay.blit(displayVal, (x, y))
        displayVal = mahFont.render('Moe Text', True, self.blue)
        self.gameDisplay.blit(displayVal, (x + 200, y + 200))
        displayVal = mahFont.render(zed, True, self.blue)
        self.gameDisplay.blit(displayVal, (x + 400, y + 400))



#starts main loop, checks keyboard
    def startLooper(self):
        while not self.crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                    pygame.quit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        print('a pressed and working')
                    if event.key == pygame.K_d:
                        x_move = -0.3
                    if event.key == pygame.K_w:
                        y_move = 0.3
                    if event.key == pygame.K_s:
                        y_move = -0.3

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        x_move = 0
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        y_move = 0

                #OpenGL reference
                #if event.key == pygame.K_e:
                  #  glTranslatef(0, 0, 1)
                #if event.key == pygame.K_r:
                  #  glTranslatef(0, 0, -1)

            self.animatePrimitive(1, 1)
            self.drawText(50, 50, 'This has been passed in')
            pygame.display.update()           #pygame.display.flip() Also works
        pygame.quit()


if __name__ == '__main__':
    print('mnr')
    qorgi = initializePyGame()
    qorgi.basicColorInit()
    qorgi.displaySet()
    qorgi.initializePrimitive()
    qorgi.startLooper()
