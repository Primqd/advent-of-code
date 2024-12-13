from typing import *
from dsu import DSU
from collections import defaultdict

FIELD : List[str] = open(r"2024/Day 12/d12.txt").read().split("\n")
VISIT : List[List[int]] = [[0 for __ in range(len(FIELD[0]))] for _ in range(len(FIELD))] # visited matrix, 0 = not visited, 1 = visit
VALID : Callable[[int, int], bool] = lambda i, j: 0 <= i < len(FIELD) and 0 <= j < len(FIELD[0])# util function; on grid

res : int = 0 # result

def flood(i : int, j : int, edge : Dict[str, List[Tuple[int, int]]]) -> int:
    """
    Floodfills from point (i, j).
    Populates edge dict with edge points.
    edge["xu"] = list of edge points that lay ABOVE a HORIZONTAL line
    edge["xd"] = list of edge points that lay BELOW a HORIZONTAL line
    edge["yr"] = list of edge points that lay TO THE RIGHT of a VERTICAL line
    edge["yl"] = list of edge points that lay TO THE LEFT of a VERTICAL line 
    Returns area from floodfilling at that point.
    """
    if (not VALID(i, j)) or (VISIT[i][j] == 1): return 0 # already visited or not on grid
    VISIT[i][j] = 1 # we visited the square
    area = 1

    # add edge values
    edge["yr"].append((i + 1, j)) # right
    edge["yl"].append((i - 1, j)) # left
    edge["xd"].append((i, j + 1)) # down
    edge["xu"].append((i, j - 1)) # up

    if VALID(i + 1, j) and FIELD[i][j] == FIELD[i + 1][j]: # right
        edge["yr"].pop(edge["yr"].index((i + 1, j))) # removes right from edge
        if VISIT[i + 1][j] == 0: # not visited yet
            da = flood(i + 1, j, edge)
            area += da
            
    
    if VALID(i - 1, j) and FIELD[i][j] == FIELD[i - 1][j]: # left
        edge["yl"].pop(edge["yl"].index((i - 1, j)))
        if VISIT[i - 1][j] == 0: # not visited yet
            da = flood(i - 1, j, edge)
            area += da
            

    if VALID(i, j + 1) and FIELD[i][j] == FIELD[i][j + 1]: # down
        edge["xd"].pop(edge["xd"].index((i, j + 1))) # removes right from edge
        if VISIT[i][j + 1] == 0: # not visited yet
            da = flood(i, j + 1, edge)
            area += da
            

    if VALID(i, j - 1) and FIELD[i][j] == FIELD[i][j - 1]: # up
        edge["xu"].pop(edge["xu"].index((i, j - 1))) # removes right from edge
        if VISIT[i][j - 1] == 0: # not visited yet
            da = flood(i, j - 1, edge)
            area += da
    
    return area

for i in range(len(FIELD)):
    for j in range(len(FIELD[0])):
        if VISIT[i][j] == 0: # undiscovered yet
            goon = {"xu" : [], "xd" : [], "yr" : [], "yl" : []}
            area = flood(i, j, goon)
            sides = 0
            for dir, e in goon.items():
                sus : Dict[int, DSU] = defaultdict(DSU) # sus[i] = dsu for i
                for x, y in e: # edge points
                    if dir[0] == "x": sus[y].add(x) # categorize by seocnd variable
                    elif dir[0] == "y": sus[x].add(y) # categorize by first variable
                sides += sum([len(s) for s in sus.values()]) # add up unique disjoint sets for each side
            res += sides * area

print(res)
    
