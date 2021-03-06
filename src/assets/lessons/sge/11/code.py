from cira.ciragame import *
# this is a comment
class MyGame(CiraGame):
    # engine variables
    title = "Quick Start"

    # These are the variables for my "player" pixel
    x = 9
    y = 11
    red = 0
    green = 0
    blue = 255

    # These are the variables for my "chaser" pixel
    cpuX=0
    cpuY=0
    cpuRed=255
    cpuGreen=0
    cpuBlue=0

    speed = 10
    turn = 0
    speedUp = 0

    #Game over?
    gameOver = False
    messagePrinted = False

    # called once when the program starts up
    def awake(self):
        pass

    # called at the beginning of each play session
    def start(self):
        if self.gameOver:
            # These are the variables for my "player" pixel
            self.x = 9
            self.y = 11
            self.red = 0
            self.green = 0
            self.blue = 255

            # These are the variables for my "chaser" pixel
            self.cpuX=0
            self.cpuY=0
            self.cpuRed=255
            self.cpuGreen=0
            self.cpuBlue=0

            self.speed = 10
            self.turn = 0
            self.speedUp = 0

            #Game over?
            self.gameOver = False
            self.messagePrinted = False

        pass

    # called each time the frame updates
    def update(self):
        if self.gameOver:
            return

        if cira.keys.getKey('1-Left'):
            if self.x>0:
                self.x-=1
        elif cira.keys.getKey('1-Right'):
            if self.x<19:
                self.x+=1
        elif cira.keys.getKey('1-Up'):
            if self.y>0:
                self.y-=1
        elif cira.keys.getKey('1-Down'):
            if self.y<22:
                self.y+=1

        #Add 1 to turn
        self.turn += 1

        #Divide the turn by the speed
        # if there's no remainder, then move the computer pixel
        if self.turn % self.speed == 0:

            #Speed up the computer every 5 times it moves
            self.speedUp += 1
            if self.speedUp == 5 and self.speed > 1:
                self.speedUp = 0
                self.speed -= 1

            # If the computer is to the left of the player, move right
            # or if the computer is to the right of the player, move left
            if self.cpuX<self.x:
                self.cpuX+=1
            elif self.cpuX>self.x:
                self.cpuX-=1

            #If the computer is above the player, move down. If the computer
            # is below the player, move up.
            if self.cpuY<self.y:
                self.cpuY+=1
            elif self.cpuY>self.y:
                self.cpuY-=1

        #Check to see if the player has been caught
        if self.x == self.cpuX and self.y == self.cpuY:
            self.gameOver = True
        pass

    # called when each frame needs to be drawn
    def draw(self):

        if self.gameOver:
            if self.messagePrinted == False:
                cira.display.clearScreen(255,255,255)
                print "Final speed: " + str(self.speed)
                print "Score: " + str(self.turn)
                self.messagePrinted = True
            else:
                self.start()
        else:
            cira.display.clearScreen(0,0,0)
            cira.display.putPixel(self.x,self.y,self.red,self.green,self.blue)
            cira.display.putPixel(self.cpuX,self.cpuY,self.cpuRed,self.cpuGreen,
                self.cpuBlue)
        return
