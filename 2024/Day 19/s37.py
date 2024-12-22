from typing import *

# same as https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

SUBSTRS : List[str] = [] # list of susbstrs
TARGETS : List[str] = [] # list of target words
res : int = 0

with open(r'2024/Day 19/d19.txt', 'r') as file:
    SUBSTRS = file.readline().split(", ")
    SUBSTRS[-1] = SUBSTRS[-1][:-1] # get rid of newline

    k = file.readline()

    while k: # read targets...
        k = file.readline()[:-1]
        if k and k[-1] == '\n': k = k[:-1] # gets rid of newline
        TARGETS.append(k)
    
    TARGETS.pop() # gets rid of empty string...

for target in TARGETS:
    print(target)
    curr = "" # current substring
    dp : List[bool] = [True] + [False] * len(target)
    for i in range(len(target)):
        curr += target[i] # add current str
        for suffix in SUBSTRS:
            if curr.endswith(suffix): # good
                dp[i + 1] = dp[i + 1 - len(suffix)]
                if dp[i + 1]: break # valid
    if dp[-1]: res += 1

print(res)