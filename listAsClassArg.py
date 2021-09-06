import math
import random


#Class takes LISTS, TUPLES etc. and passes into posVal
class multiArgs():
    def __init__(self, posVal):
        print('inst')
        self.posVal = posVal

if __name__ == '__main__':
    posVar = [12, 15] #Works as List or Tuple
    qorgi = multiArgs(posVar)
        
