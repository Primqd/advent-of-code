from typing import *

SUBSTRS : List[str] = [] # list of susbstrs
TARGETS : List[str] = [] # list of target words
res : int = 0

with open(r'2024/Day 19/d19.txt', 'r') as file:
    SUBSTRS = file.readline().split(", ")
    SUBSTRS[-1] = SUBSTRS[-1][:-1] # get rid of newline

    k = file.readline()

    while k: # read targets...
        k = file.readline()
        if k and k[-1] == '\n': k = k[:-1] # gets rid of newline
        TARGETS.append(k)
    
    TARGETS.pop() # gets rid of empty string...

for target in TARGETS:
    print(target)
    curr = "" # current substring
    dp : List[int] = [1] + [0] * len(target)
    for i in range(len(target)):
        curr += target[i] # add current str
        for suffix in SUBSTRS:
            if curr.endswith(suffix): # good
                dp[i + 1] += dp[i + 1 - len(suffix)]
    res += dp[-1]

print(res)