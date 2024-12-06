from typing import *

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

"""
-1 : passed
 0 : empty
 1 : obstacle
 2 : guard (gets replaced)
"""

cx, cy = -1, -1 # position of guard
curr_dir : int = 0 # which way am i facing? with DIR
res : int = 0 # return value

# finds the location of the guard, will always exist for input
for i in range(ROW_LEN):
    for j in range(COL_LEN):
        if MATRIX[i][j] == 2:
            cx, cy = i, j
            MATRIX[cx][cy] = 0 # we can treat it as empty now that we have guard info
            break
    if cx != -1 and cy != -1: break # guard found

while VALID(cx, cy):
    MATRIX[cx][cy] = -1 # current is passed
    dx, dy = DIR[curr_dir] # which way will i move?
    while VALID(cx + dx, cy + dy) and MATRIX[cx + dx][cy + dy] != 1: # continue travelling in a direction while it's still valid
        cx += dx
        cy += dy
        MATRIX[cx][cy] = -1 # passed value
    if not VALID(cx + dx, cy + dy): break # escape condition
    while MATRIX[cx + dx][cy + dy] == 1: # continue turning right until you can move- valid path should ALWAYS exist
        curr_dir = (curr_dir + 1) % 4 # turns right
        dx, dy = DIR[curr_dir]
    
# now simulated: count passed 
for row in MATRIX:
    for ele in row:
        if ele == -1:
            res += 1

print(res)

"""
O(nm): brute force sim
"""