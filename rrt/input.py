from rrt.node import node
from rrt.droneRRT import drone

start = [ [100,100,0], [0,100,100]]
goal = [ [0, 0, 100], [100,0,0]]
obstacleCoordinates = []
droneSize = 10
droneAcceleration_X = 4
droneAcceleration_Y = 4
droneAcceleration_Z = 4
droneMass = 1
annimation = True
colors = ['r', 'g', 'y', 'k', 'b', 'm']



startNodes = []
goalNodes = []
for i in range(len(start)):
    startNodes.append(node(x = start[i][0], y = start[i][1], z = start[i][2]))
    goalNodes.append(node(x = goal[i][0], y = goal[i][1], z = goal[i][2]))
obstacles = []
for i in range(len(obstacleCoordinates)):
    obstacles.append([node(x = obstacleCoordinates[i][0], y = obstacleCoordinates[i][1], z = obstacleCoordinates[i][2]), obstacleCoordinates[i][3]])


drones = []

for i in range(len(start)):
    drones.append(drone(start = startNodes[i], finish = goalNodes[i],
                        accelerationX=droneAcceleration_X, accelerationY=droneAcceleration_Y, accelerationZ=droneAcceleration_Z,
                        size = droneSize, mass = droneMass, obstacles = obstacles, annimation = annimation, ID = i))

for i in range(len(drones)):
    for j in range(len(drones)):
        if i == j : pass
        else: drones[i].recipents.append(drones[j])