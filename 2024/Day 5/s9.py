from typing import *
from collections import defaultdict

PREF : DefaultDict[int, Set[int]] = defaultdict(set) # pref[i] gives the elements that must exist before i
TEST : List[List[int]] # list of all the tests to process

rules, cases = (lambda x : (x[:x.index("")], x[x.index("") + 1:]))(open(r"2024/Day 5/d5.txt").read().split('\n')) # reads file, splits based on new line, then seperates it into rules and cases list

for rule in rules:
    before, after = (int(i) for i in rule.split("|")) # reads before and after from rule
    PREF[after].add(before) # self-explaniatory

TEST = [[int(c) for c in k.split(',')] for k in cases] # reads cases to TEST

res : int = 0 # return val

for case in TEST:
    do : bool = True # should we consider this case?
    in_test : Set[int] = set(case) # all integers in case
    poss_parents : Set[int] = set(case) # all integers in the case that may be parents
    for idx in range(-1, -len(case) - 1, -1):
        if PREF[case[idx]].intersection(in_test).issubset(poss_parents): # parents in test are already in poss parents: continue
            poss_parents.remove(case[idx]) # no longer possible as parent
        else: # parents in test that ARENT in poss_parents: break
            do = False
            break
    
    res += case[len(case) // 2] if do else 0

print(res)

"""
idk how set runtimes work
ChatGPT says its like O(n^2) per case but idk
"""