import cmath
#Vecor Length
#Pythagorean theory, calculating a hypotenuse between points.
#a** = b** + c** : Using a as hypotenuse


class vecDistance():
    def __init__(self, Px, Py, Ox, Oy):
        #P = Player : O = Opponent
        self.Px = Px
        self.Py = Py
        self.Ox = Ox
        self.Oy = Oy

    def calcDist(self):
        distBetw = cmath.sqrt(self.Px * self.Ox + self.Py * self.Oy)
        print('Distance betwen : ', distBetw)
        
        


if __name__ == '__main__':
    #         Px, Py, Ox, Oy
    qobo = vecDistance(4,3, 9,8)
    qobo.calcDist()
    qobo = vecDistance(0, -1, 1,1)
    qobo.calcDist()
