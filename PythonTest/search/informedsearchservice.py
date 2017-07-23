import numpy as np
#we model something totally different than from "searchservice.py"
#we are not navigating through a map tyring to find the detination
class Node():
    def __init__(self, name : str, probability):
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
    #letter_matrix is two dimentional matrix
    #x represents letter position, y represents the cadidate letters with prob
    def __init__(self, beam_size,  letter_matrix):       
        self.beam_size = beam_size
        #sort each column's prob from high to low
        self.letter_matrix = letter_matrix
        self.pathes = []
        for column_data in self.letter_matrix:
             column_data = column_data.sort(key=lambda x: x.probability, reverse=True)
        


    def appendNodeAndGetNewPath(self, old_path, new_node):
        new_path = Path()
        new_path.nodes = list(old_path.nodes)
        new_path.nodes.append(new_node)
        return new_path
   
    def run(self):
        #init path with nodes from first column
        
        for node in self.letter_matrix[0][:self.beam_size]:
            path = Path()
            path.nodes.append(node)
            path.total_prob = node.probability
            self.pathes.append(path)

        for column_letter_candidates in self.letter_matrix[1:-1]:
            new_pathes = []
            
            for path in self.pathes:
                for node in column_letter_candidates:
                    new_path = self.appendNodeAndGetNewPath(path, node)
                    new_path.total_prob = path.total_prob + node.probability
                    new_pathes.append(new_path)
            #only keep the beam-size amount of pathes
            new_pathes.sort(key=lambda x: x.total_prob, reverse=True)
            self.pathes = new_pathes[:self.beam_size]
           

import unittest
class BeamSearchTest(unittest.TestCase):
    def test_beam(self):
        dic = ["cat","dog","ape"]
        #column1
        n_x1_y1 = Node("c", 0.6)
        n_x1_y2 = Node("d", 0.8)
        n_x1_y3 = Node("a", 0.7)
        #column2
        n_x2_y1 = Node("a", 0.9)
        n_x2_y2 = Node("o", 0.6)
        n_x2_y3 = Node("p", 0.7)
        #column3
        n_x3_y1 = Node("t", 0.9)
        n_x3_y2 = Node("g", 0.8)
        n_x3_y3 = Node("e", 0.7)
        
        letter_matrix = [[n_x1_y1,n_x1_y2,n_x1_y3],[n_x2_y1,n_x2_y2,n_x2_y3],[n_x3_y1,n_x3_y2,n_x3_y3]]
        service = BeamSearch(2,letter_matrix)
        service.run()
        print(service.pathes)
        #path_str = service.complete_path.getPathStr()
        #self.assertTrue(path_str == "s->a->d->g")
