import math
import random
from heapq import nsmallest
import numpy as np
from collections import defaultdict
from math import pi


import  matplotlib.pyplot as plt
class node:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.nearest = []
        self.distanceToNearest = []


class Graph:
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}



    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

    def remove_edge(self, from_node, to_node):
        self.edges[from_node].remove(to_node)
        self.edges[to_node].remove(from_node)

def get_newnode(step, nodef, nodet):
    dx = nodet.x - nodef.x
    dy = nodet.y - nodef.y
    dz = nodet.z - nodef.z
    r = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
    if r != 0:
        xx = dx * (step / r)
        yy = dy * (step / r)
        zz = dz * (step / r)
        newnode = node(nodef.x + xx, nodef.y + yy, nodef.z + zz)

    return newnode


def distance_calculations(x, y, z, xx, yy, zz):
    dx = xx - x
    dy = yy - y
    dz = zz - z
    distance = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
    return distance


def connect_avaliable(node1, node2, obstaclelist, step, safesize):
    a = distance_calculations(x=node1.x, xx=node2.x, y=node1.y, yy=node2.y, z=node1.z, zz=node2.z)
    if node1.x ==node2.x and  node1.y == node2.y and node1.z==node2.z: return False
    while a >= step:
        newnode = get_newnode(step, node1, node2)
        if check_between(newnode, obstaclelist, step, safesize):
            node1 = newnode
            a = distance_calculations(x=node1.x, xx=node2.x, y=node1.y, yy=node2.y, z=node1.z, zz=node2.z)
        else:
            return False
    return True


def check_between(node, obstaclelist, step, safesize):
    if len(obstaclelist) != 0:
        for i in range(len(obstaclelist)):
            dCrit = distance_calculations(x=node.x, y=node.y, z=node.z, xx=obstaclelist[i][0],
                                          yy=obstaclelist[i][1], zz=obstaclelist[i][2])
        if dCrit <= step + safesize:
            return False
    else : return True
    return True


def get_randomlist(iterations, minRand, maxRand, obstaclelist, step, safesize):
    list = []
    i = 0
    while i < iterations:
        x = random.randint(minRand, maxRand)
        y = random.randint(minRand, maxRand)
        z = random.randint(minRand, maxRand)
        newnode = node(x, y, z)
        if check_between(newnode, obstaclelist, step, safesize) == True:
            list.append(newnode)
            i = i + 1


    return list





def k_nearest_nodes(nodelist, k, obstaclelist, step, safesize):


    for i in range(len(nodelist)):
        nodelistSecond = nodelist.copy()
        listToAnalyze = remove_unconnected_points(node = nodelist[i], nodelist = nodelistSecond, obstaclelist=obstaclelist, step = step , safesize = safesize)

        nodelist[i].nearest, nodelist[i].distanceToNearest = k_nearest_nodes_for_singlenode(node = nodelist[i], nodelist = listToAnalyze, k = k)


def k_nearest_nodes_for_singlenode(node, nodelist, k):
    distance = []
    nearestNodesNumber = []
    nearestNodes = []
    for j in range(len(nodelist)):
        distance.append(distance_calculations(x=node.x, y=node.y, z=node.z,
                                              xx=nodelist[j].x, yy=nodelist[j].y, zz=nodelist[j].z))
    kMin = nsmallest(k, distance)

    for l in range(len(kMin)):
        nearestNodesNumber.append(distance.index(kMin[l]))
        nearestNodes.append(nodelist[nearestNodesNumber[l]])
    distance = []
    for l in range(len(kMin)):
        distance.append(distance_calculations(x=node.x, y=node.y, z=node.z,
                                              xx=nearestNodes[l].x, yy=nearestNodes[l].y, zz=nearestNodes[l].z))
    return nearestNodes, distance


