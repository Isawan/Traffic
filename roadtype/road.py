import numpy as np

EMPTY = 0

class Road:
    def __init__(self,length,loc=[],vel=[]):
        self.cars = np.zeros(length,dtype=np.int32)
        self.vel = np.zeros(length,dtype=np.int32)
        self.length = length
        
        self.insert_cars(loc,vel)

    def insert_cars(self,pos,vel):
        raise NotImplementedError()

    def insert_car(self,pos,vel):
        if self.cars[pos] != EMPTY:
            raise Exception()
        self.cars[pos] = 1
        self.vel[pos] = vel
    
    @property
    def car_location(self):
        return np.nonzero(self.cars)[0]

    @property
    def car_vel(self):
        return self.vel[self.car_location]

    @property
    def distance(self):
        carloc = self.car_location
        # Handle empty road
        if len(carloc) == 0:
            raise Exception('Empty Road')

        enddist = self._handle_end_dist(carloc)
        return np.append(np.diff(carloc),enddist)
    
    def __str__(self):
        a = ['\0']*self.length
        for i,c in enumerate(self.cars):
            if c:
                a[i] = str(self.vel[i])
            else:
                a[i] = '.'
        return ''.join(a)


