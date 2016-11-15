import numpy as np
import matplotlib.pyplot as plt
import time

L = 100
vmax = 5
# Used to populate the road
prob_car = 0.2
# Probability of slowing down
prob_slow = 0.1

EMPTY = 0

class Road:
    def __init__(self,length):
        self.cars = np.zeros(L,dtype=np.int32)
        self.vel = np.zeros(L,dtype=np.int32)
        self.length = length

    def insert_car(self,pos,vel):
        if self.cars[pos] != EMPTY:
            raise Exception()
        self.cars[pos] = 1
        self.vel[pos] = vel

    def __str__(self):
        np.set_printoptions(linewidth=L*2)
        a = str(self.vel)
        np.set_printoptions()
        return a

def populate_road(road):
    for i,r in enumerate(np.random.binomial(2,prob_car,L)):
        if r != 1: continue
        road.insert_car(i,3)

# Returns an array containing distance to next car
def distance(road):
    carloc = np.nonzero(road.cars)[0]
    enddist = carloc[0]+road.length-carloc[-1]
    #print(carloc[0])
    #print(carloc[-1])
    #print(road.length )
    #print(enddist)
    return np.append(np.diff(carloc),
            enddist)
    

def step(road):
    dist = distance(road)
    carloc = np.nonzero(road.cars)[0]
    carvel = road.vel[carloc]
    
    # Acceleration
    p = np.where(np.logical_and(carvel<vmax, dist>carvel))
    #print('carvel\n',carvel)
    #print('carloc\n',carloc)
    #print('dist\n',dist)
    #print(p)
    carvel[p] += 1

    # Deceleration
    carvel = np.where(carvel<dist,carvel,dist-1)

    # Random
    p = np.where(carvel>0)[0]
    r = np.random.binomial(1,prob_slow,len(p))
    carvel[p] -= r
    

    # Car motion
    carloc += carvel

    # Put car into road
    newroad = Road(road.length)
    newroad.cars[carloc%road.length] = 1
    newroad.vel[carloc%road.length] = carvel
    
    return newroad

if __name__ == '__main__':
    road = Road(L)
    populate_road(road)
    roadlist = []
    while True:
        print(road)
        road = step(road)
