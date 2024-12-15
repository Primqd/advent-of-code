from __future__ import annotations
from typing import *

MATRIX : List[List[Object]]= [] # holds grid data: Objects, or Robot
OPERATIONS : str = "" # holds operatons
DISP : Dict[str, Tuple[int, int]] = { # displacement for given op
    "^" : (0, -1), # upward
    "v" : (0, 1), # downward
    "<" : (-1, 0), # left
    ">" : (1, 0) # right
}

cx, cy = -1, -1 # current location of robot

class Object:
    """
    Stores information about everything in the set!
    """
    def __init__(self, c_type : str, x : int, y : int): # what should operations be considered as?
        self.c_type : str = c_type
        self.x = x # current x pos
        self.y = y # current y pos
    
    def move(self, dx : int, dy : int) -> bool:
        # print(self.c_type, (self.x, self.y), (dx, dy))
        # Attempts moving +dx or +dy. Returns if operation went through.
        
        if self.c_type == "#": return False # walls cant move, silly!
        elif self.c_type == ".": return True # air doesn't move + movement on it will always go through
        else: # box OR robot
            if MATRIX[self.y + dy][self.x + dx].move(dx, dy): # i can move there!
                self.x += dx
                self.y += dy
                MATRIX[self.y][self.x] = self # move yerself over there
                if self.c_type == "@": # if you're a robot, need to "clean up" residual object: otherwise, should be cleaned up by other
                    MATRIX[self.y - dy][self.x - dx] = Object(".", self.x - dx, self.y - dy) # empty space from where robot moves
                return True
            else: # can't move there
                return False
        

with open(r"2024/Day 15/d15.txt") as file:
    s = False # start reading operaitons?
    LINES : List[str] = file.readlines()
    for idx in range(len(LINES)):
        if s:
            OPERATIONS += LINES[idx][:-1] # new line char
        else:
            if LINES[idx] == "\n": # empty line: start reading operations
                s = True
                continue
            curr = [] # current row
            for col in range(len(LINES[idx])):
                if LINES[idx][col] != "@": # not robot
                    if LINES[idx][col] == "\n": continue
                    curr.append(Object(LINES[idx][col], col, idx))
                else: # robot
                    cx, cy = col, idx
                    curr.append(Object("@", cx, cy))
            MATRIX.append(curr)



for op in OPERATIONS: # process movements
    if MATRIX[cy][cx].move(*DISP[op]): # moved
        dx, dy = DISP[op]
        cx += dx
        cy += dy
        # for line in MATRIX:
        #     print([i.c_type for i in line])

res : int = 0 # result

for row in range(len(MATRIX)):
    for col in range(len(MATRIX[0])):
        if MATRIX[row][col].c_type == "O": # box
            res += row * 100 + col

print(res)