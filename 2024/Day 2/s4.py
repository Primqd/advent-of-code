from typing import *

REPORTS : List[List[int]] = []

# gets input & reads to REPORTS; each element = 1 report
with open(r'2024\Day 2\d2.txt', 'r') as file:
    for line in file:
        REPORTS.append([int(i) for i in line.split()])

safe : int = 0 # tracks how many safe reports there are

def isSafe(report : List[int]):
    """
    Checks if a report is safe.
    Sorting O(nlgn) => O(n) one pass:
    - check 0 and 1 index for increase and decrease
    - check every subsequent pair (1, 2), (2, 3),... for same direction + allowed abs diff
    """
    curr_safe : bool = True # track whether the current report is safe
    if report == sorted(report) or report == sorted(report, reverse = True): # either increasing or decreasing
        for a, b in zip(range(len(report) - 1), range(1, len(report))): # iterate through every (0, 1), (1, 2), (2,3), etc...
            if abs(report[b] - report[a]) > 3 or abs(report[b] - report[a]) == 0: # too far apart!
                curr_safe = False
                break
        return curr_safe
    else: # not incr or decr
        return False

for r in REPORTS:
    for i in range(len(r)): # simulates removing index i and checking if it's safe I KNOW IT DOESN'T NEED TO BE O(n^2lgn) BUT I'M LAZY :)
        if isSafe(r[:i] + r[i + 1:]):
            safe += 1
            break

print(safe)

"""
Sorting + Brute Force O(n^2lgn) => O(n) three pass
- look at first two elements to determine direction
- check 0 and 1 index for increase and decrease
- check every subsequent pair (1, 2), (2, 3)... for same direction + allowed abs diff
- doesn't satisfy? remove element (damper) and continue
- another unsatisfy? drop report and go to next
Edge case: what if 0 and 1 index is the one to remove?
- brute force removing those ones first :)
- why three pass and not one pass  
"""