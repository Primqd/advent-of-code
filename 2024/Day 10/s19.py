from typing import *
from collections import defaultdict

MATRIX : List[List[int]] = [[int(i) for i in line] for line in open(r"2024/Day 10/d10.txt", "r").read().split('\n')] # read input as matrix
ROWS :  int = len(MATRIX)
COLS : int = len(MATRIX[0])
VALID : Callable[[int, int], bool] = lambda i, j : (0 <= i < ROWS and 0 <= j < COLS) # util function to check if point is valid
PASSED : Dict[Tuple[int, int], Set[Tuple[int, int]]] = defaultdict(set) # PASSED[(i, j)] returns all trail heads that have passed through (i, j)

def dfs(i : int, j : int, oi : int, oj : int) -> int:
    """
    From (i, j), returns the number of trail paths (score) starting from (oi, oj)
    Assumes (i, j) is a valid point, and that (oi, oj) is the trailhead..
    DOES NOT CHECK WHETHER THE VALUE IS A TRAILHEAD!
    """
    if MATRIX[i][j] == 9: # trailend
        if (oi, oj) not in PASSED[(i, j)]: # hasn't been considered by this trail head yet
            PASSED[(i, j)].add((oi, oj)) # adds to visited
            return 1
        else: return 0
    else:
        res = 0
        if VALID(i - 1, j) and MATRIX[i - 1][j] - MATRIX[i][j] == 1: res += dfs(i - 1, j, oi, oj) # up
        if VALID(i, j + 1) and MATRIX[i][j + 1] - MATRIX[i][j] == 1: res += dfs(i, j + 1, oi, oj) # right
        if VALID(i + 1, j) and MATRIX[i + 1][j] - MATRIX[i][j] == 1: res += dfs(i + 1, j, oi, oj) # down
        if VALID(i, j - 1) and MATRIX[i][j - 1] - MATRIX[i][j] == 1: res += dfs(i, j - 1, oi, oj) # left
        return res

res : int = 0 # return value

for i in range(ROWS):
    for j in range(COLS):
        if MATRIX[i][j] == 0:
            res += dfs(i, j, i, j)

print(res)

"""
O(nm) worst case i think
"""