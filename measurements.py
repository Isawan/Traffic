import numpy as np

# Check number of cars that pass the end of the road.
class Flow:
    def __init__(self):
        self._table = []

    def measure(self,road,newloc,newvel):
        count = np.count_nonzero(newloc >= road.length)
        self._table.append(count)

    @property
    def results(self):
        return np.array(self._table)

# Doesn't do anything. Use for testing.
class DummyMeasure:
    def __init__(self):
        pass
    def measure(self,road,newloc,newvel):
        pass

# Checks the total density of the road
class Density:
    def __init__(self):
        self._table = []

    def measure(self,road,newloc,newvel):
        endloc = newloc[newloc<30]
        self._table.append(len(endloc)/30)

    @property
    def results(self):
        return np.array(self._table)
        
