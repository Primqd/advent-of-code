from typing import *
from re import findall

# reads lines from input, finds all integers using RegEx, and casts to int
# res: EQNS[i] represents equation: 0 = final res
EQNS : List[List[int]] = [[int(i) for i in findall("\d+", line)] for line in open(r"2024/Day 7/d7.txt").read().split("\n")]

res : int = 0 # store result

for eqn in EQNS:
    print(eqn) # optional but takes a shit long time, nice to know it's still working
    for i in range(2 ** (len(eqn) - 2)): # iterates over all binary digits from 0 to 2 ** (n - 2): to brute force every comb
        ops : str = bin(i)[2:] # binary representation of i
        ops = "0" * (len(eqn) - 2 - len(ops)) + ops # populates prefix with zeroes
        
        curr : int = eqn[1] # current integer
        for eqn_idx, op in zip(range(2, len(eqn)), ops): # index of next number in eqn and operation
            if op == "0": # addition operator
                curr += eqn[eqn_idx]
            else: # op == "1": multiplication operator
                curr *= eqn[eqn_idx]
        if curr == eqn[0]: # works: add value and break
            res += eqn[0]
            break

print(res)
        
            
        

"""
O(n2^n) per test case due to brute force generating every bin number
I don't *think* there's a better way (test cases line up anyways), might be faster with genetic algorithms but i aint setting allat up
"""