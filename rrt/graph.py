from collections import defaultdict

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