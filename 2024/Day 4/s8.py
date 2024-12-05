from typing import *

MATRIX : List[str] = open(r"2024/Day 4/d4.txt", "r").readlines() # word search as matrix
ROW_LEN : int = len(MATRIX[0]) - 1 # because apparently white space characters are included in each line :shrug:
COL_LEN : int = len(MATRIX) # to match up with ROW_LEN :)

def valid(i : int, j : int) -> bool:
    """
    Checks the word search at point (i, j) for any instances of 'X-MAS', considering (i, j) as the 'A'.
    Assumes (i, j) is a real point in the matrix.

    Returns if the point (i, j) is a "X-MAS point."
    """

    if MATRIX[i][j] != 'A': return False # exit case
    elif i + 1 >= ROW_LEN or j + 1 >= COL_LEN or i - 1 < 0 or j - 1 < 0: return False # X-MAS would extend outside the matrix
    lt, rt, rb, lb = MATRIX[i - 1][j - 1], MATRIX[i - 1][j + 1], MATRIX[i + 1][j + 1], MATRIX[i + 1][j - 1] # left top, right top, right bottom, left bottom
    return (lt == rt == 'M' and rb == lb == 'S') or (rt == rb == 'M' and lt == lb == 'S') or (rb == lb == 'M' and rt == lt == 'S') or (lb == lt == 'M' and rt == rb == 'S') # hard coding every case :(

res : int = 0 # result

for i in range(ROW_LEN):
    for j in range(COL_LEN):
        res += 1 if valid(i, j) else 0

print(res)

"""
O(nm) time
"""