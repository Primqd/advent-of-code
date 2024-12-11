from typing import *
from collections import Counter, defaultdict

STONES : Dict[str, int] = Counter([i for i in open(r"2024/Day 11/d11.txt").read().split(" ")]) # input

for blink in range(75):
    new_stones : Dict[str, int] = defaultdict(int) # to replace STONES
    for stone, freq in STONES.items():
        # simulate breaking for val, then multiply by frequency
        if stone == "0": # shift to 1
            new_stones["1"] += freq
        elif len(stone) % 2 == 0: # break into two
            a, b = str(int(stone[:len(stone) // 2])), str(int(stone[len(stone) // 2:]))
            new_stones[a] += freq
            new_stones[b] += freq
        else: # no rules
            new_stones[str(int(stone) * 2024)] += freq
    STONES = new_stones

print(sum([int(i) for i in STONES.values()]))

# this one took me forever ;-; only solved this one cause i looked at solution to similar problem i remember seeing
# problem and solution i stole from: https://leetcode.com/problems/total-characters-in-string-after-transformations-i/solutions/5972920/string-evolution-the-transformation-challenge-easy-cpp-hashing-solution/

# dp? bases of unique values which is better
# idk runtime but i'd guess like O(unique elements * 75)