from typing import *
from re import compile # nice detection

LIN_COEFF : Pattern = compile("\d+") # finds all digits in line: for digit detection
FILE : List[str] = open(r"2024/Day 13/d13.txt", "r").read().split("\n")
SYSTEMS : List[List[List[int]]] = [] # SYSTEMS[i] represents the ith system: 1st ele = coeffs for butt1, 2nd = coeffs for butt2, 3rd = sols for system

def isInteger(a : float, epsilon : float = 0.01):
    """
    Returns whether a is approximately an integer with epsilon error.
    """
    return abs(a - round(a)) < epsilon

def solve(A : List[int], B : List[int], S : List[int]) -> List[float]:
    """
    Solves the linear system represented by A, B, and S.
    x1 * a + x2 * b = xs
    y1 * a + y2 * b = ys
    Solves for a and b.


    Let res represent the returned value.
    - res[0] == -1 : no solution
    - res[0] == 0 : solved system, res[1] = a and res[2] = b
    - res[0] == 1 : infinite solutions, equations are multiples of each other. res[1] == c s.t. Ac = S, res[2] == C s.t. BC = S
    """
    x1, y1 = A # first eqn coeff
    x2, y2 = B # second equation coeff
    xs, ys = S # solutions

    if (x1 / y1 == x2 / y2 == xs / ys): # is equation linear multiple of itself?
        if xs / x1 == ys / y1: # S is part of the solutions of the system
            return [1, xs / x1, xs / x2]
        else: # S is not part of the solutions of the system
            return [-1]
    else: # not linear multiple of itself
        c = x2 / y2
        a = (xs - c * ys)/(x1 - c * y1)
        b = (ys - y1 * a)/y2
        return [0, a, b]

ret : int = 0 # return value

for i in range(0, len(FILE), 4):
    A : List[int] = [int(i) for i in LIN_COEFF.findall(FILE[i])] # coeffs for button A
    B : List[int] = [int(i) for i in LIN_COEFF.findall(FILE[i + 1])] # coeffs for button B
    S : List[int] = [int(i) for i in LIN_COEFF.findall(FILE[i + 2])] # coeffs for solutions

    sol : List[int] = solve(A, B, S) # solved? linear system
    if sol[0] == -1: continue # no solution
    elif sol[0] == 0: # 1 solution
        if isInteger(sol[1]) and isInteger(sol[2]) and sol[1] <= 100 and sol[2] <= 100: # solution points are integers (real button presses) and under 100 presses per button
            print(A, B, S)
            print(sol)
            ret += round(sol[1]) * 3 + round(sol[2]) # add needed tokens: a is weighted 3x vs. b
    else: # infinite solutions, which apparently we don't need to consider LOL
        ...

print(ret)

