## Almanzi, Nicholas | Lehmann, Margaret | Nuebel, Ryan | Confeiteiro, Victoria
## CS110 A53, A51, A53, A52
## Project#1

import pygame
import sys
from pygame.locals import *
from tkinter import*
import random
from Pacman import*
from Pellets import*
from Walls import*
from Ghosts import*

# https://www.youtube.com/watch?v=Y7joZ67mC6o&index=1&\
# list=PLQVvvaa0QuDcxG_Cajz1JyTH6eAvka93C
# ^this is a link to a video in a series on videos we watched to get a basic
# understanding of pygame

# initializes pygame
pygame.init()


clock = pygame.time.Clock() # sets variable to Clock class
window = pygame.display.set_mode((456, 504)) # size of window
                                             #http://www.pygame.org/docs/ref/dis
                                             # play.html
pygame.display.set_caption("Pacman Flash") # title of window

# got colors from paint
black = (0,0,0)
white = (255,255,255)
         
class GUI(Frame):
    def __init__(self):

        # creates window
        self.__startWindow = Tk()
        self.__startWindow.title("Pacman")

        # creates top and bottom frame
        self.__topFrame = Frame()
        self.__bottomFrame = Frame()

        # places image in top frame 
        self.__image = PhotoImage(file = "pac1.gif")
        self.__imageLabel = Label(self.__topFrame, image = self.__image)

        # places start/exit buttons in bottom frame 
        self.__startButton = Button(self.__bottomFrame, \
                                    text="Start Game!", \
                                    command=self.__doThese)

        self.__exitButton = Button(self.__bottomFrame, \
                                  text="Exit", \
                                  command=self.__quit) 
                                  
        # packs everything
        self.__imageLabel.pack()
        self.__startButton.pack(side="left")
        self.__exitButton.pack(side="right")
        self.__topFrame.pack()
        self.__bottomFrame.pack() 

        mainloop()

    def __quit(self):
        # Closes start window
        self.__startWindow.withdraw()
        # http://www.pygame.org/docs/ref/pygame.html#pygame.quit
        # uninitializes all pygame modules
        pygame.quit()
        # python interpreter exits
        sys.exit()

    def __doThese(self):
        # Closes start window
        # Found the .withdraw() here:
        # http://www.blog.pythonlibrary.org/2012/07/26/
        # tkinter-how-to-show-hide-a-window/
        self.__startWindow.withdraw()
        # Runs game
        self.__runGame()
        
    def __runGame(self):
        self.__openingTheme = pygame.mixer.Sound('pacman_beginning.wav')
        self.__openingTheme.play()
        #plays intro music
        #http://www.pygame.org/docs/ref/mixer.html

        self.__pelletList = pygame.sprite.Group()
        self.__allSprites = pygame.sprite.Group()
        self.__wallList = pygame.sprite.Group()
        self.__ghostsList = pygame.sprite.Group()
        #In pygame, Group is a class containing objects created by the Sprite
        #class
        #http://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group

        #creates an instance of the pacman sprite
        self.__direction = "right"
        self.__pacman = Pacman(self.__direction, 216, 216, window)
        #http://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.add
        #adds a sprite to a group
        self.__allSprites.add(self.__pacman)

        #initializes all variables
        self.__moveX = 0
        self.__moveY = 0
        self.__score = 0
        self.__compare = 0
        self.__changeGhost = 0
        self.__die = 0
        self.__timeDelay = 0


        # creates the walls
        self.__wallX1 = [#row1
                         0,24,48,72,96,120,144,168,192,216,240,264,288,312,
                         336,360,384,408,432,\
                         #row2
                         0,216,432,\
                         #row3
                         0,48,72,96,144,168,216,264,288,336,360,384,432,\
                         #row4
                         0,432,\
                         #row5
                         0,24,72,120,168,192,216,240,264,312,360,408,432,\
                         #row6
                         0,120,216,312,432,\
                         #row7
                         0,24,48,72,120,192,240,312,360,384,408,432,\
                         #row8
                         0,24,48,72,120,312,360,384,408,432,\
                         #row9
                         0,24,48,72,120,168,192,240,264,312,360,384,408,432,\
                         #row10
                         0,168,264,432,\
                         #row11
                         0,48,72,120,168,192,216,240,264,312,360,384,432,\
                         #row12
                         0,48,72,360,384,432,\
                         #row13
                         0,48,72,120,168,192,216,240,264,312,360,384,432,\
                         #row14
                         0,216,432,\
                         #row15
                         0,48,72,120,144,168,216,264,288,312,360,384,432,\
                         #row16
                         0,72,360,432,\
                         #row17
                         0,24,72,120,168,192,216,240,264,312,360,408,432,\
                         #row18
                         0,120,216,312,432,\
                         #row19
                         0,48,96,120,144,168,264,288,312,336,384,432,\
                         #row20
                         0,432,
                         #row21
                         0,24,48,72,96,120,144,168,192,216,240,264,288,312,\
                         336,360,384,408,432]

        self.__wallY1 = [#row1
                         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                         #row2
                         24,24,24,
                         #row3
                         48,48,48,48,48,48,48,48,48,48,48,48,48,
                         #row4
                         72,72,
                         #row5
                         96,96,96,96,96,96,96,96,96,96,96,96,96,
                         #row6
                         120,120,120,120,120,
                         #row7
                         144,144,144,144,144,144,144,144,144,144,144,144,
                         #row8
                         168,168,168,168,168,168,168,168,168,168,
                         #row9
                         192,192,192,192,192,192,192,192,192,192,192,192,192,192,
                         #row10
                         216,216,216,216,
                         #row11
                         240,240,240,240,240,240,240,240,240,240,240,240,240,
                         #row12
                         264,264,264,264,264,264,
                         #row13
                         288,288,288,288,288,288,288,288,288,288,288,288,288,
                         #row14
                         312,312,312,
                         #row15
                         336,336,336,336,336,336,336,336,336,336,336,336,336,
                         #row16
                         360,360,360,360,
                         #row17
                         384,384,384,384,384,384,384,384,384,384,384,384,384,
                         #row18
                         408,408,408,408,408,
                         #row19
                         432,432,432,432,432,432,432,432,432,432,432,432,
                         #row20
                         456,456,
                         #row21
                         480,480,480,480,480,480,480,480,480,480,480,480,480,480,480,480,480,
                         480,480]
        #goes through wall coordinate lists and spawns each square wall
        for i in range(len(self.__wallX1)):
            self.__wall = Walls(self.__wallX1[i],self.__wallY1[i])
            self.__wallList.add(self.__wall)



        #creates the pellets
        # X-coordinates for the pellets
        self.__x1 = [#row1
                     36,60,84,108,132,156,180,204,252,276,300,\
                     324,348,372,396,420,\
                     #row2
                     36,132,204,252,324,420,\
                     #row3
                     36,60,84,108,132,156,180,204,228,252,276,300,\
                     324,348,372,396,420,\
                     #row4
                     60,108,156,300,348,396,\
                     #row5
                     36,60,84,108,156,180,204,252,276,300,348,372,396,420,\
                     #row6
                     108,156,180,228,276,300,348,\
                     #row7
                     108,156,180,204,228,252,276,300,348,\
                     #row8
                     108,156,300,348,\
                     #row9
                     36,60,84,108,132,156,300,324,348,372,396,420,\
                     #row10
                     36,108,156,300,348,420,\
                     #row11
                     36,108,132,156,180,204,228,252,276,300,324,348,420,\
                     #row12
                     36,108,156,300,348,420,\
                     #row13
                     36,60,84,108,132,156,180,204,252,276,300,324,348,372,\
                     396,420,\
                     #row14
                     36,108,204,252,348,420,\
                     #row15
                     36,60,108,132,156,180,204,228,252,276,300,324,348,396,420,\
                     #row16
                     60,108,156,300,348,396,\
                     #row17
                     36,60,84,108,156,180,204,252,276,300,348,372,396,420,\
                     #row18
                     36,84,204,228,252,372,420,\
                     #row19
                     36,60,84,108,132,156,180,204,228,252,276,300,324,348,\
                     372,396,420]

        # Y-cooridnates for the pellets
        self.__y1 = [#row1
                     36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,\
                     #row2
                     60,60,60,60,60,60,\
                     #row3
                     84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,\
                     #row4
                     108,108,108,108,108,108,\
                     #row5
                     132,132,132,132,132,132,132,132,132,132,132,132,132,132,\
                     #row6
                     156,156,156,156,156,156,156,\
                     #row7
                     180,180,180,180,180,180,180,180,180,\
                     #row8
                     204,204,204,204,\
                     #row9
                     228,228,228,228,228,228,228,228,228,228,228,228,\
                     #row10
                     252,252,252,252,252,252,\
                     #row11
                     276,276,276,276,276,276,276,276,276,276,276,276,276,\
                     #row12
                     300,300,300,300,300,300,\
                     #row13
                     324,324,324,324,324,324,324,324,324,324,324,324,324,324,\
                     324,324,\
                     #row14
                     348,348,348,348,348,348,\
                     #row15
                     372,372,372,372,372,372,372,372,372,372,372,372,372,\
                     372,372,\
                     #row16
                     396,396,396,396,396,396,\
                     #row17
                     420,420,420,420,420,420,420,420,420,420,420,420,420,420,\
                     #row18
                     444,444,444,444,444,444,444,\
                     #row19
                     468,468,468,468,468,468,468,468,468,\
                     468,468,468,468,468,468,468,468]
        
        #goes through pellet coordinate lists and spawns each pellet          
        for i in range(len(self.__x1)):
            self.__pellet = Pellets(white, 5, 5)
            self.__pellet.rect.x = self.__x1[i]
            self.__pellet.rect.y = self.__y1[i]
            self.__pelletList.add(self.__pellet)
            self.__allSprites.add(self.__pellet)



        # creates an instance of each ghost
        self.__victoria = Ghosts("victoria.png",0,0, window)
        self.__margie = Ghosts("margie.png",408,0, window)
        self.__nick = Ghosts("nick.png",0,456, window)
        self.__ryan = Ghosts("ryan.png",408,456, window)

        #adds each ghost to ghost list
        self.__ghostsList.add(self.__victoria)
        self.__ghostsList.add(self.__margie)
        self.__ghostsList.add(self.__nick)
        self.__ghostsList.add(self.__ryan)

        #loop to run the game
        self.__gameLoop=True
        while self.__gameLoop == True:
            # http://www.pygame.org/docs/ref/event.html#pygame.event.get
            # gets event from the queue
            for event in pygame.event.get():
                if (event.type==pygame.QUIT):
                    gameLoop=False

                # http://www.pygame.org/docs/ref/key.html
                # checks the event type based on certain key presses
                elif (event.type==pygame.KEYDOWN):
                    if (event.key==pygame.K_LEFT):
                        self.__moveX = -1
                        self.__moveY = 0
                        self.__direction = "left"
                    elif (event.key==pygame.K_RIGHT):
                        self.__moveX = 1
                        self.__moveY = 0
                        self.__direction = "right"
                    elif (event.key==pygame.K_UP):
                        self.__moveX = 0
                        self.__moveY = -1
                        self.__direction = "up"
                    elif (event.key==pygame.K_DOWN):
                        self.__moveX = 0
                        self.__moveY = 1
                        self.__direction = "down"

                elif (event.type==pygame.KEYUP):
                    if (event.key==pygame.K_LEFT):
                        self.__moveX = 0
                        self.__moveY = 0
                        self.__direction = "left"
                    elif (event.key==pygame.K_RIGHT):
                        self.__moveX = 0
                        self.__moveY = 0
                        self.__direction = "right"
                    elif (event.key==pygame.K_UP):
                        self.__moveY = 0
                        self.__moveY = 0
                        self.__direction = "up"
                    elif (event.key==pygame.K_DOWN):
                        self.__moveY = 0
                        self.__moveY = 0
                        self.__direction = "down"

            window.fill(black)

            # gets x and y coords
            self.__x = self.__pacman.getX()

            self.__y = self.__pacman.getY()

            # sets x and y new coords 
            self.__pacman.setX(self.__x+self.__moveX)

            self.__pacman.setY(self.__y+self.__moveY)

            #http://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group.draw
            # sets rect values equal to pacman's new values
            self.__pacman.rect.x += self.__moveX

            self.__pacman.rect.y += self.__moveY

            # draws the pellets
            self.__pelletList.draw(window)

            # draws the walls
            self.__wallList.draw(window)

            # has the ghosts chnage position every 50 loops of the game
            if self.__changeGhost%50 == 0:
            #Victoria
                #gives the new x-values a random number
                self.__victX = random.randint(0,408)

                #gives the new y-values a random number
                self.__victY = random.randint(0,456)

                #sets the new x-value in ghost the class
                self.__victoria.setX(self.__victX)

                #sets the new y-value in ghost the class
                self.__victoria.setY(self.__victY)

                #changes the rect's x and y to equal the ghosts
                self.__victoria.rect.x = self.__victX

                self.__victoria.rect.y = self.__victY

                #Margie

                self.__margX = random.randint(0,408)

                self.__margY = random.randint(0,456)

                self.__margie.setX(self.__margX)

                self.__margie.setY(self.__margY)

                self.__margie.rect.x = self.__margX

                self.__margie.rect.y = self.__margY

                #Nick

                self.__nickX = random.randint(0,408)

                self.__nickY = random.randint(0,456)

                self.__nick.setX(self.__nickX)

                self.__nick.setY(self.__nickY)

                self.__nick.rect.x = self.__nickX

                self.__nick.rect.y = self.__nickY

                #Ryan

                self.__ryanX = random.randint(0,408)

                self.__ryanY = random.randint(0,456)

                self.__ryan.setX(self.__ryanX)

                self.__ryan.setY(self.__ryanY)

                self.__ryan.rect.x = self.__ryanX

                self.__ryan.rect.y = self.__ryanY

                # renders the ghosts
                self.__victoria.flip()
                self.__margie.flip()
                self.__nick.flip()
                self.__ryan.flip()


            # draws the ghosts in the same spot everytime the changeGhost
            # is not a multiple of 50
            else:
                self.__victoria.flip()
                self.__margie.flip()
                self.__nick.flip()
                self.__ryan.flip()

            # adds 1 each loop so that it knows when the loop is a multiple
            # of 50
            self.__changeGhost += 1

            #http://www.pygame.org/docs/ref/sprite.html\
            ##pygame.sprite.spritecollide
            # Collision detection for the Pellets and deletes the pellet
            self.__pelletHitList = pygame.sprite.\
                                   spritecollide(self.__pacman,\
                                                 self.__pelletList, True)
            #adds 1 to the score each time  there is a pellet collision
            for self.__pellet in self.__pelletHitList:
                self.__score += 1

            # if all dots are eaten displays the win screen
            if self.__score == 197:
                self.__winScreen()

            # collision detection for the ghosts and pacman
            self.__ghostHitList = pygame.sprite.\
                                   spritecollide(self.__pacman,\
                                                 self.__ghostsList, True)

            # add 1 to die if ghostHitList goes up
            for self.__ghost in self.__ghostHitList:
                self.__die += 1

            # checks if ghost hit list is more than 1
            if self.__die > 0:
                #allows for a 50 frame delay so the ghost collision is visible
                if self.__timeDelay == 50:
                    self.__loseScreen(self.__score)
                # once a ghost hit this goes up so on the next loop the lose
                # screen will display
                self.__timeDelay += 50

            # collision detection for walls
            self.__collided = pygame.sprite.spritecollide(self.__pacman,\
                                                          self.__wallList,\
                                                          False)
            # if there is a wall collision occurs runs
            if self.__compare < len(self.__collided):
                # if moving right and hits wall, everything will change to
                # equal the left conditions
                if self.__direction == "right":
                    self.__moveX = -1
                    self.__moveY = 0
                    self.__direction = "left"
                elif self.__direction == "left":
                    self.__moveX = 1
                    self.__moveY = 0
                    self.__direction = "right"
                elif self.__direction == "down":
                    self.__moveY = 0
                    self.__moveY = -1
                    self.__direction = "up"
                elif self.__direction == "up":
                    self.__moveY = 0
                    self.__moveY = 1
                    self.__direction = "down"

            # sets direction in Pacman class
            self.__pacman.setDirection(self.__direction)

            # updates pacman
            self.__pacman.flip()

            # 60 frames per second
            clock.tick(60)

            # updates the display
            pygame.display.update()

    ## Narrative: displays message box for winner
    ## Preconditions: must be called
    ## Post conditions: displays message box for winner
    def __winScreen(self):
        messagebox.showinfo("Winner","YOU WIN!!!")
        pygame.quit()
        sys.exit()

    ## Narrative: displays loser message box
    ## Preconditions: Passed in value for score
    ## Post conditions: displays loser message box
    def __loseScreen(self,score):
        self.__score = score
        messagebox.showinfo("Loser","You lose..." + \
                            "\nYour score is: " + str(self.__score))
        pygame.quit()
        sys.exit()
