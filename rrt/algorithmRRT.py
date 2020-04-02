from  input.input import colors
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, axes3d
from rrt.functions import *
fig = plt.figure()
fig2 = plt.figure()
ax = fig.add_subplot(111, projection='3d')



def rrt(drone, target):

    possibleToConnect = False

    if node_distance(node1 = drone.position, node2 = target) <= drone.size:
        drone.RRTfinished = True
    else: drone.RRTfinished = False
    minRandX = -100
    maxRandX = 100
    minRandY = -100
    maxRandY = 100
    minRandZ = -100
    maxRandZ = 100
    goalSampleRate = 100
    if drone.RRTfinished == True: pass
    else:
        while possibleToConnect == False :
            """
            if drone.ID == 1:
                if drone.position.x < target.x :
                    minRandX = int(drone.position.x - 30 )
                    maxRandX = int(target.x)
                    minRandZ = int(drone.position.z)
                    maxRandZ = int(drone.position.z)
                    minRandY = int(drone.position.y)
                    maxRandY = int(drone.position.y)
                else:
                    maxRandX = int(drone.position.x - 30 )
                    minRandX = int(target.x)
                    minRandZ = int(drone.position.z)
                    maxRandZ = int(drone.position.z)
                    minRandY = int(drone.position.y)
                    maxRandY = int(drone.position.y)
            if drone.ID == 2:
                if drone.position.y < target.y :
                    minRandY = int(drone.position.y -30 )
                    maxRandY = int(target.y)
                    minRandZ = int(drone.position.z)
                    maxRandZ = int(drone.position.z)
                    minRandX = int(drone.position.x)
                    maxRandX = int(drone.position.x)
                else:
                    maxRandY =int(drone.position.y - 30 )
                    minRandY = int(target.y)
                    minRandZ = int(drone.position.z)
                    maxRandZ = int(drone.position.z)
                    minRandX = int(drone.position.x)
                    maxRandX = int(drone.position.x)
            if drone.ID ==3 :
                if drone.position.z < target.z :
                    minRandZ = int(drone.position.z - 30 )
                    maxRandZ = int(target.z)
                    minRandY  = int(drone.position.y)
                    maxRandY =  int(drone.position.y)
                    minRandX =  int(drone.position.x)
                    maxRandX =  int(drone.position.x)
                else:
                    maxRandZ = int(drone.position.z - 30 )
                    minRandZ = int(target.z)
                    minRandY = int(drone.position.y)
                    maxRandY = int(drone.position.y)
                    minRandX = int(drone.position.x)
                    maxRandX = int(drone.position.x)
            """



            randomNode = get_random_node(drone)
            #check_nearest(node1 = randomNode, nodeList=drone.nodeList)

            newnode = make_step(nodef = drone.position, nodet=randomNode, stepx = drone.velocity.x, stepy = drone.velocity.y, stepz = drone.velocity.z)

            drone.velocity = get_velocity(drone)

            drone2 = drone_collision(drone=drone, node1=newnode)[1]

            drone.minRandx = min(drone.start.x, drone.finish.x)
            drone.maxRandx = max(drone.start.x, drone.finish.x)
            drone.minRandy = min(drone.start.y, drone.finish.y)
            drone.maxRandy = max(drone.start.y, drone.finish.y)
            drone.minRandz = min(drone.start.z, drone.finish.z)
            drone.maxRandz = max(drone.start.z, drone.finish.z)



            if node_obstacle_collision(node1 = newnode, obstacles=drone.obstacles) :

                drone.goalSampleRate = 0
                possibleToConnect = False


            elif (drone2 != False) :
                drone.goalSampleRate = 0
                possibleToConnect = False
                collide = collision(drone1 = drone, drone2 = drone2, newnode = newnode)
                collide.exchange()
            else:
                drone.goalSampleRate = 100
                newnode.parent = drone.nodeList[len(drone.nodeList) - 1]

                drone.velocities.append(drone.velocity)
                drone.nodeList.append(newnode)
                drone.position = newnode
                possibleToConnect = True
                set_acceleration(drone, percantageX=5, percantageY = 5, percantageZ = 5)





            if node_distance(drone.position, target) <= drone.size :
                drone.RRTfinished = True
                drone.nodeList.append(target)
                drone.path = generate_final_course(gnode = target, nodelist = drone.nodeList)

            if drone.annimation:
                ax.scatter(newnode.x, newnode.y, newnode.z, color = colors[drone.ID])
                plt.pause(0.001)




