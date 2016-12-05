import numpy as np
import roadtype.road as road

vnew = 5

class StraightRoad(road.Road):

    def insert_cars(self,pos,vel):
        for i,p in enumerate(pos):
            if p >= self.length:
                continue
            else:
                self.cars[p] = 1
                self.vel[p] = vel[i]

        # Insert new cars
        if not np.any(self.cars[:3]):
            self.cars[0] = 1
            self.vel[0] = vnew

    #Return very large number
    def _handle_end_dist(self,carloc):
        return 10000
