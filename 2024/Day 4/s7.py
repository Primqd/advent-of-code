from typing import *

MATRIX : List[str] = open(r"2024/Day 4/d4.txt", "r").readlines() # word search as matrix
ROW_LEN : int = len(MATRIX[0]) - 1 # because apparently white space characters are included in each line :shrug:
COL_LEN : int = len(MATRIX) # to match up with ROW_LEN :)

def valid(i : int, j : int) -> int:
    """
    Checks the word search at point (i, j) for any instances of 'XMAS', considering (i, j) as the 'X'.
    Assumes (i, j) is a real point in the matrix.

    Returns the number of XMAS instances found from that point.
    """
    ret : int = 0

    if MATRIX[i][j] != 'X': return 0 # exit case
    for x, y in [(-1, -1),(-1, 0),(-1, 1),(0, 1),(1, 1),(1, 0),(1, -1),(0, -1)]: # iterates over all directions relative to (i, j)
        if not(0 <= i + 3 * x < ROW_LEN and 0 <= j + 3 * y < COL_LEN): continue # checks if "XMAS" can fit in that direction
        elif MATRIX[i][j] + MATRIX[i + x][j + y] + MATRIX[i + 2 * x][j + 2 * y] + MATRIX[i + 3 * x][j + 3 * y] == "XMAS": ret += 1 # valid "XMAS"
        # else: print([(i + k * x, j + k * y) for k in range(4)])
    
    return ret

res : int = 0 # result

for i in range(ROW_LEN):
    for j in range(COL_LEN):
        res += valid(i, j)

print(res)

"""
O(nm) time; 8x seach on every point
"""