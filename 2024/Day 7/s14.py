from functools import lru_cache
from typing import *
from re import findall

# reads lines from input, finds all integers using RegEx (still cast to int)
# res: EQNS[i] represents equation: idx 0 = final res
EQNS : List[List[int]] = [[int(i) for i in findall("\d+", line)] for line in open(r"2024/Day 7/d7.txt").read().split("\n")]

res : int = 0 # result

@lru_cache(maxsize= None) # automatic dp :)
def pow_3(n : int) -> List[str]:
    """
    Generates every combination of the strings "+", "*", and "|" (concat) of length n: the power set.  
    """
    if n == 1: # return condition
        return ["+", "*", "|"]
    else:
        prev : List[str] = pow_3(n - 1) # last powset
        ret : List[str] = [] # new powset
        ret.extend(["+" + k for k in prev]) # new addition first operator
        ret.extend(["*" + k for k in prev]) # new mult first operator
        ret.extend(["|" + k for k in prev]) # new concat operator
        return ret    

for eqn in EQNS:
    print(eqn) # optional but takes a shit long time, nice to know it's still working
    for ops in pow_3(len(eqn) - 2): # all possible operators
        curr : int = eqn[1] # current integer
        for eqn_idx, op in zip(range(2, len(eqn)), ops): # index of next number in eqn and operaton
            if op == "+":
                curr += eqn[eqn_idx]
            elif op == "*":
                curr *= eqn[eqn_idx]
            elif op == "|": # concat
                curr = int(str(curr) + str(eqn[eqn_idx]))
        if curr == eqn[0]: # works: add value and break
            res += eqn[0]
            break

print(res)

"""
O(n3^n) per test case due to brute force generating every set of ops
I don't *think* there's a better way (test cases line up anyways), might be faster with genetic algorithms but i aint setting allat up
"""