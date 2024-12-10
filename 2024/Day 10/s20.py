from typing import *

MATRIX : List[List[int]] = [[int(i) for i in line] for line in open(r"2024/Day 10/d10.txt", "r").read().split('\n')] # read input as matrix
ROWS :  int = len(MATRIX)
COLS : int = len(MATRIX[0])
VALID : Callable[[int, int], bool] = lambda i, j : (0 <= i < ROWS and 0 <= j < COLS) # util function to check if point is valid
DP : List[List[int]] = [[-1 for __ in range(COLS)] for _ in range(ROWS)] # DP[i][j] returns the number of completable trail paths starting from (i, j): -1 means discovered

def discover(i : int, j : int) -> int:
    """
    From (i, j), returns the number of trail paths (score) starting from (i, j).
    Assumes (i, j) is a valid point.
    DOES NOT CHECK WHETHER THE VALUE IS A TRAILHEAD!
    """
    if MATRIX[i][j] == 9: # trailend
        DP[i][j] = 1 # one trail path possible to reach from here: itself
        return 1
    else:
        res = 0
        if VALID(i - 1, j) and MATRIX[i - 1][j] - MATRIX[i][j] == 1: res += discover(i - 1, j) # up
        if VALID(i, j + 1) and MATRIX[i][j + 1] - MATRIX[i][j] == 1: res += discover(i, j + 1) # right
        if VALID(i + 1, j) and MATRIX[i + 1][j] - MATRIX[i][j] == 1: res += discover(i + 1, j) # down
        if VALID(i, j - 1) and MATRIX[i][j - 1] - MATRIX[i][j] == 1: res += discover(i, j - 1) # left
        DP[i][j] = res
        return res

res : int = 0 # return value

for i in range(ROWS):
    for j in range(COLS):
        if MATRIX[i][j] == 0:
            res += discover(i, j)


print(res)

"""
O(nm) worst case i think
"""