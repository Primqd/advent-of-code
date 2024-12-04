from re import findall, split # RegEx python
from typing import * # useful type hints

# in order to use my funny code from p1, will be doing some very jank steps

def process_sec(section : str) -> int:
    """
    Processes all mult() commands in a section.
    ASSUMES section is good to go (see code).
    uses funny code from s5.py :)
    """
    res : int = 0
    mults : List[str] = findall("mul\(\d+,\d+\)", section) # finds all mult calls
    for mult in mults:
        res += (lambda x : x[0] * x[1])([int(k) for k in findall("\d+", mult)])
    return res

IN : str = open(r'2024\Day 3\d3.txt', 'r').read() # opens file and immediately reads as string

split_dont : List[str] = split("don't\(\)", IN) # splits string based on "don't()" calls

# retrieves the "activate mult" sections by considering the first section ("do" by default) and only looking at sections w/ "do()" afterward
split_do : List[str] = [split_dont[0]]

for mult_dont_sec in split_dont:
    mult_do : List[str] = split("do\(\)", mult_dont_sec)
    if len(mult_do) > 1: # s.t. sections without do() active are ignored
        split_do.extend(mult_do[1:]) # just incase multiple do()'s before don't()

print(sum([process_sec(sec) for sec in split_do])) # calls process_sec on all verified sections and sums it up :)