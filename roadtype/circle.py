import roadtype.road as road

class CircularRoad(road.Road):
    def insert_cars(self,pos,vel):
        if len(pos) == 0: return
        i = pos % self.length
        self.cars[i] = 1
        self.vel[i] = vel

    
    def _handle_end_dist(self,carloc):
        return carloc[0]+self.length-carloc[-1]
