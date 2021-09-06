#Generates tilemaps.



class mapper():
    def __init__(self, xWidth, yHeight):
        self.xWidth = xWidth
        self.yHeight = yHeight
        self.mapArr = []

    def makeMap(self):
        totalSize = self.xWidth * self.yHeight
        for xed in range(totalSize):
            self.mapArr.append(0)

    def mapSize(self):
        self.totalInd = len(self.mapArr)
        print(len(self.mapArr))


    def mapShape(self):
        #Tests for consistency.
        #self.mapArr.insert(4,1)
        #self.mapArr.insert(54,1)
        
        for xed in range(self.xWidth):
            qwikVal = self.xWidth * xed
            print(self.mapArr[qwikVal:qwikVal+self.xWidth:])

    def mapTBEncloser(self):
        for xed in range(self.xWidth):
            self.mapArr.pop(xed)
            self.mapArr.insert(xed, 1)
            self.mapArr.pop(self.totalInd-self.xWidth+xed)
            self.mapArr.insert(self.totalInd-self.xWidth+xed, 1)

    def mapSideEncloserStep(self):
        self.sideList = []
        for yed in range(self.yHeight):
            sideVal = self.xWidth * yed
            self.sideList.append(sideVal)
            #self.sideList.append(sideVal - 1)

    def mapEncloseSides(self):
        for yed in range(self.yHeight):
            self.sideList[yed]
            self.mapArr.pop(self.sideList[yed])
            self.mapArr.insert(self.sideList[yed], 1)
            self.mapArr.pop(self.sideList[yed]-1)
            self.mapArr.insert(self.sideList[yed]-1, 1)
        
#####
    def createColumn(self, cVal):
        columnList = []
        self.cVal = cVal
        for zed in range(self.xWidth):
            columnList.append(self.cVal * xWidth)
        print(columnList)
        for zed in range(self.totalInd):
            None
                
                
                
            

            
if __name__ == '__main__':
    qobo = mapper(12,12)
    qobo.makeMap()
    qobo.mapSize()
    qobo.mapShape()
    print('------------------break')
    qobo.mapTBEncloser()
    qobo.mapShape()
    qobo.mapSideEncloserStep()
    qobo.mapShape()
    print(qobo.sideList)
    qobo.mapEncloseSides()
    print('========break')
    qobo.mapShape()
