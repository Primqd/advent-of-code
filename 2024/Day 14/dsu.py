# disjoint set union implementation
# this time between points :o

from typing import *
from collections import defaultdict

class DSU:
    """
    DSU between points
    """
    def __init__(self):
        self.parent : Dict[Tuple[int, int], Tuple[int, int]] = {}
    
    def add(self, e : Tuple[int, int]) -> None:
        # adds e as a disjoint set (or if already in the set, does nothing)

        if e in self: return # already in the set
        self.parent[e] = e # e is a parent of itself

        # unique functionality for this problem: automatically union with adajacent points
        x, y = e # coordinates of point
        if (x + 1, y) in self: self._union(e, (x + 1, y))
        if (x - 1, y) in self: self._union(e, (x - 1, y))
        if (x, y + 1) in self: self._union(e, (x, y + 1))
        if (x, y - 1) in self: self._union(e, (x, y - 1))

    def _find(self, x : Tuple[int, int]) -> Tuple[int, int]:
        # Returns x's arbitrary parent
        if self.parent[x] == x: return x # x is its own parent
        self.parent[x] = self._find(self.parent[x]) # recursively find and set arbirary parent to x's parent
        return self.parent[x]
    
    def _union(self, x : Tuple[int, int], y : Tuple[int, int]) -> bool:
        # merges x and y sets; returns whether changed status
        x_root : Tuple[int, int] = self._find(x) # finds x's arbitrary parent
        y_root : Tuple[int, int] = self._find(y) # find y's arbirary parent
        if x_root == y_root: return False # already part of same set

        # arbitrarily makes y arbitrary parent the child of x arbitrary parent
        self.parent[y_root] = x_root
    
    def __len__(self) -> int:
        # returns number of disjoint sets within DSU
        arb_parents : Set[int] = set() # stores the arbitrary parents within the set
        for key in self.parent.keys(): arb_parents.add(self._find(key))
        return len(arb_parents)
    
    def group_sizes(self) -> List[int]:
        # returns a list of the sizes of each disjoint set
        parents : Dict[int, int] = dict() # stores parent and its size
        for key in self.parent.keys(): parents[self._find(key)] = parents.get(self._find(key), 0) + 1
        return list(parents.values())
    
    def __contains__(self, x : Tuple[int, int]) -> bool:
        # returns whether x is in the DSU
        return x in self.parent
