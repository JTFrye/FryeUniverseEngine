

#This class takes inComing list and stores as a tuple, with a list inside
#Yeah, I dunno. self.inComing[0][X], first index is tuple
class listReceiveNUnpack:
    def __init__(self, *inComing):
        self.derp = 1
        self.herp = 0
        self.inComing = inComing


    def getAllLen(self):
#Prints ALL : len : 1 & 2
        print(len(self.inComing))
        print(len(self.inComing[0]))
#Prints Lists, right most value indicates which one : len : 4 & 3
        print(len(self.inComing[0][0]))
        print(len(self.inComing[0][1]))
#Prints Index inside List : len 6
        print(len(self.inComing[0][0][0]))
#Prints slice of letter in etc.
        print(len(self.inComing[0][0][0][0]))
#Value map. X = 1, [0] = 2, [0][0] = 4, [0][1] = 3, [0][0][0] = 6


#Prints Both lists inside
    def firstListPrint(self):
        for xed in range(len(self.inComing[0])):
            print('Both nested lists : ', self.inComing[0][xed])
        return xed

#Prints dooter list
    def secondListPrint(self):
        for xed in range(len(self.inComing[0][0])):
            print('dooter List : ', self.inComing[0][0][xed])
        return xed

#Prints humdinger list
    def thirdListPrint(self):
        for xed in range(len(self.inComing[0][1])):
            print('humdinger list : ', self.inComing[0][1][xed])
        return xed

    def unpackListLocal(self):
        encapList = []
        for xed in range(len(self.inComing[0][0])):
            encapList.append(self.inComing[0][0][xed])

        print('Encapsulated list : ', encapList)
        
if __name__ == '__main__':
#List to pass in. dooter and humdinger!
    numBlock = (['dooter', 'pookie', 'filet', 'sirloin'], ['humdinger', 'woosh woosh', 'rottasaywah'])
#Instantiate
    qrono = listReceiveNUnpack(numBlock)
#Prints
    qrono.getAllLen()
    qrono.firstListPrint()
    qrono.secondListPrint()
    qrono.thirdListPrint()
#Unpacking Exp
    qrono.unpackListLocal()
    
