from typing import *
from collections import defaultdict

# reads lines from input makes it into a matrix
MAT : List[List[str]] = [[c for c in line] for line in open(r"2024/Day 8/d8.txt").read().split('\n')]
NODES : DefaultDict[str, List[Tuple[int, int]]] = defaultdict(list) # NODES[i] returns a list of tuples representing the points where antennas of frequency i are
ANTI : Set[Tuple[int, int]] = set() # all points that antinodes exist at
res : int = 0 # result
# identifies all nodes
for i in range(len(MAT)):
    for j in range(len(MAT[0])):
        # all coordinates
        if MAT[i][j] != '.': # not empty
            NODES[MAT[i][j]].append((i, j))

for f_nodes in NODES.values(): # iterate over all same-frequency nodes in NODES
    # iterate over all pairs of nodes in f_nodes
    for a in range(len(f_nodes) - 1): # first node
        for b in range(a + 1, len(f_nodes)): # second node
            dx, dy = (lambda i, j : (i[0] - j[0], i[1] - j[1]))(f_nodes[a], f_nodes[b]) # differences between coordinates 
            x1, y1 = (lambda i : (i[0] + dx, i[1] + dy))(f_nodes[a]) # first antinode
            x2, y2 = (lambda i : (i[0] - dx, i[1] - dy))(f_nodes[b]) # second antinode
            if not((x1, y1) in ANTI) and 0 <= x1 < len(MAT) and 0 <= y1 < len(MAT[0]): # valid antinode point that hasn't been considered
                ANTI.add((x1, y1))
                res += 1
            if not((x2, y2) in ANTI) and 0 <= x2 < len(MAT) and 0 <= y2 < len(MAT[0]): # see above
                ANTI.add((x2, y2))
                res += 1

print(res)

"""
O(T(n_T)^2)
T = types of frequencies
n_T = number of nodes of said frequency

brute forces through every single pair and simulates their antinode
"""
            