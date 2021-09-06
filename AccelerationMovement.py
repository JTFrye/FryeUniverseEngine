import time



class VecAccel():
    def __init__(self, xVal, yVal, Accel, Velocity, Distance):
        self.xVal = xVal
        self.yVal = yVal
        self.Accel = Accel
        self.Velocity = Velocity
        self.Distance = Distance
        self.deltaArr = []

    def VelObj(self):
        #object is constant velocity
        self.logVal = time.perf_counter()
        self.deltaArr.append(self.logVal)
        for xed in range(25):
            self.logVal = time.perf_counter()
            self.deltaArr.append(self.logVal)
            self.deltaTotal = self.deltaArr[xed] - self.deltaArr[xed-1]
            print(self.deltaTotal)
            newDist = self.Velocity//self.deltaTotal
            print(newDist)

    def AccelObj(self):
        
        for xed in range(25):
            logVal = time.perf_counter()
            self.deltaArr.append(logVal)
            deltaTotal = self.deltaArr[-1] - self.deltaArr[0]
            print(deltaTotal)




if __name__ == '__main__':
    print('mnr')
    qobo = VecAccel(25.0,25.0, 2.0, 1.0, 1.0)
    qobo.VelObj()
    qobo.AccelObj()
