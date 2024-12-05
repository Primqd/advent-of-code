from typing import *

REPORTS : List[List[int]] = []

# gets input & reads to REPORTS; each element = 1 report
with open(r'2024\Day 2\d2.txt', 'r') as file:
    for line in file:
        REPORTS.append([int(i) for i in line.split()])

safe : int = 0 # tracks how many safe reports there are

for report in REPORTS:
    if report == sorted(report) or report == sorted(report, reverse = True): # either increasing or decreasing
        curr_safe : bool = True # track whether the current report is safe
        for a, b in zip(range(len(report) - 1), range(1, len(report))): # iterate through every (0, 1), (1, 2), (2,3), etc...
            if abs(report[b] - report[a]) > 3 or abs(report[b] - report[a]) == 0: # too far apart!
                curr_safe = False
                break
        safe += 1 if curr_safe else 0

print(safe)

"""
Sorting O(nlgn) => O(n) one pass:
- check 0 and 1 index for increase and decrease
- check every subsequent pair (1, 2), (2, 3),... for same direction + allowed abs diff

...but i'm lazy
"""