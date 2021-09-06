#Unit length Vector
#One Vector Point 'faces' Another Vector point even when moving different direction.
# Pv = Player Vecotor x,y : Tv = Target Vector x,y
#P->T : Player watching Target
#P->T = 1 : or P ^ T
#Vector = Target - Player (V = Destination - Origin)



class VecWatch():
    def __init__(self, Px, Py, Tx, Ty):
        self.Px = Px
        self.Py = Py
        self.Tx = Tx
        self.Ty = Ty

    def calcHat(self):
        self.Vexer = (self.Px + self.Tx)/1 + (self.Py + self.Ty) / 1
        print(self.Px + self.Tx)
        print(self.Py + self.Ty)
        print(self.Vexer)






if __name__ == '__main__':
    print('mnr')
    qobo = VecWatch(3,4, 1,2)
    qobo.calcHat()
