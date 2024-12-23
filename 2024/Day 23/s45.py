from typing import *
from collections import defaultdict

GRAPH : DefaultDict[str, Set[str]] = defaultdict(set) # graph[i] gives all elements connected to i
T_STR : Set[str] = set() # set of computers that start with t
passed : Set[Tuple[str, str, str]] = set() # passed combinations

for a, b in [i.split('-') for i in open("2024/Day 23/d23.txt").read().split('\n')]: # all edges
    GRAPH[a].add(b)
    GRAPH[b].add(a)
    if a[0] == "t": T_STR.add(a)
    if b[0] == "t": T_STR.add(b)

res : int = 0

for t in T_STR: # computer starts with t.
    for second in GRAPH[t]: # second connected
        if second == t: continue # duplicate
        for third in GRAPH[second]: 
            if third == t or third == second: continue # duplicate
            if t in GRAPH[third] and tuple(sorted([t, second, third])) not in passed:
                res += 1
                passed.add(tuple(sorted([t, second, third])))

print(res)