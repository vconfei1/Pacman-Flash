## Almanzi, Nicholas | Lehmann, Margaret | Nuebel, Ryan | Confeiteiro, Victoria
## CS110 A53, A51, A53, A52
## Project#1

import pygame
import sys
from pygame.locals import *

class Ghosts(pygame.sprite.Sprite):
 
    def __init__(self, ghost = '', x = '', y = '', window = ''):
        pygame.sprite.Sprite.__init__(self)
        self.__window = window
        self.__x = x
        self.__y = y
        self.__ghost = ghost
        self.image = pygame.image.load(self.__ghost)
        self.__timeTarget = 1
        self.__timeNum = 0
        self.__currentImage = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    ## Narrative: Set a value to x
    ## Preconditions: Passed in value
    ## Post conditions: Set a value to x
    def setX(self, x):
        self.__x = x

    ## Narrative: Returns back value x
    ## Preconditions: Must be called
    ## Post conditions: Returns back value x
    def getX(self):
        return(self.__x)

    ## Narrative: Set a value to y
    ## Preconditions: Passed in value
    ## Post conditions: Set a value to y 
    def setY(self, y):
        self.__y = y

    ## Narrative: Returns back value y
    ## Preconditions: Must be called
    ## Post conditions: Returns back value y
    def getY(self):
        return(self.__y)
    
    ## Narrative: Set a value to ghost
    ## Preconditions: Passed in value
    ## Post conditions: Set a value to ghost 
    def setGhost(self, ghost):
        self.__ghost = ghost

    ## Narrative: Returns back value ghost
    ## Preconditions: Must be called
    ## Post conditions: Returns back value ghost
    def getGhost(self):
        return(self.__ghost)

    # redraws ghosts every frame because timeTarget = 1
    def flip(self):
        self.__timeNum+=1
        if (self.__timeNum==self.__timeTarget):
            self.__render()
            self.__timeNum=0

    # draws the ghost
    def __render(self):
            self.__window.blit(self.image, (self.__x,self.__y))

    def __str__(self):
        return("X: " + str(self.__x) +\
               "\nY: " + str(self.__y) +\
               "\nGhost: " + str(self.image))
