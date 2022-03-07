from random import random
from math import dist, sqrt, pi, cos, sin, trunc

import sys
sys.path.append("/")
from approaches import *

def dist(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def setup(radius):
    def rand():
        #https://stackoverflow.com/questions/8595973/truncate-to-three-decimals-in-python
        def truncate(number, digits) -> float:
            stepper = 10.0 ** digits
            return trunc(stepper * number) / stepper
        theta = random() * 2 * pi
        r = sqrt(random()) * radius
        return truncate(cos(theta) * r, 3), truncate(sin(theta) * r, 3)
    
    applicants = [rand(), rand(),rand(), rand()]
    treasure = rand()
    return applicants, treasure

applicants, treasure = setup(20)

import matplotlib.pyplot as plt
island = plt.Circle((0,0), 20, color = 'yellow')
fig, ax = plt.subplots()
ax.set_ylim(-22,22)
ax.set_xlim(-22,22)
ax.axis("equal")
ax.add_patch(island)
data1 = approach1(applicants,treasure)

ax.scatter(*zip(*applicants), label='Applicants', color='black')

(mx1,my1),(mx2,my2) = data1["midpoints"]
#Draw arrows
a,b,c,d = [applicants[i] for i in [(0,1,2,3),(0,2,1,3),(0,3,1,2)][data1["idx"]]]

ax.arrow(*a, mx1 - a[0], my1 - a[1],color = 'green',head_width=0.5, length_includes_head=True)
ax.arrow(*b, mx1 - b[0], my1 - b[1],color = 'green',head_width=0.5, length_includes_head=True)
ax.arrow(*c, mx2 - c[0], my2 - c[1],color = 'green',head_width=0.5, length_includes_head=True)
ax.arrow(*d, mx2 - d[0], my2 - d[1],color = 'green',head_width=0.5, length_includes_head=True)

if dist(mx1,my1,*treasure)+dist(*b,mx1,my1) < dist(mx2,my2,*treasure)+dist(*c,mx2,my2):
    ax.arrow(mx1,my1,treasure[0]-mx1,treasure[1]-my1,color = 'green',head_width=0.5, length_includes_head=True)
else:
    ax.arrow(mx2,my2,treasure[0]-mx2,treasure[1]-my2,color = 'green',head_width=0.5, length_includes_head=True)

ax.plot(*treasure, 'ro', label='Treasure')
ax.legend()

plt.show()