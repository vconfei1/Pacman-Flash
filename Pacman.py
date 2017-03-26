## Almanzi, Nicholas | Lehmann, Margaret | Nuebel, Ryan | Confeiteiro, Victoria
## CS110 A53, A51, A53, A52
## Project#1

import pygame
import sys
from pygame.locals import *

#In pygame, sprite is a module that deals with game objects and sprite.Sprite is
#a class for visual object sprites
class Pacman(pygame.sprite.Sprite):
 
    def __init__(self, direction = '', x = '', y = '', window = ''):
        pygame.sprite.Sprite.__init__(self)
        self.__x = x
        self.__y = y
        self.__direction = direction
        self.__window = window
        self.__i1r = pygame.image.load("p1right.png")
        self.__i1d = pygame.image.load("p1down.png")
        self.__i1l = pygame.image.load("p1left.png")
        self.__i1u = pygame.image.load("p1up.png")
        self.__i2 = pygame.image.load("p2.png")
        self.__timeTarget = 10
        self.__timeNum = 0
        self.__currentImage = 0
        #timeTarget, timeNum, and currentImage deal with Pacman's mouth opening
        #and closing. Explained further in mouth() function
        
        self.rect = self.__i2.get_rect()
        self.rect.x = x
        self.rect.y = y
        #.rect sets the dimensions of the sprite so spritecollide can detect when the rectangular hitbox around the sprites overlap
        #http://www.pygame.org/docs/ref/sprite.html

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

    ## Narrative: Returns back value y
    ## Preconditions: Must be called
    ## Post conditions: Returns back value y
    def setY(self, y):
        self.__y = y

    ## Narrative: Returns back value y
    ## Preconditions: Must be called
    ## Post conditions: Returns back value y
    def getY(self):
        return(self.__y)

    ## Narrative: Set a value to direction
    ## Preconditions: Passed in value
    ## Post conditions: Set a value to direction
    def setDirection(self, direction):
        self.__direction = direction

    ## Narrative: Returns back value direction
    ## Preconditions: Must be called
    ## Post conditions: Returns back value direction
    def getDirection(self):
        return(self.__direction)

    #Changes images between open and close mouth
    def flip(self):
        self.__timeNum+=1
        if (self.__timeNum==self.__timeTarget):
            if (self.__currentImage==0):
                self.__currentImage=1
            else:
                self.__currentImage=0
            self.__timeNum=0
        self.__render()
    #Every frame timeNum goes up 1 until it reaches 10. Once it reaches 10, the
    #currentImage changes in order to open/close Pacman's mouth, and timeNum
    #resets
    def __render(self):
        if (self.__currentImage==0):
            if self.__direction == "right":
                self.__window.blit(self.__i1r, (self.__x,self.__y))
            if self.__direction == "down":
                self.__window.blit(self.__i1d, (self.__x,self.__y))
            if self.__direction == "left":
                self.__window.blit(self.__i1l, (self.__x,self.__y))
            if self.__direction == "up":
                self.__window.blit(self.__i1u, (self.__x,self.__y))
    #Renders Pacman depending on which direction he is facing and whether his
    #mouth is open or closed 
        else:
            self.__window.blit(self.__i2, (self.__x,self.__y))
            #.blit displays an image on another image
            #http://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit

    def __str__(self):
        return("X: " + str(self.__x) +\
               "\nY: " + str(self.__y) +\
               "\nDirection: " + str(self.__direction))
