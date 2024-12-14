# d14.txt should have extra starting line with width and height
from typing import *
from re import compile
from dsu import DSU

WIDTH, HEIGHT = 0, 0 # stores width and height of grid; will initalize when reading input
DETECT_DIGITS : Pattern = compile("-*\d+") # pattern to detect digits in input

class Robot:
    """
    Utility class to process robot data.
    """
    def __init__(self, x : int, y : int, dx : int, dy : int) -> None:
        # init pos
        self.x = x
        self.y = y

        # velocity
        self.dx = dx
        self.dy = dy
    
    def step(self) -> None:
        """
        Simulates stepping once.
        """
        self.x = (self.x + self.dx) % WIDTH
        self.y = (self.y + self.dy) % HEIGHT
    
    def process(self) -> Tuple[int, int]:
        """
        Simulates stepping 100 times. Returns the final position after stepping 100 times as (x, y).
        """
        for _ in range(100):
            self.step()
        return (self.x, self.y)

ROBOTS : List[Robot] = []

with open(r"2024/Day 14/d14.txt") as file:
    for line in file:
        digits : List[int] = [int(i) for i in DETECT_DIGITS.findall(line)]
        if len(digits) == 2: # width and height
            WIDTH, HEIGHT = digits
        else: # robot
            ROBOTS.append(Robot(*digits)) # creates robot and immediately simulates its movement

curr : int = 0 # current iteration

Q1, Q2, Q3, Q4 = 0, 0, 0, 0 # robot totals

for iter in range(1, 100_001):
    for robot in ROBOTS: robot.step()
    positions : List[Tuple[int]] = [(i.x, i.y) for i in ROBOTS]
    pts : DSU = DSU() # abusing DSU again :)
    for point in positions: pts.add(point)
    
    if max(pts.group_sizes()) >= 50: # PRINTING
        MATRIX : List[List[str]] = [["." for _ in range(WIDTH)] for __ in range(HEIGHT)]
        for x, y in positions:
            MATRIX[y][x] = "*"
        for line in MATRIX: print("".join(line))
        print(f"ITER = {iter}")
        break

# ITER = res value

# le ultimate troll method: checks for connected area >= 50 (guessed would be connected)