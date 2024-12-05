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
    # tests if the case is valid; same as s9.py

    do : bool = True # is this case valid?
    in_test : Set[int] = set(case) # all integers in case
    poss_parents : Set[int] = set(case) # all integers in the case that may be parents
    for idx in range(-1, -len(case) - 1, -1):
        if PREF[case[idx]].intersection(in_test).issubset(poss_parents): # parents in test are already in poss parents: continue
            poss_parents.remove(case[idx]) # no longer possible as parent
        else: # parents in test that ARENT in poss_parents: not valid
            do = False
            break
    
    if do: continue # vlaid case; nothign to change

    sorted_case : List[int] = [] # mock sorting of elements
    while len(sorted_case) < len(case) // 2 + 1: # can get midpoint
        curr : Set[int] = set(sorted_case) # current elements
        for ele in case: # next line "ele not in curr" relies on no duplicate elements in test case... :( 
            if ele not in curr and PREF[ele].intersection(in_test).issubset(curr): # parents already exist in the sorted case. this element should always exist, otherwise no possible one can be formed.
                sorted_case.append(ele)
                break
    
    res += sorted_case[-1]

print(res)
"""
uhhhh
ChatGPT says its like O(n^2) for valid and O(n^3) for invalid cases
:shrug:
"""