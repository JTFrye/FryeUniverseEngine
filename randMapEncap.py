import random


class mapGen():
    def __init__(self, width = 60, height = 40):
        self.width = width
        self.height = height
        print(width)
        print(height)
        

    def getRandomBlock(self):
        wallPercent = 35
        if random.randint(1,100) < wallPercent:
            return '#'
        else :
            return ' '

    def generateRow(self):
        return ['#'] + [self.getRandomBlock() for xed in range(self.width - 2)] + ['#']


    def levelGen(self):
        edge = ['#'] * self.width
        level = [edge] + [self.generateRow() for xed in range(self.height-2)] + [edge]
        for yed in level:
            print( ''.join(yed))
        
        
if __name__ == '__main__':
    print('mnr')
    qrog = mapGen()
    qrog.getRandomBlock()
    qrog.generateRow()
    qrog.levelGen()
    

ref = '''
wallPercent = 35

def getBlock():
    if random.randint(1,100) < wallPercent:
        return '#'
    else :
        return ' '

edge = ['#'] * width

def generateRow():
    return ['#'] + [getBlock() for xed in range(width-2)] + ['#']

level = [edge] + [generateRow() for xed in range(height-2)] + [edge]

for row in level:
    print( ''.join(row))
'''
derp = '''
tileMap = [
    ['#','#','#','#']
    ['#',' ',' ','#']
    ['#',' ',' ','#']
    ['#','#','#','#']
]'''

