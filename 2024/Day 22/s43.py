from typing import *

CODES : List[int] = [int(i) for i in open(r"2024/Day 22/d22.txt").read().split('\n')]
MOD : int = 16777216 # mod constant

def sim(n : int) -> int:
    # simulates the 2000th secret number from n
    k = n
    for _ in range(2000):
        k ^= (k << 6) # * 64
        k %= MOD
        k ^= (k >> 5) # // 32
        k %= MOD
        k ^= (k << 11) # * 2048
        k %= MOD
    return k

print(sum([sim(i) for i in CODES])) 