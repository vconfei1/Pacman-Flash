## Almanzi, Nicholas | Lehmann, Margaret | Nuebel, Ryan | Confeiteiro, Victoria
## CS110 A53, A51, A53, A52
## Project#1

import pygame
import sys
from pygame.locals import *

class Pellets(pygame.sprite.Sprite):
 
    def __init__(self, color = '', width = '', height = ''):
        pygame.sprite.Sprite.__init__(self)
        self.__color = color
        self.__width = width
        self.__height = height

        #http://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill
        #object that represents images
        self.image = pygame.Surface([int(self.__width),\
                                       int(self.__height)])
        #http://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill
        #fills a surface with a solid color
        self.image.fill(self.__color)
        self.rect = self.image.get_rect()

    ## Narrative: Set a value to color
    ## Preconditions: Passed in value
    ## Post conditions: Set a value to color
    def setColor(self, color):
        self.__color = color

    ## Narrative: Returns back value color
    ## Preconditions: Must be called
    ## Post conditions: Returns back value color
    def getColor(self):
        return(self.__color)

    ## Narrative: Set a value to width
    ## Preconditions: Passed in value
    ## Post conditions: Set a value to width
    def setWidth(self, width):
        self.__width = width

    ## Narrative: Returns back value width
    ## Preconditions: Must be called
    ## Post conditions: Returns back value width
    def getWidth(self):
        return(self.__width)

    ## Narrative: Set a value to height
    ## Preconditions: Passed in value
    ## Post conditions: Set a value to height
    def setHeight(self, height):
        self.__height = height

    ## Narrative: Returns back value height
    ## Preconditions: Must be called
    ## Post conditions: Returns back value height
    def getHeight(self):
        return(self.__height)

    def __str__(self):
        return("Color: " + str(self.__color) +\
               "\nWidth: " + str(self.__width) +\
               "\nHeight: " + str(self.__height))
