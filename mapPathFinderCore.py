import math

class mapPather():
    def __init__(self, walkCount = 500):
        #1 and 9 are to make sure printing out correctly
        self.pLoc = 'pLoc'
        self.tLoc = 'tLoc'
        
        self.yxMap = [['1',0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0,0,'9']]

        #YX & Target Values under pLoc and tLoc
        self.comDict = {}

        self.moveList = []
        
        self.walkCount = walkCount

#Prints Map
    def printMap(self):
        for xed in range(len(self.yxMap)):
            print(self.yxMap[xed])
        
#Finds a specific value and prints
    def printYX(self, yIn, xIn):
        yLoc = yIn
        xLoc = xIn
        print('specific values returned : ', self.yxMap[yIn][xIn])

#Formatting. Replace 0
    def reformZed(self, varIn):
        for xed in range(len(self.yxMap)):
            for yed in range(len(self.yxMap)):
                if self.yxMap[xed][yed] == 0:
                    self.yxMap[xed][yed] = varIn
        

#Mark X as player locale. 
    def playerLoc(self, yIn = 9, xIn = 5):
        if self.yxMap[yIn][xIn] == '0':
            self.yxMap[yIn][xIn] = 'X'
            self.comDict[self.pLoc] = [yIn, xIn]
            #Get val. self.comDict['pLoc][1] returns list xIn etc.

#Mark letter 'T' as target locale
    def targetLoc(self, yIn = 2, xIn = 8):
        if self.yxMap[yIn][xIn] == '0':
            self.yxMap[yIn][xIn] = 'T'
            self.comDict[self.tLoc] = [yIn, xIn]
#Finds a value among map
    def findVal(self, searchVal):
        for xed in range(len(self.yxMap)):
            for yed in range(len(self.yxMap)):
                if self.yxMap[xed][yed] == searchVal:
                    self.newVar = self.yxMap[xed][yed]
                    self.mapVal = (xed, yed)
                    return self.mapVal

    def retAll(self):
        print('Player YX : ', self.comDict[self.pLoc])
        print('Target YX : ', self.comDict[self.tLoc])


#Calculates a direct path and saves it to a list.
    def vertexDirect(self):
#Temporary YX values so we can calculate entire path before moving.        
        self.tempY = self.comDict[self.pLoc][0]
        self.tempX = self.comDict[self.pLoc][1]
        while self.walkCount > 0:
            if self.yxMap[self.comDict[self.pLoc][0]][self.comDict[self.pLoc][1]] == 'T':
                print('Target Struck')
            elif self.yxMap[self.tempY][self.tempX] == 'T':
                print('LIST OF REQUIRED MOVES CALCULATED')
                break
                
                
            self.walkCount -= 1

#Subtracts target location from current location(temp)
            self.vertY = self.comDict[self.tLoc][0] - self.tempY
            self.vertX = self.comDict[self.tLoc][1] - self.tempX
#Calculates length of hypot.                
            self.vectorLen = math.sqrt(self.vertY ** 2 + self.vertX ** 2)
#Converts to single unit length to move one unit at a time

#This confirms unit length = 1
            #unadjustedY = self.vertY/self.vectorLen
            #unadjustedX = self.vertX/self.vectorLen
            #print('raw YX : ', unadjustedY, ' , ',  unadjustedX)
            #print('totes unit length = ', unadjustedY ** 2 + unadjustedX ** 2)
            
            
            self.unitLenY = round(self.vertY/self.vectorLen)
            self.unitLenX = round(self.vertX/self.vectorLen)
#New current location(temp values)
            self.tempY = self.tempY + self.unitLenY
            self.tempX = self.tempX + self.unitLenX

#List of moves required to get to target
            self.moveList.append((self.unitLenY, self.unitLenX, self.walkCount))

            print('move Vals : ', self.tempY, self.tempX, self.walkCount)
#Parses and moves plocation
    def listParser(self):
        print('Values are (Y, X, total moves) : ', self.moveList)
        print('----------------------------------\n' * 3)
        for xed in range(len(self.moveList)):
            print('all YX values! : ', self.moveList[xed][0], ' , ', self.moveList[xed][1])
            self.comDict[self.pLoc][0] = self.comDict[self.pLoc][0] + self.moveList[xed][0]
            self.comDict[self.pLoc][1] = self.comDict[self.pLoc][1] + self.moveList[xed][1]
            #self.yxMap[self.comDict[self.pLoc][0]][self.comDict[self.pLoc][1]] = 'V'
            if self.yxMap[self.comDict[self.pLoc][0]][self.comDict[self.pLoc][1]] == 'T':
                print('Target Struck')
                self.yxMap[self.comDict[self.pLoc][0]][self.comDict[self.pLoc][1]] = 'C'
            else:
                self.yxMap[self.comDict[self.pLoc][0]][self.comDict[self.pLoc][1]] = 'V'
        return xed

    def runAll(self):    
        #Converts Zero to str('0')
        self.reformZed('0')
        #Starter YX coord. 'X' Marks the spot
        self.playerLoc(9,3)
        #Target YX coord. 'T' Marks Spot('C' when hit)
        self.targetLoc(2,8)
        #Non-critical. Can return location of any indice, first line printed
        print(self.findVal('9'))
        #Prints map. Kinda duh
        self.printMap()
        #Player and target YX returned
        self.retAll()
        #finds path, saves to list, DOES NOT MOVE CHARACTER
        self.vertexDirect()
        #uses path list to move character
        self.listParser()
        #shows path taken.
        #Legend : X = Start | T = Target | C = Target Complete
        #V is the path taken
        self.printMap()

        
if __name__ == '__main__':
    crom = mapPather()
    crom.runAll()
