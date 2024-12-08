from typing import *
from collections import defaultdict
from math import gcd

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

def rp_fac(a : int, b : int) -> Tuple[int, int]:
    """
    Factorizes a and b until they're relatively prime, and then returns them
    """
    while gcd(a, b) > 1: # still has factor
        a //= gcd(a, b)
        b //= gcd(a, b)
    return (a, b)

for f_nodes in NODES.values(): # iterate over all same-frequency nodes in NODES
    # iterate over all pairs of nodes in f_nodes
    for a in range(len(f_nodes) - 1): # first node
        for b in range(a + 1, len(f_nodes)): # second node
            dx, dy = rp_fac(*(lambda i, j : (i[0] - j[0], i[1] - j[1]))(f_nodes[a], f_nodes[b])) # relatively prime differences between two points

            # first segment of line: ray from first node that doesn't intersect second node
            x, y = f_nodes[a] # first node points
            while 0 <= x < len(MAT) and 0 <= y < len(MAT[0]): # while x and y are still valid
                if (x, y) not in ANTI: # unrecorded antinode
                    ANTI.add((x, y))
                    res += 1
                # travels along line
                x += dx
                y += dy
            
            # second segment of line: ray opposite to first
            x, y = f_nodes[b] # second node points
            while 0 <= x < len(MAT) and 0 <= y < len(MAT[0]): # while x and y are still valid
                if (x, y) not in ANTI: # unrecorded antinode
                    ANTI.add((x, y))
                    res += 1
                # travels along line in opp dir
                x -= dx
                y -= dy

print(res)

"""
uhh idk runtime but it's at least O(T(n_T)^2) and less than O(nm) obviously
T = types of frequencies
n_T = number of nodes of said frequency

brute forces through every single pair and travels along their antinode line :)
"""
            