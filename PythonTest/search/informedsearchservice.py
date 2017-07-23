import numpy as np
#we model something totally different than from "searchservice.py"
#we are not navigating through a map tyring to find the detination
class Node():
    def __init__(self, name : str, probability : int):
        self.name = name
        self.probability = probability

class Path():
    def __init__(self):
        #collection for Node
        self.nodes = []
        self.total_prob = -1
       
    def getPathStr(self):
        names = [x.name for x in self.nodes]
        str = "->".join(names)
        return str
     
    def getCumulativeProb(self):
        cumulative_prob = sum(x.probability for x in self.nodes)
        return cumulative_prob  
    
#beam search, evaluate top-n nodes as each time level expands
#ex.  [sa],[sb], as it expands, the full list is [sab],[sad],[sba],[sbc]
#cumulative pro is compared among these 4, and only keep top-n (beam size)
#[sab],[sad], rest are removed, the logic here is totally differen than
#the one from super class, we will expand
class BeamSearch():
    def __init__(self, beam_size,  process_data):       
        self.beam_size = beam_size
        self.process_data = process_data


    def appendNodeAndGetNewPath(self, old_path, new_node):
        new_path = Path()
        new_path.nodes = list(old_path.nodes)
        new_path.nodes.append(new_node)
        return new_path
   
    def run(self):
        for data in self.process_data:
            
            #sort the data and take top-n
            data = data.sort(key=lambda x: x.probability, reverse=True)
            data = data[:beam_size]
            
            for path in self.pathes:
                for x in data:
                    new_path = self.appendNodeAndGetNewPath(path, x)
                    new_pathes.append(new_path)
                #only keep the beam-size amount of pathes
                new_pathes.sort(key=lambda x: x.total_prob, reverse=True)
                new_pathes = new_pathes[:beam_size]
           
            self.pathes = new_pathes

import unittest
class BeamSearchTest(unittest.TestCase):
    def test_beam(self):
        data = []
        service = BeamSearch(2,data)
        service.run()
        #path_str = service.complete_path.getPathStr()
        #self.assertTrue(path_str == "s->a->d->g")
