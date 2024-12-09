from typing import *
from collections import deque # am abusing deque for something not a queue? yes :)

DM : str = open(r"2024/Day 9/d9.txt").readline() # input + get rid of last line
db_str : Deque[int] = deque([i // 2 for i in range(0, len(DM), 2) for _ in range(int(DM[i]))]) # result of simply considering data blocks, ignoring empty spaces
curr_idx : int = 0 # current simulated index
curr_dm_idx : int = 0 # current index in DM
res : int = 0

while db_str:
    if curr_dm_idx % 2 == 0: # data block
        for _ in range(int(DM[curr_dm_idx])): # iterates over all elements in datablock
            if db_str:
                res += db_str.popleft() * curr_idx
                curr_idx += 1
    else: # free memory
        for _ in range(int(DM[curr_dm_idx])):
            if db_str:
                res += db_str.pop() * curr_idx
                curr_idx += 1
    curr_dm_idx += 1

print(res)

"""
boy i don't even know what the time complexity for this one is
probably pure two-pointer method but fuck that shit bro
"""