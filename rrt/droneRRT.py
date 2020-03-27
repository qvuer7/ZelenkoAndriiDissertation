import math
from rrt.node import node

class drone:
    def __init__(self, start, finish,
                 accelerationX, accelerationY, accelerationZ,
                 size, mass, obstacles,
                 annimation, ID):
        self.start = start
        self.finish = finish
        self.accelerationX = accelerationX
        self.accelerationY = accelerationY
        self.accelerationZ = accelerationZ
        self.size = size
        self.mass = mass
        self.obstacles = obstacles
        self.position = start
        self.nodeList = [start]
        self.path = None
        self.RRTfinished = False
        self.annimation = annimation
        self.recipents = []
        self.intercaptors = []
        self.intercaptionPoint = []
        self.ID = ID

    def draw_line(self, start, end):
        line = [start]
        i = 0
        while node_distance(line[i], end) >= self.size:
            line.append(make_step(nodef=line[i], nodet=end, stepx=self.size, stepy=self.size, stepz=self.size))
            i = i + 1
        self.line = line


def node_distance(node1, node2):
    dx = node1.x - node2.x
    dy = node1.y - node2.y
    dz = node1.z - node2.z

    distance = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
    return distance

def make_step(nodef, nodet, stepx, stepy, stepz):

    dx = nodet.x - nodef.x
    dy = nodet.y - nodef.y
    dz = nodet.z - nodef.z

    r = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
    xx = dx * (stepx / r)
    yy = dy * (stepy / r)
    zz = dz * (stepz / r)
    newnode = node(nodef.x + xx, nodef.y + yy, nodef.z + zz)

    return newnode