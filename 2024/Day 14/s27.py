# d14.txt should have extra starting line with width and height
from typing import *
from re import compile

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

positions : List[Tuple[int]] = [] # stores final positions

with open(r"2024/Day 14/d14.txt") as file:
    for line in file:
        digits : List[int] = [int(i) for i in DETECT_DIGITS.findall(line)]
        if len(digits) == 2: # width and height
            WIDTH, HEIGHT = digits
        else: # robot
            positions.append(Robot(*digits).process()) # creates robot and immediately simulates its movement

Q1, Q2, Q3, Q4 = 0, 0, 0, 0 # robot totals
MID_WIDTH, MID_HEIGHT = WIDTH // 2, HEIGHT // 2 # middle of width and middle of height

for x, y in positions:
    if x == MID_WIDTH or y == MID_HEIGHT: continue # in middle: don't count
    if x < MID_WIDTH and y < MID_HEIGHT: Q1 += 1 # (-, -)
    elif x > MID_WIDTH and y < MID_HEIGHT: Q2 += 1 # (+, -)
    elif x > MID_WIDTH and y > MID_HEIGHT: Q3 += 1 # (+. +)
    elif x < MID_WIDTH and y > MID_HEIGHT: Q4 += 1 # (-, +)

print(Q1 * Q2 * Q3 * Q4)