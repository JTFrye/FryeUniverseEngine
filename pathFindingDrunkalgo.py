import random


class levGen():
    def __init__(self, mapW, mapH, walkCount):

        #Map HW parameters
        self.mapW = mapW
        self.mapH = mapH
        #Character starting location, number of steps
        self.x = self.mapW // 2
        self.y = self.mapH //2
        self.walkCount = walkCount
        #DebugStuff
        self.debugLoga = []
        self.debugLogb = []

#Generates for of *
    def rowGen(self):
        return ['*'] * self.mapW

#Assembles rows into map
    def mapGen(self):
        self.fullMap = []
        for xer in range(self.mapH):
            self.fullMap.append(self.rowGen())


#Creates the X target on map
    def createTarget(self, targetX, targetY):
        self.targetX = targetX
        self.targetY = targetY
        self.fullMap[self.targetX][self.targetY] = 'X'

#Random number Gen
    def randNumGen(self):
        self.ranNum = random.randint(1,4)

        
#****************************Algo
#The drunken walk Algo
        
    def drunkWalk(self):
        
#Walk loop begin
        while self.walkCount > 0:

            
#replaces * with _ where character walked, count step
            if self.fullMap[self.y][self.x] == '*':
                self.fullMap[self.y][self.x] = 'O'
                self.walkCount -= 1
            elif self.fullMap[self.y][self.x] == 'X':
                print('target HIT')
                print(self.walkCount)
                break

            
#Randomizes num 1-4
            self.randNumGen()
#Walks
            if self.ranNum == 1 and self.x < self.mapW - 3:
                self.x += 1
            if self.ranNum == 2 and self.x > 3:
                self.x -= 1 
            if self.ranNum == 3 and self.y < self.mapH - 3:
                self.y += 1
            if self.ranNum == 4 and self.y > 3:
                self.y -= 1


#*******************
        
#prints results            
    def printResults(self):
        for dexer in self.fullMap:
            print( ' '.join(dexer))

#Emergency Debug Stuff
    def debugL(self):
        print('******XXXXXXXX******\n' * 3)
        print(self.debugLoga)
        print('******YYYYYYYYYY******\n' * 3)
        print(self.debugLogb)


if __name__ == '__main__':
    qorgi = levGen(55, 35, 600)
    qorgi.mapGen()
    qorgi.createTarget(4,41)
    qorgi.drunkWalk() #runs drunk algo
    qorgi.printResults()
   