def remove_unconnected_points(node, nodelist, obstaclelist, step, safesize):
    checknodelist = nodelist.copy()
    a = len(checknodelist)
    i = 0
    while i < a:
        avaliable = connect_avaliable(node1=node, node2=checknodelist[i], obstaclelist=obstaclelist, step=step,
                                      safesize=safesize)
        if avaliable == False:
            checknodelist.remove(checknodelist[i])
            a = len(checknodelist)

        else:
            i = i + 1

    return checknodelist

def dijsktra(graph, initial, end):

    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {nodee: shortest_paths[nodee] for nodee in shortest_paths if nodee not in visited}
        if not next_destinations:
            return "Route Not Possible"
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path



def sct_obst(obstaclenodelistt, color, ax):
    """
     Plotting obstalces
    """
    obstaclenodelist = obstacle_coordinates(obstaclenodelistt)
    for i in range(len(obstaclenodelist)):
        ax.scatter(obstaclenodelist[i].x, obstaclenodelist[i].y, obstaclenodelist[i].z, color=color)


def obstacle_coordinates(list):
    """
    recieving all obstacles coordinates
    """
    a = 10
    b = 10
    u = np.linspace(0, 2 * np.pi, a)
    v = np.linspace(0, np.pi, b)

    xx = [0 for i in range(len(list))]
    yy = [0 for i in range(len(list))]
    zz = [0 for i in range(len(list))]
    obstaclenodes = []
    for i in range(len(list)):
        xx[i] = list[i][3] * np.outer(np.cos(u), np.sin(v)) + list[i][0]
        yy[i] = list[i][3] * np.outer(np.sin(u), np.sin(v)) + list[i][1]
        zz[i] = list[i][3] * np.outer(np.ones(np.size(u)), np.cos(v)) + list[i][2]
        for ii in range(a):
            for iii in range(b):
                obstaclenodes.append(node(xx[i][ii][iii], yy[i][ii][iii], zz[i][ii][iii]))

    return obstaclenodes


def new_positions_spherical_coordinates(R,n, node):
    nodes = []
    for i in range(n):
        phi = random.uniform(0,2*pi)
        costheta = random.uniform(-1, 1)
        theta = math.acos(costheta)
        r = random.uniform(0,R)
        x = node.x  + r * math.sin(theta) * math.cos(phi)
        y = node.y + r * math.sin(phi)
        z = node.z +  r * math.cos(theta)
        nodes.append(node(x,y,z))
    return nodes

def get_lines(node1, node2, node3, node4, DRONE_SIZE1, DRONE_SIZE2, stepx, stepy, stepz):
    line1 = []
    line2 = []
    while node_distance(node1=node1, node2=node2) > DRONE_SIZE1 :
        node1 = cal_dist_and_angle(nodef=node1, nodet=node2, stepx=stepx, stepy= stepy, stepz = stepz)[0]
        line1.append(node1)
    while node_distance(node1=node3, node2=node4) > DRONE_SIZE2 *5:
        node3 = cal_dist_and_angle(nodef=node3, nodet=node4, stepx=stepx, stepy= stepy, stepz = stepz)[0]
        line2.append(node3)


    return line1, line2


def get_line(node1, node2, dronesize, stepx, stepy, stepz):
    line = [node1]
    while node_distance(node1=node1, node2=node2) > dronesize :

        node1 = cal_dist_and_angle(nodef=node1, nodet=node2, stepx=stepx, stepy= stepy, stepz = stepz)[0]
        line.append(node1)
    line.append(node2)
    return line


def check_line_interceptionPRM(lines, dronesize1, dronesize2):
    for i in range(len(lines[0])):
        for j in range(len(lines[1])):
            if node_distance(node1 = lines[1][j], node2 = lines[0][i]) < dronesize1 + dronesize2 :
                return True
            else: continue
    return False



