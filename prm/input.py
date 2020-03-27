
from collections import defaultdict




obstacleCoordinates = []
step = 1
droneSize = 3
start = [[0,0,0], [100,0,0]]
goal = [[100, 100 , 100], [0, 100, 100]]
GNODE = [None for i in range(len(start))]
SNODE = [None for i in range(len(start))]
path = [None for i in range(len(start))]
colors = ['r','b','g','k','y', 'm']
class node:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.nearest = []
        self.distanceToNearest = []
for i in range(len(GNODE)):
    GNODE[i] = node(goal[i][0], goal[i][1], goal[i][2])
    SNODE[i] = node(start[i][0], start[i][1], start[i][2])



