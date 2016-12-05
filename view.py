import numpy as np
import matplotlib.pyplot as plt
import road
import measurements
from roadtype.circle import CircularRoad as ClosedRoad
from roadtype.straight import StraightRoad as OpenRoad

runs = 10000
L = 10000
#np.random.seed(10)

plt.figure()

roadlist = [0]*runs
r0 = ClosedRoad(L)
road.populate_road(r0,10,3)
roadlist[0] = r0

flow = measurements.Flow()
density = measurements.Density()

# Plot for different spacing
for i in range(1,runs):
    print(i)
    roadlist[i] = road.step(roadlist[i-1],vmax=5,
            measurements=[flow,density])
    #roadlist[i-1] = None

# Prepare for plot
#v = np.array([r.vel + 1 for r in roadlist],dtype=np.float)
#c = np.array([r.cars for r in roadlist],dtype=np.float)
#v[np.where(c==0)] = 0 
#plt.figure(1)
#plt.pcolormesh(v,cmap='afmhot')

#plt.figure(2)
d = np.convolve(density.results,np.ones(100)/100,mode='same')
f = np.convolve(flow.results,np.ones(100)/100,mode='same')
plt.scatter(d,f)
plt.show()
