#Used for 'locals()' under IDLE to see all objects
import gc


#The list
masterList = []
masterDict = {}

#Class, two Vals
class dispObj():
    def __init__(self, xVal, yVal):
        self.xVal = xVal
        self.yVal = yVal

    def addVals(self):
        return self.xVal + self.yVal



#tVal{x} variable
for x in range(50):
    #experimental val for calling instance with variable name
    fVar = f'tVal{x}'

    #instance
    tempVal = dispObj(x, x)
    #adds to dict
    masterDict[x] = dispObj(x, x)
    #adds tempVal to list
    masterList.append(tempVal)




if __name__ == '__main__':
    qobo = dispObj(5,4)
    print('------------------------------------------\n' *3)
    #print(masterList)
    #print(masterDict)
    print('in idle lookup masterList or masterDict')
    print('------------------------------------------\n' *3)
#How to access instance in list attributes and methods.
    print(masterList[5].addVals())
    print(masterList[5].xVal)
    print(masterList[5].xVal = 8)
    print(masterList[5].addVals())
