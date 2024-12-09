from typing import *

DM : str = open(r"2024/Day 9/d9.txt").readline() # input + get rid of last line
curr_dm : List[List[int]] = [] # sections of dm
for i in range(len(DM)):
    if i % 2 == 0: # data block
        curr_dm.append([i // 2] * int(DM[i]))
    else: # free block
        curr_dm.append([0] * int(DM[i])) # might as well be 0 blocks 

# pre-process greedy moves
for i in range(1, len(curr_dm), 2): # free blocks
    # print(i)
    free_len : int = len(curr_dm[i]) # length of free section
    cfp : int = 0 # current position in free section
    for j in range(len(curr_dm) - 1, i, -1): # dm blocks
        if free_len == 0: break 
        if len(curr_dm[j]) <= free_len:
            if len(curr_dm[j]) == 0 or curr_dm[j][0] == 0: continue # zero set, already free memeory or already considered
            curr_dm[i][cfp : cfp + len(curr_dm[j])] = curr_dm[j]
            curr_dm[j] = [0] * len(curr_dm[j])
            free_len -= len(curr_dm[j])
            cfp += len(curr_dm[j])

flat = [j for i in curr_dm for j in i]
print(sum([a * b for a, b in zip(flat, range(len(flat)))]))

# return result

"""
fuck you, no annotations on what ANY of the last shit means

holy shit this problem genuinely made me want to fucking murder somebody
this problem is SO GODDAMN BULLSHIT.
watch as there's some magical "oh if you actually consider it as a greedy problem you can do it in O(n)" fuck you method
...i mean there probably is some method like that
idk i'm bad, i haven't studied comp programming in forever

it's like 12 and i STILL have phyisics notes to do for my class tomorrow
fuck this

probably pure 2pointer method (vs. ~n^2 reverse serach like i do) but as i said in s17- fuck that
"""