def two_path_rebuild(path, graph, goals, starts,ax):
    lines= []
    for i in range(len(path[0])):
        for j in range(len(path[1])):
            if i == len(path[0]) - 1:
                pass
            elif j == len(path[1]) - 1:
                return path
            else:
                lines.append(get_line(node1 = path[0][i], node2 = path[0][i + 1], dronesize = 1, stepx = 1, stepy = 1, stepz = 1))
    for k in range(len(lines)):
        for h in range(len(lines[k])):
            ax.scatter(lines[k][h].x,lines[k][h].y, lines[k][h].z, color = 'g')


    return path

def get_drone_line(drone):
    lines = []
    for i in range(len(drone.path)):
        if i == len(drone.path) - 1:
            pass
        else:
            line = get_line(node1 = drone.path[i], node2 = drone.path[i + 1], dronesize=drone.dronesize, stepx = drone.stepx, stepy = drone.stepy, stepz = drone.stepz)
            lines.append(line)
    drone.lines = lines


def check_line_interception(drone):
    for i in range(len(drone.recipents)):
        for j in range(len(drone.pathLines)):
            for o in range(len(drone.pathLines[j])):
                for k in range(len(drone.recipents[i].pathLines)):
                    for t in range(len(drone.recipents[i].pathLines[k])):
                        if node_distance(node1 = drone.pathLines[j][o], node2 = drone.recipents[i].pathLines[k][t]) < drone.dronesize + drone.recipents[i].dronesize :


                            try:
                                drone.graph.remove_edge(from_node=drone.pathLines[j][0], to_node=drone.pathLines[j][-1])
                            except: ValueError
                            drone.path = dijsktra(graph = drone.graph, initial = drone.start, end = drone.goal)

                            return True
                else: continue
    return False


def drone_line(drone):
    line = []
    knode = drone.snode
    line.append(knode)

    while node_distance(node1 = knode, node2 = drone.gnode) > drone.DRONE_SIZE*5:
        knode = cal_dist_and_angle(nodef = knode, nodet = drone.gnode, stepx = drone.stepX, stepy = drone.stepY,
                                   stepz = drone.stepZ)[0]
        line.append(knode)
    drone.line = line

def node_distance(node1, node2):
    r = calculations(xx=node1.x, yy=node1.y, zz=node1.z, x=node2.x, y=node2.y, z=node2.z)
    return r

def calculations(x, y, z, xx, yy, zz):
    dx = xx - x
    dy = yy - y
    dz = zz - z

    distance = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)

    return distance

def cal_dist_and_angle(nodef, nodet, stepx, stepy, stepz):
    """
    Cartesian calculations generates newnode according to step
    """

    dx = nodet.x - nodef.x
    dy = nodet.y - nodef.y
    dz = nodet.z - nodef.z

    r = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
    xx = dx * (stepx / r)
    yy = dy * (stepy / r)
    zz = dz * (stepz / r)
    newnode = node(nodef.x + xx, nodef.y + yy, nodef.z + zz)

    return newnode, r

def magnitudes_to_magnitude_angles_calulation(accelerationx, accelerationy, accelerationz):
    # calculations from magnitudes between points to angles and magnitude
    accelerationMagnitude = points_to_magnitude_step_calculation(x2 = accelerationx, y2 = accelerationy, z2 = accelerationz)[0]
    cosX = accelerationx / accelerationMagnitude
    cosY = accelerationy / accelerationMagnitude
    cosZ = accelerationz / accelerationMagnitude

    return accelerationMagnitude, cosX, cosY, cosZ

def points_to_magnitude_step_calculation(x2,y2,z2,x1 = 0,y1 = 0,z1 = 0):

    #calculations from points to magnitude of vector and distances between points
    magnitude = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    try: stepx = (x2 / (x2 - x1)) * magnitude
    except ZeroDivisionError: stepx = 0
    try : stepy = (y2 / (y2 - y1)) * magnitude
    except ZeroDivisionError: stepy = 0
    try: stepz = (z2 / (z2 - z1)) * magnitude
    except ZeroDivisionError: stepz = 0
    return magnitude, stepx, stepy, stepz