import random
import math

class levGen():
    def __init__(self, mapW, mapH, x, y, walkCount):

        #Map HW parameters
        self.mapW = mapW
        self.mapH = mapH
        #Character starting location, number of steps
        self.x = x
        self.y = y
        self.walkCount = walkCount
        
#Generates for of *
    def rowGen(self):
        return ['*'] * self.mapW

#Assembles rows into map
    def mapGen(self):
        self.fullMap = []
        for xer in range(self.mapH):
            self.fullMap.append(self.rowGen())


#Creates the X target on map and writes the PlayerPos
    def createTarget(self, targetX, targetY):
        self.targetX = targetX
        self.targetY = targetY
        self.fullMap[self.targetX][self.targetY] = 'X'
        print(targetX, ' , ', targetY)
        self.fullMap[self.x][self.y] = '!'

#Random number Gen
    def randNumGen(self):
        self.ranNum = random.randint(1,4)

        
#****************************Algo
#The drunken walk Algo
        
    def drunkWalk(self):
        
#Walk loop begin
        while self.walkCount > 0:

            
#replaces * with _ where character walked, count step
            if self.fullMap[self.x][self.y] == '*':
                self.fullMap[self.x][self.y] = 'O'
                self.walkCount -= 1
            elif self.fullMap[self.x][self.y] == 'X':
                print('target HIT')
                print('Total Steps Left = ', self.walkCount)
                break

            
#Randomizes num 1-4
            self.randNumGen()
#Walks
            if self.ranNum == 1 and self.x < self.mapH - 3:
                self.x += 1
            if self.ranNum == 2 and self.x > 3:
                self.x -= 1 
            if self.ranNum == 3 and self.y < self.mapW - 3:
                self.y += 1
            if self.ranNum == 4 and self.y > 3:
                self.y -= 1


#*******************

    def vertexPath(self):
        
        while self.walkCount > 0:

            print(self.x, ' , ', self.y)
#replaces * with _ where character walked, count step
            if self.fullMap[self.x][self.y] == '*':
                self.fullMap[self.x][self.y] = 'O'
                self.walkCount -= 1
            elif self.fullMap[self.x][self.y] == 'X':
                print('target HIT')
                print(self.walkCount)
                self.walkCount = 0
                break
            
            findVertX = self.targetX - self.x
            findVertY = self.targetY - self.y
            vecL = math.sqrt(findVertX ** 2 + findVertY ** 2)
            unitLX = round(findVertX/vecL)
            unitLY = round(findVertY/vecL)
            self.y = self.y + unitLY
            self.x = self.x + unitLX
            #print(self.walkCount)
                    
#prints results            
    def printResults(self):
        for dexer in self.fullMap:
            print( ' '.join(dexer))

if __name__ == '__main__':
    qorgi = levGen(55, 35, 33, 3, 600)
    qorgi.mapGen()
    qorgi.createTarget(4,41)
    #qorgi.drunkWalk() #runs drunk algo
    qorgi.vertexPath()   #Direct path calc
    qorgi.printResults()
   
