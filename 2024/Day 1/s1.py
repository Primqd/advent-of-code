from typing import *

L1 : List[int] = [] # left list
L2 : List[int] = [] # right list

# gets input & reads to L1 and L2
with open(r'2024\Day 1\d1.txt', 'r') as file:
    for line in file:
        ele_1, ele_2 = (int(i) for i in line.split())
        L1.append(ele_1)
        L2.append(ele_2)

# sorts lists
L1.sort()
L2.sort()

# brute force adds diff
print(sum([abs(L1[i] - L2[i]) for i in range(len(L1))]))
