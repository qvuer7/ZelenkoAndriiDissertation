from prm.functions import *
from prm.algorithmPRM import algorithmPRM
from prm.functions import magnitudes_to_magnitude_angles_calulation


class dronePRM:
    def __init__(self, nodelist, ID, goal, start, graph, obstaclelist, stepx, stepy, stepz,  dronesize, ax):
        self.stepx = stepx
        self.stepy = stepy
        self.stepz = stepz
        self.ax = ax
        self.step = magnitudes_to_magnitude_angles_calulation(accelerationx=stepx, accelerationy=stepy, accelerationz = stepz)[0]
        self.dronesize = dronesize
        self.ID = ID
        self.goal = goal
        self.start = start
        self.graph = graph
        self.recipents = []
        self.obstaclelist = obstaclelist
        self.nodelist = nodelist
        self.lines = None
        self.connect()
        self.path = dijsktra(self.graph, initial=self.start, end=self.goal)
        self.pathLines = []
        self.problemLine = None
        for i in range(len(self.path)):
            if i == len(self.path) - 1:
                pass
            else:
                self.pathLines.append(get_line(node1 = self.path[i], node2 = self.path[i + 1], dronesize=self.dronesize, stepx = self.stepx, stepy = self.stepy, stepz = self.stepz))


    def connect(self):
        startNearest = None
        j = 1
        while startNearest is None:
            startNearestNodes = k_nearest_nodes_for_singlenode(node=self.start, nodelist=self.nodelist, k=j)[0]
            for i in range(len(startNearestNodes)):
                startAv = connect_avaliable(node1 = self.start, node2 = startNearestNodes[i], obstaclelist=self.obstaclelist,step = self.step,safesize = self.dronesize)
                if startAv:
                    startNearest = startNearestNodes[i]
                else:
                    j = j + 1
        goalNearest = None
        j = 1
        while goalNearest is None:
            goalNearestNodes = k_nearest_nodes_for_singlenode(node=self.goal, nodelist=self.nodelist, k=j)[0]
            for i in range(len(goalNearestNodes)):
                goalAv = connect_avaliable(node1=self.goal, node2=goalNearestNodes[i],
                                            obstaclelist=self.obstaclelist, step=self.step, safesize=self.dronesize)
                if goalAv:
                    goalNearest = goalNearestNodes[i]
                else:
                    j = j + 1
        startDistance = node_distance(self.start, startNearest)
        goalDistance = node_distance(self.goal, goalNearest)
        self.graph.add_edge(from_node = self.start, to_node=startNearest, weight=startDistance)
        self.graph.add_edge(from_node = self.goal, to_node = goalNearest, weight = goalDistance)

    def get_path(self):
        algorithmPRM(self)