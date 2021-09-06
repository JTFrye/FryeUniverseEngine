import math

Pai = math.pi

#Radian ranges from 0 to 2*Pi (6.28)
#XY, Rad initalized to 0, dirXY
class playerXY():
    def __init__(self, xPos = 10, yPos = 10, plAng = 0.0):
        self.xPos = xPos
        self.yPos = yPos
        self.plAng = plAng
        self.dirX = math.sin(self.plAng)
        self.dirY = math.cos(self.plAng)

    
    def moveXYwDir(self):
        self.xPos = self.xPos + self.dirX
        self.yPos = self.yPos + self.dirY
        print('X location : ', self.xPos)
        print('Y location : ', self.yPos)

    def xyDirCur(self):
        print('dirX = ', self.dirX)
        print('dirY = ', self.dirY)
   
    def rotateLeft(self, clicks = 25):
        for xed in range(clicks):
            if self.plAng > 6.18:
                self.plAng = 0
            elif self.plAng < 0:
                self.plAng = 6.18
            else:    
                self.plAng += 0.05
                self.dirX = math.sin(self.plAng)
                self.dirY = math.cos(self.plAng)
                

    def rotateRight(self, clicks = 25):
        for xed in range(clicks):
            if self.plAng > 6.18:
                self.plAng = 0
            elif self.plAng < 0.0:
                self.plAng = 6.18
            else:    
                self.plAng += -0.05
                self.dirX = math.sin(self.plAng)
                self.dirY = math.cos(self.plAng)

    def printSep(self):
        print('-------------------------------------------\n' * 3)
        
if __name__ == '__main__':
    boa = playerXY()
    boa.printSep()
    boa.moveXYwDir()
    boa.printSep()
    boa.xyDirCur()
    
#    boa.printSep() #Prints Lines in IDLE
#    boa.xyDirCur() #Current DirXY values
#    boa.moveXYwDir() # moves XY according to RADnDir
#    boa.rotateLeft() #tank controls yo
#    boa.rotateRight()  #gotta go both ways
