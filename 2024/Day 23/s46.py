from typing import *
from collections import defaultdict

GRAPH : DefaultDict[str, Set[str]] = defaultdict(set) # graph[i] gives all elements connected to i
COMPS : Set[str] = set() # all computers

for a, b in [i.split('-') for i in open("2024/Day 23/d23.txt").read().split('\n')]: # all edges
    GRAPH[a].add(b)
    GRAPH[b].add(a)
    COMPS.add(a)
    COMPS.add(b)

def connected(already : Set[str], new : str): # checks whether new computer is connected to all computers alreayd in the network
    for comp in already:
        if new not in GRAPH[comp]: return False
    return True

max_ele : Set[str] = set()

for first in COMPS:
    if first in max_ele: continue # already considered
    for second in GRAPH[first]:
        if first == second or first in max_ele: continue # same ele
        curr : Set[str] = {first, second} # current connected computers
        for other in COMPS:
            if other == first or other == second: continue # same as first or second
            elif connected(curr, other): curr.add(other)
        if len(curr) > len(max_ele):
            max_ele = curr

print(",".join(sorted(max_ele)))
