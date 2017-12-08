"""Advent of Code 2017 Day 7: Recursive Circus""" 

import helper
import re
from collections import defaultdict

class TowerGraph:
    def __init__(self):
        self._graph = defaultdict(dict)
    def add_children(self, parent, children):
        if "children" not in self._graph[parent]:
            self._graph[parent]["children"] = []
        for child in children:
            self._graph[parent]["children"].append(child)
    def add_node(self, node, weight):
        self._graph[node]["weight"] = int(weight)
    def find_root(self, curr_node):
        """Find root of tree given an arbitrary node."""
        while True:
            up = False
            for node in self._graph.keys():
                if curr_node in self._graph[node]["children"]:
                    curr_node = node
                    up = True
                    break # restart the loop
            if not up:
                break
        return curr_node  # root
    def get_total_weight(self, node):
        """Get the total weight of a node (itself + children)."""
        curr = self._graph[node]
        # Base case: no children, return weight
        if len(curr["children"]) == 0:
            return(curr["weight"])
        else:
            sum_weight = []
            for child in curr["children"]:
                sum_weight.append(self.get_total_weight(child))
            return(sum(sum_weight) + curr["weight"])
    def find_unbalanced(self, node):
        curr = self._graph[node]
        sum_weight = []
        for child in curr["children"]:
            sum_weight.append(self.get_total_weight(child))
        # Children are unbalanced / find index of unbalanced child
        if len(set(sum_weight)) > 1:  
            i = [sum_weight.index(w) for w in list(set(sum_weight)) 
                 if sum_weight.count(w) == 1][0]
            j = [sum_weight.index(w) for w in list(set(sum_weight)) 
                 if sum_weight.count(w) > 1][0]
            wrong_weight = sum_weight[i] - sum_weight[j]
            wrong_node = curr["children"][i]
            return self.find_unbalanced(wrong_node)
        return node


data = helper.read_day(7).splitlines()
tower = TowerGraph()
for row in data:
    # Collect alphanumeric pieces (ignore cruft)
    node, weight, *children = re.findall("\w+", row)
    tower.add_node(node, weight)
    tower.add_children(node, children)
root = tower.find_root(node)

# Check balance
print(tower.find_unbalanced(root))
