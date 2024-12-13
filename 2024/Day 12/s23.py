from typing import *

FIELD : List[str] = open(r"2024/Day 12/d12.txt").read().split("\n")
VISIT : List[List[int]] = [[0 for __ in range(len(FIELD[0]))] for _ in range(len(FIELD))] # visited matrix, 0 = not visited, 1 = visit
VALID : Callable[[int, int], bool] = lambda i, j: 0 <= i < len(FIELD) and 0 <= j < len(FIELD[0])# util function; on grid

res : int = 0 # result

def flood(i : int, j : int) -> Tuple[int, int]:
    """
    Floodfills from point (i, j).
    Returns (area, perimeter) from floodfilling at that point.
    """
    if (not VALID(i, j)) or (VISIT[i][j] == 1): return (0, 0) # already visited or not on grid
    VISIT[i][j] = 1 # we visited the square
    area, perim = 1, 4

    if VALID(i + 1, j) and FIELD[i][j] == FIELD[i + 1][j]: # right
        perim -= 1
        if VISIT[i + 1][j] == 0: # not visited yet
            da, dp = flood(i + 1, j)
            area += da
            perim += dp
    
    if VALID(i - 1, j) and FIELD[i][j] == FIELD[i - 1][j]: # left
        perim -= 1
        if VISIT[i - 1][j] == 0: # not visited yet
            da, dp = flood(i - 1, j)
            area += da
            perim += dp

    if VALID(i, j + 1) and FIELD[i][j] == FIELD[i][j + 1]: # down
        perim -= 1
        if VISIT[i][j + 1] == 0: # not visited yet
            da, dp = flood(i, j + 1)
            area += da
            perim += dp

    if VALID(i, j - 1) and FIELD[i][j] == FIELD[i][j - 1]: # up
        perim -= 1
        if VISIT[i][j - 1] == 0: # not visited yet
            da, dp = flood(i, j - 1)
            area += da
            perim += dp
    
    return area, perim

for x in range(len(FIELD)):
    for y in range(len(FIELD[0])):
        if VISIT[x][y] == 0:
            res += (lambda x, y : x * y)(*flood(x, y))

print(res)
    
