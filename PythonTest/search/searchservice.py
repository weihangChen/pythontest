import numpy as np
#https://www.youtube.com/watch?v=j1H3jAAGlEA
#http://bradley.bradley.edu/~chris/searches.html
#the simulated path can be viewed from path.jpg
#stack push, pop, last in, first out, add to top
#https://www.cs.cmu.edu/~adamchik/15-121/lectures/Stacks%20and%20Queues/Stacks%20and%20Queues.html
#https://en.wikibooks.org/wiki/Algorithm_Implementation/Viterbi_algorithm
#todo, it is ok to keep the evaluate first path function, just need to
#introduct a leveling function, so before going down to next level, all the
#pathes are evaulated and only keep the n-best for beam search
#core classes
class Node():
    def __init__(self, name : str):
        self.name = name
        #list of destination
        self.destinations = []

class EvaulationResult():
    def __init__(self):
        self.success = False
        self.new_pathes = []
        self.complete_path = []

class BeenTo():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __eq__(self, obj):
        t1 = self.start == obj.start and self.end == obj.end
        t2 = self.start == obj.end and self.end == obj.start
        return t1 or t2


class Path():
    def __init__(self):
        #collection for Node
        self.nodes = []
        self.total_prob = -1
       
    def getPathStr(self):
        names = [x.name for x in self.nodes]
        str = "->".join(names)
        return str
        


class Search():
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
        #it starts from ns
        self.start = self.ns
        #it ends at ng
        self.end = self.ng
        #the core path object contains all the path decision
        initial_path = Path()
        initial_path.nodes.append(self.ns)
        self.pathes = [initial_path]
        #used to avoid going bouncing between two same nodes
        self.dead_pathes = []
        #the final result pathes being generated
        self.complete_path = []
    
    def appendNodeAndGetNewPath(self, old_path, new_node):
        new_path = Path()
        new_path.nodes = list(old_path.nodes)
        new_path.nodes.append(new_node)
        return new_path

    def evaluatePath(self, path: Path):
        result = EvaulationResult()
        last_node_in_path = path.nodes[-1]
        destinations = last_node_in_path.destinations
        #if destination found
        
        hit = any(x for x in destinations if x.name == self.end.name)
        if hit == True:
            result.success = True
            result.complete_path = self.appendNodeAndGetNewPath(path, self.end)
           
        else:
            result.success = False
            for x in last_node_in_path.destinations:
                beento = BeenTo(last_node_in_path.name, x.name)
                #if nodeA goes to nodeB, then nodeB should not go back to nodeA
                is_dead_path = False
                for dead_path in self.dead_pathes:
                    if dead_path == beento:
                        is_dead_path = True
                        break

                if is_dead_path == False:
                    self.dead_pathes.append(beento)
                    new_path = self.appendNodeAndGetNewPath(path, x)
                    result.new_pathes.append(new_path)
        return result

    def run(self):
        #when queue is empty, not found
        if len(self.pathes) == 0:
            return None

        first_path = self.pathes[0]
        result = self.evaluatePath(first_path)
        if result.success:
            self.complete_path = result.complete_path
            return None

        #detination not reached, continue the resursion
        self.enqueue(result.new_pathes)
        self.run()
          

    def enqueue(self, new_pathes):
        pass
    #remove the first path
    def dequeue(self):
        self.pathes.pop(0)

#difference between depthfirst and breadthfirst is that
class DepthFirstSearch(Search):
    def __init__(self): 
        super(DepthFirstSearch, self).__init__()

    #add to start of the queue
    def enqueue(self, new_pathes):
        self.dequeue()
        for index, x in enumerate(new_pathes):
            self.pathes.insert(index, x)


class BreadthFirstSearch(Search):
    def __init__(self): 
        super(BreadthFirstSearch, self).__init__()

    #add to end of the queue
    def enqueue(self, new_pathes):
        self.dequeue()
        for x in new_pathes:
            self.pathes.append(x)



import unittest
class DepthFirstSearchTest(unittest.TestCase):
    def test_depthfirst(self):
        service = DepthFirstSearch()
        service.run()
        path_str = service.complete_path.getPathStr()
        self.assertTrue(path_str == "s->a->d->g")
