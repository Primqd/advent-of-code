from typing import *
from collections import defaultdict, deque

CODES : List[int] = [int(i) for i in open(r"2024/Day 22/d22.txt").read().split('\n')]
MOD : int = 16777216 # mod constant

c = len(CODES)

seq_map : Dict[Tuple[int, int, int, int], int] = defaultdict(int) # seq_map[i] returns the profit from using the sequence i

for i in range(c):
    curr = CODES[i]
    prev = curr # previous day's code
    # print(f"{i} / {c}")
    
    window : Deque[int] = deque() # tracks current window
    passed : Set[Tuple[int, int, int, int]] = set() # tracks whether we've seen the given pattern before
    for _ in range(2000): # simulates secret numbers... 
        curr ^= (curr << 6) # * 64
        curr %= MOD
        curr ^= (curr >> 5) # // 32
        curr %= MOD
        curr ^= (curr << 11) # * 2048
        curr %= MOD
        window.append(curr % 10 - prev % 10) # difference in prices
        if len(window) > 4: window.popleft()
        if len(window) == 4: # can generate seq
            seq = tuple(window)
            if seq not in passed:
                seq_map[seq] += curr % 10 # add current value to sequence
                passed.add(seq) # we've seen this sequence now...
        prev = curr
    
print(max(seq_map.values()))
        

