import time
import math


#Theory. topSpeed = 140 units. acceleration = 11 units. Time = 12.72
# Reached via topSpeed/Acceleration = totalTime
#Newtonian theories a = (topSpeed/currentSpeed)/deltaT


#Requirements Current Speed, Top speed, Time, Acceleration
class accelTest:
    def __init__(self, currentSpeed = 0.0, topSpeed = 85.0, acceleration = 5.0):
        #minimum requirements...other than timeDelta
        self.currentSpeed = currentSpeed
        self.topSpeed = topSpeed
        self.acceleration = acceleration

        #deltaT calculation array
        self.deltaArr = []


    def deltaT(self, clicks = 30):
        tempAccel = 0
        for xed in range(clicks):
            self.logVal = time.perf_counter()
            self.deltaArr.append(self.logVal)
            self.deltaTotal = self.deltaArr[xed] - self.deltaArr[xed-1]
            print(self.deltaTotal)
            try:
                tempAccel = (self.topSpeed-self.currentSpeed) / self.deltaTotal
            except:
                print('blah')
            print('------------------', tempAccel)
            self.currentSpeed = self.currentSpeed + tempAccel
            print('*************************', self.currentSpeed)


#velocity += acceleration * dt
#position += 0.5 * velociy * dt
    def dummyTest(self):
        acceleration = 9.8
        velocity = 0
        position = 20
        dt = .02
        self.tempL = []
        self.tempR = []
        for xem in range(95):
            velocity += acceleration * dt
            position += 0.5 * velocity * dt
            self.tempL.append(velocity)
            self.tempR.append(position)
        
if __name__ == '__main__':
    corgi = accelTest()
    corgi.deltaT()
    corgi.dummyTest()
    print(corgi.tempL)
