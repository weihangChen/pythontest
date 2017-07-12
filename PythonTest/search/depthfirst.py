from search import isearch
import numpy as np
#https://www.youtube.com/watch?v=j1H3jAAGlEA
#simulate the beam search from above, the simulated path can be viewed from
#path.jpg


class Node():
    def __init__(self, name : str):
        self.name = name
        #list of destination
        self.destinations = []


class DepthFirst():
    def __init__(self):
        #create nodes, start is ns, destination is ng
        self.ns = Node("s")
        self.na = Node("a")
        self.nb = Node("b")
        self.nc = Node("c")
        self.nd = Node("d")
        self.ne = Node("e")
        self.nf = Node("f")
        self.ng = Node("g")
        #s
        self.ns.destinations.append(self.na)
        self.ns.destinations.append(self.nb)
        #a
        self.na.destinations.append(self.nb)
        self.na.destinations.append(self.nd)
        #b
        self.nb.destinations.append(self.na)
        self.nb.destinations.append(self.nc)
        #c
        self.nc.destinations.append(self.ne)
        #d
        self.nd.destinations.append(self.ng)

        self.queue = [[self.ns]]
        self.foundpath = []

    def run(self):
        #when queue is empty, not found
        if len(self.queue) == 0:
            return None
        #if last item from the queue's first array is "ng" the path is found
        size = len(self.foundpath)
        if self.foundpath[size - 1].name == self.ng.name:
            return self.foundpath
        enqueue()
        run()
          

    def enqueue(self):
        pass

    def dequeue(self):
        pass


import unittest
class DepthFirstTest(unittest.TestCase):
    def test_depthfirst(self):
        service = DepthFirst()
        result = service.run()
        


