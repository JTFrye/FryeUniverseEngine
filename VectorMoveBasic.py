#This is to outline points and vectors.
#A vector is an orientation/angle and length/magnitude : vec = (orientations, length)
#In games these are represented as x, y
#Position is also represented as x,y
#PlayerNewPosition = Player Old Position + Velocity(aka. vector)
#P = Px + Vx, Yx + Vy


class pointNvector():
    def __init__(self, Px, Py, Vx, Vy):
        #P = player, V = vector
        self.Px = Px
        self.Py = Py
        self.Vx = Vx
        self.Vy = Vy
        print('starting location is X, Y : ', self.Px, ' , ', self.Py)
        
    def updatePlayer(self, Px, Py):
        self.Px = Px
        self.Py = Py

    def updateVec(self, Vx, Vy):
        self.Vx = Vx
        self.Vy = Vy

    def movPlayer(self):
        self.Px = self.Px + self.Vx
        self.Py = self.Py + self.Vy
        print('your new location is X, Y : ', self.Px, ' , ', self.Py)
    
    def printAllVal(self):
        print('All Values = : ', self.Px, ' , ', self.Py, ' , ', self.Vx, ' , ', self.Vy)
    

if __name__ == '__main__':
    #pass in values x,y for player and x,y for vector
    #                   (Px, Py, Vx, Vy)
    qobo = pointNvector(5,7,2,2)
    qobo.movPlayer()
    qobo.movPlayer()
    print('updating vector size')
    qobo.updateVec(9,11)
    qobo.movPlayer()
    qobo.printAllVal()
