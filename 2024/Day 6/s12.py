from typing import *
from collections import defaultdict
from copy import deepcopy

# Reads lines from input and converts to matrix of integers for ease. See blurb below for more.
MATRIX : List[List[int]] = [[{"." : 0, "#" : 1, "^" : 2, "\n" : "will get removed"}[ele] for ele in line][:-1] if line.count("\n") > 0 else [{"." : 0, "#" : 1}[ele] for ele in line] for line in open(r"2024/Day 6/d6.txt", "r").readlines()]
ROW_LEN : int = len(MATRIX) # length of row
COL_LEN : int = len(MATRIX[0]) # length of col
DIR : List[Tuple[int, int]] = [ # encodes direction values
    (-1, 0), # upward
    (0, 1), # right
    (1, 0), # downward
    (0, -1)  # left
]
VALID : Callable[[int, int], bool] = lambda x, y : 0 <= x < ROW_LEN and 0 <= y < COL_LEN # checks whether point is on the matrix, i'm lazy leave me alone
GUARD_IX, GUARD_IY = -1, -1 # init coords of guard

"""
 0 : empty
 1 : obstacle
 2 : guard (gets replaced)
"""

# finds the location of the guard
for i in range(ROW_LEN):
    for j in range(COL_LEN):
        if MATRIX[i][j] == 2:
            GUARD_IX, GUARD_IY = i, j
            MATRIX[GUARD_IX][GUARD_IY] = 0 # we can treat it as empty now that we have guard info
            break
    if GUARD_IX != -1 and GUARD_IY != -1: break # guard found

def loop(mat : List[List[int]]) -> bool:
    """
    Returns whether the guard can't escape the given matrix mat- the matrix is a loop.
    O(nm) runtime.
    """
    cx, cy = GUARD_IX, GUARD_IY # position of guard
    curr_dir : int = 0 # which way am i facing? with DIR
    res : int = 0 # return value
    passed : DefaultDict[Tuple[int, int], Set[int]] = defaultdict(set) # passed[(i, j)] returns set of directions that the guard has been thru when moving past this coord: if it's ever the same, return true
    passed[(cx, cy)].add(curr_dir) # init pos

    while VALID(cx, cy):
        dx, dy = DIR[curr_dir] # which way will i move?
        while VALID(cx + dx, cy + dy) and mat[cx + dx][cy + dy] != 1: # continue travelling in a direction while it's still valid
            cx += dx
            cy += dy
            if curr_dir in passed[(cx, cy)]: return True # in same position again: break condition
            else: passed[(cx, cy)].add(curr_dir) # add current condition to dict
        if not VALID(cx + dx, cy + dy): break # escape condition
        while mat[cx + dx][cy + dy] == 1: # continue turning right until you can move- valid path should ALWAYS exist
            curr_dir = (curr_dir + 1) % 4 # turns right
            dx, dy = DIR[curr_dir]
        
    # escaped: not loop
    return False

res : int = 0

# brute forces adding objects in every coordinate, then uses loop to check if it's possible. slow ik :(
for i in range(ROW_LEN):
    for j in range(COL_LEN):
        print(i, j) # not neccessary, but this program takes a while- O((nm)^2) is no joke ;-;
        if i == GUARD_IX and j == GUARD_IY: continue # edge case
        if MATRIX[i][j] == 0: # empty: can add test obj
            MATRIX[i][j] = 1 # temporarily add object there
            if loop(MATRIX): res += 1
            MATRIX[i][j] = 0 # undo object

print(res)
"""
O((nm)^2): brute force sim :))
"""