import helper
import re
from collections import defaultdict, deque

# Parse input as graph
# Store graph as a dictionary of lists (adjacency list)
graph = defaultdict(list)
inp = helper.read_day(12).strip().splitlines()
for line in inp:
    ids = list(map(int, re.findall("\w+", line)))
    for i in ids[1:]:
        graph[ids[0]].append(i)

# Part 1
# How many programs are in the group with program ID 0?
# Use Breadth-First Search, starting with node 0.

def bfs(g, s):
    """Breadth-first search for graph g, starting at node s.
    Returns a set of traversed nodes."""
    q = deque([s])
    discovered = set([s])
    while len(q) > 0:
        curr = q.popleft()
        for neigh in g[curr]:    
            if neigh not in discovered:
                discovered.add(neigh)
                q.append(neigh)
    return discovered

nodes = bfs(graph, 0)
print("Part 1:", len(nodes))

# Part 2
# Find number of connected components of the graph using BFS.

discovered = set()
connected = 0
for node in graph.keys():
    if node not in discovered:
        discovered = discovered.union(bfs(graph, node))
        connected += 1
print("Part 2:", connected)
