from rrt.droneRRT import drone
from rrt.node import node

start = [[0, 0, 0], [100, 0, 100]]  # add [x,y,z] for each new drone start
goal = [[100, 100, 100], [0, 100, 0]]  # add [x,y,z] for each new drone finish
obstacleCoordinates = []  # add [x,y,z, radius] for each new obstacle coordinate and sizing
droneSize = 10  # set all drones sizing
initialVelocityX = 0  # set initial drone velocity in x
initialVelocityY = 0  # set initial drone velocity in y
initialVelocityZ = 0  # set initial drone velocity in z
maxAccelerationX = 10  # set max drone acceleration in x
maxAccelerationY = 10  # set max drone acceleration in y
maxAccelerationZ = 10  # set max drone acceleration in z
step = 1  # set drone maximum step distance used for PRM(in later version will be fixed)
droneMass = 1  # set drone mass, used for intertia calculations, will be improved in later version
annimation = True  # True to observe path building process, False to observe only path
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
                        initialVelocityX = initialVelocityX, initialVelocityY = initialVelocityY, initialVelocityZ = initialVelocityZ,
                        size = droneSize, mass = droneMass, obstacles = obstacles, annimation = annimation, ID = i,
                        maxAccelerationX = maxAccelerationX, maxAccelerationY = maxAccelerationY, maxAccelerationZ=maxAccelerationZ))


for i in range(len(drones)):
    for j in range(len(drones)):
        if i == j : pass
        else: drones[i].recipents.append(drones[j])

GNODE = [node(0, 0, 0) for i in range(len(start))]
SNODE = [node(0, 0, 0) for i in range(len(start))]
path = [None for i in range(len(start))]
for i in range(len(GNODE)):
    GNODE[i] = node(goal[i][0], goal[i][1], goal[i][2])
    SNODE[i] = node(start[i][0], start[i][1], start[i][2])