## Almanzi, Nicholas | Lehmann, Margaret | Nuebel, Ryan | Confeiteiro, Victoria
## CS110 A53, A51, A53, A52
## Project#1

import pygame
import sys
from pygame.locals import *

class Walls(pygame.sprite.Sprite):
    
    def __init__(self,x = '',y = ''):
        pygame.sprite.Sprite.__init__(self)
        self.__x = x
        self.__y = y
        self.image = pygame.image.load("block.png")
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

    def __str__(self):
        return(self.__x + ',' + self.__y)
