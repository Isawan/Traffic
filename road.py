import numpy as np
import matplotlib.pyplot as plt
import time
from roadtype.circle import CircularRoad as Road
import measurements

L = 100
vmax = 5
# Used to populate the road
prob_car = 0.2
# Probability of slowing down
prob_slow = 0.1

def populate_road(road,spacing,vel):
    for i in range(0,road.length,spacing):
        road.insert_car(i,vel)

def step(road,vmax=5,measurements=[]):
    try:
        dist = road.distance#distance(road)
    except Exception as e:
        #print(e)
        assert(str(e)=='Empty Road')
        newroad = road.__class__(road.length)
        return newroad

    carloc = road.car_location
    carvel = road.car_vel
    
    # Acceleration
    p = np.where(np.logical_and(carvel<vmax, dist>carvel))
    carvel[p] += 1

    # Deceleration
    carvel = np.where(carvel<dist,carvel,dist-1)

    # Random
    p = np.where(carvel>0)[0]
    r = np.random.binomial(1,prob_slow,len(p))
    carvel[p] -= r
    
    # Car motion
    carloc += carvel

    # Take measurements
    for m in measurements:
        m.measure(road,carloc,carvel)

    # Put car into road
    newroad = road.__class__(road.length)

    newroad.insert_cars(carloc,carvel) 
    return newroad

if __name__ == '__main__':
    road = Road(L)
    populate_road(road)
    roadlist = []
    while True:
        print(road)
        road = step(road)
