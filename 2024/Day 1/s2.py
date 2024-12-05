from typing import *
from collections import Counter

L1 : List[int] = [] # left list
L2 : List[int] = [] # right list

# gets input & reads to L1 and L2
with open(r'2024\Day 1\d1.txt', 'r') as file:
    for line in file:
        ele_1, ele_2 = (int(i) for i in line.split())
        L1.append(ele_1)
        L2.append(ele_2)

# makes L2 into frequency map
freq : Counter[int, int] = Counter(L2)

# brute force adds diff
print(sum([sum([L1[i] * freq[L1[i]]]) if L1[i] in freq else 0 for i in range(len(L1))]))
