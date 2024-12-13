# disjoint set union implementation

# it's 1:34 am, fuck you whoever made this problem

from typing import *

class DSU:
    """
    DSU between integers
    """
    def __init__(self):
        self.parent : Dict[int, int] = {}
    
    def add(self, x : int) -> None:
        # adds x as a disjoint set (or if already in the set, does nothing)

        if x in self: return # already in the set
        self.parent[x] = x # x is a parent of itself

        # unique functionality for this problem: automatically union with adajacent values
        if x - 1 in self: self._union(x, x-1)
        if x + 1 in self: self._union(x, x+1)

    def _find(self, x : int) -> int:
        # Returns x's arbitrary parent
        if self.parent[x] == x: return x # x is its own parent
        self.parent[x] = self._find(self.parent[x]) # recursively find and set arbirary parent to x's parent
        return self.parent[x]
    
    def _union(self, x : int, y : int) -> bool:
        # merges x and y sets; returns whether changed status
        x_root : int = self._find(x) # finds x's arbitrary parent
        y_root : int = self._find(y) # find y's arbirary parent
        if x_root == y_root: return False # already part of same set

        # arbitrarily makes y arbitrary parent the child of x arbitrary parent
        self.parent[y_root] = x_root
    
    def __len__(self) -> int:
        # returns number of disjoint sets within DSU
        for key in self.parent.keys(): self._find(key) # makes each one a star tree to make computations nicer
        arb_parents : Set[int] = set() # stores the arbitrary parents within the set
        for key in self.parent.keys(): arb_parents.add(self._find(key))
        return len(arb_parents)
    
    def __contains__(self, x : int) -> bool:
        # returns whether x is in the DSU
        return x in self.parent
